<!-- image -->

## CompactLogix 5370 Controllers

1769-L16ER-BB1B, 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B, 1769-L19ER-BB1BK, 1769-L24ER-QB1B, 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B, 1769-L30ER, 1769-L30ER-NSE,

1769-L30ERK, 1769-L30ERM, 1769-L30ERMK, 1769-L33ERMO,

1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK,

1769-L36ERM, 1769-L36ERMO, 1769-L37ERM, 1769-L37ERMK,

1769-L37ERMO, 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMO

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

|                               | Preface                                                                                                                                  |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                               | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9     |
|                               | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                         |
|                               | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9       |
|                               | Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 |
|                               | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11      |
|                               | Chapter 1                                                                                                                                |
| CompactLogix 5370 Controllers | CompactLogix 5370 Control System Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14                               |
| Overview                      | Controller Functionality . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   15   |
|                               | Support for Integrated Motion over an EtherNet/IP Network . . . . . . . . . . . . . . . . . 16                                           |
|                               | Electronic Keying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17   |
|                               | More Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17           |
|                               | Example System Configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                |
|                               | EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18               |
|                               | DeviceNet Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20             |
|                               | Chapter 2                                                                                                                                |
| Install the CompactLogix 5370 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23    |
| L1 Controller                 | CompactLogix 5370 L1 Controller Parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                           |
|                               | Install the Secure Digital Card. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26          |
|                               | Install the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28  |
|                               | Mount the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28            |
|                               | Ground the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30             |
|                               | Install the Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30          |
|                               | Install the Removable Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31                          |
|                               | Connect Power to the Controller (Series B and C). . . . . . . . . . . . . . . . . . . . . . . . . . . 32                                 |
|                               | Connect to the Controller Via a USB Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                    |
|                               | Connect the Controller to an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37                            |
|                               | Connecting to Different EtherNet/IP Network Topologies. . . . . . . . . . . . . . . . . . . . 37                                         |
|                               | Chapter 3                                                                                                                                |
| Install the CompactLogix 5370 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41    |
| L2 Controller                 | CompactLogix 5370 L2 Controller Parts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42                            |
|                               | Install the Secure Digital Card. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43          |
|                               | Install the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45  |
|                               | Mount the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45            |
|                               | Ground the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49             |
|                               | Install the Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49          |
|                               | Remove and Replace the Removable Terminal Block. . . . . . . . . . . . . . . . . . . . . . . . 51                                        |
|                               | Wire the Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51               |
|                               | Wire Size and Terminal Screw Torque . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                           |
|                               | Connect Power to the Control System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                           |
|                               | Connect to the Controller Via a USB Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                    |
|                               | Connect the Controller to an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                            |

|                               | Connecting to Different EtherNet/IP Network Topologies. . . . . . . . . . . . . . . . . . . . 56                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                               | Chapter 4                                                                                                                               |
| Install the CompactLogix 5370 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59   |
| L3 Controller                 | CompactLogix 5370 L3 Controller Parts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60                           |
|                               | Install the Secure Digital Card. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61         |
|                               | Install the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63 |
|                               | Assemble the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63              |
|                               | Remove and Replace the Removable Terminal Block. . . . . . . . . . . . . . . . . . . . . . . . 65                                       |
|                               | Wire the Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65              |
|                               | Wire Size and Terminal Screw Torque . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                          |
|                               | Mount the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66           |
|                               | Ground the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69            |
|                               | Connect Power to the Control System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70                          |
|                               | Connect to the Controller Via a USB Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                   |
|                               | Connect the Controller to an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                           |
|                               | Connecting to Different EtherNet/IP Network Topologies. . . . . . . . . . . . . . . . . . . . 72                                        |
|                               | Chapter 5                                                                                                                               |
| Complete Software Tasks       | Set the IP Address of a Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74            |
| Required at CompactLogix 5370 | Use the BOOTP Server to Set the IP Address of the Controller . . . . . . . . . . . . . . . . 75                                         |
| Controller Installation       | Use the DHCP Server to Set the IP Address of the Controller . . . . . . . . . . . . . . . . 80                                          |
|                               | Use RSLinx Classic Software to Set the Controller IP Address . . . . . . . . . . . . . . . . 81                                         |
|                               | Use the Logix Designer Application to Set the IP Address of the Controller . . . . . 82                                                 |
|                               | Use the SD Card to Set the IP Address of the Controller . . . . . . . . . . . . . . . . . . . . . 85                                    |
|                               | Change the IP Address of a Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                |
|                               | Change the Network IP Address with RSLinx Classic Software. . . . . . . . . . . . . . . . 87                                            |
|                               | Change the Network IP Address with Logix Designer Application . . . . . . . . . . . . . 88                                              |
|                               | Change the Network IP Address with an SD Card . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                                  |
|                               | Load the Controller Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90           |
|                               | Use the ControlFLASH Software to Load Firmware. . . . . . . . . . . . . . . . . . . . . . . . . . 90                                    |
|                               | Use AutoFlash to Load Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                       |
|                               | Use the Secure Digital Card to Load Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                               |
|                               | Select the Operating Mode of the Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                    |

## Chapter 6

| Communicate Over Networks   | EtherNet/IP Network Communication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                     |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Available Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100             |
|                             | EtherNet/IP Network Functionality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101                         |
|                             | Nodes on an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                          |
|                             | EtherNet/IP Network Topologies. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104                        |
|                             | Socket Interface with CompactLogix 5370 Controllers . . . . . . . . . . . . . . . . . . . . . 108                                        |
|                             | Quality of Service (QoS) and I/O Module Connections. . . . . . . . . . . . . . . . . . . . . . . 109                                     |
|                             | EtherNet/IP Network Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                          |
|                             | DeviceNet Network Communication. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                   |
|                             | Available Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111           |
|                             | Compact I/O 1769-SDN DeviceNet Scanner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112                                 |
|                             | Power Supply Distance Rating. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113                      |
|                             | Current Capacity in CompactLogix 5370 L3 Control Systems . . . . . . . . . . . . . . . . 116                                             |
|                             | Chapter 7                                                                                                                                |
| Use I/O Modules with        | Select I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117     |
| CompactLogix 5370           | Connect Field Power to I/O Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117                         |
| L1 Controllers              | Embedded I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                  |
|                             | Local Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127                  |
|                             | Distributed I/O Modules over an EtherNet/IP Network. . . . . . . . . . . . . . . . . . . . . . 130                                       |
|                             | Validate I/O Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131    |
|                             | Set the Number of Local Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                                  |
|                             | Empty Slots and Removal and Insertion Under Power Situations. . . . . . . . . . . . . 131                                                |
|                             | Estimate Requested Packet Interval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132                           |
|                             | Module Faults Related to RPI Estimates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133                           |
|                             | Calculate System Power Consumption. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                              |
|                             | Physical Placement of I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                         |
|                             | Use the Event Task. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135      |
|                             | Configure I/O. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138 |
|                             | Common Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139                            |
|                             | I/O Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139           |
|                             | Configure Distributed I/O Modules on an EtherNet/IP Network . . . . . . . . . . . . . . . . . . 140                                      |
|                             | Monitor I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143      |
|                             | Bus Off Detection and Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144                       |
|                             | Chapter 8                                                                                                                                |
| Use I/O Modules with        | Select I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145     |
| CompactLogix 5370           | Embedded I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                  |
|                             | Determine Embedded Module Update Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158                            |
| L2 Controllers              | Channel Update Times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158                 |
|                             | Embedded Analog I/O Modules Data Arrays. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                         |
|                             | Input Array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163      |
|                             | Output Array. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164        |
|                             | Configuration Array. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164             |
|                             | Local Expansion Modules - Optional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172                         |
|                             | Distributed I/O Modules over an EtherNet/IP Network. . . . . . . . . . . . . . . . . . . . . . 173                                       |

|                      | Validate I/O Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175          |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Estimate Requested Packet Interval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175                                 |
|                      | Module Fault Related to RPI Estimates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176                                 |
|                      | System Power Availability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176                        |
|                      | Power Supply Distance Rating. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177                            |
|                      | Configure Local I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179                  |
|                      | Configure Embedded I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179                                |
|                      | Configure Local Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180                                |
|                      | Common Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181                                  |
|                      | I/O Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181                 |
|                      | Configure Distributed I/O Modules on an EtherNet/IP Network . . . . . . . . . . . . . . . . . . 182                                            |
|                      | Configure Distributed I/O Modules on a DeviceNet Network. . . . . . . . . . . . . . . . . . . . . 185                                          |
|                      | Monitor I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187            |
|                      | End Cap Detection and Module Faults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188                                  |
|                      | Chapter 9                                                                                                                                      |
| Use I/O Modules with | Select I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189           |
| CompactLogix 5370    | Local Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189                        |
| L3 Controllers       | Distributed I/O Modules over an EtherNet/IP Network. . . . . . . . . . . . . . . . . . . . . . 191                                             |
|                      | Distributed I/O Modules over a DeviceNet Network . . . . . . . . . . . . . . . . . . . . . . . . 191                                           |
|                      | Validate I/O Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193          |
|                      | Estimate Requested Packet Interval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193                                 |
|                      | Module Fault Related to RPI Estimates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194                                 |
|                      | Calculate System Power Consumption. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194                                    |
|                      | Physical Placement of I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197                               |
|                      | Power Supply Distance Rating. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199                            |
|                      | Configure I/O. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201       |
|                      | Common Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202                                  |
|                      | I/O Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202                 |
|                      | Configure Distributed I/O Modules on an EtherNet/IP Network . . . . . . . . . . . . . . . . . . 203                                            |
|                      | Configure Distributed I/O Modules on a DeviceNet Network. . . . . . . . . . . . . . . . . . . . 206                                            |
|                      | Monitor I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208              |
|                      | End Cap Detection and Module Faults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209                                  |
|                      | Chapter 10                                                                                                                                     |
| Develop Applications | Elements of a Control Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211                      |
|                      | Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212  |
|                      | Task Priority . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215              |
|                      | Programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216     |
|                      | Scheduled and Unscheduled Programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217                                     |
|                      | Routines. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218    |
|                      | Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219 |
|                      | Extended Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                    |
|                      | Programming Languages. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221                   |
|                      | Access Extended Properties in Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                                |
|                      | Access the Module Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223                 |
|                      | Create the Add-On Instruction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223                           |
|                      | Monitoring Controller Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224                 |

Monitoring Controller Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

|                                | Monitoring I/O Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                | I/O Communication Timeout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225                      |
|                                | I/O Communication Timeout to a Specific I/O Module . . . . . . . . . . . . . . . . . . . . . . 225                                       |
|                                | Interrupt the Execution of Logic and Execute the Fault Handler . . . . . . . . . . . . . 226                                             |
|                                | System Overhead Time Slice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227              |
|                                | Configure the System Overhead Time Slice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228                                |
|                                | Sample Controller Projects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229                   |
|                                | Chapter 11                                                                                                                               |
| Develop Integrated Motion Over | Motion Axes Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232       |
| an EtherNet/IP Network         | AXIS_VIRTUAL Axis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232             |
| Application                    | AXIS_CIP_DRIVE Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232              |
|                                | Maximum Number of Position Loop-configured Drives . . . . . . . . . . . . . . . . . . . . . . . . . 233                                  |
|                                | Position Loop-configured Drive Limits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233                           |
|                                | Time Synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234         |
|                                | Configure Integrated Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235            |
|                                | Enable Time Synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235                      |
|                                | Add a Drive. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236       |
|                                | Scalability in Applications Using Integrated Motion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238                          |
|                                | 1769-L18ERM-BB1B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239               |
|                                | 1769-L27ERM-QBFC1B Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240                          |
|                                | Chapter 12                                                                                                                               |
| Use a Secure Digital Card      | Store or Load a Project with the Secure Digital Card. . . . . . . . . . . . . . . . . . . . . . . . . . . 242                            |
|                                | Store a Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243  |
|                                | Load a Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245 |
|                                | Appendix A                                                                                                                               |
| Troubleshoot the Module        | Use Logix Designer Application for Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . 247                             |
|                                | Fault Type Determination. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249                  |
|                                | Use the CompactLogix 5370 Controllers Status Indicators . . . . . . . . . . . . . . . . . . . . . . 250                                  |
|                                | Appendix B                                                                                                                               |
| Replacement Considerations     | Product Comparison. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253        |
|                                | Power Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253                 |
|                                | Embedded DC Input Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253                           |
|                                | Firmware Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253                 |
|                                | Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254 |
|                                | Power Supply Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255       |
|                                | Series B and C Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255              |
|                                | Series A Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255          |
|                                | Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256       |

|                                                                | Appendix C                                                                                                                                                                                                            |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect Power to the Series A CompactLogix 5370 L1 Controllers | Connect External Power to Series A L1 Controllers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257 Connect Field Power to Series A L1 Controllers for I/O Devices . . . . . . . . . . . . . . . . . . 261 |
|                                                                | Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . 265                                                                        |

## About This Publication

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

This manual describes the necessary tasks to install, configure, program, and operate a CompactLogix™ 5370 controller. This manual is intended for automation engineers and control system developers.

CompactLogix 5370 controllers are designed to provide solutions for small and medium-sized applications.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication aren't in alignment with the movement toward inclusive language in technology. We're proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                                                          | Page           |
|--------------------------------------------------------------------------------|----------------|
| Added conformal coated controller catalog numbers                              | Throughout     |
| Updated to include CompactLogix 5370 L1 series C controller information        | Throughout     |
| Updated to include CompactLogix 5370 L2 series B controller information        | Throughout     |
| Updated CompactLogix 5370 L3 controller information                            | Throughout     |
| Added information regarding battery-less, embedded Energy Storage Module (ESM) | 35 ,  54 ,  71 |

## Abbreviations

This table lists the abbreviations that this manual uses.

| Abbreviation   | Full Term                           |
|----------------|-------------------------------------|
| BOOTP          | Bootstrap Protocol                  |
| CIP™           | Common Industrial Protocol          |
| CJC            | Cold Junction Composition           |
| COS            | Change of state                     |
| CST            | Coordinated System Time             |
| DHCP           | Dynamic Host Configuration Protocol |
| DINT           | Signed double integer               |
| DLR            | Device Level Ring                   |
| GSV            | Get System Value                    |
| HMI            | Human Machine Interface             |
| IOT            | Immediate Output                    |
| IP             | Internet Protocol                   |
| JSR            | Jump to Subroutine                  |
| MCR            | Master Control Relay                |
| MSG            | Message                             |
| NEC            | National Electrical Code            |
| QoS            | Quality of Service                  |
| RPI            | Requested packet interval           |
| RTB            | Removable terminal block            |
| RTD            | Resistance Temperature Detector     |
| RUIP           | Removal and insertion under power   |
| SD             | Secure Digital                      |
| SELV           | Safety Extra Low Voltage            |
| SINT           | Signed short integer                |
| SNMP           | Simple Network Management Protocol  |
| SSV            | Set System Value                    |
| TCP            | Transmission Control Protocol       |
| USB            | Universal Serial Bus                |
| UTC            | Coordinated Universal Time          |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

| Resource                                                                                                                                     | Description                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CompactLogix System Selection Guide, publication 1769-SG001                                                                                  | Describes available components for selecting a CompactLogix system                                                                                                                           |
| CompactLogix Controllers Specifications Technical Data, publication 1769-TD005                                                               | Provides CompactLogix controller specifications for all CompactLogix controllers                                                                                                             |
| 1769 Compact I/O Modules Specifications Technical Data, publication 1769-TD006                                                               | Provides specifications for all 1769 Compact I/O™ Modules                                                                                                                                    |
| CompactLogix Communication Modules Specifications Technical Data, publication 1769-TD007                                                     | Provides specifications for all CompactLogix Communication Modules                                                                                                                           |
| CompactLogix 5370 L3 Controllers Installation Instructions, publication 1769-IN029                                                           | Describes how to install CompactLogix 5370 L1 controllers                                                                                                                                    |
| CompactLogix 5370 L3 Controllers Installation Instructions, publication 1769-IN090 Describes how to install CompactLogix 5370 L2 controllers |                                                                                                                                                                                              |
| CompactLogix 5370 L3 Controllers Installation Instructions, publication 1769-IN023 Describes how to install CompactLogix 5370 L3 controllers |                                                                                                                                                                                              |
| Armor CompactLogix Controllers Installation Instructions, publication 1769-IN021                                                             | Describes how to install the Armor™ CompactLogix controllers                                                                                                                                 |
| Electronic Keying in Logix 5000 Control Systems Application Technique, publication LOGIX-AT001                                               | Describes the types of Electronic Keying available in Logix 5000™ control systems                                                                                                            |
| Execution Time and Memory Use for Logix 5000 Controller Instructions Reference Manual, publication 1756-RM087                                | Helps estimate the memory use and execution time of programmed logic and in selecting among different programming options.                                                                   |
| Integrated Motion on the EtherNet/IP Network: Configuration and Startup User Manual, publication MOTION-UM003                                | Describes how to configure an Integrated Motion over EtherNet/IP™ motion application and to start up that motion solution in a Logix 5000 control system                                     |
| Logix 5000 Controllers Common Procedures Programming Manual, publication 1756-PM001                                                          | Provides links to a collection of programming manuals that describe how you can use procedures that are common to all Logix 5000 controller projects                                         |
| Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003                                                         | Provides details about each available instruction for a Logix-based controller                                                                                                               |
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                                                 | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                                                  | Provides general guidelines for installing a Rockwell Automation industrial system                                                                                                           |

## Notes:

<!-- image -->

## CompactLogix 5370 Controllers Overview

The CompactLogix™ 5370 controllers offer state-of-the-art control, communication, and I/O elements in a distributed control package. This product family includes the following CompactLogix 5370 controllers:

- 1769-L16ER-BB1B
- 1769-L18ER-BB1B
- 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK
- 1769-L19ER-BB1B, 1769-L19ER-BB1BK
- 1769-L24ER-QB1B
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK
- 1769-L27ERM-QBFC1B
- 1769-L30ER, 1769-L30ERK
- 1769-L30ERM, 1769-L30ERMK
- 1769-L30ER-NSE
- 1769-L33ER, 1769-L33ERK
- 1769-L33ERM, 1769-L33ERMK
- 1769-L33ERMO
- 1769-L36ERM
- 1769-L36ERMO
- 1769-L37ERM, 1769-L37ERMK
- 1769-L37ERMO(1)
- 1769-L38ERM, 1769-L38ERMK
- 1769-L38ERMO(1)

Among the features the CompactLogix 5370 controllers support, are dual EtherNet/IP™ ports on each controller and support for Integrated Motion over an EtherNet/IP network on some CompactLogix 5370 controllers.

The Armor™ CompactLogix controller, 1769-L33ERMO, 1769-L36ERMO, 1769-L37ERMO, or 1769L38ERMO, combines the CompactLogix controller with a power supply in an IP67-rated housing for mounting on a machine. For information on how to install the Armor CompactLogix controller, see the Armor CompactLogix Controller Installation Instructions, publication 1769-IN021 .

## CompactLogix 5370 Control System Components

This table describes the components a CompactLogix 5370 controller uses in a typical control system.

| System Component                                         | Product Family                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Product Family                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Product Family                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System Component                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | CompactLogix 5370 L1 Controllers CompactLogix 5370 L2 Controllers CompactLogix 5370 L3 Controllers                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                          | Controller One of the controllers that is documented in this publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Controller One of the controllers that is documented in this publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Controller One of the controllers that is documented in this publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Power supply                                             | External power supply that is connected to the embedded 24V DC nominal input of the controller, nonisolated power supply. The power supply has a 10…28.8 input range.                                                                                                                                                                                                                                                                                                                                                                         | External power supply that is connected to the embedded 24V DC input of the controller, isolated power supply                                                                                                                                                                                                                                                                                                                                                                                                                                 | One of the following 1769 Compact I/O™ power supplies: • 1769-PA2, 1769-PA2K • 1769-PB2, 1769-PB2K • 1769-PA4, 1769-PA4K • 1769-PB4, 1769-PB4K                                                                                                                                                                                                                                                                                                                                                                                                |
| Communication networks components                        | Any of the following: • EtherNet/IP network via built-in EtherNet/ IP network ports • USB connection only for programming and firmware updates                                                                                                                                                                                                                                                                                                                                                                                                | Any of the following: • EtherNet/IP network via built-in EtherNet/IP network ports • DeviceNet® network via a 1769-SDN module • USB connection only for programming and firmware updates                                                                                                                                                                                                                                                                                                                                                      | Any of the following: • EtherNet/IP network via built-in EtherNet/IP network ports • DeviceNet® network via a 1769-SDN module • USB connection only for programming and firmware updates                                                                                                                                                                                                                                                                                                                                                      |
| Software                                                 | • One of the following: – RSLogix 5000® software, version 20.xx.xx, - For CompactLogix 5370 controllers that are using firmware revision 20.xxx – Logix Designer application, version 21.00.00 or later, - For CompactLogix 5370 controllers that are using firmware revision 21.000 or later • RSLinx® Classic software, version 2.59.xx or later • RSNetWorx™ for DeviceNet software, version 11.00.00 or later IMPORTANT: This software isn’t used with CompactLogix 5370 L1 controllers because they do not offer DeviceNet connectivity. | • One of the following: – RSLogix 5000® software, version 20.xx.xx, - For CompactLogix 5370 controllers that are using firmware revision 20.xxx – Logix Designer application, version 21.00.00 or later, - For CompactLogix 5370 controllers that are using firmware revision 21.000 or later • RSLinx® Classic software, version 2.59.xx or later • RSNetWorx™ for DeviceNet software, version 11.00.00 or later IMPORTANT: This software isn’t used with CompactLogix 5370 L1 controllers because they do not offer DeviceNet connectivity. | • One of the following: – RSLogix 5000® software, version 20.xx.xx, - For CompactLogix 5370 controllers that are using firmware revision 20.xxx – Logix Designer application, version 21.00.00 or later, - For CompactLogix 5370 controllers that are using firmware revision 21.000 or later • RSLinx® Classic software, version 2.59.xx or later • RSNetWorx™ for DeviceNet software, version 11.00.00 or later IMPORTANT: This software isn’t used with CompactLogix 5370 L1 controllers because they do not offer DeviceNet connectivity. |
| Secure Digital (SD) card for external nonvolatile memory | • 1784-SD1 card - Ships with CompactLogix 5370 controller and offers 1 GB of memory • 1784-SD2 card - Available for separate purchase and offers 2 GB of memory                                                                                                                                                                                                                                                                                                                                                                               | • 1784-SD1 card - Ships with CompactLogix 5370 controller and offers 1 GB of memory • 1784-SD2 card - Available for separate purchase and offers 2 GB of memory                                                                                                                                                                                                                                                                                                                                                                               | • 1784-SD1 card - Ships with CompactLogix 5370 controller and offers 1 GB of memory • 1784-SD2 card - Available for separate purchase and offers 2 GB of memory                                                                                                                                                                                                                                                                                                                                                                               |
| I/O modules                                              | • 16 embedded 24V DC digital input points - The nominal input voltage is 24V DC but the operating range is 10…28.8V DC. • 16 embedded 24V DC digital output points - The nominal input voltage is 24V DC but the operating range is 10…28.8V DC. • Local expansion modules- 1734 POINT I/O™ modules • Distributed I/O - Multiple I/O module product lines over an EtherNet/IP network                                                                                                                                                         | • 16 embedded 24V DC digital input points • 16 embedded 24V DC digital output points • Only 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers – Four embedded high-speed counters – Four embedded universal analog input points – Two embedded analog output points • Local expansion modules- 1769 Compact I/O modules • Distributed I/O - Multiple I/O module product lines over DeviceNet and EtherNet/IP networks                                                                                                                      | • Local expansion modules- 1769 Compact I/ O modules • Distributed I/O - Multiple I/O module product lines over DeviceNet and EtherNet/IP networks                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                          | Reset button If held in during controller power-up, it clears the user program from the internal memory of the controller.                                                                                                                                                                                                                                                                                                                                                                                                                    | Reset button If held in during controller power-up, it clears the user program from the internal memory of the controller.                                                                                                                                                                                                                                                                                                                                                                                                                    | Reset button If held in during controller power-up, it clears the user program from the internal memory of the controller.                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Controller Functionality

This table describes the functionality available with CompactLogix 5370 controllers.

| Cat. No.                            | Controller Tasks Supported   | Programs Supported Per Task   | Internal Energy Storage Solution         | EtherNet/IP Network Topology Support           | Power Supply Distance Rating   | Onboard User Memory Size   | Local I/O Module Support                   |
|-------------------------------------|------------------------------|-------------------------------|------------------------------------------|------------------------------------------------|--------------------------------|----------------------------|--------------------------------------------|
| 1769-L16ER-BB1B                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear |                                | 384 KB                     | As many as six 1734 POINT I/O modules(1)   |
| 1769-L18ER-BB1B                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | NA                             | 512 KB                     | As many as eight 1734 POINT I/O modules(1) |
| 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear |                                | 512 KB                     | As many as eight 1734 POINT I/O modules(1) |
| 1769-L19ER-BB1B, 1769-L19ER-BB1BK   |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear |                                | 1 MB                       | As many as eight 1734 POINT I/O modules(1) |
| 1769-L24ER-QB1B                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | See footnote(2)                | 768 KB                     | As many as four Compact I/O modules        |
| 1769-L24ER-QBFC1BK                  |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | See footnote(2)                | 768 KB                     | As many as four Compact I/O modules        |
| 1769-L27ERM-QBFC1B                  |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | See footnote(2)                | 1 MB                       | As many as four Compact I/O modules        |
| 1769-L30ER, 1769-L30ERK             |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 1 MB                       | As many as eight Compact I/O modules       |
| 1769-L30ER-NSE                      |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 1 MB                       | As many as eight Compact I/O modules       |
| 1769-L33ER, 1769-L33ERK             |                              | 32 1000                       | Yes - Eliminating the need for a battery | • Traditional star                             | 4                              | 1 MB                       | As many as 16                              |
| 2 MB p modules 1769-L33ERM, 1769-L33ERMK                                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 2 MB                       | Compact I/O                                |
| 1769-L33ERMO                        |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 1 MB                       | —                                          |
| 1769-L36ERM                         |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 3 MB                       | As many as 30 Compact I/O modules          |
| 1769-L36ERMO                        |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 4 MB                       | —                                          |
| 1769-L37ERMO(3)                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 5 MB                       | —                                          |
| 1769-L38ERM, 1769-L38ERMK           |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              | 5 MB                       |                                            |
| 1769-L38ERMO(3)                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              |                            |                                            |
|                                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              |                            |                                            |
|                                     |                              | 32 1000                       | Yes - Eliminating the need for a battery | topologies: • Device Level Ring (DLR) • Linear | 4                              |                            |                                            |

For more information on power supply distance rating regarding how to use Compact I/O modules in a CompactLogix 5370 L2 control system, see Chapter 8, page 177 .

(3) Available at software version 31 and firmware revision 31.

The 1769-L30ER-NSE controller is intended for use in applications that require the installed controller to deplete its residual stored energy to specific levels before transporting it into or out of your application.

<!-- image -->

WARNING: If your application requires the 1769-L30ER-NSE controller to deplete its residual stored energy to 200 µJ or fewer before you transport it into or out of the application, complete these steps before you remove the controller.

1. Turn off power to the chassis.

After you turn off power, the OK status indicator on the controller transitions from Green to Steady Red to OFF.

2. Wait at least 15 minutes for the residual stored energy to decrease to 200 µJ or fewer before you remove the controller.

There's no visual indication of when the 15 minutes has expired. You must track that time period.

## IMPORTANT

The Real Time Clock (RTC) does not retain its time and date when the power is off.

Some applications require that the installed controller to deplete its residual stored energy to specific levels before transporting it into or out of your application. This requirement can include other devices that also require a wait time before removing them. See the documentation of those products for more information.

## Support for Integrated Motion over an EtherNet/IP Network

The following CompactLogix 5370 controllers support Integrated Motion over an EtherNet/IP network:

- 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK
- 1769-L27ERM-QBFC1B
- 1769-L30ERM, 1769-L30ERMK
- 1769-L33ERM, 1769-L33ERMK
- 1769-L33ERMO
- 1769-L36ERM
- 1769-L36ERMO
- 1769-L37ERM, 1769-L37ERMK
- 1769-L37ERMO(1)
- 1769-L38ERM, 1769-L38ERMK
- 1769-L38ERMO(1)

For more information on how to use CompactLogix 5370 controllers in applications that require Integrated Motion over an EtherNet/IP network, see Chapter 11, page 231 .

## Electronic Keying

Electronic Keying reduces the possibility that you use the wrong device in a control system. It compares the device that is defined in your project to the installed device. If keying fails, a fault occurs.

## Electronic Keying Attributes

| Attribute Description                                                                     |
|-------------------------------------------------------------------------------------------|
| Vendor The device manufacturer.                                                           |
| Device Type The general type of the product, for example, digital I/O module.             |
| Product Code The specific type of the product. The Product Code maps to a catalog number. |
| Major Revision A number that represents the functional capabilities of a device.          |
| Minor Revision A number that represents behavior changes in the device.                   |

## Electronic Keying Options

| Keying Option Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatible Module           | Lets the installed device accept the key of the device that is defined in the project when the installed device can emulate the defined device. With Compatible Module, you can typically replace a device with another device that has the following characteristics: • Same catalog number • Same or higher Major Revision • Minor Revision as follows: – If the Major Revision is the same, the Minor Revision must be the same or higher. – If the Major Revision is higher, the Minor Revision can be any number.                                                                                                 |
| Disable Keying              | Indicates that the keying attributes aren’t considered when attempting to communicate with a device. With Disable Keying, communication can occur with a device other than the type specified in the project. ATTENTION: Be extremely cautious when using Disable Keying; if used incorrectly, this option can lead to personal injury or death, property damage, or economic loss. We strongly recommend that you do not use Disable Keying. If you use Disable Keying, you must take full responsibility for understanding whether the device being used can fulfill the functional requirements of the application. |
| Exact Match                 | Indicates that all keying attributes must match to establish communication. If any attribute does not match precisely, communication with the device does not occur.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

Carefully consider the implications of each keying option when selecting one.

## IMPORTANT

Changing Electronic Keying parameters online interrupts connections to the device and any devices that are connected through the device. Connections from other controllers can also be broken. If an I/O connection to a device is interrupted, the result can be a loss of data.

## More Information

For more detailed information on Electronic Keying, see Electronic Keying in Logix 5000™ Control Systems Application Technique, publication LOGIX-AT001 .

## Example System Configurations

CompactLogix 5370 controllers support the following networks:

- EtherNet/IP network - All CompactLogix 5370 controllers
- DeviceNet network - Only CompactLogix 5370 L2 and L3 controllers

## EtherNet/IP Network

## IMPORTANT

In addition to using CompactLogix 5370 controllers in a DLR network topology on an EtherNet/IP network, you can also use them in linear or star EtherNet/IP network topologies.

For more information on the other EtherNet/IP network topologies, see Chapter6, page 99 .

Some of the CompactLogix 5370 controllers support Integrated Motion over an EtherNet/IP network, if desired. For more information on using Integrated Motion over an EtherNet/IP network, see Chapter 11, page 231 .

## Example 1769-L18ERM-BB1B Control System Configuration on an EtherNet/IP Network

<!-- image -->

Kinetix 5500

## Example 1769-L27ERM-QBFC1B Control System Configuration on an EtherNet/IP Network

<!-- image -->

## Example 1769-L33ERM Control System Configuration on an EtherNet/IP Network

<!-- image -->

## DeviceNet Network

## IMPORTANT

CompactLogix 5370 L2 and L3 controllers can send messages to devices on the DeviceNet network; however, these controllers can't receive messages from those devices on the DeviceNet network.

## Example 1769-L24ER-QB1B Control System Configuration on a DeviceNet Network

<!-- image -->

Figure 1 - Example 1769-L33ERM Control System Configuration on a DeviceNet Network

<!-- image -->

For more information on how to use the CompactLogix 5370 L2 or L3 controllers on DeviceNet networks, see Chapter 6, page 111 .

## Environment and Enclosure

<!-- image -->

ATTENTION: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in EN/IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment isn't intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure-type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 for more installation requirements
- NEMA 250 and EN/IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosure

## North American Hazardous Location Approval

<!-- image -->

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | WARNING: ?EXPLOSION HAZARD - • Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. • Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. • Substitution of components may impair suitability for Class I, Division 2.                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | WARNING: ?RISQUE D’EXPLOSION - • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. • La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2.                                                                                                                                  |

<!-- image -->

<!-- image -->

## Install the CompactLogix 5370 L1 Controller

## UK and European Hazardous Location Approval

The following applies to products marked II 3 G. Such products:

- are Equipment Group II, Equipment Category 3, and comply with the Essential Health and Safety Requirements relating to the design and construction of such equipment given in Schedule 1 of UKEX Regulation 2016 No. 1107 and Annex II to EU Directive 2014/34/EU. See the UKEX and EU Declaration of Conformity at rok.auto/certifications for details.
- provide protection type II 3 G Ex ec IIC T4 Gc according to EN IEC 60079-7.
- comply to Standards: EN IEC 60079-0:2018, EN IEC 60079-7:2015+A1:2018 reference certificate number UL 21 ATEX 2603X and UL22UKEX2515X.
- are intended for use in areas in which explosive atmospheres caused by gases, vapors, mists, or air are unlikely to occur, or are likely to occur only infrequently and for short periods. Such locations correspond to Zone 2 classification according to UKEX regulation 2016 No. 1107 and ATEX directive 2014/34/EU.

## Special Considerations for Safe Use

<!-- image -->

## WARNING: ?

- The equipment shall be mounted in an UKEX/ATEX Zone 2 certified enclosure with a minimum ingress protection rating of at least IP54 (in accordance with EN IEC 60079-0) and used in an environment of not more than Pollution Degree 2 (as defined in EN/IEC 60664-1). The enclosure must be accessible only by the use of a tool.
- This equipment must be used within its specified ratings that are defined by Rockwell Automation.
- Provisions shall be made to prevent the rated voltage from being exceeded by transient disturbances of more than 140% of the peak rated voltage when applied in Zone 2 environments.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Enclosure must be marked with the following: "Warning - Do not open when energized." After installation of equipment into the enclosure, access to termination compartments must be dimensioned so that conductors can be readily connected.
- The instructions in the user manual shall be observed.
- This equipment must be used only with UKEX/ATEX certified Rockwell Automation backplanes.
- Earthing is accomplished through mounting of modules on rail.

## Prevent Electrostatic Discharge

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## Before You Begin

The CompactLogix™ 5370 L1 series B and C controller redesign occurred to provide an option to use one external power supply for system power and field side power.

There are differences between the CompactLogix 5370 L1, series A and B, controllers, which are detailed throughout the sections of this manual.

Consider the details in this section before installing a CompactLogix 5370 L1 controller.

<!-- image -->

ATTENTION: If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment can be impaired.

- The control system includes the controller, an embedded power supply, and embedded I/O points.

<!-- image -->

- The embedded power supply for the series A L16ER, L18ER, or L18ERM controller is a 24V DC nominal, non-isolated power supply with an input range of 10…28.8V DC. You wire the embedded power supply via a removable connector.
- The embedded power supply for the series B and C L16ER, L18ER, and L18ERM controllers, and the series A and C L19ER controller is a 24V DC nominal, isolated power supply. The input range of the power supply is 10…28.8V DC. You wire the embedded power supply via a removable connector.

## IMPORTANT

You must use a dedicated external Class 2/SELV-approved power supply to provide power to the system, according to the needs of the application, and within the operating voltage range of the controller for only series A L16ER, L18ER, and L18ERM controllers.

You can't use the external power supply that provides power to the embedded power supply of the controller to provide power to any other components or devices in the application for only series A L16ER, L18ER, and L18ERM controllers.

- A second, fused external power supply must be used to provide power to other components for only series A L16ER, L18ER, and L18ERM controllers (see Appendix C, page 257).
- Power for other components can be provided from the external power supply that is used to provide power to the system for only series B and C L16ER, L18ER, L18ERM controllers, and series A and C L19ER controllers.
- The controller has 16 embedded digital input points and 16 embedded digital output points. You wire the input and output points via a removable connector.
- The controller supports the use of a limited number of 1734 POINT I/O  modules on the POINTBus™ backplane as local expansion modules.

## IMPORTANT

You must use the latest series and firmware revision for all 1734 POINT I/O modules in the local expansion slots to make sure that your application operates as expected. Use of an older firmware revision renders the entire 1734 bus inoperable.

This table lists local expansion module support by controller catalog number.

## Local Expansion Module Support for CompactLogix 5370 L1 Controllers

| Cat. No.                            |   1734 POINT I/O Modules Supported, Max |
|-------------------------------------|-----------------------------------------|
| 1769-L16ER-BB1B                     |                                       6 |
| 1769-L18ER-BB1B                     |                                       8 |
| 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK |                                       8 |
| 1769-L19ER-BB1B, 1769-L19ER-BB1BK   |                                       8 |

See Chapter 7, page 117 for further information about the I/O modules.

<!-- image -->

ATTENTION: Do not discard the end cap. Use this end cap to cover the exposed interconnections on the last mounting base on the DIN rail. Failure to do so could result in equipment damage or injury from electric shock. For more information on how to terminate the end of your system, see page 31 .

1734 POINT I/O modules support removal and insertion under power.

## CompactLogix 5370 L1 Controller Parts

These parts are included in the box when you order your controller:

- Controller - Specific catalog number varies by order
- 1784-SD1 Secure Digital (SD) card with 1 GB of memory storage

A 1784-SD2 SD card with 2 GB of memory storage, or more 1784-SD1 SD cards, are also available if you need extra memory.

## IMPORTANT

The life expectancy of nonvolatile media is dependent on the number of write cycles that are performed. Nonvolatile media use a wear leveling technique or technology for prolonging the service life, but avoid frequent writes.

Avoid frequent writes when logging data. We recommend that you log data to a buffer in the memory of your controller and limit the number of times data is written to removable media.

- An end cap protective cover that slides onto the right side of the CompactLogix 5370 L1 control system.

## Install the Secure Digital Card

The CompactLogix 5370 L1 controller is shipped from the factory with the 1784-SD1 SD card installed.

Complete these steps to reinstall an SD card that has been removed from the controller back into the controller or to install a new SD card into the controller.

We recommend that you leave the SD card in the controller, even when it isn't used. If the controller experiences a major non-recoverable fault, extended fault information is saved to the card.

<!-- image -->

WARNING: ?When you insert or remove the SD card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

1. Verify that the SD card is locked or unlocked according to your preference. Consider that, if the card is unlocked, the controller can write data to it or read data from it.

Unlocked

<!-- image -->

2. Open the door for the SD card.

<!-- image -->

Locked

<!-- image -->

3. Insert the SD card into the SD card slot. You can install the SD card in only one orientation. The beveled corner is at the top. If you feel resistance when inserting the SD card, pull it out and change the orientation.
4. Gently press the card until it clicks into place.
5. Close the SD card door.

<!-- image -->

<!-- image -->

We recommend that you keep the SD card door closed during normal system operation. For more information on how to use the SD card, see Chapter 12, page 241 .

## Install the System

Complete these steps to install the CompactLogix 5370 L1 control system.

