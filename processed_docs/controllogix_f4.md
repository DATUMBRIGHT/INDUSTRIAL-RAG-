<!-- image -->

## ControlLogix 5570 and 5560 Controllers

Catalog Numbers 1756-L71, 1756-L72, 1756-L73, 1756-L73XT, 1756-L74, 1756-L75, 1756-L72EROM, 1756-L73EROM, 1756-L61, 1756-L62, 1756-L63, 1756-L63XT, 1756-L64, 1756-L65

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

|                             | Preface . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . . . . . . .9   |
|-----------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------|
|                             | Summary of Changes . . . .  . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . 9                  |
|                             | ControlLogix Controllers. . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . 9                        |
|                             | Standard ControlLogix Controllers . . . . . . . . . . . . . . . . . . . . . . . . . 10          |                                                        |
|                             | Redundant ControlLogix Controllers . . . . . . . . . . . . . . . . . . . . . . . 11             |                                                        |
|                             | Extreme Environment ControlLogix Controllers . . . . . . . . . . . . 11                         |                                                        |
|                             | Armor ControlLogix Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |                                                        |
|                             | Before You Begin. . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . 12             |
|                             | Required Software . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 12                     |
|                             | Additional Resources . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 13                   |
|                             | Chapter 1                                                                                       |                                                        |
| Install a ControlLogix 5570 | Before You Begin. . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . 17             |
| Controller                  | ControlLogix 5570 Controller Parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17   |                                                        |
|                             | Parts Included with ControlLogix 5570 Controllers. . . . . . . . . . 17                         |                                                        |
|                             | Parts Available for Use with ControlLogix 5570 Controllers . . 18                               |                                                        |
|                             | Controller Installation. . . . . . .  . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 18                     |
|                             | Insert the Controller into the Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 |                                                        |
|                             | Insert the Key . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . . . . . . 20                 |
|                             | Install the SD Card . . . . . . . . .  . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 21                   |
|                             | Remove the SD Card . . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . 23                   |
|                             | Install the ESM . . . . . .  . . . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . . . . . 24             |
|                             | Uninstall the ESM . . . . .  . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . 25               |
|                             | Chapter 2                                                                                       |                                                        |
| Install a ControlLogix 5560 | Before You Begin. . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . 31             |
| Controller                  | ControlLogix 5560 Controller Parts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31   |                                                        |
|                             | Parts Not Included with the Controller . . . . . . . . . . . . . . . . . . . . . 31             |                                                        |
|                             | Controller Installation. . . . . . .  . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 32                     |
|                             | CompactFlash Card Installation and Removal . . . . . . . . . . . . . . . . . . . 32             |                                                        |
|                             | Battery Connection and Replacement. . . . . . . . . . . . . . . . . . . . . . . . . . . 36      |                                                        |
|                             | Insert the Controller into the Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 |                                                        |
|                             | Remove the Controller from the Chassis . . . . . . . . . . . . . . . . . . . . . . . . 40       |                                                        |
|                             | Chapter 3                                                                                       |                                                        |
| Start Using the Controller  | Make Connections . . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 41                   |
|                             | ControlLogix 5570 Connection Options . . . . . . . . . . . . . . . . . . . . 41                 |                                                        |
|                             | ControlLogix 5560 Connection Options . . . . . . . . . . . . . . . . . . . . 41                 |                                                        |
|                             | Connect to a ControlLogix 5570 Controller . . . . . . . . . . . . . . . . . . . . 42            |                                                        |
|                             | Configure the USB Driver  . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . 43                     |
|                             | Connect to a ControlLogix 5560 Controller . . . . . . . . . . . . . . . . . . . . 45            |                                                        |
|                             | Configure the Serial Driver . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 46                       |
|                             | Upgrade Controller Firmware. . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 48                       |
|                             | Determine Required Controller Firmware. . . . . . . . . . . . . . . . . . . 49                  |                                                        |

ControlLogix System and Controllers

Communication Networks

| Obtain Controller Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                 |
|-----------------------------------------------------------------------------------------------------------------------------|
| Use ControlFLASH Software to Update Firmware. . . . . . . . . . . 50                                                        |
| Use AutoFlash to Update Firmware. . . . . . . . . . . . . . . . . . . . . . . . . 55                                        |
| Set the Communication Path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                           |
| Go Online with the Controller . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 59                        |
| Download to the Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                         |
| Use the Who Active Dialog Box to Download . . . . . . . . . . . . . . . 60                                                  |
| Use the Controller Status Menu to Download . . . . . . . . . . . . . . . 61                                                 |
| Upload from the Controller. . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 61                      |
| Use the Who Active Dialog Box to Upload . . . . . . . . . . . . . . . . . . 61                                              |
| Use the Controller Status Menu to Upload . . . . . . . . . . . . . . . . . . 62                                             |
| Choose the Controller Operation Mode . . . . . . . . . . . . . . . . . . . . . . . . 63                                     |
| Use the Mode Switch to Change the Operation Mode . . . . . . . . 63                                                         |
| Use the Logix Designer Application to Change the Operation Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65 |
| Load or Store to the Memory Card . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                               |
| Store to the Memory Card . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 66                             |
| Load from the Memory Card . .  . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 69                                |
| Other Memory Card Tasks. . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 71                               |
| Use ControlLogix Energy Storage Modules (ESMs) . . . . . . . . . . . . . . 71                                               |
| Save the Program to On-board NVS Memory . . . . . . . . . . . . . . . . 72                                                  |
| Clear the Program from Onboard NVS Memory . . . . . . . . . . . . . 72                                                      |
| Estimate the ESM Support of the WallClockTime . . . . . . . . . . . . . . . 73                                              |
| Maintain the Battery (Only 1756-L6x Controllers) . . . . . . . . . . . . . . 73                                             |
| Check the Battery Status  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 74                         |
| 1756-BA1 or 1756-BATA Battery Life . . . . . . . . . . . . . . . . . . . . . . 74                                           |
| 1756-BATM Battery Module and Battery Life . . . . . . . . . . . . . . . 75                                                  |
| Estimate 1756-BA2 Battery Life . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                   |
| Estimate 1756-BA2 Battery Life After Warnings. . . . . . . . . . . . . 77                                                   |
| Battery Storage and Disposal . .  . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 78                             |
| Chapter 4                                                                                                                   |
| ControlLogix System . . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 79                |
| Configuration Options . . . . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 79                          |
| Design a ControlLogix System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                           |
| ControlLogix Controller Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                             |
| System, Communication, and Programming Features. . . . . . . . . 83                                                         |
| Memory Options . . . . . .  . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 84                     |
| Electronic Keying. . . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 85                   |
| Chapter 5                                                                                                                   |
| Networks Available. . . .  . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . 87              |
| EtherNet/IP Network Communication. . . . . . . . . . . . . . . . . . . . . . . . . 87                                       |
| ControlLogix EtherNet/IP Module Features . . . . . . . . . . . . . . . . 88                                                 |
| ControlLogix EtherNet/IP Communication Modules . . . . . . . . 89                                                           |
| Software for EtherNet/IP Networks . . . . . . . . . . . . . . . . . . . . . . . . 90                                        |

|                                  | Connections Over an EtherNet/IP Network . . . . . . . . . . . . . . . . 90                                                                                                 |           |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|                                  | Double Data Rate (DDR) Backplane Communication . . . . . . . 90                                                                                                            |           |
|                                  | ControlNet Network Communication . . . . . . . . . . . . . . . . . . . . . . . . . 91                                                                                      |           |
|                                  | ControlLogix ControlNet Module Features . . . . . . . . . . . . . . . . . 92                                                                                               |           |
|                                  | ControlLogix ControlNet Modules . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                       |           |
|                                  | Software for ControlNet Networks . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                      |           |
|                                  | Connections Over a ControlNet Network. . . . . . . . . . . . . . . . . . . 94                                                                                              |           |
|                                  | DeviceNet Network Communication.   . . . . . . . . . . . . .  . . . . . . . . . . . . . 94                                                                                 |           |
|                                  | ControlLogix DeviceNet Module Features . . . . . . . . . . . . . . . . . . 95                                                                                              |           |
|                                  | ControlLogix DeviceNet Bridge and Linking Devices . . . . . . . . 96                                                                                                       |           |
|                                  | Software for DeviceNet Networks . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                                                     |           |
|                                  | Connections Over DeviceNet Networks . . . . . . . . . . . . . . . . . . . . 96                                                                                             |           |
|                                  | ControlLogix DeviceNet Module Memory . . . . . . . . . . . . . . . . . . 96                                                                                                |           |
|                                  | Data Highway Plus (DH+) Network Communication . . . . . . . . . . . 97                                                                                                     |           |
|                                  | Communicate Over a DH+ Network . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                            |           |
|                                  | Universal Remote I/O (RIO) Communication . . . . . . . . . . . . . . . . . . 99                                                                                            |           |
|                                  | Communicate over a Universal Remote I/O Network . . . . . . . 100                                                                                                          |           |
|                                  | Foundation Fieldbus Communication . . . . . . . . . . . . . . . . . . . . . . . . . 100                                                                                    |           |
|                                  | HART Communication . . . . . . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 102                                                                       |           |
| Chapter 6                        | Chapter 6                                                                                                                                                                  | Chapter 6 |
| Serial Communication             | ControlLogix 5560 Controller Serial Port . . . . . . . . . . . . . . . . . . . . . . 103                                                                                   |           |
| on ControlLogix 5560 Controllers | ControlLogix Chassis Serial Communication Options. . . . . . . 103                                                                                                         |           |
|                                  | Communication with Serial Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . 104                                                                                |           |
|                                  | DF1 Master Protocol . . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 104                                                                |           |
|                                  | DF1 Point to Point Protocol . . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 104                                                                      |           |
|                                  | DF1 Radio Modem Protocol . . . . .  . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 105                                                                         |           |
|                                  | DF1 Radio Modem Advantages. . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                                                      |           |
|                                  | DF1 Radio Modem Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                                                      |           |
|                                  | DF1 Radio Modem Protocol Parameters . . . . . . . . . . . . . . . . . . . 107                                                                                              |           |
|                                  | DF1 Slave Protocol . . . . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 108                                                             |           |
|                                  | DH-485 Protocol . . . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 108                                                              |           |
|                                  | ASCII Protocol . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 109                                                           |           |
|                                  | Configure the ControlLogix 5560 Controller for Serial                                                                                                                      |           |
|                                  | Broadcast Messages Over a Serial Port. . . . . . . . . . . . . . . . . . . . . . . . . . 112                                                                               |           |
|                                  | Configure Controller Serial Port Properties. . . . . . . . . . . . . . . . . 113                                                                                           |           |
|                                  | Program the Message Instruction . . . . . . . . . . . . . . . . . . . . . . . . . . 114                                                                                    |           |
|                                  | Modbus Support . . . . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 114                                                             |           |
|                                  | Chapter 7                                                                                                                                                                  |           |
| Manage Controller                | Connection Overview . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 115                                                                  |           |
| Communication                    | Produce and Consume (Interlock) Data. . . . . . . . . . . . . . . . . . . . . . . . 115                                                                                    |           |
|                                  | Connection Requirements of a Produced or Consumed Tag . 116                                                                                                                |           |
|                                  | Send and Receive Messages . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 118 Determine Whether to Cache Message Connections . . . . . . . . 118 |           |

Determine Whether to Cache Message Connections . . . . . . . . 118

|                             | Calculate Connection Use .  . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . . 119         |
|-----------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------|
|                             | Local Connections. . . . . . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 119             |
|                             | Remote Connections . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 120         |
|                             | Connections Example. . . . . . . .  . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 121               |
|                             | Chapter 8                                                                                          |                                               |
| I/O Modules                 | Selecting ControlLogix I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . 123         |                                               |
|                             | Local I/O Modules . . . . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 123           |
|                             | Add Local I/O to the I/O Configuration . . . . . . . . . . . . . . . . . . . 124                   |                                               |
|                             | Remote I/O Modules. . . . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 125           |
|                             | Add Remote I/O to the I/O Configuration. . . . . . . . . . . . . . . . . 126                       |                                               |
|                             | Distributed I/O . . .  . . . . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . . . . 129 |
|                             | Add Distributed I/O to the I/O Configuration . . . . . . . . . . . . . 130                         |                                               |
|                             | Reconfigure an I/O Module . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 132             |
|                             | Reconfigure an I/O Module Via the Module Properties. . . . . . 133                                 |                                               |
|                             | Reconfigure an I/O Module Via a Message Instruction . . . . . . 134                                |                                               |
|                             | Add to the I/O Configuration While Online . . . . . . . . . . . . . . . . . . . 134                |                                               |
|                             | Modules and Devices That Can Be Added While Online . . . . 135                                     |                                               |
|                             | Online Additions - ControlNet Considerations. . . . . . . . . . . . . 135                          |                                               |
|                             | Online Additions—EtherNet/IP Considerations . . . . . . . . . . . 138                              |                                               |
|                             | Determine When Data Is Updated . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139         |                                               |
|                             | Chapter 9                                                                                          |                                               |
| Develop Motion Applications | Motion Control Options . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 141             |
|                             | Motion Overview . . . . . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . 142         |
|                             | Obtain Axis Information . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 142             |
|                             | Program Motion Control . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 143             |
|                             | Example . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . 144         |
|                             | Chapter 10                                                                                         |                                               |
| Develop Applications        | Elements of a Control Application. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145     |                                               |
|                             | Tasks. . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . . . 145     |
|                             | Task Priority . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 148           |
|                             | Programs . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . . 148       |
|                             | Scheduled and Unscheduled Programs . . . . . . . . . . . . . . . . . . . . . 150                   |                                               |
|                             | Routines. . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . . . 151       |
|                             | Parameters and Local Tags . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 152             |
|                             | Extended Properties . . . . . . .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 153             |
|                             | Access Extended Properties in Logic. . . . . . . . . . . . . . . . . . . . . . . . 153             |                                               |
|                             | Programming Languages . . . . . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 155             |
|                             | Add-On Instructions . . . . . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 156           |
|                             | Access the Module Object . . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 157             |
|                             | Create the Add-On Instruction. . . . . . . . . . . . . . . . . . . . . . . . . . . . 157           |                                               |
|                             | Monitoring Controller Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158 |                                               |
|                             | Monitoring I/O Connections . . . .  . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 158               |
|                             | Determine If I/O Communication Has Timed Out . . . . . . . . . 160                                 |                                               |

|                             | Determine If I/O Communication to a                                                          |                                         |
|-----------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------|
|                             | Specific I/O Module Has Timed Out . . . . . . . . . . . . . . . . . . . . . . 160            |                                         |
|                             | Interrupt the Execution of Logic and                                                         |                                         |
|                             | Execute the Fault Handler. . . .  . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . 161         |
|                             | System Overhead Time Slice . . . . . . . . .  . . . . . . . . . . . . .                      | . . . . . . . . . . . . 162             |
|                             | Configure the System Overhead Time Slice . . . . . . . . . . . . . . . . . 163               |                                         |
|                             | Sample Controller Projects . .  . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . 164         |
|                             | Chapter 11                                                                                   |                                         |
| Using the PhaseManager Tool | PhaseManager Overview . . . . . .  . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . 165       |
|                             | Minimum System Requirements. .  . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . 167         |
|                             | State Model Overview . . .  . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . 167 |
|                             | How Equipment Changes States . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . 168           |
|                             | Manually Change States. . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 169       |
|                             | PhaseManager Tool versus Other State Models . . . . . . . . . . . . . . . . . 170            |                                         |
|                             | Equipment Phase Instructions. .  . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . 170       |
|                             | Appendix A                                                                                   |                                         |
| Troubleshoot the Module     | Troubleshoot in the Logix Designer Application . . . . . . . . . . . . . . . . 171           |                                         |
|                             | Fault Type Determination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173 |                                         |
|                             | ControlLogix 5570 Controller Status Display and Indicators . . . . 174                       |                                         |
|                             | ControlLogix 5570 Controller Status Display . . . . . . . . . . . . . . . . . . 174          |                                         |
|                             | General Status Messages. . . .  . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 174       |
|                             | Fault Messages . . . . . . . . . .  . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . 176     |
|                             | Major Fault Messages . . . . . .  . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . 177       |
|                             | I/O Fault Codes. . . . . . . . .  . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 179     |
|                             | ControlLogix 5570 Controller Status Indicators . . . . . . . . . . . . . . . . 182           |                                         |
|                             | RUN Indicator. . . . . . . . . . .  . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . 182       |
|                             | FORCE Indicator . . . . . . . . .  . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 182       |
|                             | SD Indicator . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . 183     |
|                             | OK Indicator . . . . . .  . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . 183 |
|                             | ControlLogix 5560 Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . 184  |                                         |
|                             | RUN Indicator. . . . . . . . . . .  . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . 184       |
|                             | I/O Indicator . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 184     |
|                             | FORCE Indicator . . . . . . . . .  . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 185       |
|                             | RS-232 Indicator . . . . . . . . .  . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . 185       |
|                             | BAT Indicator . . . . . . . . . .  . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 185     |
|                             | OK Indicator . . . . . .  . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . 186 |
|                             | Index . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 187               |

## Notes:

## Summary of Changes

## ControlLogix Controllers

This publication provides this information:

- Design and planning considerations
- Installation procedures
- Configuration procedures
- Maintenance and troubleshooting methods

This publication is designed for use by anyone responsible for planning and implementing a ControlLogix® system:

- Application engineers
- Control engineers
- Instrumentation technicians

The contents of this publication are for anyone who already has an understanding of Logix 5000® control systems, programming techniques, and communication networks.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                                                                                                       | Page   |
|-----------------------------------------------------------------------------------------------------------------------------|--------|
| Removed Redundant Systems chapter and replaced with reference to the Redundancy Systems User Manual, publication 1756-UM015 | 11     |
| Updated references to ControlLogix chassis and power supply installation instructions 13, 17, 31                            |        |
| Updated the number of programs per task for ControlLogix 5570 controllers 83                                                |        |
| Added SD Card Unprotected message                                                                                           | 175    |

There are five types of ControlLogix controllers available. These types include the following:

- Standard ControlLogix controllers
- Extreme environment ControlLogix controllers
- Armor™ ControlLogix controllers
- Standard GuardLogix® controllers
- Armor GuardLogix controllers

This manual explains how to use standard, extreme environment, and Armor ControlLogix controllers.

For detailed information about GuardLogix and Armor GuardLogix safety controllers, see the following publications.

| Resource                                                                                                | Description                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GuardLogix 5570 Controllers User Manual, publication 1756-UM022                                         | Provides information on how to install, configure, and operate GuardLogix 5570 controllers in Studio 5000 ® projects, version 21 or later.                               |
| GuardLogix 5570 and Compact GuardLogix 5370 Controller Systems Reference Manual, publication 1756-RM099 | Provides information on how to meet safety application requirements for GuardLogix 5570 controllers in Studio 5000 projects, version 21 or later.                        |
| GuardLogix Controllers User Manual, publication 1756-UM020                                              | Provides information on how to install, configure, and operate GuardLogix 5560 and GuardLogix 5570 controllers in RSLogix 5000® projects, version 20 or earlier.         |
| GuardLogix Controller Systems Safety Reference Manual, publication 1756-RM093                           | Provides information on how to meet safety application requirements for GuardLogix 5560 and GuardLogix 5570 controllers in RSLogix 5000 projects, version 20 or earlier. |
| GuardLogix Safety Application Instruction Set Safety Reference Manual, publication 1756-RM095           | Provides programmers with details about the GuardLogix safety application instruction set.                                                                               |

## Standard ControlLogix Controllers

The following table describes ControlLogix 5560 and 5570 catalog numbers.

Table 1 - ControlLogix Catalog Numbers

| Controller Family Cat. No.                                        |
|-------------------------------------------------------------------|
| ControlLogix 5560 1756-L61, 1756-L62,1756-L63, 1756-L64,1756-L65  |
| ControlLogix 5570 1756-L71, 1756-L72, 1756-L73,1756-L74, 1756-L75 |

The standard ControlLogix controllers share many similar features, but also have some differences. The following table provides an overview of the differences between the controllers. For further details about these features and differences, see the appropriate chapters of this manual.

Table 2 - Differences between ControlLogix 5570 and 5560 Controllers

| Feature                                                    | ControlLogix 5570                                   | ControlLogix 5560     |
|------------------------------------------------------------|-----------------------------------------------------|-----------------------|
| Clock support and backup for memory retention at powerdown | Energy Storage Module (ESM) Battery                 |                       |
| Communication ports (built-in) USB                         |                                                     | Serial                |
| Connections, controller                                    | 500                                                 | 250                   |
| Memory, nonvolatile                                        | Secure Digital (SD) card                            | CompactFlash card     |
| Status display and status indicators                       | Scrolling status display and four status indicators | Six status indicators |
| Unconnected buffer defaults 20 (40, max)                   |                                                     | 10 (40, max)          |

For information on using ControlLogix controllers in SIL 2 applications, see the ControlLogix SIL 2 Applications Safety Reference Manual, publication 1756-RM001 .

## Redundant ControlLogix Controllers

Certain ControlLogix controllers are also supported for use in redundancy systems. For more information about controllers and redundancy systems, see the Redundancy Systems User Manual, publication 1756-UM015 .

## Extreme Environment ControlLogix Controllers

The extreme environment ControlLogix controllers, catalog numbers 1756-L73XT and 1756-L63XT, provide the same functionality as the 1756-L73 and 1756-L63 controllers, but are designed to withstand temperatures -25…+70 °C (-13…+158 °F).

## Armor ControlLogix Controllers

The Armor ControlLogix controller combines a 1756-L72 or 1756-L73 ControlLogix controller with two EtherNet/IP™ DLR-capable 1756-EN3TR communication modules in an IP67-rated housing for mounting on a machine. For more information about the Armor ControlLogix controllers, catalog numbers 1756-L72EROM and 1756-L73EROM, refer to the Armor ControlLogix Controller Installation Instructions, publication 1756-IN061 .

Though the 1756-L72EROM and 1756-L73EROM controllers have functionality identical to that of the 1756-L72 and 1756-L73 controllers, the Armor controller energy storage modules (ESM) cannot be removed or replaced.

## Before You Begin

Before you begin using your ControlLogix controller, verify that you have the applications that are required to configure and program the controller.

## Required Software

Use Table 3 to identify the minimum software versions that are required to use your ControlLogix controller.

Table 3 - Required Software for Controller Use

|              | Cat. No. Studio 5000 Environment RSLogix 5000 Software RSLinx® Classic                                                               |                                                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|              | 1756-L61/A — Version 12.06.00 or later Any version                                                                                   |                                                                              |
|              | 1756-L61/B — Version 13.04.00 or later                                                                                               |                                                                              |
|              | 1756-L62/A — Version 12.06.00 or later                                                                                               |                                                                              |
|              | 1756-L62/B — Version 13.04.00 or later                                                                                               |                                                                              |
|              | 1756-L63/A — • If not using a CompactFlash card, version 10.07.00 or later • If using a CompactFlash card, version 11.16.00 or later |                                                                              |
|              | 1756-L63/B — Version 13.04.00 or later                                                                                               |                                                                              |
|              | 1756-L63XT/B — Version 13.04.00 or later Version 2.55.00 or later                                                                    |                                                                              |
|              | 1756-L64/B — Version 16.03.00 or later Any version                                                                                   |                                                                              |
|              | 1756-L65/B — Version 17.01.02 or later                                                                                               |                                                                              |
|              |                                                                                                                                      | 1756-L71 Version 21.00.00 or later Version 20.01.02 Version 2.59.00 or later |
|              |                                                                                                                                      | 1756-L72 Version 19.01.00 or later Version 2.57.00 or later                  |
| 1756-L73     |                                                                                                                                      | 1756-L72 Version 19.01.00 or later Version 2.57.00 or later                  |
| 1756-L73XT   |                                                                                                                                      | 1756-L72 Version 19.01.00 or later Version 2.57.00 or later                  |
| 1756-L74     |                                                                                                                                      | 1756-L72 Version 19.01.00 or later Version 2.57.00 or later                  |
| 1756-L75     |                                                                                                                                      | 1756-L72 Version 19.01.00 or later Version 2.57.00 or later                  |
|              |                                                                                                                                      | 1756-L72EROM 2.59.02 or later                                                |
| 1756-L73EROM |                                                                                                                                      | 1756-L72EROM 2.59.02 or later                                                |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                              | Description                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756 ControlLogix and GuardLogix Controllers Technical Data, publication 1756-TD001                                   | Provides specifications for ControlLogix and GuardLogix controllers.                                                                           |
| 1756 ControlLogix I/O Specifications Technical Data, publication 1756-TD002                                           | Provides specifications for ControlLogix I/O modules.                                                                                          |
| ControlLogix 5570 Controllers Installation Instructions, publication 1756-IN088                                       | Provides installation instructions for ControlLogix 5570 controllers.                                                                          |
| Armor ControlLogix Controllers Installation Instructions, publication 1756-IN061                                      | Provides information about how to install the Armor ControlLogix controllers.                                                                  |
| ControlLogix Battery Module Installation Instructions, publication 1756-IN576                                         | Provides information for battery module installation.                                                                                          |
| ControlLogix Chassis Installation Instructions, publication1756-IN621                                                 | Describes how to install and troubleshoot standard and ControlLogix-XT™ versions of the 1756 chassis.                                          |
| ControlLogix Power Supply Installation Instructions, publication 1756-IN619                                           | Provides information on how to install ControlLogix standard power supplies.                                                                   |
| ControlLogix Redundant Power Supply Installation Instructions, publication 1756-IN620                                 | Provides information on how to install ControlLogix redundant power supplies.                                                                  |
| ControlLogix Analog I/O Modules User Manual, publication 1756-UM009                                                   | Provides information about analog I/O module configuration properties.                                                                         |
| ControlLogix Configurable Flowmeter Module User Manual, publication 1756-UM010                                        | Provides information about configurable flowmeter configuration properties.                                                                    |
| ControlLogix Data Highway Plus-Remote I/O Communication Interface Module User Manual, publication 1756-UM514          | Provides information about Data Highway Plus™ communication and remote I/O communication module configuration properties.                      |
| ControlLogix DH-485 Communication Module User Manual, publication 1756-UM532                                          | Describes how to connect a 1756-DH485 module to a DH-485 network with multiple controllers.                                                    |
| ControlLogix Digital I/O Modules User Manual, publication 1756-UM058                                                  | Provides information about digital I/O module configuration properties.                                                                        |
| ControlLogix HART Analog I/O Modules User Manual, publication 1756-UM533                                              | Describes how to use HART analog I/O modules.                                                                                                  |
| ControlLogix High-speed Analog I/O Module User Manual, publication 1756-UM005                                         | Provides information about high-speed analog I/O module configuration properties.                                                              |
| ControlLogix High-speed Counter Module User Manual, publication 1756-UM007                                            | Provides information about high-speed counter-module configuration properties.                                                                 |
| ControlLogix Low-speed Counter Module User Manual, publication 1756-UM536                                             | Provides information about low-speed counter-module configuration properties.                                                                  |
| ControlLogix Peer I/O Control Application Technique, publication 1756-AT016                                           | Describes typical peer control applications and provides details about how to configure I/O modules for peer control operation.                |
| ControlLogix Programmable Limit Switch Module User Manual, publication 1756-UM002                                     | Provides information about programmable limit switch configuration properties.                                                                 |
| Redundancy Systems User Manual, publication 1756-UM015                                                                | Describes how to set up, configure, program, monitor, and troubleshoot Logix SIS, ControlLogix 5580, and ControlLogix 5570 redundancy systems. |
| ControlLogix Redundancy System User Manual, publication 1756-UM523                                                    | Provides information about ControlLogix standard redundancy systems.                                                                           |
| ControlLogix Remote I/O Communication Module User Manual, publication 1756-UM534                                      | Provides information for remote I/O network communication configuration.                                                                       |
| ControlLogix SIL 2 System Configuration Using RSLogix 5000 Subroutines Application Technique, publication 1756-AT010  | Provides information about ControlLogix SIL 2-certified fault-tolerant systems.                                                                |
| ControlLogix SIL 2 System Configuration Using SIL 2 Add-On Instructions Application Technique, publication 1756-AT012 | Provides information about ControlLogix SIL 2-certified fault-tolerant systems.                                                                |
| ControlLogix System Selection Guide, publication 1756-SG001                                                           | Describes how to design and select components for your ControlLogix system.                                                                    |
| ControlNet Network Configuration User Manual, publication CNET-UM001                                                  | Describes how to use ControlNet® modules.                                                                                                      |
| DeviceNet Network Configuration User Manual, publication DNET-UM004                                                   | Provides information about DeviceNet® modules and devices.                                                                                     |
| Ethernet Design Considerations Reference Manual, publication ENET-RM002                                               | Provides additional information about network design for your system.                                                                          |
| EtherNet/IP and ControlNet to FOUNDATION Fieldbus Linking Device User Manual, publication 1788-UM057                  | Describes in detail how to use the available Foundation Fieldbus devices.                                                                      |
| EtherNet/IP Network Configuration User Manual, publication ENET-UM001                                                 | Provides information about EtherNet/IP communication modules.                                                                                  |
| FOUNDATION Fieldbus Design Considerations Reference Manual, publication PROCES-RM005                                  | Describes in detail how to use the available Foundation Fieldbus devices.                                                                      |