## Mount the System

You mount a CompactLogix 5370 L1 control system on a DIN rail. Before you complete the steps that are required to install the system, install a DIN rail.

<!-- image -->

WARNING: ?When used in a Class I, Division 2, hazardous location, this equipment must be mounted in a suitable enclosure with proper wiring method that complies with the governing electrical codes.

Available DIN Rails

<!-- image -->

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc plated chromate-passivated steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum or plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately. Be sure to ground the DIN rail properly. Refer to Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for more information.

You can mount the CompactLogix 5370 L1 controller on these DIN rails:

- EN 50 022 - 35 x 7.5 mm (1.38 x 0.30 in.)
- EN 50 022 - 35 x 15 mm (1.38 x 0.59 in.)

## IMPORTANT

You must install bumpers on the back of your CompactLogix 5370 L1 controller before mounting it on the EN 50022 - 35 x 15 mm (1.38 x 0.59 in.) DIN rail.

For more information about which bumpers to order, see Knowledgebase Technote, 5370 L16ER/L18ER recommended Bumpers for use with 1.38 x 0.59 in. DIN rail.

Minimum Spacing

Maintain spacing from enclosure walls, wireways, and adjacent equipment. Allow 50 mm (2 in.) of space on all sides, as shown. This spacing provides ventilation and electrical isolation.

<!-- image -->

## System Dimensions

## CompactLogix 5370 L1 Control System Dimensions

<!-- image -->

<!-- image -->

CompactLogix 5370 L1 Control System Dimensions with Expansion I/O Modules Installed

<!-- image -->

<!-- image -->

## Ground the System

<!-- image -->

ATTENTION: This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the power supply's mounting tabs or DIN rail (if used) aren't required unless the mounting surface can't be grounded. See Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for additional information.

## Install the Controller

Complete these steps to install the controller.

1. Pull out the locking tabs.
2. Slide the controller into position on the DIN rail and push the locking tabs in.

<!-- image -->

<!-- image -->

3. If you aren't using local expansion modules, use the tongue-and-groove slots on the right side of the controller to slide a protective covering onto the controller. The protective cover ships with the controller.

The covering covers the exposed interconnections on the right side of the controller. Failure to use a protective covering can result in equipment damage or injury from electric shock.

<!-- image -->

If you're using local expansion modules, see Chapter 7, page 127 for more information on how to install them in a CompactLogix 5370 L1 control system.

## Install the Removable Terminal Block

A removable terminal block (RTB) is supplied with your wiring base assembly. To remove, pull up on the RTB handle. This feature allows the mounting base to be removed and replaced as necessary without removing any wires. To reinsert the removable terminal block, proceed as follows:

1. Insert the end opposite the handle into the base unit. This end has a curved section that engages with the wiring base.
2. Rotate the RTB into the wiring base until it locks itself in place.
3. If an I/O module is installed, snap the RTB handle into place on the module.

<!-- image -->

<!-- image -->

WARNING: ?When you connect or disconnect the RTB with field-side power applied, an electric arc can occur. This can cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

## Connect Power to the Controller (Series B and C)

For information to connect power to a series A L1 controller, see Appendix C, page 257 .

## IMPORTANT

This section describes how to power the controller via the VDC+ and VDC- terminals.

Connections to the VDC+ and VDC- terminals do not provide power to input or output devices that are connected to the embedded I/O modules of the controller or local expansion modules. Power must be connected to the FP+ and FP- terminals to provide power to input or output devices that are connected to the embedded I/O modules of the controller or local expansion modules.

The external power supply can be used to power both the VDC+/- and FP+/- terminals on the series B and C L1 controllers.

For more information on how to provide power to input or output devices that are connected to the embedded I/O modules of the controller and local expansion modules, see Chapter 7, page 117 .

WARNING: Do not connect directly to line voltage. Line voltage must be supplied by a suitable, approved isolating transformer or power supply having short circuit capacity not exceeding 100VA maximum or equivalent. The controller power requirement is 30VA.

<!-- image -->

Power is connected to the controller via a removable connector that is connected to the front of the controller. This graphic shows the connector.

<!-- image -->

## IMPORTANT

The controller is grounded once it's installed on a DIN rail as described on page 28 .

Consider these points before completing the steps in this section:

- This section describes how to connect an external 24V DC power source to the CompactLogix 5370 L1 controller.

For information on how to provide field power to input and output devices that are connected to the embedded I/O modules of the controller and local expansion modules via the removable connector, see Chapter 7, page 117 .

- Use a power source that most effectively meets your application needs. That is, calculate the power requirements for your application before choosing a power source to avoid using a power source that far exceeds your application requirements.
- This section assumes that any DIN rail that you use has been grounded following Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .
- The embedded power supply of the CompactLogix 5370 L1 controller provides power to the controller and POINTBus backplane.
- Not all Class 2/SELV-listed power supplies are certified for use in all applications, for example, use in nonhazardous and hazardous environments. Before installing an external power supply, consult all specification and certification
- information to verify that you're using an acceptable external power supply.
- Only for example purposes, this section describes how to use a 1606-XLE120E, NEC Class 2 switched-mode power supply. The exact steps for other external power supplies can vary from the steps that are described here.

Complete these steps to connect power to the CompactLogix series B and C L16ER, L18ER, and L18ERM controllers, and series A and C L19ER controllers.

1. Verify that the external 24V DC power source isn't powered.
2. Mount the external 24V DC power source on a DIN rail. The external 24V DC power source can be installed on the same DIN rail as the controller

or a separate DIN rail.

3. Connect wires to the 24V DC+ and 24V DC- connections on the external 24V DC power source.

<!-- image -->

WARNING: ?If you connect or disconnect wiring while the field-side power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

4. Pull the removable connector off the CompactLogix 5370 L1 controller.
5. Connect the wire that is connected to the 24V DC+ terminal on the external 24V DC power source to the VDC+ terminal. The VDC+ terminal is the top terminal on the removable connector.
6. Connect the wire that is connected to the 24V DC- terminal on the external 24V DC power source to the VDC- terminal. The VDC- terminal is the second from the top on the removable connector.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

If your application requires a power control device, for example, a switch or relay, between the external 24V DC power source and the CompactLogix 5370 L1 controller to control when the controller is powered, you must install the power control device at the VDC+ terminal on the removable connector.

If you install the power control device at the VDC- terminal, the CompactLogix 5370 L1 controller can have problems powering up or powering down properly.

7. Plug the removable connector back into the controller.
8. Secure the removable connector in place.
9. Turn on power to the external 24V DC power source.

<!-- image -->

This graphic shows an external 24V DC power source that is connected to a CompactLogix 5370 L1 controller.

<!-- image -->

<!-- image -->

CompactLogix 5370 Controllers have an embedded, battery-less Energy Storage Module (ESM) that provides power to the CPU upon power-down, allowing the controller to write customer application and tag data to the onboard nonvolatile memory. In some cases, the ESM continues to provide enough power to keep the wall clock active until its residual stored energy is depleted.

## Connect to the Controller Via a USB Cable

The controller has a USB port that uses a Type B receptacle. The port is USB 2.0-compatible and operates at 12 Mbps.

Use a USB cable to connect your computer to the USB port. With this connection, you can update firmware and download programs to the controller directly from your computer.

<!-- image -->

<!-- image -->

ATTENTION: The USB port is intended only for temporary local programming purposes and not intended for permanent connection.

The USB cable isn't to exceed 3.0 m (9.84 ft) and must not contain hubs.

WARNING: ?Do not use the USB port in hazardous locations.

Plug the USB cable into the CompactLogix 5370 L1 controller.

<!-- image -->

## Connect the Controller to an EtherNet/IP Network

<!-- image -->

WARNING: ?If you connect or disconnect the communication cable with power applied to this module or any device on the network, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Connect the RJ45 connector of the Ethernet cable to one of the Ethernet ports on the controller. The ports are on the bottom of the controller.

<!-- image -->

## IMPORTANT

This example shows how to connect the controller to the network through one port. Depending on the network topology of your application, you can connect both ports of the controller to the EtherNet/IP™ network.

## Connecting to Different EtherNet/IP Network Topologies

CompactLogix 5370 L1 controllers have embedded switch technology and two EtherNet/IP ports that let you use it in various EtherNet/IP network topologies:

- Device Level Ring network topology - Both ports on the controller are connected to the network.
- Linear network topology - Both ports on the controller are connected to the network.
- Star network topology - One port on the controller is connected to the network.

There are connection and configuration requirements for each EtherNet/IP network topology.

For more information, see Chapter 6, page 99 .

## Notes:

## Environment and Enclosure

<!-- image -->

ATTENTION: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in EN IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment isn't intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure-type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 for more installation requirements.
- NEMA 250 and EN/IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosure.

## North American Hazardous Location Approval

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |

<!-- image -->

## WARNING: EXPLOSION HAZARD -

- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Substitution of components may impair suitability for Class I, Division 2.

<!-- image -->

## WARNING: RISQUE D'EXPLOSION -

- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement.
- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit.
- La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2.

<!-- image -->

## Install the CompactLogix 5370 L2 Controller

## UK and European Hazardous Location Approval

The following applies to products marked II 3 G. Such products:

- Are Equipment Group II, Equipment Category 3, and comply with the Essential Health and Safety Requirements relating to the design and construction of such equipment given in Schedule 1 of UKEX Regulation 2016 No. 1107 and Annex II to UKEX and EU Directive 2014/ 34/EU. See the UKEX and EU Declaration of Conformity at rok.auto/certifications for details.
- Provides protection type II 3 G Ex ec IIC T4 Gc according to EN 60079-7.
- Comply to Standards: EN IEC 60079-0:2018, EN IEC 60079-7:2015+A1:2018 reference certificate number DEMKO12ATEX1116807X and UL22UKEX2516X.
- Are intended for use in areas in which explosive atmospheres caused by gases, vapors, mists, or air are unlikely to occur, or are likely to occur only infrequently and for short periods. Such locations correspond to Zone 2 classification according to UKEX regulation 2016 No. 1107 and ATEX directive 2014/34/EU.

## IEC Hazardous Location Approval

The following applies to products with IECEx certification. Such modules:

- Are intended for use in areas in which explosive atmospheres caused by gases, vapors, mists, or air are unlikely to occur, or are likely to occur only infrequently and for short periods. Such locations correspond to Zone 2 classification to IEC 60079-0.
- Provide protection type II 3 G Ex ec IIC T4 Gc according to IEC 60079-7.
- Comply to Standards: IEC 60079-0:7th edition, IEC 60079-7:5.1 Edition, reference IECEx certificate number IECEx UL 21.0112X.

## Special Considerations for Safe Use

<!-- image -->

## WARNING:

- The equipment shall be mounted in an UKEX/ATEX/IECEX Zone 2 certified enclosure with a minimum ingress protection rating of at least IP54 (in accordance with EN 60079-0) and used in an environment of not more than Pollution Degree 2 (as defined in EN 60664-1). The enclosure must be accessible only by the use of a tool.
- This equipment must be used within its specified ratings that are defined by Rockwell Automation.
- Provisions shall be made to prevent the rated voltage from being exceeded by transient disturbances of more than 140% of the peak rated voltage when applied in Zone 2 environments.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Enclosure must be marked with the following: "Warning - Do not open when energized." After installation of equipment into the enclosure, access to termination compartments must be dimensioned so that conductors can be readily connected.
- The instructions in the user manual shall be observed.
- This equipment must be used only with UKEX/ATEX/IECEX certified Rockwell Automation backplanes.
- Earthing is accomplished through mounting of modules on rail.
- This equipment isn't resistant to sunlight or other sources of UV radiation.

## Prevent Electrostatic Discharge

<!-- image -->

## ATTENTION:

- This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:
- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## Before You Begin

Consider these details before installing a CompactLogix™ 5370 L2 controller:

- The control system includes a controller, an embedded power supply, embedded I/O points, and a 1769-ECR/1769-ECRK right end cap.
- The embedded power supply is a 24V DC input, isolated power supply This graphic shows an example CompactLogix 5370 L2 controller.

## 1769-L24ER-QBFC1B Control System

<!-- image -->

<!-- image -->

ATTENTION: You must use an external power supply that is Class 2 or SELVlisted for series A L1 controllers.

For example, you can use a 1606-XLSDNET4, standard switched-mode power supply, as shown in this chapter.

- The controllers have embedded I/O points. You wire the input and output points via a removable connector.
- The controller supports the use of up to four Compact I/O™ modules on the local 1769 CompactBus backplane as local expansion modules.
- For more information on how to use embedded I/O points and local expansion modules, see Chapter 8, page 145 .
- You must terminate the end of the CompactBus via a 1769-ECR/1769-ECRK right end cap as shown in step 6 on page 50 .
- You can't remove nor install Compact I/O modules while the controller is powered.

<!-- image -->

ATTENTION: CompactLogix 5370 L2 control systems do not support removal and insertion under power (RIUP). Removing a 1769 Compact I/O module or end cap generates a controller fault and may also result in damage to system components.

## CompactLogix 5370 L2 Controller Parts

These parts are included in the box when you order your controller:

- Controller - Specific catalog number varies by order
- 1769-ECR/1769-ECRK Compact I/O end cap/terminator
- 1784-SD1 Secure Digital (SD) card with 1 GB of memory storage

A 1784-SD2 SD card with 2 GB of memory storage, or more1784-SD1 SD cards, are also available if you need extra memory.

## IMPORTANT

The life expectancy of nonvolatile media is dependent on the number of write cycles that are performed. Nonvolatile media use a wear leveling technique or technology for prolonging the service life, but avoid frequent writes.

Avoid frequent writes when logging data. We recommend that you log data to a buffer in the memory of your controller and limit the number of times data is written to removable media.

## Install the Secure Digital Card

The CompactLogix 5370 L2 controller is shipped from the factory with the 1784-SD1 SD card installed .

Complete these steps to reinstall an SD card that has been removed from the controller back into the controller or to install a new SD card into the controller.

We recommend that you leave the SD card in the controller, even when it isn't used. If the controller experiences a Major Non-recoverable Fault, extended fault information is saved to the card.

<!-- image -->

WARNING: When you insert or remove the SD card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

1. Verify that the SD card is locked or unlocked according to your preference. Consider that, if the card is unlocked, the controller can write data to it or read data from it.
2. Open the door for the SD card.
3. Insert the SD card into the SD card slot. You can install the SD card in one orientation only. The beveled corner is at the bottom.

<!-- image -->

<!-- image -->

If you feel resistance when inserting the SD card, pull it out and change the orientation.

## 4. Gently press the card until it clicks into place.

<!-- image -->

5. Close the SD card door.

<!-- image -->

We recommend that you keep the SD card door closed during normal system operation. For more information on how to use the SD card, see Chapter 12, page 241 .

## Install the System

Complete these tasks to install the CompactLogix 5370 L2 control system.

## Mount the System

CompactLogix 5370 L2 control systems are mounted on a DIN rail. Install the DIN rail before completing the steps that are required to install the system.

<!-- image -->

WARNING: When used in a Class I, Division 2, hazardous location, this equipment must be mounted in a suitable enclosure with proper wiring method that complies with the governing electrical codes.

Available DIN Rails

You can mount the CompactLogix 5370 L2 controller on these DIN rails:

- EN 50 022 - 35 x 7.5 mm (1.38 x 0.30 in.)
- EN 50 022 - 35 x 15 mm (1.38 x 0.59 in.)

<!-- image -->

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc-plated chromate-passivated steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum or plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately. Be sure to ground the DIN rail properly. Refer to Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for more information.

## Minimum Spacing

Maintain spacing from enclosure walls, wireways, and adjacent equipment. Allow 50 mm (2 in.) of space on all sides, as shown. This spacing provides ventilation and electrical isolation.

<!-- image -->

<!-- image -->

## System Dimensions

## 1769-L24ER-QB1B Controller System Dimensions

<!-- image -->

<!-- image -->

1769-L24ER-QB1B Controller System Dimensions with Expansion Modules Installed

<!-- image -->

## 1769-L24ER-QBFC1B Controller System Dimensions

<!-- image -->

<!-- image -->

1769-L24ER-QBFC1B Controller System Dimensions with Expansion Modules Installed

<!-- image -->

## 1769-L27ERM-QBFC1B Controller System Dimensions

<!-- image -->

<!-- image -->

## 1769-L27ERM-QBFC1B Controller System Dimensions with Expansion Modules Installed

<!-- image -->

## Ground the System

<!-- image -->

ATTENTION: This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the power supply's mounting tabs or DIN rail (if used) aren't required unless the mounting surface can't be grounded. See Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation® publication 1770-4.1, for additional information.

## Install the Controller

Complete these steps to install the controller.

1. Pull out the bottom locking tabs.
2. Hook the top of the controller on the DIN rail.
3. Swing it downward until the controller is flush against the DIN rail and push it down against the DIN rail.
4. Push the controller against the DIN rail.
5. Push the locking tabs in.

<!-- image -->

<!-- image -->

6. If you aren't using local expansion modules, slide the 1769-ECR/1769-ECRK end cap onto the right side of the controller.

IMPORTANT

You must install an end cap onto the right side of the CompactLogix 5370 L2 controller system either at the end of the controller. You must also install an end cap at the end of any local expansion modules that can be installed onto the controller.

<!-- image -->

7. Secure the end cap onto the controller by pushing the locking mechanism to the left.

<!-- image -->

If you're using local expansion modules, see Chapter 8, page 172 for more information on how to install them in a CompactLogix 5370 L2 control system.

## Remove and Replace the Removable Terminal Block

To remove the RTB, loosen the upper and lower retaining screws. The terminal block backs away from the module as you remove the screws. When replacing the terminal block, torque the retaining screws to 0.46 N·m (4.1 lb·in).

<!-- image -->

| Item Description              |
|-------------------------------|
| 1 Wiring the fingersafe cover |
| 2 Lower retaining screws      |
| 3 Upper retaining screws      |

## Wire the Terminal Block

When wiring the terminal block, keep the fingersafe cover in place.

1. Loosen the retaining screws to be wired.
2. Route the wire under the terminal pressure plate.

You can use the bare wire or a spade lug. The terminals accept a 6.35 mm (0.25 in.) spade lug.

<!-- image -->

The retaining screws are non-captive. You can use a ring lug [maximum 6.35 mm (0.25 in.) o.d. with a 3.53 mm (0.139 in.) minimum i.d. (M3.5)] with the module.

3. Tighten the retaining screw and make sure that the pressure plate secures the wire. Recommended torque when you tighten the retaining screws is 0.68 N·m (6 lb·in).

<!-- image -->

If you must remove the fingersafe cover, insert a screwdriver into one of the square wiring holes and gently pry the cover off. If you wire the terminal block with the fingersafe cover removed, you can't put it back on the terminal block because of wires in the way.

## Wire Size and Terminal Screw Torque

Each terminal accepts one or two wires with these restrictions:

| Wire Type   | Wire Size Terminal Screw Torque Retaining Screw Torque                         |
|-------------|--------------------------------------------------------------------------------|
| Solid       | Cu-90 °C (194 °F) #14…#22 AWG 0.68 N•m (6 lb•in) 0.46 N•m (4.1 lb•in)          |
|             | Stranded Cu-90 °C (194 °F) #16…#22 AWG 0.68 N•m (6 lb•in) 0.46 N•m (4.1 lb•in) |

## Connect Power to the Control System

You must connect an external Class 2 or SELV-listed power supply to the embedded power supply of the controller. The external power supply converts 115/230V AC power to 24V DC power.

<!-- image -->

WARNING: Do not connect directly to line voltage. Line voltage must be supplied by a suitable, approved isolating transformer or power supply having short circuit capacity not exceeding 100VA maximum or equivalent.

Consider these points before completing the steps in this section:

- This section describes how to connect power only to the embedded power supply of the CompactLogix 5370 L2 controller.

For information on how to wire the embedded I/O module available on CompactLogix 5370 L2 controllers, see Chapter 8, page 145 .

- Not all Class 2 or SELV-listed power supplies are certified for use in all applications, for example, use in nonhazardous and hazardous environments.
- Before installing an external power supply, consult all specification and certification information to verify that you're using an acceptable external power supply.
- This section describes how to wire terminals +24V DC and COM on the CompactLogix 5370 L2 controller. They're the only terminals you wire to power the CompactLogix 5370 L2 control system.

Use only the FG terminal when connecting a field device to the controller.

For example purposes, this section uses a 1606-XLDNET4, standard switched-mode power supply.

IMPORTANT

The 1606-XLDNET4 power supply isn't certified for use in all applications, for example, you can't use it in hazardous locations.

Complete these steps to connect power to the CompactLogix 5370 L2 control system.

1. Verify that the external 24V DC power source isn't powered.
2. Mount the external 24V DC power source on a DIN rail.
3. The external 24V DC power source can be installed on the same DIN rail as the controller or a separate DIN rail.
3. Connect the wires to the 24V DC+ and 24V DC- connections on the external 24V DC power source.

<!-- image -->

WARNING: If you connect or disconnect wiring while the field-side power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

4. Strip 8 mm (0.31 in.) insulation from the end of the wire that you connect to the +24V DC terminal on the controller.

5. Connect the wire from the 24V DC+ terminal on the external 24V DC power source to the +24V DC terminal on the controller.
6. Strip 8 mm (0.31 in.) insulation from the end of the wire that you connect to the COM terminal on the controller.
7. Connect the wire from the 24V DC- terminal on the external 24V DC power source to the COM terminal on the controller.

<!-- image -->

<!-- image -->

## IMPORTANT

If your application requires a power control device, for example, a switch or relay, between the external power supply and the embedded power supply of the CompactLogix 5370 L2 controller to control when the controller is powered, you must install the power control device at the +24V DC terminal on the controller.

If you install the power control device at the COM terminal, the CompactLogix 5370 L2 controller can't power up or power down properly.

This graphic shows an external 24V DC power source that is connected to a CompactLogix 5370 L2 controller.

<!-- image -->

## IMPORTANT

When you remove power from the CompactLogix 5370 L2 controller to cycle power, the OK status indicator of the controller remains lit briefly as the controller passes through its shutdown sequence.

Do not reapply power from the external power supply to the embedded power supply of the CompactLogix 5370 L2 controller until after the OK status indicator of the controller is off.

<!-- image -->

CompactLogix 5370 Controllers have an embedded, battery-less Energy Storage Module (ESM) that provides power to the CPU upon power-down, allowing the controller to write customer application and tag data to the onboard nonvolatile memory. In some cases, the ESM continues to provide enough power to keep the wall clock active until its residual stored energy is depleted.

## Connect to the Controller Via a USB Cable

The controller has a USB port that uses a Type B receptacle. The port is USB 2.0-compatible and operates at 12 Mbps.

Use a USB cable to connect your computer to the USB port. With this connection, you can update firmware and download programs to the controller directly from your computer.

<!-- image -->

<!-- image -->

ATTENTION: The USB port is intended only for temporary local programming purposes and not intended for permanent connection.

The USB cable isn't to exceed 3.0 m (9.84 ft) and must not contain hubs.

WARNING: Do not use the USB port in hazardous locations.

Plug the USB cable into the CompactLogix 5370 L2 controller.

<!-- image -->

## Connect the Controller to an EtherNet/IP Network

<!-- image -->

WARNING: If you connect or disconnect the communication cable with power that is applied to this module or any device on the network, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Connect the RJ45 connector of the Ethernet cable to one of the Ethernet ports on the controller. The ports are on the bottom of the controller.

<!-- image -->

ATTENTION: Do not plug a DH-485 network cable or a NAP cable into the Ethernet port. Undesirable behavior and/or damage to the port can result.

<!-- image -->

## IMPORTANT

This example shows how to connect the controller to the network through one port. Depending on the network topology of your application, you can connect both ports of the controller to the EtherNet/IP™ network.

## Connecting to Different EtherNet/IP Network Topologies

CompactLogix 5370 L2 controllers have embedded switch technology and two EtherNet/IP ports that let you use it in various EtherNet/IP network topologies:

- Device Level Ring network topology - Both ports on the controller are connected to the network.
- Linear network topology - Both ports on the controller are connected to the network.
- Star network topology - One port on the controller is connected to the network.

There are connection and configuration requirements for each EtherNet/IP network topology.

For more information about EtherNet/IP Network Topologies, see Chapter 6, page 104 .

## Environment and Enclosure

<!-- image -->

ATTENTION: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II

applications (as defined in EN/IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment isn't intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure-type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 for more installation requirements.
- NEMA 250 and EN IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosure.

## North American Hazardous Location Approval

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |

<!-- image -->

<!-- image -->

| WARNING: EXPLOSION HAZARD - • Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. • Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. • Substitution of components may impair suitability for Class I, Division 2.   | WARNING: RISQUE D’EXPLOSION - • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. • La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

## Install the CompactLogix 5370 L3 Controller

## UK and European Hazardous Location Approval

The following applies to products marked II 3 G. Such products:

- Are Equipment Group II, Equipment Category 3, and comply with the Essential Health and Safety Requirements relating to the design and construction of such equipment given in Schedule 1 of UKEX Regulation 2016 No. 1107 and Annex II to EU Directive 2014/34/EU. See the UKEx and EU Declaration of Conformity at rok.auto/certifications for details.
- Provides protection type II 3 G Ex ec IIC T5 Gc according to EN 60079-7.
- Comply to Standards: EN IEC 60079-0:2018, EN IEC 60079-7:2015+A1:2018 reference certificate number UL 21 ATEX 2603X and UL22UKEX2515X.
- Are intended for use in areas in which explosive atmospheres caused by gases, vapors, mists, or air are unlikely to occur, or are likely to occur only infrequently and for short periods. Such locations correspond to Zone 2 classification according to UKEX regulation 2016 No. 1107 and ATEX directive 2014/34/EU.

## Special Considerations for Safe Use

<!-- image -->

## WARNING:

- The equipment shall be mounted in an UKEX/ATEX Zone 2 certified enclosure with a minimum ingress protection rating of at least IP54 (in accordance with EN 60079-0) and used in an environment of not more than Pollution Degree 2 (as defined in EN 60664-1). The enclosure must be accessible only by the use of a tool.
- This equipment must be used within its specified ratings that are defined by Rockwell Automation.
- Provisions shall be made to prevent the rated voltage from being exceeded by transient disturbances of more than 140% of the peak rated voltage when applied in Zone 2 environments.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Enclosure must be marked with the following: "Warning - Do not open when energized." After installation of equipment into the enclosure, access to termination compartments must be dimensioned so that conductors can be readily connected.
- The instructions in the user manual shall be observed.
- This equipment must be used only with UKEX/ATEX certified Rockwell Automation backplanes.
- Earthing is accomplished through mounting of modules on rail.
- Devices shall be used in an environment of not more than Pollution Degree 2.
- This equipment isn't resistant to sunlight or other sources of UV radiation.

## Prevent Electrostatic Discharge

<!-- image -->

## ATTENTION:

- This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:
- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## Before You Begin

Consider these details when planning your CompactLogix™ 5370 L3 control system:

- The controller is the leftmost device in the system.
- Only one controller can be used on a local 1769 CompactBus. The controller supports the local bank and up to two more banks.
- The controller has a power supply distance rating of four. This rating means that the controller must be within four slots of the power supply. You can install as many as three modules between the power supply and the controller, as shown in this graphic.
- The controllers support this many local expansion modules across multiple I/O banks.

<!-- image -->

## Number of Local Expansion Modules Supported Across Multiple I/O Banks

| Cat. No.                                                       | Local Expansion Modules Supported, Max   |
|----------------------------------------------------------------|------------------------------------------|
| 1769-L30ER 1769-L30ERK 1769-L30ERM 1769-L30ERMK 1769-L30ER-NSE | 8                                        |
| 1769-L33ER 1769-L33ERK 1769-L33ERM 1769-L33ERMK                | 16                                       |
| 1769-L33ERMO                                                   | —                                        |
| 1769-L36ERM                                                    | 30                                       |
| 1769-L36ERMO                                                   | —                                        |
| 1769-L37ERM, 1769-L37ERMK 31                                   |                                          |
| 1769-L37ERMO(1)                                                | —                                        |
| 1769-L38ERM, 1769-L38ERMK 31                                   |                                          |
| 1769-L38ERMO(1)                                                | —                                        |

- Each I/O bank requires its own power supply.
- You must terminate the end of the last bank in a CompactLogix 5370 L3 control system. You can terminate a bank at the left or right end of the bank dependent upon your system design.

A 1769-ECx end cap is required to terminate the end of the last bank in the control system.

For example, if a CompactLogix 5370 L3 control system uses one bank, you must use a 1769-ECR/1769-ECRK right end cap to terminate the right end of the bank.

For graphics of CompactLogix 5370 L3 control systems that use one bank or multiple banks, see page 66 .

<!-- image -->

ATTENTION: The CompactLogix 5370 L3 control systems do not support removal and insertion under power (RIUP). These events occur while the CompactLogix system is under power:

- Any break in the connection between the power supply and the controller, for example, removing the power supply, controller, or an I/ O module, can subject the logic circuitry to transient conditions above the normal design thresholds and can result in damage to system components or unexpected behavior.
- Removing an end cap or an I/O module faults the controller and can also result in damage to system components.

## CompactLogix 5370 L3 Controller Parts

These parts are included in the box when you order your controller:

- Controller - Specific catalog number varies by order
- 1784-SD1 Secure Digital (SD) card with 1 GB of memory storage A 1784-SD2 SD card with 2 GB of memory storage, or more 1784-SD1 SD cards, are also available if you need more memory.

## IMPORTANT

The life expectancy of nonvolatile media is dependent on the number of write cycles that are performed. Nonvolatile media use a wear leveling technique or technology for prolonging the service life, but avoid frequent writes.

Avoid frequent writes when logging data. We recommend that you log data to a buffer in the memory of your controller and limit the number of times data is written to removable media.

## Install the Secure Digital Card

The CompactLogix 5370 L3 controllers ship from the factory with the 1784-SD1 SD card installed.

Complete these steps to reinstall an SD card that has been removed from the controller back into the controller or to install a new SD card into the controller.

## IMPORTANT

For more information on how to access the SD card in a 1769-L33ERMO, 1769-L36ERMO, 1769-L37ERMO (1) , or 1769-L38ERMO (1) ) controller, see the Armor™ CompactLogix Controllers Installation Instructions, publication 1769-IN021 .

(1) Available at software version 31 and firmware revision 31.

We recommend that you leave the SD card in the controller, even when it isn't used. If the controller experiences a Major Non-recoverable Fault, extended fault information is saved to the card.

<!-- image -->

WARNING: When you insert or remove the Secure Digital (SD) Card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

1. Verify that the SD card is locked or unlocked according to your preference. Consider the following when deciding to lock the card before installation:
- If the card is unlocked, the controller can write data to it or read data from it.

Unlocked

<!-- image -->

2. Open the door for the SD card.

<!-- image -->

Locked

<!-- image -->

3. Insert the SD card into the SD card slot.

You can install the SD card in only one orientation. The beveled corner is at the top. An orientation logo is printed on the card.

If you feel resistance when inserting the SD card, pull it out and change the orientation.

4. Gently press the card until it clicks into place.
5. Close the SD card door.

<!-- image -->

<!-- image -->

We recommend that you keep the SD card door closed during normal system operation. For more information on how to use the SD card, see Chapter 12, page 241 .

## Install the System

Complete these steps to install the CompactLogix 5370 L3 control system.

## Assemble the System

IMPORTANT

For more information on how to install a 1769-L33ERMO, 1769-L36ERMO, 1769-L37ERMO(1), or 1769-L38ERMO(1) controller, see the Armor CompactLogix Controllers Installation Instructions, publication 1769-IN021 .

(1) Available at software version 31 and firmware revision 31.

You can attach an adjacent Compact I/O module or 1769 Compact I/O power supply to a CompactLogix 5370 L3 controller before or after mounting. For mounting instructions, see page 66 or page 69.

<!-- image -->

ATTENTION: Do not remove or replace this module while power is applied. Interruption of the backplane can result in unintentional operation or machine motion.

<!-- image -->

WARNING: Remove power before removing or inserting this module. If you insert or remove the module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Complete these steps to install the controller. This example describes how to attach a 1769 Compact I/O power supply to the controller.

1. Verify that line power is disconnected.
2. Make sure that the bus lever of the 1769 Compact I/O power supply is in the unlocked position. The bus lever leans to the right in the unlocked position.

<!-- image -->

3. Use the upper and lower tongue-and-groove slots to secure the controller and power supply together.
4. Move the power supply back along the tongue-and-groove slots until the bus connectors align with each other.
5. Use your fingers or a small screwdriver to push the bus lever of the power supply back slightly to clear the positioning tab.
6. Move the bus lever of the power supply fully to the left until it clicks, which makes sure that it locks.
7. If your system does not use any local expansion modules, use the tongue-and-groove slots that were previously described to attach a 1769-ECR Compact I/O end cap terminator to the last module in the system.

<!-- image -->

<!-- image -->

IMPORTANT

You must install an end cap onto the right side of the CompactLogix 5370 L3 controller system either at the end of the controller. You must also install an end cap at the end of any local expansion modules that can be installed onto the controller.

8. Wire the 1769 Compact I/O power supply according to the directions in the Compact I/O Expansion Power Supplies installation instructions, publication 1769-IN028 . If you're using local expansion modules, see Chapter 9, page 189 .

## Remove and Replace the Removable Terminal Block

To remove the terminal block, loosen the upper and lower retaining screws. The terminal block backs away from the module as you remove the screws. When replacing the terminal block, torque the retaining screws to 0.46 N·m (4.1 lb·in).

<!-- image -->

.

| Item Description                       |
|----------------------------------------|
| 1 Wiring the fingersafe terminal block |
| 2 Lower retaining screws               |
| 3 Upper retaining screws               |

## Wire the Terminal Block

When wiring the terminal block, keep the fingersafe cover in place.

1. Loosen the terminal screws to be wired.
2. Route the wire under the terminal pressure plate.
3. You can use the bare wire or a spade lug. The terminals accept a 6.35 mm (0.25 in.) spade lug.

<!-- image -->

The terminal screws are non-captive. You can use a ring lug [maximum 6.35 mm (0.25 in.) o.d. with a 3.53 mm (0.139 in.) minimum i.d. (M3.5)] with the module.

3. Tighten the terminal screw and make sure that the pressure plate secures the wire. Recommended torque when you tighten the terminal screws is 0.68 N·m (6 lb·in).

<!-- image -->

If you must remove the fingersafe cover, insert a screwdriver into one of the square wiring holes and gently pry the cover off. If you wire the terminal block with the fingersafe cover removed, you can't put it back on the terminal block because of wires in the way.

## Wire Size and Terminal Screw Torque

Each terminal accepts one or two wires with the following restrictions.

| Wire Type   | Wire Size Terminal Screw Torque Retaining Screw Torque                         |
|-------------|--------------------------------------------------------------------------------|
| Solid       | Cu-90 °C (194 °F) #14…#22 AWG 0.68 N•m (6 lb•in) 0.46 N•m (4.1 lb•in)          |
|             | Stranded Cu-90 °C (194 °F) #16…#22 AWG 0.68 N•m (6 lb•in) 0.46 N•m (4.1 lb•in) |

## Horizontal Orientation

## Mount the System

You can mount a CompactLogix 5370 L3 control system on a DIN rail or on a panel.

<!-- image -->

ATTENTION: During panel or DIN rail mounting of all devices, be sure that all debris (such as metal chips or wire strands) is kept from falling into the controller. Debris that falls into the controller could cause damage while the controller is energized.

A CompactLogix 5370 L3 control system must be mounted so that the modules are horizontal to each other. If you separate modules into multiple banks, the banks can be vertical or horizontal to each other.

Example CompactLogix 5370 L3 Control Systems with Local Expansion Modules Installed

<!-- image -->

Bank 1

Bank 2

Before you mount a CompactLogix 5370 L3 control system, consider these requirements.

Minimum Spacing

Maintain spacing from enclosure walls, wireways, and adjacent equipment. Allow 50 mm (2 in.) of space on all sides, as shown. This spacing provides ventilation and electrical isolation.

## Vertical Orientation

1769-CRRx Cable

<!-- image -->

## System Dimensions

This graphic shows the system dimensions.

<!-- image -->

<!-- image -->

## Power Supply Distance Rating

CompactLogix 5370 L3 controllers and the Compact I/O modules have power supply distance ratings. Power supply distance ratings determine how many slots in a bank that a device can be from the power supply.

For example, a product with a power supply distance rating of four can only have up to three slots between it and the power supply.

| Device                                                              | Power Supply Distance Rating                                                                                                                                            |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CompactLogix 5370 L3 controller 1769 Compact I/O DeviceNet® scanner | 4                                                                                                                                                                       |
| Compact I/O module                                                  | 4…8, depending on module For more information about the power supply distance rating for a Compact I/O module, see CompactLogix Selection Guide, publication 1769-SG001 |

CompactLogix 5370 L3 controllers must be the leftmost device in the control system, and the system only enables up to three modules between the controller and the power supply. This graphic shows an example configuration.

<!-- image -->

## Ground the System

<!-- image -->

ATTENTION: This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the power supply's mounting tabs or DIN rail (if used) aren't required unless the mounting surface can't be grounded. See Industrial Automation Wiring and Grounding Guidelines, Rockwell

Automation publication 1770-4.1, for additional information.

Mount the Controller on a Panel

Use two M4 or #8 pan head screws to mount the controller. Mounting screws are required on many modules. Use the assembled modules as a template to drill holes in the panel, as follows:

IMPORTANT

Due to module mounting hole tolerance, it's important to follow this procedure.

1. On a clean work surface, assemble no more than three modules.
2. Use the assembled modules as a template and carefully mark the center of all modulemounting holes on the panel.
3. Return the assembled modules to the clean work surface, including any previously mounted modules.
4. Drill and tap the mounting holes for the recommended M4 or #8 screw.
5. Place the modules back on the panel and check for proper hole alignment.

<!-- image -->

The grounding plate, that is, where you install the mounting screws, grounds the module when it's panel-mounted.

6. Use the mounting screws to attach the modules to the panel.

<!-- image -->

If you're mounting more modules, mount only the last one of this group and put the others aside. This process reduces remounting time when you are drilling and tapping the next group of modules.

7. Repeat steps 1 … 6 for any remaining modules.

Mount the Controller on the DIN Rail

You can mount the controller on these DIN rails:

- EN 50 022 - 35 x 7.5 mm (1.38 x 0.30 in.)
- EN 50 022 - 35 x 15 mm (1.38 x 0.59 in.)

<!-- image -->

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc-plated chromate-passivated steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum or plastic) that can corrode, oxidize, or you're poor conductors, can result in improper or intermittent grounding. Secure DIN rail to a mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately. Be sure to ground the DIN rail properly. Refer to Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for more information.

1. Before mounting the controller on a DIN rail, close the DIN rail latches of the controller.
2. Press the DIN rail mounting area of the controller against the DIN rail.

The latches momentarily open and lock into place.

## Connect Power to the Control System

Connect power to the CompactLogix 5370 L3 control system that is based on the 1769 Compact I/O power supply your application uses. For more information on how to connect power to your CompactLogix 5370 L3 control system, see the Compact I/O Expansion Power Supplies Installation Instructions, publication 1769-IN028 .

<!-- image -->

CompactLogix 5370 Controllers have an embedded, battery-less Energy Storage Module (ESM) that provides power to the CPU upon power-down, allowing the controller to write customer application and tag data to the onboard nonvolatile memory. In some cases, the ESM continues to provide enough power to keep the wall clock active until its residual stored energy is depleted.

## Connect to the Controller Via a USB Cable

The controller has a USB port that uses a Type B receptacle. The port is USB 2.0-compatible and operates at 12 Mbps.

Use a USB cable to connect your computer to the USB port. With this connection, you can update firmware and download programs to the controller directly from your computer.

<!-- image -->

ATTENTION: The USB port is intended only for temporary local programming purposes and not intended for permanent connection. The USB cable isn't to exceed 3.0 m (9.84 ft) and must not contain hubs.

<!-- image -->

WARNING: Do not use the USB port in hazardous locations.

## IMPORTANT

For more information on how to connect a USB cable to a 1769L33ERMO, 1769-L36ERMO, 1769-L37ERMO (1) , 1769-L38ERMO (1) ) controller, see the Armor CompactLogix Controllers Installation Instructions, publication 1769-IN021 .

(1) Available at software version 31 and firmware revision 31.

Plug the USB cable into the CompactLogix 5370 L3 controller as shown.

<!-- image -->

## Connect the Controller to an EtherNet/IP Network

<!-- image -->

WARNING: If you connect or disconnect the communication cable with power that is applied to this module or any device on the network, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Connect the RJ45 connector of the Ethernet cable to one of the Ethernet ports on the controller. The ports are on the bottom of the controller.

<!-- image -->

ATTENTION: Do not plug a DH-485 network cable or a NAP cable into the Ethernet port. Undesirable behavior or damage to the port can result.

<!-- image -->

## IMPORTANT

This example shows how to connect the controller to the network through one port. Depending on the Ethernet network topology of your application, you can connect both ports of the controller to the EtherNet/IP™ network.

## Connecting to Different EtherNet/IP Network Topologies

The CompactLogix 5370 L3 controllers have embedded switch technology and two EtherNet/IP ports that let you use it in different EtherNet/IP network topologies:

- Device Level Ring network topology - Both ports on the controller are connected to the network with requirements about how the connections are made.
- Linear network topology - Both ports on the controller are connected to the network with requirements about how the connections are made.
- Star network topology - One port on the controller is connected to the network.

For more information, see Chapter 6, page 99 .

<!-- image -->

## Complete Software Tasks Required at CompactLogix 5370 Controller Installation

To complete the tasks that are described in this chapter, you must have the software that is described in the following table installed on your computer.

| Software                    | Required Version                                                                                                                                                                                                            |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RSLinx® Classic             | 2.59.00 or later CompactLogix™ 5370 L2 controllers require RSLinx Classic software, version 2.59.01 or later. The 1769-L19ER-BB1B controller requires RSLinx Classic software, version 3.74.00                              |
| RSLogix 5000®               | 20 - For CompactLogix 5370 controllers using firmware revision 20. RSLogix 5000 software does not support the 1769-L19ER-BB1B controller.                                                                                   |
| Studio 5000 Logix Designer® | 21 or later - For CompactLogix 5370 controllers using firmware revision 21 or later. 28 or later - For the 1769-L19ER-BB1B controller.                                                                                      |
| BOOTP-DHCP server           | Most current version is installed with RSLinx Classic software installation                                                                                                                                                 |
| ControlFLASH™               | Installed with the installation of one of the following: • RSLogix 5000 software, version 20 • Studio 5000® environment, version 21 or later • Studio 5000 environment, version 28 or later for 1769-L19ER-BB1B controllers |

CompactLogix 5370 controllers require a network Internet Protocol (IP) address to operate on an EtherNet/IP™ network.

The IP address uniquely identifies the controller. The IP address is in the form xxx.xxx.xxx.xxx where each xxx is a number from 000 … 254 with some exceptions for reserved values. These numbers are examples of reserved values that you can't use:

- 000.xxx . xxx . xxx
- 127.xxx . xxx . xxx
- 224 to 255.xxx . xxx . xxx

Some other values are reserved based on an application-by-application basis.

You can complete one of these tasks dependent on system conditions:

- Set the IP address for a controller that does not have one assigned.
- Change the IP address for a controller that has an IP address that is assigned to it.

## IMPORTANT

CompactLogix 5370 controllers have two EtherNet/IP ports to connect to an EtherNet/IP network. The ports carry the same network traffic as part of the embedded switch of the controller. However, the controller uses only one IP address.

## Set the IP Address of a Controller

You must set the IP address of a CompactLogix 5370 controller when the controller powers up for the first time, that is, when commissioning the controller for the first time. You aren't required to set an IP address each time the controller cycles power.

You can use these tools to set the IP address of a CompactLogix 5370 controller:

- Bootstrap Protocol (BOOTP) server
- Dynamic Host Configuration Protocol (DHCP) server
- RSLinx Classic software
- Studio 5000 Logix Designer® application
- SD card

## IMPORTANT

Each tool has connection requirements to set the IP address of the controller via that tool. For example, your computer must be connected to the controller via a USB cable to set the initial IP address of the controller with RSLinx Classic software or the application.

This figure describes how to set the IP address of your CompactLogix 5370 controller on a power cycle during initial installation or after operation has begun.

<!-- image -->

## Use the BOOTP Server to Set the IP Address of the Controller

Bootstrap Protocol (BOOTP) is a protocol that enables the controller to communicate with a BOOTP server. The server can be used to assign an IP address. You can use the BOOTP server to set an IP address for your CompactLogix 5370 controller.

Consider these points when using the BOOTP server:

- The BOOTP server is installed automatically when you install RSLinx Classic software or the Studio 5000 environment on your computer. The BOOTP server sets an IP address and other Transmission Control Protocol (TCP) parameters.
- A CompactLogix 5370 controller ships from the factory without an IP address and BOOTP-enabled.
- This section describes how to use a Rockwell Automation® BOOTP/DHCP server. If you use another BOOTP/DHCP server, contact your network administrator to verify that you're using it correctly.
- To use the BOOTP server, your computer and the controller must be connected to the same EtherNet/IP network.
- If the controller is BOOTP-disabled, you can't use the BOOTP server to set the IP address.

There are two conditions in which the CompactLogix 5370 controllers use the BOOTP servers to set the IP address of the controller:

- Initial powerup - Because the CompactLogix 5370 controller ships with BOOTPenabled, when it is first powered up, the controller sends a request for an IP address on the EtherNet/IP network. You can use the BOOTP server to set the IP address, as described later in this section.
- Powerup after controller operation has begun - When controller power is cycled after operation has begun, the BOOTP/DHCP server sets the IP address if one of these conditions exists:
- Controller is BOOTP-enabled - You set the IP address manually with the BOOTP server.
- Controller is DHCP-enabled - The IP address is set automatically via the DHCP server.

Access the BOOTP/DHCP utility from one of these locations:

- Start&gt;Programs&gt;Rockwell Software&gt;BOOTP-DHCP Server If you haven't installed the utility, you can download and install it from rok.auto/ certifications .
- Tools directory on the programming software installation CD

## IMPORTANT

1769-L18ERM-BB1B Controller

<!-- image -->

Before you start the BOOTP/DHCP utility, make sure that you have the hardware (MAC) address of the controller. The hardware address is on the front of the controller and uses an address in a format similar to the following: 00:00:BC:2E:69:F6

## Example Locations of Controller Hardware Address

1769-L24ER-QB1B Controller

<!-- image -->

Complete these steps to set the IP address of the controller with the BOOTP/DHCP server.

## IMPORTANT

To use the BOOTP server, your computer and the controller must be connected to the same EtherNet/IP network.

1. Start the BOOTP/DHCP software.
2. From the Tools menu, select Network Settings.

<!-- image -->

1769-L33ER Controller

<!-- image -->

3. Enter the Subnet Mask of the network.

<!-- image -->

The Gateway address, Primary or Secondary DNS address, and Domain Name fields are optional.

4. Select OK.

The Request History panel appears with the hardware addresses of all devices that issue BOOTP requests. This process can take some time to complete.

5. Select the appropriate module.
6. Select Add to Relation List.

<!-- image -->

<!-- image -->

The New Entry dialog box appears.

7. Enter an IP Address, Hostname, and Description for the controller.
8. Select OK.
9. To assign this configuration to the controller, wait for the controller to appear in the Relation List panel and select it.

<!-- image -->

## 10. Select Disable BOOTP/DHCP.

<!-- image -->

When power is cycled, the controller uses the assigned configuration and does not issue a BOOTP request.

## IMPORTANT

If you do not select Disable BOOTP/DHCP on a power cycle, the host controller clears the current IP configuration and begins sending BOOTP requests again.

If you select Disable BOOTP/DHCP and it does not disable BOOTP/DHCP, use RSLinx Classic software or the Studio 5000 environment to disable BOOTP/DHCP.

To disable BOOTP/DHCP from RSLinx Classic software, perform the following:

1. Make sure that a USB cable is connected to your computer and the controller.
2. Start RSLinx Classic software.
3. After several seconds, an RSWho dialog box appears.
3. If no RSWho dialog box appears, from the Communications pull-down menu, select RSWho.
4. Navigate to the USB network.
5. Right-click on the controller and select Module Configuration.

<!-- image -->

<!-- image -->

6. Select the Port Configuration tab.
7. From the Network Configuration Type, select Static to disable BOOTP/DHCP.
8. Select OK.

<!-- image -->

To disable BOOTP/DHCP from the Studio 5000 environment, perform the following:

1. Start the application.
2. Open the project.
3. Right-click on the controller and select Properties.
4. On the Controller Properties dialog box, select the Internet Protocol tab.
5. Select Manually configure IP settings.
6. Select OK.
7. When prompted to confirm the IP address setting, select Yes.

<!-- image -->

<!-- image -->

## Using DHCP Software

Dynamic Host Configuration Protocol (DHCP) software automatically assigns IP addresses to client stations logging on to a TCP/IP network. DHCP is based on BOOTP and maintains some backward compatibility. The main difference is that BOOTP allows for manual configuration (static), while DHCP allows for both static and dynamic allocation of network addresses and configurations to newly attached modules.

Be cautious when using DHCP software to configure a module. A BOOTP client, such as the EtherNet/IP communication modules, can start from a DHCP server only if the DHCP server is written to handle BOOTP queries. This requirement is specific to the DHCP software package used. Consult your system administrator to see if a DHCP package supports BOOTP commands and manual IP allocation.

<!-- image -->

ATTENTION: The EtherNet/IP communication module must be assigned a fixed network address. The IP address of this module must not be dynamically provided.

Failure to observe this precaution may result in unintended machine motion or loss of process control.

## Use the DHCP Server to Set the IP Address of the Controller

Dynamic Host Configuration Protocol (DHCP) server automatically assigns IP addresses to client stations logging on to a TCP/IP network. DHCP is based on BOOTP and maintains some backward compatibility. The main difference is that BOOTP manual configuration (static), while DHCP enables static and dynamic allocation of network addresses and configurations to newly attached controllers.

Be cautious when using the DHCP server to configure a controller. A BOOTP client, such as the CompactLogix 5370 controllers, can start from a DHCP server only if the DHCP server is written to handle BOOTP queries. This requirement is specific to the DHCP server used. Consult your system administrator to see if a DHCP server supports BOOTP commands and manual IP allocation.

<!-- image -->

ATTENTION: Assign the CompactLogix 5370 controllers a fixed network address. The IP address of this controller isn't to be dynamically provided. Failure to observe this precaution can result in unintended machine motion or loss of process control.

If you use the Rockwell Automation BOOTP or DHCP server in an uplinked subnet where a DHCP server exists, a controller can procure an address from the enterprise server before the Rockwell Automation utility even sees the controller. Disconnect from the uplink to set the address and configure the controller to retain its static address before reconnecting to the uplink, if necessary.

## Use RSLinx Classic Software to Set the Controller IP Address

You can use RSLinx Classic software to set the IP address of the CompactLogix 5370 controller.

IMPORTANT

To set the IP address, that is, assign an IP address to a controller that does not have one, for a CompactLogix 5370 controller via RSLinx Classic software, you must be connected to your controller via the USB port.

Complete these steps to set the IP address of the controller with RSLinx Classic software.

IMPORTANT These steps show a 1769-L36ERM controller. The same steps also apply to all CompactLogix 5370 controllers with slight variations in screens.

1. Make sure that a USB cable is connected to your computer and the controller.
2. Start RSLinx Classic software.

After several seconds, an RSWho dialog box appears.

3. If no RSWho dialog box appears, from the Communications pull-down menu, select RSWho.

<!-- image -->

The RSWho dialog box appears and includes the USB driver.

4. Right-click the EtherNet/IP module and select Module Configuration.

<!-- image -->

The Module Configuration dialog box appears.

5. Select the Port Configuration tab.

<!-- image -->

6. For Network Configuration Type, select Static to assign this configuration to the port.

IMPORTANT If you select Dynamic, on a power cycle, the controller clears the current IP configuration and starts to send BOOTP requests.

7. Enter the new IP address and Network Mask.
8. Select OK.

As with all configuration changes, if desired, make sure that you're using the SD card in a way that does not overwrite the IP address at the next controller power cycle.

For more information on how to use the SD card, see Chapter 12, page 241 .

## Use the Logix Designer Application to Set the IP Address of the Controller

You can use Logix Designer application to set the IP address of a CompactLogix 5370 controller. To set the IP address via the application, you must be connected to your controller via the USB port.

Complete these steps to set the IP address of the controller.

## IMPORTANT

These steps show a 1769-L18ERM-BB1B controller. The same steps also apply to all CompactLogix 5370 controllers with slight variations in screens.

1. Start the application.
2. Set the Project Path.
- a. Select RSWho.

<!-- image -->

The RSWho dialog box appears.

- b. Navigate over the USB network and select the CompactLogix 5370 controller.
- c. Select Set Project Path.

<!-- image -->

3. Select Download.
4. Select Download again.

<!-- image -->

<!-- image -->

The new project is downloaded to the controller and the project goes online, in Remote Program or Program mode.

5. Right-click the controller name and select Properties.

<!-- image -->

6. On the Controller Properties dialog box, select the Internet Protocol tab. The IP Settings Configuration values show that the controller has no IP address that is assigned to it.
7. Select Manually configure IP settings.
8. Enter desired IP address and other configuration information and select OK.
9. When prompted to confirm the IP address setting, select Yes.

<!-- image -->

<!-- image -->

<!-- image -->

The controller now uses the newly set IP address.

## Use the SD Card to Set the IP Address of the Controller

You can use an SD card to set the IP address for a CompactLogix 5370 controller. If you use the SD card to set the IP address, it eliminates the need for software to complete this task.

## IMPORTANT

To set the IP address from an SD card, software isn't required during the power-up process. However, you must have previously saved the project to the SD card.

The IP address of the CompactLogix 5370 controller is automatically configured at power-up as long as you've configured an IP address, stored the program onto a controller, and set the SD card to the Load Image parameter set to On Power Up.

The option to set the IP address of a CompactLogix 5370 controller via an SD card at power-up is only one part of the process to load an entire project to the controller from the SD card.

Use this option carefully. For example, the SD card can contain a desirable IP address as part of an undesirable project, for example, a project that is older than the project currently used on the controller.

These requirements apply when using the SD card to set the IP address on a CompactLogix 5370 controller:

- A project must be stored on the SD card.
- The project that is stored on the SD card is configured with the Load Image parameter set to On Power Up.

For more information on how to use the SD card, see Chapter 12, page 241 .

## Change the IP Address of a Controller

You can change the IP address of a CompactLogix 5370 controller after system operation has begun. In this case, the controller has an IP address that is assigned to it, but you must change that IP address.

You can use these tools to change the IP address of a controller:

- RSLinx Classic software
- Studio 5000 Logix Designer application
- SD card

## IMPORTANT

You can't use any of these tools to change the IP address of a controller:

- Bootstrap Protocol (BOOTP) server
- Dynamic Host Configuration Protocol (DHCP) server

Consider these factors when you determine how to change the IP address of a controller:

- Network isolation from, or integration into, the plant/enterprise network
- Network size - For large, isolated networks, it can be more convenient and safer to use a BOOTP/DHCP server rather than the Logix Designer application or RSLinx Classic software. A BOOTP/DHCP server limits the possibility of duplicate IP address assignment.

However, you can only use the BOOTP/DHCP server to set the IP address of the controller and not to change it. If you decide to change the IP address of the controller and want to use a BOOTP/DHCP server to limit the possibility of duplicate IP address assignment, you must first clear the IP address.

After clearing the IP address, use the steps for using the BOOTP Server on page 75 or the DHCP Server on page 80 to set the IP address of the controller.

- Company policies and procedures that deal with plant floor network installation and maintenance
- Level of involvement by IT personnel in plant-floor network installation and maintenance
- Type of training that is offered to control engineers and maintenance personnel

## Change the Network IP Address with RSLinx Classic Software

## IMPORTANT

The steps on page 81 describe how to use RSLinx Classic Software to assign an IP address for a CompactLogix 5370 controller that does not have an IP address.

The steps in this section describe how to use RSLinx Classic Software to change the IP address on a CompactLogix 5370 controller that has an IP address that is assigned to it.

The graphics in this section show how to change the IP address for a 1769-L36ERM controller. The same steps also apply to all other CompactLogix 5370 controllers with slight variations in screens.

1. Right-click the controller and select Module Configuration.
2. Select the Port Configuration tab when the Module Configuration dialog box appears. The controller has an IP address and Network Configuration Type.
3. Enter a new IP address and make any other desired changes.
4. To assign this configuration to the controller, select Static in the Network Configuration Type section of the dialog box.

<!-- image -->

## IMPORTANT

If you select Dynamic, on a power cycle, the controller clears the current IP configuration and starts to send BOOTP or DHCP requests, depending on the controller configuration.

<!-- image -->

5. Select OK.

## Change the Network IP Address with Logix Designer Application

## IMPORTANT

The steps on page 82 describe how to use the Logix Designer Application to assign an IP address for a CompactLogix 5370 controller that does not have an IP address.

The steps in this section describe how to change the IP address on a CompactLogix 5370 controller that has an IP address that is assigned to it.

You can change the IP address of a CompactLogix 5370 controller via Logix Designer application over a USB or EtherNet/IP network connection.

The graphics in this section show how to change the IP address for a 1769-L18ERM-BB1B controller over a USB connection. The same steps also apply to all other CompactLogix 5370 controllers with slight variations in screens.

1. Verify that your computer is connected to the controller.
2. Verify that your project is online.
3. Right-click the controller name and select Properties.

<!-- image -->

You can also right-click the Ethernet node in the I/O Configuration section and select Properties. The Controller Properties dialog box appears on the Internet Protocol tab.

4. Change the IP address of the controller.
5. Make other changes where necessary.
6. Select OK.

<!-- image -->

## Change the Network IP Address with an SD Card

You can use an SD card to change the IP address for a CompactLogix 5370 controller when controller power is cycled. If you use the SD card to change the IP address, it removes the need for software to complete this task.

## IMPORTANT

To set the IP address from an SD card, software isn't required during the power-up process. However, you must have previously saved the project to the SD card.

These requirements apply when using the SD card to change the IP address on a CompactLogix 5370 controller:

- A project is stored on the SD card.
- The project that is stored on the SD card includes another IP address for the CompactLogix 5370 controller than the IP address currently in use on the physical controller that houses the SD card.
- The project that is stored on the SD card is configured with the Load Image parameter set to On Power Up.
- Power is cycled to the controller with the SD card installed.

For more information on how to use the SD card, see Chapter 12, page 241 .

## Load the Controller Firmware

You must download the current firmware before you can use the CompactLogix 5370 controller.

## IMPORTANT

Do not interrupt a firmware update while it is in process. Firmware update interruption can cause the firmware revision of the CompactLogix 5370 controller to revert to its out-of-the-box revision level, that is, 1.xxx.

To load the firmware, you can use any of the following:

- ControlFLASH software that installs with Logix Designer application
- AutoFlash that launches through the application when you download a project and the controller does not have the matching firmware revision
- SD card (catalog numbers 1784-SD1 or 1784-SD2) with an image stored on the card

If you use the ControlFLASH or AutoFlash utilities, you need an EtherNet/IP network or USB connection to the controller.

## IMPORTANT

The controller firmware revision that is loaded via the ControlFLASH software or the AutoFlash option can be overwritten after future controller power cycles if the conditions described on page 96 exist.

The firmware is available with the application or you can download it from the support website at rok.auto/support .

## Use the ControlFLASH Software to Load Firmware

You can use the ControlFLASH software to load firmware through a USB or EtherNet/IP network connection. We recommend the following when you load the firmware via the ControlFLASH software:

- Use a USB connection to load the firmware.
- Remove the SD card, if one is installed in the controller.

Complete these steps to use the ControlFLASH software to load the firmware.

## IMPORTANT

These steps show a 1769-L36ERM controller. The same steps also apply to all other CompactLogix 5370 controllers with slight variations in screens.

1. Verify that a connection exists between your computer and the CompactLogix 5370 controller.
2. Select Start&gt;All Programs&gt;FLASH Programming Tools&gt;ControlFLASH.

<!-- image -->

3. When the Welcome dialog box appears, select Next.
4. Select the controller catalog number and select Next.
5. Expand the network until you see the controller.
6. Select the controller at the first instance in which it appears, as shown in the following graphic, and select OK.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

If you expand the controller, that is, expand the network beyond the first instance in which it appears on the left side of the screen, you receive the following message:

The target device isn't in the proper mode to accept an update in ControlFLASH.

7. Select the revision level to which you want to update the controller and select Next.
8. To start the update of the controller, select Finish and Yes.

<!-- image -->

<!-- image -->

<!-- image -->

Before the firmware update begins, you see the following dialog box. Take the required action for your application. In this example, the update continues when OK is selected.

<!-- image -->

After the controller is updated, the status dialog box displays the message Update complete.

<!-- image -->

9. Select OK.
10. To close the ControlFLASH software, select Cancel and Yes.

Automatic Update for CompactLogix 5370 L1 Embedded I/O Module

IMPORTANT This section applies only to CompactLogix 5370 L1 controllers.

After the controller firmware update process is complete, the controller can execute a firmware update for its embedded I/O module.

Remember these points regarding the automatic firmware update for the embedded I/O module:

- The firmware update occurs on only the embedded I/O module, not the local expansion modules.

If you must update the firmware revision on any 1734 POINT I/O™ modules that are used as local expansion modules, you must do so before installing them in the CompactLogix 5370 L1 control system.

- The firmware update on the embedded I/O module occurs automatically. No user action is required.
- The update process can take a few minutes to complete.
- During the firmware update process, the OK status indicator on the controller remains in a flashing red state.
- Do not cycle power to the controller while the firmware update for the embedded I/O module is taking place.

## Use AutoFlash to Load Firmware

You can use AutoFlash to load firmware through a USB or EtherNet/IP network connection.

Let the update complete without interruption. If you interrupt a firmware update that is in process, you're alerted that an error has occurred. In this case, cycle power to the controller. The firmware revision level reverts to the 1.xxx revision level and you can begin the update process again.

Complete these steps to use the AutoFlash utility to load the firmware.

## IMPORTANT

These steps show a 1769-L36ERM controller. The same steps also apply to all CompactLogix 5370 controllers with slight variations in screens.

1. Make sure that the network connection is made and your network driver is configured in RSLinx Classic software.
2. Create a controller project.
3. To specify the controller path, select RSWho.
4. Select your controller and select Download.

<!-- image -->

<!-- image -->

You can also select to select Update Firmware to complete this process. If you do so, skip to step 6 .

A dialog box appears to indicate that the project revision and controller firmware revision are different.

5. Select Update Firmware.
6. Use the checkbox and pull-down menu to select your controller and firmware revision.
7. Select Update.
8. When the Update Firmware dialog box appears, select Yes.

<!-- image -->

<!-- image -->

<!-- image -->

Before the firmware update begins, you can be warned about your controller missing its SD card. Take the required action, typically select OK, and the firmware update will begin.

9. When the firmware update is complete, the Download dialog box appears and you can continue by downloading your project to the controller.

<!-- image -->

## Use the Secure Digital Card to Load Firmware

You can use an installed SD card to load firmware on a CompactLogix 5370 controller. If you use the SD card to load the firmware, it eliminates the need for software to complete this task.

## IMPORTANT

An installed SD card automatically updates the firmware of the controller if the SD card is configured with the Load Image parameter set to On Power Up. This feature is and can't be disabled.

Your application requires the following to load the firmware from an SD card at power-up:

- You must have saved the project to the SD card before the power cycle.
- The firmware revision in the project that is stored on the SD card differs from the firmware revision on the CompactLogix 5370 controller.

For more information on how to use the SD card, see Chapter 12, page 241 .

## Select the Operating Mode of the Controller

CompactLogix 5370 controllers have slightly different front designs and mode switch placements.

<!-- image -->

WARNING: When you change switch settings while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## Mode Switch Placement on a CompactLogix 5370 L1 Controller

<!-- image -->

## Mode Switch Placement on a CompactLogix 5370 L2 Controller

<!-- image -->

## Mode Switch Placement on a CompactLogix 5370 L3 Controller

<!-- image -->

Use the mode switch on the controller to set the operating mode of the CompactLogix 5370 controller.

| Mode Switch Position Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run                                | You can perform these tasks: • Upload projects. • Run the program and enable outputs. You can’t perform these tasks: • Update controller firmware. • Create or delete tasks, programs, or routines. • Create or delete tags or edit online. • Import a program to the controller. • Change the port configuration of the controller, advanced port configuration, nor network configuration settings. • Change controller configuration parameters that are directly set for operation on a Device Level Ring (DLR) network topology. |
| Prog                               | You can perform these tasks: • Update controller firmware. • Disable outputs. • Upload/download projects. • Create, modify, and delete tasks, programs, or routines. • Change the port configuration of the controller, advanced port configuration, nor network configuration settings. You can’t perform these tasks: • Use the controller to execute (scan) tasks.                                                                                                                                                                 |
| Rem                                | You can perform these tasks: • Upload/download projects. • Change the port configuration of the controller, advanced port configuration, nor network configuration settings. • Change between Remote Program, Remote Test, and Remote Run modes through the application.                                                                                                                                                                                                                                                              |
| Rem                                | Remote Run • Enable outputs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Rem                                | Remote Program • Create, modify, and delete tasks, programs, or routines. • Download projects.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Rem                                | Remote Test  • Execute tasks with outputs disabled. • Edit online.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## EtherNet/IP Network Communication

## Communicate Over Networks

All CompactLogix™ 5370 controllers support these tasks over an

## EtherNet/IP™ network:

- Control distributed I/O
- Send/receive messages to/from other devices on the same network or another network
- Produce/consume (interlock) data between controllers
- Socket interface

CompactLogix 5370 L2 and L3 controllers support these tasks over a

DeviceNet® network:

- Control distributed I/O
- Send messages to devices on the same network; the controller can't receive messages from other devices on the network.

All CompactLogix 5370 controllers also support temporary connections from your computer via a USB connection.

The EtherNet/IP network offers a full suite of control, configuration, and data collection services by layering the Common Industrial Protocol (CIP™) over the standard Internet protocols, such as TCP/IP and UDP. This combination of well-accepted standards provides the capability that is required to support information data exchange and control applications.

The CompactLogix 5370 controllers use socket interface transactions and conventional communication over the EtherNet/IP network to communicate with Ethernet devices that do not support the EtherNet/IP application protocol.

For more information on socket interface transactions, see page 108 .

<!-- image -->

## Available Software

Use the software listed in this table with a CompactLogix 5370 controller on an EtherNet/IP network.

| Software                                | Required Version                                                                                                                                                                               | Functions                                                                                                                                                                  | Required                                                                                           |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| RSLogix 5000                            | Version 20 - For CompactLogix 5370 controllers that are using firmware revision 20.                                                                                                            | • Configure the CompactLogix project. • Define EtherNet/IP communication. • Change IP address for devices on network, including the CompactLogix 5370 controller.          | Yes. Studio 5000 Logix Designer application, version 28 or later - For 1769-L19ER-BB1B controllers |
| Studio 5000 Logix Designer® application | Version 21 or later - For CompactLogix 5370 controllers that are using firmware revision 21 or later.  (1)                                                                                     | • Configure the CompactLogix project. • Define EtherNet/IP communication. • Change IP address for devices on network, including the CompactLogix 5370 controller.          | Yes. Studio 5000 Logix Designer application, version 28 or later - For 1769-L19ER-BB1B controllers |
| RSLinx® Classic                         | 2.59.00 or later CompactLogix 5370 L2 controllers require RSLinx Classic software, version 2.59.01 or later. The 1769-L19ER-BB1B controller requires RSLinx Classic software, version 3.74.00. | • Assign or change IP addresses to devices on an EtherNet/IP network. • Configure communication devices. • Provide diagnostics. • Establish communication between devices. | Yes. Studio 5000 Logix Designer application, version 28 or later - For 1769-L19ER-BB1B controllers |
| BOOTP/DHCP utility                      | Most current version is installed with RSLinx Classic software installation.                                                                                                                   | Assign IP addresses to devices on an EtherNet/IP network.                                                                                                                  | No                                                                                                 |

(1) If you're using the L19 you must have at a minimum, Studio 5000®, version 28. There's no version of RSLogix 5000 software, version 20, for support of the L19.

## EtherNet/IP Network Functionality

The CompactLogix 5370 controllers offer this EtherNet/IP network functionality:

- Dual built-in EtherNet/IP network ports
- Support for the following EtherNet/IP network topologies:
- Device-level Ring Network topology
- Linear Network Topology
- Star Network Topology
- Support for CIP Sync™ technology
- Support for Integrated Motion over an EtherNet/IP network - Only the following controllers support this functionality:
- 1769-L18ERM-BB1B
- 1769-L18ERM-BB1BK
- 1769-L27ERM-QBFC1B
- 1769-L30ERM
- 1769-L30ERMK
- 1769-L33ERM
- 1769-L33ERMK
- 1769-L33ERMO
- 1769-L36ERM
- 1769-L36ERMO
- 1769-L37ERM
- 1769-L37ERMK
- 1769-L37ERMO(1)
- 1769-L38ERM
- 1769-L38ERMK
- 1769-L38ERMO(1)
- Socket interface to communicate with Ethernet devices that do not support the EtherNet/IP application protocol
- Duplicate IP address detection
- Unicast and multicast communication
- Support messaging, produced/consumed tags, HMI, and distributed I/O
- Interface via RJ45, twisted-pair cables
- Support half/full-duplex 10 Mbps or 100 Mbps operation
- Support standard switches
- No network scheduling required
- No routing tables required

## Nodes on an EtherNet/IP Network

When configuring your CompactLogix 5370 control system, you must account for the number of Ethernet nodes you include in the I/O configuration section of your project. CompactLogix 5370 controllers have limits on the number of nodes that they support in the I/O configuration section.

## CompactLogix 5370 Controller Ethernet Node Guidelines

| Cat. No.                              |   Ethernet Nodes Supported |
|---------------------------------------|----------------------------|
| 1769-L16ER-BB1B                       |                          4 |
| 1769-L18ER-BB1B                       |                          8 |
| 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK   |                          8 |
| 1769-L19ER-BB1B, 1769-L19ER-BB1BK     |                          8 |
| 1769-L24ER-QB1B                       |                          8 |
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK |                          8 |
| 1769-L27ERM-QBFC1B                    |                         16 |
| 1769-L30ER, 1769-L30ERK               |                         16 |
| 1769-L30ERM, 1769-L30ERMK             |                         16 |
| 1769-L30ER-NSE                        |                         16 |
| 1769-L33ER, 1769-L33ERK               |                         32 |
| 1769-L33ERM, 1769-L33ERMK             |                         32 |
| 1769-L33ERMO                          |                         32 |
| 1769-L36ERM                           |                         48 |
| 1769-L36ERMO                          |                         48 |
| 1769-L37ERM, 1769-L37ERMK             |                         64 |
| 1769-L37ERMO(1)                       |                         64 |
| 1769-L38ERM, 1769-L38ERMK             |                         80 |
| 1769-L38ERMO(1)                       |                         80 |

(1) Available at software version 31 and firmware revision 31.

## IMPORTANT

While CompactLogix 5370 controllers offer the option of using Ethernet node count to effectively design a control system, the controllers do have connection limits on an EtherNet/IP network.

For more information on how to design EtherNet/IP network use in your CompactLogix 5370 control system, see these resources:

- The EtherNet/IP Capacity Tool Wizard embedded in the Integrated Architecture® Builder (IAB) software from Rockwell Automation: https:// www.rockwellautomation.com/en-us/support/product/productselection-configuration/integrated-architecture-builder.html The EtherNet/IP Capacity Tool Wizard helps you in the initial layout of

your EtherNet/IP network.

- Ethernet Design Considerations Reference Manual, publication ENET-RM002 .

## Devices Included in the Node Count

Any devices that you add directly to the local Ethernet I/O configuration are counted toward the node limitation of the controller. The following are example devices that are added to the I/ O configuration section in your project and must be counted:

- Remote communication adapters
- I/O modules that are directly connected to the EtherNet/IP network, for example the 1732E-IB16M12R ArmorBlock® EtherNet/IP module
- Motion devices, such as drives
- Remote controllers
- HMI devices that are included in the I/O configuration section, for example, PanelView™ Plus terminals
- Linking devices, such as the 1788-EN2DNR, Ethernet-to-DeviceNet linking device or 1788-EN2DNROM, On-Machine™ Ethernet-to-DeviceNet linking device
- Third-party devices that are directly connected to the EtherNet/IP network

## Devices Excluded from the Node Count

When considering the Ethernet node limitation of a CompactLogix 5370 controller, you do not count Ethernet devices that exist on the EtherNet/IP network but aren't added to the I/O configuration section of the project.

The following devices aren't added to the I/O configuration section in your project and aren't counted among the total number of nodes:

- Computer
- HMIs that aren't added to the I/O configuration section, for example, PanelView™ Plus terminals
- MSG instructions
- Devices the CompactLogix 5370 controllers use a socket interface to communicate with.

For example, the following devices require communication via a socket interface:

- Modbus TCP/IP device
- Barcode scanners

## EtherNet/IP Network Topologies

CompactLogix 5370 controllers support the EtherNet/IP network types that are detailed in this section. Each of these EtherNet/IP network topologies supports applications that use Integrated Motion over an EtherNet/IP network, if necessary.

Device-level Ring Network Topology

A DLR network topology is a single-fault tolerant ring network that is intended for the interconnection of automation devices. A DLR network is composed of Supervisor (Active and Backup) nodes and Ring nodes.

DLR network topologies automatically convert to linear network topologies when a fault is detected. The conversion to the new network topology maintains communication of data on the network. The fault condition is typically easily detected and corrected.

CompactLogix 5370 controllers connect directly to a DLR network topology, that is, without requiring a 1783-ETAP tap to connect to the network. The controllers can function in any of the roles on a DLR network topology, that is, active supervisor node, back-up supervisor node or ring node.

## IMPORTANT

The topology graphics that are shown in this section are examples of applications that use only DLR network topologies.

We recommend that you exercise caution if you consider designing an application that includes the connection of a DLR topology with a linear or star network topology.

For more information on using a DLR network topology, see the EtherNet/IP Embedded Switch Technology Application Guide, publication ENET-AP005 .

## Example 1769-L18ERM-BB1B Control System Using DLR Network Topology

<!-- image -->

## Example 1769-L27ERM-QBFC1B Control System Using DLR Network Topology

<!-- image -->

Kinetix 5500

## Example 1769-L33ERM Control System Using a DLR Network Topology

<!-- image -->

## Linear Network Topology

A linear network topology is a collection of devices that are daisy-chained together across an EtherNet/IP network. Devices that can connect to a linear network topology use embedded switch technology to remove any need for a separate switch, as required in Star network topologies.

## Example 1769-L18ERM-BB1B Control System Using a Linear Network Topology

<!-- image -->

## Example 1769-L24ER-QB1B Control System Using a Linear Network Topology

<!-- image -->

## Example 1769-L33ERM Control System Using a Linear Network Topology

<!-- image -->

## Star Network Topology

A star network topology is a traditional EtherNet/IP network that includes multiple devices that are connected to each other via an Ethernet switch.

## Example1769-L18ERM-BB1B Control System Using a Star Network Topology

<!-- image -->

Example 1769-L27ERM-QBFC1B Control System Using a Star Network Topology

<!-- image -->

## Example 1769-L33ERM Control System Using a Star Network Topology

<!-- image -->

## Socket Interface with CompactLogix 5370 Controllers

CompactLogix 5370 controllers can use socket interfaces to communicate with Ethernet devices that do not support the EtherNet/IP application protocol. The socket interface is implemented via the Socket Object. CompactLogix 5370 controllers communicate with the Socket Object via MSG instructions. To communicate with another device, you must understand the application protocol of the other device.

CompactLogix 5370 controllers support up to 32 socket instances.

## IMPORTANT

Keep the following in mind when using sockets with CompactLogix 5370 controllers:

- A significant difference between CompactLogix 5370 controllers and other Logix 5000™ controllers is the communication path. CompactLogix 5370 controllers do not require a separate EtherNet/IP network communication module, for example, a 1756-EN2T module. In the case of the CompactLogix 5370 controllers, the MSG is sent to the controller itself by using the path '1,0'.
- All CompactLogix 5370 controllers must use unconnected MSG instructions for socket servers. When you configure a message for a CompactLogix 5370 controller, make sure that the Connected checkbox on the Message Configuration dialog box is cleared.

For more information on socket interface, see EtherNet/IP Socket Interface Application Technique, publication ENET-AT002 .

## Quality of Service (QoS) and I/O Module Connections

CompactLogix 5370 controllers support Quality of Service (QoS) technology. QoS lets the controller prioritize EtherNet/IP network traffic. By default, the CompactLogix 5370 controllers are QoS-enabled. QoS can be disabled by configuring a message instruction in the Logix Designer application.

Some EtherNet/IP devices do not support QoS technology unless the firmware of the device is updated to a required minimum firmware revision level. For example, the ControlLogix® 1756ENBT communication module must use firmware revision 4.005 or later to support QoS technology.

To make sure communication between CompactLogix 5370 controllers and I/O modules are maintained, verify that the EtherNet/IP devices use the minimum firmware revision level of the product that is required to support QoS technology.

For more information on the following, see Knowledgebase Technote, QoS Compatibility with Embedded Switch Technology Products:

- Minimum firmware revision levels of EtherNet IP devices to support QoS technology
- Enable/disable QoS.

## EtherNet/IP Network Connections

CompactLogix 5370 controllers use connections to manage communication on the EtherNet/IP network. A connection is a point-to-point communication mechanism that is used to transfer data between a transmitter and a receiver. Connections can be logical or physical.

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system.

Connections are allocations of resources that provide more reliable communication between devices than unconnected messages.