|                                                                                                              | Resource Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Guidelines for Handling Lithium Batteries Technical Data, publication AG-5.4                                 | Describes how to store, handle, transport, and dispose of lithium batteries.                                    |
| Integrated Architecture and CIP Sync™ Configuration Application Technique, publication IA-AT003              | Describes how to configure CIP Sync™ with Integrated Architecture® products and applications.                   |
| Integrated Motion on the EtherNet/IP Network Configuration and Startup User Manual, publication MOTION-UM003 | Details how to design your ControlLogix system for Integrated Motion on the EtherNet/ IP network applications.  |
| Logix 5000 Controllers Add-On Instructions Programming Manual, publication 1756-PM010                        | Describes in detail how to use Add-On instructions.                                                             |
| Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003                         | Provides more information about GSV instructions, SSV instructions, objects, and attributes.                    |
| Logix 5000 Controllers I/O and Tag Data Programming Manual, publication 1756-PM004                           | Describes how to create and configure program tags for optimal task and program execution.                      |
| Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014               | Provides more information for I/O faults.                                                                       |
| Logix 5000 Controllers Messages Programming Manual, publication 1756-PM012                                   | Provides information for controller messages.                                                                   |
| Logix 5000 Controllers Motion Instructions Reference Manual, publication MOTION-RM002                        | Provides programmers with details about the motion instructions that are available for a Logix 5000 controller. |
| Logix 5000 Controllers Nonvolatile Memory Card Programming Manual, publication 1756-PM017                    | Provides information about changing the project that is available to load from nonvolatile memory,              |
| Logix 5000 Controllers Produced and Consumed Tags Programming Manual, publication 1756-PM011                 | Provides more information for produced and consumed tags.                                                       |
| Motion Coordinate System User Manual, publication MOTION-UM002                                               | Details how to create and configure a coordinated motion application system.                                    |
| PhaseManager™ User Manual, publication LOGIX-UM001                                                           | Provides more information about instructions for use with equipment phases.                                     |
| SERCOS and Analog Motion Configuration and Startup User Manual, publication MOTION-UM001                     | Details how to configure a sercos motion application system.                                                    |
| ControlLogix SIL 2 Applications Safety Reference Manual, publication 1756-RM001                              | Provides specific configuration and programming considerations.                                                 |
| Using Logix 5000 Controllers as Masters or Slaves on Modbus Application Solution, publication CIG-AP129      | Describes how to use Modbus sample programs.                                                                    |
| Industrial Automation Wiring and Grounding Guidelines Application Data, publication 1770-4.1                 | Provides general guidelines to install a Rockwell Automation industrial system.                                 |
| Product Certifications website, rok.auto/certifications                                                      | Provides declarations of conformity, certificates, and other certification details.                             |

You can view or download publications at https://www.rockwellautomation.com/global/literature-library/ overview.page To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

<!-- image -->

## Install a ControlLogix 5570 Controller

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

## Environment and Enclosure

<!-- image -->

## ATTENTION:

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is not intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to help prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to help prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for the application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for additional installation requirements
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosure

<!-- image -->

## North American Hazardous Location Approval

<!-- image -->

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | WARNING: EXPLOSION HAZARD • Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. • Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. • Substitution of components may impair suitability for Class I, Division 2. • If this product contains batteries, they must only be changed in an area known to be nonhazardous.   | WARNING: RISQUE D’EXPLOSION • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. • La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2. • S'assurer que l'environnement est classé non dangereux avant de changer les piles.                                                |

## European Hazardous Location Approval

The following applies when the product bears the Ex Marking.

This equipment is intended for use in potentially explosive atmospheres as defined by European Union Directive 94/9/EC and has been found to comply with the Essential Health and Safety Requirements relating to the design and construction of Category 3 equipment intended for use in Zone 2 potentially explosive atmospheres, given in Annex II to this Directive.

Compliance with the Essential Health and Safety Requirements has been assured by compliance with EN 60079-15 and EN 60079-0.

<!-- image -->

ATTENTION: This equipment is not resistant to sunlight or other sources of UV radiation.

<!-- image -->

## WARNING:

- This equipment shall be mounted in an ATEX certified enclosure with a minimum ingress protection rating of at least IP54 (as defined in IEC60529) and used in an environment of not more than Pollution Degree 2 (as defined in IEC 60664-1) when applied in Zone 2 environments. The enclosure must utilize a tool removable cover or door.
- This equipment shall be used within its specified ratings defined by Rockwell Automation.
- This equipment must be used only with ATEX certified Rockwell Automation backplanes.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.

<!-- image -->

## Before You Begin

## ControlLogix 5570 Controller Parts

To install a ControlLogix® chassis and power supply before you install your controller and power supply, see the following publications:

- ControlLogix Chassis Installation Instructions, publication 1756-IN621
- ControlLogix Power Supply Installation Instructions, publication 1756-IN619
- ControlLogix Redundant Power Supply Installation Instructions, publication 1756-IN620

These sections describe parts that are included with ControlLogix 5570 controllers and available accessory parts.

## Parts Included with ControlLogix 5570 Controllers

These parts are included with the controller:

- 1756-ESMCAP capacitor-based energy storage module (ESM)
- 1784-SD1 Secure Digital (SD) card, 1 GB
- 1747-KY controller key

Figure 1 - Parts with the ControlLogix 5570 Controller

<!-- image -->

IMPORTANT

The controllers ship with an SD card installed. We recommend that you leave the SD card installed.

## Controller Installation

.

## Parts Available for Use with ControlLogix 5570 Controllers

You can choose to use the parts included with the controller and these parts specific to your application.