All EtherNet/IP connections are unscheduled. An unscheduled connection is a message transfer between controllers that the requested packet interval (RPI) or the program, such as an MSG instruction, triggers. Unscheduled messaging lets you send and receive data when needed.

## CompactLogix 5370 Controller EtherNet/IP Network Port Specifications

| Cat. No.           | Connections   | CIP Unconnected Messages (backplane + Ethernet) (backplane + Etht) Controller TCP CIP I/O HMI/MSG                 | Packet Rate Capacity (packets/second) (1)   | Packet Rate Capacity (packets/second) (1)   | SNMP Support (password required)   | Media Support    | Produced/Consumed Tags                  | Produced/Consumed Tags   |
|--------------------|---------------|-----------------|---------------------------------------------|---------------------------------------------|------------------------------------|------------------|-----------------------------------------|--------------------------|
| Cat. No.           |               | CIP Unconnected Messages (backplane + Ethernet) (backplane + Etht) Controller TCP CIP I/O HMI/MSG                 |                                             |                                             | SNMP Support (password required)   | Media Support    | Number of Multicast Tags, Max (2)       | Unicast Available        |
| 1769-L16ER-BB1B    |               | 256 120 256 256 | 6000 @ 500 bytes/ packet                    | messages/s @ 20% comm. timeslice            |                                    | Yes Twisted Pair | produced tags 128 unicast produced tags | Yes                      |
| 1769-L18ER-BB1B    |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L18ERM-BB1B   |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L18ERM-BB1BK  |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L19ER-BB1B    |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L19ER-BB1BK   |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L24ER-QB1B    |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L24ER-QBFC1B  |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L24ER-QBFC1BK |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L27ERM-QBFC1B |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L30ER         |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L30ERK        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L30ERM        |               |                 |                                             | 400                                         |                                    |                  | 32 multicast                            |                          |
| 1769-L30ERMK       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L30ER-NSE     |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L33ER         |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L33ERK        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L33ERM        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L33ERMK       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L33ERMO       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L36ERM        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L36ERMO       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L37ERM        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L37ERMK       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L37ERMO(3)    |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L38ERM        |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L38ERMK       |               |                 |                                             |                                             |                                    |                  |                                         |                          |
| 1769-L38ERMO(3)    |               |                 |                                             |                                             |                                    |                  |                                         |                          |

(1) Total packet rate capacity = I/O Produced Tag, max + HMI/MSG, max Packet rates vary depending on packet size. For more detailed specifications, see the capacity section of the EDS file for the catalog number.

(2) These are the maximum numbers of CIP I/O connections.

(3) Available at software version 31 and firmware revision 31.

## DeviceNet Network Communication

The CompactLogix 5370 L2 and L3 controllers communicate with other devices over the DeviceNet network via a Compact I/O 1769-SDN DeviceNet scanner. The DeviceNet network uses the Common Industrial Protocol (CIP) to provide the control, configuration, and data collection capabilities for industrial devices.

## IMPORTANT

This section applies to applications using only CompactLogix 5370 L2 and L3 controllers. CompactLogix 5370 L1 controllers do not operate on DeviceNet networks.

## Available Software

The software applications that are listed in this table are required when using a CompactLogix 5370 L2 or L3 controller on a DeviceNet network.

| Software                 | Required Version                                                                                                                                                                       | Functions                                                                                         |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| RSLogix 5000®            | 20 - For CompactLogix 5370 controllers using firmware revision 20.                                                                                                                     |                                                                                                   |
| Studio 5000® environment | 21 or later - For CompactLogix 5370 controllers using firmware revision 21 or later. Studio 5000 environment, version 28 or later - For 1769-L19ER-BB1B controllers.                   | Configure the CompactLogix project                                                                |
| RSLinx Classic           | 2.59.00 or later(1), (2),(3)                                                                                                                                                                                        | • Configure communication devices • Provide diagnostics • Establish communication between devices |
| RSNetWorx™ for DeviceNet | One of the following: • 11.00.00 or later if used with RSLogix 5000 software, version 20.xx.xx • 21.00.00 or later if used with the Studio 5000 environment, version 21.00.00 or later | • Configure DeviceNet devices • Define the scanlist for the DeviceNet network                     |

- (1) CompactLogix 5370 L2 controllers require RSLinx Classic software, version 2.59.01 or later.
- (2) We recommend that you use RSLinx Classic software, version 3.51.00 or later, with the Studio 5000 environment, version 21.00.00 or later.
- (3) RSLinx Classic software, version 3.74.00 is recommended for use with the 1769-L19ER-BB1B controller.

## Example 1769-L24ER-QB1B Control System Using a DeviceNet Network

<!-- image -->

## Example 1769-L33ERM Control System Using a DeviceNet Network

<!-- image -->

## Compact I/O 1769-SDN DeviceNet Scanner

You connect a CompactLogix 5370 L2 or L3 controller to a DeviceNet network via a Compact I/ O 1769-SDN DeviceNet scanner.

Before installing the scanner, consider these details:

- You can connect the scanner to an adjacent controller, power supply, or I/O module.
- You must account for these two requirements jointly:
- Power Supply Distance Rating, described on page 113
- Current Capacity in CompactLogix 5370 L3 Control Systems, described on page 116
- The scanner, as a master, can own up to 63 slave I/O nodes.
- Another DeviceNet master can own a scanner that is simultaneously a master and be a slave.

The scanner has this functionality:

- Supports messaging to devices, not controller to controller
- Supports control-level network to device-level network for programming, configuration, control, or data collection
- Supports back up your CompactLogix 5370 L2 or L3 controller on the DeviceNet network For more information on using the 1769-SDN to back up your CompactLogix 5370 L2 or L3 controller, see the 1769-SDN DeviceNet Scanner Module User Manual, publication 1769-UM009 .
- Shares a common application layer with EtherNet/IP networks
- Offers diagnostics for improved data collection and fault detection

## Power Supply Distance Rating

CompactLogix 5370 L2 and L3 control systems enable you to install 1769-SDN scanners as local expansion modules. The 1769-SDN scanner has a power supply distance rating that you must consider before installing it.

Power supply distance rating is the number of slots a 1769-SDN scanner can be installed away from the power supply. The 1769-SDN scanner has a power supply distance rating of four. Therefore, your CompactLogix 5370 L2 or L3 control system can include up to three modules between the 1769-SDN scanner and the power supply.

The power supply distance rating of the 1769-SDN scanner as a design consideration differs by CompactLogix L2 controller catalog number.

## CompactLogix 5370 L2 Control Systems

In a CompactLogix 5370 L2 control system, you can install a 1769-SDN scanner on the right side of the control system. The controller has an embedded power supply, which disallows the installation of 1769-SDN scanners between the controller and the power supply.

Additionally, the controller has embedded I/O modules that disallow installation of the 1769SDN scanner directly to the right of the embedded power supply. CompactLogix 5370 L2 control systems have one or two embedded I/O modules, described as follows:

- 1769-L24ER-QB1B controller - One embedded I/O module
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers - Two embedded I/O modules

While the embedded I/O modules aren't considered local expansion modules, you must still include each embedded I/O module in the module slot count when determining where to install the 1769-SDN scanner as a local expansion module.

The farthest local expansion module slot where you can install the 1769-SDN scanner in a CompactLogix 5370 L2 control system is module slot number two or three as determined by the controller catalog number that is used in the control system.

This table lists the farthest local expansion module slot where you can install a 1769-SDN scanner and meet its power supply distance rating requirement.

## Example CompactLogix 5370 L2 Control Systems with a 1769-SDN Scanner

<!-- image -->

## CompactLogix 5370 L3 Control Systems

CompactLogix 5370 L3 control systems do not have embedded I/O modules. You begin counting local expansion slots with the first Compact I/O module installed next to the power supply when determining where to install a 1769-SDN scanner and meet its power supply distance rating.

In CompactLogix 5370 L3 control systems, you can install 1769-SDN scanners to the left or right side of the power supply. You can also use local and extra banks in CompactLogix 5370 L3 control systems, with each allowing the inclusion of a 1769-SDN scanner.

In the local bank, the controller must be the leftmost device in the system and you can only install up to three modules between the controller and the power supply. Therefore, any 1769SDN scanners that are installed to the left of the power supply in the local bank, are in a module slot that meets the power supply distance rating requirements of the module.

CompactLogix 5370 L3 control systems also support the use of extra banks for the local expansion modules of the system. Each additional bank requires a 1769 Compact I/O power supply. The bank can be designed with local expansion modules on either side of the power supply.

In this case, you must install the 1769-SDN scanner with no more three Compact I/O modules between the scanner and the power, regardless of whether the modules are installed to the left or right of the power supply.

This graphic shows 1769-SDN scanners that are installed in a 1769-L36ERM control system that meet the power supply distance rating of the module.

<!-- image -->

## Current Capacity in CompactLogix 5370 L3 Control Systems

In a local or extra bank, the modules that are installed on either side of the power supply can't draw more current than the power supply can supply. This requirement partially dictates module placement on the bank.

For example, if a bank uses a 1769-PA2 Compact I/O power supply, each side of the bank has a current capacity of 1 A at 5V DC and 0.4 A at 24V DC. Because a

1769-SDN scanner has a current draw of 440 mA at 5V DC and 0 mA at 24V DC, you can only install up to two scanners on each side of the power supply in the bank in this case.

For more information on 1769 Compact I/O power supply maximum current capacity and calculations you can use to design the modules that are used in local or extra banks, see Chapter 9, page 194 .

## Select I/O Modules

<!-- image -->

## Use I/O Modules with CompactLogix 5370 L1 Controllers

This chapter details the I/O module options that CompactLogix™ 5370 L1 control systems offer.

## Connect Field Power to I/O Devices

Chapter 2, page 32, describes how to connect power to an L1 series B or C controller. The graphics in this section show how to connect a dedicated, Class 2/SELV-listed external 24V DC power source to the VDC+ and VDC- terminals on the removable connector. Those connections provide power to only the system-side of the embedded I/O and local expansion I/O modules.

## IMPORTANT

You must connect a separate external power source to the FP+ and FPterminals on the removable connector on the controller to power the field-side circuitry of the embedded I/O modules and the local expansion modules for only series A L1 controllers. See Appendix C, page 257 for further information.

Power connections to the FP+ and FP- terminals provides power to input and output devices that are connected to the embedded I/O modules or local expansion modules of the controller. For example, input or output devices, such as a barcode scanner.

The embedded I/O of the controller and the field-side power of the local expansion modules is 24V DC nominally with an input range of 10…28.8V DC.

This graphic shows the removable connector.

<!-- image -->

IMPORTANT

The controller is grounded once it's installed on a DIN rail as described in Chapter 2, page 28 .

Consider these points before completing the steps in this section:

- This section describes how to connect a 24V DC power source to power input or output devices that are connected to the embedded I/O or local expansion modules of the CompactLogix 5370 L1 controller via FP+ and FP- terminals.

For information on how to connect 24V DC power to the CompactLogix 5370 L1 controller and the POINTBus™ backplane via VDC+ and VDC- terminals on the removable connector, see Chapter 2, page 32 .

- The external 24V DC power source that is connected to the FP+ and FP- terminals must be separate from the power source that is dedicated to power the controller via the VDC+ and VDC- terminals for only series A controllers (see Appendix C, page 257).
- You can use the external 24V DC power source that provides power to the FP+ and FPterminals to power other components or devices in the application.
- The external 24V DC power source that provides power to the FP+ and FP- terminals can be installed on the same DIN rail as the external 24V DC power source that provides power to the VDC+ and VDC- terminals or you can install the external 24V DC power sources on separate DIN rails.
- Use a power source that most effectively meets your application needs. That is, calculate the power requirements of your application before choosing a power source to avoid using a power source that far exceeds your application requirements:
- Limit field power current to 3 A or use a 1734-FPD module to avoid blowing the internal fuse.
- Install a user-replaceable fuse with overcurrent protection of 4…6 A @ 52.5…68.25
- This section assumes that any DIN rail that you use has been grounded following Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .
- For example purposes, this section describes how to use a 1606-XLE80E, Class 2 switched-mode power supply with the FP+ and FP- terminals. The exact steps for other external power supplies can vary from the steps that are described here.

## IMPORTANT

Do not use the following steps to connect power to the CompactLogix 5370 series A L16ER, L18ER, and L18 ERM controllers. Appendix C, page 257 provides steps to connect power to the CompactLogix 5370 series A L16ER, L18ER, and L18 ERM controllers. The steps are also an optional way to connect power to a series B or C L1 controller.

Complete these steps to connect power to CompactLogix 5370 series B and C L16ER, L18ER, or L18ERM controllers, and series A and C L19 controllers.

1. Verify that the separate external 24V DC power source that powers the CompactLogix 5370 L1 controller isn't powered.
2. Connect the wires to the + and - connections on the external 24V DC power source.

<!-- image -->

WARNING: If you connect or disconnect wiring while the field-side power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

3. Loosen the screws that secure the removable connector to the CompactLogix 5370 L1 controller and pull the connector off the controller.
4. Connect the wire that is connected to the + terminal on the external 24V DC power source to the FP+ terminal. The FP+ terminal is the fourth terminal from the top on the removable connector.
5. Connect the wire that is connected to the - terminal on the external 24V DC power source to the FP- terminal. The FP- terminal is the fifth terminal from the top on the removable connector.
6. Plug the removable connector into the controller.

<!-- image -->

<!-- image -->

<!-- image -->

7. Secure the removable connector in place.
8. Turn on power to the separate external 24V DC power source connected to the removable connector.

<!-- image -->

The following graphic shows separate external 24V DC power supply that is connected to the VDC+/VDC- and FP+/FP- terminals on the removable connector, respectively.

<!-- image -->

IMPORTANT

No wires are connected to the NC terminal.

## Embedded I/O Modules

CompactLogix 5370 L1 controllers provide an embedded power supply and an embedded I/O module with these points:

- 16 sinking 24V DC digital input points
- 16 sourcing 24V DC digital output points

The following diagram shows the wiring terminals on the embedded I/O module.

<!-- image -->

Consider the following when you connect input or output devices to the embedded I/O modules of your CompactLogix 5370 L1 controller:

- You must connect an external 24V DC power source to the FP+ and FP- terminals on the removable connector on the controller to the power input and output devices that are connected to the embedded I/O modules on the controller:
- Series A for L16ER, L18ER, and L18ERM controllers require an extra external 24V DC power source for the FP+ and FP- terminal connections. For more information on how to connect an extra external power source for a series A L1 controller to the FP+ and FP- terminals, see Appendix C, page 257 .
- Series B and C controllers use the external 24V DC power source that is connected to the VDC+ and VDC- terminals on the controller for the FP+ and FP- terminal connections. Series B and C controllers can also use an extra external 24V DC power source for the FP+ and FP- terminal connections. See Appendix C, page 257 for more information on how to connect the extra external power source to the FP+ and FPterminals. For more information on how to connect the external power source to the FP+ and FP- terminals on the series B and C controllers, see page 118 .

The field-side power requirement of the embedded I/O modules of the controller is 24V DC nominally with an input range of 10…28.8V DC.

- The available RPI range of the I/O points is 1.0 ms … 750.0 ms and can be changed by 0.5 ms increments. The default setting is 20 ms.

## IMPORTANT

- If you attempt to use an RPI value that is not valid, the application automatically rounds the value down to the closest 0.5 ms increment when you apply the change.

For example, if you set the RPI = 1.75 ms, when you select Apply or OK, the value is rounded down to 1.5 ms and applied.

- The RPI value for embedded I/O module is intended to establish a time interval at which data is transmitted. However, the configuration of your CompactLogix 5370 L1 control system can affect the actual time interval of data transmission. For more information, see Estimate Requested Packet Interval on page 132 .

Complete these steps to wire the input and output points on the CompactLogix 5370 L1 controller.

1. Verify that the control system isn't powered.
2. Use a small screwdriver to push the spring release clip and insert the wire.
3. With the wire in place, pull the screwdriver off the spring release clip.
4. Repeat step 2 for all embedded I/O wires that are needed in your application.

<!-- image -->

To remove a wire from the removable connector, complete these steps.

1. Verify that the control system isn't powered.
2. Use a small screwdriver to push the spring release clip and pull out the wire.

Remove and Replace and I/O Module Connector

Complete these steps to remove and replace and I/O module connector.

1. Verify that the control system isn't powered.
2. Use a small screwdriver to loosen the screws that secure the connector to the module.
3. Pull the connector out from the I/O module to remove it.
4. Disconnect any wires from the connector.
5. Connect any wires to the replacement connector.
6. Push the replacement connector back into the I/O module.
7. Secure the connector to the I/O module with the small screwdriver.

<!-- image -->

## Embedded Input Points

The embedded input points on the CompactLogix 5370 L1 controllers support 2-wire and 3wire input devices. You can wire the input devices to be powered in one of the following methods:

- By using an external power supply, as shown in Figure 2 on page 124 - In this case, you can monitor the input devices even if field power is interrupted, for example, by the Master Control Relay (MCR).

This method is required if you must continue reading data from the input devices when the embedded output terminals are disabled, for example, when the use of an MCR disrupts output power.

- By using the V terminal on the embedded I/O module, as shown in Figure 4 on page 125 - In this case, you can't monitor the input devices even if field power is interrupted, for example, by the MCR.

Figure 2 on page 124 and Figure 3 on page 124 show examples of how to power 2-wire and 3wire input devices in your application.

## IMPORTANT

When using Figure 2 on page 124 and Figure 3 on page 124, use the following guidelines:

- With this wiring configuration, you can monitor the input devices even if field power is interrupted, for example, by the MCR. The FP- connection must be maintained as a reference for inputs to function.
- With this wiring configuration, the controller does not help protect fieldside devices from overcurrent draw conditions.
- Design your application so that power consumption does not exceed the power supply ratings.
- The following figure is a wiring example that complies with the National Electrical Code (NEC) standard for isolation between system and field power.
- The FP+ terminal on the removable connector is the voltage connection.
- The FP- terminal on the removable connector is the common connection.
- The MCR must be closed for the removable connector to provide power to the embedded I/O module.
- Install a user-replaceable fuse with overcurrent protection of 

For series A L1 controllers only, you must use a separate, dedicated Class 2 power supply for the CompactLogix 5370 L1 controller and a separate power supply for the embedded I/O module (see Appendix C, Connect Field Power to Series A L1 Controllers for I/O Devices ).

Figure 2 - CompactLogix 5370 L16ER, L18ER, and L18ERM Controllers with Input Devices Powered by External Power Supplies (Series A [Alternate Series B and C])

<!-- image -->

Figure 3 - CompactLogix 5370 L1 Controllers with Input Devices Powered by External Power Supplies (Series B and C)

<!-- image -->

Figure 4 on page 125 and Figure 5 on page 126 shows examples of how to power 2-wire and 3wire input devices in your application with connections to a V terminal.

## IMPORTANT

When using Figure 4 on page 125 and Figure 5 on page 126, use the following guidelines:

- With this wiring configuration, the input devices lose power if the removable connector does not power the embedded I/O modules.
- With this wiring configuration, the controller does not help protect fieldside devices from overcurrent draw conditions.
- Design your application so that power consumption does not exceed the power supply ratings.
- The following figure is a wiring example that complies with the National Electrical Code (NEC) standard for isolation between system and field power.
- The FP+ terminal on the removable connector is the Voltage connection.
- The FP- terminal on the removable connector is the Common connection.
- The MCR must be closed for the removable connector to provide power to the embedded I/O module.
- Install a user-replaceable fuse with overcurrent protection of 4…6 A in line between the incoming power and the FP+ terminal.

For series A L1 controllers only, you must use a separate, dedicated Class 2 power supply for the CompactLogix 5370 L1 controller and a separate power supply for the embedded I/O module (see Appendix C, Connect Field Power to Series A L1 Controllers for I/O Devices ).

Figure 4 - CompactLogix 5370 Series B and C L16ER, L18ER, and L18ERM Controllers, and series A and C L19 Controllers with Input Devices Powered by a V Terminal on Embedded I/O Module (Series A [Alternate Series B and C])

<!-- image -->

Figure 5 - CompactLogix 5370 L1 Controllers with Input Devices Powered by a V Terminal on Embedded I/O Module (Series B and C)

<!-- image -->

## Embedded Output Points

The embedded output points on the CompactLogix 5370 L1 controllers support 2-wire systems. The embedded power supply in the controller powers the embedded output points over the POINTBus backplane.

This figure shows examples of how to connect 2-wire systems to embedded output points 0…7. The same wiring connections can be used with output points 8…15.

## IMPORTANT

Do not exceed the per point output current rating or the total output module current rating.

## CompactLogix 5370 L1 Controllers Embedded Digital Output Point Wiring Diagram

<!-- image -->

This figure shows an example of how to connect 2-wire systems to embedded output points 0…4 and use an external terminal block with a bus connector strip.

## IMPORTANT

Do not exceed the per point output current rating or the total output module current rating.

## CompactLogix 5370 L1 Controllers Embedded Digital Output Point Wiring Diagram

<!-- image -->

## Local Expansion Modules

CompactLogix 5370 L1 controllers support the use of 1734 POINT I/O™ modules as local expansion modules along the POINTBus backplane.

## IMPORTANT

For a full description of how to use 1734 POINT I/O modules, see the POINT I/O Digital and Analog Modules and POINTBlock I/O Modules, publication 1734-UM001 .

Consider the following when using local expansion modules:

- The controllers support this many local expansion modules.

## Maximum 1734 POINT I/O Modules Available as Local Expansion Modules

| Cat. No.                            | Local 1734 POINT I/O Modules Supported, Max   |
|-------------------------------------|-----------------------------------------------|
| 1769-L16ER-BB1B                     | 6                                             |
| 1769-L18ER-BB1B                     |                                               |
| 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK | 8                                             |
| 1769-L19ER-BB1B, 1769-L19ER-BB1BK   |                                               |

- You can use up to the maximum number of 1734 POINT I/O modules with the CompactLogix 5370 L1 controllers that are listed in this table. This condition applies only as long as the total current drawn by the embedded I/O and local expansion modules does not exceed the available POINTBus backplane current of 1 A and field power current of 3 A.

## IMPORTANT

Do not put more than three of the 1734-IT2I or 1734-IR2 modules on the POINT I/O bus that draws power from the same power source. This restriction includes power sources such as from communication adapters or the 1734-EPAC or 1734-EP24DC expansion power supply modules. The inrush current exceeds the current limit of the DC to DC converter in the power source.

Based on the configuration of your application, you can use one of the following devices to make more POINTBus backplane current or field power current available:

- -1734-EP24DC POINT I/O Expansion Power Supply - An expansion power supply is installed between embedded I/O modules and local expansion modules or between local expansion modules.

The expansion power supply breaks the available POINTBus backplane current between the modules to its left and right. With the expansion power supply installed, the modules to its left can draw up to 1 A of POINTBus backplane current. The modules to the right of the expansion power supply can draw as much current as is provided by the expansion power supply.

Additionally, the expansion power supply breaks the available field power current between the modules to its left and right. With the expansion power supply installed, the modules to its left can draw up to 3 A of field power current. The modules to the right of the expansion power supply can draw as much field power current as allowed by the expansion power supply.

For example, if you need six 1734-IR2 modules as local expansion modules for a 1769L18ER-BB1B controller application, you must include the 1734-EP24DC expansion power supply in the local expansion-module installation.

For more information on the 1734-EP24DC expansion power supply, see the POINT I/O 24V DC Expansion Power Supply Installation Instructions, publication 1734-IN058 .

- -1734-FPD POINT I/O Field Power Distributor Module - A field power distributor module can also be installed between embedded I/O modules and local expansion modules or between local expansion modules.

The field power distributor module breaks the available field power current between the modules to its left and right. With the field power distributor module installed, the modules to its left can draw up to 3 A of field power current. The modules to the right of the field power distributor module can draw as much field power current as allowed by the field power distributor.

For more information on the 1734-FPD POINT I/O Field Power Distributor module, see the POINT I/O Field Power Distributor Module Installation Instructions, publication 1734-IN059 .

## IMPORTANT

Remember, the field power distributor module changes only the level of field power current available in the system. It does not affect the level of POINTBus backplane current available.

- You must connect an external 24V DC power source to the FP+ and FP- terminals on the removable connector on the controller. This connection provides power to input and output devices that are connected to the local expansion modules.
- Series A controllers require an extra external 24V DC power source for the FP+ and FP- terminal connections. For more information on how to connect an extra external power source for series A L1 controller to the FP+ and FP- terminals, see Appendix C, Connect Field Power to Series A L1 Controllers for I/O Devices
- Series B and C controllers use the external 24V DC power source that is connected to the VDC+ and VDC- terminals on the controller for the FP+ and FP- terminal connections. Series B and C controllers can also use an extra external 24V DC power source for the FP+ and FP- terminal connections.

## IMPORTANT

Install a user-replaceable fuse with overcurrent protection of 4…6 A in line between the incoming power and the FP+ terminal.

The field-side power requirement of the local expansion modules of the controller is 24V DC nominally with an input range of 10…28.8V DC.

For more information on how to connect a power source to the FP+ and FP- terminals, see page 117 .

- We recommend that you update all 1734 POINT I/O modules that are designated as local expansion modules to the most current firmware revision before installing them in a CompactLogix 5370 L1 system.
- The available RPI range of each local expansion module is 1.0 … 750.0 ms and can be changed by 0.5 ms increments. The default setting is module-dependent.

You can configure RPI values for each local expansion module in your control system. However, the complete I/O configuration has an impact on the rate at which data is transmitted in a CompactLogix 5370 L1 control system. For more information, see page 132 .

- Before installing a 1734 POINT I/O module into a CompactLogix 5370 L1 control system, make sure the I/O module is set to Autobaud. 1734 POINT I/O modules are set to Autobaud by default.

If you must return a 1734 POINT I/O module to Autobaud, see the POINT I/O Digital and Analog Modules and POINTBlock I/O Modules, publication 1734-UM001 .

- When possible, use specialty 1734 POINT I/O modules to meet unique application requirements.
- Make sure that there are no empty slots between the controller and local expansion modules or between local expansion modules.
- The Expansion I/O parameter in the project of the controller must match the number of local expansion modules that are installed in the system. This requirement is so the controller can establish connections to the local expansion modules.
- You must use a 1734-232ASC, firmware revision 4.002 or later, to access an RS-232 network in your CompactLogix 5370 L1 controller application.

| IMPORTANT   | Field power is required for the 1734-232ASC module. The module can’t receive adequate power without the application of field power.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|

## Distributed I/O Modules over an EtherNet/IP Network

You can include distributed I/O modules over an EtherNet/IP™ network in your CompactLogix 5370 L1 control system.

Consider the following when using distributed I/O modules over an EtherNet/IP network:

- Each remote EtherNet/IP adapter included in the system must be counted toward the maximum number of EtherNet/IP nodes of the controller.

For more information on maximum number of EtherNet/IP nodes, see Chapter 6, page 102 .

- The configurable RPI settings vary depending on which distributed I/O modules are used in the system.
- To add distributed I/O modules to your CompactLogix 5370 L1 control system, see page 140 .

## CompactLogix 5370 L1 Control System That Uses All Three I/O module Options

<!-- image -->

## Validate I/O Layout

You must validate the layout of 1734 POINT I/O modules in your CompactLogix 5370 L1 control system. Consider the points detailed in this section when validating I/O layout placement.

## Set the Number of Local Expansion Modules

You must specify the number of local expansion modules a CompactLogix 5370 L1 control system requires when creating a project or when you change the number of local expansion modules. This graphic depicts the module selection.

<!-- image -->

Each time the controller is powered up, it compares the number of local expansion modules present on the POINTBus backplane to the Expansion

I/O value. The controller does not allow any I/O connections until the number of local expansion modules present equals the Expansion I/O value.

## Empty Slots and Removal and Insertion Under Power Situations

The POINT I/O system can't detect an empty terminal base. For this reason, there are numerous situations in which you can potentially configure a system that is unusable or one that exercises unintended control.

Follow these rules for I/O system configuration and RIUP of I/O modules.

<!-- image -->

WARNING: If you insert or remove the module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

## IMPORTANT

1734 POINT I/O modules support RIUP in CompactLogix 5370 L1 control systems.

- A correct I/O system does not have any empty terminal bases. If necessary, you can use a 1734-ARM POINT I/O Address Reserve module to replace a 1734 POINT I/O module in a CompactLogix 5370 control system.
- After you cycle power, the controller only enables I/O connections if the number of local expansion modules present on POINTBus matches the value that is used for the Expansion I/O parameter in the project.
- If a 1734 POINT I/O module is removed under power, the operation of the other I/O modules isn't disrupted.

- When you remove an I/O module that has an active connection from the controller, the controller I/O status indicator flashes green to indicate the condition.

## IMPORTANT

If you enabled the 'Major Fault On Controller If Connection Fails While in Run Mode' parameter when configuring the module in the Studio 5000® environment project, removal of the module causes the controller to transition to a major fault condition.

- If multiple contiguous modules are removed under power, connections to all modules in the contiguous missing module set are disallowed until all modules are replaced. The controller can't detect an empty base. Therefore, it does not know the physical positioning of the modules until all missing modules are replaced.
- If a module that separates two sets of contiguous missing modules is removed, the two sets merge into one set. All modules must be replaced before connections are permitted to any module in the set.
- If modules of different types are removed and returned to the wrong locations, attempts to connect to these modules fail during verification of Electronic Keying.

## IMPORTANT

If Electronic Keying is set to Disable Keying, no verification of electronic keying occurs and unintended control can occur.

- If modules of the same type are removed and returned to the wrong locations, they accept connections from the controller. The modules also reconfigure with the correct data once they pass their electronic keying check.

## Estimate Requested Packet Interval

The requested packet interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. You set an RPI rate for each I/O module in your system.

The CompactLogix 5370 L1 controllers attempt to scan an I/O module at the configured RPI rate. For individual I/O modules, a module RPI overlap minor fault (further described on page 133) occurs if there are enough I/O modules with RPI rates set too fast that they can't all be serviced in the allotted interval.

The configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can affect the effective scan frequency for any individual module:

- Other 1734 POINT I/O module RPI rate settings
- Number of other 1734 POINT I/O modules in the system
- Types of other 1734 POINT I/O modules in the system
- Application user task priorities

In general, follow these guidelines when setting the RPI rates in a CompactLogix 5370 L1 control system:

- For digital I/O modules:
- 1…2 modules can be scanned in 2 ms.
- 3…4 modules can be scanned in 4 ms.
- 5…8 modules can be scanned in 8 ms.

## IMPORTANT

When considering digital I/O modules, remember that they can be the embedded I/O module on the controller or 1734 POINT I/O modules that are used as Local Expansion Modules. Therefore, the consideration for using two modules can be the embedded I/O module and a 1734 POINT I/O module or two 1734 POINT I/O modules.

- For specialty and analog I/O modules (except 1734-485ASC modules):
- One module can be scanned at 20 ms.
- For each additional module, add 20 ms.

For example, if a CompactLogix 5370 L1 control system uses two analog modules, the module can be scanned in 40 ms.

- For 1734-485ASC modules, the total data size for all ASC modules determines the RPI rates:
- For total data size less than 20 bytes, each module can be scanned in 20 ms.
- For data size greater than 20 bytes, use the size value as the RPI.

For example, if the total data size is 40 bytes, each ASC module can be scanned in 40 ms.

You aren't required to set individual RPI values of 1734 POINT I/O modules to the values listed previously. For example, if your application scans one or two modules, you do not have to use RPI rates of 2 ms. Remember, though, that higher RPI rates result in less frequent data scans.

The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Module Faults Related to RPI Estimates

When following the guidelines described on page 133, most CompactLogix 5370 L1 control systems operate as expected.

Some systems that follow the guidelines can experience minor faults that are described in this table.

|                    |                                                                                                                                                           | Name Fault Information Condition In Which Fault Occurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module RPI Overlap | (Type 03) I/O fault (Code 94) Module RPI overlap detected Module Slot = x, where x is the slot number of the I/O module in the I/ O Configuration section | This fault is logged when the current RPI update of an I/O module overlaps with its previous RPI update. The Minor Faults tab in the Controller Properties dialog box indicates which module that the RPI overlaps. If multiple I/O modules experience the fault, the application indicates that the fault occurred on the first such I/O module. Typically, it’s an I/O module with a lower RPI rate and/or an I/O module with large input/output data sizes. For example, the 1734-232ASC and 1734-485ASC modules use large input/output data sizes. Once the fault is cleared from the first I/O module, the application indicates the next module that experiences the fault. This pattern continues until the fault is cleared from all affected I/O modules. To avoid this fault, set the RPI rate of the I/O modules to a higher numerical value. |

## Calculate System Power Consumption

An embedded 24V DC nominal, non-isolated power supply with an input range of 10…28.8V DC powers the CompactLogix 5370 L1 control system.

The embedded power supply provides 1 A @ 5V DC to the POINTBus backplane to power all system components, including local expansion modules, in most system configurations. Local expansion modules include 1734 POINT I/O modules.

In some circumstances, you can configure a system that requires more current than the embedded power supply of the system provides. This type of configuration results from using a combination of local expansion modules that, when combined with current consumption of the rest of the system, exceeds 1 A @ 5V DC.

In this case, you can take any of the following actions to make sure that your system configuration has enough power:

- Insert a 1734-EP24DC POINT I/O expansion power supply between local expansion modules to increase the POINTBus backplane power.
- Insert a 1734-FPD POINT I/O Field Potential Distribution module between local expansion modules to renew field power or change the field power from DC to AC. The Field Potential Distribution module separates DC I/O modules from AC I/O modules on the same POINTBus.

## IMPORTANT

The 1734-FPD POINT I/O Field Power Distributor is required if the devices connected to the local expansion modules consume more than 3 A.

## Physical Placement of I/O Modules

Before you physically install the I/O modules, you must assemble, mount, and ground the system as described in Chapter 2, page 21 .

## Use the Event Task

The CompactLogix 5370 L1 controllers support the use of an Event task with their embedded input points. You can configure embedded input point terminals to trigger an Event task if a change of state (COS) occurs.

## IMPORTANT

When using the Event task with the CompactLogix 5370 L1 controllers, consider these points:

- You can use the Event task only with Logix Designer application, version 21.00.00 and later.
- You can use the Event task only with the embedded input points of the controller. You can't use the Event task with input points in the local expansion modules, for example, a 1734-IB4 module.
- You can use the Event task only if the input point has an input data state change.
- An event is recognized only when it maintains the same state for at least the duration of the input filter time specified.
- Configure the Event task at a rate that stops task overlap conditions.
- Configure the Event task at a rate that is likely to succeed.

A 2 ms signal width is the minimum pulse width that can be used at which the Event task succeeds.

You can configure multiple embedded input points to trigger an Event task. However, we recommend that you enable COS for only one point. If you enable COS for multiple points, a task overlap of the Event task can occur.

You can configure an Event task to trigger if one of these events occurs:

- An event occurs on one point on an input module.
- A trigger event does not occur in a time interval.

You configure whether the task updates output modules at the end of the task. After the task executes, it does not execute again until the event occurs again. Each Event task requires a trigger.

This table describes the triggers for an Event task available in a CompactLogix 5370 L1 control system.

| Trigger                 | Description                                                                                                                                                                              |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Data State Change | The input point triggers the Event task that is based on the change of state (COS) configuration for the point. The COS configuration is set on the Module Definition dialog box.        |
| Consumed Tag            | Only one consumed tag can trigger an Event task. Use an Immediate Output (IOT) instruction in the producing controller to signal the production of new data.                             |
|                         | Axis Registration 1 or 2 A registration input triggers the Event task.                                                                                                                   |
| Axis Watch              | A watch position triggers the Event task.                                                                                                                                                |
| Motion Group Execution  | The coarse update period for the motion group triggers the execution of the motion planner and the Event task. Because the motion planner interrupts all other tasks, it executes first. |
|                         | EVENT Instruction Multiple EVENT instructions can trigger the same task.                                                                                                                 |

For more information on Event tasks, see the following publications:

- Logix 5000™ Controllers Common Procedures Programming Manual, publication 1756-PM001
- Using Event Tasks with Logix 5000 Controllers, publication LOGIX-WP003

Complete the following steps to configure the Event task.

1. Open the project.
2. Right-click Embedded Discrete\_IO and select Properties.
3. On the Module Properties dialog box, complete the following steps.
- a. Select the Input Configuration tab.
- b. Enable COS for the digital input points on which a state change, that is, Off to On or On to Off, triggers the Event task.
- c. Set the desired input filter time for each COS-enabled input point.

<!-- image -->

IMPORTANT An event is recognized only when it maintains the same state for at least the duration of the input filter time specified.

## d. Select OK.

<!-- image -->

4. Right-click Tasks and select New Task.
5. On the New Task dialog box, complete the following steps.
- a. Name the task.
- b. Change the task type to Event.
- c. Select the trigger.
- d. Select the tag.
- e. If desired, set a time so the Event task executes if no event occurs with the value. On the following example dialog box, the time is 10 ms. If no event occurs for 10 ms, the Event task executes.
- f. Set the task priority.

<!-- image -->

The default Event task priority level is 10. For more information about Event tasks, see Using Event Tasks with Logix 5000 Controllers white paper, LOGIX-WP003 .

- g. Make more desired configuration changes.
- h. Select OK.

<!-- image -->

The new Event task appears in the Controller Organizer.

<!-- image -->

## Configure I/O

Complete these steps to add a 1734 POINT I/O module to your CompactLogix 5370 L1 control system.

1. Right-click PointIO and select New Module.

<!-- image -->

You can also right-click Expansion I/O.

2. Select the desired I/O module and select Create.

<!-- image -->

The New Module dialog box appears.

3. Configure the new I/O module as necessary and select OK.

<!-- image -->

## Common Configuration Parameters

While the configuration options vary from module to module, there are some common options you typically configure when using 1734 POINT I/O modules in a CompactLogix 5370 L1 control system, as described in this table.

## CompactLogix 5370 L1 Control System Configuration Options

| Configuration Option                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requested packet interval (RPI)                                 | The RPI specifies the interval at which data is transmitted or received over a connection. For POINTBus backplane local expansion modules, data is transmitted to the controller at the RPI. When scanned on the local bus or over an EtherNet/IP network, I/O modules are scanned at the RPI specified in the module configuration. Typically, you configure an RPI in milliseconds (ms). • For local expansion modules, the range is 1.0…750 ms and the RPI must be configured in 0.5 ms increments. That is, you can’t set the RPI to a value of 2.3 ms. It must be 2.0 or 2.5. • For remote I/O modules over an EtherNet/IP network, the range is 2.0…750 ms and the RPI must be configured in 1.0 ms increments. That is, you can’t set the RPI to a value of 2.3 ms. It must be 2.0 or 3.0. |
| Module definition                                               | Set of configuration parameters that affect data transmission between the controller and the I/O module. The parameters include the following: • Series - Hardware series of the module. • Revision - Major and minor firmware revision levels that are used on the module. • Electronic Keying - See LOGIX-AT001 for Electronic Keying information. • Connection - Type of connection between the controller that writes the configuration and the I/O module, such as Output. • Data format - Type of data that is transferred between the controller and I/O module and what tags are generated when the configuration is complete.                                                                                                                                                            |
| Major Fault on Controller If Connection Fails While in Run Mode | This option determines how the controller is affected if the connection to an I/O module fails in Run mode or if the controller is unable to establish a connection to the module. You can configure the project so that a connection failure causes a major fault on the controller or not. The default setting is for the option to be disabled. For example, if this option is enabled and an I/O module is removed while in Run mode, a major fault occurs on the controller. The default setting for the embedded I/O module is that this option is enabled. The default setting for local expansion modules is that this option is disabled.                                                                                                                                                |

## I/O Connections

A CompactLogix 5370 L1 control system uses connections to transmit I/O data. This table describes the connection types.

| IMPORTANT   | You can only use direct connections with the local expansion modules in a CompactLogix 5370 L1 control system.   |
|-------------|------------------------------------------------------------------------------------------------------------------|

## CompactLogix 5370 L1 Control System I/O Module Connections

| Connection     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct         | A direct connection is a real-time, data-transfer link between the controller and an I/O module. The controller maintains and monitors the connection. Any break in the connection, such as a module fault, causes the controller to set fault status bits in the data area that is associated with the module. Typically, analog I/O modules, diagnostic I/O modules, and specialty modules require direct connections.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Rack-optimized | Rack-optimized connections aren’t available with local expansion modules that are used in CompactLogix 5370 L1 control systems. For digital I/O modules, you can select rack-optimized connections. This option is used with distributed I/O modules and the Rack Optimization connection selection is made when configuring the remote adapter. For example, if you want to use a rack-optimized connection with digital I/O modules in a remote 1734 POINT I/O system, you configure the 1734-AENT(R) module to use a connection type of Rack Optimization. A rack-optimized connection consolidates connection usage between the controller and all digital I/O modules in a remote chassis or on one DIN rail. Rather than having individual, direct connections for each I/O module, there’s one connection for the entire rack (or DIN rail). |

## Configure Distributed I/O Modules on an EtherNet/IP Network

Your CompactLogix 5370 L1 control system can use distributed I/O modules on an EtherNet/IP network.

## IMPORTANT

When adding distributed I/O modules, remember to count the remote Ethernet adapter to remain within the maximum number of EtherNet/IP network nodes limitation for your controller.

The distributed I/O modules that are connected to the controller via the remote Ethernet adapter aren't counted toward the maximum Ethernet node limit for the controller.

For example, a 1769-L16ER-BB1B controller supports up to four Ethernet nodes. You can add up to four remote Ethernet adapters to the I/O Configuration section because each remote adapter counts against the node count. However, you can add as many remote I/O modules to the chassis of the adapter as necessary. Remote I/O modules do not count against the node count.

For more information on node limitations, see page 102 .

Complete these steps to configure distributed I/O modules on an EtherNet/IP network.

1. Right-click Ethernet and select New Module.
2. Select the desired Ethernet adapter and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. Configure the new Ethernet adapter as necessary and select OK.
4. Right-click the new adapter and select New Module.
5. Select the desired I/O module and select Create.

<!-- image -->

<!-- image -->

<!-- image -->

The New Module dialog box appears.

6. Configure the new I/O module as necessary and select OK.
7. To add all desired distributed I/O modules to the project, repeat these steps.

<!-- image -->

The following graphic is an example of a 1769-L18ERM-BB1B control system that uses distributed I/O modules over an EtherNet/IP network.

<!-- image -->

## Monitor I/O Modules

With CompactLogix 5370 L1 controllers, you can use the following options to monitor I/O modules:

- QuickView™ Pane below the Controller Organizer
- Connection tab in the Module Properties dialog box
- Programming logic to monitor fault data so you can act

When a fault occurs on an I/O module, a yellow triangle on the module listing in the Controller Organizer alerts you to the fault.

<!-- image -->

The following graphic shows the Quick View Pane, which indicates the type of fault.

<!-- image -->

To see the fault description on the Connection tab in Module Properties dialog box, complete these steps.

1. In the I/O Configuration, right-click the faulted I/O module and select Properties.

<!-- image -->

2. To diagnose the issue, select the Connection tab and use the fault description, in the Module Fault section.
3. To close the dialog box and remedy the issue, select OK.

<!-- image -->

## Bus Off Detection and Recovery

When the POINTBus backplane experiences a bus off condition, the CompactLogix 5370 L1 controller indicates this condition via a BUS OFF minor fault (Type 03, Code 01). When this fault occurs, the connections between the controller and I/O modules are broken.

Complete these steps to identify the source of the BUS OFF minor fault.

1. Make sure the number of local expansion modules in the project matches the number of modules that are physically installed in the system.
2. Make sure that all mounting bases are locked and I/O modules are securely installed on mounting bases.
3. Make sure all 1734 POINT I/O modules are configured to use the Autobaud rate.

IMPORTANT

You can't change the Autobaud setting for a 1734 POINT I/O when the module is installed in a CompactLogix 5370 L1 control system.

If you must return a 1734 POINT I/O module to Autobaud, see the POINT I/O Digital and Analog Modules and POINTBlock I/O Modules, publication 1734-UM001.

If these steps do not remedy the fault condition, contact Rockwell Automation® technical support.

## Select I/O Modules

<!-- image -->

## Use I/O Modules with CompactLogix 5370 L2 Controllers

This chapter details the I/O module options CompactLogix™ 5370 L2 control systems offer.

## Embedded I/O Modules

CompactLogix 5370 L2 controllers provide embedded I/O modules. The catalog number determines the number and type of points. This table describes which embedded I/O modules CompactLogix 5370 L2 controllers support.

| Cat. No.                              | Sinking/ Sourcing 24V DC Digital Input Points   | Sourcing 24V DC Digital Output Points   | High-speed Counters   | High-speed Counter Output Points   | Universal Analog Input Points   | Analog Output Points   |
|---------------------------------------|-------------------------------------------------|-----------------------------------------|-----------------------|------------------------------------|---------------------------------|------------------------|
| 1769-L24ER-QB1B                       |                                                 | 16 16                                   |                       | - - --                             |                                 |                        |
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK |                                                 | 16 16                                   |                       | 4 4 42                             |                                 |                        |
| 1769-L27ERM-QBFC1B                    |                                                 | 16 16                                   |                       | 4 4 42                             |                                 |                        |

## IMPORTANT

Remember the following when using the embedded I/O modules on CompactLogix 5370 L2 controllers:

- 1769-L24ER-QB1B controller - The digital input points and digital output points are on one embedded I/O module. Therefore, the 1769-L24ER-QB1B controller is considered to have one embedded I/O module.
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers - The digital input points and digital output points are on one embedded I/O module. The high-speed counter input/output points, universal analog input points, and analog output points are on another single embedded I/O module. Therefore, the 1769-L24ER-QBFC1B, 1769L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers are considered to have two embedded I/O modules.

You configure an RPI rate for the embedded I/O modules to establish the time intervals at which data is transmitted between the controller and each embedded I/O point. The available RPI range of the embedded I/O points is 0.5 … 750.0 ms and can be changed by 0.5 ms increments. The default setting is 20 ms.

## IMPORTANT

- If you attempt to use an RPI value that is not valid, the application automatically rounds the value down to the closest 0.5 ms increment when you apply the change.
- For example, if you set the RPI = 1.75 ms, when you select Apply or OK, the value is rounded down to 1.5 ms and applied.
- The RPI value for an embedded I/O module is intended to establish a time interval at which data is transmitted. However, the configuration of your CompactLogix 5370 L2 control system can affect the actual time interval of data transmission.

For more information regarding estimating the RPI value, see page 175 .

## Embedded Digital I/O Points

The embedded digital I/O module on CompactLogix 5370 L2 contains 16 24V DC sinking inputs and 16 24V DC sourcing outputs. The inputs can be configured to use digital filtering by input group. Filter times can be specified for OFF to ON and ON to OFF.

Group 0 is used to configure inputs 0…7. Group 1 is used to configure inputs 8…15. The default filter time for each group is 8 ms. You can adjust the filter times to 0.0 ms, 0.1 ms, 0.5 ms, 1.0 ms, 2.0 ms, and 4.0 ms, as shown in this graphic.

<!-- image -->

IMPORTANT The embedded digital I/O points on the 1769-L24ER-QBFC1B and 1769L27ERM-QBFC1B controllers are organized and wired the same.

## CompactLogix 5370 L2 Controllers Embedded Digital I/O Module Wiring Termination Points

<!-- image -->

## CompactLogix 5370 L2 Controllers Embedded Digital Input Point Wiring Diagram

+ DC (Sinking)
- DC (Sourcing)

<!-- image -->

## CompactLogix 5370 L2 Controllers Embedded Digital Output Point Wiring Diagram

<!-- image -->

## Embedded Analog I/O Points

## IMPORTANT

The embedded analog I/O points are available on only the 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers.

The 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers support four embedded universal analog inputs that can function as differential or single-ended inputs. This capability applies only if you do not use RTDs. If you use RTDs in your system, you can use up to two RTDs or a combination of one RTD and two universal analog inputs. The 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers also support two embedded standard analog outputs that can function as single-ended outputs. The inputs and outputs are considered channels. Each channel configuration offers multiple configuration options.

This table lists the available embedded analog input channel types and ranges for the channel type. The configuration choices are made on the Input Configuration tab of the Module Properties dialog box, as shown.

## Input Types and Ranges

<!-- image -->

This figure shows the embedded analog I/O points and how each termination point is used with different analog input types.

## IMPORTANT

The embedded analog I/O points on the 1769-L24ER-QBFC1B and 1769L27ERM-QBFC1B controllers are organized and wired the same.

## 1769-L27ERM-QBFC1B Controller Embedded Analog I/O Wiring Termination Points

<!-- image -->

<!-- image -->

<!-- image -->

This figure shows an example of ungrounded and grounded thermocouple wiring diagrams on a 1769-L27ERM-QBFC1B controller.

## 1769-L27ERM-QBFC1B Controller Thermocouple Wiring Diagrams

## Ungrounded Thermocouple

<!-- image -->

## IMPORTANT

## Grounded Thermocouple

<!-- image -->

You must order Cold Junction Connectors, catalog number 1769-CJC, separately from the CompactLogix 5370 L2 controllers.

This figure shows an example of devices with differential connections that are wired to the embedded analog inputs on a 1769-L27ERM-QBFC1B controller when it's operating with voltage or current input types.

1769-L27ERM-QBFC1B Controller Differential Connections Diagrams

<!-- image -->

## IMPORTANT

For both input types, we recommend that you use Belden #8761 or equivalent cable.

This figure shows an example of devices with single-ended connections that are wired to the embedded analog inputs on a 1769-L27ERM-QBFC1B controller when it's operating with voltage or current input types.

1769-L27ERM-QBFC1B Controller Single-ended Connections Wiring Diagrams

Voltage Input Type Single-ended Voltage Connections

Current Input Type Single-ended Current Connections

<!-- image -->

## IMPORTANT

For single-ended connections, remember the following:

- For both input types, we recommend that you use Belden #8761 or equivalent cable.
- The mV ranges with the Voltage input type do not support single-ended encoder wiring.
- All commons are electrically tied together in the controller.
- If multiple power supplies are used, the commons must have the same reference.

This figure shows an example of 2-wire, 3-wire, and 4-wire RTD/Resistance wiring diagrams on a 1769-L27ERM-QBFC1B controller.

## 1769-L27ERM-QBFC1B RTD/Resistance Wiring Diagrams

<!-- image -->

IMPORTANT

For all wiring diagrams, we recommend that you use Belden #83503 or 9533 cable.

This table lists the available embedded analog output channel types and ranges for the channel type. The configuration choices are made on the Output Configuration tab of the Module Properties dialog box, as shown in the table.

## Output Types and Ranges

<!-- image -->

This figure shows an example of wiring input devices to the analog output points on the 1769L27ERM-QBFC1B controller when it's operating in voltage or current mode.

## 1769-L27ERM-QBFC1B Controller Analog Output Wiring Diagrams

<!-- image -->

## Embedded High-speed Counters

## IMPORTANT

The embedded high-speed counters are available on only the 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers.

The 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers support four embedded highspeed counters. Each counter is a differential input. Therefore, two input terminals are required for one counter. For example, the A0+ and A0- terminals are required for counter A0.

The L2 embedded high-speed counters operate like the 1769-HSC module. See 1769-UM006 for further information.

Each counter uses differential inputs that are compatible with standard differential-line driver output devices and single-ended devices. This shows the embedded high-speed counter input points.

IMPORTANT The embedded high-speed counter points on the 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers are organized and wired the same.

## 1769-L27ERM-QBFC1B Controller Embedded High-speed Counter Wiring Termination Points

<!-- image -->

This figure shows an example of a differential encoder that is wired to the embedded highspeed counter inputs on a 1769-L27ERM-QBFC1B controller.

## 1769-L27ERM-QBFC1B Controller Differential Encoder with High-speed Counter Input Wiring Diagram

<!-- image -->

This figure shows an example of a single-ended encoder that is wired to the embedded highspeed counter inputs on a 1769-L27ERM-QBFC1B controller.

1769-L27ERM-QBFC1B Controller Single-ended Encoder with High-speed Counter Input Wiring Diagram

<!-- image -->

The embedded high-speed counter also supports four output points. This figure shows a wiring diagram for the embedded high-speed counter output points.

IMPORTANT

The embedded high-speed counter points on the 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B controllers are organized and wired the same.

## 1769-L27ERM-QBFC1B Controller Embedded High-speed Counter Output Wiring Diagram

<!-- image -->

## Wiring the Embedded I/O Modules

Complete these steps to wire the input and output points on the CompactLogix 5370 L2 controller.

1. Verify that the control system isn't powered.
2. Strip 10 mm (0.39 in.) insulation from the end of the wire.
3. Push the wire into the open terminal until it's secure.
4. If your wire is too thin to push into the open terminal for secure placement, we recommend that you connect the wire to a ferrule and insert it into the open terminal.
4. Repeat step 3 for all embedded I/O wires that are needed in your application.

<!-- image -->

To remove a wire from the removable connector, complete these steps.

1. Verify that the control system isn't powered.
2. Use a small screwdriver to push the spring release clip and pull out the wire.

<!-- image -->

You can use a continuity tester to determine if the connection point is operating correctly, that is, the connection point is a complete circuit. You use a continuity tester if any issues arise with a removable connector and you suspect that a connection point can no longer be functioning as a complete circuit.

The indication mechanism, for example, a light that illuminates on the tester, varies by continuity tester. The following example graphic shows a continuity tester with one connection point. In this case, if the circuit is operating correctly, the indicator light turns on.

Insert a continuity tester into the suspected I/O connection point as shown in the following graphic.

<!-- image -->

## Remove and Replace the Connector

Complete these steps to remove and replace an embedded I/O module connector.

1. Verify that the control system isn't powered.
2. Compress the small release clips at the top and bottom of the connector and tilt the top of the connector away from the module.
3. Pull the connector away from the module and disconnect any wires.
4. Connect the wires to the replacement connector.
5. Push the connector back into the module and engage the clips to secure the connector.

<!-- image -->

## Determine Embedded Module Update Time

## IMPORTANT

This section applies to the 1769-L24ER-QBFC1B and 1769-L27ERMQBFC1B controllers because only those controllers have embedded universal analog input points.

The module update time is the time that the module requires to sample and convert the input signals of all enabled analog input channels and provide the resulting data values to the controller.

You calculate the module update time by adding the update times for each enabled analog input channel on the module. Each channel update time calculation is the result of several configuration choices that are described in the following section.

## Channel Update Times

A combination of the update times that are detailed in this section determines the channel update time for an enabled analog input channel.

Channel Input Type and Filter Frequency Selection Update Time

When you enable an embedded analog input channel, you must select an input type and a filter frequency for that input. The selections that you make determine the value that is required when calculating channel update time.

## IMPORTANT

Each channel input type has multiple ranges or types. For example, a voltage input type can use one of six voltage ranges. Regardless of which voltage range the channel uses, the channel update time remains the same.

This table shows the channel update times for each channel input type and filter frequency selection.

## Channel Update Times

| Filter Frequency Selection(1) Channel Update Times Based on Input Type Selection Voltage, Current, or Thermocouple Input Type  Resistance or RTD Input Type   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10 Hz 307 ms 614 ms                                                                                                                                           |
| 50 Hz 67 ms 134 ms                                                                                                                                            |
| 60 Hz 57 ms 114 ms                                                                                                                                            |
| 250 Hz 19 ms 38 ms                                                                                                                                            |
| 500 Hz 13 ms 26 ms                                                                                                                                            |
| 1 kHz 11 ms 22 ms                                                                                                                                             |

## Cold Junction Compensation Update Times

You must account for more voltage at the junction of the thermocouple field wires and the input point. This condition applies when you use any of the thermocouple input types on your embedded analog input. More voltage can alter the input signal on that point and, therefore, affect the update time of that channel.

The process to account for increased voltage at an input point by using a thermocouple type input is cold junction compensation (CJC). You enable CJC for a given channel on the Input Configuration tab of the Module Configuration dialog box, as shown in the following graphic.

By default, CJC is disabled. You must clear the Disable Cold Junction Compensation checkbox to use CJC for a given channel.

<!-- image -->

You aren't required to enable CJC for a channel by using the thermocouple input type. If you enable CJC and select Update Cold Junction Compensation every other scan, an extra update time exists on the channel. This extra update time increases the overall channel update time.

The filter frequency selection for the channel determines the CJC update time. This table shows the CJC update times that are based on filter frequency selections.

## Channel Update Times

| Filter Frequency Selection (1)   | CJC Update Time   |
|----------------------------------|-------------------|
|                                  | 10 Hz 614 ms      |
|                                  | 50 Hz 134 ms      |
| 60 Hz                            | 114 ms            |
| 250 Hz                           | 38 ms             |
| 500 Hz                           | 26 ms             |
| 1 kHz                            | 22 ms             |

## IMPORTANT

Keep the following in mind when calculating the CJC update time:

- If multiple input channels are configured to use a thermocouple input type and another filter value is selected for each, the filter frequency selection with the slowest update time determines the CJC update time. For example, if one input channel uses a thermocouple input with a 50 Hz filter frequency and another input channel uses a thermocouple input with a 60 Hz filter frequency, the CJC channel update time is 134 ms.
- The CJC update time that increases overall module update time is only used once regardless of the number of input channels on a module that have CJC enabled to scan every other scan. In other words, if your module uses a filter frequency selection of 250 Hz and includes three channels with CJC enabled to scan every other scan, you add only one instance of CJC update time to the overall equation. Instead of including 38 ms for each channel, you include 38 ms once.

## Open Circuit Detection Update Time

Open circuit detection is used to verify that the field wiring is physically connected to the embedded analog input point. If this feature is enabled and the field wiring is disconnected from the input, the application alerts you to the condition and an open wire bit is set for the respective input channel in the tags for the project.

Open circuit detection can be enabled or disabled on any channel input type except for an input channel that is configured to use the 0…20 mA input range. The configuration selection is made on the Input Configuration tab on the Module Properties dialog box, as shown in the following graphic. The configuration choice, that is, enabled or disabled, is the result of an Open Circuit Response selection for the channel.

To disable open circuit detection, select Disable. To enable open circuit detection, select any of the other four options.

<!-- image -->

This table describes the module response that is associated with each enable selection.

## Open Circuit Detection Response Definitions

| Response Option Definition   |                                                                                                                                                            |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upscale                      | Sets the input data value to the full upper-scale value of the channel data word. The selected input type and data format determines the full-scale value. |
| Downscale                    | Sets the input data value to full lower-scale value of channel data word. The selected input type and data format determines the low scale value.          |
|                              | Last State Sets the input data value to the last input value before the detection of the open-circuit.                                                     |
| Zero                         | Sets the input data value to 0 to force the channel data word to 0.                                                                                        |

When you enable open circuit detection for an input channel, an extra update time is used to calculate the overall channel type. The increase in channel update time is 11 ms for each channel that enables open circuit detection response.

This table lists example module update times that are based on channel configurations.

## Example Module Update Times

| Example Enabled Analog Input Channel Configuration                                                                                                                                                                                                                                                                                                                         | Channel Update Time Calculations                                                                                                                                                                                                                         | Module Update Time   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| • Channel 0: – Input type = Current – Filter Frequency Selection = 60 Hz                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                          | 57 ms 57 ms          |
| • Channel 0: – Input type = Current – Filter Frequency Selection = 60 Hz • Channel 2: – Input type = RTD – Filter Frequency Selection = 60 Hz                                                                                                                                                                                                                              | Channel 0 update time + Channel 2 update time 57 ms + 114 ms                                                                                                                                                                                             | 171 ms               |
| • Channel 0: – Input type = Voltage – Filter Frequency Selection = 60 Hz – Open Circuit Detection = Enabled • Channel 2: – Input type = RTD – Filter Frequency Selection = 10 Hz                                                                                                                                                                                           | (Channel 0 update time + Open Circuit Detection time) + Channel 2 update time (57 ms + 11 ms) + 614 ms                                                                                                                                                   | 682 ms               |
| • Channel 0: – Input type = RTD – Filter Frequency Selection = 10 Hz – Open Circuit Detection = Enabled • Channel 2: – Input type = Thermocouple – Filter Frequency Selection = 60 Hz – CJC = Enabled – Open Circuit Detection = Enabled • Channel 3: – Input type = Thermocouple – Filter Frequency Selection = 500 Hz – CJC = Enabled – Open Circuit Detection = Enabled | (Channel 0 update time + Open Circuit Detection time) + (Channel 2 update time + Open Circuit Detection time) + (Channel 3 update time + Open Circuit Detection time) + CJC Update time (614 ms + 11 ms) + (57 ms + 11 ms) + (13 ms + 11 ms) + 114 ms(1) | 831 ms               |

## Embedded Analog I/O Modules Data Arrays

The section describes the data table structures for the embedded analog I/O modules on the CompactLogix 5370 L2 controllers. The embedded analog

I/O modules have arrays for the following data:

- Input data
- Output data
- Configuration data

You can access the data via the tags in the application.

## IMPORTANT

The analog I/O modules data structures apply to only the 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers.

The 1769-L24ER-QB1B controller does not have an embedded analog I/O module.

## Where:

## Input Array

The input data array for the embedded analog I/O module contains 11 words as described in this table. This array is read-only and the default value for all bits is 0.

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Input Data Array

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0        | Word                                                    |                                              |                                                                   |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |
|----------------------------------------------|---------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0            | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0                      | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 | 0 S Analog Read (Input) Data Value Channel 0 |
| 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1            | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1                      | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 | 1 S Analog Read (Input) Data Value Channel 1 |
| 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2            | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2                      | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 | 2 S Analog Read (Input) Data Value Channel 2 |
| 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3            | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3                      | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 | 3 S Analog Read (Input) Data Value Channel 3 |
| 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                                    | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                                              | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         | 4 Nu Timestamp Value                         |
|                                              | 5 Nu UI4 OI4 OC4 OC3 OC2 OC1 OC0 Nu SI4 SI3 SI2 SI1 SI0 |                                              |                                                                   |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |
|                                              |                                                         |                                              | 6 LI3 HI3 UI3 OI3 LI2 HI2 UI2 OI2 LI1 HI1 UI1 OI1 LI0 HI0 UI0 OI0 |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |
| 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value                    | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value                              | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         | 7 S Cold Junction Compensation Value         |
| 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0                 | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0                           | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      | 8 S Output Data Loopback/Echo Channel 0      |
| 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1                 | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1                           | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      | 9 S Output Data Loopback/Echo Channel 1      |
|                                              |                                                         | 10 Nu UO1 OO1 Nu UO0 OO0 Nu SO1 SO0          | 10 Nu UO1 OO1 Nu UO0 OO0 Nu SO1 SO0                               | 10 Nu UO1 OO1 Nu UO0 OO0 Nu SO1 SO0          | 10 Nu UO1 OO1 Nu UO0 OO0 Nu SO1 SO0          | 10 Nu UO1 OO1 Nu UO0 OO0 Nu SO1 SO0          |                                              |                                              |                                              |                                              |                                              |                                              |                                              |                                              |

Analog Read (Input) Data Value Channel x is the data that is read from the field device that is connected to the channel.

## Timestamp Value is the timestamp of when data was received at the corresponding channel.

Cold Junction Compensation value is the converted CJC data. The data is calculated in the following manner:

- If the CJC is open, the converted value is 25 °C (77 °F).
- If the CJC isn't opened and the Update CJC sensor every other scan option is disabled, the converted value is 25 °C (77 °F).
- If the CJC isn't opened and the Update CJC sensor every other scan option is enabled, the converted value is the measured temperature.

S Sign bit

|     | Nu Bit not used                                                                                                                                                                                                                                                                                              |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SIx | General status bit for an input channel. Bits 0…3 are for input channels. Bit 4 is for CJC. If the bit is 0, the channel is operating normally. If the bit is 1, a fault has occurred on the channel.                                                                                                        |
| OIx | Overrange alarm bit for an input channel. 0 = Channel is operating normally 1 = Input signal is over normal range.                                                                                                                                                                                           |
| UIx | Underrange alarm bit for an input channel. 0 = Channel is operating normally 1 = For bits 0…3, that is, input channels, the input signal is under the normal range. For bit 4, that is, channel using the thermocouple/mV, RTD/Resistance input type, the input value equals the minimum value of the range. |
| HIx | High alarm bit for an input channel 0. 0 = Channel is operating normally 1 = Input signal is above the user-defined range                                                                                                                                                                                    |
| LIx | Low alarm bit for an input channel 0. 0 = Channel is operating normally 1 = Input signal is below the user-defined range.                                                                                                                                                                                    |
| OCx | Open circuit detection bit. 0 = Channel isn’t experiencing an open circuit condition 1 = Channel is experiencing an open circuit condition                                                                                                                                                                   |
| SOx | General status bit for output channel 0 or 1. 0 = Channel operating normally 1 = A fault has occurred on the channel                                                                                                                                                                                         |
| OOx | Overrange alarm bit for output channel 0 or 1. 0 = Channel is operating normally 1 = Output signal is over the normal range                                                                                                                                                                                  |
| UOx | Underrange alarm bit for output channel 0 or 1. 0 = Channel is operating normally 1 = Output signal is below the normal range                                                                                                                                                                                |

## Output Array

The embedded analog I/O output image array of the module contains four words as described in this table. This array is write-only and the default value for all bits is 0.

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Output Data Array

| Bit                                                                            | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       | Bit                                                                                                                       |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Word                                                                           |                                                                                                                           | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                     |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |
|                                                                                | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    | 0 S Analog Output Data Value Channel 0                                                                                    |
|                                                                                | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    | 1 S Analog Output Data Value Channel 1                                                                                    |
| 2 Nu                                                                           |                                                                                                                           | CL I3                                                                                                                     | CH I3                                                                                                                     | CL I2                                                                                                                     | CH I2                                                                                                                     | CL I1                                                                                                                     | CH I1                                                                                                                     | CL I0                                                                                                                     | CH I0                                                                                                                     |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |
| 3 Nu                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           | CL O1                                                                                                                     | CH O1                                                                                                                     | CL O0                                                                                                                     | CH O0                                                                                                                     |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |                                                                                                                           |
| Analog Output Data Value Channel x is the data that is written to the channel. | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            | Analog Output Data Value Channel x is the data that is written to the channel.                                            |
|                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                | S Sign bit                                                                                                                |
|                                                                                | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           | Nu Bit not used                                                                                                           |
| CH Ix                                                                          | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel High Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch  |
| Where: CL Ix                                                                   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   | Use this bit to cancel Low Process Alarm Latch functionality for an input. 0 = Do not cancel 1 = Cancel the alarm latch   |
| CH Ox                                                                          | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch | Use this bit to cancel High Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch |
| CL Ox                                                                          | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  | Use this bit to cancel Low Process Alarm Latch functionality for an output. 0 = Do not cancel 1 = Cancel the alarm latch  |

## Configuration Array

The embedded analog I/O configuration image array of the module contains 43 words as described in this table.

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Configuration Image Array

| Word  Bit  15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0  0 Real Time Sample Value  1 ETS Nu  2 EC Nu EA AL EI EO Open Circuit Ch0 0V Adj Filter Setting ChI0  3 Wire &amp; CLCD TU ChIo Nu Inpt Dta Fm ChI0 Nu Inpt Tp/RngeSel ChI0  4 S Process Alarm High Data Value Universal Input Channel 0  5 S Process Alarm Low Data Value Universal Input Channel 0  6 S Alarm Dead Band Value Universal Input Channel 0  7 Nu  8 EC Nu EA AL EI EO Open Circuit ChI 1 0V Adj Filter Setting ChI1  9 Nu TU ChI1 Nu Inpt Dta Fm ChI1 Nu Inpt Tp/RngeSel ChI1  10 S Process Alarm High Data Value Universal Input Channel 1  11 S Process Alarm Low Data Value Universal Input Channel 1  12 S Alarm Dead Band Value Universal Input Channel 1  13 Nu  14 EC Nu EA AL EI EO Open Circuit ChI 2 0V Adj Filter Setting ChI2  15 Wire &amp; CLCD TU ChI1 Nu Inpt Dta Fm ChI2 Nu Inpt Tp/RngeSel ChI2  16 S Process Alarm High Data Value Universal Input Channel 2  17 S Process Alarm Low Data Value Universal Input Channel 2   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Configuration Image Array (Continued)

18 S Alarm Dead Band Value Universal Input Channel 2

19 Nu

20 EC Nu

EA AL EI EO Open Circuit ChI 3 0V Adj Filter Setting ChI3

21 Nu

TU ChI1 Nu

Inpt Dta Fm ChI3 Nu

Inpt Tp/RngeSel ChI3

22 S Process Alarm High Data Value Universal Input Channel 3

23 S Process Alarm Low Data Value Universal Input Channel 3

24 S Alarm Dead Band Value Universal Input Channel 3

25 Nu

26 CJC Ses

Cycle

Calib

Nu CJC WP Nu

TU CJC

27 Nu

28 EC NU

EHI ELI LC ER FM PM Nu PFE

29 Nu

Outpt Fm ChI0

Nu

Outpt Tp/RngeSel Ch0

30 S Fault Value Channel 0

31 S Program (Idle) Value Channel 0

32 S Clamp High Data Value Channel 0

33 S Clamp Low Data Value Channel 0

34 S Ramp Rate Channel 0

35 Nu

36 EC Nu

EHI ELI LC ER FM PM Nu PFE

37 Nu

Outpt Fm ChI1

Nu

Outpt Tp/RngeSel ChI1

38 S Fault Value Channel 1

39 S Program (Idle) Value Channel 1

40 S Clamp High Data Value Channel 1

41 S Clamp Low Data Value Channel 1

42 S Ramp Rate Channel 1

Word

Bit

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Configuration Image Array (Continued)

| Bit              | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 | Bit                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| EC               | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                | Use to enable or disable a channel. Each channel can be individually enabled. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                |
| Inpt Dta FM CHIx | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             | Use this bit to select the form in which the analog data is returned to the controller and used in the control program.                                                                                                                                                                                                                                             |
| EA               | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           | Use this bit to enable or disable the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                           |
| AL               | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          | Use this bit to enable or disable alarm latching on the process alarm of a channel. 0 = No latch 1 = Latch                                                                                                                                                                                                                                                          |
| EI               | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             | Use this bit to enable or disable interrupts on the process alarms of a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                             |
| EO               | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   | Use this bit to enable or disable Open Circuit functionality on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                   |
| Open Circuit Chx | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               | Use to set the Open Circuit Response for a channel. 0 = Upscale 1 = Downscale 2 = Last State 3 = Zero                                                                                                                                                                                                                                                               |
| OV adjust        | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). | CJC is performed by default by taking the CJC sensor temperature value for a given channel, converting that to a thermocouple voltage, and adding that voltage from the measured value before converting to a user value. If this bit is set for a given channel, the signal value is directly converted to a user value (No cold junction compensation performed). |
| Wire & CLCD      | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               | Use to set the wire mode. The combination of values in bits 14 and 15 determine the mode, as listed in the following table. Table 1 -                                                                                                                                                                                                                               |
| Wire & CLCD      |                                                                                                                                                                                                                                                                                                                                                                     | Bit 15 Value Bit 14 Value Mode                                                                                                                                                                                                                                                                                                                                      | Bit 15 Value Bit 14 Value Mode                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| Wire & CLCD      |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     | 0 0 3-wire and cycle lead compensation - Enable                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| Wire & CLCD      | 0                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                                                                                                                   | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        | 3-wire and cycle lead compensation - Disable                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| Wire & CLCD      | 1                                                                                                                                                                                                                                                                                                                                                                   | 0                                                                                                                                                                                                                                                                                                                                                                   | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       | 2-wire (No lead compensation)                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                     |
| TU Chx           | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     | Use to set the temperature units. 1 1  0 = Degrees Celsius 1 = Degrees Fahrenheit p 1  4 i (N l d ti )                                                                                                                                                                                                                                                                                                                                                                     |

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Configuration Image Array (Continued)

| Word          | Bit                                                                                                                                                                                                                                                                                                                                                        | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169 | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  | Inpt Dta Fm ChIx Use these bits to select the form the analog input data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the input data form that is used, see the Analog Input Data Format table on page 169                                                                                                  |
|               | Inpt Tp / Rnge Sel ChIx                                                                                                                                                                                                                                                                                                                                    | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            | Use these bits to select the input type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Input Type and Operating Range table on page 170 .                                                                                                                                                                                                            |
|               | Filter Setting Chx                                                                                                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         | Use these bits to select the filter setting for a channel. For more information on what selections determine the filter settings for a channel, see the Input Filter Selections table on page 169 .                                                                                                                                                                                                                                                         |
|               | Process Alarm High Data Value Channel x                                                                                                                                                                                                                                                                                                                    | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            | Use to configure the Process Alarm High value for a channel. Configuration is done by using words 4, 10, 16, and 22 to set the Alarm High value.                                                                                                                                                                                                                                                                                                            |
|               | Process Alarm Low Data Value Channel x                                                                                                                                                                                                                                                                                                                     | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               | Use to configure the Process Alarm Low value for a channel. Configuration is done by using words 5, 11, 17, and 23 to set the Low High value.                                                                                                                                                                                                                                                                                                               |
| Where (cont.) | Alarm Dead Band Data Value Channel x                                                                                                                                                                                                                                                                                                                       | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            | Use to configure the Alarm Deadband value for a channel. Configuration is done by using words 6, 12, 18, and 24 to set the deadband alarm value.                                                                                                                                                                                                                                                                                                            |
| Where (cont.) | ETS                                                                                                                                                                                                                                                                                                                                                        | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    | Use to enable or disable the timestamping function on the module. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                    |
| Where (cont.) | Real Time Stamp Value                                                                                                                                                                                                                                                                                                                                      | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   | Use to set the Real Time Sample value. The available range = 0 … 5000 ms.                                                                                                                                                                                                                                                                                                                                                                                   |
| Where (cont.) | UpdateC JCComp ensatio nEn                                                                                                                                                                                                                                                                                                                                 | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use this bit to enable or disable a CJC sensor. • If enabled, the CJC is read once every other module scan, and its value is updated in the CJC status word. This value is also used for thermocouple cold junction compensation. • If disabled, the CJC sensor value isn’t acquired, and the CJC temperature is fixed at 25 °C (77 °F) for all channels. The CJC is also fixed at 25 °C ° qp (77 °F) for all channels if it’s determined to be broken (short or open circuit). 0 = Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Where (cont.) | Cycle Calib                                                                                                                                                                                                                                                                                                                                                | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable | 1 = Enable Use this bit to enable Cycle Calibration. • If enabled, the internal calibration of the module occurs once every 5 minutes. • If disabled, the internal calibration of the module occurs only once at power on/ reset. Cycle Calibration enables the module to readjust for environmental changes such as variations in temperature. However, the module throughput is slightly reduced during the calibration operation. 0 = Disable 1 = Enable |

## CompactLogix 5370 L2 Controller Embedded Analog I/O Module Configuration Image Array (Continued)

| Word          | Bit                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Where (cont.) | CJC WP                          | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable | Use this bit to enable or disable the CJC Weighted Profile. • If enabled, the CJC temperature for each channel is scaled by multiplying the single CJC reading by a predefined scale factor that is derived from lab measurements of the stable temperature of each terminal block pin. In this condition, all channel data is overridden with the CJC temperature of that channel. • If disabled, the single CJC reading is applied directly to all channels. If the CJC sensors are installed in a remote terminal block, the weighted profile must be disabled. In this condition, channel data is presented in the input table as normal. 0 = Disable 1 = Enable |
| Where (cont.) | PFE                             | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Use this bit to select whether data from the Program/Idle m ode or the Fault Enable mode is applied. 0 = Program/Idle mode data applied 1 = Fault mode data applied                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Where (cont.) | ER                              | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to enable or disable ramping for each channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Where (cont.) | EHI                             | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Use this bit to enable or disable the output channel interrupt function when a High Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Where (cont.) | ELI                             | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to enable or disable the output channel interrupt function when a Low Clamp alarm is set. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Where (cont.) | PM                              | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Use this bit to set data a channel uses when it is in Program/Idle mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Where (cont.) | FM                              | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the data a channel uses when it is in Fault mode. 0 = Hold Last State value 1 = User-defined value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Where (cont.) | LC                              | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Use this bit to enable or disable latch functionality when Low/High clamp and Under/Over range alarm conditions exist on a channel. 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Where (cont.) | Outpt Dta Fm ChIx               | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       | Use these bits to select the form the analog output data is presented to the controller and used by the controller. The combination of multiple selections in words and bits determines this value. For more information on what selections determine the output data form that is used, see the Analog Output Data Format table on page 171 .                                                                                                                                                                                                                                                                                                                       |
| Where (cont.) | Outpt Tp / Rnge Sel ChIx        | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   | Use these bits to select the output type and operating range for a channel. For more information on what selections determine the input type and operating range for a channel, see the Analog Output Type and Operating Range table on page 171 .                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Where (cont.) | Fault Value Channel x           | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Use this bit to configure the Fault mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Where (cont.) | Program (Idle) Value Channel x  | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use this bit to configure the Program/Idle mode value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Where (cont.) | ClampHi gh Data Value Channel x | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Use this bit to configure the Clamp High data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Where (cont.) | Clamp Low Data Value Channel    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Use this bit to configure the Clamp Low data value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Where (cont.) | Ramp Rate Channel x             | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Use this bit to set the Ramp Rate value for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Input Filter Selections

This table lists the bit value combinations that you can use to select a filter setting for a channel. You use bits 0…3 in words 2, 8, 14, and 20 to make this selection.

## Input Filter Selections

| Filter Value   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   |
|----------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
|                | Bit 03 Bit 02 Bit 01 Bit 00             |                                         |                                         |
| 60 Hz          | 0000                                    |                                         |                                         |
| 50 Hz          | 0 0 0 1                                 |                                         |                                         |
| 10 Hz          | 0 0 1                                   |                                         |                                         |
| 250 Hz         | 0 0 1 1                                 |                                         |                                         |
| 500 Hz         | 0 1 0 0                                 |                                         |                                         |
| 1 kHz          | 0 1 0 1                                 |                                         |                                         |
| Spare (1)      | Values 6...15                           | Values 6...15                           | Values 6...15                           |