| If your application requires                               | Then use this part                 |
|------------------------------------------------------------|------------------------------------|
| USB connection from a computer to the controller USB cable | (1)                                |
| Nonvolatile memory                                         | 1784-SD1 (1 GB) or 1784-SD2 (2 GB) |
| ESM without WallClockTime back-up power 1756-ESMNSE        | This ESM does not have WallClockTime back-up power. Use this ESM if your application requires that the ESM ESM depletes its residual stored energy to 40 µJ or less (2 before transporting it into or out of your application. (2) Additionally, you can use this ESM with only a 1756-L73 (8 MB) or smaller memory-sized controller.                                    |
| ESM that secures the controller by blocking the USB (2) connection and SD card use(2) This ESM provides your application an enhanced degree of security.                                                            | 1756-ESMNRM                        |

<!-- image -->

WARNING: Do not use the USB port in hazardous locations.

<!-- image -->

## ATTENTION:

- The USB port is intended only for temporary local programming purposes and not intended for permanent connection.
- The USB cable is not to exceed 3.0 m (9.84 ft) and must not contain hubs.

To install the controller, complete the tasks summarized in this table.

|    | Task                                   |   Page |
|-----|----------------------------------------|--------|
|     | Insert the Controller into the Chassis |     19 |
|     | Insert the Key                         |     20 |
|     | Install the SD Card                    |     21 |
|     | Remove the SD Card                     |     23 |
|     | Install the ESM                        |     24 |

## Insert the Controller into the Chassis

When installing a ControlLogix controller, you can do the following:

- Place the controller in any slot.
- Use multiple controllers in the same chassis.

You can install or remove a ControlLogix controller while chassis power is on and the system is operating.

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the controller and its mating connector on the chassis. Worn contacts may create electrical resistance that can affect controller operation.

## Table 4 - Prevent Electrostatic Discharge

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

IMPORTANT The ESM begins charging when one of these actions occurs:

- The controller and ESM are installed into a powered chassis.
- Power is applied to the chassis that contains a controller with the ESM installed.
- An ESM is installed into a powered controller.

After power is applied, the ESM charges for up to two minutes as indicated by CHRG or ESM Charging on the status display.

## Insert the Key

1. Align the circuit board with the top and bottom guides in the chassis.
2. Slide the module into the chassis until it snaps into place.
3. Verify that the controller is flush with the power supply or other installed modules.

<!-- image -->

After you have inserted the controller into the chassis, reference the Troubleshoot the Module on page 171 for information to interpret the status indicators.

After the controller is installed, insert the key.

<!-- image -->

## Install the SD Card

Complete these steps to install the SD card in the controller.

We recommend that you leave the SD card in the controller, even when it is not used. If the controller experiences a major nonrecoverable fault, fault information is saved to the card.

<!-- image -->

WARNING: When you insert or remove the Secure Digital (SD) memory card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

1. Verify that the SD card is locked or unlocked according to your preference.

<!-- image -->

For more information about the lock/unlock memory settings, see the Load or Store to the Memory Card on page 66 .

2. Open the door for the SD card.
3. Insert the SD card into the SD card slot.

<!-- image -->

4. Gently press the card until it clicks into place.
5. Close the SD card door.

<!-- image -->

<!-- image -->

## Remove the SD Card

The controller ships with an SD card installed. Complete these steps to remove the SD card from the controller.

<!-- image -->

WARNING: When you insert or remove the Secure Digital (SD) memory card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

## IMPORTANT

- Verify that the SD card status indicator is off and that the card is not in use before removing it.
- We recommend that you do the following:
- – Leave an SD card installed.
- – Use the SD cards available from Rockwell Automation (catalog number 1784-SD1 or 1784-SD2).
- While other SD cards can be used with the controller, Rockwell Automation has not tested the use of those cards with the controller. If you use an SD card other than those cards that are available from Rockwell Automation, you can experience data corruption or loss.
- Also, SD cards that are not provided by Rockwell Automation do not have the same industrial, environmental, and certification ratings as those cards that are available from Rockwell Automation.
1. Verify that the SD card is not in use by checking to be sure that the SD indicator is Off.
- TIP You can also put the controller into Hard Run mode to keep the controller from writing to the SD card while it is removed.
2. Open the door to access the SD card.

<!-- image -->

## Install the ESM

3. Press and release the SD card to eject it.
4. Remove the SD card and close the door.

<!-- image -->

To install an ESM in the controller, complete these steps.

<!-- image -->

ATTENTION: To avoid potential damage to the product when inserting the ESM, align it in the track and slide forward with minimal force until the ESM snaps into place.

1. Align the tongue-and-groove slots of the ESM and controller.
2. Slide the ESM back until it snaps into place.

<!-- image -->

The ESM begins charging after installation. The following status messages indicate charging status:

- ESM Charging
- CHRG

## Uninstall the ESM

.

After you install the ESM, it can take up to 15 seconds for the charging status messages to display.

## IMPORTANT

Allow the ESM to finish charging before removing power from the controller. Failure to do so can result in the loss of the application program. A type 1, code 40 major fault is logged on powerup.

To verify that the ESM is fully charged, check the status display to confirm that messages CHRG or ESM charging are no longer indicated.

TIP We recommend that you check the WallClockTime object attributes after installing an ESM to verify that the time of the controller is correct.

The ESM contains a real-time clock. If the ESM is new or came from another controller, the WallClockTime object attributes for your controller can change.

WARNING: If your application requires the ESM to deplete its residual stored energy to 40 µJ or less before you transport it into or out of the application, use only the 1756-(SP)ESMNSE(XT) module. In this case, complete these steps before you remove the ESM.

- Turn power off to the chassis.

After you turn power off to the chassis, the controller's OK status indicator transitions from green to steady red to OFF.

- Wait at least 20 minutes for the residual stored energy to decrease to 40 µJ or less before you remove the ESM.

There is no visual indication of when the 20 minutes has expired. You must track that time period .

WARNING: When you insert or remove the energy storage module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

<!-- image -->

<!-- image -->

Be sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector.

## IMPORTANT

Before you remove an ESM, make the necessary adjustments to your program to account for potential changes to the WallClockTime attribute.

Consider these points before removing the ESM:

- The following ESM modules can be currently installed in your 1756-L7x or 1756-L7xXT controller:
- – 1756-ESMCAP
- – 1756-ESMNSE
- – 1756-ESMCAPXT
- – 1756-ESMNSEXT
- The 1756-L7x controllers come with the 1756-ESMCAP module installed. The 1756-L7xXT extreme temperature controller ships with a 1756-ESMCAPXT module installed. For more information on how to use a 1756-ESMNSE, 1756-ESMNRM, 1756-ESMNSEXT, or 1756-ESMNRMXT module, see page 24 .
- After the 1756-L7x or 1756-L7xXT controllers lose power, because the chassis power is turned off or the controller has been removed from a powered chassis, do not immediately remove the ESM.

Wait until the OK status indicator on the controller transitions from green to steady red to OFF before you remove the ESM.

- You can use the 1756-ESMNSE module with only a 1756-L73 (8 MB) or smaller memory-sized controller.
- Use the 1756-ESMNSE module if your application requires that the ESM depletes its residual stored energy to 40 μJ or less before transporting it into or out of your application.
- Once it is installed, you cannot remove the 1756-ESMNRM or 1756-ESMNRMXT module from a 1756-L7x or 1756-L7xXT controller.
- The Armor™ controller energy storage modules (ESM) cannot be removed or replaced.

Complete these steps to remove an ESM module from the controller.

1. Remove the key from the mode switch.

## IMPORTANT

The next step depends on which of the following conditions applies to your application.

- If you are removing the ESM from a powered 1756-L7x controller, go to step 2 .
- If you are removing the ESM from a 1756-L7x controller that is not powered, because the chassis power is turned off or the controller has been removed from a powered chassis, do not immediately remove the ESM.

Wait until the OK status indicator on the controller transitions from green to steady red to OFF before you remove the ESM.

After the OK status indicator transitions to Off, go to step 2 .

2. Use your thumb to press down on the black release and pull the ESM away from the controller.

<!-- image -->

<!-- image -->

## Notes:

<!-- image -->

## Install a ControlLogix 5560 Controller

ATTENTION: This equipment is not resistant to sunlight or other sources of UV radiation.

## Environment and Enclosure

<!-- image -->

## ATTENTION:

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is not intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to help prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to help prevent or minimize the spread of flame, complying with a flame spread rating of 5VA or be approved for the application if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for additional installation requirements
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosure

<!-- image -->

## North American Hazardous Location Approval

<!-- image -->

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | WARNING: EXPLOSION HAZARD • Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. • Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. • Substitution of components may impair suitability for Class I, Division 2. • If this product contains batteries, they must only be changed in an area known to be nonhazardous.   | WARNING: RISQUE D’EXPLOSION • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. • Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. • La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2. • S'assurer que l'environnement est classé non dangereux avant de changer les piles.                                                |

## European Hazardous Location Approval

The following applies when the product bears the Ex Marking.

This equipment is intended for use in potentially explosive atmospheres as defined by European Union Directive 94/9/EC and has been found to comply with the Essential Health and Safety Requirements relating to the design and construction of Category 3 equipment intended for use in Zone 2 potentially explosive atmospheres, given in Annex II to this Directive.

Compliance with the Essential Health and Safety Requirements has been assured by compliance with EN 60079-15 and EN 60079-0.

<!-- image -->

ATTENTION: This equipment is not resistant to sunlight or other sources of UV radiation.

<!-- image -->

## WARNING:

- This equipment shall be mounted in an ATEX certified enclosure with a minimum ingress protection rating of at least IP54 (as defined in IEC60529) and used in an environment of not more than Pollution Degree 2 (as defined in IEC 60664-1) when applied in Zone 2 environments. The enclosure must utilize a tool removable cover or door.
- This equipment shall be used within its specified ratings defined by Rockwell Automation.
- This equipment must be used only with ATEX certified Rockwell Automation backplanes.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.

<!-- image -->

## Before You Begin

## ControlLogix 5560 Controller Parts

To install a ControlLogix® chassis and power supply before you install your controller and power supply, see the following publications:

- ControlLogix Chassis Installation Instructions, publication 1756-IN621
- ControlLogix Power Supply Installation Instructions, publication 1756-IN619
- ControlLogix Redundant Power Supply Installation Instructions, publication 1756-IN620

These sections describe parts that are included with ControlLogix 5560 controllers and available accessory parts:

- One of the following batteries is included with your controller:
- – For series A controllers, catalog number 1756-BA1
- – For series B controllers, catalog number 1756-BA2
- Key, catalog number 1747-KY

Figure 2 - Parts Included with ControlLogix 5560 Controllers

<!-- image -->

## Parts Not Included with the Controller

You can choose to use the parts included with the controller and these parts specific to your application.

| If your application requires                                                 | Then use this component      |
|------------------------------------------------------------------------------|------------------------------|
| RS-232 connection to the controller                                          | 1756-CP3 serial cable        |
| Nonvolatile memory                                                           | 1784-CF128 CompactFlash card |
| Expanded battery life for extended memory retention 1756-BATM battery module | (1)                          |

## Controller Installation

## CompactFlash Card Installation and Removal

To install the controller, complete the tasks summarized in this table.

|    | Task                                       |   Page |
|-----|--------------------------------------------|--------|
|     | CompactFlash Card Installation and Removal |     32 |
|     | Battery Connection and Replacement         |     36 |
|     | Insert the Controller into the Chassis     |     38 |
|     | Remove the Controller from the Chassis     |     40 |

The installation and removal of a CompactFlash card depends on the controller.

<!-- image -->

WARNING: When you insert or remove the CompactFlash card while power is on, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

- If you are using a series A controller, reference these sections:
- – Install a CompactFlash Card in a Series A Controller on page 33 .
- – Remove a CompactFlash Card from a Series A Controller on page 33 .
- If you are using a series B controller, reference these sections:
- – Install a CompactFlash Card in a Series B Controller on page 34 .
- – Remove a CompactFlash Card from a Series B Controller on page 35 .

## Install a CompactFlash Card in a Series A Controller

Complete these steps to install a CompactFlash card in a series A controller.

.

<!-- image -->

1. Lay the controller on its side with the front facing to the left.
2. Raise the locking clip.
3. Insert the CompactFlash card into the slot at the bottom of the controller.
4. Pull the clip forward and downward until it snaps into place over the card.

## Remove a CompactFlash Card from a Series A Controller

Complete these steps to remove a CompactFlash card from a series A controller.

<!-- image -->

1. Lay the controller in its side with the mode switch facing left.
2. Raise the locking clip.
3. Gently pull the card out of the slot.

## Install a CompactFlash Card in a Series B Controller

Complete these steps to install a CompactFlash card in a series B controller.

<!-- image -->

1. Open the door of the controller and push the CompactFlash latch to the left.
2. Insert the CompactFlash card with the Allen-Bradley® logo pointing left.
3. Release the latch and secure it over the CompactFlash card.

## Remove a CompactFlash Card from a Series B Controller

Complete these steps to remove a CompactFlash card from a series B controller.

<!-- image -->

1. Verify that the OK indicator is steady green and open the door of the controller.
2. Push and hold the CompactFlash latch to the left.
3. Push the eject button and remove the card.
4. Release the latch.

## Battery Connection and Replacement

<!-- image -->

<!-- image -->

This product contains a hermetically sealed lithium battery that may need to be replaced during the life of the product.

At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste.

The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are recovered.

WARNING: When you connect or disconnect the battery an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

For safety information on the handling of lithium batteries, including handling and disposal of leaking batteries, see Guidelines for Handling Lithium Batteries, publication AG-5.4 .

## IMPORTANT

To help prevent program loss, replace a 1756-BA1 or 1756-BA2 battery according to the following schedule even if the BAT status indicator is Off.

| If the temperature 2.54 cm (1 in.) below the chassis is   | Replace the battery within   |
|-----------------------------------------------------------|------------------------------|
| -25…+35 °C (-13…+95                                      | F) No replacement required   |
| 36…40 °C (96.8…104   F)                                  | 3 years                      |
| 41…45 °C (105.8…113   F)                                 | 2 years                      |
| 46…50 °C (114.8…122   F)                                 | 16 months                    |
| 51…55 °C (123.8…131   F)                                 | 11 months                    |
| 56…70 °C (132.8…158  F)                                  | 8 months                     |

ATTENTION: Store batteries in a cool, dry environment. We recommend 25 C (77  F) with 40…60% relative humidity. You can store batteries for up to 30 days between -45…+85  C (-49…+185  F), such as during transportation. To avoid leakage or other hazards, do not store batteries above 60C (140  F) for more than 30 days.

<!-- image -->

Connection of the battery varies depending on your controller series:

- If you are using a series A controller, see page 37 .
- If you are using a series B controller, see page 38 .

## Install the Battery on a Series A Controller

Complete these steps to install a 1756-BA1 battery on a series A controller.

For information to install a 1756-BATM battery module or replace a 1756-BATM assembly, see the ControlLogix Battery Module Installation Instructions, publication 1756-IN576 .

<!-- image -->

ATTENTION: For a series A controller, connect only a 1756-BA1 battery or a 1756-BATM battery module. The use of other batteries can damage the controller.

<!-- image -->

| Wire Terminal Location Connected Wire   |
|-----------------------------------------|
| Top No connection                       |
| Middle Black lead (-)                   |
| Bottom Red lead (+)                     |

1. Connect the battery connector to the port to the right of the battery slot.
2. Snap the battery into the battery slot.
3. Write the date on the battery label.
4. Attach the label to the inside of the controller door.

## Insert the Controller into the Chassis

## Install the Battery on a Series B Controller

Complete these steps to install the battery on a series B controller.

<!-- image -->

ATTENTION: For a series B controller, connect only a 1756-BA2 battery. The use of other batteries can damage the controller.

<!-- image -->

1. Plug the battery connector into the battery port (+ Red, - Black).
2. Insert the battery, with the arrow pointing up, into the battery slot.
3. Write the date on the battery label.
4. Attach the label to the inside of the controller door.

When installing a ControlLogix controller, you can do the following:

- Place the controller in any slot.
- Use multiple controllers in the same chassis.

You can install a ControlLogix controller while chassis power is on and the system is operating.

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Repeated electrical arcing causes excessive wear to contacts on both the controller and its mating connector on the chassis. Worn contacts may create electrical resistance that can affect controller operation.

## Table 5 - Prevent Electrostatic Discharge

<!-- image -->

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

ATTENTION: If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment can be impaired.

Complete these steps to insert the controller into the chassis.

1. Insert the key into the controller.
2. Turn the key to the PROG position.
3. Align the circuit board with the top and bottom guides in the chassis.
4. Slide the module into the chassis.
5. Verify that the controller is flush with the power supply or other installed modules.
6. Verify that the top and bottom latches are engaged.

<!-- image -->

After you have inserted the controller into the chassis, review the state of the controller information in Troubleshoot the Module on page 171 .

## Remove the Controller from the Chassis

You can remove a controller while chassis power is on and the system is operating. The devices that are owned by the controller go to their configured fault state if you remove the controller.

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electric arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Repeated electrical arcing causes excessive wear to contacts on both the controller and its mating connector in the chassis. Worn contacts may create electrical resistance that can affect controller operation.

Complete these steps to remove the controller from the chassis.

1. Press the locking tabs on the top and bottom of the controller.
2. Slide the controller out of the chassis.

<!-- image -->

## Make Connections

## Start Using the Controller

Before you can begin using your controller, you must make a connection to the controller.

## ControlLogix 5570 Connection Options

Connection options with the ControlLogix® 5570 controller include the following:

- Connect by using a USB cable as described in Connect to a ControlLogix 5570 Controller on page 42 .
- Install and configure a communication module in the chassis with the controller as described in the installation instructions for the communication module.

For information on Double Data Rate (DDR) backplane communication usage, see Double Data Rate (DDR) Backplane Communication on page 90 .

## ControlLogix 5560 Connection Options

Connection options with the ControlLogix 5560 controller include the following:

- Connect by using a serial cable as described in Connect to a ControlLogix 5560 Controller on page 45 .
- Install and configure a communication module in the chassis with the controller as described in the installation instructions for the communication module.

TIP When upgrading your 1756-L6x controller firmware, we recommend that you use a network connection other than the serial cable. Serial connections are slower than other communication connections.

<!-- image -->

## Connect to a ControlLogix 5570 Controller

The controller has a USB port that uses a Type B receptacle. The port is USB 2.0 compatible and runs at 12 Mbps.

To use the USB port of the controller, you must have RSLinx ® ® software, version 2.56 or later, installed on your workstation. Use a USB cable to connect your workstation to the USB port. With this connection, you can update firmware and download programs to the controller directly from your workstation.

<!-- image -->

ATTENTION: The USB port is intended only for temporary local programming purposes and not intended for permanent connection. The USB cable is not to exceed 3.0 m (9.84 ft) and must not contain hubs.

<!-- image -->

WARNING: Do not use the USB port in hazardous locations.

Figure 3 - USB Connection

<!-- image -->

## Configure the USB Driver

To configure RSLinx software to use a USB port, first configure a USB driver.

To configure a USB driver, perform this procedure.

1. Connect your controller and workstation by using a USB cable.

The Found New Hardware Wizard dialog box appears.

<!-- image -->

2. Click any of the Windows® Update connection options and click Next.
2. TIP If the software for the USB driver is not found and the installation is canceled, verify that you have installed RSLinx Classic software, version 2.57 or later.
3. Click Install the software automatically (Recommended) and click Next. The software is installed.

<!-- image -->

4. Click Finish to configure your USB driver.
5. From the Communications dropdown menu, choose RSWho.

<!-- image -->

The USB port driver appears.

<!-- image -->

Your controller appears under two drivers, a virtual chassis and the USB port. You can use either driver to browse to your controller.

## Connect to a ControlLogix 5560 Controller

The ControlLogix® 5560 controller uses a serial port for workstation connections.

<!-- image -->

WARNING: If you connect or disconnect the serial cable with power applied to this module or the serial device on the other end of the cable, an electric arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

To connect a workstation to the serial port, you can make your own serial cable or use one of these cables:

- 1756-CP3 serial cable
- 1747-CP3 cable from the SLC™ product family (if you use this cable, it can be difficult to close the controller door)

<!-- image -->

Follow these guidelines if you make your own serial cable:

- Limit the length to 15.2 m (50 ft).
- Wire the connectors as shown.
- Attach the shield to the connectors.

<!-- image -->

Plug the controller end of the serial cable into the RS-232 port on the front of the controller.

<!-- image -->

## Configure the Serial Driver

Use RSLinx software to configure the RS-232 DF1 device driver for serial communication.

To configure the driver, perform this procedure.

1. In RSLinx software, from the Communications menu, choose Configure Drivers.

<!-- image -->

2. From the Available Driver Types dropdown menu, choose the RS-232 DF1 device driver.
3. Click Add New.

<!-- image -->

The Add New RSLinx Driver dialog box appears.

<!-- image -->

4. Type the driver name and click OK.

5. Specify the serial port settings.
- a. From the Comm Port dropdown menu, choose the serial port on the workstation to which the cable is connected.
- b. From the Device dropdown menu, choose Logix 5550/ CompactLogix.
- c. Click Auto-Configure.
6. If the auto configuration is successful, click OK.

<!-- image -->

If the auto configuration is not successful, verify that the correct Comm Port was selected.

7. Click Close.

Upgrade Controller Firmware You can choose to upgrade the controller firmware by using one of these tools:

- ControlFLASH™ software that is packaged with the Studio 5000® environment
- AutoFlash feature of the Logix Designer application

To upgrade your controller firmware, complete the tasks that are listed in this table.

|    | Task                                         |   Page |
|-----|----------------------------------------------|--------|
|     | Determine Required Controller Firmware       |     49 |
|     | Obtain Controller Firmware                   |     50 |
|     | Use ControlFLASH Software to Update Firmware |     50 |
|     | Use AutoFlash to Update Firmware             |     55 |

## Determine Required Controller Firmware

## IMPORTANT

The controller must be in Remote Program or Program mode and all major recoverable faults must be cleared to accept upgrades.

Use Table 6 to determine what firmware revision is required for your controller.

Table 6 - Firmware Required for Controllers

| Controller   | Series   | Use this firmware revision                                                                      |
|--------------|----------|-------------------------------------------------------------------------------------------------|
| 1756-L61     | A        | 12.x or later                                                                                   |
| 1756-L61     | B        | 13.40 or later                                                                                  |
| 1756-L62     | A        | 12.x or later                                                                                   |
| 1756-L62     | B        | 13.40 or later                                                                                  |
| 1756-L63     | A        | • If not using a CompactFlash card, 10.x or later • If using a CompactFlash card, 11.x or later |
| 1756-L63     | B        | 13.40 or later                                                                                  |
| 1756-L63XT   | B        | 13.40 or later                                                                                  |
| 1756-L64     | B        | 16 or later                                                                                     |
| 1756-L65     | B        | 17 or later                                                                                     |
| 1756-L71     | A        | 20 or later                                                                                     |
| 1756-L72     | A        | 19 or later                                                                                     |
| 1756-L72EROM | A        | 19 or later                                                                                     |
| 1756-L73     | A        | 19 or later                                                                                     |
| 1756-L73XT   | A        | 19 or later                                                                                     |
| 1756-L73EROM | A        | 19 or later                                                                                     |
| 1756-L74     | A        | 19 or later                                                                                     |
| 1756-L75     | A        | 19 or later                                                                                     |

1756-L7x Controllers

<!-- image -->

## Obtain Controller Firmware

Controller firmware is packaged with the Studio 5000 environment. In addition, controller firmware is also available for download from the Rockwell Automation Technical Support website at https:// www.rockwellautomation.com/support/.

## Use ControlFLASH Software to Update Firmware

To upgrade your controller firmware with ControlFLASH software, complete these steps.

## IMPORTANT

If the SD card is locked and the Load Image option of the store project is set to On Power Up, the controller firmware is not updated as a result of these steps. The previously stored firmware and project are loaded instead.

1. Verify that the network connection is made and the network driver has been configured in RSLinx software.
2. Start ControlFLASH software and click Next to begin the upgrade process.
3. Select the catalog number of your controller and click Next.

<!-- image -->

1756-L6x Controllers

<!-- image -->

4. Expand the network driver to locate your controller.

1756-L7x Controller with USB Network Driver

<!-- image -->

<!-- image -->

5. Select the controller and click Next.

6. Select the desired firmware revision and click Next.

1756-L7x Controller Upgrade

<!-- image -->

## 1756-L6x Controller Upgrade

<!-- image -->

- TIP If you are using a 1756-L7x controller and experience a Script File Error after selecting the firmware revision number (see the following example), there is likely an anomaly with your firmware files.

<!-- image -->

To recover, perform the following:

- Go to https://www.rockwellautomation.com/support/ and download the firmware revision you are trying to upgrade. Replace the firmware revision that you have previously installed with that posted on the Technical Support website.
- If the replacement firmware revision does not resolve the anomaly, contact Rockwell Automation Technical Support.
7. Click Finish.

<!-- image -->

8. When a confirmation dialog box appears, click Yes.

<!-- image -->

Before the firmware update begins, this dialog box appears. Take the required action for your application. In this example, the upgrade continues when you click OK.

<!-- image -->

A progress dialog box indicates the progress of the firmware update. The 1756-L7x controllers show progress in updates and blocks. The 1756L6x controllers show progress only in blocks.

<!-- image -->

WARNING: Let the firmware update fully complete before cycling power or otherwise interrupting the upgrade.

TIP If the ControlFLASH upgrade of the controller is interrupted, the controllers revert to boot firmware that is firmware revision 1.xxx .

When the upgrade is complete, the Update Status dialog box indicates that the upgrade is complete.

9. Click OK.
10. Close ControlFLASH software.

<!-- image -->

## Use AutoFlash to Update Firmware

To upgrade your controller firmware with the AutoFlash feature, complete these steps.

## IMPORTANT

If the SD card is locked and the Load Image option of the stored project is set to On Power Up, the controller firmware is not updated as a result of these steps. The previously stored firmware and project are loaded instead.

1. Verify the following:
- The network connection is made.
- The network driver has been configured in RSLinx Classic software.
- The controller is in Remote Program or Program mode and all major recoverable faults are cleared.
2. Use the Logix Designer application to create a controller project.
3. On the Path bar, click Who Active.

<!-- image -->

4. Select your controller and click Update Firmware.

1756-L7x Controller with USB Driver

<!-- image -->

1756-L6x Controller with Ethernet Driver

<!-- image -->

5. Select the firmware revision to upgrade to and click Update.
6. On the Update Firmware dialog box, click Yes.
7. On the ControlFLASH dialog box, click OK.

<!-- image -->

<!-- image -->

<!-- image -->

A progress dialog box indicates the progress of the firmware update. The 1756-L7x controllers show progress in updates and blocks. The 1756L6x controllers show progress only in blocks.

## Set the Communication Path

<!-- image -->

WARNING: Let the firmware update fully complete before cycling power or otherwise interrupting the upgrade.

- TIP If the upgrade of the controller is interrupted, the controllers revert to firmware revision 1.xxx .

When the upgrade is complete, the Update Status dialog box indicates that the upgrade is complete.

To go online with the controller, you must specify a communication path in the Logix Designer application. You specify the communication path after you create a controller program.

Complete these steps to specify the communication path after you have created your program.

1. Click Who Active.
2. Expand the communication path and select the controller.
3. Click Set Project Path.

<!-- image -->

<!-- image -->

## Go Online with the Controller Use one of these methods to go online with the controller:

- After setting the communication path, click Go Online in the Who Active dialog box.
- From the Controller Status menu, choose Go Online.

<!-- image -->

<!-- image -->

When you download a project to the controller, it moves the project from the Logix Designer application onto the controller. You can download a project in two ways:

- Use the Who Active Dialog Box to Download on page 60
- Use the Controller Status Menu to Download on page 61

## Download to the Controller

## Use the Who Active Dialog Box to Download

You can use the features of the Who Active dialog box to download to your controller after you have set the communication path. Complete these steps to download to the controller.

1. After setting the communication path, click Download in the Who Active dialog box.
2. Read the warnings on the Download dialog box and click Download.

<!-- image -->

<!-- image -->

## Upload from the Controller

## Use the Controller Status Menu to Download

After you set a communication path in the Logix Designer application, you can use the Controller Status menu to download to the controller. To download, from the Controller Status menu, choose Download.

Figure 4 - Download Via the Controller Status Menu

<!-- image -->

TIP After the download completes on a 1756-L7x controller, the project name is indicated on the scrolling status display.

When you upload a project to the controller, it copies the project from the controller to the Logix Designer application. To upload a project, use one of these methods:

- Use the Who Active Dialog Box to Upload , page 61
- Use the Controller Status Menu to Upload , page 62

## Use the Who Active Dialog Box to Upload

You can use the features of the Who Active dialog box to upload from your controller after you have set the communication path. Complete these steps to upload from the controller.

1. After setting the communication path, click Upload in the Who Active dialog box.

<!-- image -->

2. Click Upload after verifying the project that you are uploading in the Connected to Upload dialog box.

<!-- image -->

## Use the Controller Status Menu to Upload

After you have set a communication path in the project, you can use the Controller Status menu to upload from the controller. To upload, from the Controller Status menu, choose Upload.

Figure 5 - Upload Via the Controller Status Menu

<!-- image -->

## Choose the Controller Operation Mode

Use Table 7 as a reference when determining your controller Operation mode.

Table 7 - Controller Operation Modes and Meanings

| If you want to                                                         | Select one of these modes   | Select one of these modes   | Select one of these modes   | Select one of these modes   | Select one of these modes   |
|------------------------------------------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
|                                                                        | Run Remote                  | Program                     |                             |                             |                             |
| Turn outputs to the state commanded by the logic of the project        | X X                         | Program                     |                             |                             |                             |
| Turn outputs to their configured state for Program mode                |                             | XX X                        |                             |                             |                             |
| Execute (scan) tasks                                                   | X X X                       |                             |                             |                             |                             |
| Change the mode of the controller via the Logix Designer application   |                             | X XX                        |                             |                             |                             |
| Download a project                                                     |                             | X X X X                     |                             |                             |                             |
| Schedule a ControlNet® network                                         |                             | X X                         |                             |                             |                             |
| While online, edit the project                                         |                             | X X X X                     |                             |                             |                             |
| Send messages                                                          | X X X                       |                             |                             |                             |                             |
| Send and receive data in response to a message from another controller |                             | X X XX X                    |                             |                             |                             |
| Produce and consume tags                                               |                             | X X X X X                   |                             |                             |                             |

## Use the Mode Switch to Change the Operation Mode

Use the mode switch to change the operation mode. The controller mode switch provides a mechanical means to enhance controller and control system security. You must physically move the mode switch on the controller to change its operating mode from RUN, to REM, or to PROG. When the mode switch on the controller is set to RUN mode, features like online editing, program downloads, and firmware updates are prohibited. See Table 7 for a complete list of prohibited features.

The physical mode switch can complement other authorization and authentication methods that similarly control user-access to the controller, such as the following:

- Logix CPU Security tool
- FactoryTalk® Security service

## IMPORTANT

During runtime, we recommend that you place the controller mode switch in RUN mode and remove the key (if applicable) from the switch. This can help discourage unauthorized access to the controller or potential tampering with the program of the controller, configuration, or device firmware. Place the mode switch in REM or PROG mode during controller commissioning and maintenance and whenever temporary access is necessary to change the program, configuration, or firmware of the product.

The mode switch on the front of the controller can be used to change the controller to one of these modes:

- Run (RUN)
- Remote (REM)
- Program (PROG)

1756-L7x

1756-L6x

<!-- image -->

<!-- image -->

| Mode Switch Position   | Available Controller Modes                                                                                                                                                                                                                                                                                                          | ATTENTION:                                                                                                                                                                            |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUN                    | Run mode—The controller is actively controlling the process/machine. Projects cannot be edited in the Logix Designer application when in Run mode.                                                                                                                                                                                  | Run mode is used only when all conditions are safe.                                                                                                                                   |
| REM                    | Remote Run mode—This mode is identical to Run mode except you can edit the project online.                                                                                                                                                                                                                                          | You are able to modify a project file online in Remote Run mode. Be sure to control outputs with care to avoid injury to personnel and damage to equipment.                           |
| REM                    | Remote Program mode—This mode is identical to Program mode.                                                                                                                                                                                                                                                                         | You are able to modify a project file online in Remote Run mode. Be sure to control outputs with care to avoid injury to personnel and damage to equipment.                           |
| REM                    | Remote Test mode—The controller mode during which code is executing. I/O is not controlled, and limited editing operations are available. Output modules are commanded to their Program mode state (on, off, or hold).                                                                                                              | Outputs are commanded to their Program mode state, which can cause a dangerous situation.                                                                                             |
| REM                    | Note: The mode of the controller can be changed from within the Logix Designer application.                                                                                                                                                                                                                                         | Outputs are commanded to their Program mode state, which can cause a dangerous situation.                                                                                             |
| PROG                   | Program mode—The controller mode during which programming language is not executing. I/O is not controlled, and limited editing operations are available. Output modules are commanded to their Program mode state (On, Off, or Hold). In this position, controller modes cannot be changed through the Logix Designer application. | Do not use Program mode as an emergency stop (E-stop). Program mode is not a safety device. Outputs are commanded to their Program mode state, which can cause a dangerous situation. |

## Use the Logix Designer Application to Change the Operation Mode

Dependent on the mode of the controller you specify by using the mode switch, you can change the Operation mode of the controller in the Logix Designer application.

After you are online with the controller and the controller mode switch is set to Remote (REM or the center position), you can use the Controller Status menu in the upper-left corner of the application window to specify these operation modes:

- Remote Program
- Remote Run
- Remote Test

Figure 6 - Operation Mode

TIP For this example, the controller mode switch is set to Remote mode. If your controller mode switch is set to Run or Program modes, the menu options change.

<!-- image -->

## Load or Store to the Memory Card

The memory card that is compatible with your ControlLogix controller is used to load or store the contents of user memory for the controller.

## Store to the Memory Card

After you are online with the controller and have changed the controller to Program or Remote Program mode, complete these steps to store a project to the memory card.

1. Open the Controller Properties dialog box and click the Nonvolatile Memory tab.
2. Click Load/Store.

<!-- image -->

TIP If Load/Store is dimmed (unavailable), verify the following:

- You have specified the correct communication path and are online with the controller in Program mode.
- The memory card is installed.
- With the 1756-L7x controllers, if the SD card is locked, Store is dimmed (unavailable) and the locked status is indicated in the bottom-left corner of the Nonvolatile memory/Load Store dialog box. See step 4 .

If the memory card is not installed, a message in the lower-left corner of the Nonvolatile Memory tab indicates the missing card as shown here.

<!-- image -->

3. Change the Load Image, Load Mode, and Automatic Firmware Update properties according to your application requirements.

The following table describes the Load Image options that you can choose for the project.

## IMPORTANT

If the SD card is locked and the Load Image option of the project is set to On Power Up, the controller firmware is not updated as a result of a firmware update. The previously stored firmware and project are loaded instead.

| If you want the image (project) to load when                             | Then choose       |
|--------------------------------------------------------------------------|-------------------|
| Power to the controller is applied or cycled                             | On Power Up       |
| The controller has lost the project and power has been cycled or applied | On Corrupt Memory |
| Initiated via the Logix Designer application                             | User Initiated    |

The following table describes the Load Mode options that you can choose for the project.

| If you want the controller to go to this mode after loading   | Then choose           |
|---------------------------------------------------------------|-----------------------|
| Program                                                       | Program (remote only) |
| Run                                                           | Run (remote only)     |

The following table describes the Automatic Firmware Update options that you can choose for the project. The Automatic Firmware Update property is also referred to as the Firmware Supervisor feature.

| If you want to                                                                                                                                                          | Then choose                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Enable automatic firmware updates so that I/O devices in the configuration tree of the controller that are configured to use Exact Match Keying are updated as required | Enable and Store Files to Image (1) |
| Disable automatic firmware updates and remove any I/O firmware files that are stored with the image                                                                     | Disable and Delete Files from Image |
| Disable automatic firmware updates when there are no firmware files are stored with the image                                                                           | Disable                             |

4. Click Store.
5. If a confirmation dialog box appears, click Yes.

<!-- image -->

The project is saved to the memory card as indicated by the controller status indicators.

|          | With these controllers These indications show the store status                                                                                                                                                                                                                                                                                                                                                                  |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-L6x | While the store is in progress, the following occurs: • OK indicator on the controller is steady red • A dialog box in the Logix Designer application indicates that the store is in progress When the store is complete, the following occurs: • The OK indicator on the controller is momentarily red, then steady green                                                                                                      |
| 1756-L7x | While the store is in progress, the following occurs: • OK indicator is flashing green • SD indicator is flashing green • SAVE is shown on the status display • A dialog box in the Logix Designer application indicates that the store is in progress When the store is complete, the following occurs: • The OK indicator on the controller is momentarily red, then steady green • The SD indicator on the controller is Off |

IMPORTANT

Allow the store to complete without interruption. If you interrupt the store, data corruption or loss can occur.

## Load from the Memory Card

After you have set the communication path, are online with the controller, and have changed the controller to Program mode, complete these steps to load a project to the controller from the memory card.

1. Open the Controller Properties and click the Nonvolatile Memory tab.
2. Click Load/Store.
3. TIP If Load/Store is dimmed (unavailable), verify the following:
- You have specified the correct communication path and are online with the controller.
- The memory card is installed.

<!-- image -->

If the memory card is not installed, a message in the lower-left corner of the Nonvolatile Memory tab indicates the missing card as shown here.

<!-- image -->

3. Verify that the image in nonvolatile memory (that is, the project on the memory card) is the project that you want to load.
2. TIP If no project is stored on the memory card, a message in the lower-left corner of the Nonvolatile Memory tab indicates that an image (or project) is not available as shown here.
3. TIP For information to change the project that is available to load from nonvolatile memory, see the Logix 5000® Controllers Nonvolatile Memory Programming Manual, publication 1756-PM017 .

<!-- image -->

.

## 4. Click Load.

<!-- image -->

5. If a confirmation dialog box appears, click Yes.

The project is loaded to the controller as indicated by the controller status indicators.

|          | With these controllers These indications show the store status                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-L6x | While the load is in progress, the following occurs: • OK indicator on the controller is flashing green • A dialog box in the Logix Designer application indicates that the store is in progress When the load is complete, the following occurs: • The OK indicator on the controller is momentarily red, then steady green                                                                                                                                                                                       |
| 1756-L7x | While the load is in progress, the following occurs: • OK indicator is steady red • SD indicator is flashing green • LOAD is shown on the status display • UPDT can be shown on the status display if the firmware is also updating with the load • A dialog box in the Logix Designer application indicates that the store is in progress When the load is complete, the following occurs: • The OK indicator on the controller is momentarily red, then steady green • The SD indicator on the controller is Off |

IMPORTANT Allow the load to complete without interruption. If you interrupt the load, data corruption or loss can occur.

## Use ControlLogix Energy Storage Modules (ESMs)

## Other Memory Card Tasks

Other tasks that you can complete by using the memory cards of the controller include the following:

- Change the image that is loaded from the card
- Check for a load that was completed
- Clear an image from the memory card
- Store an empty image
- Change load parameters
- Read/write application data to the card

For more information to complete any of these tasks, see the Logix 5000 Controllers Memory Card Programming Manual, publication 1756-PM017 .

You can use the ControlLogix ESMs to execute one of the following tasks:

- Provide power to 1756-L7x controllers to save the program to the onboard nonvolatile storage (NVS) memory of the controller after power is removed from the chassis or the controller is removed from a powered chassis.

.

## IMPORTANT

When you are using an ESM to save the program to onboard NVS memory, you are not saving the program to the SD card installed in the controller.

- Clear the program from the onboard NVS memory of the 1756-L7x controller. For more information, see Clear the Program from Onboard NVS Memory .

This table describes the energy storage modules (ESM).

| Cat. No.  Description                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-ESMCAP Capacitor-based ESM The 1756-L7x controllers come with this ESM installed.                                                                                                                                                                                                                                                     |
| 1756-ESMNSE Capacitor-based ESM without WallClockTime back-up power Use this ESM if your application requires that the ESM depletes its residual stored energy to 40 mJ or less before transporting it into or out of your application. Additionally, you can use this ESM with only a 1756-L73 (8 MB) or smaller memory-sized controller. |
| 1756-ESMNRM Secure capacitor-based ESM (nonremovable) This ESM provides your application an enhanced degree of security by blocking physical access to the USB connector and the SD card.                                                                                                                                                  |

## Save the Program to On-board NVS Memory

Follow these steps to save the program to NVS memory when the controller loses power.

1. Remove power from the controller.

You can remove power in one of two ways:

- Turn power off to the chassis while the controller is installed in the chassis.
- Remove the controller from a powered chassis.

Immediately after the controller is no longer powered, the program starts saving while the OK status indicator is green (this green is a dimmer green than normal operation), then turns red after program save is complete. Once the ESM stops operating, it turns off.

This graphic shows the OK status indicator on the controller.

<!-- image -->

2. Leave the ESM on the controller until the OK status indicator is Off.

## Clear the Program from Onboard NVS Memory

If your application lets you, follow these steps to clear the program from the onboard NVS memory of the 1756-L7x controller.

1. Remove the ESM from the controller.
2. Remove power from the controller.

You can remove power in one of the following two ways:

- Turn power off to the chassis while the controller is installed in the chassis.
- Remove the controller from a powered chassis.
3. Reinstall the ESM into the controller.
4. Restore power to the controller in one of these two ways:
- If the controller is installed in the chassis, turn power back onto the chassis.
- If the controller is not installed into the chassis, reinstall the controller into the chassis and turn power back onto the chassis.

## Estimate the ESM Support of the WallClockTime

## Maintain the Battery (Only 1756-L6x Controllers)

The ESM provides support for the maintenance of the WallClockTime of the controller when power is not applied. Use this table to estimate the hold-up time of the ESM based on the temperature of the controller and installed ESM.

|                   |   Temperature 1756-ESMCAP 1756-ESMNRM 1756-ESMNSE |    |
|-------------------|---------------------------------------------------|----|
| 20 °C (68 °F) 12  |                                                12 |  0 |
| 40 °C (104 °F) 10 |                                                10 |  0 |
| 60 °C (140 °F) 7  |                                                 7 |  0 |

## IMPORTANT

Any action that causes the 1756-L7x controller to reset (hard or soft), without an ESM installed, results in the WallClockTime of the controller being reset to the factory default of 01/01/1998.

To check the status of the ESM, see General Status Messages on page 174 .

This section explains how to monitor and maintain the lithium batteries that the ControlLogix controllers support.

Table 8 - 1756-L6x Controllers and Compatible Batteries

| Cat. No.                   | Series   | Compatible Battery                 |
|----------------------------|----------|------------------------------------|
| 1756-L61 1756-L62 1756-L63 | A        | 1756-BA1 or 1756-BATA or 1756-BATM |
| 1756-L61 1756-L62          | B        | 1756-BA2                           |
|                            | B        | 1756-L63XT                         |

For further information, see the Additional Resources section in the preface.

## Check the Battery Status

When the battery is approximately 95% discharged, these low-battery warnings are indicated:

- The BAT is steady red.
- A minor fault (type 10, code 10) is logged.

## IMPORTANT

To help prevent possible battery leakage, even if the BAT status indicator is off, replace a battery according to this schedule.

| If the temperature 2.54 cm (1 in.) below the chassis is   | Replace the battery within   |
|-----------------------------------------------------------|------------------------------|
| -25…35   C (-13…95   F)                                 | No replacement required      |
| 36…40   C (96.8…104   F)                                | 3 years                      |
| 41…45   C (105.8…113  F)                                | 2 years                      |
| 46…50   C (114.8…122   F)                               | 16 months                    |
| 51…55   C (123.8…131   F)                               | 11 months                    |
| 56…70   C (132.8…158  F)                                | 8 months                     |

## 1756-BA1 or 1756-BATA Battery Life

To estimate how long a 1756-BA1 or 1756-BATA battery can support controller memory on 1756-L6x, series A controllers, perform this procedure.

1. Determine the temperature 2.54 cm (1 in.) below the chassis.
2. Determine the weekly percentage of time that the controller is turned on.

## EXAMPLE

If a controller is Off at one of these times:

- 8 hr/day during a 5-day work week
- All day Saturday and Sunday

Then the controller is off 52% of the time:

- Total hours per week = 7 x 24 = 168 hrs
- Total off hours per week = (5 days x 8 hr/day) + Saturday + Sunday = 88 hrs
- Percentage off time = 88/168 = 52%

3. Determine the estimated worst-case battery life before and after the BAT status indicator turns on.
4. For each year of battery life, decrease the time before the BAT status indicator turns on by the percentage that is shown in the table.

Do not decrease the time after the BAT status indicator turns on.

## IMPORTANT

If the BAT status indicator turns on when you apply power to the controller, the remaining battery life can be less than Table 9 indicates. Some of the battery life can be used up while the controller is off and unable to turn on the BAT status indicator.

Table 9 - Worst-case Estimates of 1756-BA1 Battery Life

| Temperature Battery Life Before BAT Status Indicator Turns On Battery Life After BAT   | Status Indicator Turns On and Power is Off   | Temperature Battery Life Before BAT Status Indicator Turns On Battery Life After BAT   |
|----------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------|
| Power Off 100% Power Off 50% Yearly Decrease                                           | Status Indicator Turns On and Power is Off   |                                                                                        |
| 60 °C (140 °F) 22 days 43 days 23% 6 hrs                                               |                                              |                                                                                        |
| 25 °C (77 °F) 21 days 42 days 17% 28 hrs                                               |                                              |                                                                                        |
|                                                                                        | 0 °C (32 °F) 14 days 28 days 17% 2.5 days    |                                                                                        |

Table 10 - Worst-case Estimates of 1756-BATA Battery Life

| Temperature Battery Life Before BAT Status Indicator Turns On Battery Life After BAT   | Temperature Battery Life Before BAT Status Indicator Turns On Battery Life After BAT   | Status Indicator Turns On and Power is Off   |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------|
| Power Off 100% Power Off 50% Yearly                                                    | Decrease                                                                               | Status Indicator Turns On and Power is Off   |
|                                                                                        |                                                                                        | 60 °C (140 °F) 98 days 204 days 11% 104 days |
| 25 °C (77 °F) 146 days 268 days 5%                                                     |                                                                                        | 157 days                                     |
| 0 °C (32 °F) 105 days 222 days 6%                                                      |                                                                                        | 113 days                                     |

## 1756-BATM Battery Module and Battery Life

Use the 1756-BATM battery module with any 1756-L6x/A controller. The battery module is highly recommended for higher-memory controllers.

## IMPORTANT

If your project is not stored in nonvolatile memory, the use of the battery module is highly recommended.

When the 1756-BATA battery within the 1756-BATM module is approximately 50% discharged, these low-battery warnings are indicated:

- The BAT is steady red.
- A minor fault (type 10, code 10) is logged.

## Estimate 1756-BA2 Battery Life

The 1756-BA2 batteries are for use in 1756-L6x/B controllers. Use Table 11 to estimate how much time can elapse before the battery becomes low.

Table 11 - Worst-case Estimates of 1756-BA2 Life according to Temperatures and Power Cycles

| Temperature 2.54 cm (1 in.) Below the Chassis, max   | Power Cycles Battery Life Before the BAT Status Indicator Turns Red   | Power Cycles Battery Life Before the BAT Status Indicator Turns Red   | Power Cycles Battery Life Before the BAT Status Indicator Turns Red   | Power Cycles Battery Life Before the BAT Status Indicator Turns Red   | Power Cycles Battery Life Before the BAT Status Indicator Turns Red   |
|------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
|                                                      | Project Size                                                          | Project Size                                                          | Project Size                                                          | Project Size                                                          |                                                                       |
|                                                      | 1 MB  2 MB 4 MB                                                       | 8 MB 16 MB                                                            |                                                                       |                                                                       |                                                                       |
| -25…35 °C (-13…95 °F)                                | 3 per day                                                             | 3 years 3 years 26 months 20 months 10 months                         |                                                                       |                                                                       |                                                                       |
|                                                      |                                                                       | 2 per day or less 3 years 3 years 3 years 31 months 16 months         |                                                                       |                                                                       |                                                                       |
| 41…45 °C (105.8…113 °F)                              | 3 per day                                                             | 2 years 2 years 2 years 20 months 10 months                           |                                                                       |                                                                       |                                                                       |
|                                                      |                                                                       | 2 per day or less 2 years 2 years 2 years 2 years 16 months           |                                                                       |                                                                       |                                                                       |
| 46…50 °C (105.8…113 °F)                              |                                                                       | 3 per day or less 16 months 16 months 16 months 16 months 10 months   |                                                                       |                                                                       |                                                                       |
| 51…55 °C (123.8…131 °F)                              | 3 per day or less 11 months 11 months 11 months 11 months 10 months   |                                                                       |                                                                       |                                                                       |                                                                       |
| 56…70 °C (132.8…158 °F)                              | 3 per day or less 8 months 8 months 8 months 8 months 8 months        |                                                                       |                                                                       |                                                                       |                                                                       |

## Estimate 1756-BA2 Battery Life After Warnings

Use this table to estimate the battery life after the low-battery warnings are indicated. Use these times even if the controller does not have power because there is a small power-drain on the battery.

## IMPORTANT

When you power up the controller, see if there is a low-battery warning. If you get a low-battery warning for the first time, you have less battery life than this table shows. While powered down, the controller still drains the battery but it cannot give the low-battery warning.

|                                                          | Power Cycles Battery Life After the BAT Status Indicator Turns Red (worst case)   | Power Cycles Battery Life After the BAT Status Indicator Turns Red (worst case)   | Power Cycles Battery Life After the BAT Status Indicator Turns Red (worst case)   | Power Cycles Battery Life After the BAT Status Indicator Turns Red (worst case)   | Power Cycles Battery Life After the BAT Status Indicator Turns Red (worst case)   |
|----------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|                                                          | Project Size                                                                      | Project Size                                                                      | Project Size                                                                      | Project Size                                                                      | Project Size                                                                      |
|                                                          | 1 MB 2 MB 4 MB 8 MB 16 MB                                                         |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 0…20 °C (32…68 °F) 3 per day                             | 26 weeks 18 weeks 12 weeks 9 weeks 5 weeks                                        |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 26 weeks 26 weeks 26 weeks 22 weeks 13 weeks                                      |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 26 weeks 26 weeks 26 weeks 26 weeks 26 weeks |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 21…40 °C (69.8…104 °F) 3 per day                         | 18 weeks 14 weeks 10 weeks 8 weeks 5 weeks                                        |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 24 weeks 21 weeks 18 weeks 16 weeks 11 weeks                                      |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 26 weeks 26 weeks 26 weeks 26 weeks 26 weeks |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 41…45 °C (105.8…113 °F) 3 per day                        | 12 weeks 10 weeks 7 weeks 6 weeks 4 weeks                                         |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 15 weeks 14 weeks 12 weeks 11 weeks 8 weeks                                       |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 17 weeks 17 weeks 17 weeks 17 weeks 16 weeks |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 46…50 °C (105.8…113 °F) 3 per day                        | 10 weeks 8 weeks 6 weeks 6 weeks 3 weeks                                          |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 12 weeks 11 weeks 10 weeks 9 weeks 7 weeks                                        |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 12 weeks 12 weeks 12 weeks 12 weeks 12 weeks |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 51…55 °C (123.8…131 °F) 3 per day                        | 7 weeks 6 weeks 5 weeks 4 weeks 3 weeks                                           |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 8 weeks 8 weeks 7 weeks 7 weeks 5 weeks                                           |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 8 weeks 8 weeks 8 weeks 8 weeks 8 weeks      |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 56…60 °C (132.8…140 °F) 3 per day                        | 5 weeks 5 weeks 4 weeks 4 weeks 2 weeks                                           |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per day                                                | 6 weeks 6 weeks 5 weeks 5 weeks 4 weeks                                           |                                                                                   |                                                                                   |                                                                                   |                                                                                   |
| 1 per month 6 weeks 6 weeks 6 weeks 6 weeks 6 weeks      |                                                                                   |                                                                                   |                                                                                   |                                                                                   |                                                                                   |

## EXAMPLE

Under these conditions, the battery lasts at least 20 months before the BAT status indicator turns red:

- The maximum temperature 2.54 cm (1 in.) below the chassis = 45 °C (113 °F).
- You cycle power to the controller three times per day.
- The controller contains an 8 MB project.

## Battery Storage and Disposal

<!-- image -->

<!-- image -->

Follow these general rules to store your batteries:

- Store batteries in a cool, dry environment. We recommend 25 °C (77 °F) with 40…60% relative humidity.
- You can store batteries for up to 30 days in temperatures from -45…85 °C (-49…185 °F), such as during transportation.
- To avoid leakage or other hazards, do not store batteries above 60 °C (140 °F) for more than 30 days.

This product contains a sealed lithium battery that must be replaced during the life of the product.

At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste.

The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are recovered.

## ControlLogix System

<!-- image -->

## ControlLogix System and Controllers

The ControlLogix® system is chassis-based and provides the option to configure a control system that uses sequential, process, motion, drive control, and communication and I/O capabilities.

## Configuration Options

This section describes some of the many system configuration options that are available with ControlLogix controllers.

## Standalone Controller and I/O

One of the simplest ControlLogix configurations is a standalone controller with I/O assembled in one chassis.

Figure 7 - Standalone Controller and I/O5

<!-- image -->

## Multiple Controllers in One Chassis

For some applications, multiple controllers can be used in one ControlLogix chassis. For example, for better performance, multiple controllers can be used in motion applications.

Figure 8 - Multiple Controllers in One Chassis

<!-- image -->

## Multiple Devices Connected Via Multiple Networks

For some applications, various devices can be connected to the ControlLogix chassis via multiple communication networks. For example, a system can be connected to the following:

- Distributed I/O via an Ethernet network
- A PowerFlex® drive connected via a DeviceNet® network
- Flowmeters that are connected via a HART connection

Figure 9 - Multiple Devices Connected Via Multiple Networks

<!-- image -->

Design a ControlLogix System When you design a ControlLogix system, there are several system components
idfliiSf hildh to consider for your application. Some of these components include the following:

- I/O devices
- Motion control and drive requirements
- Communication modules
- Controllers
- Chassis
- Power supplies
- Studio 5000® environment

For more information to design and select components for your ControlLogix system, see the ControlLogix Selection Guide, publication 1756-SG001.

See the Additional Resources section in the preface for more information if you are designing your ControlLogix System for any of the following applications:

- Motion with Integrated Motion on the EtherNet/IP™ network
- Motion with the use of a coordinate system
- Motion with Sercos or analog motion
- Enhanced redundancy
- Standard redundancy
- SIL 2
- SIL 2 fault-tolerant I/O with Studio 5000 subroutines
- SIL 2 fault-tolerant I/O with Studio 5000 Add-On Instructions

## ControlLogix Controller Features

Table 12 - ControlLogix Controller Features

| Feature                                 | 1756-L61, 1756-L62, 1756-L63, 1756- L64, 1756-L65                                                                                | 1756-L71, 1756-L72, 1756-L73, 1756- L74, 1756-L75                                                                                                                                                                                   | 1756-L72EROM, 1756-L73EROM                                                                                                                                                                                                          |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller tasks                        | • 32 tasks • 100 programs/task • Event tasks: all event triggers                                                                 | • 32 tasks • 1000 programs/task starting in Logix Designer application version 24 and later • 100 programs/task starting in Logix Designer application version 15 • 32 programs/task prior to Logix Designer application version 15 | • 32 tasks • 1000 programs/task starting in Logix Designer application version 24 and later • 100 programs/task starting in Logix Designer application version 15 • 32 programs/task prior to Logix Designer application version 15 |
| Communication ports                     | 1 port - RS-232 serial                                                                                                           | 1 port - USB, 2.0 full-speed, Type B                                                                                                                                                                                                | 1 port - USB, 2.0 full-speed, Type B                                                                                                                                                                                                |
| Communication options                   | • EtherNet/IP • ControlNet® • DeviceNet • Data Highway Plus™ • Remote I/O • SynchLink™ • Third-party process and device networks | • EtherNet/IP • ControlNet® • DeviceNet • Data Highway Plus™ • Remote I/O • SynchLink™ • Third-party process and device networks                                                                                                    | EtherNet/IP                                                                                                                                                                                                                         |
| Serial port communication               | • ASCII • DF1 full/half-duplex • DF1 radio modem • DH-485 • Modbus via logic                                                     | N/A                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                 |
| Controller connections supported, max   | 250                                                                                                                              | 500                                                                                                                                                                                                                                 | 500                                                                                                                                                                                                                                 |
| Network connections, per network module | • 128 ControlNet (1756-CN2/B) • 100 ControlNet (1756-CN2/A) • 40 ControlNet (1756-CNB) • 256 EtherNet/IP; 128 TCP (1756-EN2x)    | • 128 ControlNet (1756-CN2/B) • 100 ControlNet (1756-CN2/A) • 40 ControlNet (1756-CNB) • 256 EtherNet/IP; 128 TCP (1756-EN2x)                                                                                                       | 256 EtherNet/IP; 128 TCP (1756-EN2x)                                                                                                                                                                                                |
| Controller redundancy                   | Full support except for motion applications                                                                                      | Full support except for motion applications                                                                                                                                                                                         | Full support except for motion applications                                                                                                                                                                                         |
| Integrated motion                       | • Integrated Motion on the EtherNet/IP network • Sercos interface • Analog options: – Encoder input – LDT input – SSI input      | • Integrated Motion on the EtherNet/IP network • Sercos interface • Analog options: – Encoder input – LDT input – SSI input                                                                                                         | • Integrated Motion on the EtherNet/IP network • Sercos interface • Analog options: – Encoder input – LDT input – SSI input                                                                                                         |
| Programming languages                   | • Relay ladder • Structured text • Function block • Sequential function chart (SFC)                                              | • Relay ladder • Structured text • Function block • Sequential function chart (SFC)                                                                                                                                                 | • Relay ladder • Structured text • Function block • Sequential function chart (SFC)                                                                                                                                                 |

The ControlLogix controllers are part of the Logix 5000® family of controllers that are offered by Rockwell Automation. The sections that follow describe the differentiating features of the ControlLogix controllers.

## System, Communication, and Programming Features

Table 12 lists the system, communication, and programming features available with ControlLogix controllers.

## Memory Options

The ControlLogix controller is available in different combinations of user memory. Use Table 13 to determine which controller meets your memory requirements.

.

Table 13 - ControlLogix Controller Memory Options

| Controller                | Memory for Data and Logic I/O   |                           | Back-up Memory        |
|---------------------------|---------------------------------|---------------------------|-----------------------|
| 1756-L61                  | 2 MB                            | 478 KB                    | CompactFlash card (1) |
| 1756-L62                  | 4 MB                            | 478 KB                    | CompactFlash card (1) |
| 1756-L63, 1756-L63XT 8 MB |                                 | 478 KB                    | CompactFlash card (1) |
| 1756-L64                  | 16 MB                           | 478 KB                    | CompactFlash card (1) |
| 1756-L65                  | 32 MB                           | 478 KB                    | CompactFlash card (1) |
| 1756-L71                  | 2 MB                            | 0.98 MB (1006 KB) SD card |                       |
| 1756-L72                  | 4 MB                            | 0.98 MB (1006 KB) SD card |                       |
| 1756-L73, 1756-L73XT 8 MB |                                 | 0.98 MB (1006 KB) SD card |                       |
| 1756-L74                  | 16 MB                           | 0.98 MB (1006 KB) SD card |                       |
| 1756-L75                  | 32 MB                           | 0.98 MB (1006 KB) SD card |                       |
| 1756-L72EROM 4 MB         |                                 | 0.98 MB (1006 KB) SD card |                       |
| 1756-L73EROM 8 MB         |                                 | 0.98 MB (1006 KB) SD card |                       |

## IMPORTANT

The 1756-L7x controllers ship with an SD card installed. We recommend that you leave the SD card installed, so if a fault occurs, diagnostic data is automatically written to the card and Rockwell Automation can use the data to troubleshoot the anomaly.

## IMPORTANT

We recommend that you use the SD cards available from Rockwell Automation (catalog numbers 1784-SD1 or 1784-SD2).

While other SD cards can be used with the controller, Rockwell Automation has not tested the use of those cards with the controller. If you use an SD card other than those cards that are available from Rockwell Automation, you can experience data corruption or loss.

Also, SD cards that are not provided by Rockwell Automation can have different industrial, environmental, and certification ratings as those cards that are available from Rockwell Automation and can have difficulty with survival in the same industrial environments as the industrially rated versions available from Rockwell Automation.

## Electronic Keying

Electronic Keying reduces the possibility that you use the wrong device in a control system. It compares the device that is defined in your project to the installed device. If keying fails, a fault occurs. These attributes are compared.

| Attribute Description                                                                     |
|-------------------------------------------------------------------------------------------|
| Vendor The device manufacturer.                                                           |
| Device Type The general type of the product, for example, digital I/O module.             |
| Product Code The specific type of the product. The Product Code maps to a catalog number. |
| Major Revision A number that represents the functional capabilities of a device.          |
| Minor Revision A number that represents behavior changes in the device.                   |

The following Electronic Keying options are available.

| Keying Option Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatible Module Lets the installed device accept the key of the device that is defined in the project when the installed device can emulate the defined device. With Compatible Module, you can typically replace a device with another device that has the following characteristics: • Same catalog number • Same or higher Major Revision • Minor Revision as follows: – If the Major Revision is the same, the Minor Revision must be the same or higher. – If the Major Revision is higher, the Minor Revision can be any number.                                                                                     |
| Disable Keying Indicates that the keying attributes are not considered when attempting to communicate with a device. With Disable Keying, communication can occur with a device other than the type specified in the project. ATTENTION: Be cautious when using Disable Keying; if used incorrectly, this option can lead to personal injury or death, property damage, or economic loss. We strongly recommend that you do not use Disable Keying. If you use Disable Keying, you must take full responsibility for understanding whether the device being used can fulfill the functional requirements of the application. |
| Exact Match Indicates that all keying attributes must match to establish communication. If any attribute does not match precisely, communication with the device does not occur.                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Carefully consider the implications of each keying option when selecting one.

| IMPORTANT   | Changing Electronic Keying parameters online interrupts connections to the device and any devices that are connected through the device. Connections from other controllers can also be broken. If an I/O connection to a device is interrupted, the result can be a loss of data.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## More Information

For more detailed information on Electronic Keying, see Electronic Keying in the Logix 5000 Control Systems Application Technique, publication LOGIX-AT001 .

## Notes:

## Networks Available

## EtherNet/IP Network Communication

## Communication Networks

Several communication networks are available for use with ControlLogix® systems. Table 14 describes typical network applications that are used with ControlLogix systems and lists the networks available to support such applications.

Table 14 - Applications and Supported Networks

| Application Type                                                                                                          | Supported Networks                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Integrated Motion                                                                                                         | EtherNet/IP™                                                                                           |
| Integrated Motion on the EtherNet/IP network for time synchronization EtherNet/IP                                         |                                                                                                        |
| Control of distributed I/O                                                                                                | • ControlNet® • DeviceNet® • EtherNet/IP • Foundation Fieldbus • HART • Universal remote I/O           |
| Produce/consume data between controllers                                                                                  | • ControlNet • EtherNet/IP                                                                             |
| Messaging to and from other devices, including access to the controller via the Studio 5000 Logix Designer ®  application | • ControlNet • DeviceNet (only to devices) • Data Highway Plus™ (DH+™) • DH-485 • EtherNet/IP • Serial |

For more information about network design for your system, see the Ethernet Design Considerations Reference Manual, publication ENET-RM002 .

The EtherNet/IP network offers a full suite of control, configuration, and data collection services by layering the Common Industrial Protocol (CIP™) over the standard internet protocols, such as TCP/IP and UDP. This combination of well-accepted standards provides the capability that is required to support information data exchange and control applications.

The EtherNet/IP network uses commercially available Ethernet components and physical media, providing you with a cost-effective plant-floor solution.

<!-- image -->

Figure 10 - EtherNet/IP Network Example

<!-- image -->

For more information about using EtherNet/IP modules, see the EtherNet/IP Modules in Logix 5000 Control Systems User Manual, publication ENET-UM001 .

## ControlLogix EtherNet/IP Module Features

The ControlLogix EtherNet/IP communication modules provide these features:

- Support for messaging, produced/consumed tags, HMI, and distributed I/O
- The ability to encapsulate messages within the standard TCP/UDP/IP protocol
- A common application layer with ControlNet and DeviceNet networks
- Network connections via an RJ45 cable
- Support half/full duplex 10 MB or 100 MB operation
- Support standard switches

## ControlLogix EtherNet/IP Communication Modules

For EtherNet/IP network communication in a ControlLogix system, you have a number of modules to choose from. Table 15 lists their primary features.

Table 15 - EtherNet/IP Communication Modules and Capabilities

| Module  Is used to                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-ENBT • Connect controllers to I/O modules (requires an adapter for distributed I/O). • Communicate with other EtherNet/IP devices (messages). • Serve as a pathway to share data between Logix 5000® controllers (produce/ consume). • Bridge EtherNet/IP nodes to route messages to devices on other networks.                                                                                                                                                                |
| 1756-EN2T • Perform the same functions as a 1756-ENBT module, with twice the capacity for more demanding applications. • Provide a temporary configuration connection via the USB port. • Configure IP addresses quickly by using rotary switches. • Supports as many as 8 integrated motion on the EtherNet/IP network axes                                                                                                                                                        |
| 1756-EN2F • Perform the same functions as a 1756-EN2T module. • Connect fiber media by an LC fiber connector on the module.                                                                                                                                                                                                                                                                                                                                                         |
| 1756-EN2TR • Perform the same functions as a 1756-EN2T module. • Support communication on a ring topology for a Device Level Ring (DLR) single-fault tolerant ring network.                                                                                                                                                                                                                                                                                                         |
| 1756-EN2TRXT • Perform the same functions as a 1756-EN2T module. • Support communication on a ring topology for a Device Level Ring (DLR) single-fault tolerant ring network. • Operate in extreme environments with -25…+70 °C (-13…+158 °F) temperatures.                                                                                                                                                                                                                         |
| 1756-EN3TR • Perform the same functions as the 1756-EN2TR module. • Extended Integrated Motion on EtherNet/IP network. • Support of up to 128 motion axes.                                                                                                                                                                                                                                                                                                                          |
| 1756-EN2TSC • Perform the same functions as a 1756-ENBT module, with twice the capacity for more demanding applications. • Provide a temporary configuration connection via the USB port. • Configure IP addresses quickly by using rotary switches.                                                                                                                                                                                                                                |
| 1756-EN2TXT • Perform the same functions as a 1756-EN2T module. • Operate in extreme environments with -25…+70 °C (-13…+158 °F) temperatures.                                                                                                                                                                                                                                                                                                                                       |
| 1756-EWEB • Provide customizable webpages for external access to controller information. • Provide remote access via an internet browser to tags in a local ControlLogix controller. • Communicate with other EtherNet/IP devices (messages). • Bridge EtherNet/IP nodes to route messages to devices on other networks. • Support Ethernet devices that are not EtherNet/IP-based with a socket interface. This module does not provide support for I/O or produced/consumed tags. |

## Software for EtherNet/IP Networks

Table 16 lists software that is used with the EtherNet/IP networks and modules

.

Table 16 - Software for Use with EtherNet/IP Networks

| Software           | Is used to                                                                                                                                | Required or Optional   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|                    | Logix Designer application • Configure ControlLogix projects. • Define EtherNet/IP communication.                                         | Required               |
|                    | RSLinx® Classic or FactoryTalk® Linx • Configure communication devices. • Provide diagnostics. • Establish communication between devices. | Required               |
| BOOTP/DHCP Utility | Assign IP addresses to devices on an EtherNet/IP network. Optional                                                                        |                        |
|                    | RSNetWorx™ for EtherNet/IP™ • Configure EtherNet/IP devices by IP addresses and/or host names. • Provide bandwidth status.                |                        |

## Connections Over an EtherNet/IP Network

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system. Connections are allocations of resources that provide more reliable communication between devices as compared to unconnected messages.

All EtherNet/IP connections are unscheduled. The requested packet interval (RPI) for I/O control or the program, such as an MSG instruction triggers an unscheduled connection. Unscheduled messaging lets you send and receive data when needed.

## Double Data Rate (DDR) Backplane Communication

DDR communication can be achieved with the 1756-L7x controller. The following communication modules support DDR when used with the 1756-L7x controller. Some modules require a minimum series:

- 1756-EN2T/C
- 1756-EN2TR/B
- 1756-EN2TF/B
- 1756-EN2TXT/C
- 1756-RM/B

DDR communication is achieved most efficiently when all modules in the communication path are DDR modules, or, in other words, as one conversation (connection) only between DDR modules.

## ControlNet Network Communication

DDR communication is achievable in a chassis with a mix of DDR and nonDDR modules. The DDR communication occurs between the modules that support it. If non-DDR modules are also in the chassis, communication between those modules is at the non-DDR rate.

For example, you can have a chassis with two 1756-L7x controllers in slots 0 and 1 communicating with each other by using DDR, and two 1756-L6x controllers in slots 2 and 3 communicating by using non-DDR.

When multicast communication is used within a chassis to multiple modules, the transmission rate is limited to the slowest module—or at the non-DDR rate.

For example, if a 1756-L7x controller is producing a tag to a 1756-L7x controller and a 1756-L6x controller on the same multicast connection, it must use the non-DDR rate.

The ControlNet network is a real-time control network that provides highspeed transport of time-critical I/O and interlocking data and messaging data. This includes the upload and download of program and configuration data on one physical-media link. The highly efficient data transfer capability of the ControlNet network significantly enhances I/O performance and peer-to-peer communication in any system or application.

The ControlNet network is highly deterministic and repeatable and is unaffected when devices are connected or disconnected from the network. This quality results in dependable, synchronized, and coordinated real-time performance.

The ControlNet network often functions as the following:

- A substitute/replacement for the remote I/O (RIO) network because the ControlNet network adeptly handles large numbers of I/O points
- A backbone for multiple distributed DeviceNet networks
- A peer interlocking network

Figure 11 - ControlNet Network Overview

<!-- image -->

In this example, these actions occur via the ControlNet network:

- The controllers produce and consume tags.
- The controllers initiate MSG instructions that do the following:
- – Send and receive data.
- – Configure devices.
- The workstation is used to do the following:
- – Configure the ControlNet devices and the ControlNet network.
- – Download and upload projects from the controllers.

For more information about using ControlNet modules, see ControlNet Modules in Logix 5000 Control Systems User Manual, publication CNET-UM001 .

## ControlLogix ControlNet Module Features

The ControlNet communication modules provide these features:

- Support for messaging, produced/consumed tags, and distributed I/O
- Use a common application layer with DeviceNet and EtherNet/IP networks
- Requires no routing tables
- Support the use of coax and fiber repeaters for isolation and increased distance
- Support redundant media (only 1756-CNBR, 1756-CN2R, and 1756-CN2RXT modules)

## ControlLogix ControlNet Modules

Table 17 lists the available ControlLogix ControlNet modules and their primary features.

Table 17 - ControlNet Modules and Capabilities

| Module Is used to                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-CNB • Control I/O modules. • Communicate with other ControlNet devices (messages). • Share data with other Logix 5000 controllers (produce/consume). • Bridge ControlNet links to route messages to devices on other networks. |
| 1756-CNBR • Perform the same functions as a 1756-CNB module. • Support redundant ControlNet media.                                                                                                                                  |
| 1756-CN2 • Perform the same functions as a 1756-CNB module. • Provide twice the capacity for more demanding applications.                                                                                                           |
| 1756-CN2R • Perform the same functions as a 1756-CN2 module. • Support redundant ControlNet media.                                                                                                                                  |
| 1756-CN2RXT • Perform same functions as a 1756-CN2R module. • Operate in extreme environments with -25…+70 °C (-13…+158 °F) temperatures.                                                                                           |

## Software for ControlNet Networks

Table 18 lists software that is used with the ControlNet networks and modules.

Table 18 - Software for Use with ControlNet Networks

| Software  Is used to                                                                                                               | Required or Optional   |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Logix Designer application • Configure ControlLogix projects. • Define ControlNet communication.                                   | Required               |
| RSNetWorx™ for ControlNet™ • Configure ControlNet devices. • Schedule a network.                                                   | Required               |
| RSLinx® Classic or Enterprise • Configure communication devices. • Provide diagnostics. • Establish communication between devices. | Required               |

## DeviceNet Network Communication

## Connections Over a ControlNet Network

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system. Connections are allocations of resources that provide communication between devices as compared to unconnected messages.

Table 19 - ControlNet Connections

| Connection Definition                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduled (unique to a ControlNet network) | A scheduled connection is unique to ControlNet communication. A scheduled connection lets you send and receive data repeatedly at a predetermined interval, which is the requested packet interval (RPI). For example, a connection to an I/O module is a scheduled connection because you repeatedly receive data from the module at a specified interval. Other scheduled connections include connections to the following: • Communication devices • Produced/consumed tags On a ControlNet network, you must use RSNetWorx for ControlNet software to enable all scheduled connections and establish a network update time (NUT). A scheduled connection reserves network bandwidth specifically to handle the connection. |
|                                            | Unscheduled An unscheduled connection is a message transfer between devices that the requested packet interval (RPI) or the program, such as an MSG instruction, triggers. Unscheduled messaging allows you to send and receive data when you must: Unscheduled connections use the remainder of network bandwidth after scheduled connections are allocated.                                                                                                                                                                                                                                                                                                                                                                  |

## ControlNet Module Connections

The 1756-CNB and 1756-CNBR communication modules support 64 CIP connections over a ControlNet network. However, for optimal performance, configure a maximum of 48 connections for each module.

The 1756-CN2, 1756-CN2R, and 1756-CN2RXT communication modules support 128 connections over a ControlNet network, all of which can be configured without risk of performance degradation.

The DeviceNet network uses the Common Industrial Protocol (CIP) to provide the control, configuration, and data collection capabilities for industrial devices. The DeviceNet network uses the proven Controller Area Network (CAN) technology, which lowers installation costs and decreases installation time and costly downtime.

A DeviceNet network provides access to the intelligence present in your devices by letting you connect devices directly to plant-floor controllers without having to hard-wire each device into an I/O module.

With a ControlLogix system, DeviceNet communication requires the use of a 1756-DNB DeviceNet communication module.

<!-- image -->

In this example, the ControlLogix controller is connected to the DeviceNet network and devices via the 1788-EN2DNR linking device.

For more information about using DeviceNet modules and devices, see DeviceNet Modules in Logix 5000 Control Systems User Manual, publication DNET-UM004 .

## ControlLogix DeviceNet Module Features

The DeviceNet communication module provides these features:

- Supports messaging to devices (not controller to controller)
- Shares a common application layer with ControlNet and EtherNet/IP networks
- Offers diagnostics for improved data collection and fault detection
- Requires less wiring than standard, hard-wired systems

## ControlLogix DeviceNet Bridge and Linking Devices

Table 20 lists the available ControlLogix DeviceNet bridge and linking devices that can be used with the DeviceNet network.

Table 20 - DeviceNet Communication Modules and Capabilities

| Module/Device Is used to                                                                    |
|---------------------------------------------------------------------------------------------|
| 1756-DNB  • Control I/O modules. • Communicate with other DeviceNet devices (via messages). |
| 1788-EN2DNR Link an EtherNet/IP network to a DeviceNet network.                             |
| 1788-CN2DN Link a ControlNet network to a DeviceNet network.                                |

## Software for DeviceNet Networks

Table 21 lists software that is used with the DeviceNet networks and modules.

Table 21 - Software for Use with DeviceNet Networks

| Software  Is used to                                                                                                              | Required or Optional   |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Logix Designer application • Configure ControlLogix projects. • Define DeviceNet communication.                                   | Required               |
| RSNetWorx™ for DeviceNet™ • Configure DeviceNet devices. • Define the scan list for those devices.                                | Required               |
| RSLinx Classic or Enterprise • Configure communication devices. • Provide diagnostics. • Establish communication between devices. | Required               |

## Connections Over DeviceNet Networks

The ControlLogix controller requires two connections for each 1756-DNB module. One connection is for module status and configuration. The other connection is a rack-optimized connection for the device data.

## ControlLogix DeviceNet Module Memory

The 1756-DNB module has fixed sections of memory for the input and output data of the DeviceNet devices on the network. Each device on your network requires some input or output memory of the scanner. Some devices send and receive data, so they need input and output memory. The 1756-DNB module supports up to add the following:

- 124 DINTs of input data
- 123 DINTs of output data

## Data Highway Plus (DH+) Network Communication

For DH+ network communication, you have two module options for use in the ControlLogix chassis. Table 22 lists the DH+ modules and capabilities.

Table 22 - DH+ Modules and Capabilities

| RIO Module Is used to                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-DHRIO • Function as a remote I/O (RIO) scanner. • Support 32 logical rack connections or 16 block transfer connections per channel. • Establish connections between controllers and I/O adapters. • Distribute control so that each controller has its own I/O.                                                                               |
| 1756-DHRIOXT • Function as a remote I/O (RIO) scanner. • Support 32 logical rack connections or 16 block transfer connections per channel. • Establish connections between controllers and I/O adapters. • Distribute control so that each controller has its own I/O. • Operate in extreme environments with -25…70 °C (-13…158 °F) temperatures. |

For DH+ network communication, use a 1756-DHRIO or 1756-DHRIOXT module in the ControlLogix chassis to exchange information between these controllers:

- PLC and SLC™ controllers
- ControlLogix controllers and PLC or SLC controllers
- ControlLogix controllers

The DH+ network also provides the following:

- Data exchange between controllers
- Plant-wide data sharing
- Cellular level data sharing

You can connect a maximum of 32 stations to one DH+ link:

- Channel A supports 57.6 Kbps, 115.2 Kbps, and 230.4 Kbps.
- Channel B supports 57.6 Kbps and 115.2 Kbps.

Figure 13 - ControlLogix DH+ Network Communication Example

<!-- image -->

## Communicate Over a DH+ Network

For the controller to communicate to a workstation or other device over a DH+ network, use RSLinx Classic software to do the following:

- Specify a unique link ID for each ControlLogix backplane and additional network in the communication path.
- Configure the routing table for the 1756-DHRIO or 1756-DHRIOXT module.

The 1756-DHRIO or 1756-DHRIOXT module can route a message through up to four communication networks and three chassis. This limit applies only to the routing of a message and not to the total number of networks or chassis in a system.

For more information to configure and use a DH+ network via the 1756-DHRIO or 1756-DHRIOXT module, see the Data Highway PlusRemote I/O Communication Interface Module User Manual, publication 1756-UM514 .

## Universal Remote I/O (RIO) Communication

For universal remote I/O communication, you have two module options for use in the ControlLogix chassis. Table 23 lists the RIO modules and capabilities.

Table 23 - RIO Modules and Capabilities

| RIO Module Is used to                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-RIO • Function as an RIO scanner and adapter. • Support connections to 32 racks in any combination of rack size or block transfers. • Update data to the ControlLogix controller by using scheduled connections.                                                                                                                  |
| 1756-DHRIO • Function as an RIO scanner. • Support 32 logical rack connections or 16 block transfer connections per channel. • Establish connections between controllers and I/O adapters. • Distribute control so that each controller has its own I/O.                                                                               |
| 1756-DHRIOXT • Function as an RIO scanner. • Support 32 logical rack connections or 16 block transfer connections per channel. • Establish connections between controllers and I/O adapters. • Distribute control so that each controller has its own I/O. • Operate in extreme environments with -25…70 °C (-13…158 °F) temperatures. |

When a channel on the 1756-DHRIO or 1756-DHRIOXT module is configured for remote I/O, the module acts as a scanner for a universal remote I/O network. The controller communicates to the module to send and receive the I/O data on the universal remote I/O network.

The 1756-RIO module can act as a scanner or adapter on a remote I/O network. The 1756-RIO module transfers digital, block transfer, analog, and specialty data without message instructions.

Figure 14 - ControlLogix Universal Remote I/O Communication Example

<!-- image -->

## Foundation Fieldbus Communication

## Communicate over a Universal Remote I/O Network

For the controller to control I/O over a universal remote I/O network, you must complete these tasks.

1. Configure the remote I/O adapter.
2. Lay out the remote I/O network cable.
3. Connect the remote I/O network cable.
4. Configure the scanner channel.

For more information to configure a remote I/O network with the 1756-RIO, 1756-DHRIO, or 1756-DHRIOXT modules, see these publications:

- Data Highway Plus-Remote I/O Communication Interface Module User Manual, publication 1756-UM514
- ControlLogix Remote I/O Communication Module User Manual, publication 1756-UM534

As you design your remote I/O network, remember the following:

- All devices that are connected to a remote I/O network must communicate by using the same communication rate. These rates are available for remote I/O:
- – 57.6 Kbps
- – 115.2 Kbps
- – 230.4 Kbps
- You must assign unique partial and full racks to each channel used in Remote I/O Scanner mode.

Both channels of a 1756-DHRIO or 1756-DHRIOXT module cannot scan the same partial or full rack address. Both module channels can communicate to 00…37 octal or 40…77 octal, but each channel can communicate only with one address at a time in whichever of these two ranges it falls.

Foundation Fieldbus is an open interoperable fieldbus that is designed for process control instrumentation. The fieldbus devices that are described in Table 24 can be connected to the ControlLogix controller via another network as shown in the following example.

Table 24 - Fieldbus Devices and Capabilities

| Fieldbus Device Is used to                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1788-EN2FFR • Bridge an EtherNet/IP network to Foundation Fieldbus. • Connect via a low-speed serial (H1) and high-speed Ethernet (HSE) network connections. • Access devices directly via an OPC server. |
| 1788-CN2FFR • Connect via low-speed serial (H1) connections. • Bridge a ControlNet network to a Foundation Fieldbus. • Support redundant ControlNet media.                                                |

Foundation Fieldbus distributes and executes control in the device. The Foundation Fieldbus linking device does the following:

- Bridges from an EtherNet/IP network to an H1 connection
- Accepts HSE or EtherNet/IP messages and converts them to the H1 protocol

## Figure 15 - Foundation Fieldbus Example

<!-- image -->

For more information about using the Foundation Fieldbus devices available from Rockwell Automation, see these publications:

- EtherNet/IP and ControlNet to FOUNDATION Fieldbus Linking Device User Manual, publication 1788-UM057
- FOUNDATION Fieldbus Design Considerations Reference Manual, publication PROCES-RM005

## HART Communication

HART (Highway Addressable Remote Transducer) is an open protocol that is designed for process control instrumentation.

| Device                       | Is used to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              | 1756 analog HART I/O modules: • Act as HART master to allow communication with HART field devices. • Interface directly with field devices (through built-in HART modems), which eliminates the need for external hardware and more wiring. • Provide access to more field device data, including voltage and current measurements. • Directly connect asset management software to HART devices. • Support differential wiring for environments where improved noise immunity is needed (input modules). |
| ProSoft interface MVI56-HART | • Acquire data or control application with slow update requirements, such as a tank farm. • Does not require external hardware to access HART signal. • Does not provide a direct connection to asset management software.                                                                                                                                                                                                                                                                                |

The HART protocol combines digital signals with analog signals to ready the digital signal for the Process Variable (PV). The HART protocol also provides diagnostic data from the transmitter.

Figure 16 - HART Protocol Example

<!-- image -->

For more information about using the HART I/O modules, see the ControlLogix HART Analog I/O Modules User Manual, publication 1756-UM533 .

For more information about the ProSoft HART interface, see the ProSoft Technologies website at http://www.prosoft-technology.com .

## ControlLogix 5560 Controller Serial Port

## Serial Communication on ControlLogix 5560 Controllers

ControlLogix® 5560 controllers have a built-in RS-232 port that can be used in various serial-based applications. The potential serial communication applications include the following:

- DF1 modes (including broadcast message support)
- DF1 radio modem
- ASCII device communication

Figure 17 - ControlLogix DF1 Device Communication Example

<!-- image -->

## ControlLogix Chassis Serial Communication Options

You can use the serial port of the ControlLogix controller or use ProSoft modules in the ControlLogix to achieve serial communication. Options specific to the ControlLogix controller serial port are described in this chapter.

For more information about ProSoft modules that can be used to establish serial communication, see the ProSoft Technology website or go to http://www.prosoft-technology.com and browse available products.

<!-- image -->

## Communication with Serial Devices

Table 25 - Serial Port Modes, Protocols, and Uses

| Mode Protocol     | Is used to                                                                                                                                              |   Page |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| System DF1 Master | Control polling and message transmission between the master and slave nodes.                                                                            |    104 |
|                   | DF1 Point to Point • Communicate between the controller and one other DF1-protocol-compatible device. • Program the controller via the serial port.     |    104 |
|                   | DF1 Radio Modem • Communication with SLC™ 500 and MicroLogix™ 1500 controllers. • This protocol supports master/slave and store/forward configurations. |    105 |
| DF1 Slave         | Configure the controller as a slave station in a master/slave serial communication network.                                                             |    108 |
| DH-485            | Communication with other DH-485 devices via a multi-master and token-passing network that enables programming and peer-to-peer messaging.               |    108 |
| User ASCII        | • Communicate with ASCII devices. • Use ASCII instructions to read and write data from and to an ASCII device.                                          |    109 |

## DF1 Master Protocol

## DF1 Point to Point Protocol

The master/slave network includes one controller that is configured as the master node and up to 254 slave nodes. Link slave nodes by using modems or line drivers.

A master/slave network can have node numbers from 0…254. Each node must have a unique node address. Also, at least two nodes, one master and one slave, must exist to define your link as a network.

The DF1 Point to Point protocol is used when connecting from the controller to one DF1 device. DF1 Point to Point protocol is the default System mode protocol. Default parameters are listed in Table 26 .

Table 26 - Default DF1 Point to Point Parameters

| Parameter   | Value   |
|-------------|---------|
| Baud Rate   | 19,200  |
| Data Bits   | 8       |
| Parity      | None    |
| Stop Bits   | 1       |

When configuring the controller for serial communication, you first specify a Serial Port mode (System or User), then a protocol.

Figure 18 - Serial Port Mode in the Controller Properties

<!-- image -->

Table 25 describes the serial communication protocols for use with each mode.

## DF1 Radio Modem Protocol

Table 26 - Default DF1 Point to Point Parameters

| Parameter      | Value        |
|----------------|--------------|
| Control Line   | No Handshake |
| RTS send Delay | 0            |
| RTS Off Delay  | 0            |

Your ControlLogix controller includes a driver that lets it communicate over the DF1 Radio Modem protocol. The DF1 radio modem driver implements a protocol, optimized for use with radio modem networks, that is a hybrid between DF1 full-duplex protocol and DF1 half-duplex protocol, and therefore is not compatible with these protocols.

## IMPORTANT

The DF1 radio modem driver is used only among devices that support and are configured for the DF1 Radio Modem protocol.

Additionally, there are some radio modem network configurations that do not work with the DF1 radio modem driver. In these configurations, continue to use DF1 half-duplex protocol.

Figure 19 - DF1 Radio Modem Network Example

<!-- image -->

Like DF1 full-duplex protocol, the DF1 radio modem lets any node initiate to any other node at any time (that is, if the radio modem network supports fullduplex data-port buffering and radio-transmission collision avoidance). Like DF1 half-duplex protocol, a node ignores any packets received that have a destination address other than its own, except for broadcast packets and passthru packets.

Unlike DF1 full-duplex or DF1 half-duplex protocols, the DF1 radio modem protocol excludes ACKs, NAKs, ENQs, or poll packets. The CRC checksum verifies Data integrity.

## DF1 Radio Modem Advantages

The primary advantage of using the DF1 radio modem protocol for radio modem networks is in transmission efficiency. Each read/write transaction (command and reply) requires only one transmission by the initiator (to send the command) and one transmission by the responder (to return the reply). This efficiency minimizes the number of times the radios must key-up to transmit, which maximizes radio life and minimizes radio power consumption.

In contrast, DF1 half-duplex protocol requires five transmissions for the DF1 master to complete a read/write transaction with a DF1 slave—three by the master and two by the slave.

The DF1 radio modem driver can be used in a pseudo master/slave mode with any radio modems, as long as the designated master node is the only node that initiates MSG instructions, and as long as only one MSG instruction is triggered at a time.

For modern serial radio modems that support full-duplex data port buffering and radio transmission collision avoidance, the DF1 radio modem driver can be used to configure a masterless peer-to-peer radio network, where any node can initiate communication to any other node at any time, as long as the nodes are within radio range so that they receive transmissions from each other.

## DF1 Radio Modem Limitations

These considerations must be made if you can implement the new DF1 radio modem driver in your radio modem network:

- If the devices on the network are ControlLogix controllers, you must configure them with the DF1 radio modem driver via RSLogix 5000® software, version 17.01.02 or later or Logix Designer application, version 21.00.00 or later. If not, then make sure that the nodes can support the DF1 radio modem protocol.

Table 27 - DF1 Radio Protocol Parameters

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Station Address | Specifies the node address of the controller on the serial network. Select a number 1…254 decimal, inclusive. To optimize network performance, assign node addresses in sequential order. Initiators, such as personal computers, are assigned the lowest address numbers to minimize the time that is required to initialize the network.                                                                                                                                                                                                                       |
| Error Detection | Click one of the radio buttons to specify the error detection scheme that is used for all messages. • BCC - the processor sends and accepts messages that end with a BCC byte. • CRC - the processor sends and accepts messages with a 2-byte CRC.                                                                                                                                                                                                                                                                                                               |
|                 | Enable Store and Forward Check ’Enable Store and Forward’ if you want to enable the store and forward functionality. When enabled, the destination address of any received message is compared to the Store and Forward tag table. If there is a match, the message is then forwarded (rebroadcasted) out the port. From the Store and Forward Tag dropdown menu, choose an integer (INT[16]) tag. Each bit is a station address. If this controller reads a message that is destined for a station that has its bit set in this table, it forwards the message. |

- If each node receives the radio transmissions of each other node, being within radio transmission/reception range and on a common receiving frequency (via a Simplex radio mode or via one, common, full-duplex repeater) the radio modems must handle full-duplex data port buffering and radio transmission collision avoidance.

If so, you can take full advantage of the peer-to-peer message initiation capability in each node (for example, the ladder logic in any node can trigger an MSG instruction to any other node at any time).

If not all modems can handle full-duplex data port buffering and radio transmission collision avoidance, you can use the DF1 radio modem driver. Use the DF1 radio modem driver only if you limit MSG instruction initiation to one master node who transmits to each other node.

- If not all nodes receive the radio transmission of each other node, you can use the DF1 radio modem driver. Use the DF1 radio modem driver only if you limit MSG instruction initiation to the node connected to the master radio modem who transmits to each other radio modem in the network.
- You can take advantage of the ControlLogix controller channel-tochannel passthru to program the other nodes via RSLinx® Classic and Logix Designer applications that run on a personal computer that is connected to a local ControlLogix controller via DH-485, DH+™, or Ethernet network.

## DF1 Radio Modem Protocol Parameters

Use Table 27 as a reference when setting the parameters for the use of the DF1 Radio Modem Protocol.

## DF1 Slave Protocol

## DH-485 Protocol

With the DF1 slave protocol, a controller uses DF1 half-duplex protocol. One node is designated as the master and it controls who has access to the link. The other nodes are slave stations and must wait for permission from the master before transmitting.

Make these considerations when using the DF1 Slave protocol:

- If multiple slave stations are used on the network, link slave stations by using modems or line drivers to the master.
- If you are using one slave station on the network, you do not need a modem to connect the slave station to the master.
- Control parameters can be configured without handshaking.
- 2…255 nodes can be connected to one link.

The controller can send and receive messages to and from other controllers on a DH-485 network. The DH-485 connection supports remote programming and monitoring via the Logix Designer application. However, excessive traffic over a DH-485 connection can adversely affect overall controller performance and lead to timeouts and decreased performance of the configuration.

You can also use a 1756-DH485 module to connect the ControlLogix chassis to a DH-485 network with multiple controllers. For more information, see the ControlLogix DH-485 Communication Module User Manual, publication 1756-UM532 .

## IMPORTANT

Use Logix 5000® controllers on DH-485 networks only when you want to add controllers to an existing DH-485 network.

For new applications with Logix 5000 controllers, we recommend that you use networks in the NetLinx open architecture.

The DH-485 protocol uses RS-485 half-duplex as its physical interface. RS-485 is a definition of electrical characteristics, not a protocol. You can configure the RS-232 port of the ControlLogix controller to act as a DH-485 interface.

To connect the controller to the DH-485 network, you must use these components:

- A 1761-NET-AIC converter (two controllers can be connected to one converter)
- An RS-232 cable (catalog number 1756-CP3 or 1747-CP3) for each controller to connect to the converter

## ASCII Protocol

Figure 20 - DH-485 Network Communication Overview

<!-- image -->

44136

IMPORTANT A DH-485 network consists of multiple cable segments. Limit the total length of the segments to 1219 m (4000 ft).

When you configure the serial port for User mode and the ASCII protocol, you can use it to do the following:

- Read ASCII characters from a weigh scale module or barcode reader.
- Send and receive messages from an ASCII-triggered device, such as a MessageView™ terminal.

## Configure the ControlLogix 5560 Controller for Serial Communication

After you configure the controller for use with the ASCII protocol, program the controller by using the ASCII instructions. Reference the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003, for information about the ASCII instructions.

Complete these steps to configure your 1756-L6x controller for serial communication after creating a controller project in the Logix Designer application.

1. Open the Controller Properties and click the Serial Port tab.
2. From the Mode dropdown menu, choose the mode that corresponds to your intended protocol.

<!-- image -->

Use this table as a reference.

| For this protocol   | Choose this mode   |
|---------------------|--------------------|
| DF1 Master          | System             |
| DF1 Point to Point  |                    |
| DF1 Radio Modem     |                    |
| DF1 Slave           |                    |
| DH-485              |                    |
| ASCII               | User               |

3. Specify the remaining properties in the Serial Port tab according to your communication preferences.
4. If you are using the System mode protocols, click the System Protocol tab and specify the protocol parameters.
- a. From the Protocol dropdown, choose the protocol that you need.
- b. Specify the parameters for the protocol.
5. If you are using the User mode protocol (ASCII), click the User Protocol tab and specify the ASCII parameters.

<!-- image -->

<!-- image -->

<!-- image -->

## Broadcast Messages Over a Serial Port

After you have configured the controller for ASCII protocol communication, reference the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003, for the available ASCII instructions.

You can broadcast messages over a serial port connection from a master controller to its slave controllers by using several communication protocols. These protocols include the following:

- DF1 Master
- DF1 Radio Modem
- DF1 Slave

Use the 'message' tag to broadcast over a serial port. Because messages are sent to receiving controllers, only the 'write' type messages can be used for broadcasting.

The broadcast feature can be configured by using ladder logic or structured text. The broadcast feature can also be set by modifying the path value of a message tag in the tag editor.

To configure and program the controller to broadcast messages via the serial port, complete these procedures:

- Configure Controller Serial Port Properties on page 113
- Program the Message Instruction on page 114

For these procedure examples, ladder logic programming is used.

## Configure Controller Serial Port Properties

First, set the System Protocol by following these steps.

1. In the Controller Organizer, right-click the controller and choose Properties.
2. In the Controller Properties dialog box, from the System Protocol tab, choose the settings for the controller and click OK.

<!-- image -->

## Modbus Support

Use this table when specifying settings for the protocols listed.

| Field                        | DF-1 Master Protocol                                                                                                                                       | DF-1 Slave Protocol                                                                                   | DF-1 Radio Modem Protocol                                                                                                                                                                                                                                                                     |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Station Address              |                                                                                                                                                            | Controller station address number Controller station address number Controller station address number |                                                                                                                                                                                                                                                                                               |
| Transmit Retries             | 3                                                                                                                                                          | 3                                                                                                     | N/A                                                                                                                                                                                                                                                                                           |
| ACK Timeout                  | 50                                                                                                                                                         | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                           |
| Slave Poll Timeout           | N/A                                                                                                                                                        | 3000                                                                                                  | N/A                                                                                                                                                                                                                                                                                           |
| Reply Message Wait 5         |                                                                                                                                                            | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                           |
| Polling Mode                 | Message: polls the slave by using the message instruction Slave: initiates messages for slave-to-slave broadcast Standard: schedules polling for the slave | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                           |
| EOT Suppression              | N/A                                                                                                                                                        | Disable                                                                                               | N/A                                                                                                                                                                                                                                                                                           |
| Error Detection              | BCC                                                                                                                                                        | BCC                                                                                                   | BCC                                                                                                                                                                                                                                                                                           |
| Duplicate Detection Enabled  |                                                                                                                                                            | Enabled                                                                                               | N/A                                                                                                                                                                                                                                                                                           |
| Enable Store and Forward N/A |                                                                                                                                                            | N/A                                                                                                   | Choose enable if you want to use the store and forward tag. The last bit of the INT[16] Enable Store and Forward array must be ’enabled.’ For example, say that you create an INT[16] tag named EnableSandF. Then EnableSandF[15].15 must be set to 1 for broadcast to work on a radio modem. |

## Program the Message Instruction

Add and configure the message instruction according to the protocol you are using. For more information to specify the configuration details, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

| IMPORTANT   | When using structured text, broadcast over a serial port is set by typing MSG(aMsg) and right-clicking an MSG to display the Message Configuration dialog box.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

To use ControlLogix controllers with the Modbus protocol, establish a serial port connection and execute a ladder-logic routine.

Two controller projects specific to the Modbus network are available as sample programs within the Logix Designer application:

- ModbusMaster.ACD
- ModbusSlave.ACD

For information about using these sample programs, see the Using Logix 5000 Controllers as Masters or Slaves on Modbus Application Solution, publication CIG-AP129 .

## Connection Overview

## Produce and Consume (Interlock) Data

<!-- image -->

## Manage Controller Communication

A Logix 5000® system uses a connection to establish a communication link between two devices. The types of connections include the following:

- Controller-to-local I/O modules or local communication modules
- Controller-to-remote I/O or remote communication modules
- Controller-to-remote I/O (rack-optimized) modules
- Produced and consumed tags
- Messages
- Controller access via the Studio 5000 Logix Designer® application
- Controller access via RSLinx® Classic or FactoryTalk® Linx applications for HMI or other applications

ControlLogix® controllers let you produce (transmit) and consume (receive) system-shared tags.

Figure 21 - Illustration of Produced and Consumed Tags

<!-- image -->

The system-shared tags are explained in Table 28 .

Table 28 - Produced and Consumed Tag Definitions

| Tag Definition                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produced tag A tag that a controller makes available for use by other controllers. Multiple controllers can simultaneously consume (receive) the data. A produced tag sends its data to one or more consumed tags (consumers) without using logic.         |
| Consumed tag A tag that receives the data of a produced tag. The data type of the consumed tag must match the data type (including any array dimensions) of the produced tag. The RPI of the consumed tag determines the period at which the data updates. |

For two controllers to share produced or consumed tags, the controllers must be attached to the same network. You cannot bridge produced and consumed tags over two networks.

Produced and consumed tags use connections of the controller and the communication modules being used. For a ControlNet® network, produced and consumed tags use scheduled connections.

## Connection Requirements of a Produced or Consumed Tag

Produced and consumed tags each require connections. As you increase the number of controllers that can consume a produced tag, you reduce the number of connections the controller has available for other operations, like communication and I/O.

## IMPORTANT

If a consumed-tag connection fails, the other tags being consumed from that remote controller stop receiving new data.

Each produced or consumed tag uses the number of connections that are listed in Table 29. Adding status information to a produced/consumed tag does not affect the number of connections used.

.

Table 29 - Produced and Consumed Tag Connections

| This Type of Tag           | Uses This Many Connections                   | Of This Module   |
|----------------------------|----------------------------------------------|------------------|
| Produced tag               | number_of_configuredconsumers + 1 Controller |                  |
| Consumed tag               | 1                                            |                  |
| Produced or consumed tag 1 |                                              | Communication    |

## EXAMPLE

Calculations of connections for produced or consumed tags:

- A ControlLogix controller producing 4 tags for 1 controller uses 8 connections.

Each tag uses 2 connections (1 consumer + 1 = 2).

2 connections per tag x 4 tags = 8 connections.

- Consuming 4 tags from a controller uses 4 connections (1 connection per tag x 4 tags = 4 connections).

The number of available connections limits the number of tags that can be produced or consumed. If the controller uses its connections for I/O and communication devices, no connections are left for produced and consumed tags.

Table 30 - ControlLogix Modules and Available Connections

| Module Type Cat. No.   |                                                                 |   Available Connections |
|------------------------|-----------------------------------------------------------------|-------------------------|
| Controller             | 1756-L7x                                                        |                     500 |
|                        | 1756-L6x                                                        |                     250 |
|                        | EtherNet/IP™ • 1756-EN2F • 1756-EN2T • 1756-EN2TXT • 1756-EN2TR |                     256 |
|                        | • 1756-ENBT • 1756-EWEB                                         |                     128 |
| ControlNet             | • 1756-CN2 • 1756-CN2R • 1756-CN2RXT                            |                     128 |
|                        | • 1756-CNB • 1756-CNBR                                          |                      64 |

For more information about produced/consumed tags, see the Logix 5000 Controllers Produced and Consumed Tags Programming Manual, publication 1756-PM011 .

## Send and Receive Messages

Messages transfer data to other devices, such as other controllers or operator interfaces. The MSG instruction is a ladder logic output instruction that asynchronously reads or writes a block of data to or from another module over the backplane or a network. The size of the instruction depends on the data types and message command that you program.

Messages use connection resources to send or receive data. Messages can leave the connection open (cache) or closed when the message is done transmitting.

Each message uses one connection out of the controller, regardless of how many devices are in the message path. To conserve connections, configure one message to read from or write to multiple devices.

Table 31 - Message Types

| Message Type                                | Communication Method       | Connected Message Message Can Be   | Cached   |
|---------------------------------------------|----------------------------|------------------------------------|----------|
| CIP™ data table read or write N/A           |                            | Configurable Yes                   |          |
| PLC-2®, PLC-3®, PLC-5®, or SLC™ (all types) | CIP  CIP with Source ID No | No                                 | No No    |
| PLC-2®, PLC-3®, PLC-5®, or SLC™ (all types) | DH+™                       | Yes                                | Yes      |
| CIP generic                                 | N/A                        | Optional  (1)                      | Yes(2)   |
| Block-transfer read or write N/A            |                            | Yes                                | Yes      |

For more information about using messages, see these publications:

- Logix 5000 Controllers Messages, publication 1756-PM012
- Logix 5000 Controllers General Instructions, publication 1756-RM003

## Determine Whether to Cache Message Connections

When you configure an MSG instruction, you can choose whether to cache the connection. Use Table 32 to determine options for caching connections.

.

Table 32 - Options for Caching Connections

| If the message executes Then   |                                                                                                                                                                  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repeatedly                     | Cache the connection. This keeps the connection open and optimizes execution time. Opening a connection each time the message executes increases execution time. |
| Infrequently                   | Do not cache the connection. This closes the connection upon completion of the message, which frees up that connection for other uses.                           |

TIP Cached connections transfer data faster than uncached connections. The controller supports only 32 cached messages.

## Calculate Connection Use

Table 33 - Local Chassis Connections

| Local Connection To                                                                                                              | Device Quantity Connections per Device   | Total Connections   |
|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------|
| Local I/O module (a direct connection)                                                                                           | 1                                        |                     |
| 1756-M16SE, 1756-M08SE, or 1756-M02AE servo module                                                                               | 3                                        |                     |
| • 1756-CN2, 1756-CN2R, 1756-CN2RXT ControlNet communication module • 1756-CNB, 1756-CNBR ControlNet communication module         | 0                                        |                     |
| • 1756-EN2F, 1756-EN2T, 1756-EN2TXT, or 1756-EN2TR EtherNet/IP communication module • 1756-ENBT EtherNet/IP communication module | 0                                        |                     |
| 1756-EWEB EtherNet/IP web server module                                                                                          | 0                                        |                     |
| 1756-DNB DeviceNet® communication module                                                                                         | 2                                        |                     |
| 1756-RIO remote I/O communication module (Connection count depends on module configuration and can be as many as 10 per module.) | 1                                        |                     |
| 1756-DHRIO DH+/universal remote I/O communication module Each adapter that is associated with the module                         | 1 1                                      |                     |
| 1756-DHRIOXT DH+/universal remote I/O communication module Each adapter that is associated with the module                       | 1 1                                      |                     |
| 1756-DH-485 DH-485 communication module                                                                                          | 1                                        |                     |
|                                                                                                                                  |                                          | Total               |

The total connection requirements of a ControlLogix system include local and remote connections.

## Local Connections

Local connections refer to connections used to communicate between modules that are housed in the same ControlLogix chassis (that is, the local modules). Use Table 33 to calculate the number of local connections that are based on the configuration of your local chassis.

Table 34 - Remote Connections

| Remote Connection Type                                                                                                         | Device Quantity Connections per Device   | Total Connections   |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------|
| Remote ControlNet communication module I/O configured as direct connection (none) I/O configured as rack-optimized connection  | 0 1                                      |                     |
| Remote I/O module over a ControlNet network (direct connection)                                                                | 1                                        |                     |
| Remote EtherNet/IP communication module I/O configured as direct connection (none) I/O configured as rack-optimized connection | 0 1                                      |                     |
| Remote I/O module over a EtherNet/IP network (direct connection)                                                               | 1                                        |                     |
| Remote device over a DeviceNet network (accounted for in rack-optimized connection for local 1756-DNB)                         | 0                                        |                     |
| DeviceNet module in a remote chassis                                                                                           | 2                                        |                     |
| Other remote communication adapter                                                                                             | 1                                        |                     |
| Produced tag Each consumer                                                                                                     | 1 1                                      |                     |
| Consumed tag                                                                                                                   | 1                                        |                     |
| Message (see Table 31 for message types) Connected Unconnected                                                                 | 1 0                                      |                     |
| Block transfer message                                                                                                         | 1                                        |                     |
| Total                                                                                                                          | Total                                    | Total               |

## Remote Connections

Use remote connections when the communication module is in a chassis that is remote from the controller. The number of connections a communication module supports determines how many remote connections the controller can access through that module.

Table 35 - Connections Example Calculation

| Connection Type                               |     | Device Quantity Connections per Device   | Total Connections   |
|-----------------------------------------------|-----|------------------------------------------|---------------------|
| Controller to local I/O modules               | 4   | 1                                        | 4                   |
| Controller to 1756-ENBT module                | 1   | 0                                        | 0                   |
| Controller to 1756-DNB module                 | 1   | 2                                        | 2                   |
| Controller to Logix Designer application      | 1   | 1                                        | 1                   |
| Message to CompactLogix controller            | 2   | 1                                        | 2                   |
| Produced tag Consumed by FlexLogix controller | 1 1 | 1 1                                      | 1 1                 |
| Total                                         |     |                                          | 11                  |

## Connections Example

In this example system, the 1756 ControlLogix controller does the following:

- Controls local digital I/O modules in the same chassis
- Controls remote I/O devices on a DeviceNet network
- Sends and receives messages to and from a CompactLogix® controller on an EtherNet/IP network
- Produces one tag that the 1794 FlexLogix™ controller consumes
- Is programmed via the Logix Designer application

<!-- image -->

The ControlLogix controller in this example uses these connections.

## Notes:

## Selecting ControlLogix I/O Modules

## Local I/O Modules

## I/O Modules

Rockwell Automation offers several ControlLogix® I/O modules for use in ControlLogix systems. When you select your I/O modules, remember the following:

- A wide variety of digital, analog, and specialty I/O modules are available from Rockwell Automation. Some features of these I/O modules include the following:
- – Field-side diagnostics
- – Electronic fusing
- – Individually isolated inputs/outputs
- Removable terminal blocks (RTBs) or 1492 wiring systems are required for use with I/O modules.
- 1492 PanelConnect™ modules and cables can be used to connect input modules to sensors.

For more information about ControlLogix I/O module features, specifications, and wiring options, see the ControlLogix System Selection Guide, publication 1756-SG001 .

The ControlLogix chassis that you choose affects how many local I/O modules you can use. Several ControlLogix chassis sizes are available to suit your configuration requirements. You can fill the slots of your chassis with any combination of controllers, communication modules, and I/O modules.

Table 36 lists the available ControlLogix and ControlLogix-XT™ chassis and the number of slots available with each.

<!-- image -->

Table 36 - ControlLogix and ControlLogix-XT™ Chassis and Slots

| Chassis    | Slots   |
|------------|---------|
| 1756-A4    | 4       |
| 1756-A4LXT |         |
| 1756-A5XT  | 5       |
| 1756-A7    | 7       |
| 1756-A7LXT |         |
| 1756-A7XT  |         |
| 1756-A10   | 10      |
| 1756-A10XT |         |
| 1756-A13   | 13      |
| 1756-A17   | 17      |

If you have empty slots in your chassis, use the 1756-N2 or 1756-N2XT slot-filler module.

## Add Local I/O to the I/O Configuration

If you are adding local I/O, add the I/O module to the backplane with the controller. To add an I/O module to the local chassis, complete these steps.

1. Right-click the backplane and choose New Module.
2. Select the I/O module that you want to add and click OK.

<!-- image -->

<!-- image -->

## Remote I/O Modules

3. Specify the configuration properties according to the module and network configuration you are using.

See the Additional Resources section in the preface for more information if you are designing your ControlLogix System for any of the following modules:

- Analog I/O
- Configurable flowmeter
- Digital I/O
- HART analog I/O
- High-speed analog I/O
- High-speed counter
- Low-speed counter
- Programmable limit switch

Remote I/O refers to I/O that is not in the local chassis and is connected to the controller via a communication network.

The ControlLogix controller supports the use of remote I/O via these networks:

- EtherNet/IP™
- ControlNet®
- DeviceNet®
- Universal remote I/O

For more information about the network configurations that can be used to connect remote I/O, see Communication Networks on page 87 .

Figure 22 - ControlLogix Controller and Remote I/O Example

ControlLogix Controller Chassis

<!-- image -->

## Add Remote I/O to the I/O Configuration

If you are adding remote I/O, add the I/O modules to the backplane of the remote communication module that is connected to the controller. To add a remote I/O to the I/O Configuration folder in the Logix Designer application, complete these steps.

1. Add a communication module to the backplane that contains the controller.
2. Specify the communication module properties according to your network configuration.

<!-- image -->

For more information about the communication module and network properties, see the Additional Resources section in the preface.

3. Right-click the communication network and choose New Module.

<!-- image -->

4. Add the remote communication module that you are using.
5. Specify the chassis and connection properties according to your network configuration.
6. Right-click the backplane of the newly added communication module and choose New Module.
7. Select the I/O module that you want to add and click OK.

<!-- image -->

<!-- image -->

<!-- image -->

8. Specify the Module Properties according to your module and application.

See the Additional Resources section in the preface for more information about the module configuration properties for any of the following modules:

- Analog I/O
- Configurable flowmeter
- Digital I/O
- HART analog I/O
- High-speed analog I/O
- High-speed counter
- Low-speed counter
- Programmable limit switch
9. Add any other I/O modules that you are using in the remote chassis.
10. Complete steps 1 … 9 until your remote I/O network and I/O modules are configured.

<!-- image -->

## Distributed I/O

Distributed I/O refers to I/O that is remote from the controller and is not designed for use with a specific controller. Examples of distributed I/O that can be used with Logix 5000® controllers include the following:

- 1794 FLEX™ I/O modules
- 1734 POINT I/O™ modules
- 1797 FLEX Ex™ I/O modules
- 1738 ArmorPOINT® I/O modules
- 1732 ArmorBlock® I/O modules
- 1753 GuardPLC™ Safety I/O modules
- 1790 CompactBlock™ LDX I/O modules
- 1791 CompactBlock Guard Safety I/O modules
- 1791 CompactBlock I/O modules
- 1732DS ArmorBlock Guard Safety I/O modules
- 1792 ArmorBlock MaXum™ I/O modules

Distributed I/O is connected to the ControlLogix controller via a communication network. The ControlLogix controller supports the use of distributed I/O via these networks:

- EtherNet/IP
- ControlNet
- DeviceNet

Figure 23 - ControlLogix System with Distributed I/O Example

ControlLogix Controller Chassis

<!-- image -->

## Add Distributed I/O to the I/O Configuration

If you are adding distributed I/O, add the I/O modules to the communication adapter of the I/O. To add distributed I/O to the I/O Configuration folder for the ControlLogix controller, complete these steps.

1. Add a communication module to the backplane that contains the controller.
2. Specify the communication module properties according to your network configuration.

<!-- image -->

For more information about the communication module and network properties, see the Additional Resources section in the preface.

3. Right-click the communication network and choose New Module.

<!-- image -->

4. Add the communication adapter for the distributed I/O platform that you are using.
5. Specify the module and connection properties according to your network configuration.
6. Right-click the bus of the newly added communication adapter and choose New Module.
7. Select the I/O module that you want to add and click OK.

<!-- image -->

<!-- image -->

<!-- image -->

## Reconfigure an I/O Module

8. Specify the Module Properties according to your module and application.

For more information about the module configuration properties, see the user manual for the I/O module you are adding.

9. Add any other I/O modules that you are using in this bus.
10. Complete steps 1 … 9 until your remote I/O network and distributed I/ O modules are configured.

If an I/O module supports reconfiguration, you can reconfigure the module via the following:

- The Module Properties dialog box in the I/O Configuration folder
- An MSG instruction in program logic

## IMPORTANT

Use care when changing the configuration of an I/O module. You can inadvertently cause the I/O module to operate incorrectly.

Use an MSG instruction of type Module Reconfigure to send new configuration information to an I/O module. During the reconfiguration, consider the following:

- Input modules continue to send input data to the controller
- Output modules continue to control their output devices

## Reconfigure an I/O Module Via the Module Properties

To reconfigure an I/O module by using the module properties, right-click the module in the I/O Configuration tree and choose Properties. Then, edit the properties that you must change and click Apply.

<!-- image -->

<!-- image -->

## EXAMPLE

## Reconfigure an I/O module

When reconfigure[5] is on, the MOV instruction sets the high alarm to 60 for the local module in slot 4. The Module Reconfigure message then sends the new alarm value to the module. The ONS instruction does not allow the rung to send multiple messages to the module while the reconfigure[5] is on.

<!-- image -->

For more information about using message instructions, see the Logix 5000 Controllers General Instruction Reference Manual, publication 1756-RM003 .

With RSLogix 5000 software, version 15.02.00 or later, and Logix Designer application, version 21.00.00 or later, you can add I/O and other devices to the controller configuration while you are online and in Run mode.

The modules and devices you can add while online depends on the version of the software you are using. Later versions have more modules and devices that can be added while online.

You can add these modules and devices to the local or remote chassis via the unscheduled portion of a ControlNet network or via an EtherNet/IP network.

## Add to the I/O Configuration While Online

## Reconfigure an I/O Module Via a Message Instruction

To reconfigure an I/O module via a message instruction, use this procedure.

1. Set the required member of the configuration tag of the module to the new value.
2. Send a Module Reconfigure message to the module.

## Modules and Devices That Can Be Added While Online

These modules and devices can be added to the ControlLogix controller I/O configuration while online as of RSLogix 5000® software, version 19.01.00 or later and Logix Designer application, version 21.00.00 or later.

- 1756 controllers
- 1756 ControlNet modules
- 1756 DeviceNet bridges
- 1756 EtherNet/IP modules
- 1756 I/O and specialty modules
- 1756-DHRIO
- 1756-DHRIOXT

## IMPORTANT

These ControlLogix modules cannot be added while online:

- Motion modules (1756-MO2AE, 1756-HYD02, 1756-MO2AS, 1756-MO3SE, 1756-MO8SE, 1756-MO8SEG, 1756-M16SE)
- 1756-RIO
- 1756-SYNCH
- 1756-56AMXN

## Online Additions - ControlNet Considerations

ControlNet considerations that must be made depend upon the ControlLogix ControlNet modules you are using.

## 1756-CNB and 1756-CNBR Modules

When you add I/O to the ControlNet network via the 1756-CNB or 1756-CNBR modules while online, these considerations must be made:

- Digital I/O modules can be added as rack-optimized connections if the parent module is configured with rack-optimized connections.

TIP While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online.

- Digital I/O modules can also be added as direct connections.
- Analog I/O modules can be added only as direct connections.
- Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI.

- If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or none of the following:
- – HMI traffic
- – MSG traffic
- – Programming workstations
- Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations:
- – Use a NUT of 10 ms or more.
- – Keep the SMAX and UMAX values as small as possible.
- If the module has a Real Time Sample (RTS), disable it or set it to a rate that is greater than the RPI.
- You can add I/O modules until you reach these limits:
- – 75% of CPU utilization of the 1756-CNB or 1756-CNBR communication module
- – Plan for a CPU-use increase of 1…4% of the 1756-CNB or 1756-CNBR module for each I/O module you add, depending on the RPI.
- – 48 connections on the 1756-CNB or 1756-CNBR communication module
- – Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet™ software after the network has been scheduled.

## 1756-CN2, 1756-CN2R, 1756-CN2RXT Modules

The use of 1756-CN2/B, 1756-CN2R/B, and 1756-CN2RXT modules provides increased capacity for adding I/O while online compared to 1756-CNB or 1756-CNBR modules. With this increased capacity, you can easily add I/O and increase ControlNet connections that are used with less impact on the overall system.

Table 37 demonstrates the performance factors of the 1756-CN2/B, 1756-CN2R/B, and 1756-CN2RXT modules when adding I/O online.

Table 37 - 1756-CN2, 1756-CN2R, and 1756-CN2RXT Performance Example (1)

| No. of Direct Analog I/O Connections Added Online   |    |                                                                     |    |    |    |    |
|-----------------------------------------------------|----|---------------------------------------------------------------------|----|----|----|----|
| No. of Direct Analog I/O Connections Added Online   | Avg. (3 g API(3)    | CPU %(2)  CPU %(2)  Avg. (3 g API(3) CPU %(2)  CPU %(2)  CPU %(2)  CPU %(2)                                                                     | Avg. (3 g API(3)    | Avg. (3 g API(3)    | Avg. (3 g API(3)    | Avg. (3 g API(3)    |
| 0                                                   |    | 1.50% N/A 1.50% N/A 1.50% N/A 1.50% N/A 1.50% N/A 1.50% N/A         |    |    |    |    |
| 1                                                   |    | 4.80% 2.0 3.70% 4.0 2.50% 10.0 2.30% 20.0 1.90% 50.0 1.70% 100.0    |    |    |    |    |
| 2                                                   |    | 7.00% 2.0 5.00% 4.0 3.30% 10.0 2.70% 20.0 2.10% 50.0 1.90% 100.0    |    |    |    |    |
| 3                                                   |    | 9.00% 2.0 6.10% 4.0 3.80% 10.0 3.00% 20.0 2.20% 50.0 2.00% 100.0    |    |    |    |    |
| 4                                                   |    | 11.20% 2.2 7.40% 4.0 4.40% 10.0 3.40% 20.0 2.40% 50.0 2.10% 100.0   |    |    |    |    |
| 5                                                   |    | 11.50% 3.3 8.70% 4.0 5.00% 10.0 3.70% 20.0 2.60% 50.0 2.20% 100.0   |    |    |    |    |
| 6                                                   |    | 12.80% 3.3 9.70% 4.0 5.50% 10.0 4.00% 20.0 2.70% 50.0 2.30% 100.0   |    |    |    |    |
| 7                                                   |    | 13.80% 3.4 10.80% 4.0 5.90% 10.0 4.30% 20.0 2.90% 50.0 2.30% 100.0  |    |    |    |    |
| 8                                                   |    | 15.10% 3.4 11.90% 4.0 6.40% 10.0 4.50% 20.0 3.00% 50.0 2.50% 100.0  |    |    |    |    |
| 9                                                   |    | 15.00% 3.3 13.20% 4.0 7.00% 10.0 4.80% 20.0 3.20% 50.0 2.60% 100.0  |    |    |    |    |
| 10                                                  |    | 15.60% 3.6 13.20% 4.0 7.50% 10.0 5.20% 20.0 3.40% 50.0 2.70% 100.0  |    |    |    |    |
| 11                                                  |    | 16.40% 3.8 13.50% 4.0 8.20% 10.0 5.50% 20.0 3.50% 50.0 2.70% 100.0  |    |    |    |    |
| 12                                                  |    | 17.00% 3.8 14.00% 4.0 8.80% 10.0 5.80% 20.0 3.70% 50.0 2.80% 100.0  |    |    |    |    |
| 13                                                  |    | 17.80% 3.7 14.60% 4.0 9.30% 10.0 6.10% 20.0 3.80% 50.0 2.90% 100.0  |    |    |    |    |
| 14                                                  |    | 18.50% 3.7 15.20% 4.0 9.90% 10.0 6.40% 20.0 4.00% 50.0 2.90% 100.0  |    |    |    |    |
| 15                                                  |    | 19.40% 3.9 15.80% 4.0 10.50% 10.0 6.70% 20.0 4.10% 50.0 3.00% 100.0 |    |    |    |    |

Because of the increased performance that is provided by the 1756-CN2, 1756-CN2R, and 1756-CN2RXT modules, many of the considerations that must be made with the 1756-CNB and 1756-CNBR modules are not applicable. With the 1756-CN2, 1756-CN2R, and 1756-CN2RXT modules, you can add I/O while online as long as you use reasonable RPI settings and remain within the CPU limitations of the ControlNet module.

When adding to the I/O Configuration with 1756-CN2, 1756-CN2R, and 1756-CN2RXT modules, make these considerations:

- Digital I/O modules can be added as rack-optimized connections if the parent module is configured with rack-optimized connections.

TIP While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online.

- Digital I/O modules can also be added as direct connections.
- Analog I/O modules can be added only as direct connections.
- Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI.

- If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or none of the following:
- – HMI traffic
- – MSG traffic
- – Programming workstations
- If the module has a Real Time Sample (RTS), disable it or set it to a rate that is greater than the RPI.
- You can add I/O modules until you reach these limits:
- – 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module.
- – Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx for ControlNet software after the network has been scheduled.

## Online Additions—EtherNet/IP Considerations

When you add I/O modules to the EtherNet/IP network, make these considerations:

- The EtherNet/IP I/O modules that you add can be added as these connection types:
- – Rack-optimized connections, including new and existing connections
- – Direct connections
- You can add I/O modules until you reach the limits of the communication connections of the module.

For EtherNet/IP module limitations, see the EtherNet/IP Modules in Logix 5000 Control Systems User Manual, publication ENET-UM001 .

## Determine When Data Is Updated

ControlLogix controllers update date asynchronously with the execution of logic. Use this flowchart to determine when a producer, such as a controller, input module, or bridge, sends data.

Figure 24 - Data Update Flowchart

<!-- image -->

- Over a ControlNet network, remote data is sent at the actual packet interval.
- Over an EtherNet/IP network, remote data is sent close to the RPI.

## Notes:

## Motion Control Options

## Develop Motion Applications

ControlLogix® controllers support digital, analog, and Integrated Motion interfaces:

- Digital drive interfaces include EtherNet/IP™ connected drives and Sercos interface connected drives.
- Analog drives support ±10V analog output and can interface with various feedback device types including quadrature encoder, SSI, and LVDT feedback.
- Integrated Motion on an EtherNet/IP network supports Kinetix® 350, Kinetix 5500, Kinetix 6500, and PowerFlex® 755 drives.

<!-- image -->

## Motion Overview

## Obtain Axis Information

The configuration process varies, depending on your application and your drive selection. The following are general steps to configure a motion application.

1. Create a controller project.
2. Select the type of drive.
3. Create axis tags as needed.
4. Configure the drive.
5. Create axes as needed.

| Drive Type       | Requirements                                                                      |
|------------------|-----------------------------------------------------------------------------------|
| CIP Sync™        | • EtherNet/IP communication module • Digital drive with an EtherNet/IP connection |
| Sercos interface | Select a Sercos interface module: • 1756-M03SE • 1756-M08SE • 1756-M16SE          |
| Analog interface | Select an analog interface module: • 1756-HYD02 • 1756-M02AE • 1756-M02AS         |

You can obtain axis information by using these methods:

- Double-click the axis to open the Axis Properties dialog box.
- Use a Get System Value (GSV) or Set System Value (SSV) instruction to read or change the configuration at runtime.
- View the Quick View pane to see the state and faults of an axis.
- Use an axis tag for status and faults.

Figure 25 - Obtain Axis Information

<!-- image -->

## Program Motion Control

The controller provides a set of motion control instructions for your axes:

- The controller uses these instructions just like the rest of the Logix 5000® instructions.
- Each motion instruction works on one or more axes.
- Each motion instruction needs a motion control tag. The tag uses a MOTION\_INSTRUCTION data type and stores the information status of the instruction.
- You can program by using motion control instructions in these programming languages:
- – Ladder Diagram (LD)
- – Structured Text (ST)
- – Sequential Function Chart (SFC)

Figure 26 - Motion Control Instruction

<!-- image -->

<!-- image -->

ATTENTION: Use the tag for the motion control operation of motion instruction only once. Unintended operation of the control variables can happen if you reuse of the same motion control tag in other instructions.

## Example

In this example, a simple ladder diagram that homes, jogs, and moves an axis.

If Initialize\_Pushbutton = on and the axis = off (My\_Axis\_X.ServoActionStatus = off) then the MSO instruction turns on the axis .

<!-- image -->

## Elements of a Control Application

## Tasks

## Develop Applications

A control application is composed of several elements that require planning for efficient application execution. Application elements include the following:

- Tasks
- Programs
- Routines
- Parameters and Local Tags

Figure 27 - Elements of a Control Program

<!-- image -->

A Logix 5000® controller lets you use multiple tasks to schedule and prioritize the execution of your programs based on criteria. This multitasking allocates the processing time of the controller among the operations in your application:

- The controller executes only one task at a time.
- One task can interrupt the execution of another and take control.

- In any given task, multiple programs can be used. However, only one program executes at a time.
- You can display tasks in the Controller or Logical Organizer views, as necessary.

Figure 28 - Task Within a Control Application

<!-- image -->

Figure 29 - Tasks

<!-- image -->

Table 38 - Task Types and Execution Frequency

| Task Type Task Execution                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous Constant                                                                                    | The continuous task runs in the background. Any CPU time that is not allocated to other operations (such as motion, communication, and other tasks) is used to execute the programs in the continuous task. • The continuous task runs constantly. When the continuous task completes a full scan, it restarts immediately. • A project does not require a continuous task. If used, there can be only one continuous task.                                                         |
| Periodic • At a set interval, such as each 100 ms • Multiple times within the scan of your other logic | A periodic task performs a function at an interval. • Whenever the time for the periodic task expires, the task interrupts any lower priority tasks, executes once, and returns control to where the previous task left off. • You can configure the time period from 0.1…2,000,000.00 ms. The default is 10 ms. It is also controller and configuration dependent. • The performance of a periodic task depends on the type of Logix 5000 controller and on the logic in the task. |
|                                                                                                        | Event Immediately when an event occurs An event task performs a function only when an event (trigger) occurs. The trigger for the event task can be the following: • Module input data change of state • A consumed tag trigger • An EVENT instruction • An axis trigger • A motion event trigger                                                                                                                                                                                   |

The ControlLogix® controller supports up to 32 tasks, only one of which can be continuous.

A task can have up to 1000 programs, starting with the Logix Designer application, version 24.00.00 and later, each with its own executable routines and program-scoped tags. Once a task is triggered (activated), the programs that are assigned to the task execute in the order in which they are grouped. Programs can appear only once in the Controller Organizer and multiple tasks cannot share them.

A task provides scheduling and priority information for a set of one or more programs. Configure tasks as continuous, periodic, or event by using the Task Properties dialog box.

Figure 30 - Configuring the Task Type

<!-- image -->

Table 38 explains the types of tasks that you can configure.

## Programs

## Task Priority

Each task in the controller has a priority level. The operating system uses the priority level to determine which task to execute when multiple tasks are triggered. A higher priority task interrupts any lower priority task. The continuous task has the lowest priority and a periodic or event task interrupts it.

You can configure periodic and event tasks to execute from the lowest priority of 15 up to the highest priority of 1. Configure the task priority by using the Task Properties dialog box.

Figure 31 - Configure Task Priority

<!-- image -->

The controller operating system is a preemptive multitasking system that is in compliance with IEC 1131-3. This system provides the following:

- Programs to group data and logic
- Routines to encapsulate executable code that is written in one programming language

Each program contains the following:

- Local Tags
- Parameters
- A main executable routine
- Other routines
- An optional fault routine

Figure 32 - Program Within a Control Application

Figure 33 - Programs

<!-- image -->

Controller Organizer

<!-- image -->

Logical Organizer

## Scheduled and Unscheduled Programs

The scheduled programs within a task execute to completion from first to last. Programs that are not attached to any task show up as unscheduled programs.

Unscheduled programs within a task are downloaded to the controller with the entire project. The controller verifies unscheduled programs but does not execute them.

You must schedule a program within a task before the controller can scan the program. To schedule an unscheduled program, use the Program/ Phase Schedule tab of the Task Properties dialog box.

Figure 34 - Scheduling an Unscheduled Program

<!-- image -->

## Routines

A routine is a set of logic instructions in one programming language, such as Ladder Diagram (ladder logic). Routines provide the executable code for the project in a controller. A routine is similar to a program file or subroutine in a PLC or SLC™ processor.

Each program has a main routine. The main is the first routine to execute when the controller triggers the associated task and calls the associated program. Use logic, such as the Jump to Subroutine ( JSR) instruction, to call other routines.

You can also specify an optional program fault routine. The controller executes this routine if it encounters an instruction-execution fault within any of the routines in the associated program.

Figure 35 - Routines in a Control Application

<!-- image -->

Figure 36 - Routines

<!-- image -->

## Parameters and Local Tags

With a Logix 5000 controller, you use a tag (alphanumeric name) to address data (variables). In Logix 5000 controllers, there is no fixed, numeric format. The tag name identifies the data and lets you do the following:

- Organize your data to mirror your machinery.
- Document your application as you develop it.

This example shows data tags that are created within the scope of the Main Program of the controller.

Figure 37 - Tags Example

Controller Organizer —Main Program Parameters and Local Tags

<!-- image -->

## Program Tags Window—Main Program Parameters and Local Tags

<!-- image -->

There are several guidelines for creating and configuring parameters and local tags for optimal task and program execution. For more information, see the Logix 5000 Controllers and I/O Tag Data Programming Manual, publication 1756-PM004 .

## Extended Properties

The Extended Properties feature lets you define more information, such as limits, engineering units, or state identifiers, for various components within your controller project.

| Component   | Extended Properties                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Tag         | In the tag editor, add extended properties to a tag.                                                                                              |
|             | User-defined data type In the data type editor, add extended properties to data types.                                                            |
|             | Add-On Instructions In the properties that are associated with the Add-On Instruction definition, add extended properties to Add-On Instructions. |

Pass-through behavior is the ability to assign extended properties at a higher level of a structure or Add-On Instruction and have that extended property automatically available for all members. Pass-through behavior is available for descriptions, state identifiers, and engineering units and you can configure it. Configure pass-through behavior on the Project tab of the Controller Properties dialog box. If you choose not to show pass-through properties, only extended properties that have been configured for a given component are displayed.

Pass-through behavior is not available for limits. When an instance of a tag is created, if limits are associated with the data type, the instance is copied.

You must know which tags have limits that are associated with them as there is no indication in the tag browser that extended properties are defined for a tag. If, however, you try to use extended properties that have not been defined for a tag, the editors show a visual indication and the routine does not verify.

## Access Extended Properties in Logic

You can access limits that are defined on tags by using the .@Min and .@Max syntax:

- You cannot write to extended properties values in logic.
- To use extended tag properties in an Add-On Instruction, you must pass them in as input operands to the Add-On Instruction.
- Alias tags that have extended properties cannot access the extended properties in logic.
- Limits can be configured for input and output parameters in Add-On Instructions. However, limits cannot be defined on an InOut parameter of an Add-On Instruction.
- Limits cannot be accessed inside Add-On Instruction logic. Limits are only for use by HMI applications.

If an array tag is using indirect addressing to access limits in logic, the following conditions apply:

- If the array tag has limits that are configured, the extended properties are applied to any array element that does not explicitly have that particular extended property configured. For example, if the array tag MyArray has Max configured to 100, any element of the array that does not have Max configured inherits the value of 100 when being used in logic. However, it is not visible to you that the value inherited from MyArray is configured in the tag properties.
- At least one array element must have a limit that is configured for indirectly referenced array logic to verify. For example, if MyArray[x].@Max is being used in logic, at least one array element of MyArray[] must have Max extended property configured if MyArray has not configured Max.
- Under the following circumstances a data type default value is used:
- – Array is accessed programmatically with indirect reference.
- – Array tag does not have the extended property configured.
- – A member of an array does not have the extended property configured.

For example, for an array of SINT type, when max limit is called in logic for a member, the value 127 is used.

If an array element is directly accessed, the element has to have the extended property defined. If not, verification fails.

## Programming Languages

The ControlLogix controller supports these programming languages: online and offline.

Table 39 - ControlLogix Controller Programming Languages

| Language               | Is best used in programs with                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------|
| Relay ladder           | Continuous or parallel execution of multiple operations (not sequenced)                                   |
| Relay ladder           | Boolean or bit-based operations                                                                           |
| Relay ladder           | Complex logical operations                                                                                |
| Relay ladder           | Message and communication processing                                                                      |
| Relay ladder           | Machine interlocking                                                                                      |
| Relay ladder           | Operations that service or maintenance personnel have to interpret to troubleshoot the machine or process |
| Function block diagram | Continuous process and drive control                                                                      |
| Function block diagram | Loop control                                                                                              |
| Function block diagram | Calculations in circuit flow                                                                              |
|                        | Sequential function chart (SFC) High-level management of multiple operations                              |
|                        | Repetitive sequence of operations                                                                         |
|                        | Batch process                                                                                             |
|                        | Motion control using structured text                                                                      |
|                        | State machine operations                                                                                  |
| Structured text        | Complex mathematical operations                                                                           |
| Structured text        | Specialized array or table loop processing                                                                |
| Structured text        | ASCII string handling or protocol processing                                                              |

For information about programming in these languages, see the Logix 5000 Controllers Common Procedures Programming Manual, publication 1756-PM001 .

## Add-On Instructions

Table 40 - Add-On Instruction Capabilities

| Capability              | Description                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Save Time               | With Add-On Instructions, you can combine your most commonly used logic into sets of reusable instructions. You save time when you create instructions for your projects and share them with others. Add-On Instructions increase project consistency because commonly used algorithms all work in the same manner, regardless of who implements the project. |
| Use Standard Editors    | You create Add-On Instructions by using one of three programming editors: • Relay Ladder • Function Block Diagram • Structured Text                                                                                                                                                                                                                           |
|                         | Export Add-On Instructions You can export Add-On Instructions to other projects and copy and paste them from one project to another. Give each instruction a unique name so that you don’t accidentally overwrite another instruction of the same name.                                                                                                       |
| Use Context Views       | Context views let you visualize the logic of an instruction for instant, simplified online troubleshooting of your Add-On Instructions. Each instruction contains a revision, a change history, and an auto-generated help page.                                                                                                                              |
| Create Custom Help      | When you create an instruction, you enter information for the description fields. This information becomes custom Help.                                                                                                                                                                                                                                       |
| Apply Source Protection | As the creator of Add-On Instructions, you can limit users of your instructions to read-only access, or you can bar access to the internal logic or local parameters that are used by the instructions. This source protection lets you stop unwanted changes to your instructions and helps protect your intellectual property.                              |

Once defined in a project, Add-On Instructions behave similarly to the built-in instructions in Logix 5000 controllers. They appear on the instruction tool bar for easy access along with internal instructions.

Figure 38 - Add-On Instructions

## Controller Organizer

<!-- image -->

With RSLogix 5000® software, version 16.03.00 or later, and Logix Designer application, version 21.00.00 or later, you can design and configure sets of commonly used instructions to increase project consistency. Similar to the built-in instructions that are contained in Logix 5000 controllers, these instructions you create are called Add-On Instructions. Add-On Instructions reuse common control algorithms. With them, you can do the following:

- Ease maintenance by animating logic for one instance.
- Help protect intellectual property with locking instructions.
- Reduce documentation development time.

You can use Add-On Instructions across multiple projects. You can define your instructions, obtain them from somebody else, or copy them from another project.

Table 40 explains some of the capabilities and advantages of use Add-On Instructions.

## Access the Module Object

The MODULE object provides status information about a module. To select a particular module object, set the Object Name operand of the GSV/SSV instruction to the module name. The specified module must be present in the I/O Configuration section of the controller organizer and must have a device name.

## Create the Add-On Instruction

With Logix Designer application, version 24.00.00 and later, you can access a MODULE object directly from an Add-On Instruction. Previously, you could access the MODULE object data but not from within an Add-On Instruction.

You must create a Module Reference parameter when you define the Add-On Instruction to access the MODULE object data. A Module Reference parameter is an InOut parameter of the MODULE data type that points to the MODULE Object of a hardware module. You can use module reference parameters in both Add-On Instruction logic and program logic.

<!-- image -->

For more information on the Module Reference parameter, see the Logix 5000 Controllers Add-On Instructions Programming Manual, publication 1756-PM010 and the Logix Designer application online help.

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

## Monitoring Controller Status

## Monitoring I/O Connections

The ControlLogix controller uses Get System Value (GSV) and Set System Value (SSV) instructions to get and set (change) controller data. The controller stores system data in objects. There is no status file, as in the PLC-5® processor.

The GSV instruction retrieves the specified information and places it in the destination. The SSV instruction sets the specified attribute with data from the source. Both instructions are available from the Input/Output tab of the Instruction toolbar.

Figure 39 - GSV and SSV Instructions for Monitoring and Setting Attributes

<!-- image -->

When you add a GSV/SSV instruction to the program, the object classes, object names, and attribute names for the instruction are shown. For the GSV instruction, you can get values for the available attributes. For the SSV instruction, only the attributes you can set are shown.

Some object types appear repeatedly, so you have to specify the object name. For example, there can be several tasks in your application. Each task has its own Task object that you access by the task name.

There are several objects and attributes that you can use the GSV and SSV instructions to monitor and set the system. For more information about GSV instructions, SSV instructions, objects, and attributes see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

If communication with a device in the I/O configuration of the controller does not occur in an application-specific period, the communication times out and the controller produces warnings.

The minimum timeout period that, once expired without communication, causes a timeout is 100 ms. The timeout period can be greater, depending on the RPI of the application. For example, if your application uses the default RPI = 20 ms, the timeout period is 160 ms.

For more information on how to determine the time for your application, search the Rockwell Automation® Knowledgebase for answer ID 38535. The document is available at https://www.rockwellautomation.com/ knowledgebase .

When a timeout does occur, the controller produces these warnings;

- An I/O fault status code is indicated on the status display of the 1756-L7x controller.
- The I/O status indicator on the front of the 1756-L6x controller flashes green.
- A shows over the I/O configuration folder and over the devices that have timed out. !
- A module fault code is produced, which you can access via the following:
- – The Module Properties dialog box
- – A GSV instruction

For more information about I/O faults, see the Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

## Determine If I/O Communication Has Timed Out

This example can be used with the 1756-L7x or 1756-L6x controllers:

- The GSV instruction gets the status of the I/O status indicator (via the LEDStatus attribute of the Module object) and stores it in the IO\_LED tag.
- IO\_LED is a DINT tag that stores the status of the I/O status indicator or status display on the front of the controller.
- If IO\_LED equals 2, then at least one I/O connection has been lost and the Fault\_Alert is set.

Figure 40 - GSV Used to Identify I/O Timeout

<!-- image -->

For more information about attributes available with the Module object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

## Determine If I/O Communication to a Specific I/O Module Has Timed Out

If communication times out with a device (module) in the I/O configuration of the controller, the controller produces a fault code and fault information for the module. You can use GSV instructions to get fault code and information via the FaultCode and FaultInfo attributes of the Module object.

For more information about attributes available with the Module object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

## I/O Module Properties

<!-- image -->

## Parent Communication Module Properties

General

Connection*

Module Info

Backplane

Requested Packet Interval (RPl):

Inhibit Module

Major Fault On Controller If Connection Fails While in Run Mode

Use Scheduled Connection over ControllNet

For more information about programming the Controller Fault Handler, see the Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

20.0ms

## Interrupt the Execution of Logic and Execute the Fault Handler

Dependent on your application, you can want an I/O connection error to cause the Controller Fault Handler to execute. To do so, set the module property that causes a major fault to result from an I/O connection error. The major fault causes the execution of the Controller Fault Handler.

First, develop a routine in the Controller Fault Handler that can respond to I/ O connection faults. Then, in the Module Properties dialog box of the I/O module or parent communication module, check Major Fault On Controller If Connection Fails While in Run Mode.

Figure 41 - I/O Connection Fault Causes Major Fault

(2.0 - 750.0 ms)

## System Overhead Time Slice

The controller communicates with other devices at a specified rate (scheduled) or when processing time is available to service the communication.

The system overhead time slice specifies the percentage of time a controller devotes to service communication. If you have a continuous task, the system overhead time slice that is entered on the Advanced tab of the Controller Properties dialog box specifies the continuous task/service communication ratio. However, if there is no continuous task, the overhead time slice has no effect.

Table 41 shows the ratio between the continuous task and service communication at various system overhead time slices for RSLogix 5000 software, version 16.03.00 or later, and the Logix Designer application, version 21.00.00 or later.

Table 41 - Ratio between Continuous Task and Service Communication

| Time Slice   |      | Continuous Task Duration Service Communication Duration   |
|--------------|------|-----------------------------------------------------------|
| 10%          | 9 ms | 1 ms                                                      |
| 20%          | 4 ms | 1 ms                                                      |
| 25%          | 3 ms | 1 ms                                                      |
| 33%          | 2 ms | 1 ms                                                      |
| 50%          | 1 ms | 1 ms                                                      |
| 66%          | 1 ms | 2 ms                                                      |
| 75%          | 1 ms | 3 ms                                                      |
| 80%          | 1 ms | 4 ms                                                      |
| 90%          | 1 ms | 9 ms                                                      |

As shown in the table, if the system overhead time slice is less than or equal to 50%, the duration stays fixed at 1 ms. The same applies for 66% and higher, except there are multiple 1 ms intervals. For example, at 66% there are two 1 ms intervals of consecutive time and at 90%, there are nine 1 ms intervals of consecutive time.

## Configure the System Overhead Time Slice

To configure the system overhead time slice, perform this procedure.

1. In the Controller Organizer, right-click the controller and choose Properties.

The Controller Properties dialog box appears.

<!-- image -->

2. Click the Advanced tab.
3. Enter a numeric value in the System Overhead Time Slice box.
4. Use Run Continuous Task (default) or Reserve for System Tasks.
- The Run Continue Task radio button is used when there is no communication or background tasks to process; controller immediately returns to the continuous task.
- The Reserve for System Task radio button allocates the entire 1 ms of the system overhead time slice whether the controller has communication or background tasks to perform before returning back to the continuous task. This option lets you simulate a communication load on the controller during design and programming before HMIs, controller to controller messaging, and so forth, are configured.
5. Click OK.

## Sample Controller Projects

The Studio 5000 Logix Designer® application includes sample projects that you can copy and modify to fit your application. To access the sample projects, choose Open Sample Project in the Studio 5000® interface and navigate to Samples &gt; ENU &gt; v24 &gt; Rockwell Automation.

Figure 42 - Opening Sample Projects

<!-- image -->

<!-- image -->

## PhaseManager Overview

## Using the PhaseManager Tool

The PhaseManager™ tool lets you add equipment phases to your controller. An equipment phase helps you lay out your code in sections that are easier to write, find, follow, and change.

| Term  Description                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Equipment phase • As with a program, an equipment phase is run in a task and is given a set of routines and tags. • Unlike a program, an equipment phase runs by a state model and lets you do one activity.                                                                                                            |
| State model • A state model divides the operating cycle of your equipment into a series of states. Each state is an instance in the operation of the equipment, the actions, or conditions of the equipment at a given time. • The state model of an equipment phase resembles that of the S88 and PackML state models. |
| State machine An equipment phase includes an embedded state machine that does the following: • Calls the routine that is associated with an active state • Manages the transitions between states with minimal coding • Makes sure that the equipment goes from state to state along an allowable path                  |
| PHASE tag When you add an equipment phase, the application creates a tag for the equipment phase. The tag uses the PHASE data type.                                                                                                                                                                                     |

Table 42 - PhaseManager Terminology

<!-- image -->

Figure 43 - PhaseManager Overview

<!-- image -->

## Minimum System Requirements

## State Model Overview

To develop PhaseManager programs, you need the following:

- A ControlLogix® controller at firmware revision 16 or later
- A communication path to the controller
- RSLogix 5000® software, version 16.03.00 or later or Logix Designer application, version 21.00.00 or later

To enable PhaseManager support, you need the Full or Professional edition of the software, or the software with PhaseManager software (catalog number 9324-RLDPMENE).

A state model defines what your equipment does under different conditions, and how the states relate to each other. Each state can be described as an Acting state or Waiting state.

Table 43 - States in PhaseManager Software

| State Description                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------|
| Acting Does something or several things for a certain time or until certain conditions are met. An acting state runs once or repeatedly. |
| Waiting Shows that certain conditions are met and the equipment is waiting for the signal to go to the next state.                       |

Figure 44 - PhaseManager State Transitions

<!-- image -->

= Transition

<!-- image -->

With a state model, you define the behavior of your equipment during Acting states.

Table 44 - Acting States in the PhaseManager State Model

| State    | Question to Ask                                                              |
|----------|------------------------------------------------------------------------------|
|          | Resetting How does the equipment get ready to run?                           |
| Running  | What does the equipment do to make the product?                              |
| Holding  | How does the equipment temporarily stop making product without making scrap? |
|          | Restarting How does the equipment resume production after holding?           |
| Stopping | What happens during a normal shutdown?                                       |
| Aborting | How does the equipment shut down if a fault or failure occurs?               |

## How Equipment Changes States

The arrows of the state model show the states through which your equipment progresses:

- Each arrow is called a transition.
- A state model lets the equipment make only certain transitions. This restriction standardizes the behavior of the equipment so that other equipment using the same model behaves the same way.

Figure 45 - PhaseManager Transition Commands

Table 45 - PhaseManager Transitions

| Type of Transition Description                                                                                                                                                                                                                                                                                       | Type of Transition Description                                                                                                                                                                                                                                                                                       | Type of Transition Description                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command A command tells the equipment to do something. For example, the operator pushes the start button to begin production and the stop button to halt production. The PhaseManager tool uses these commands:                                                                                                      | Command A command tells the equipment to do something. For example, the operator pushes the start button to begin production and the stop button to halt production. The PhaseManager tool uses these commands:                                                                                                      | Command A command tells the equipment to do something. For example, the operator pushes the start button to begin production and the stop button to halt production. The PhaseManager tool uses these commands:                                                                                                      |
|                                                                                                                                                                                                                                                                                                                      | Reset Stop Restart Start Hold Abort                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                      |
| Done Equipment goes to a waiting state when it is finished with what it is doing. You do not give the equipment a command. Instead, you configure your code to signal when the phase state is finished.                                                                                                              | Done Equipment goes to a waiting state when it is finished with what it is doing. You do not give the equipment a command. Instead, you configure your code to signal when the phase state is finished.                                                                                                              | Done Equipment goes to a waiting state when it is finished with what it is doing. You do not give the equipment a command. Instead, you configure your code to signal when the phase state is finished.                                                                                                              |
| A fault tells you that something out of the ordinary has happened. You configure your code to look for faults and act if it finds any. If you want to shut down your equipment as quickly as possible when it detects a fault, configure your code to look for that fault and give the abort command if it finds it. | A fault tells you that something out of the ordinary has happened. You configure your code to look for faults and act if it finds any. If you want to shut down your equipment as quickly as possible when it detects a fault, configure your code to look for that fault and give the abort command if it finds it. | A fault tells you that something out of the ordinary has happened. You configure your code to look for faults and act if it finds any. If you want to shut down your equipment as quickly as possible when it detects a fault, configure your code to look for that fault and give the abort command if it finds it. |

## Manually Change States

You can manually change an equipment phase. To change a PhaseManager state, perform this procedure.

1. Open the Equipment Phase Monitor.
2. Take ownership of the equipment phase by clicking Owners and clicking Yes.
3. Click the command that initiates the state you need (for example, Start or Reset).
4. After you have finished manually changing the state, click Owners to release your ownership.

<!-- image -->

## PhaseManager Tool versus Other State Models

## Equipment Phase Instructions

Table 46 compares PhaseManager state models to other state models.

Table 46 - PhaseManager Tool and Other State Models

| PhaseManager Tool          | S88                        | PackML           |
|----------------------------|----------------------------|------------------|
| Resetting…Idle             | Idle                       | Starting…Ready   |
| Running…Complete           | Running…Complete Producing |                  |
| Subroutines or breakpoints | Pausing…Paused             | Standby          |
| Holding…Held               | Holding…Held               | Holding…Held     |
| Restarting                 | Restarting                 | None             |
| Stopping…Stopped           | Stopping…Stopped           | Stopping…Stopped |
| Aborting…Aborted           | Aborting…Aborted           | Aborting…Aborted |

The controller supports several equipment-phase relay ladder and structured text instructions.

Table 47 - Instructions for Use with PhaseManager Tool

|      | Instruction Instruction Function                                                                                                                                                                                 |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      | PSC Signal a phase that the state routine is complete and to go ahead to the next state.                                                                                                                         |
|      | PCMD Change the state or substate of a phase.                                                                                                                                                                    |
| PFL  | Signal a failure for a phase.                                                                                                                                                                                    |
| PCLF | Clear the failure code of a phase.                                                                                                                                                                               |
| PXRQ | Initiate communication with FactoryTalk® Batch software.                                                                                                                                                         |
| PRNP | Clear the NewInputParameters bit of a phase.                                                                                                                                                                     |
| PPD  | Configure breakpoints within the logic of a phase.                                                                                                                                                               |
| PATT | Take ownership of a phase to one of the following: • Stop another program or FactoryTalk Batch software from commanding a phase. • Make sure another program or FactoryTalk Batch software does not own a phase. |
| PDET | Relinquish ownership of a phase.                                                                                                                                                                                 |
| POVR | Override a command.                                                                                                                                                                                              |

For more information about instructions for use with equipment phases, see the PhaseManager User Manual, publication LOGIX-UM001 .

## Troubleshoot in the Logix Designer Application

## Troubleshoot the Module

The Studio 5000 Logix Designer® application indicates fault conditions in the following ways:

- Warning signal on the main screen next to the module - This occurs when the connection to the module is broken. The controller state also indicates Faulted and the Controller fault is illuminated in red.

<!-- image -->

<!-- image -->

- Message in the status line of a screen.

<!-- image -->

On the Module Info tab, in the Status section, the Major and Minor Faults are listed along with the Internal State of the module.

Notification in the Tag Editor - General module faults are also reported in the Tag Editor. Diagnostic faults are reported only in the tag editor.

The Value field indicates a fault with the number 1.

<!-- image -->

## Fault Type Determination

To display recent fault information in the Major Faults tab of the Module Properties screen, you must check the Major Fault on Controller option in the Connection tab.

<!-- image -->

When you are monitoring the configuration properties of a module in the Logix Designer application and receive a Communication fault message, the Major Faults tab indicates the type of fault under Recent Faults.

<!-- image -->

## ControlLogix 5570 Controller Status Display and Indicators

## ControlLogix 5570 Controller Status Display

ControlLogix® 5570 controllers have four status indicators and one fourcharacter scrolling status display.

Figure 46 - 1756-L7x Status Display and Indicators

<!-- image -->

The ControlLogix 5570 controller status display scrolls messages that provide information about the firmware revision, ESM status, project status, and major faults of the controller.

## General Status Messages

The messages that are described in Table 48 are typically indicated upon powerup, powerdown, and while the controller is running to show the status of the controller and the ESM.

Table 48 - General Status Messages

| Message                                        | Interpretation                                                                                                                                                                                                                                                                      |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No message is indicated The controller is Off. | Check the OK indicator to determine if the controller is powered and determine the state of the controller.                                                                                                                                                                         |
| TEST                                           | The controller is conducting power-up tests.                                                                                                                                                                                                                                        |
| PASS                                           | Power-up tests have been successfully completed.                                                                                                                                                                                                                                    |
| SAVE                                           | A project is being saved to the SD card. You can also view the SD Indicator (see page 183) for more status information. Allow the save to complete before: • removing the SD card. • disconnecting power.                                                                           |
|                                                | LOAD A project is being loaded from the SD card at controller powerup. You can also view the SD Indicator (see page 183) for more status information. Allow the load to complete before doing the following: • Removing the SD card • Disconnecting power • Removing the ESM module |
|                                                | UPDT A firmware update is being conducted from the SD card upon powerup. You can also view the SD Indicator (see page 183) for more status information. If you do not want the firmware to update upon powerup, change the Load Image property of the controller.                   |
|                                                | CHRG The capacitor-based ESM is being charged.                                                                                                                                                                                                                                      |
| 1756-L7x/X                                     | The controller catalog number and series.                                                                                                                                                                                                                                           |

Table 48 - General Status Messages (Continued)

| Message                        | Interpretation                                                                                                                                                                                                                                                                                                     |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rev XX. X.x .xxx               | The major and minor revision of the firmware of the controller.                                                                                                                                                                                                                                                    |
| No Project                     | No project is loaded on the controller. To load a project, do one of the following: • Use the Logix Designer application to download the project to the controller • Use an SD card to load a project to the controller                                                                                            |
| Project Name                   | The name of the project that is currently loaded on the controller.                                                                                                                                                                                                                                                |
| BUSY                           | The I/O modules that are associated with the controller are not yet fully powered. Allow time for powerup and I/O module self-testing.                                                                                                                                                                             |
| Corrupt Certificate Received   | The security certificate that is associated with the firmware is corrupted. Go to https://www.rockwellautomation.com/support/ and download the firmware revision you are trying to upgrade to. Replace the firmware revision that you have previously installed with that posted on the Technical Support website. |
|                                | Corrupt Image Received The firmware file is corrupted. Go to https://www.rockwellautomation.com/support/ and download the firmware revision you are trying to upgrade to. Replace the firmware revision that you have previously installed with that posted on the Technical Support website.                      |
|                                | ESM Not Present An ESM is not present and the controller cannot save the application at powerdown. Insert a compatible ESM, and, if using a capacitor-based ESM, do not remove power until the ESM is charged.                                                                                                     |
|                                | ESM Incompatible The ESM is incompatible with the memory size of the controller. Replace the incompatible ESM with a compatible ESM.                                                                                                                                                                               |
|                                | ESM Hardware Failure A failure with the ESM has occurred and the controller is incapable of saving of the program in the event of a powerdown. Replace the ESM before removing power to the controller so the controller program is saved.                                                                         |
|                                | ESM Energy Low The capacitor-based ESM does not have sufficient energy to enable the controller to save the program in the event of a powerdown. Replace the ESM.                                                                                                                                                  |
|                                | ESM Charging The capacitor-based ESM is charging. Do not remove power until charging is complete.                                                                                                                                                                                                                  |
|                                | Flash in Progress A firmware update initiated via ControlFLASH™ or AutoFlash utilities is in progress. Allow the firmware update to complete without interruption.                                                                                                                                                 |
| Firmware Installation Required | The controller is using boot firmware (that is revision 1.xxx) and requires a firmware update. Upgrade controller firmware.                                                                                                                                                                                        |
|                                | SD Card Locked An SD card that is locked is installed.                                                                                                                                                                                                                                                             |
|                                | SD Card Unprotected The controller SD card has become unprotected and is available for remote read/write operations.                                                                                                                                                                                               |

## Fault Messages

If the controller displays a fault, these messages can be indicated on the status display.

Table 49 - Fault Messages

| Message                                | Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Major Fault TXX:CXX message            | A major fault of Type XX and Code XX has been detected. For example, if the status display indicates Major Fault T04:C42 Invalid JMP Target, a JMP instruction is programmed to jump to an invalid LBL instruction. For details about major recoverable faults, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .                                                                                                                                                                                                                                                                                                                          |
| I/O Fault Local:X #XXXX message        | An I/O fault has occurred on a module in the local chassis. The slot number and fault code are indicated along with a brief description. For example, I/O Fault Local:3 #0107 Connection Not Found indicates that a connection to the local I/O module in slot three is not open. Take corrective action specific to the type of fault indicated. For details about each I/O fault code, see the Logix 5000 Controllers Major, Minor, and I/O FaultsLogix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .                                                                                                                                              |
| I/O Fault ModuleName #XXXX message     | An I/O fault has occurred on a module in a remote chassis. The name of the faulted module is indicated with the fault code and a brief description of the fault. For example, I/O Fault My_Module #0107 Connection Not Found indicates that a connection to the module named My_Module is not open. Take corrective action specific to the type of fault indicated. For details about each I/O fault code, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .                                                                                                                                                                               |
| I/O Fault ModuleParent:X #XXXX message | An I/O fault has occurred on a module in a remote chassis. The parent name of the module is indicated because no module name is configured in the I/O Configuration tree of the Logix Designer application. In addition, the fault code is indicated with a brief description of the fault. For example, I/O Fault My_CNet:3 #0107 Connection Not Found indicates that a connection to a module in slot 3 of the chassis with the communication module named My_CNet is not open. Take corrective action specific to the type of fault indicated. For details about each I/O fault code, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 . |
| X I/O Faults                           | I/O faults are present and X = the number of I/O faults present. If there are multiple I/O faults, the controller indicates that the first fault reported. As each I/O fault is resolved, the number of faults indicated decreases and the I/O Fault message indicates the next fault reported. Take corrective action specific to the type of fault indicated. For details about each I/O fault code, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .                                                                                                                                                                                   |

## Major Fault Messages

The Major Fault TXX:CXX message on the controller status display indicates major faults. Table 50 lists fault types, codes, and the associated messages as they are shown on the status display.

For detailed descriptions and suggested recovery methods for major faults, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

Table 50 - Major Fault Status Messages

|    |       | Type Code Message                                         |
|----|-------|-----------------------------------------------------------|
|    |       | 11Run Mode Powerup                                        |
|    |       | 1 60 Nonrecoverable                                       |
| 1  | 61    | Nonrecoverable – Diagnostics Saved on CF Card             |
| 1  | 62    | Nonrecoverable – Diagnostics and Program Saved on SD card |
| 3  | 16    | I/O Connection Failure                                    |
| 3  | 20    | Chassis Failure                                           |
|    | 3 21  |                                                           |
| 3  | 23    | Connection Failure                                        |
| 4  | 16    | Unknown Instruction                                       |
| 4  | 20    | Invalid Array Subscript                                   |
| 4  | 21    | Control Structure LEN or POS < 0                          |
| 4  | 31    | Invalid JSR Parameter                                     |
| 4  | 34    | Timer Failure                                             |
| 4  | 42    | Invalid JMP Target                                        |
|    |       | 4 82 SFC Jump Back Failure                                |
|    |       | 4 83 Value Out of Range                                   |
|    |       | 4 84 Stack Overflow                                       |
|    |       | 4 89 Invalid Target Step                                  |
| 4  | 90    | Invalid Instruction                                       |
| 4  | 91    | Invalid Context                                           |
|    |       | 4 92 Invalid Action                                       |
| 4  |       | 990 User-defined                                          |
|    | 4 991 |                                                           |
|    | 4 992 |                                                           |
|    | 4 993 |                                                           |
|    | 4 994 |                                                           |
|    | 4 995 |                                                           |
|    | 4 996 |                                                           |
|    | 4 997 |                                                           |
|    | 4 998 |                                                           |
|    | 4 999 |                                                           |

Table 50 - Major Fault Status Messages (Continued)

|    |    | Type Code Message                                                   |
|----|----|---------------------------------------------------------------------|
|    |    | 6 1 Task Watchdog Expired                                           |
|    |    | 7 40 Save Failure                                                   |
| 7  | 41 | Bad Restore Type                                                    |
| 7  | 42 | Bad Restore Revision                                                |
| 7  | 43 | Bad Restore Checksum                                                |
| 7  | 44 | Failed to Restore Processor Memory                                  |
| 8  | 1  | Keyswitch Change Ignored                                            |
| 11 | 1  | Positive Overtravel Limit Exceeded                                  |
| 11 | 2  | Negative Overtravel Limit Exceeded                                  |
| 11 | 3  | Position Error Tolerance Exceeded                                   |
| 11 | 4  | Encoder Channel Connection Fault                                    |
| 11 | 5  | Encoder Noise Event Detected                                        |
| 11 | 6  | Sercos Drive Fault                                                  |
| 11 | 7  | Synchronous Connection Fault                                        |
| 11 | 8  | Servo Module Fault                                                  |
| 11 | 9  | Asynchronous Connection Fault                                       |
| 11 | 10 | Motor Fault                                                         |
| 11 | 11 | Motor Thermal Fault                                                 |
| 11 | 12 | Drive Thermal Fault                                                 |
| 11 | 13 | Sercos Communications Fault                                         |
| 11 | 14 | Inactive Drive Enable Input Detected                                |
| 11 | 15 | Drive Phase Loss Detected                                           |
| 11 | 16 | DriveGuard® Fault                                                   |
| 11 | 32 | Motion Task Overlap Fault                                           |
| 11 | 33 | CST Reference Loss Detected                                         |
| 12 | 32 | Disqualified Secondary Controller Cycle Power                       |
| 12 | 33 | Unpartnered Controller Identified in New Primary Chassis            |
| 12 | 34 | Keyswitch Positions of Primary and Secondary Controllers Mismatched |
| 14 | 1  | Safety Task Watchdog Expired                                        |
| 14 | 2  | Error In Routine of Safety Task                                     |
| 14 | 3  | Safety Partner Missing                                              |
| 14 | 4  | Safety Partner Unavailable                                          |
| 14 | 5  | Safety Partner Hardware Incompatible                                |
| 14 | 6  | Safety Partner Firmware Incompatible                                |
| 14 | 7  | Safety Task Inoperable                                              |
| 14 | 8  | Coordinated System Time (CST) Not Found                             |
| 14 | 9  | Safety Partner Nonrecoverable Controller Fault                      |
| 18 | 1  | CIP Motion Initialization Fault                                     |
| 18 | 2  | CIP Motion Initialization Fault Mfg                                 |

Table 50 - Major Fault Status Messages (Continued)

| Type Code Message                   |
|-------------------------------------|
| 18 3 CIP Motion Axis Fault          |
| 18 4 CIP Motion Axis Fault Mfg      |
| 18 5 CIP Motion Fault               |
| 18 6 CIP™ Module Fault              |
| 18 7 Motion Group Fault             |
| 18 8 CIP Motion Configuration Fault |
| 18 9 CIP Motion APR Fault           |
| 18 10 CIP Motion APR Fault Mfg      |
| 18 128 CIP Motion Guard Fault       |

## I/O Fault Codes

The controller indicates I/O faults on the status display in one of these formats:

- I/O Fault Local:X #XXXX message
- I/O Fault ModuleName #XXXX message
- I/O Fault ModuleParent:X #XXXX message

The first part of the format is used to indicate the location of the module with a fault. How the location is indicated depends on your I/O configuration and the properties of the module that are specified in Logix Designer application.

The latter part of the format, #XXXX message, can be used to diagnose the type of I/O fault and potential corrective actions. For details about each I/O fault code, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 .

Table 51 - I/O Fault Messages

| Code Message                   |
|--------------------------------|
| #0001 Connection Failure       |
| #0002 Insufficient Resource    |
| #0003 Invalid Value            |
| #0004 IOI Syntax               |
| #0005 Destination Unknown      |
| #0006 Partial Data Transferred |
| #0007 Connection Lost          |
| #0008 Service Unsupported      |
| #0009 Invalid Attribute Value  |
| #000A Attribute List Error     |
| #000B State Already Exists     |
| #000C Object Mode Conflict     |

Table 51 - I/O Fault Messages (Continued)

| Code Message                       |
|------------------------------------|
| #000D Object Already Exists        |
| #000E Attribute Not Settable       |
| #000F Permission Denied            |
| #0010 Device State Conflict        |
| #0011 Reply Too Large              |
| #0012 Fragment Primitive           |
| #0013 Insufficient Command Data    |
| #0014 Attribute Not Supported      |
| #0015 Data Too Large               |
| #0100 Connection In Use            |
| #0103 Transport Not Supported      |
| #0106 Ownership Conflict           |
| #0107 Connection Not Found         |
| #0108 Invalid Connection Type      |
| #0109 Invalid Connection Size      |
| #0110 Module Not Configured        |
| #0111 RPI Out of Range             |
| #0113 Out of Connections           |
| #0114 Wrong Module                 |
| #0115 Wrong Device Type            |
| #0116 Wrong Revision               |
| #0117 Invalid Connection Point     |
| #0118 Invalid Configuration Format |
| #0119 Module Not Owned             |
| #011A Out of Connection Resources  |
| #0203 Connection Timeout           |
| #0204 Unconnected Message Timeout  |
| #0205 Invalid Parameter            |
| #0206 Message Too Large            |
| #0301 No Buffer Memory             |
| #0302 Bandwidth Not Available      |
| #0303 No Bridge Available          |
| #0304 ControlNet® Schedule Error   |
| #0305 Signature Mismatch           |
| #0306 CCM Not Available            |
| #0311 Invalid Port                 |
| #0312 Invalid Link Address         |
| #0315 Invalid Segment Type         |
| #0317 Connection Not Scheduled     |

Table 51 - I/O Fault Messages (Continued)

| Code Message                                       |
|----------------------------------------------------|
| #0318 Invalid Link Address                         |
| #0319 No Secondary Resources Available             |
| #031E No Available Resources                       |
| #031F No Available Resources                       |
| #0800 Network Link Offline                         |
| #0801 Incompatible Multicast RPI                   |
| #0814 Data Type Mismatch                           |
| #FD01 Bad Backplane EEPROM                         |
| #FD02 No Error Code                                |
| #FD03 Missing Required Connection                  |
| #FD04 No CST Master                                |
| #FD05 Axis or GRP Not Assigned                     |
| #FD06 Sercos Transition Fault                      |
| #FD07 Sercos Init Ring Fault                       |
| #FD08 Sercos Comm Fault                            |
| #FD09 Sercos Init Node Fault                       |
| #FD0A Axis Attribute Reject                        |
| #FD1F Safety I/O                                   |
| #FD20 No Safety Task                               |
| #FE01 Invalid Connection Type                      |
| #FE02 Invalid Update Rate                          |
| #FE03 Invalid Input Connection                     |
| #FE04 Invalid Input Data Pointer                   |
| #FE05 Invalid Input Data Size                      |
| #FE06 Invalid Input Force Pointer                  |
| #FE07 Invalid Output Connection                    |
| #FE08 Invalid Output Data Pointer                  |
| #FE09 Invalid Output Data Size                     |
| #FE0A Invalid Output Force Pointer                 |
| #FE0B Invalid Symbol String                        |
| #FE0C Invalid Scheduled Personal Computer Instance |
| #FE0D Invalid Symbol Instance                      |
| #FE0E Module Firmware Updating                     |
| #FE0F Invalid Firmware File Revision               |
| #FE10 Firmware File Not Found                      |
| #FE11 Firmware File Invalid                        |
| #FE12 Automatic Firmware Update Failed             |
| #FE13 Update Failed - Active Connection            |
| #FE14 Searching Firmware File                      |

## ControlLogix 5570 Controller Status Indicators

Table 51 - I/O Fault Messages (Continued)

| Code Message                  |
|-------------------------------|
| #FE22 Invalid Connection Type |
| #FE23 Invalid Unicast Allowed |
| #FF00 No Connection Instance  |
| #FF01 Path Too Long           |
| #FF04 Invalid State           |
| #FF08 Invalid Path            |
| #FF0B Invalid Config          |
| #FF0E No Connection Allowed   |

The status indicators are below the status display on the controller. They indicate the state of the controller as described in these tables.

## RUN Indicator

Use the mode switch on the front of the controller or use the Controller Status menu in the Logix Designer application to change the controller mode that is shown by the RUN indicator.

Table 52 - RUN Indicator

| State Description                              |
|------------------------------------------------|
| Off The controller is in Program or Test mode. |
| Steady green The controller is in Run mode.    |

## FORCE Indicator

The Force indicator shows if I/O forces are enabled on the controller.

Table 53 - FORCE Indicator

| State Description                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off No tags contain I/O force values.                                                                                                                                                                                                         |
| Steady yellow I/O forces are active (enabled) though I/O force values and can be configured. Use caution if you install (add) a force. If you install (add) a force, it immediately takes effect.                                             |
| Flashing yellow One or more input or output addresses have been forced to an On or Off state, but the forces have not been enabled. Use caution if you enable I/O forces. If you enable I/O forces, all existing I/O forces also take effect. |

## SD Indicator

The SD indicator shows if the SD card is in use.

Table 54 - SD Indicator

| State Description                                                                   |
|-------------------------------------------------------------------------------------|
| Off No activity is occurring with the SD card.                                      |
| Flashing green The controller is reading from or writing to the SD card.            |
| Do not remove the SD card while the controller is reading or writing.  Steady green |
| Flashing red The SD card does not have a valid file system.                         |
| Steady red The controller does not recognize the SD card.                           |

## OK Indicator

The OK indicator shows the state of the controller.

Table 55 - OK Indicator

| State   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off     | No power is applied to the controller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|         | Flashing red Either of the following is true: • It is a new controller, out of the box, and it requires a firmware update. If a update firmware update is required, the status display indicates Firmware Installation Required. To update firmware, see Upgrade Controller Firmware on page 48 . • It is a previously used or in-use controller and a major fault has occurred. For details about major recoverable and nonrecoverable faults, see the Logix 5000 Controllers Major, Minor, and I/O Faults Programming Manual, publication 1756-PM014 . |
|         | Steady red One of the following is true: • The controller is completing power-up diagnostics. • The charge of the capacitor in the ESM is being discharged upon powerdown. • The controller is powered, but is inoperable. • The controller is loading a project to nonvolatile memory.                                                                                                                                                                                                                                                                  |
|         | Steady green The controller is operating normally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## ControlLogix 5560 Status Indicators

ControlLogix 5560 controllers have status indicators on the front of the controller that show the state of the controller.

<!-- image -->

## RUN Indicator

Use the mode switch on the front of the controller or use the Controller Status menu in the Logix Designer application to change the controller mode that is shown by the RUN indicator.

Table 56 - RUN Indicator

| State   | Description                                 |
|---------|---------------------------------------------|
| Off     | The controller is in Program or Test mode.  |
|         | Steady green The controller is in Run mode. |

## I/O Indicator

The I/O indicator shows the status of I/O modules in the project of the controller.

Table 57 - I/O Indicator

| State Description                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Either of the following is true: • There are no devices are in the I/O configuration of the controller. If needed, add the required devices to the I/O configuration of the controller. • The controller does not contain a project (controller memory is empty). If prepared, download the project to the controller. |
| Steady green The controller is communicating with the devices in its I/O configuration.                                                                                                                                                                                                                                    |
| Flashing green One or more devices in the I/O configuration of the controller are not responding. For more information, go online with the Logix Designer application to check the I/O configuration of the controller.                                                                                                    |
| Flashing red A chassis fault exists. Troubleshoot the chassis and replace it if necessary.                                                                                                                                                                                                                                 |

## FORCE Indicator

The FORCE indicator shows if I/O forces are active or enabled.

Table 58 - FORCE Indicator

| State Description                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Either of the following is true: • No tags contain I/O force values. • I/O forces are inactive (disabled).                                                                                                                                |
| Steady yellow I/O forces are active (enabled) though I/O force values and can be configured. Use caution if you install (add) a force. If you install (add) a force, it immediately takes effect.                                             |
| Flashing yellow One or more input or output addresses have been forced to an On or Off state, but the forces have not been enabled. Use caution if you enable I/O forces. If you enable I/O forces, all existing I/O forces also take effect. |

## RS-232 Indicator

The RS-232 indicator shows if the serial port is in use.

Table 59 - RS-232 Status Indicator

| State Description                                   |
|-----------------------------------------------------|
| Off There is no serial connection activity.         |
| Flashing green There is serial connection activity. |

## BAT Indicator

The BAT indicator shows the charge of the battery and if the program is being saved.

Table 60 - BAT Indicator

| State Controller Series   | Description                                                                                                                                                                                                                                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           | Off N/A The controller is able to support memory.                                                                                                                                                                                                                                                       |
| Steady green A            | The series A controllers do not use this state.                                                                                                                                                                                                                                                         |
| B                         | The series B controller is conducting a save of the program to internal nonvolatile memory during a controller power down.                                                                                                                                                                                                                                                                                                         |
|                           | Steady red N/A Either of the following is true: • A battery is not installed. • The battery is 95% discharged and requires replacement. If the indicator is steady red before a power down, the indicator remains red while the controller is completing a program save to internal-nonvolatile memory. |

## OK Indicator

The OK indicator shows the state of the controller.

Table 61 - OK Indicator

| State  Description                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off  No power is applied to the controller.                                                                                                                                                                                                                               |
| Flashing red Either of the following is true: • It is a new controller, out of the box, and it requires a firmware update. • It is a previously used or in-use controller and a major fault has occurred. • The controller is experiencing a nonrecoverable, major fault. |
| Steady red • A nonrecoverable major fault occurred and the program was cleared from memory. • The controller is powered up, in diagnostics mode. • The controller is powered, but inoperable.                                                                             |
| Steady green The controller is operating normally.                                                                                                                                                                                                                        |
| Flashing green The controller is storing or loading a project to or from nonvolatile memory. If using a CompactFlash card, leave the card in the controller until the OK status indicator turns steady green.                                                             |

## Numerics

## 1756-ESMNRM 26

| 1747-KY controller key               | controller parts  18 ESM  26                 |
|--------------------------------------|----------------------------------------------|
| key  17                              | 1756-ESMNRMXT                                |
| 1756-BA1                             | ESM  26                                      |
| check level  74                      | 1756-ESMNSE                                  |
| controller parts  31 78              | controller parts  18                         |
| storage                              | ESM  26                                      |
| 1756-BA2                             | 1756-ESMNSEXT                                |
| check level  74 controller parts  31 | ESM  26                                      |
| estimate life  76                    | 1756-EWEB                                    |
| life after warning  77               | uses  89                                     |
| storage  78                          | 1756-IF8H                                    |
| 1756-BATM                            | uses  102                                    |
| battery  75                          | 1756-L6x                                     |
| controller parts  31                 | BAT indicator  185                           |
| 1756-CN2                             | CPU  84                                      |
| uses  93                             | FORCE indicator  185                         |
| 1756-CN2R                            | I/O indicator  184                           |
| uses  93                             | installation                                 |
| 1756-CN2RXT                          | battery, install  36                         |
| uses  93                             | battery, uninstall  36                       |
| 1756-CNB                             | CompactFlash card, removal  into chassis  38 |
| uses  93                             | memory options  84                           |
| 1756-CNBR                            | OK indicator  186                            |
|                                      | indicator  185                               |
| 1756-CP3                             | port  103                                    |
| controller parts  31                 | serial driver  46                            |
| 1756-DHRIO                           | serial port  45                              |
| communication via  98 uses           | 1756-L72EROM  11 11                          |
| remote I/O  97 ,  99                 | 1756-L73EROM                                 |
| 1756-DHRIOXT uses  97 99             | 1756-L7x CPU  84                             |
| ,  1756-DNB                          | double data rate (DDR)  41 ,  90             |
| uses  96                             | FORCE indicator  182                         |
| 1756-EN2F                            | installation                                 |
| uses  89                             | ESM, uninstall  24                           |
| 1756-EN2T                            | into chassis  19                             |
| uses  89                             | key  20                                      |
| 1756-EN2TR                           | SD card, install  21 SD card, removal  23    |
| uses  89                             | memory options  84                           |
| 1756-EN2TRXT                         | OK indicator  183                            |
| uses  89                             | parts                                        |
| 1756-EN2TSC                          | included  17                                 |
| uses  89                             | SD indicator  183 status display             |
| 1756-EN2TXT                          | 174 status indicators  182 ,  184            |
| uses  89                             | 1756-L7xXT                                   |
| 1756-EN3TR                           | extreme temperature controller  26           |
| uses  89                             | 1756-N2  124                                 |
| 1756-ENBT                            | 1756-N2XT  124                               |
| uses  89                             | 1756-RIO                                     |
| 1756-ESMCAP                          | uses  99                                     |
| controller parts  17                 | 1784-SD1  18                                 |
| ESM  26                              |                                              |
| 1756-ESMCAPXT                        | load from  69 SD card  17                    |
| ESM  26                              |                                              |
|                                      | 66                                           |
|                                      | store to                                     |

## 1784-SD2

controller parts 18

load from 69

store to 66

## 1788-CN2DN

uses 96

## 1788-CN2FFR

uses 101

1788-EN2DNR

uses 96

## 1788-EN2FFR

uses 101

## A

## add

distributed I/O 130

local I/O 124

remote I/O 126

## Add-On Instructions

in project 156

## application

elements 145

networks and 87

## Armor ControlLogix controller

1756-L72EROM 11

1756-L73EROM 11

## Armor ControlLogix controllers 9

ASCII 109

## AutoFlash

upgrade 55

axis

obtain information 142

## B

## BAT indicator

1756-L6x 185

## battery

1756-BA2

estimate 76

life after warning 77

catalog number 31

check if low 74

install 36

life and use 75

replacement 74

schedule 74

storage 78

uninstall 36

## broadcast

messages 112

## C

## cache

message options 118

messages

about 118

## calculate

connection use 119

## change

equipment phase 169

## chassis

ControlLogix

list 124

insert controller 19 , 38

## communication

Data Highway Plus 97 , 98

DH-485 network 108

Foundation Fieldbus 100

HART 102

network options 83

path

set 58

universal remote I/O 99

## CompactFlash card

installation 32

load from 69

other tasks 71

removal 32

store to 66

## comparison

PhaseManager 170

## configure

motion 142

serial driver 46

system overhead time slice 163

## connect

DH-485 network 108

## connection

calculate use 119

DeviceNet

network 96

EtherNet/IP 90

network 90

example 121

local 119

message, required 118

produce/consume

data and 116

required 117

remote 120

scheduled

ControlNet 94

unscheduled

ControlNet 94

## consume

data 115

continuous task 147

## ControlFLASH software 50

## controller

1756-L6x

battery, install 36

battery, uninstall 36

CompactFlash card, installation 32

CompactFlash card, removal 32

insert into chassis 38

serial driver 46

1756-L7x

communication options 83

ESM, uninstall 24

insert into chassis 19

key, insert 20

SD card, install 21

| SD card, removal  23                              | CPU                                      |
|---------------------------------------------------|------------------------------------------|
| status display  174 status indicators  182 ,  184 | controller  84                           |
| battery                                           |                                          |
| check  74                                         | D                                        |
| communication path set  58                        | Data Highway Plus network  k  97         |
| connections                                       | design                                   |
| calculate  119                                    | system  82                               |
| CPU resources  84                                 | develop                                  |
| design system with  82                            | applications                             |
| download  59                                      | 145 motion applications  141             |
| estimate                                          | DeviceNet                                |
| battery life  76                                  | connection use  96                       |
| firmware  48 obtain  50                           | module                                   |
| go online  59                                     | memory  96 network  94                   |
| memory options  84                                | software for  96                         |
| monitor connections  158 159                      | DF1                                      |
| ,  parts included  18                             | master  104                              |
| program  148                                      | point to point  104 radio modem  105     |
| routine  151                                      |                                          |
| tags  152                                         | slave  108                               |
| tasks  145                                        | DH-485 network                           |
| upload  61                                        |                                          |
| controller parts                                  | example configuration  108 overview  108 |
| 1756-BA1  31                                      | display 1756-L7x  174                    |
| 1756-BA2  31 1756-BATM  31                        | distributed                              |
| 1756-CP3  31                                      | I/O  129                                 |
| 1756-ESMCAP  17                                   | add  130                                 |
| 1756-ESMNRM  18                                   | double data rate (DDR)                   |
| 1756-ESMNSE  18                                   | 1756-L7x  41 ,  90                       |
| 1784-SD2  18                                      | download                                 |
| battery  31                                       | 59                                       |
| energy storage module                             | project                                  |
| catalog number  17 ,  18 catalog number ESM. See energy stor age module.                                                   | E electronic keying about  85            |
| SAMTEC RSP-119350  18 31                          |                                          |
| serial cable  USB cable  18                       | electrostatic discharge                  |
|                                                   | 39                                       |
| ControlLogix                                      | elements control application  145        |
| chassis list  124                                 | equipment phase                          |
| design system  82 I/O                             | instructions  170 error                  |
| remote  125                                       | script file                              |
| selection  123                                    | 53 ESM  26                               |
| remote I/O local  123                             | 1756-ESMCAP  1756-ESMCAPXT               |
| slot filler  124                                  | 26 26                                    |
| ControlLogix-XT                                   | 1756-ESMNRMXT  26 1756-ESMNSE  26        |
|                                                   | 1756-ESMNSEXT  26                        |
| chassis                                           |                                          |
| list  124                                         | uninstall  24                            |
| ControlNet                                        |                                          |
| module capability                                 | EtherNet/IP                              |
| 92                                                | add while online  138 connections  90 88 |
| module features  92 module list  93               | module features  network  87             |
| network  91                                       | software for  90                         |
| scheduled connection                              |                                          |
| scheduled connection  94                          | 147                                      |
| unscheduled connection                            |                                          |
|                                                   | event task                               |
| unscheduled connection  94                        |                                          |

## example configuration

## I/O configuration

| DH-485 network  108                              | add                                                                   |
|--------------------------------------------------|-----------------------------------------------------------------------|
| extreme temperature controller 1756-L7xXT  26    | distributed I/O  130 local I/O  124 remote I/O  126 while online  134 |
| F                                                | I/O indicator                                                         |
|                                                  | 1756-L6x                                                              |
| fault code                                       | 184 indicator  182                                                    |
| use GSV to get  160 fault handler                | BAT 1756-L6x                                                          |
|                                                  | 185                                                                   |
| execute at I/O fault  161 fault messages  176    | FORCE 1756-L6x  185                                                   |
| I/O  179                                         | 182                                                                   |
|                                                  | 1756-L7x                                                              |
| features  83                                     | I/O 1756-L6x  184                                                     |
| controller communication  83 programming  83     | OK                                                                    |
| filler slot                                      | 1756-L6x                                                              |
|                                                  | 186 1756-L7x                                                          |
| slot filler                                      | 183 RS232                                                             |
| 124 firmware                                     | 1756-L6x  185                                                         |
| controller  48                                   | SD 1756-L7x  183                                                      |
| determine  49 obtain  50                         | install                                                               |
| 53                                               | 1756-L6x                                                              |
| security certificate, error                      | battery  36                                                           |
| upgrade                                          |                                                                       |
| AutoFlash, use  55                               | CompactFlash card  32 insert into chassis  38                         |
| FORCE indicator 1756-L6x  185                    | 1756-L7x                                                              |
|                                                  | insert into chassis  19 key, insert  20                               |
| 1756-L7x  182 Foundation Fieldbus  100           | SD card  21                                                           |
|                                                  | battery  36                                                           |
| G 174                                            | CompactFlash card  32 SD card  21                                     |
| general status messages                          | instruction ASCII  110                                                |
| GSV                                              | motion  143                                                           |
| fault code  160 monitor                          |                                                                       |
| connection  160                                  | K                                                                     |
| H                                                | 1747-KY controller key  17 insert  20                                 |
| HART. See Highway Addressable Remote Transducer. |                                                                       |
| Highway Addressable Remote Transducer 102        | L                                                                     |
| hold-up time ESM WallClockTime  73               | load from memory card  69 local connection  119                       |
| I                                                | I/O add  124                                                          |
| I/O                                              | 123                                                                   |
| connection error                                 | remote I/O  Add-On Instructions                                       |
| 161 ControlLogix remote  125                     | Logix Designer application 156 program  148                           |
| selection  123                                   |                                                                       |
|                                                  | routine  151                                                          |
| determine data update  distributed  129          | 152                                                                   |
| 139 fault codes  179                             | tags                                                                  |
| 132                                              | tasks  145                                                            |
| reconfigure                                      |                                                                       |
| remote  125                                      |                                                                       |
|                                                  | key                                                                   |

## M

## P

| memory                                                    | path                                             |
|-----------------------------------------------------------|--------------------------------------------------|
| DeviceNet module  96 options  84                          | set communication  58                            |
| memory card                                               | periodic task  147                               |
| load from  69                                             | PhaseManager                                     |
| other tasks  71                                           | about  165                                       |
| store to  66                                              | change states  169                               |
| message                                                   | comparison  170                                  |
| about  118                                                | equipment phase instructions  170                |
| broadcast over serial  112                                | state model  167                                 |
| cache  118                                                | system requirements  167 terminology  165        |
| determine if  f  118 fault  176                           | transition  168                                  |
| reconfigure I/O module  132                               | port                                             |
| status display  174 114                                   | communication  83                                |
| Modbus network                                            | prevent electrostatic discharge  39              |
| mode                                                      |                                                  |
| serial port  104                                          | priority task  148                               |
| module                                                    | produce                                          |
| ControlNet  92 ,  93                                      | data  115                                        |
| EtherNet/IP  88                                           | produce/consume                                  |
| motion                                                    |                                                  |
| about  142                                                | connections                                      |
| application  141                                          | required  116 data  115                          |
| instructions  143                                         | program                                          |
| program  143                                              | in project  148                                  |
| MVI56-HART                                                | scheduled  150                                   |
| uses  102                                                 | system overhead time slice  162 unscheduled  150 |
| N                                                         | programming languages  155 project               |
|                                                           | 156                                              |
| network                                                   | Add-On Instructions  download  59 elements  145  |
| application and  87 controller options  83 ControlNet  91 | go online  59                                    |
|                                                           | program  148 routine  151                        |
| Data Highway Plus  98                                     |                                                  |
| Data Highway Plus DH+. See Data Highway                   | tags  152                                        |
| Plus. DeviceNet  94                                       | tasks  145                                       |
| EtherNet/IP  87                                           | upload  61                                       |
| Foundation Fieldbus  100                                  | protocol                                         |
| HART  102                                                 | ASCII  109                                       |
|                                                           | DF1                                              |
| universal remote I/O  99 84                               | master                                           |
| nonvolatile memory                                        | 104 point to point  radio modem                  |
|                                                           | 104 105 slave  108 Modbus network  114           |
| obtain                                                    | serial port  104                                 |
| axis information                                          |                                                  |
| firmware  50                                              |                                                  |
| OK indicator                                              |                                                  |
| 1756-L6x  1756-L7x                                        | messages  remote                                 |
| online                                                    | 118                                              |
| add EtherNet/IP  138                                      | connection  120 I/O  125                         |
| to I/O configuration                                      |                                                  |
| 134                                                       |                                                  |
| go  59                                                    | add  126                                         |
| options                                                   |                                                  |
| memory                                                    | ControlLogix                                     |
| 84                                                        |                                                  |
|                                                           | remote I/O                                       |
|                                                           | R                                                |
|                                                           | receive                                          |
|                                                           | 186 183                                          |
|                                                           | O                                                |
|                                                           | 142                                              |

local 123

universal 99

## remove

1756-L6x

CompactFlash card 32

1756-L7x

SD card 23

CompactFlash card 32

SD card 23

## replace

battery

schedule 74

## required

connections

messages 117 , 118

## requirement

PhaseManager

system 167

RIO. See universal remote I/O

## routine

in project 151

## RS232

DF1 device driver 46 indicator

1756-L6x 185

## RSWho

set

path 58

## S

## SAMTEC RSP-119350

controller parts 18

scheduled

program 150

script file

error 53

## SD card

1784-SD1 17

install 21

load from 69

other tasks 71

removal 23

store to 66

## SD indicator

1756-L7x 183

## security certificate

error 53

## selection

I/O 123

send

messages 118

## serial

broadcast 112

cable

catalog number 31

DH-485 network configuration

108

driver 46

Modbus network 114

## serial port

1756-L6x 45

ASCII 109

DF1

master 104

point to point 104

radio modem 105

slave 108

mode 104

protocols 104

service communication 162

set up

serial driver 46

## software

DeviceNet and 96

EtherNet/IP and 90

required

USB 42

specifications 13

state model

overview 167

## status

battery 74

display

1756-L7x 174

fault messages 176

indicators

1756-L7x 182 , 184

messages

display 174

monitor

connections 158 , 159

## storage

battery 78

store

to memory card 66

system

83

system overhead time slice 162

configure 163

## system requirements

PhaseManager 167

## T

## tag

consume 115

in project 152

produce 115

## task

continuous 147

event 147

in project 145

periodic 147

priority 148

time slice 162

transition

PhaseManager 168

type

USB 42

## U

## uninstall

1756-L6x

battery 36

1756-L7x

ESM 24

battery 36

ESM 24

## universal remote I/O 99

communicate via 100

## unscheduled

program 150

## update

determine frequency 139

## upgrade

firmware

AutoFlash, use 55

## upload

project 61

## USB

cable

catalog number 18

software required 42

type 42

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

Allen-Bradley, ArmorBlock, ArmorBlock MaXum, ArmorPOINT, Compact I/O, CompactLogix, ControlFLASH, ControlLogix, ControlLogix-XT, Data Highway Plus, DH+, expanding human possibility, FactoryTalk, FLEX, FLEX Ex, FlexLogix, GuardLogix, Integrated Architecture, Kinetix, Logix5000, MessageView, MicroLogix, PanelView, PhaseManager, PLC-5, POINT I/O, PowerFlex, RediSTATION, Rockwell Automation, RSBizWare, RSFieldbus, RSLinx, RSLogix 5000, RSNetWorx, RSView, Series 9000, SLC, Stratix, Studio 5000, and Studio 5000 Logix Designer are trademarks of Rockwell Automation.

ControlNet, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 UNITEDKINGD0M:RockwellAutomationLtd.Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:（44)（1908)838-800