- (1) An attempt to write a non-valid (any Spare value) or Not Used bit configuration into the Input Filter Response Select field causes a Module Configuration Error (contained in the Mod\_Condition Array).

## Analog Input Data Format

This table lists the bit value combinations that you can use to select the output data format for analog data that is sent to the controller for a channel. You use bits 8…10 in words 3, 9, 15, and 21 to make this selection.

## Analog Input Data Format

| Analog Output Data Format   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   |
|-----------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
|                             | Bit 10 Bit 09 Bit 08                    |                                         |                                         |
| Raw/Proportional Data       | 0 0 0                                   |                                         |                                         |
| Engineering Units           | 0 0 1                                   |                                         |                                         |
| Engineering Units x 10      | 0 1 0                                   |                                         |                                         |
| Scaled for PID              | 0 1 1                                   |                                         |                                         |
| Percent Range               | 1 0 0                                   |                                         |                                         |
| Spare (1)                   | Values 5...7                            | Values 5...7                            | Values 5...7                            |

## Analog Input Type and Operating Range

This table lists the bit value combinations that you can use to select the input type and operating range for a channel. You use bits 0…5 in words 3, 9, 15, 21, 29, and 37 to make the selections.

## Analog Input Type and Operating Range

| Input Type and Normal Operating Range   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   | Bit Settings (Words 3, 9, 15, and 21)   |
|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
| Input Type and Normal Operating Range   |                                         | Bit 05 Bit 04 Bit 03 Bit 02 Bit Bit 00  |                                         |                                         |                                         |                                         |
| -10…10V DC                              |                                         | 000000                                  |                                         |                                         |                                         |                                         |
| 0…5V DC                                 |                                         | 000001                                  |                                         |                                         |                                         |                                         |
| 0…10V DC                                |                                         | 00001 0                                 |                                         |                                         |                                         |                                         |
| 4…20 mA                                 |                                         | 00001 1                                 |                                         |                                         |                                         |                                         |
| 1…5V DC                                 |                                         | 0001 00                                 |                                         |                                         |                                         |                                         |
| 0…20 mA                                 |                                         | 0001 01                                 |                                         |                                         |                                         |                                         |
| -50 mV…50 mv                            |                                         | 0 0 0 1 1 0                             |                                         |                                         |                                         |                                         |
| -100…+100 mV                            |                                         | 0 0 0 1 1 1                             |                                         |                                         |                                         |                                         |
| Thermocouple J                          |                                         | 001 000                                 |                                         |                                         |                                         |                                         |
| Thermocouple K                          |                                         | 001 001                                 |                                         |                                         |                                         |                                         |
| Thermocouple T                          |                                         | 001 01 0                                |                                         |                                         |                                         |                                         |
| Thermocouple E                          |                                         | 001 01 1                                |                                         |                                         |                                         |                                         |
| Thermocouple R                          |                                         | 001 1 00                                |                                         |                                         |                                         |                                         |
| Thermocouple S                          |                                         | 001 1 01                                |                                         |                                         |                                         |                                         |
| Thermocouple B                          |                                         | 001 1 1 0                               |                                         |                                         |                                         |                                         |
| Thermocouple N                          |                                         | 001 1 1 1                               |                                         |                                         |                                         |                                         |
| Thermocouple C                          |                                         | 0 1 0 0 0 0                             |                                         |                                         |                                         |                                         |
| 100  PT 385                            |                                         | 0 1 0 0 0 1                             |                                         |                                         |                                         |                                         |
| 200  PT 385                            |                                         | 0 1 0 0 1 0                             |                                         |                                         |                                         |                                         |
| 500  PT 385                            |                                         | 0 1 0 0 1 1                             |                                         |                                         |                                         |                                         |
| 1000  PT 385                           |                                         | 01 01 00                                |                                         |                                         |                                         |                                         |
| 100  PT 3916                           |                                         | 01 01 01                                |                                         |                                         |                                         |                                         |
| 200  PT 3916                           |                                         | 0 1 0 1 1 0                             |                                         |                                         |                                         |                                         |
| 500  PT 3916                           |                                         | 0 1 0 1 1 1                             |                                         |                                         |                                         |                                         |
| 1000  PT 3916                          |                                         | 0 1 1 0 0 0                             |                                         |                                         |                                         |                                         |
| 10  CU 426                             |                                         | 0 1 1 0 0 1                             |                                         |                                         |                                         |                                         |
| 120  Ni 618                            |                                         | 0 1 1 0 1 0                             |                                         |                                         |                                         |                                         |
| 120  Ni 672                            |                                         | 0 1 1 0 1 1                             |                                         |                                         |                                         |                                         |
| 604  NiFe 518                          |                                         | 01 1 1 00                               |                                         |                                         |                                         |                                         |
| 150                                    |                                         | 01 1 1 01                               |                                         |                                         |                                         |                                         |
| 500                                    |                                         | 01 1 1 1 0                              |                                         |                                         |                                         |                                         |
| 1000                                   |                                         | 01 1 1 1 1                              |                                         |                                         |                                         |                                         |
| 3000                                   |                                         | 1 00000                                 |                                         |                                         |                                         |                                         |

## Analog Output Data Format

This table lists the bit value combinations that you can use to select the output data format for analog data that is sent to the controller for a channel. You use bits 8…10 in words 29 and 37 to make this selection.

## Analog Output Data Format

| Analog Output Data Format   | Bit Settings (Words 29 and 37)   | Bit Settings (Words 29 and 37)   |            |
|-----------------------------|----------------------------------|----------------------------------|------------|
|                             |                                  | Bit 10 Bit 09 Bit 08             |            |
| Raw/Proportional Data       |                                  | 0 0 0                            |            |
| Engineering Units           |                                  | 0 0 1                            |            |
| Scaled for PID              | 0 1                              | 0                                |            |
| Percent Range               | 0 1                              | 1                                |            |
| Spare (1)                   | Values 4…7                       | Values 4…7                       | Values 4…7 |

## Analog Output Type and Operating Range

This table lists the bit value combinations that you can use to select the input type and operating range for a channel. You use bits 0…5 in words 29 and 37 to make the selections.

## Analog Output Type and Operating Range

| Output Type and Normal Operating Range   |        |                                        |
|------------------------------------------|--------|----------------------------------------|
| Output Type and Normal Operating Range   |        | Bit 05 Bit 04 Bit 03 Bit 02 Bit Bit 00 |
| -10…10V DC                               | 000000 |                                        |
| 0…5V DC 0 0 0 0 0 1                      |        |                                        |
| 0…10V DC 0 0 0 0 1 0                     |        |                                        |
| 4…20 mA 0 0 0 0 1 1                      |        |                                        |
| 1…5V DC 0 0 0 1 0 0                      |        |                                        |
| 0…20 mA 0 0 0 1 0 1                      |        |                                        |

## Local Expansion Modules - Optional

CompactLogix 5370 L2 control systems support the use of Compact I/O™ modules as local expansion modules along a CompactBus backplane:

- The controllers support as many as four Compact I/O modules as local expansion modules.
- When possible, use specialty Compact I/O modules to meet unique application requirements.
- Consider using a 1492 wiring system for each I/O module as an alternative to the terminal block that comes with the module.
- Use 1492 PanelConnect™ modules and cables if you're connecting input modules to sensors.
- Install local expansion modules in the same local bank as the CompactLogix 5370 L2 controller.

## Install Local Expansion Modules

Complete these steps to install local expansion modules in your CompactLogix 5370 L2 control system.

1. Attach the Compact I/O modules as described in these publications:
- Compact I/O Modules Installation Instructions, publication 1769-IN088
- Compact I/O DeviceNet® Scanner Module Installation Instructions, publication 1769-IN060
2. Use the tongue-and-groove slots to attach a 1769-ECR Compact I/O end cap terminator to the last module in the system.
3. Move the lever of the end cap bus terminator fully to the left until it clicks to lock the end cap bus terminator.

## Wire Local Expansion Modules

Wire each Compact I/O module that is used as a local expansion module according to the technical documentation for that module.

## Distributed I/O Modules over an EtherNet/IP Network

You can include distributed I/O modules over an EtherNet/IP™ network in your CompactLogix 5370 L2 control system.

Consider these points when using distributed I/O modules over an EtherNet/IP network:

- Each remote EtherNet/IP adapter included in the system must be counted toward the maximum number of EtherNet/IP nodes of the controller.

For more information on maximum number of EtherNet/IP nodes, see Chapter 6, page 102 .

- The configurable RPI settings vary depending on which distributed I/O modules are used in the system.
- For information to add distributed I/O modules to your CompactLogix 5370 L2 control system, see page 185 .

The following graphic shows a CompactLogix 5370 L2 control system on an EtherNet/IP network that uses all three I/O module options.

<!-- image -->

## Distributed I/O Modules over a DeviceNet Network

You can include distributed I/O modules over a DeviceNet network in your CompactLogix 5370 L2 control system.

You must use the following to use distributed I/O modules over a DeviceNet network in your CompactLogix 5370 L2 control system:

- Logix Designer application or the Studio 5000® environment - For more information, see page 182 .
- RSNetWorx™ for DeviceNet software - For more information, see page 185 .

The following graphic shows a CompactLogix 5370 L2 control system on a DeviceNet network that uses all three I/O module options.

<!-- image -->

## Validate I/O Layout

You must validate the layout of I/O modules in your CompactLogix 5370 L2 control system. Consider the points detailed in this section when validating I/O layout placement.

## Estimate Requested Packet Interval

The requested packet interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. You set an RPI rate for each I/O module in your system, including embedded I/O modules, local expansion modules, or distributed I/O modules over an EtherNet/IP network.

The CompactLogix 5370 L2 controllers attempt to scan an I/O module at the configured RPI rate. The controller scans distributed I/O modules at the configured RPI rates.

With embedded I/O modules and local expansion modules, however, some system configuration parameters determine the actual rate at which the controller scans the modules. That is, the controller can be configured to scan an I/O module at one rate but actually scan the module at another rate.

For individual I/O modules, a module RPI overlap minor fault (further described on page 176) occurs if there is at least one I/O module that can't be serviced within its RPI time.

The configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can affect the effective scan frequency for any individual embedded or local expansion module:

- Rates at which RPI values are set for embedded I/O modules
- Number of embedded I/O modules that are used in the system
- Types of embedded I/O modules that are used in the system
- Rates at which RPI values are set for Compact I/O modules
- Number of Compact I/O modules in the system
- Types of Compact I/O modules in the system
- Application user task priorities

## Requested Packet Interval Rate Guidelines

| Type of Module Guidelines(1)            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All digital                             | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…30 modules can be scanned in 2 ms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Mix of digital and analog or all analog | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…13 modules can be scanned in 2 ms. • 14…30 modules can be scanned in 3 ms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Specialty                               | The following conditions apply: • For every 1769-SDN module in the system, increase every RPI by 2 ms for every other module. • For every 1769-HSC module in the system, increase every RPI by 1 ms for every other module. • For every 1769-ASCII module in the system, increase every RPI by 1 ms for every other module. • For every 1769-SM2 module in the system, increase every RPI by 2 ms for every other module.                                                                                                                                                                                                                                             |
|                                         | (1) The guidelines in this table do not factor in the following items, which affect the CMX5370 controller CPU loading: I/O RPI timing does not affect the task priority. Event and periodic tasks have higher priority than I/O and user tasks. IOT (Immediate Output Instruction) Messaging CompactBus browsing such as accessing DeviceNet network through 1769-SDN using CMX5370 Ethernet or USB connection. Module RPI guidelines can require adjustment (increase of 1 ms or more) if the CMX5370 controller application includes one or more of the listings in this table. Monitor controller minor faults to determine if Module RPI overlaps have occurred. |

| IMPORTANT   | When considering the number of I/O modules, remember that they can be the embedded I/O modules on the controller or Compact I/O modules that are used as local expansion modules. Therefore, the consideration for using modules can be any of the following system configurations: • Only embedded I/O modules • Only Compact I/O modules • Some combination of embedded I/O modules and Compact I/O modules   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

You can set the RPI rates higher for individual Compact I/O modules. The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Module Fault Related to RPI Estimates

When following the RPI rate guidelines, most CompactLogix 5370 L2 control systems operate as expected. Some systems that follow the guidelines can experience a Module RPI Overlap minor fault that is described in this table.

|                    |                                                                                                                                                           | Name Fault Information Condition in Which Fault Occurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module RPI Overlap | (Type 03) I/O fault (Code 94) Module RPI overlap detected Module Slot = x , where x is the slot number of the I/O module in the I/O Configuration section | This fault is logged when the current RPI update of an I/O module overlaps with its previous RPI update. The Minor Faults tab in the Controller Properties dialog box indicates in which module the RPI overlap occurs. If multiple I/O modules experience the fault, the application indicates that the fault occurred on the first such I/O module. Typically, it’s an I/O module with large Input/Output array sizes. Example modules that use large Input/Output array sizes include the 1769-SDN and 1769-HSC modules. In these cases, we recommend that you adjust the RPI of the module to eliminate the fault. Once the fault is cleared from the first I/O module, the application indicates the next module that experiences the fault. This pattern continues until the fault is cleared from all affected I/O modules. To avoid this fault, set the RPI rate of the I/O modules to higher numerical values. We recommend that you use an RPI value that is not a common multiple of other module RPI values, such as 2.5 ms, 5.5 ms, or 7 ms: • We recommend that you do not run CompactLogix 5370 L2 control systems with Module RPI Overlap faults. • A system that experiences many Module RPI Overlap faults can’t operate optimally because I/O data isn’t sampled at the expected rate that RPI settings determine. • When the project is downloaded or the RPI value of a module is adjusted, it’s expected to have a minor fault. Faults under these conditions are transitionary. Clear the fault and wait for the fault to reappear before adjusting the RPI value or the task priorities. |

## System Power Availability

An embedded 24V DC Input, nonisolated power supply powers all components in a CompactLogix 5370 L2 control system.

The embedded power supply provides the following power to the CompactBus:

- 1769-L24ER-QB1B controller:
- 1.54 A @ 5V DC
- 0.95 A @ 24V DC
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers:
- 1 A @ 5V DC
- 0.8 A @ 24V DC

The embedded power supply can power any combination of controller, embedded I/O modules, and local expansion modules that are used in your application.

## Power Supply Distance Rating

In a CompactLogix 5370 L2 control system, you can install Compact I/O modules on as local expansion modules to the right of the controller system. Compact I/O modules each have a power supply distance rating that you must consider before you install them.

Power supply distance rating is the number of slots a Compact I/O module can be installed away from the power supply. If a Compact I/O module has a distance rating of three, you can include up to two modules between the Compact I/O module and the power supply.

Additionally, the controller has embedded I/O modules that are designed to protect against installation of a Compact I/O module directly to the right of the embedded power supply. CompactLogix 5370 L2 control systems have embedded I/O modules in the controller. CompactLogix 5370 L2 control systems have one or two embedded I/O modules as described as follows:

- 1769-L24ER-QB1B controller - one embedded I/O module
- 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, and 1769-L27ERM-QBFC1B controllers - two embedded I/O modules

The embedded I/O modules aren't considered local expansion modules. However, you must still include each embedded I/O module in the module slot count when determining where to install Compact I/O module as a local expansion module.

Because CompactLogix 5370 L2 control systems only allow up to four local expansion modules in the system, you can install most Compact I/O modules in any local expansion module slot. Some Compact I/O modules have power supply distance ratings that affect where you can install them in the CompactLogix 5370 L2 control system.

For example, the 1769-ASCII Compact ASCII and 1769-HSC Compact high-speed counter modules each have a power supply distance rating of four. The farthest local expansion module slot where you can install one of these modules in a CompactLogix 5370 L2 control system is module slot number two or three. The controller catalog number that is used in the control system determines the slot number.

This table describes the farthest local expansion module slot where you can install a 1769-HSC high-speed counter module and meet its power supply distance rating requirement.

## Example CompactLogix 5370 L2 Control Systems with a 1769-HSC High-speed Counter Module

<!-- image -->

## Example CompactLogix 5370 L2 Control Systems with a 1769-HSC High-speed Counter Module (Continued)

<!-- image -->

| Controller Cat. No.                                       | Number of Embedded I/O Modules   | 1769-HSC High-speed Counter Module Power Supply Distance Rating Calculation Impact                                                                                                                                                                                                                                                                                                                                                                                                                   | 1769-HSC High-speed Counter Module Power Supply Distance Rating Calculation Impact                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B | 2                                | The embedded I/O modules are the first two modules in the module count. At its maximum power supply distance rating, the 1769-HSC high-speed counter module can be installed in slot 2 of the local expansion modules, as shown here. Three modules between the power supply and the 1769-HSC high-speed counter module. With this controller catalog number, you can only install one local expansion module between the controller and the 1769-HSC high-speed counter. 1769-HSC High-speed Module | physical appearance and the appearance of the module in the application.                                                                                                                                                                                                                                                             |
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | /OConfiguration 1769Bus [0]1769-L27ERM-QBFC1BSample_project EmbeddedI/O [1]EmbeddedDiscrete_IO [2] EmbeddedAnalog_IO [3]EmbeddedCounters ExpansionI/0 [4]1769-IA81/AIsolated_digital input_m [5]1769-HSC/BHigh_speed_counter Ethernet 1769-L27ERM-QBFC1BSample_project                                                               |
| 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK, 1769-L27ERM-QBFC1B |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Modules [2] and [3] are shown separately but are considered one module when counting modules to meet power supply distance rating requirements. 1769-HSC high-speed counter module is shown as module [5] in this location but considered the fourth module when counting modules to meet power supply distance rating requirements. |

For more information about the power supply distance rating for a Compact I/O module, see CompactLogix Selection Guide, publication 1769-SG001.

Configure Local I/O Modules You can configure one of these types of local I/O modules in the programming software
i environment:

## Configure Embedded I/O Modules

Embedded I/O modules are automatically created in the I/O Configuration portion of the Controller Organizer. Complete these steps to configure an embedded I/O module in your CompactLogix 5370 L2 control system.

1. Right-click the embedded I/O module and select Properties.
2. Select the required tab, make the necessary changes, and select OK.

<!-- image -->

<!-- image -->

IMPORTANT

You can also use the tags to configure the embedded I/O modules of the CompactLogix 5370 L2 controller. When attempting to use the tags to make analog I/O module selections in the input, output, and configuration data arrays, the options are complicated.

## Configure Local Expansion Modules

Complete these steps to add a Compact I/O module to your CompactLogix 5370 L2 control system and configure it.

1. Right-click the 1769 Bus and select New Module.
2. Select the desired I/O module and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. Configure the new I/O module as necessary and select OK.

<!-- image -->

## Common Configuration Parameters

| Configuration Option                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requested packet interval (RPI)                                  | The RPI specifies the interval at which data is transmitted or received over a connection. For 1769 Compact Local I/O modules, data is transmitted to the controller at the RPI. When scanned on the local bus or over an EtherNet/IP network, input modules are scanned at the RPI specified in the module configuration. Typically, you configure an RPI in milliseconds (ms). For I/O modules, the range is 0.5…750 ms. When scanned over a DeviceNet network via a 1769-SDN scanner in the CompactLogix 5370 L2 control system, distributed input modules are scanned at the rate the DeviceNet adapter that connects the input modules to the network supports. For example, if your system includes a remote system of 1734 POINT I/O™ modules on a DeviceNet network, the 1769-SDN scanner can only scan the distributed 1734 POINT I/O modules as quickly as the 1734-ADN DeviceNet adapter can transmit the data. |
| Module definition                                                | Set of configuration parameters that affect data transmission between the controller and the I/O module. The parameters include the following: • Series - Hardware series of the module. • Revision - Major and minor firmware revision levels that are used on the module. • Electronic Keying - See LOGIX-AT001 for Electronic Keying information. • Connection - Type of connection between the controller writing the configuration and the I/O module, such as Output. • Data format - Type of data that is transferred between the controller and I/O module and what tags are generated when the configuration is complete.                                                                                                                                                                                                                                                                                         |
| Module Fault on Controller If Connection Fails While in Run Mode | This option determines how the controller is affected if the connection to an I/O module fails in Run mode. You can configure the project so that a connection failure causes a major fault on the controller or not. The default setting is for the option to be enabled, that is, if the connection to an I/O module fails in Run mode, a major fault occurs on the controller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## I/O Connections

IMPORTANT You can only use direct connections with the local expansion modules in a CompactLogix 5370 L2 control system.

A Logix 5000™ system uses connections to transmit I/O data, as described in this table.

## I/O Module Connections

| Connection     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct         | A direct connection is a real-time, data-transfer link between the controller and an I/O module. The controller maintains and monitors the connection. Any break in the connection, such as a module fault, causes the controller to set fault status bits in the data area that is associated with the module. Typically, analog I/O modules, diagnostic I/O modules, and specialty modules require direct connections.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Rack-optimized | For digital I/O modules, you can select rack-optimized communication. This option is used with distributed I/O modules and the Rack Optimization connection selection is made when configuring the remote adapter. For example, if your CompactLogix 5370 L2 control system includes distributed digital I/O modules over an EtherNet/IP and you want to use a rack-optimized connection with those digital I/O modules, you must configure the EtherNet/IP adapter of the distributed digital I/O modules to use a connection type of Rack Optimization. A rack-optimized connection consolidates connection usage between the controller and the digital I/O modules in a remote chassis or on one DIN rail. Rather than having individual, direct connections for each I/O module, there’s one connection for the entire rack (or DIN rail). |

## Common Configuration Parameters

While the configuration options vary from module to module, there are some common options you typically configure when using Compact I/O modules in a CompactLogix 5370 L2 control system, as described in this table.

## Configure Distributed I/O Modules on an EtherNet/IP Network

Your CompactLogix 5370 L2 control system can use distributed I/O modules on an EtherNet/IP network.

## IMPORTANT

When adding distributed I/O modules, remember to count the remote Ethernet adapter to remain within the maximum number of EtherNet/IP network nodes limitation for your controller.

The distributed I/O modules that are connected to the controller via the remote Ethernet adapter aren't counted toward the maximum Ethernet node limit for the controller.

For example, a 1769-L27ERM-QBFC1B controller supports up to 16 Ethernet nodes. You can add up to 16 remote Ethernet adapters to the I/ O Configuration section because each remote adapter counts against the node count. However, you can add as many remote I/O modules to the chassis of the adapter as necessary. Remote I/O modules do not count against the node count.

For more information on node limitations, see Chapter 6, page 102 .

Complete these steps to configure distributed I/O modules on an EtherNet/IP network.

1. Right-click Ethernet and select New Module.
2. Select the desired Ethernet adapter and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. Configure the new Ethernet adapter as necessary and select OK.
4. Right-click the new adapter and select New Module.
5. Select the desired I/O module and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

<!-- image -->

6. Configure the new I/O module as necessary and select OK.
7. Repeat these steps to add all desired distributed I/O modules.

<!-- image -->

This graphic is an example of a 1769-L27ERM-QBFC1B control system that uses distributed I/O modules over an EtherNet/IP network.

<!-- image -->

## Configure Distributed I/O Modules on a DeviceNet Network

Your CompactLogix 5370 L2 control system can use distributed I/O modules on a DeviceNet network.

Complete these steps to configure distributed I/O modules on a DeviceNet network.

1. If you haven't done so, install a 1769-SDN Compact I/O DeviceNet scanner into the local bank of your CompactLogix 5370 L2 control system.
2. Right-click 1769 Bus and select New Module.
3. Select the 1769-SDN scanner and select Create.

<!-- image -->

<!-- image -->

4. Select a Major Revision and select OK.

<!-- image -->

The New Module dialog box appears.

5. Configure the new 1769-SDN scanner as necessary and select OK.
6. Use RSNetWorx for DeviceNet software to define the scan list in the 1769-SDN scanner to communicate data between the devices and the controller through the scanner.

<!-- image -->

The following graphic is an example of a 1769-L27ERM-QBFC1B control system that uses distributed I/O modules on a DeviceNet network.

<!-- image -->

## Monitor I/O Modules

With CompactLogix 5370 L2 controllers, you can use the following options to monitor I/O modules:

- QuickView™ pane below the Controller Organizer
- Connection tab in the Module Properties dialog box
- Programming logic to monitor fault data so you can act.

When a fault occurs on an I/O module, a yellow triangle on the module listing in the Controller Organizer alerts you to the fault, as shown in this graphic.

<!-- image -->

This graphic shows the Quick View pane, which indicates the type of fault.

<!-- image -->

To see the fault description on the Connection tab in Module Properties dialog box, complete these steps.

1. In the I/O Configuration, right-click the faulted I/O module and select Properties.

<!-- image -->

2. Select the Connection tab and use the fault description, in the Module Fault section, to diagnose the issue.
3. Select OK to close the dialog box and remedy the issue.

<!-- image -->

## End Cap Detection and Module Faults

End cap detection is performed through the last module on a 1769 Bus. If that module experiences a fault such that it can't communicate on the 1769 Bus, the following events occur:

- End cap detection fails
- Controller faults

## Select I/O Modules

<!-- image -->

## Use I/O Modules with CompactLogix 5370 L3 Controllers

This chapter details the I/O module options that CompactLogix™ 5370 L3 control systems offer.

## Local Expansion Modules

CompactLogix 5370 L3 control systems support the use of Compact I/O™ modules as local expansion modules along a CompactBus backplane.

Consider the following when using local expansion modules:

- The controllers support this many local Compact I/O modules across up to three I/O banks, that is, the local bank and two more banks.
- When possible, use specialty Compact I/O modules to meet unique application requirements.
- Consider using a 1492 wiring system for each I/O module as an alternative to the terminal block that comes with the module.
- Use 1492 PanelConnect™ modules and cables if you're connecting input modules to sensors.

| Cat. No.                                                          | Maximum Local Expansion Modules Supported   |
|-------------------------------------------------------------------|---------------------------------------------|
| 1769- L30ER, 1769-L30ERK 1769-L30ERM, 1769-L30ERMK 1769-L30ER-NSE | 8                                           |
| 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK                 | 16                                          |
| 1769-L33ERMO                                                      | —                                           |
| 1769-L36ERM                                                       | 30                                          |
| 1769-L36ERMO                                                      | —                                           |
| 1769-L37ERM, 1769-L37ERMK                                         | 31                                          |
| 1769-L37ERMO(1)                                                   | —                                           |
| 1769-L38ERM, 1769-L38ERMK                                         | 31                                          |
| 1769-L38ERMO(1)                                                   | —                                           |

## Install Local Expansion Modules

Complete these steps to install local expansion modules in your CompactLogix 5370 L3 control system:

1. Attach the 1769 Compact communication or I/O modules as described in these publications:
- Compact I/O Modules Installation Instructions, publication 1769-IN088
- Compact I/O DeviceNet® Scanner Module Installation Instructions, publication 1769-IN060
2. If your system uses only a local bank, complete these steps.
- a. Use the tongue-and-groove slots to attach a 1769-ECR Compact I/O end cap terminator to the last module in the system.
- b. Move the lever of the end cap bus terminator fully to the left until it clicks to lock the end cap bus terminator.
3. If your system uses more banks, follow these steps.
- a. Install a 1769-CRx Compact I/O communication bus expansion cable at the right end of the local bank .
- b. Connect the 1769-CRx cable to the additional bank as necessary. How you connect to the first extra bank—on the right or left side of the bank, determines the expansion cable that is installed at the end of the local bank. See page 190 for an example of how to connect a local bank to extra banks.
- c. Complete the installation of the remaining banks in your system.

## IMPORTANT

Make sure that you install an end cap at the end of the last bank in your system.

This figure shows example systems with local expansion modules included.

Figure 6 - Example CompactLogix 5370 L3 Control Systems

<!-- image -->

## Wire Local Expansion Modules

Wire each Compact I/O module that is used as a local expansion module according to the technical documentation for that module.

## Distributed I/O Modules over an EtherNet/IP Network

You can include distributed I/O modules over an EtherNet/IP™ network in your CompactLogix 5370 control system. Consider the following when using distributed I/O modules over an EtherNet/IP network:

- Each remote EtherNet/IP adapter included in the system must be counted toward the maximum number of EtherNet/IP nodes for the controller.

For more information on the maximum number of EtherNet/IP nodes, see page 102 .

- The configurable RPI settings vary depending on which distributed I/O modules are used in the system.
- For information to add distributed I/O modules to your CompactLogix 5370 control system, see page 206 .

This graphic shows an example 1769-L33ERM control system that uses local expansion modules and distributed I/O modules over an EtherNet/IP network.

<!-- image -->

## Distributed I/O Modules over a DeviceNet Network

You can include distributed I/O modules over a DeviceNet network in your CompactLogix 5370 L3 control system. Consider the following when using distributed I/O modules over a DeviceNet network:

You must use this software to include distributed I/O modules over a DeviceNet network in your CompactLogix 5370 L3 control system:

- Logix Designer application or the Studio 5000® environment - for more information, see page 203 .
- RSNetWorx™ for DeviceNet software - for more information, see page 111 .

This graphic shows an example 1769-L33ERM control system that uses local expansion modules and distributed I/O modules over a DeviceNet network.

<!-- image -->

## Validate I/O Layout

After you've selected your I/O modules, you must validate the system that you want to design. Consider the points detailed in this section when validating I/O layout placement.

## Estimate Requested Packet Interval

The requested packet interval (RPI) defines the frequency at which the controller sends data to and receives data from I/O modules. You set an RPI rate for each I/O module in your system.

The CompactLogix 5370 L3 controllers attempt to scan an I/O module at the configured RPI rate. For individual I/O modules, a Module RPI Overlap minor fault (further described on page 194) occurs if there is at least one I/O module that can't be serviced within its RPI time.

The configuration parameters for a system determine the impact on actual RPI rates. These configuration factors can affect the effective scan frequency for any individual module:

- Rates at which RPI rates are set for other Compact I/O modules
- Number of other Compact I/O modules in the system
- Types of other Compact I/O modules in the system
- Application user task priorities

## Requested Packet Interval Rate Guidelines

| Type of Module                          | Guidelines(1)                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All digital                             | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…30 modules can be scanned in 2 ms.                                                                                                                                                                                                                                                          |
| Mix of digital and analog or all analog | The following guidelines apply: • 1…2 modules can be scanned in 0.5 ms. • 3…4 modules can be scanned in 1 ms. • 5…13 modules can be scanned in 2 ms. • 14…30 modules can be scanned in 3 ms.                                                                                                                                                                                                                  |
| Specialty                               | The following conditions apply: • For every 1769-SDN module in the system, increase the RPI of every other module by 2 ms. • For every 1769-HSC module in the system, increase the RPI of every other module by 1 ms. • For every 1769-ASCII module in the system, increase the RPI of every other module by 1 ms. • For every 1769-SM2 module in the system, increase the RPI of every other module by 2 ms. |

You can set the RPI rates of individual Compact I/O modules higher than the rates listed. The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Module Fault Related to RPI Estimates

When following the RPI rate guidelines, most CompactLogix 5370 L3 control systems operate as expected. Some systems that follow the guidelines can experience a Module RPI Overlap minor fault as described in this table.

## Fault Related to RPI

|                    |                                                                                                                                                           | Name Fault Information Condition In Which Fault Occurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module RPI Overlap | (Type 03) I/O fault (Code 94) Module RPI overlap detected Module Slot = x , where x is the slot number of the I/O module in the I/O Configuration section | This fault is logged when the current RPI update of an I/O module overlaps with its previous RPI update. The Minor Faults tab in the Controller Properties dialog box indicates in which module the RPI overlap occurs. If multiple I/O modules experience the fault, the application indicates that the fault occurred on the first such I/O module. Typically, it’s an I/O module with large Input/Output array sizes. Example modules that use large Input/Output array sizes include the 1769-SDN and 1769-HSC modules. In these cases, we recommend that you adjust the RPI of the module to eliminate the fault. Once the fault is cleared from the first I/O module, the application indicates the next module that experiences the fault. This pattern continues until the fault is cleared from all affected I/O modules. To avoid this fault, set the RPI rate of the I/O modules to higher numerical values. We recommend that you use an RPI value that is not a common multiple of other module RPI values, such as 2.5 ms, 5.5 ms, or 7 ms. • We recommend that you do not run CompactLogix 5370 L3 control systems with Module RPI Overlap faults. • A system that experiences many Module RPI Overlap faults can’t operate optimally because I/O data isn’t sampled at the expected rate that the RPI settings determine. • When the project is downloaded or the RPI value of an I/O module is adjusted, it’s expected to have a minor fault. Faults under these conditions are transitionary. Clear the fault and wait for the fault to reappear before adjusting the RPI value or the task priorities. |

## Calculate System Power Consumption

The 1769 Compact I/O power supplies provide power to CompactLogix local and more banks. The provided power is measured in current capacity.

Consider these points when designing your CompactLogix 5370 L3 control system banks:

- 1769 Compact I/O power supplies have two maximum current capacity requirements that affect how you design and configure one bank.

The following are the maximum current capacity requirements:

- Maximum current capacity for one bank
- Maximum current capacity for each side of the power supply

Current Capacity for Single Bank

<!-- image -->

- The maximum current capacity requirements vary by the power supply that is used in the bank.

|          | Power Supply Cat. No. Max Current Capacity for Single Bank Max Current Capacity for Each Side of Bank(1)   |
|----------|------------------------------------------------------------------------------------------------------------|
| 1769-PA2 | 2 A at 5V DC and 0.8 A at 24V DC 1 A at 5V DC and 0.4 A at 24V DC                                          |
| 1769-PB2 | 2 A at 5V DC and 0.8 A at 24V DC 1 A at 5V DC and 0.4 A at 24V DC                                          |
| 1769-PA4 | 4 A at 5V DC and 2 A at 24V DC 2 A at 5V DC and 1 A at 24V DC                                              |
| 1769-PB4 | 4 A at 5V DC and 2 A at 24V DC 2 A at 5V DC and 1 A at 24V DC                                              |

Calculate Power Consumption in Single Bank

## IMPORTANT

One bank requires the CompactLogix 5370 L3 controllers to reside in the leftmost slot. At minimum, you must calculate the power consumption of the controller on the left side of the power supply. If more modules are installed on the left side of the power supply, you must calculate the power consumption for those modules as well. If more modules are installed to the right of the power supply, you must calculate the power consumption for that side separately.

Use this table to calculate power consumption in one bank.

## Module Power Consumption Calculation for a Local Bank

| Side of Power Supply                                                                                    | Device Cat. No.                                                                                                                                                                    | Number of Modules(1)                                                                                    | Module Current Requirements                                                                             | Module Current Requirements                                                                             | Calculated Current = (Number of Modules) x (Module Current Requirements)   | Calculated Current = (Number of Modules) x (Module Current Requirements)   |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                                                                                                         |                                                                                                                                                                                    |                                                                                                         |                                                                                                         |                                                                                                         |                                                                            | at 5V DC (in mA) at 24V DC (in mA) at 5V DC (in mA) at 24V DC (in mA)      |
| Left - Required                                                                                         | 1769-L30ER, 1769-L30ERK 1769-L30ERM, 1769-L30ERMK 1769-L30ER-NSE 1769-L33ER, 1769-L33ERK 1769-L33ERM, 1769-L33ERMK 1769-L36ERM 1769-L37ERM, 1769-L37ERMK 1769-L38ERM, 1769-L38ERMK | 1                                                                                                       | 500                                                                                                     | 225                                                                                                     | 500                                                                        | 225                                                                        |
| Left - Optional                                                                                         | I/O Module-specific                                                                                                                                                                |                                                                                                         | Up to 3 Module-specific Module-specific                                                                 |                                                                                                         |                                                                            |                                                                            |
| Left - Optional                                                                                         | Total Current Required (2) :                                                                                                                                                       |                                                                                                         |                                                                                                         |                                                                                                         |                                                                            |                                                                            |
| Right                                                                                                   | I/O Module-specific IMPORTANT: Insert a separate row in this calculation for each I/O module.                                                                                      |                                                                                                         | Up to 8 Module-specific Module-specific                                                                 |                                                                                                         |                                                                            |                                                                            |
| Right                                                                                                   | Total Current Required (2) :                                                                                                                                                       |                                                                                                         |                                                                                                         |                                                                                                         |                                                                            |                                                                            |
| Total Current Required for Single Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Single Bank if Modules Are Installed on Both Sides of the Power Supply (3) :                                                                            | Total Current Required for Single Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Single Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Single Bank if Modules Are Installed on Both Sides of the Power Supply (3) : |                                                                            |                                                                            |

## Calculate Power Consumption in an Additional Bank

## IMPORTANT

In extra banks, you can install I/O modules to the left side, right side, or both sides of the power supply.

Use this table to calculate power consumption in an extra bank.

## Module Power Consumption Calculation for an Additional Bank

| Side of Power Supply                                                                             | Device Cat. No.                                                                                  | Number of Modules(1)                                                                             | Module Current Requirements                                                                      | Calculated Current = (Number of Modules) x (Module Current Requirements)                         | Calculated Current = (Number of Modules) x (Module Current Requirements)   |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                                                                                                  |                                                                                                  |                                                                                                  |                                                                                                  |                                                                                                  | at 5V DC (in mA) at 24V DC (in mA) at 5V DC (in mA) at 24V DC (in mA)      |
| Left - Optional in an extra bank                                                                 | I/O Modules IMPORTANT: Insert a separate row in this calculation for each I/O module.            |                                                                                                  | Up to 8 Module-specific Module-specific                                                          |                                                                                                  |                                                                            |
|                                                                                                  | Total Current Required (2) :                                                                     |                                                                                                  |                                                                                                  |                                                                                                  |                                                                            |
| Right - Optional in one bank                                                                     | I/O Modules IMPORTANT: Insert a separate row for each I/O module.                                |                                                                                                  | Up to 8 Module-specific Module-specific                                                          |                                                                                                  |                                                                            |
|                                                                                                  | Total Current Required (2) :                                                                     |                                                                                                  |                                                                                                  |                                                                                                  |                                                                            |
| Total Current Required for Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Bank if Modules Are Installed on Both Sides of the Power Supply (3) : | Total Current Required for Bank if Modules Are Installed on Both Sides of the Power Supply (3) : |                                                                            |

## Physical Placement of I/O Modules

Depending on the controller catalog number, CompactLogix 5370 L3 controllers support from 8 to 30 I/O modules. For more information on local expansion module catalog numbers, see page 189 .

Consider these factors when determining the physical placement of the I/O modules:

- You can install I/O modules in local and extra banks.
- You can install I/O modules to the left and right of the power supply.
- When a system requires multiple banks, you can install the additional banks horizontally or vertically, as shown in this graphic.
- Each I/O module also has a power supply distance rating and maximum current draw. Considered jointly, distance ratings and current draw determine where I/O modules can be placed in a bank and what configuration of modules can be installed in the bank.

<!-- image -->

For more information on power supply distance ratings, see page 69. For more information on system power consumption, see page 194 .

## Local Bank

To validate the local bank design, confirm that the design meets these requirements:

- The controller is the leftmost device in the local bank.
- No more than three modules are installed between the controller and the left side of the power supply.
- No more than eight modules are installed to the right of the power supply.
- The power consumption of the modules on each side of the power supply does not exceed the capacity of the power supply for that side.
- The total power consumption by all modules in the bank does not exceed the capacity of the power supply for the entire bank.
- Modules are installed such that all power supply distance rating and system power consumption requirements are met.

For example, the 1769-SDN scanner has a power supply distance rating of four. If the design includes the installation of a 1769-SDN scanner with greater than three modules between it and the power supply, the design is invalid.

## IMPORTANT

Make sure that you take power supply distance ratings into consideration when you design a system. If you install a module that violates its power supply distance rating specification, the system can operate normally for a time, but experience operational issues, such as I/O faults.

## This example graphic shows a local bank.

1769 Compact I/O Power Supply

<!-- image -->

## Additional Banks

If your application calls for twelve or more I/O modules, at minimum, you must install the modules in extra banks. The conditions of each application determine the number of extra banks.

Once the local bank design is validated, you must validate the design for any additional banks. To validate extra bank designs, confirm that the design meets these requirements:

- Compact I/O communication bus expansion cables are used properly.

<!-- image -->

Compact I/O expansion cables have the same dimensions as the end caps regardless of whether they're installed at the right or left side of the communication bus.

- No more than eight modules are installed on either side of the power supply.
- The power consumption of the modules on each side of the power supply does not exceed the capacity of the power supply for that side.
- Modules are installed such that all power supply distance rating requirements are met.
- End caps are installed properly, as shown in the following graphic.

<!-- image -->

## Power Supply Distance Rating

CompactLogix 5370 L3 control systems do not have embedded I/O modules. You begin counting local expansion slots with the first Compact I/O module installed next to the power supply when determining where to install a

Compact I/O module and meet its power supply distance rating.

In CompactLogix 5370 L3 control systems, you can install Compact I/O modules to the left or right side of the power supply. You can also use local and extra banks in CompactLogix 5370 L3 control systems, with each allowing the inclusion of Compact I/O modules.

## Local Bank

In the local bank, the controller must be the leftmost device in the system and you can only install up to three modules between the controller and the power supply. Therefore, any Compact I/O modules that are installed to the left of the power supply in the local bank are in a module slot that meets the power supply distance rating requirements for the module.

## Additional Banks

CompactLogix 5370 L3 control systems also support the use of extra banks for the local expansion modules of the system. Every additional bank requires a 1769 Compact I/O power supply. The bank can be designed with local expansion modules on either side of the power supply.

Most Compact I/O modules have power supply distance rating values that allow you to install them in any slot on either side of the power supply in extra banks. Some Compact I/O modules have power supply distance ratings that affect where you can install them in the CompactLogix 5370 L3 control system.

For example, the 1769-ASCII Compact ASCII and 1769-HSC Compact high-speed counter modules each have a power supply distance rating of four. These modules can be installed in local expansion module slots one through three.

In this case, you must install the 1769-ASCII module and 1769-HSC high-speed counter module with no more three Compact I/O modules between the module and the power. This requirement is true regardless of whether the modules are installed to the left or right of the power supply.

This graphic shows 1769-HSC high-speed counter modules that are installed in a 1769-L36ERM control system that meet the power supply distance rating of the module.

<!-- image -->

## IMPORTANT

The Module Power Consumption Calculation for an Additional Bank table on page 196 shows example systems with 1769-HSC high-speed counter modules in each control system because it has a power supply distance rating of four and can't be installed as far from the Compact I/O power supply. Most Compact I/O modules have power supply distance ratings that allow you to install them anywhere in the local expansion slots of a CompactLogix 5370 L2 control system.

For more information about the power supply distance rating for a Compact I/O module, see CompactLogix Selection Guide, publication 1769-SG001.

## Configure I/O

Complete these steps to add a Compact I/O module to your CompactLogix 5370 L3 control system and configure it.

1. Right-click the 1769 Bus and select New Module.
2. Select the desired I/O module and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. Configure the new I/O module as necessary and select OK.

<!-- image -->

## Common Configuration Parameters

While the configuration options vary from module to module, there are some common options you typically configure when using Compact I/O modules in a CompactLogix 5370 L3 control system, as described in this table.

| Configuration Option                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requested packet interval (RPI)                                  | The RPI specifies the interval at which data is transmitted or received over a connection. For 1769 Compact Local I/O modules, data is transmitted to the controller at the RPI. When scanned on the local bus or over an EtherNet/IP network, input modules are scanned at the RPI specified in the module configuration. Typically, you configure an RPI in milliseconds (ms). For I/O modules, the range is 0.5…750 ms. When scanned over a DeviceNet network, distributed input modules are scanned at the rate that the DeviceNet adapter that connects the input modules to the network supports. For example, the scan rate for distributed 1734 POINT I/O™ over DeviceNet can only occur as quickly as the 1734-ADN DeviceNet adapter can transmit the data. |
| Module definition                                                | Set of configuration parameters that affect data transmission between the controller and the I/O module. The parameters include the following: • Series - Hardware series of the module. • Revision - Major and minor firmware revision levels that are used on the module. • Electronic Keying - See LOGIX-AT001 for Electronic Keying information. • Connection - Type of connection between the controller writing the configuration and the I/O module, such as Output. • Data format - Type of data that is transferred between the controller and I/O module and what tags are generated when the configuration is complete.                                                                                                                                   |
| Module Fault on Controller If Connection Fails While in Run Mode | This option determines how the controller is affected if the connection to an I/O module fails in Run mode. You can configure the project so that a connection failure causes a major fault on the controller or not. The default setting is for the option to be enabled, that is, if the connection to an I/O module fails in Run mode, a major fault occurs on the controller.                                                                                                                                                                                                                                                                                                                                                                                    |

## I/O Connections

A Logix 5000™ system uses connections to transmit I/O data, as described in this table.

| Connection     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct         | A direct connection is a real-time, data-transfer link between the controller and an I/O module. The controller maintains and monitors the connection. Any break in the connection, such as a module fault, causes the controller to set fault status bits in the data area that is associated with the module. Typically, analog I/O modules, diagnostic I/O modules, and specialty modules require direct connections.                                                                                                                                                                                                                                                                                              |
| Rack-optimized | For digital I/O modules, you can select rack-optimized communication. This option is used with distributed I/O modules and the Rack Optimization connection selection is made when configuring the remote adapter. For example, if you want to use a rack-optimized connection with digital I/O modules in a remote 1734 POINT I/O system, you configure the 1734-AENT(R) module to use a connection type of Rack Optimization. A rack-optimized connection consolidates connection usage between the controller and the digital I/O modules in a remote chassis or on one DIN rail. Rather than having individual, direct connections for each I/O module, there’s one connection for the entire rack (or DIN rail). |

## Configure Distributed I/O Modules on an EtherNet/IP Network

Your CompactLogix 5370 L3 control system can use distributed I/O modules on an EtherNet/IP network.

## IMPORTANT

When adding distributed I/O modules, remember to count the remote Ethernet adapter to remain within the maximum number of EtherNet/IP network nodes limitation for your controller.

The remote I/O modules that are connected to the controller via the Ethernet adapter aren't counted toward the maximum Ethernet node limit for the controller.

For more information on node limitations, see Chapter 6, page 102 .

Complete these steps to configure distributed I/O modules on an EtherNet/IP network.

1. Right-click Ethernet and select New Module.
2. Select the desired Ethernet adapter and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. Configure the new Ethernet adapter as necessary and select OK.
4. Right-click the new adapter and select New Module.
5. Select the desired I/O module and select Create.

<!-- image -->

<!-- image -->

<!-- image -->

The New Module dialog box appears.

6. Configure the new I/O module as necessary and select OK.
7. To add the desired distributed I/O modules, repeat these steps.

<!-- image -->

The following graphic is an example of a 1769-L33ERM control system that uses distributed I/O modules over an EtherNet/IP network.

<!-- image -->

## Configure Distributed I/O Modules on a DeviceNet Network

Your CompactLogix 5370 L3 control system can use distributed I/O modules on a DeviceNet network.

Complete these steps to configure distributed I/O modules on a DeviceNet network.

1. If you have not done so, install a 1769-SDN Compact I/O DeviceNet scanner into the local bank of your CompactLogix 5370 L3 control system.
2. Right-click 1769 Bus and select New Module.
3. Select the 1769-SDN scanner and select Create.
4. Select a Major Revision and select OK.

<!-- image -->

<!-- image -->

<!-- image -->

The New Module dialog box appears.

5. Configure the new 1769-SDN scanner as necessary and select OK.

<!-- image -->

6. Use RSNetWorx for DeviceNet software to define the scan list in the 1769-SDN scanner to communicate data between the devices and the controller through the scanner.

The following graphic is an example of a 1769-L33ERM control system that uses distributed I/O modules on a DeviceNet network.

- 1769-L33ERM
- 1769-SDN Scanner

<!-- image -->

## Monitor I/O Modules

With CompactLogix 5370 L3 controllers, you can monitor I/O modules in the following ways:

- QuickView™ Pane below the Controller Organizer
- Connection tab in the Module Properties dialog box
- Programming logic to monitor fault data so you can act

When a fault occurs on an I/O module, a yellow triangle on the module listing in the Controller Organizer alerts you to the fault.

<!-- image -->

This graphic shows the Quick View Pane, which indicates the type of fault.

<!-- image -->

To see the fault description on the Connection tab in Module Properties dialog box, complete these steps.

1. In the I/O Configuration, right-click the faulted I/O module and select Properties.

<!-- image -->

2. To diagnose the issue, select the Connection tab and use the fault description, in the Module Fault section.
3. To close the dialog box and remedy the issue, select OK.

<!-- image -->

## End Cap Detection and Module Faults

End cap detection is performed through the last module on a 1769 Bus. If that module experiences a fault such that it can't communicate on the 1769 Bus, the following events occur:

- End cap detection fails
- Controller faults

## Notes:

## Elements of a Control Application

## Develop Applications

A control application is composed of several elements that require planning for efficient application execution. This section details the elements of a control application.

## Elements of a Control Program

Control Application

<!-- image -->

<!-- image -->

## Tasks

A Logix 5000® controller lets you use multiple tasks to schedule and prioritize the execution of your programs that are based on criteria. This multitasking allocates the processing time of the controller among the different operations in your application:

- The controller executes only one task at a time.
- One task can interrupt the execution of another task and take control.
- In any given task, multiple programs can be used. However, only one program executes at a time.
- You can display tasks in the Controller or Logical Organizer views, as necessary.

## Task in a Control Application

Control Application

<!-- image -->

<!-- image -->

A task provides scheduling and priority information for a set of one or more programs. Configure tasks as continuous, periodic, or event by using the Task Properties dialog box.

## Configuring the Task Type

<!-- image -->

## Task Types and Execution Frequency

|                   | Task Type Task Execution                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous Always |                                                                                            | The continuous task runs in the background. Any CPU time that is not allocated to other operations (such as motion, communication, and other tasks) is used to execute the programs in the continuous task: • The continuous task runs constantly. When the continuous task completes a full scan, it restarts immediately. • A project does not require a continuous task. If used, there can be only one continuous task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Periodic          | • At a set interval, such as every 100 ms • Multiple times in the scan of your other logic | A periodic task performs a function at an interval: • Whenever the time for the periodic task expires, the task interrupts any lower priority tasks, executes once, and returns control to where the previous task left off. • You can configure the time period from 0.1…2,000,000.00 ms. The default is 10 ms. It’s also controller and configuration dependent. • The performance of a periodic task depends on the type of Logix 5000 controller and on the logic in the task. • The periodic task processes I/O data for CompactLogix™, FlexLogix™, DriveLogix™, and SoftLogix™ controllers with the following considerations: – For CompactLogix, FlexLogix, and DriveLogix controllers, operates at priority 6 – For SoftLogix controllers, operates at Windows priority 16 (Idle) – Higher-priority tasks take precedence over the I/O task and can affect processing – Executes at the fastest RPI that you’ve scheduled for the system – Executes for as long as it takes to scan the configured I/O modules |
| Event             | Immediately when an event occurs                                                           | An Event task performs a function only when an event (trigger) occurs. The trigger for the Event task can be the following: • A consumed tag trigger • An EVENT instruction • An axis trigger • A motion event trigger • Module input data state change IMPORTANT: With Logix Designer application, version 21.00.00 or later, you can use this trigger with 1756 ControlLogix®, 1789 SoftLogix, and CompactLogix 5370 L1 applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

The CompactLogix controller supports up to 32 tasks, only one of which can be continuous.

A task can have up to 1000 separate Programs (as described on page 216) per task, each with its own executable routines and program-scoped tags. Once a task is triggered (activated), all programs that are assigned to the task execute in the order in which they're grouped. Multiple tasks can't share Programs and Programs appear only once in the Controller Organizer.

This table explains the types of tasks that you can configure.

## Task Priority

Each task in the controller has a priority level. The operating system uses the priority level to determine which task to execute when multiple tasks are triggered. A higher priority task interrupts any lower priority task. A periodic or event task interrupts the continuous task, which has the lowest priority.

You can configure periodic tasks to execute from the lowest priority of 15 up to the highest priority of 1. Configure the task priority by using the Task Properties dialog box.

## Configure the Task Priority

<!-- image -->

## Programs

Program

Program

## Control Application

<!-- image -->

## Programs in Application

Program

Controller Organizer

Tasks

MainTask

MainProgram

Parameters and Local Tags

MainRoutine

Secondary\_Program

Parameters and Local Tags

Secondary\_1

The controller operating system is a pre-emptive multitasking system that is in compliance with IEC 1131-3. This system provides the following:

- Programs to group data and logic
- Routines to encapsulate executable code that is written in one programming language

Each program contains the following:

- Local Tags
- Parameters
- A main executable routine
- Other routines
- An optional fault routine

## Program in a Control Application

Program

Logical Organizer

Logical Modeldevelop\_applications

MainProgram

Logic and Tags

Parameters and Local Tags

主

MainRoutine

Reserve\_Program

Secondary\_Program

## Scheduled and Unscheduled Programs

The scheduled programs in a task execute to completion from first to last. Programs that aren't attached to any task show up as unscheduled programs.

Unscheduled programs in a task are downloaded to the controller with the entire project. The controller verifies unscheduled programs but does not execute them.

You must schedule a program in a task before the controller can scan the program. To schedule an unscheduled program, use the Program/Phase Schedule tab of the Task Properties dialog box.

## Scheduling an Unscheduled Program

<!-- image -->

## Routines

## Control Application

<!-- image -->

## Routines in Application

## Controller Designer

<!-- image -->

A routine is a set of logic instructions in one programming language, such as Ladder Diagram (ladder logic). Routines provide the executable code for the project in a controller. A routine is similar to a program file or subroutine in a PLC or SLC™ processor.

Each program has a main routine. This routine is the first routine to execute when the controller triggers the associated task and calls the associated program. Use logic, such as the Jump to Subroutine (JSR) instruction, to call other routines.

You can also specify an optional program fault routine. The controller executes this routine if it encounters an instruction-execution fault in any of the routines in the associated program.

## Routines in a Control Application

## Logical Designer

<!-- image -->

## Tags

With a Logix 5000 controller, you use a tag (alphanumeric name) to address data (variables). In Logix 5000 controllers, there's no fixed, numeric format. For example, as shown in the following figure, you can use the tag name north\_tank\_mix instead of a numeric format, such as N7:0.0.

The tag name itself identifies the data. The tag lets you do the following:

- Organize your data to mirror your machinery.
- Document your application as you develop it.

This example shows data tags that are created in the scope of the Main Program of the controller.

## Tags Example

## Controller Organizer - Main Program Parameters and Local Tags

<!-- image -->

## Program Tags Window - Main Program Tags

<!-- image -->

There are several guidelines to create and configure parameters and local tags for optimal task and program execution. For more information, see the Logix 5000 Controllers and I/O Tag Data Programming Manual, publication 1756-PM004 .

## Extended Properties

The Extended Properties feature lets you define more information, such as limits, engineering units, or state identifiers, for various components within your controller project.

| Component           | Extended Properties                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Tag                 | In the Tag Editor, add extended properties to a tag.                                                                          |
|                     | User-defined data type In the Data Type Editor, add extended properties to data types.                                        |
| Add-On Instructions | In the properties that are associated with the Add-On Instruction definition, add extended properties to Add-On Instructions. |

Pass-through behavior is the ability to assign extended properties at a higher level of a structure or Add-On Instruction and have that extended property automatically available for all members. Pass-through behavior is available for descriptions, state identifiers, and engineering units and you can configure it. Configure pass-through behavior on the Project tab of the Controller Properties dialog box. If you select not to show pass-through properties, only extended properties that have been configured for a given component are displayed.

Pass-through behavior isn't available for limits. When an instance of a tag is created, if limits are associated with the data type, the instance is copied.

You must know which tags have limits that are associated with them as there's no indication in the tag browser that extended properties are defined for a tag. If, however, you try to use extended properties that haven't been defined for a tag, the editors show a visual indication and the routine does not verify.

## Access Extended Properties in Logic

You can access limits that are defined on tags by using the .@Min and .@Max syntax:

- You can't write to extended properties values in logic.
- To use extended tag properties in an Add-On Instruction, you must pass them in as input operands to the Add-On Instruction.
- Alias tags that have extended properties can't access the extended properties in logic.
- Limits can be configured for input and output parameters in Add-On Instructions. However, limits can't be defined on an InOut parameter of an Add-On Instruction.
- Limits can't be accessed inside Add-On Instruction logic. Limits are for use only by HMI applications.

If an array tag is using indirect addressing to access limits in logic, these conditions apply:

- If the array tag has limits that are configured, the extended properties are applied to any array element that does not explicitly have that particular extended property configured. For example, if the array tag MyArray has Max configured to 100, any element of the array that does not have Max configured inherits the value of 100 when being used in logic. However, it isn't visible that the value inherited from MyArray is configured in the tag properties.
- At least one array element must have a limit that is configured for indirectly referenced array logic to verify. For example, if MyArray[x].@Max is being used in logic, at least one array element of MyArray[] must have Max extended property that is configured if MyArray hasn't configured Max.
- Under the following circumstances, a data type default value is used:
- Array is accessed programmatically with indirect reference.
- Array tag does not have the extended property configured.
- A member of an array does not have the extended property configured.

For example, for an array of SINT type, when max limit is called in logic for a member, use the value of 127. If an array element is directly accessed, the element has to have the extended property defined. If not, verification fails.

## Programming Languages

The CompactLogix controller supports these programming languages, online, and offline.

## CompactLogix Controller Programming Languages

| Language                        | Is best-used in programs with                                                                                 |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| Relay ladder                    | Continuous or parallel execution of multiple operations (not sequenced)                                       |
| Relay ladder                    | Boolean or bit-based operations                                                                               |
| Relay ladder                    | Complex logical operations                                                                                    |
| Relay ladder                    | Message and communication processing                                                                          |
| Relay ladder                    | Machine interlocking                                                                                          |
| Relay ladder                    | Operations that service or maintenance personnel can have to interpret to troubleshoot the machine or process |
| Function block diagram          | Continuous process and drive control                                                                          |
| Function block diagram          | Loop control                                                                                                  |
| Function block diagram          | Calculations in circuit flow                                                                                  |
| Sequential function chart (SFC) | High-level management of multiple operations                                                                  |
| Sequential function chart (SFC) | Repetitive sequence of operations                                                                             |
| Sequential function chart (SFC) | Batch process                                                                                                 |
| Sequential function chart (SFC) | Motion control using structured text                                                                          |
| Sequential function chart (SFC) | State machine operations                                                                                      |
| Structured text                 | Complex mathematical operations                                                                               |
| Structured text                 | Specialized array or table loop processing                                                                    |
| Structured text                 | ASCII string handling or protocol processing                                                                  |

For information about programming in these languages, see the Logix 5000 Controllers Common Procedures Programming Manual, publication 1756-PM001 .

## Add-On Instructions

## Add-On Instruction Capabilities

| Capability                 | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Save Time                  | With Add-On Instructions, you can combine your most commonly used logic into sets of reusable instructions. You save time when you create instructions for your projects and share them with others. Add-On Instructions increase project consistency because commonly used algorithms all work in the same manner, regardless of who implements the project. |
| Use Standard Editors       | You create Add-On Instructions by using one of three editors: • Relay Ladder • Function Block Diagram • Structured Text Once you have created instructions, you can use them in any editor.                                                                                                                                                                   |
| Export Add-On Instructions | You can export Add-On Instructions to other projects and copy and paste them from one project to another. Give each instruction  a unique name so that you don’t accidentally overwrite another instruction of the same name.                                                                                                                                 |
| Use Context Views          | Context views let you visualize the logic of an instruction for an instant, which simplifies online troubleshooting of your Add-On Instructions. Each instruction contains a revision, a change history, and an auto-generated help page.                                                                                                                     |
| Create Custom Help         | When you create an instruction, you enter information for the description fields in dialogs, information that becomes what is known as Custom Help. Custom Help makes it easier for you to get the help you need when implementing the instructions.                                                                                                          |
| Apply Source Protection    | As the creator of Add-On Instructions, you can limit users of your instructions to read-only access. You can also bar access to the internal logic or local parameters that are used by the instructions. This source protection lets you stop unwanted changes to your instructions and protects your intellectual property.                                 |

Once defined in a project, Add-On Instructions behave similarly to the built-in instructions in Logix 5000 controllers. They appear on the instruction toolbar for easy access, as do internal instructions.

## Add-On Instructions

## Controller Organizer

<!-- image -->

You can design and configure sets of commonly used instructions to increase project consistency. Similar to the built-in instructions contained in Logix 5000 controllers, these instructions you create are called Add-On Instructions. Add-On Instructions reuse common control algorithms. With them, you can do the following:

- Ease maintenance by animating logic for one instance.
- Protect intellectual property with Source Protection.
- Reduce documentation development time.

You can use Add-On Instructions across multiple projects. You can define your instructions, obtain them from somebody else, or copy them from another project.

This table explains some of the capabilities and advantages of use Add-On Instructions.

## Instruction

<!-- image -->

## Access the Module Object

The MODULE object provides status information about a module. To select a particular module object, set the Object Name operand of the GSV/SSV instruction to the module name. The specified module must be present in the I/O Configuration section of the controller organizer and must have a device name.

## Create the Add-On Instruction

With Logix Designer application, version 24.00.00 and later, you can access a MODULE object directly from an Add-On Instruction. Previously, you could access the MODULE object data but not from within an Add-On Instruction.

You must create a Module Reference parameter when you define the Add-On Instruction to access the MODULE object data. A Module Reference parameter is an InOut parameter of the MODULE data type that points to the MODULE Object of a hardware module. You can use module reference parameters in both Add-On Instruction logic and program logic.

<!-- image -->

For more information on the Module Reference parameter, see the Logix 5000 Controllers AddOn Instructions Programming Manual, publication 1756-PM010, and the Logix Designer application online help.

The MODULE object uses the following attributes to provide status information:

- EntryStatus
- FaultCode
- FaultInfo
- FWSupervisorStatus
- ForceStatus
- Instance
- LEDStatus
- Mode
- Path

The Path attribute is available with Logix Designer application, version 24.00.00 and later. This attribute provides a communication path to the module.

For more information on the attributes available in the MODULE object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

Monitoring Controller Status The CompactLogix controller uses Get System Value (GSV) and Set System Value (SSV)
ii() instructions to get and set (change) controller data. The controller stores system data in objects. There's no status file, as in the PLC-5® processor.

The GSV instruction retrieves the specified information and places it in the destination. The SSV instruction sets the specified attribute with data from the source. The instructions are available from the Input/Output tab of the Instruction toolbar.

## GSV and SSV Instructions for Monitoring

<!-- image -->

When you add a GSV/SSV instruction to the program, the object classes, object names, and attribute names for each instruction are displayed. For the GSV instruction, you can get values for the available attributes. For the SSV instruction, only those attributes you're allowed to set are displayed.

Some object types appear repeatedly, so you have to specify the object name. For example, there can be several tasks in your application. Each task has its own Task object that you access by the task name.

There are several objects and attributes that you can use the GSV and SSV instructions to monitor and set the system. For more information about GSV instructions, SSV instructions, objects, and attributes see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

If communication with a device in the I/O configuration of the controller does not occur in an application-specific period, the communication times out and the controller produces warnings.

The minimum timeout period that, once expired without communication, causes a timeout is 100 ms. The timeout period can be greater, depending on the RPI of the application. For example, if your application uses the default RPI = 20 ms, the timeout period is 160 ms.

When a timeout does occur, the controller produces these warnings:

- An I/O fault status code is indicated on the status display of the CompactLogix 5370 controller.
- The I/O status indicator on the front of the CompactLogix 5370 controller flashes green.
- A shows over the I/O configuration folder and over the devices that have timed out. !
- A module fault code is produced, which you can access via the following:
- The Module Properties dialog box
- A GSV instruction

For more information about I/O faults, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

## Monitoring I/O Connections

## I/O Communication Timeout

This example can be used with the CompactLogix 5370 controllers:

- The GSV instruction gets the status of the I/O status indicator (via the LEDStatus attribute of the Module object) and stores it in the IO\_LED tag.
- IO\_LED is a DINT tag that stores the status of the I/O status indicator or status display on the front of the controller.
- If IO\_LED equals 2, then at least one I/O connection has been lost and the Fault\_Alert is set.

## GSV Used to Identify I/O Timeout

<!-- image -->

For more information about attributes available with the Module object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

## I/O Communication Timeout to a Specific I/O Module

If communication times out with a device (module) in the I/O configuration of the controller, the controller produces a fault code and fault information for the module. You can use GSV instructions to get fault code and information via the FaultCode and FaultInfo attributes of the Module object.

For more information about attributes available with the Module object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

## I/O Module Properties

<!-- image -->

## Parent Communication Module Properties

<!-- image -->

For more information about programming the Controller Fault Handler, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

## Interrupt the Execution of Logic and Execute the Fault Handler

Depending on your application, you can want an I/O connection error to cause the Controller Fault Handler to execute. To do so, set the module property that causes a major fault to result from an I/O connection error. The major fault causes the execution of the Controller Fault Handler.

First, develop a routine in the Controller Fault Handler that can respond to I/O connection faults. In the Module Properties dialog box of the I/O module or parent communication module, select Major Fault On Controller If Connection Fails While in Run Mode.

## I/O Connection Fault Causes Major Fault

## System Overhead Time Slice

The controller communicates with other devices at a specified rate (scheduled) or when there's processing time available to service the communication.

The system overhead time slice specifies the percentage of time a controller devotes to service communication. If you have a continuous task, the System Overhead Time Slice entered in the Advanced tab of the Controller Properties dialog box specifies the continuous task/service communication ratio. However, if there's no continuous task, the overhead time slice has no effect.

This table shows the ratio between the continuous task and service communication at various system overhead time slices.

## Ratio between Continuous Task and Service Communication

| At this time slice The continuous task runs Service communication occurs for up to   |
|--------------------------------------------------------------------------------------|
| 10% 9 ms 1 ms                                                                        |
| 20% 4 ms 1 ms                                                                        |
| 25% 3 ms 1 ms                                                                        |
| 33% 2 ms 1 ms                                                                        |
| 50% 1 ms 1 ms                                                                        |
| 66% 1 ms 2 ms                                                                        |
| 75% 1 ms 3 ms                                                                        |
| 80% 1 ms 4 ms                                                                        |
| 90% 1 ms 9 ms                                                                        |

If the system overhead time slice is less than or equal to 50%, the duration stays fixed at 1 ms. The same applies for 66% and higher, except there are multiple 1 ms intervals. For example, at 66% there are two 1 ms intervals of consecutive time and at 90% there are nine 1 ms intervals of consecutive time.

## Configure the System Overhead Time Slice

To configure the system overhead time slice, perform this procedure.

1. In the Controller Organizer, right-click the controller and select Properties. The Controller Properties dialog box appears.
2. Select the Advanced tab.
3. Enter a numeric value in the System Overhead Time Slice box.
4. Use Run Continuous Task (default) or Reserve for System Tasks.
- Select Run Continue Task when there's no communication or background tasks to process; the controller immediately returns to the continuous task.
- Select Reserve for System Task to allocate the entire 1 ms of the system overhead time slice whether the controller has communication or background tasks to perform before returning back to the continuous task. This lets you simulate a communication load on the controller during design and programming before HMIs, controller to controller messaging, and so forth, are configured.
5. Select OK.

<!-- image -->

## Sample Controller Projects

The application includes sample projects that you can copy and modify to fit your application. To access the sample projects, complete these steps.

1. From the File menu, select Open.
2. Browse to the sample projects list and select a sample project.
3. Select Open.

<!-- image -->

<!-- image -->

## Notes:

<!-- image -->

## Develop Integrated Motion Over an EtherNet/IP Network Application

Some of the CompactLogix™ 5370 controllers support Integrated Motion over an EtherNet/IP™ network. This motion solution is on standard, unmodified EtherNet/IP networks with simple design or configuration as compared to traditional motion applications.

## IMPORTANT

The following CompactLogix 5370 controllers support Integrated Motion over an EtherNet/IP network:

- 1769-L18ERM-BB1B controller
- 1769-L18ERM-BB1BK controller
- 1769-L27ERM-QBFC1B controller
- 1769-L30ERM controller
- 1769-L30ERMK controller
- 1769-L33ERM controller
- 1769-L33ERMK controller
- 1769-L33ERMO controller
- 1769-L36ERM controller
- 1769-L36ERMO controller
- 1769-L37ERM controller
- 1769-L37ERMK controller
- 1769-L37ERMO controller(1)
- 1769-L38ERM controller
- 1769-L38ERMK controller
- 1769-L38ERMO controller(1)

(1) Available at software version 31 and firmware revision 31.

Integrated Motion on EtherNet/IP applications use the following:

- Standard EtherNet/IP network
- High-performance drives, including the following:
- Kinetix® 350 drives
- Kinetix 5500 drives
- Kinetix 5700 drives
- Kinetix 6500 drives
- PowerFlex® 755 drives
- Standard infrastructure components
- Programming software

For a complete description of how to use a CompactLogix 5370 controller in an application that uses Integrated Motion over an EtherNet/IP network, see the Integrated Motion on the EtherNet/IP Network: Configuration and Startup User Manual, publication MOTION-UM003 .

## Motion Axes Support

The 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L27ERM-QBFC1B, 1769-L30ERM, 1769L30ERMK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMO, 1769-L36ERM, 1769-L36ERMO, 1769L37ERM, 1769-L37ERMK, 1769-L37ERMO (1) , 1769-L38ERM, 1769-L38ERMK, and 1769-L38ERMO (1) controllers support the axes that are detailed in this section.

## AXIS\_VIRTUAL Axis

The AXIS\_VIRTUAL axis is an internal axis representation that is not associated with any physical drives. That is, you can configure the axis but it does not cause any physical motion in your system.

## AXIS\_CIP\_DRIVE Axis

The AXIS\_CIP\_DRIVE axis is a motion axis that is used with physical drives to cause physical motion in your system as determined by your application.

## Configuration Types

When adding an axis to your project, you must associate the axis to a drive. Among other configuration parameters, you must select a configuration type. The axis configuration type is also considered the drive configuration type.

For example, an AXIS\_CIP\_DRIVE axis can use a Position Loop configuration and be associated with a Kinetix 350 drive. The axis is considered a Position Loop-configured axis and the associated drive is considered a Position Loop-configured drive.

The following drives support these configuration types:

- Kinetix 350, Kinetix 5500, Kinetix 5700, and Kinetix 6500 drives
- Position loop
- Velocity loop
- Torque loop
- PowerFlex 755 drive
- Position loop
- Velocity loop
- Torque loop
- Frequency control

## Maximum Number of Position Loop-configured Drives

The CompactLogix 5370 controllers support a maximum number of EtherNet/IP nodes in a project. Any device added to the local Ethernet node in the I/O configuration is counted toward the node limitation of the controller. For more information, see Chapter 6, page 102 .

Drives are counted among the number of nodes in the I/O Configuration section of the Studio 5000® environment. If you use the maximum number of drives that a 1769-L18ERM-BB1B, 1769L18ERM-BB1BK, 1769-L27ERM-QBFC1B, 1769-L30ERM, 1769-L30ERMK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMO, 1769-L36ERM, 1769-L36ERMO, 1769-L37ERM, 1769-L37ERMK, 1769L37ERMO(1), 1769-L38ERM, 1769-L38ERMK, or 1769-L38ERMO(1) controller supports in one system, you can't add other EtherNet/IP devices to that project.

## Position Loop-configured Drive Limits

Among the maximum number drives supported by the controllers, there's a maximum number of Position Loop-configured drives that are supported in the project for the controller.

For example, the 1769-L30ERM controller supports a maximum of four Position Loopconfigured drives.

This table lists motion-related specification information for the controllers that support Integrated Motion over an EtherNet/IP network.

## CompactLogix 5370 Controllers Supporting Integrated Motion on the EtherNet/IP Network

|                                                                   | Controller Type Drive Types Supported                            | Number of Drives Supported, Max   | Number of Position Loop configured Drives Supported, Max     |
|-------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------|-----|
| 1769-L18ERM-BB1B 1769-L18ERM-BB1BK                                | Kinetix 350 Kinetix 5500 Kinetix 5700 Kinetix 6500 PowerFlex 755 |                                   | 8 2 |
| 1769-L27ERM-QBFC1B 1769-L30ERM 1769-L30ERMK                       | Kinetix 350 Kinetix 5500 Kinetix 5700 Kinetix 6500 PowerFlex 755 | 16 4                              |     |
| 1769-L33ERM 1769-L33ERMK 1769-L33ERMO                             | Kinetix 350 Kinetix 5500 Kinetix 5700 Kinetix 6500 PowerFlex 755 | 32 8                              |     |
| 1769-L36ERM 1769-L36ERMO 1769-L37ERM 1769-L37ERMK 1769-L37ERMO(1) | Kinetix 350 Kinetix 5500 Kinetix 5700 Kinetix 6500 PowerFlex 755 | 48                                | 16  |
| 1769-L38ERM 1769-L38ERMK 1769-L38ERMO(1)                          | Kinetix 350 Kinetix 5500 Kinetix 5700 Kinetix 6500 PowerFlex 755 | 80                                | 16  |

If your solution requires more than 16 Position Loop-configured drives, consider using the ControlLogix® platform. The ControlLogix platform enables up to 100 Position Loop-configured drives.

(1) Available at software version 31 and firmware revision 31.

## Time Synchronization

Integrated Motion over an EtherNet/IP network requires Time Synchronization, also known as CIP Sync™. CIP Sync provides accurate real-time (real-world time) or Coordinated Universal Time (UTC) synchronization of CompactLogix 5370 controllers and devices that are connected over an EtherNet/IP network.

CIP Sync is a time-synchronization protocol that can be applied to various applications. This chapter focuses on how to use the protocol in applications with Integrated Motion over an EtherNet/IP network.

In a CompactLogix system, the following devices are CIP Sync-capable:

- All CompactLogix 5370 controllers - Required

## IMPORTANT

While all CompactLogix 5370 controllers are CIP Sync-capable, not all controllers support Integrated Motion over an EtherNet/IP network.

A controller must be CIP Sync-capable and synchronized with other devices on the EtherNet/IP network to support Integrated Motion over an EtherNet/IP network. However, the condition of being CIP Sync-capable does not exclusively qualify a CompactLogix 5370 controller to support Integrated Motion over an EtherNet/IP network.

All controllers and communication modules must have time synchronization enabled to participate in CIP Sync.

CIP Sync requires that devices in the system function in the following roles:

- Grandmaster, also known as the coordinated system time (CST) master - Sets time for the entire system and passes the time to a Master
- Master - Sets time for its backplane
- Slave - Uses time set by Master

Configure Integrated Motion To use Integrated Motion on the EtherNet/IP network, complete the steps that are detailed in
ii this section.

| IMPORTANT   | These steps show a 1769-L36ERM controller. The same steps apply to other CompactLogix 5370 controllers that support Integrated Motion over an EtherNet/IP network with slight variations in screens.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | This section assumes that you’ve previously created a project for your 1769-L36ERM controller. If you haven’t, do so before continuing.                                                                |

## Enable Time Synchronization

Integrated Motion on the EtherNet/IP network configuration begins with enabling time synchronization in a CompactLogix 5370 controller.

To enable Time Synchronization on a CompactLogix 5370 controller, complete these steps.

1. In the Controller Organizer, right-click your controller and select Properties.

<!-- image -->

The Controller Properties dialog box appears.

2. Select the Date/Time tab.
3. Select Enable Time Synchronization.
4. Select OK.

<!-- image -->

## Add a Drive

You can only use these drives in an application that uses Integrated Motion over an EtherNet/ IP network:

- Kinetix 350 drive
- Kinetix 5500 drive
- Kinetix 5700 drive
- Kinetix 6500 drive
- PowerFlex 755 AC drive

## IMPORTANT

These steps show a Kinetix 350 drive in a 1769-L36ERM control system. The same steps apply to other CompactLogix 5370 controllers that support Integrated Motion over an EtherNet/IP network with slight variations in screens.

1. In the I/O configuration tree, right-click the Ethernet network and select New Module.

<!-- image -->

The Select Module Type dialog box appears.

2. Select the desired drive and select Create.

<!-- image -->

The New Module dialog box appears.

3. Enter a name for the module.
4. Enter a description, if desired.
5. Assign an EtherNet/IP address.

For information on setting the IP addresses, see the publications for each drive type that is listed on page 11 .

<!-- image -->

6. If you must change the configuration for any of the following parameters, select Change in the Module Definition area:
- Revision
- Electronic Keying
- Connection
- Power Structure
- Verify Power Rating on Connection

The Module dialog box appears.

<!-- image -->

7. Make the desired changes and select OK.
8. To create the drive in your project, select OK.
9. Add other components that your project requires.

## Scalability in Applications Using Integrated Motion

CompactLogix 5370 controllers offer various levels of flexibility and scalability to operate in control systems that use Integrated Motion on EtherNet/IP networks.

You can use the following controllers in control systems that require simpler configuration and complex configuration of Integrated Motion on

EtherNet/IP networks parameters:

- 1769-L30ERM, 1769-L30ERMK
- 1769-L33ERM, 1769-L33ERMK
- 1769-L33ERMO
- 1769-L36ERM
- 1769-L36ERMO
- 1769-L37ERM, 1769-L37ERMK
- 1769-L37ERMO(1)
- 1769-L38ERM, 1769-L38ERMK
- 1769-L38ERMO(1)

Control Systems Requiring Simple Configuration

Relatively simple control systems that use Integrated Motion over an EtherNet/IP network often include unmanaged switches, such as a Stratix® 2000 switch, and Kinetix 350 drives, as shown in this example.

<!-- image -->

## Control Systems Requiring Complex Configuration

Complex control systems that use Integrated Motion over an EtherNet/IP network often include managed switches. This example shows such a configuration with Stratix 6000 switch, and Kinetix 6500 and PowerFlex 755 drives.

<!-- image -->

## 1769-L18ERM-BB1B

The 1769-L18ERM-BB1B controller is typically used in control systems that require simpler configuration regarding using Integrated Motion over an EtherNet/IP network.

The simpler control system often includes unmanaged switches, such a Stratix 2000 switch, and Kinetix 350 drives, as shown in this example.

<!-- image -->

## 1769-L27ERM-QBFC1B Controller

The 1769-L27ERM-QBFC1B controller is typically used in control systems that require simpler configuration regarding using Integrated Motion over an EtherNet/IP network.

The simpler control system often includes unmanaged switches, such a Stratix 2000 switch, and Kinetix 350 drives, as shown in this example.

<!-- image -->

For more information on Integrated Motion over an EtherNet/IP network, see the publications that are listed on page 11 .

## Use a Secure Digital Card

This chapter describes the primary tasks that are required to store a project on an SD card or load a project from an SD card to the CompactLogix™ 5370 controller.

## IMPORTANT

The life expectancy of nonvolatile media is dependent on the number of write cycles that are performed. Nonvolatile media use a wear leveling technique, or technology for prolonging the service life, but avoid frequent writes.

Avoid frequent writes when logging data. We recommend that you log data to a buffer in the memory of your controller and limit the number of times data is written to removable media.

CompactLogix 5370 controllers support nonvolatile storage through the following SD cards:

- 1784-SD1 - Ships with CompactLogix 5370 controller and offers 1 GB of memory. You can order more 1784-SD1 cards if desired.
- 1784-SD2 cards - Available for separate purchase and offer 2 GB of memory.

For information on how to install or remove an SD card from a CompactLogix 5370 controller, see Chapter 4, page 61

.

## IMPORTANT

<!-- image -->

We recommend that you leave the SD card installed in the controller and the card unlocked. The SD card saves extended diagnostic information that you can send to Rockwell Automation that provides enhanced diagnostics of your application and firmware revision if circumstances require this data.

This section briefly describes how to use the SD card when installed in a CompactLogix 5370 controller. The section details how to store a project from the controller to the SD card and how to load a project from the SD card to the controller.

However, you can complete other tasks by using the SD card, such as the following:

- Change the image that is loaded from the card
- Check for a load that was completed
- Clear an image from the memory card
- Store an empty image
- Change load parameters
- Read/write application data to the card

For more detailed information on how to use an SD card, see the Logix 5000™ Controllers Nonvolatile Memory Card Programming Manual, publication 1756-PM017.

## Store or Load a Project with the Secure Digital Card

There are several options for when to load the project back into the user memory (RAM) of the CompactLogix 5370 controller. The controller configuration determines the option that is used.

This table describes the conditions and necessary configuration settings that are required for a project to be loaded from an SD card.

## Conditions and Settings for Project Loading

| Condition to Load Project from an SD Card into Controller RAM   | Required Setting in Controller Configuration   | Notes                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller power-up On Power Up                                 |                                                | • During a power cycle, you lose any online changes and tag values you haven’t stored on the memory card. • A load from a memory card can also change the firmware of the controller. • For more information, see the Logix 5000 Controllers Nonvolatile Memory Card Programming Manual, publication 1756-PM017. • You can use the application to load the project. |
| No project in the controller and you power up the controller    | On Corrupt Memory                              | • During a power cycle, you lose any online changes and tag values you haven’t stored on the memory card. • A load from a memory card can also change the firmware of the controller. • For more information, see the Logix 5000 Controllers Nonvolatile Memory Card Programming Manual, publication 1756-PM017. • You can use the application to load the project. |
| Only through application User Initiated                         |                                                | You lose any online changes and tag values that you haven’t stored on the memory card.                                                                                                                                                                                                                                                                              |

## Store a Project

Follow these steps to store a project. These steps show a 1769-L18ERM-BB1B controller. The same steps apply for other CompactLogix 5370 controllers.

1. Go online with the controller.
2. Put the controller in Program mode, that is, Remote Program or Program.
3. On the Online toolbar, select the controller properties icon.
4. Select the Nonvolatile Memory tab.
5. Select Load/Store.

<!-- image -->

<!-- image -->

<!-- image -->

If Load/Store is dimmed (unavailable), verify the following:

- You've specified the correct communication path and are online with the controller.
- The memory card is installed.

If the memory card isn't installed, this message appears in the lower-left corner of the Nonvolatile Memory tab, indicating the missing card.

<!-- image -->

Nonvolatile memory not present.

6. Select under what conditions to load the project into the user memory of the controller.

<!-- image -->

If you select On Power Up or On Corrupt Memory, you must also select the mode that you want the controller to go to after the load:

- Remote Program
- Remote Run
7. In the Automatic Firmware Update box, use the default (disable) or select the Firmware Supervisor option.

IMPORTANT The Firmware Supervisor option isn't used to update the controller firmware.

8. Select &lt;- Store.

IMPORTANT Store isn't active if an SD card is locked.

A dialog box displays to confirm the store.

9. To store the project, select Yes.
10. Select OK.

After you select Store, the project is saved to the SD card as indicated by the controller status indicators. These conditions can exist:

- While the store is in progress, the following occurs:
- The OK indicator is flashing green.
- The SD indicator is flashing green.
- A dialog box indicates that the store is in progress.
- When the store is complete, the following occurs:
- The controller resets itself.

When the controller is resets itself, the status indicators execute a sequence of state changes, such as the OK status indicator briefly in the steady red state. Wait for the controller to complete the sequence.

- After the controller fully resets itself, the OK indicator is steady green.
- The SD indicator is off.

IMPORTANT

Allow the store to complete without interruption. If you interrupt the store, data corruption or loss can occur.

## Load a Project

Follow these steps to use the application to load the project from an SD card. These steps show a 1769-L18ERM-BB1B controller. The same steps apply for other CompactLogix 5370 controllers.

1. Go online with the controller.
2. Put the controller in Program mode, that is, Remote Program or Program.
3. On the Online toolbar, select the controller properties icon.
4. Select the Nonvolatile Memory tab.
5. Select Load/Store.
6. Select Load.

<!-- image -->

<!-- image -->

A dialog box prompts you to confirm the load.

<!-- image -->

7. To load the project, select Yes.
8. Select OK.

After you select Load, the project is loaded into the controller as indicated by the controller status indicators. These conditions can exist:

- While the load is in progress, the following occurs:
- The controller resets itself.

When the controller is resetting itself, the status indicators execute a sequence of state changes, for example, a brief time with the OK status indicator in the steady red state. Wait for the controller to complete the sequence.

- After the controller fully resets itself, the OK indicator is steady green.

The SD indicator is off.

## Use Logix Designer Application for Troubleshooting

## Troubleshoot the Module

This section explains how to interpret the status indicators on your CompactLogix™ 5370 controllers. All controllers use the status indicators that are described in this table.

| Status Indicator Description   |                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------|
|                                | RUN Indicates the operating mode of the controller.                                          |
|                                | FORCE Indicates the force state.                                                             |
| I/O                            | Indicates the current state of communication between the controller and I/O modules.         |
| OK                             | Indicates the state of the controller.                                                       |
| NS                             | Indicates the EtherNet/IP™ network status regarding the controller operating on the network. |
|                                | LINK 1 Indicates the EtherNet/IP link status for port 1 if the controller.                   |
|                                | LINK 2 Indicates the EtherNet/IP link status for port 2 of the controller.                   |
| SD                             | Indicates if there’s activity on the SD card.                                                |

This section details the ways in which the Logix Designer application indicates fault conditions.

Warning signal on the main screen next to the module - This occurs when the connection to the module is broken. The controller state also indicates Faulted and the Controller fault is illuminated in red.

<!-- image -->

<!-- image -->

## Message in the status line of a screen.

<!-- image -->

On the Module Info tab, in the Status section, the Major and Minor Faults are listed along with the Internal State of the module.

Notification in the Tag Editor - General module faults are also reported in the Tag Editor. Diagnostic faults are reported only in the tag editor.

The Value field indicates a fault with the number 1.

<!-- image -->

## Fault Type Determination

To display recent fault information in the Major Faults tab of the Module Properties screen, you must select the Major Fault on Controller option in the Connection tab.

<!-- image -->

The Major Faults tab indicates the type of fault under Recent Faults. A fault displays here when you're monitoring the configuration properties of a module in the Logix Designer application and receive a Communication fault message.

<!-- image -->

## Use the CompactLogix 5370 Controllers Status Indicators

This graphic shows the controller status indicators for all CompactLogix 5370 controllers.

<!-- image -->

## Controller Mode (RUN) Status Indicator

| Status   | Description                                |
|----------|--------------------------------------------|
| Off      | The controller is in Program or Test mode. |
| Green    | The controller is in Run mode.             |

## Force State (FORCE) Status Indicator

| Status          | Description                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Off             | No tags contain I/O force values. I/O forces are inactive (disabled).                                                  |
| Yellow          | I/O forces are active (enabled). I/O force values can exist.                                                           |
| Flashing yellow | One or more input or output addresses have been forced to an On or Off condition, but the forces haven’t been enabled. |

## I/O State (I/O) Status Indicator

| Status       | Description                                                                                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off          | One of the following conditions exists: • There are no devices in the I/O configuration of the controller. - Applies to only CompactLogix 5370 L3 controllers. • The controller does not contain a project. |
| Green        | The controller is communicating with all devices in its I/O configuration.                                                                                                                                  |
|              | Flashing green One or more devices in the I/O configuration of the controller aren’t responding.                                                                                                            |
| Flashing red | One of the following conditions exists: • The controller isn’t communicating with any devices. • A fault has occurred on the controller. - Only CompactLogix 5370 L1 and L2 controllers.                    |

## Controller Status (OK) Status Indicator

| Status       | Description                                                                                                                                                                                                                                                                                                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off          | No power is applied.                                                                                                                                                                                                                                                                                                                                                     |
| Green        | The controller is OK.                                                                                                                                                                                                                                                                                                                                                    |
|              | Flashing green The controller is storing a project to or loading a project from the SD card.                                                                                                                                                                                                                                                                             |
| Red          | The controller detected a nonrecoverable major fault and cleared the project from memory.                                                                                                                                                                                                                                                                                |
| Flashing red | One of the following: • The controller requires a firmware update. • A major recoverable fault occurred on the controller. • A nonrecoverable major fault occurred on the controller and cleared the program from memory. • A controller firmware update is in process. • An embedded I/O module firmware update is in process. - Only CompactLogix 5370 L1 controllers. |
|              | Dim green to red Save to Flash at power-down.                                                                                                                                                                                                                                                                                                                            |

## Ethernet Network Status (NS) Status Indicator

| Status   | Description                                                                                        |
|----------|----------------------------------------------------------------------------------------------------|
| Off      | The port isn’t initialized; it does not have an IP address and is operating in BOOTP or DHCP mode. |
| Green    | The port has an IP address and CIP™ connections are established.                                   |
|          | Flashing green The port has an IP address, but no CIP connections are established.                 |
| Red      | The port has detected that the assigned IP address is in use.                                      |
|          | Flashing red/green The port is performing its power-up self-test.                                  |

## Ethernet Link Status (LINK 1/LINK 2) Status Indicator

| Status         | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off            | One of the following conditions exists: • No link. • Port administratively disabled. • Port disabled because rapid ring fault condition was detected (LINK2).                                                                                                                                                                                                 |
| Green          | One of the following conditions exists: • A 100 Mbps link (half- or full-duplex) exists, no activity. • A 10 Mbps link (half- or full-duplex) exists, no activity. • Ring network is operating normally and the controller is the active supervisor. • Ring network has encountered a rare partial network fault and the controller is the active supervisor. |
| Flashing green | One of the following conditions exists: • A 100 Mbps link exists and there’s activity. • A 10 Mbps link exists and there’s activity.                                                                                                                                                                                                                          |

## SD Card Activity (SD) Status Indicator

| Status       | Description                                                              |
|--------------|--------------------------------------------------------------------------|
| Off          | There’s no activity to the SD card.                                      |
|              | Flashing green The controller is reading from or writing to the SD card. |
| Flashing red | The SD card does not have a file system.                                 |

## Notes:

## Product Comparison

## Replacement Considerations

CompactLogix™ 5370 L1 series B and C controllers are direct replacements of the series A controllers. The series B and C controllers have an improved power supply circuit to the isolated power supply so that a second power supply is no longer needed.

The series A controller requires two power supplies:

- One to supply the controller power (VDC)
- One to supply the field power (FP)

This section details certain characteristics to consider when comparing CompactLogix 5370 L1 series A, B, and C controllers.

## Power Considerations

CompactLogix 5370 L1 series A, B, and C controllers

| Characteristics                                            | CompactLogix L1 Series B and C CompactLogix L1 Series A   |                                                   |
|------------------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------|
| Power dissipation                                          | 11.5 W                                                    | 12 W                                              |
| Recommended external short circuit protection, field power | User-provided 4...5 A @ 3.15...5.5 I²t fuse               | User-provided 4...6 A @ ² p 52.5...68.25 I²t fuse                                                   |
| Embedded power supply                                      |                                                           | 24V DC input, isolated 24V DC input, non-isolated |
| Line requirement (V DC), min                               | 30VA                                                      | 50VA                                              |
| Current draw @ 24V DC, field power, max                    | 3 A @ 24V DC                                              | –                                                 |

## Embedded DC Input Considerations

CompactLogix 5370 L1 series A, B, and C controllers

| Characteristics        | CompactLogix L1 Series B and C CompactLogix L1 Series A   |        |
|------------------------|-----------------------------------------------------------|--------|
| Off-state current, max | 1 mA                                                      | 1.5 mA |
| Input impedance, max   | 5.4 k                                                    | 4.7 k |

## Firmware Compatibility

For the latest information regarding firmware compatibility, refer to Rockwell Automation Product Compatibility and Download Center at: rok.auto/pcdc

<!-- image -->

## Dimensions

There are no dimension differences between the series A controller and the series B and C controllers.

<!-- image -->

## Power Supply Wiring

## Series B and C Wiring

<!-- image -->

## Series A Wiring

<!-- image -->

## Examples

## Replace the Controller

In this example:

- Replace a series A controller with a series B or C controller OR
- Replace a series B controller with a series C controller

Requirements:

| Category             | Tasks                                                                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power Supply Wiring  | The series B or C controller requires only one power supply, but the series B or C controller does support two power supplies. You can retain the current power supply design for the series A controller and avoid rewiring. |
| Controller Firmware  | Refer to Rockwell Automation Product Compatibility and Download Center (PCDC) at: rok.auto/pcdc.                                                                                                                              |
| Programming Software | Install the Studio 5000 environment compatible with the controller firmware obtained from the PCDC.                                                                                                                           |
| Personal Computer    | Use an operating system compatible with the Studio 5000 environment obtained from the PCDC.                                                                                                                                   |

## Connect External Power to Series A L1 Controllers

## Connect Power to the Series A CompactLogix 5370 L1 Controllers

This appendix explains how to connect power to series A L1 CompactLogix™ 5370 controllers.

## IMPORTANT

This section describes how to power the controller via the VDC+ and VDC- terminals.

Connections to the VDC+ and VDC- terminals do not provide power to input or output devices that are connected to the embedded I/O modules of the controller or local expansion modules. You must connect power to the FP+ and FP- terminals to provide power to I/O devices that are connected to the embedded I/O modules of the controller or local expansion modules.

For more information on how to provide power to input or output devices that are connected to the embedded I/O modules of the controller and local expansion modules, see page 261 .

The external power supply must be dedicated to the embedded supply of the controller. The external power supply converts 115/230V AC power to 24V DC or other application-required DC voltage that is within the operating range of the controller.

<!-- image -->

WARNING: Do not connect directly to line voltage. Line voltage must be supplied by a suitable, approved isolating transformer or power supply having short circuit capacity not exceeding 100VA maximum or equivalent. The controller power requirement is 50VA.

Power is connected to the controller via a removable connector that is connected to the front of the controller. The following graphic shows the connector.

<!-- image -->

## IMPORTANT

The controller is grounded once it's installed on a DIN rail as described on page 28 .

<!-- image -->

Consider these points before completing the steps in this section:

- This section describes how to connect an external 24V DC power source to the CompactLogix 5370 L1 controller.

For information on how to provide field power to input and output devices that are connected to the embedded I/O modules of the controller and local expansion modules via the removable connector, see page 117 .

<!-- image -->

ATTENTION: You must use an external power supply that is Class 2 or SELV-listed.

- The external power supply that provides power to the CompactLogix 5370 L1 controller must be dedicated to power the controller.
- You must use a separate, dedicated external 24V DC power source to connect power to other terminals on the removable connector and devices in the system, for example, the FP+ terminal or a barcode scanner, respectively.
- The external 24V DC power source that is connected to the VDC+ and VDC- terminals on the removable connector must reside in the same enclosure as the CompactLogix 5370 L1 controller.
- Use a power source that most effectively meets your application needs. That is, calculate the power requirements for your application before choosing a power source to avoid using a power source that far exceeds your application requirements.
- This section assumes that any DIN rail that you use has been grounded following Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .
- The embedded power supply of the CompactLogix 5370 L1 controller provides power to the controller and POINTBus™ backplane. It does not provide field-side power to the embedded I/O or local expansion modules.
- Not all Class 2/SELV-listed power supplies are certified for use in all applications, for example, use in nonhazardous and hazardous environments. Before installing an external power supply, consult all specification and certification
- information to verify that you're using an acceptable external power supply.
- For example purposes, this section describes how to use a 1606-XLE120E, NEC Class 2 switched-mode power supply. The exact steps for other external power supplies can vary from the steps that are described here.

Complete these steps to connect power to the CompactLogix 5370 L1 controller. CompactLogix 5370 L1 Series B and C controllers can also be connected to power as instructed in this procedure.

1. Verify that the external 24V DC power source isn't powered.
2. Mount the external 24V DC power source on a DIN rail. The external 24V DC power source can be installed on the same DIN rail as the controller

or a separate DIN rail.

3. Connect the wires to the 24V DC+ and 24V DC- connections on the external 24V DC power source.

<!-- image -->

WARNING: If you connect or disconnect the wiring while the field-side power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

4. Pull the removable connector off the CompactLogix 5370 L1 controller.
5. Connect the wire that is connected to the 24V DC+ terminal on the external 24V DC power source to the VDC+ terminal. The VDC+ terminal is the top terminal on the removable connector.

<!-- image -->

<!-- image -->

6. Connect the wire that is connected to the 24V DC- terminal on the external 24V DC power source to the VDC- terminal. The VDC- terminal is second from the top on the removable connector.

<!-- image -->

## IMPORTANT

If your application requires a power control device, for example, a switch or relay, between the external 24V DC power source and the CompactLogix 5370 L1 controller to control when the controller is powered, you must install the power control device at the VDC+ terminal on the removable connector.

If you install the power control device at the VDC- terminal, the CompactLogix 5370 L1 controller can have problems powering up or powering down properly.

7. Plug the removable connector back into the controller.
8. Secure the removable connector in place.
9. Turn on power to the external 24V DC power source.

<!-- image -->

The following graphic shows an external 24V DC power source that is connected to a CompactLogix 5370 L1 controller.

<!-- image -->

## Connect Field Power to Series A L1 Controllers for I/ O Devices

Complete these steps to connect field power to the CompactLogix 5370 L1 series A controller. CompactLogix 5370 L1 Series B and C controllers can also be connected to field power as instructed in this procedure.

1. Verify that the separate external 24V DC power source that powers the CompactLogix 5370 L1 controller isn't powered.
2. Verify that the external 24V DC power source that is connected to the FP+ and FPterminals isn't powered.
3. Mount the external power supply that connects to the FP+ and FP- terminals on a DIN rail.

The external power supply can be installed on the same DIN rail as the controller or a separate DIN rail.

4. Connect wires to the appropriate + and - connections on the external 24V DC power source.

<!-- image -->

<!-- image -->

WARNING: If you connect or disconnect wiring while the field-side power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

5. Pull the removable connector off the CompactLogix 5370 L1 controller.

<!-- image -->

6. Connect the wire that is connected to the + terminal on the external 24V DC power source to the FP+ terminal. The FP+ terminal is the fourth terminal from the top on the removable connector.
7. Connect the wire that is connected to the - terminal on the external 24V DC power source to the FP- terminal. The FP- terminal is the fifth terminal from the top on the removable connector.
8. Plug the removable connector into the controller.
9. Secure the removable connector in place.
10. Turn on power to the separate external 24V DC power source connected to the VDC+ and VDC- terminals of the removable connector.

<!-- image -->

<!-- image -->

<!-- image -->

11. Turn on power to the external 24V DC power source connected to the FP+ and FPterminals of the removable connector.

This graphic shows separate external 24V DC power supplies connected to the VDC+/VDCand FP+/FP- terminals on the removable connector, respectively.

<!-- image -->

## IMPORTANT

Install a user-replaceable fuse with overcurrent protection of 4…6 A @ 52.5…68.25 I 2 t in line between the incoming power and the FP+ terminal.

## Notes:

## Numerics

```
1734 POINT I/O modules 117 - 144 BUS OFF detection and recovery 144 configure 138 - 142 monitor faults 143 removal and insertion under power 131 requested packet interval 132 select 117 using as local expansion modules with CompactLogix 5370 L1 controllers 24 validate layout 131 - 134 1769 Compact I/O modules 189 - 209 calculate system power consumption 194 196 CompactLogix 5370 L3 controllers 59 configure 179 - 181 , 201 - 207 connections 181 , 202 end cap detection 188 , 209 local banks available with CompactLogix 5370 L3 controllers 59 monitor faults 187 , 208 requested packet interval 175 , 181 , 193 , 202 select 145 , 189 using as local expansion modules with CompactLogix 5370 L2 controllers 41 validate layout 193 - 199 1769 Compact I/O power supplies calculate system power consumption 194 196 1784-SD1 and 1784-SD2 cards 25 , 42 installation CompactLogix 5370 L1 controllers 26 27 CompactLogix 5370 L2 controllers 4 43 44 CompactLogix 5370 L3 controllers 61 62
```

## A Add-On Instructions in project 222 application elements 211 AutoFlash 90 load firmware 94 - 96 B BOOTP server 73 set IP address 75 - 78 C CompactLogix 5370 L1 controllers connecting power 32 - 35 , 257 - 263 connections to I/O modules 139 DIN rail use 28 direct connections 139 embedded I/O module 24

```
wiring diagrams 123 embedded power supply 24 , 258 example EtherNet/IP network system configuration 18 grounding 28 , 30 I/O modules 117 - 144 installation 21 - 37 grounding 30 minimum spacing 28 mounting 28 - 29 SD card 26 - 27 system dimensions 29 integrated motion over an EtherNet/IP network 231 - 240 local expansion modules 24 BUS OFF detection and recovery 144 removal and insertion under power 131 minimum spacing 28 mounting 28 - 29 networks EtherNet/IP network connection 37 USB connection 36 parts 25 place I/O modules 134 rack-optimized connections 139 select I/O modules 117 selecting operating mode 97 - 98 status indicators 247 - 251 system components 14 , 23 system dimensions 29 wiring diagrams 123 CompactLogix 5370 L2 controllers connecting power 52 - 54 connections to I/O modules 181 DIN rail use 45 direct connections 181 embedded I/O module 41 embedded power supply 41 , 52 example DeviceNet network system configuration 20 example EtherNet/IP network system configuration 19 grounding 45 , 49 installation 39 - 56 grounding 49 minimum spacing 45 mounting 45 - 46 SD card 43 - 44 system dimensions 46 integrated motion over an EtherNet/IP network 231 - 240 local expansion modules 41 minimum spacing 45 mounting 45 - 46 networks EtherNet/IP network connection 56 USB connection 55 parts 42 rack-optimized connections 181 select I/O modules 145 selecting operating mode 97 - 98 status indicators 247 - 251 system components 14 , 41 system dimensions 46
```

## CompactLogix 5370 L3 controllers

```
available local I/O banks 59 calculate system power consumption 194 196 connecting power 64 connections to I/O modules 202 DIN rail use 70 direct connections 202 example DeviceNet network system configuration 20 example EtherNet/IP network system configuration 19 grounding 69 I/O modules 189 - 209 installation 57 - 72 grounding 69 minimum spacing 66 mounting 70 SD card 61 - 62 system dimensions 68 integrated motion over an EtherNet/IP network 231 - 240 local 1769 Compact I/O modules 59 minimum spacing 66 mounting 66 - 69 , 70 networks EtherNet/IP network connection 72 USB connection 71 parts 60 power supply distance rating 59 , 69 rack-optimized connections 202 select I/O modules 189 selecting operating mode 97 - 98 status indicators 247 - 251 system components 14 , 59 system dimensions 68 configure I/O modules for use with CompactLogix 5370 L1 controllers 138 - 142 for use with CompactLogix 5370 L2 controllers 179 - 181 for use with CompactLogix 5370 L3 controllers 201 - 207 system overhead time slice 228 connections direct CompactLogix 5370 L1 controllers 139 CompactLogix 5370 L2 controllers 181 CompactLogix 5370 L3 controllers 202 rack-optimized CompactLogix 5370 L1 controllers 139 CompactLogix 5370 L2 controllers 181 CompactLogix 5370 L3 controllers 202 to I/O modules CompactLogix 5370 L1 controllers 139 CompactLogix 5370 L2 controllers 181 CompactLogix 5370 L3 controllers 202 continuous task 214 ControlFLASH utility 73 , 90 load firmware 90 - 93 controller monitor connections 224 program 216 routine 218 tags 219 tasks 212
```

## D

```
develop applications 211 Device Level Ring topology 72 DHCP server 73 set IP address 80 DIN rail CompactLogix 5370 L1 controllers 28 CompactLogix 5370 L2 controllers 45 CompactLogix 5370 L3 controllers 70 direct connections CompactLogix 5370 L1 controllers 139 CompactLogix 5370 L2 controllers 181 CompactLogix 5370 L3 controllers 202 distance rating power supply CompactLogix 5370 L3 controllers 59 , 69 E elements control application 211 embedded I/O module CompactLogix 5370 L1 controllers 24 CompactLogix 5370 L2 controllers 41 wiring diagrams 123 embedded power supply CompactLogix 5370 L1 controllers 258 calculate system power consumption 134 , 176 CompactLogix 5370 L2 controllers 52 enclosures minimum spacing CompactLogix 5370 L1 controllers 28 CompactLogix 5370 L2 controllers 45 system dimensions CompactLogix 5370 L1 controllers 29 CompactLogix 5370 L2 controllers 46 EtherNet/IP network available network topologies 37 , 56 , 72 change IP address 86 - 89 via Logix Designer application 88 via RSLinx Classic software 87 via SD card 89 connection for CompactLogix 5370 L1 controllers 37 connection for CompactLogix 5370 L2 controllers 56 connection for CompactLogix 5370 L3 controllers 72 example configurations 18 - 19 Integrated Motion over an EtherNet/IP network 16 , 231 - 240 set IP address 74 - 85 via BOOTP server 75 - 78 via DHCP server 80 via Logix Designer application 82 - 84 via RSLinx Classic software 81 - 82 via SD card 85 event task 135 - 137 , 214
```

## F

## fault code

use GSV to get 225

## faults

```
monitor I/O module faults CompactLogix 5370 L1 controllers 143 CompactLogix 5370 L2 controllers 187 CompactLogix 5370 L3 controllers 208
```

## firmware

```
load 90 - 96 via AutoFlash 94 - 96 via ControlFLASH utility 90 - 93 via SD card 96
```

## G

## grounding

CompactLogix 5370 L1 controllers

CompactLogix 5370 L2 controllers

CompactLogix 5370 L3 controllers fault code

225

monitor connection

## I

## I/O modules

```
calculate system power consumption CompactLogix 5370 L1 controllers 134 CompactLogix 5370 L2 controllers 176 CompactLogix 5370 L3 controllers 194 -196 CompactLogix 5370 L1 controllers 117 - 144 BUS OFF detection and recovery 144 local expansion modules 127 CompactLogix 5370 L2 controllers 145 - 188 local expansion modules 172 CompactLogix 5370 L3 controllers 1 189 - 209 local 1769 Compact I/O modules 59 configure for use with CompactLogix 5370 L1 controllers 138 - 142 for use with CompactLogix 5370 L2 controllers 179 - 181 for use with CompactLogix 5370 L3 controllers 201 - 207 connections CompactLogix 5370 L1 controllers 139 CompactLogix 5370 L2 controllers 181 CompactLogix 5370 L3 controllers 202 embedded I/O module on CompactLogix 5370 L1 controllers 24 embedded I/O module on CompactLogix 5370 L2 controllers 41 end cap detection CompactLogix 5370 L2 controllers 188 CompactLogix 5370 L3 controllers 209 monitor faults CompactLogix 5370 L1 controllers 143 CompactLogix 5370 L2 controllers 187 CompactLogix 5370 L3 controllers 208 place CompactLogix 5370 L1 controllers 134 requested packet interval 181 , 202 CompactLogix 5370 L1 controllers 1 132 , 139 CompactLogix 5370 L2 controllers 175 CompactLogix 5370 L3 controllers 193 select CompactLogix 5370 L1 controllers 117
```

## GSV

225

28

,

45

30

,

69

49

| CompactLogix 5370 L2 controllers  145 CompactLogix 5370 L3 controllers  189 validate layout 1734 POINT I/O modules  131 - 134 1769 Compact I/O modules  175 - 178 ,  193 - 199 CompactLogix 5370 L1 controllers   1  131 -  134 CompactLogix 5370 L2 controllers  175  -  178 CompactLogix 5370 L3 controllers  193  -  199                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| installation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CompactLogix 5370 L2 controllers  45 CompactLogix 5370 L3 controllers  70 grounding CompactLogix 5370 L1 controllers  30 CompactLogix 5370 L2 controllers  49 CompactLogix 5370 L3 controllers  69 local 1769 Compact I/O modules CompactLogix 5370 L3 controllers  189 minimum spacing CompactLogix 5370 L1 controllers  28 CompactLogix 5370 L2 controllers  45 CompactLogix 5370 L3 controllers  66 mounting CompactLogix 5370 L1 controllers  28 -  29 CompactLogix 5370 L2 controllers   4  45 -  46 CompactLogix 5370 L3 controllers   6  66 -  69 ,  70 panel mounting CompactLogix 5370 L3 controllers  70 power supply connections to CompactLogix 5370 L1 controllers  32 - 35 ,  257 -  263 power supply connections to CompactLogix 5370 L2 controllers  52 - 54 required software tasks  73 - 98 SD card CompactLogix 5370 L1 controllers  26 -  27 CompactLogix 5370 L2 controllers   4  43 -  44 CompactLogix 5370 L3 controllers  62 system dimensions CompactLogix 5370 L1 controllers  29 CompactLogix 5370 L2 controllers  CompactLogix 5370 L3 controllers  network  16 ,  231 - 240 configure  235 - 237 drive limits  233 |
| 61 -  46 68 Integrated Motion over an EtherNet/IP example configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

| via SD card  89 set  74 - 85 via BOOTP server  75 - 78 via DHCP server  80 via Logix Designer application  82 - 84 via RSLinx Classic software  81 - 82 via SD card  85  L linear network topology  72 local 1769 Compact I/O modules CompactLogix 5370 L3 controllers  59 local expansion modules 1734 POINT I/O modules  24 1769 Compact I/O modules  41   | 5370 L1 controllers  37 network connection for CompactLogix 5370 L2 controllers  56 network connection for CompactLogix 5370 L3 controllers  72 set IP address via BOOTP server   7  75 - 78 set IP address via DHCP server  80 set IP address via Logix Designer ap plication  82 - 84 set IP address via RSLinx Classic soft ware  81 - 82 set IP address via SD card  85 USB connection for CompactLogix 5370 L1 controllers  36 connection for CompactLogix 5370 L2 controllers  55                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CompactLogix 5370 L1 controllers  24 CompactLogix 5370 L2 controllers  41 local I/O banks CompactLogix 5370 L3 controllers  59 Logix Designer application AutoFlash  90 change IP address  88 configure I/O modules                                                                                                                                          | connection for CompactLogix 5370 L3 controllers  71 O operating mode selecting  97 - 98                                                                                                                                                                                                                                                                      |
| controllers  controllers  controllers                                                                                                                                                                                                                                                                                                                        | P panel mounting CompactLogix 5370 L3 controllers  70 periodic task  214 power supply connections to CompactLogix 5370 L1 controllers  32 - 35 ,  257 - 263 connections to CompactLogix 5370 L2 controllers  52 - 54 connections to CompactLogix 5370 L3 controllers  64 distance rating CompactLogix 5370 L3 controllers  69 5370 L1 controllers  24 ,  258 |
| memory storage SD cards  25 ,  42 minimum spacing CompactLogix 5370 L1 controllers  28 CompactLogix 5370 L2 controllers  45 CompactLogix 5370 L3 controllers  66                                                                                                                                                                                             | embedded power supply with CompactLogix embedded power supply with CompactLogix 5370 L2 controllers  41 ,  52 priority                                                                                                                                                                                                                                       |
| mounting CompactLogix 5370 L1 controllers  28 - 29 CompactLogix 5370 L2 controllers  45 - 46 CompactLogix 5370 L3 controllers  66 - 69 ,  70                                                                                                                                                                                                                 | task  215 program in project  216 scheduled  217 system overhead time slice  227 unscheduled  217                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              | 221                                                                                                                                                                                                                                                                                                                                                          |
| N                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                              |
| networks                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                              |
| for use with CompactLogix 5370 L1 138 - 142                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                              |
| for use with CompactLogix 5370 L2 179 - 181 for use with CompactLogix 5370 L3 201 - 207                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                              |
| Integrated Motion over an EtherNet/IP network  231 - 240                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                              |
| 245 - 246 82 - 84                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                              |
| 135 - 137                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                              |
| load a project to an SD card  set IP address  store a project to an SD card  243 - 244 using event task                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                              |
| M                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                              |
| DeviceNet                                                                                                                                                                                                                                                                                                                                                    | R                                                                                                                                                                                                                                                                                                                                                            |
| example CompactLogix 5370 L2 con troller system configuration  20 example CompactLogix 5370 L3 con troller system configuration                                                                                                                                                                                                                                                                                                                                                              | CompactLogix 5370 L1 controllers  CompactLogix 5370 L2 controllers                                                                                                                                                                                                                                                                                           |
| 20 EtherNet/IP application  88                                                                                                                                                                                                                                                                                                                               | 181 CompactLogix 5370 L3 controllers  202                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              | removal and insertion under power                                                                                                                                                                                                                                                                                                                            |
| change IP address via Logix Designer                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                              |
| change IP address via RSLinx Classic                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                              |
| software  87                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              | local expansion modules                                                                                                                                                                                                                                                                                                                                      |
| 89                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                              |
| change IP address via SD card                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              | rack-optimized connections 139                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              | programming languages                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              | project                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                              | elements  211                                                                                                                                                                                                                                                                                                                                                |
| 18 - 19                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                              |
| example configurations                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              | CompactLogix 5370 L1 controllers                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                              | 131                                                                                                                                                                                                                                                                                                                                                          |
| network connection for CompactLogix                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                              |

## requested packet interval

```
CompactLogix 5370 L1 controllers 132 , 139 CompactLogix 5370 L2 controllers 175 , 181 CompactLogix 5370 L3 controllers 193 , 202 routine in project 218 RSLinx Classic software 73 change IP address 87 set IP address 81 - 82 RSLogix 5000 software 73 RSNetWorx for DeviceNet software 73 S sample projects 229 scheduled program 217 SD card 90 , 241 - 246 change IP address 89 installation CompactLogix 5370 L1 controllers 26 27 CompactLogix 5370 L2 controllers 4 43 44 CompactLogix 5370 L3 controllers 61 62 load a project 245 - 246 load firmware 96 set IP address 85 store a project 243 - 244 software BOOTP 73 set IP address 75 - 78 DHCP 73 set IP address 80 Logix Designer application AutoFlash 90 required installation tasks 73 - 98 RSLinx Classic 73 change IP address 87 set IP address 81 - 82 RSLogix 5000 73 RSNetWorx for DeviceNet 73 Studio 5000 environment 73 star network topology 72 status monitor connections 224 status indicators 247 - 251 Studio 5000 environment 73 Studio 5000 Logix Designer application. See Logix Designer application system assembly calculate system power consumption CompactLogix 5370 L1 controllers 1 134 , 176 CompactLogix 5370 L3 controllers 194 -196 CompactLogix 5370 L3 controllers select I/O modules 189 place I/O modules CompactLogix 5370 L1 controllers 134 select I/O modules CompactLogix 5370 L1 controllers 117 CompactLogix 5370 L2 controllers 145 validate I/O modules layout
```

```
1734 POINT I/O modules 131 - 134 1769 Compact I/O modules 175 - 178 CompactLogix 5370 L1 controllers 1 131 134 CompactLogix 5370 L2 controllers 175 -178 CompactLogix 5370 L3 controllers 193 -199 system components CompactLogix 5370 L1 controllers 14 , 23 CompactLogix 5370 L2 controllers 14 , 41 CompactLogix 5370 L3 controllers 14 , 59 system dimensions CompactLogix 5370 L1 controllers 29 CompactLogix 5370 L2 controllers 46 CompactLogix 5370 L3 controllers 68 system overhead time slice 227 configure 228 system power consumption calculate CompactLogix 5370 L1 controllers 1 134 , 176 CompactLogix 5370 L3 controllers 194 -196
```

## T

in project 219

continuous

214

event

135 - 137

in project

212

periodic

214

priority

215

time slice

227

## U

## unscheduled

program

## USB cable

CompactLogix 5370 L1 controllers 36

CompactLogix 5370 L2 controllers

55

CompactLogix 5370 L3 controllers 71

## V

## validate I/O modules layout

```
1734 POINT I/O modules 131 - 134 1769 Compact I/O modules 175 - 178 , 193 199
```

## W

## wiring diagrams

CompactLogix 5370 L1 controllers 123

## tag

## task

217

,

214

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

Allen-Bradley, Armor, ArmorBlock, Compact I/O, ControlFLASH, CompactLogix, ControlLogix, DriveLogix, E3 Electronic Overload Relay, expanding human possibility, FLEX I/O, FlexLogix, Integrated Architecture Builder, Kinetix, Logix 5000, On-Machine, PanelConnect, PanelView Plus, PLC-5, POINT I/O, POINTBus, PowerFlex, QuickView, Rockwell Automation, RSLinx Classic, RSLogix 5000, RSNetWorx, SLC, SoftLogix, Stratix, Studio 5000, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

CIP, CIP Sync, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation.1201S0uthSec0ndStreet,Milwaukee,W153204-2496USA.Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV.PegasusPark:DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600.Fax:(32)26630640 ASIAPAClFIC:RockwellAutamation,Level14,CoreF,Cyberport3,100CyberportRoad,HongKong,Tel:(852)28874788,Fax:(852)25081846 UNITEDKINGD0M:RockwellAutomationLtd.Pitfieid,KilnFarmMiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800.Fax:(44)（1908)261-917