<!-- image -->

## POINT Guard I/O Safety Modules

Catalog Numbers 1734-IB8S, 1734-IB8SK, 1734-IE4S, 1734-IE4SK, 1734-OB8S, 1734-OB8SK, 1734-OBV2S, 1734-OBV2SK

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

| Preface                        | Summary of Changes . . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 7            |
|--------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------|
|                                | Terminology. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 8          |
|                                | Additional Resources . . . . . . . .  . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 8            |
|                                | Chapter 1                                                                                            |                                              |
| POINT Guard I/O Overview       | Understand Suitability for Use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 |                                              |
|                                | Safety Precautions . . . . .  . . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . . 11     |
|                                | Install or Replace Modules . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 11             |
|                                | Limit Access to the System . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 12             |
|                                | POINT Guard I/O Modules in CIP Safety Systems . . . . . . . . . . . . . . 13                         |                                              |
|                                | 1734-IB8S Digital Input Module Features . . . . . . . . . . . . . . . . . . . 13                     |                                              |
|                                | 1734-OB8S Safety Digital Output Module Features . . . . . . . . . . 14                               |                                              |
|                                | 1734-OBV2S POINT Guard I/O Module Features . . . . . . . . . . 14                                    |                                              |
|                                | 1734-IE4S Safety Analog Input Module Features. . . . . . . . . . . . . 15                            |                                              |
|                                | Programming Requirements. . . .  . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . 15                 |
|                                | CIP Safety Architectures . . . .  . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 16             |
|                                | Safety Application Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17     |                                              |
|                                | Chapter 2                                                                                            |                                              |
| Safety Inputs, Safety Outputs, | Safe States . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . . . 19 |
| and Safety Data                | POINT Guard Digital I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . 19                   |                                              |
|                                | POINT Guard I/O Analog Input Module. . . . . . . . . . . . . . . . . . . 20                          |                                              |
|                                | Safety Inputs - 1734-IB8S.   . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . 20       |
|                                | Use a Test Output with a Safety Input . . . . . . . . . . . . . . . . . . . . . . 20                 |                                              |
|                                | Single-channel Mode . . . . . . .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 22             |
|                                | Dual-channel Mode and Discrepancy Time. . . . . . . . . . . . . . . . . . 23                         |                                              |
|                                | Dual-channel, Equivalent   . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . 24         |
|                                | Dual-channels, Complementary .  . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . 25                 |
|                                | Safety Input Fault Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26       |                                              |
|                                | Input Delays . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . 26         |
|                                | Safety Analog Inputs - 1734-IE4S.  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . 27               |
|                                | Input Range. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 27           |
|                                | Scale the Input Signals .  . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . 27         |
|                                | Digital Input Filter . .  . . . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . . . 28       |
|                                | Sensor Power Supply. . . . . . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 28             |
|                                | Channel Offset. . . . . . . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 29           |
|                                | Process Alarms . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 29           |
|                                | Use a Single-channel Sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30       |                                              |
|                                | Dual-channel Equivalent Mode .  . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . 31                 |
|                                | Tachometer Mode. . . . . . . . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 32             |

|                              | Safety Outputs - 1734-OB8S, 1734-OBV2S . . . . . . . . . . . . . . . . . . . . . 35                  |                                          |
|------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------|
|                              | Safety Output with Test Pulse .   . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . 35           |
|                              | Dual-channel Mode . . . . . . . .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 36         |
|                              | Single-channel Mode, 1734-OB8S Only . . . . . . . . . . . . . . . . . . . . . 37                     |                                          |
|                              | Safety Output Fault Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37          |                                          |
|                              | Muting Lamp Operation - 1734-IB8S. . . . . . . . . . . . . . . . . . . . . . . . . . . 38            |                                          |
|                              | I/O Status Data . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 39     |
|                              | Digital I/O Status Data . . . . .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 40         |
|                              | Analog I/O Status Data . .  . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . 40       |
|                              | Chapter 3                                                                                            |                                          |
| Place Power Supplies and     | Choose a Power Supply . . . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 41       |
| Modules in a System          | Power Supply Examples. . . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 43       |
|                              | Example 1: Isolate Field Power Segments . . . . . . . . . . . . . . . . . . . . 43                   |                                          |
|                              | Example 2: POINT Guard I/O Used with AC I/O Modules. . 44                                            |                                          |
|                              | Place Series A Digital and Analog Modules . . . . . . . . . . . . . . . . . . . . . . 45             |                                          |
|                              | Place Series B Digital Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 |                                          |
|                              | Chapter 4                                                                                            |                                          |
| Install the Module           | Wire the Modules . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 48     |
|                              | Terminal Layout . . . . . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . 49       |
|                              | Connection Details . . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 50       |
|                              | Wiring Examples. . . . . .  . . . . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . . . 51 |
|                              | Emergency Stop Dual-channel Devices . . . . . . . . . . . . . . . . . . . . . . 51                   |                                          |
|                              | Single-channel Safety Contactor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52           |                                          |
|                              | Dual-channel Safety Contactors  . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . 53             |
|                              | Bipolar Safety Outputs.  . . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . . 54     |
|                              | Safety Analog Input Wiring . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . 55           |
|                              | Chapter 5                                                                                            |                                          |
| Configure the Module in a    | Install the Module on an EtherNet/IP Network . . . . . . . . . . . . . . . . . 61                    |                                          |
| GuardLogix Controller System | Add and Configure the Ethernet Bridge . . . . . . . . . . . . . . . . . . . . . 62                   |                                          |
|                              | Add and Configure the Point I/O Ethernet Adapter . . . . . . . . . 63                                |                                          |
|                              | Add and Configure Safety Digital Input Modules . . . . . . . . . . . . 66                            |                                          |
|                              | Add and Configure Safety Digital Output Modules . . . . . . . . . . 75                               |                                          |
|                              | Add and Configure Safety Analog Input Modules . . . . . . . . . . . . 80                             |                                          |
|                              | Values and States of Tags . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 89     |
|                              | Configure Safety Connections . .  . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 91         |
|                              | Configuration Ownership .  . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . 92     |
|                              | Save and Download the Module Configuration . . . . . . . . . . . . . . . . . . 93                    |                                          |
|                              | Update POINT Guard I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . 93              |                                          |

Chapter 6

| Configure the Module and a     | Before You Begin. . . . . . . . . .  . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 96                                                        |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SmartGuard Controller          | Set the Node Address. . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 96                                                            |
|                                | Auto-address the Nodes with a 1734-PDN Adapter. . . . . . . . . . . . . . 98                                                                                            |
|                                | Set Up the DeviceNet Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100                                                                          |
|                                | Configure the POINT Guard I/O Modules . . . . . . . . . . . . . . . . . . . . 101                                                                                       |
|                                | Configure Digital Safety Inputs and Test Outputs. . . . . . . . . . . 101                                                                                               |
|                                | Configure Digital Safety Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . 104                                                                                |
|                                | Configure Safety Analog Inputs   . . . . . . . . . . . . . .  . . . . . . . . . . . . . 105                                                                             |
|                                | Configure the SmartGuard Controller . . . . . . . . . . . . . . . . . . . . . . . . . 110                                                                               |
|                                | Set Up the Input and Output Connections . . . . . . . . . . . . . . . . . 110                                                                                           |
|                                | Complete the Set Up of the SmartGuard Controller . . . . . . . . 114                                                                                                    |
|                                | Save and Download Module Configuration . . . . . . . . . . . . . . . . . . . . 115                                                                                      |
|                                | Chapter 7                                                                                                                                                               |
| Configure Safety Connections   | Configure the Module in RSNetWorx for DeviceNet Software . . 117                                                                                                        |
| between a GuardLogix           | Add the POINT Guard I/O Module to the Controller Project. . . 118                                                                                                       |
| Controller and POINT Guard I/O | Complete the Safety Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122                                                                           |
| Modules on a DeviceNet         | Download the DeviceNet Network Configuration . . . . . . . . . . . . . . 124 Verify Your DeviceNet Safety Configuration . . . . . . . . . . . . . . . . . . . 125       |
| Network                        | Determine If Devices Can Be Verified. . . . . . . . . . . . . . . . . . . . . . 126                                                                                     |
|                                | Select Devices to Verify . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127                                                                      |
|                                | Review the Safety Device Verification Reports . . . . . . . . . . . . . . 129                                                                                           |
|                                | Lock Safety Devices. .  . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 129                                                                  |
|                                | Chapter 8                                                                                                                                                               |
| Replace POINT Guard I/         | The Safety Network Number . . . . . . . . . .  . . . . . . . . . . . .  . . . . . . . . . . . 131                                                                       |
| O Modules                      | Set the Safety Network Number .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 132                                                                       |
|                                | Reset a Module to Out-of-box Condition . . . . . . . . . . . . . . . . . . . . . . 133                                                                                  |
|                                | Use the Studio 5000 Logix Designer Application. . . . . . . . . . . . 134                                                                                               |
|                                | Use RSNetWorx for DeviceNet Software. . . . . . . . . . . . . . . . . . . 135                                                                                           |
|                                | Replace a Module in a GuardLogix System on an                                                                                                                           |
|                                | EtherNet/IP Network . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 136                                                               |
|                                | Replace a Module with ‘Configure Only When No Safety                                                                                                                    |
|                                | Signature Exists’ Enabled. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137 Replace a Module with ‘Configure Always’ Enabled . . . . . . . . . 142 |
|                                | Use a SmartGuard or GuardLogix Controller on a                                                                                                                          |
|                                | Appendix A                                                                                                                                                              |
| Troubleshoot the Module        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 147                                          |

Appendix B

| Get I/O Diagnostic Status from   | Message Instructions . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 151                   |                                                                                 |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Modules in Logix Systems         | Configure the Message Instruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152                                  |                                                                                 |
|                                  |                                                                                                                                | Class, Instance, and Attribute Data for I/O Modules . . . . . . . . . . . . 153 |
|                                  | Appendix C                                                                                                                     |                                                                                 |
| Safety Data                      | Series A Safety Data . . . . . . .  . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . 158                                           |
|                                  | Series B Safety Data . .  . . . . . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . . . . . . . 160                                       |
|                                  | Product Failure Rates. . . . . . .  . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . 163                                             |
|                                  | Appendix D                                                                                                                     |                                                                                 |
| Configuration Parameters         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 165 |                                                                                 |
|                                  | Appendix E                                                                                                                     |                                                                                 |
| I/O Assemblies                   | Input Assemblies . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 169               |                                                                                 |
|                                  | Output Assemblies . . . . . . . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 171                  |                                                                                 |
|                                  | Analog Input Assemblies. .  . . . . . . . . . . . . . . . . . . .                                                              | . . . . . . . . . . . . . . . . . 171                                           |
|                                  | Configuration Assemblies. . . . .  . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . 173                                               |
|                                  | Use Data from Modules Configured Via the Generic Profile . . . . . 179                                                         |                                                                                 |
| Index                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 181 |                                                                                 |

## Summary of Changes

Thoroughly read and understand this manual before you install and operate a system that uses POINT Guard I/O™ modules.

Always observe the following guidelines when using a module. In this manual, we use safety administrator to mean a person who is qualified, authorized, and responsible to secure safety in the design, installation, operation, maintenance, and disposal of the 'machine'.

- Keep this manual in a safe place where personnel can refer to it when necessary.
- Use the module properly according to the installation environment, performance ratings, and functions of the machine.

See Understand Suitability for Use on page 9 and Safety Precautions on page 11 .

Product specifications and accessories can change at any time. Consult with your Rockwell Automation representative to confirm specifications of the purchased product. Dimensions and weights are nominal and are not for manufacturing purposes, even when tolerances are shown.

Consult your Rockwell Automation representative if you have any questions or comments. Also refer to the related documentation, which is listed on page 8, as necessary.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes. Change bars identify changes in the manual.

| Change                                                        | Pages         |
|---------------------------------------------------------------|---------------|
| Updated the Light Curtain Test Pulse information              | 50            |
| Updated the description of the Dual-channel Safety Contactors | 53            |
| Updated the pulse testing information                         | 159, 162, 163 |

## Terminology

## Table 1 - Common Terms

| Term Means                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connection Logical communication channel for communication between nodes. Connections are maintained and controlled between leaders and followers.                                                                                                                                             |
| EDS Electronic data sheet a template that is used in RSNetWorx™ software to display the configuration parameters, I/O data profile, and connection-type support for a given I/O module. RSNetWorx software uses these simple text files to identify products and commission them on a network. |
| PFD Probability of a dangerous failure on demand, the average probability of a system to fail to perform its design function on demand.                                                                                                                                                        |
| PFH Average frequency of a dangerous failure per hour, the probability of a system to have a dangerous failure occur per hour.                                                                                                                                                                 |
| Proof test Periodic test that detects failures in a safety-related system so that, if necessary, the system can be restored to an as-new condition or as close as practical to this condition.                                                                                                 |
| SNN Safety network number, which uniquely identifies a network across all networks in the safety system. You must assign a unique number for each safety network or safety subnet within a system.                                                                                             |
| Standard Devices or portions of devices that do not participate in the safety function.                                                                                                                                                                                                        |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

|                                                                                                | Resource Description                                                                                                                      |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| POINT Guard I/O Safety Modules Installation Instructions, publication 1734-IN016               | Provides installation information for the safety I/O modules.                                                                             |
| POINT I/O Selection Guide, publication 1734-SG001                                              | Provides selection information for all POINT I/O™ modules.                                                                                |
| GuardLogix 5570 Controllers User Manual, publication 1756-UM022                                | Provides information on how to install, configure, program, and use GuardLogix® 5570 controllers in Studio 5000 Logix Designer® projects. |
| GuardLogix 5570 Controller Systems Safety Reference Manual, publication 1756-RM099             | Provides information on safety application requirements for GuardLogix 5570 controllers in Studio 5000 Logix Designer projects.           |
| GuardLogix Controller Systems Safety Reference Manual, publication 1756-RM093                  | Provides information on safety system requirements and describes the GuardLogix controller system.                                        |
| GuardLogix Controllers User Manual, publication 1756-UM020                                     | Provides information on how to install, configure, program, and use GuardLogix controllers in RSLogix 5000® projects.                     |
| GuardLogix Safety Application Instructions Safety Reference Manual, publication 1756-RM095     | Provides reference information that describes the GuardLogix Safety Application Instruction Set.                                          |
| SmartGuard 600 Controllers Safety Reference Manual, publication 1752-RM001                     | Describes SmartGuard™ 600-specific safety requirements and controller features.                                                           |
| Field Potential Distributor Installation Instructions, publication 1734-IN059                  | Provides installation information for 1734-FPD distributors.                                                                              |
| POINT I/O 24V DC Expansion Power Supply Installation Instructions, publication 1734-IN058      | Provides installation information for 1734-EP24DC power supplies.                                                                         |
| POINT I/O 120/240V AC Expansion Power Supply Installation Instructions, publication 1734-IN017 | Provides installation information for 1734-EPAC power supplies.                                                                           |
| POINT I/O Terminal Base Assembly Installation Instructions, publication 1734-IN511             | Provides installation information for 1734-TB and 1734-TBS assemblies.                                                                    |
| POINT I/O One-piece Terminal Base Installation Instructions, publication 1734-IN028            | Provides installation information for 1734-TOP, 1734-TOPS, 1734-TOP3, and 1734-TOP3S terminal bases.                                      |
| ODVA Media Planning and Installation Guide, www.odva.org                                       | Describes the required media components and how to plan for and install these required components.                                        |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                    | Provides general guidelines for installing a Rockwell Automation industrial system.                                                       |
| Product Certifications website, rok.auto/pec                                                   | Provides declarations of conformity, certificates, and other certification details.                                                       |

You can view or download publications at rok.auto/literature .

## Understand Suitability for Use

## POINT Guard I/O Overview

| Topic Page                                       |
|--------------------------------------------------|
| Understand Suitability for Use 9                 |
| Safety Precautions 11                            |
| POINT Guard I/O Modules in CIP Safety Systems 13 |
| Safety Application Requirements 17               |

Use the POINT Guard I/O™ safety modules in the POINT I/O™ platform to distribute safety I/O on a safety-control network that meets the requirements up to and including SIL CL3, and PLe, Cat. 4 as defined in IEC 61508, IEC 61511, IEC 62061, and ISO 13849-1. Guard I/O™ modules can be used with GuardLogix® controllers, Compact GuardLogix controllers, and SmartGuard™ controllers.

Configure the modules for use on DeviceNet® networks with RSNetWorx™ for DeviceNet software. For Ethernet networks, use the Studio 5000 Logix Designer® application.

Rockwell Automation is not responsible for conformity with any standards, codes, or regulations that apply to the combination of the products in your application or use of the product. For more information see the POINT Guard I/O Safety Modules Installation Instructions, publication 1734-IN016, and the Point I/O Selection Guide, publication 1734-SG001 .

Take all necessary steps to determine the suitability of the product for the systems, machine, and equipment with which it is used.

Know and observe all prohibitions of use applicable to these products.

Use this equipment within its specified ratings.

Before you use these products for an application that involves serious risk to life or property, verify that the whole system is designed to address the risks. Be sure that Rockwell Automation products are properly rated and installed for the intended use within the overall equipment or system.

Download firmware and product release notes from Rockwell Automation's Product Compatibility and Download Center. Do not download firmware from non-Rockwell Automation sites.

Table 1 - Requirements for Device Control

|                                                  |                                                                                                                                                                                  | Device Requirement Allen-Bradley® Bulletin Safety Components                        |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|                                                  | Emergency stop switches Use approved devices with direct opening mechanisms that comply with IEC/EN 60947-5-1.                                                                   | Bulletin 800F, 800T                                                                 |
| Door interlocking switches, limit switches       | Use approved devices with direct opening mechanisms that comply with IEC/EN 60947-5-1 and capable of switching microloads of 24V DC, 3 mA.                                       | Bulletin 440K, 440G, 440H for interlock switch Bulletin 440P, 802T for limit switch |
|                                                  | Safety sensors Use approved devices that comply with the relevant product standards, regulations, and rules in the country where used.                                           | Any Guardmaster® product                                                            |
| Relays with forcibly-guided contacts, contactors | Use approved devices with forcibly guided contacts that comply with EN 50205. For feedback purposes, use devices with contacts capable of switching micro loads of 24V DC, 3 mA. | Bulletin 700S, 100S                                                                 |
|                                                  | Other devices Evaluate whether the devices used are appropriate to satisfy the requirements of safety category levels.                                                           | –                                                                                   |

Verify that the POINT Guard I/O firmware revision is correct before you commission the safety system. Firmware information for safety I/O modules is available at rok.auto/pec .

<!-- image -->

Field power must be applied to the 1734-IE4S module when you update the firmware.

Verify that a safety administrator conducts a risk assessment on the machine and determines module suitability before installation.

<!-- image -->

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in the use of the system.

<!-- image -->

ATTENTION: Use only appropriate components or devices that comply with relevant safety standards that correspond to the required safety category and safety integrity level.

- Conformity to requirements of the safety category and safety integrity level must be determined for the entire system.
- We recommend that you consult a certification body regarding assessment of conformity to the required safety integrity level or safety category.

You must confirm that the entire system is in compliance with the applicable standards.

## Safety Precautions

Observe these precautions for proper use of POINT Guard I/O modules.

<!-- image -->

ATTENTION: As serious injury can occur due to loss of required safety function, follow these safety precautions.

- Never use test outputs as safety outputs. Test outputs are not safety outputs.
- Do not use Ethernet, DeviceNet, or ControlNet® standard I/O data or explicit message data as safety data.
- Do not use status indicators on the I/O modules for safety operations.
- Do not connect loads beyond the rated value to the safety outputs.
- Apply properly specified voltages to the module. If you apply inappropriate voltages, the module may fail to perform the specified functions, which could lead to loss of safety functions or damage to the module.
- To wire the POINT Guard I/O modules properly, use the wiring requirements and guidelines in Wire the Modules on page 48 .
- Before you connect a device to the network, set a unique network node address.
- To confirm that device wiring, configuration, and operation is correct before you begin system operation, perform the applicable tests.
- Do not disassemble, repair, or modify the module. This can result in the loss of safety functions.

## Install or Replace Modules

<!-- image -->

## ATTENTION:

- Before you connect devices to the network or connect input or output power to the device, clear previous configuration data.
- Configure the replacement device properly and confirm that it operates correctly.
- When you install or replace a module, follow the instructions and safety precautions in the POINT Guard I/O Safety Modules Installation Instructions, publication 1734-IN016 .
- After the module is installed, a safety administrator must confirm the installation and conduct trial operation and maintenance.

When you clean a module, do not use these chemicals.

- Thinner
- Benzene
- Acetone

## Limit Access to the System

When you limit access to a device to authorized users only, consider these options:

- Password protect the source and execution of the control program
- Remove the key from the controller
- Deploy EtherNet/IP™ devices in accordance with recommended architectures and concepts. See the Converged Plantwide Ethernet (CPwE) Design and Implementation Guide, publication ENET-TD001
- Implement physical barriers, such as locked cabinets

To limit access to the system, consider these options:

- Follow industry best practices to harden your personal computers and servers, like antivirus/anti-malware and application allow list solutions. These recommendations are published in Knowledgebase Document ID PN767 .
- Develop and deploy backup and disaster recovery policies and procedures. Test backups on a regular schedule.
- Minimize network exposure for all control system devices and systems, and verify that they are not accessible from the Internet.
- Locate control system networks and devices behind firewalls and isolate them from the business network.
- Subscribe to Rockwell Automation's Security Advisory Index, Knowledgebase Document ID PN1354, so you have access to information about security matters that affect Rockwell Automation products.

## POINT Guard I/O Modules in CIP Safety Systems

POINT Guard I/O modules are used in the POINT I/O platform and implement CIP Safety™ protocol extensions over EtherNet/IP and DeviceNet networks to communicate safety messages. POINT Guard I/O modules connect to EtherNet/IP or DeviceNet networks via these network adapters.

Table 2 - Network Adapters

| Network System Adapter (1)                                      |
|-----------------------------------------------------------------|
| EtherNet/IP GuardLogix 1734-AENT (Firmware Revision 3 or later) |
| 1734-AENTR                                                      |
| DeviceNet SmartGuard or GuardLogix 1734-PDN                     |

Distributed I/O communication for safety I/O data is performed through safety connections that support CIP Safety over an EtherNet/IP or DeviceNet network. Data is processed in the safety controller. A control monitors the status and fault diagnostics of POINT Guard I/O modules.

In addition to I/O state data, the modules include status data to monitor I/O faults within each circuit.

A password can help protect the configuration information of the modules.

## 1734-IB8S Digital Input Module Features

- Safety digital inputs
- – Safety devices, such as an Emergency Stop Push Button, gate switches, and safety light curtains, can be connected.
- – Dual-channel mode evaluates consistency between two input signals (channels), which allows use of the module for safety Category 3 and 4 and in applications that are rated up to and including PLe/SIL CL3 when both channels' Point Mode configurations are set to Safety Pulse Test.
- – Single-channel mode evaluates one input signal (channel), which allows use of the module for safety Category 2 and in applications that are rated up to and including PLd/SIL CL2 when the channel's Point Mode configuration is set to Safety Pulse Test.
- – You can configure a discrepancy time to control how long two channels are allowed to be discrepant before a fault is declared.
- – It is possible to perform an external wiring short circuit check when inputs are wired in combination with test outputs. The module must be wired in combination with test outputs when this function is used.
- – Independently adjustable on and off delays are available per channel.

- Test outputs (digital input modules only)
- – Separate test outputs are provided for short circuit detection of a safety input (or inputs).
- – Power (24V) can be supplied to devices, such as safety sensors.
- – Test outputs can be configured as standard outputs.
- – Specific test outputs can be used for broken-wire detection of a muting lamp.

## 1734-OB8S Safety Digital Output Module Features

- Solid-state outputs
- Dual-channel mode provides redundant control with two output signals (channels), which lets you use the module for safety Category 3 and 4, and applications that are rated up to and including PLe/SIL CL3 when both channels' Point Mode configurations are set to Safety Pulse Test.
- Single-channel mode provides control with one output signal (channel), which allows use of the module for safety Category 2, and applications that are rated up to and including PLd/SIL CL2 when the channel's Point Mode configuration is set to Safety Pulse Test.

## IMPORTANT

1734-OB8S Single-channel mode is only certified for functional safety applications with process safety times greater than or equal to 600 ms; or, applications with demand rates less than or equal to 1 demand per minute.

- Safety outputs can be pulse-tested to detect field wiring short-circuits to 24V DC.

## 1734-OBV2S POINT Guard I/O Module Features

- Four bipolar outputs (two pairs)
- Dual-channel mode provides redundant control with two output signals (channels), which allows use of the module for safety Category 3 and 4, and applications that are rated up to and including PLe/SIL CL3 when both channels' Point Mode configurations are set to Safety Pulse Test.
- Safety outputs can be pulse-tested to detect field wiring short-circuits to 24V DC (for the sourcing output of the bipolar pair) and ground (for the sinking output of the bipolar pair).

## 1734-IE4S Safety Analog Input Module Features

- Connection of up to four voltage or current sensors.
- Sensor power outputs are individually current-limited and monitored.
- Measurement of process variables, such as temperature, pressure, or flow rate.
- Seven configurable input ranges. ±10V, ±5V, 0…5V, 0…10V, 4…20 mA, 0…20 mA, Tachometer
- Tachometer mode converts 24V DC switching signals into pulses per second.
- Single-channel or dual-channel for SIL 3-rated safety devices and applications.
- Dual-channel mode evaluates the consistency between two input signals (channels), which allows use of the module in applications that are rated up to and including SIL CL3/PLe/Cat. 4.
- You can configure a discrepancy time to control how long two channels are allowed to be discrepant before a fault is declared.

## Programming Requirements

Use the minimum Software Versions listed here.

|                                                | Cat. No. Studio 5000® Environment Version   | RSLogix 5000® Software Version (EtherNet/IP Network)   | RSNetWorx for DeviceNet Software Version (DeviceNet Network)   |
|------------------------------------------------|---------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------|
| 1734-IB8S, 1734-OB8S                           |                                             | 21 or later 17(1) or later                             | 9 or later                                                     |
| 1734-OBV2S 21 or later 18 or later 21 or later |                                             |                                                        |                                                                |
|                                                |                                             | 1734-IE4S 21 or later 18(2) or later                   | 10 or later                                                    |

## CIP Safety Architectures

Use POINT Guard I/O modules in EtherNet/IP or DeviceNet safety architectures. Safety controllers control the safety outputs. Safety or standard PLC controllers can control the standard outputs.

Figure 1 - POINT Guard I/O Modules in EtherNet/IP Safety Architecture

<!-- image -->

Figure 2 - POINT Guard I/O Modules in DeviceNet Safety Architectures

<!-- image -->

## Safety Application Requirements

POINT Guard I/O modules are certified for use in safety applications up to and including PLe/Cat. 4 and SIL CL3 in which the de-energized state is the safe state. Safety application requirements include evaluation of probability of failure rates (PFD and PFH), system reaction time settings, and functional verification tests that fulfill SIL 3 criteria.

Creating, recording, and verifying the safety signature is also a required part of the safety application development process. The safety controller creates the safety signatures. The safety signature consists of an identification number, date, and time that uniquely identifies the safety portion of a project. This number includes all safety logic, data, and safety I/O configuration.

For safety system requirements, including information on the safety network number (SNN), verifying the safety signature, functional verification test intervals, system reaction time, and PFD/PFH calculations, refer to the following publications.

| For safety requirements in: See:                                                                                 |
|------------------------------------------------------------------------------------------------------------------|
| GuardLogix controller systems GuardLogix 5570 Controller Systems Safety Reference Manual, publication 1756-RM099 |
| SmartGuard 600 controller systems SmartGuard 600 Controllers Safety Reference Manual, publication 1752-RM001     |

You must read, understand, and fulfill the requirements that are detailed in these publications before operating a safety system that uses POINT Guard I/O modules.

## Notes:

## Safe States

<!-- image -->

## Safety Inputs, Safety Outputs, and Safety Data

| Topic Page                                |
|-------------------------------------------|
| Safe States 19                            |
| Safety Inputs - 1734-IB8S 20              |
| Safety Analog Inputs - 1734-IE4S 27       |
| Safety Outputs - 1734-OB8S, 1734-OBV2S 35 |
| Muting Lamp Operation - 1734-IB8S 38      |
| I/O Status Data 39                        |

## POINT Guard Digital I/O Modules

<!-- image -->

## ATTENTION:

- The safe state of the outputs is defined as the off state.
- The safe state of the module and its data is defined as the off state.
- Use the POINT Guard I/O™ module only in applications where the off state is the safe state.

## The digital POINT Guard I/O™ modules have these safe states:

- Safety outputs: OFF
- Safety input data to network: OFF (single channel and dual-channel equivalent)
- Safety input data to network: OFF/ON for input channels n/n+1 (dual-channel complementary)

Figure 3 - Safety Status

<!-- image -->

The module is designed for use in applications where the safe state is the off state.

## Safety Inputs - 1734-IB8S

## POINT Guard I/O Analog Input Module

The analog input POINT Guard I/O module has these safe states:

- Safety input data to network in single-channel configuration: 0 (OFF)
- Safety input data to network in dual-channel equivalent configuration:
- – If a diagnostic fault occurs, the signal for the faulted channel is set to 0 (OFF).
- – If a dual-channel discrepancy fault occurs, the dual-channel inputs continue to report actual input signals.

Safety inputs are used to monitor safety input devices.

## Use a Test Output with a Safety Input

A test output can be used in combination with a safety input for short circuit, cross-channel, and open-circuit fault detection. Configure the test output as a pulse test source and associate it to a specific safety input.

<!-- image -->

The test output can also be configured as a power supply to source 24V DC to an external device, for example, a light curtain.

Figure 4 - Example Use of a POINT Guard I/O Input Module

<!-- image -->

Figure 5 - Test Pulse in a Cycle

<!-- image -->

For the 1734-IB8S module, the pulse width (X) is typically 525 μs; the pulse period (Y) is typically 144 ms.

When the external input contact is closed, a test pulse is output from the test output terminal to diagnose the field wiring and input circuitry. When you use this function, short-circuits between inputs and 24V power, and between input signal lines and open circuits can be detected.

Figure 6 - Short-circuit between Input Signal Lines

<!-- image -->

## Single-channel Mode

If an error is detected, safety input data and safety input status turn off.

Figure 7 - Normal Operation and Fault Detection (Not to Scale)

<!-- image -->

| Normal Operation             | Test Output 0                        | 24V           |                |
|------------------------------|--------------------------------------|---------------|----------------|
| Safety I/O Network Data Sent | Safety Input 0 Data                  | ON OFF        |                |
| Fault Detection              | External Device Test Output 0        | 0V ON OFF     |                |
| Safety I/O Network Data Sent | Safety Input 0 Data Input Terminal 0 | ON OFF ON OFF | Fault Detected |
| to the Controller            | Safety Input 0 Status                | ON OFF        |                |

## Dual-channel Mode and Discrepancy Time

To support dual-channel safety devices, the consistency between signals on two channels can be evaluated. Either equivalent or complementary can be selected.

If the length of a discrepancy between the channels exceeds the configured discrepancy time (10…65,530 ms in increments of 10 ms), the safety input data and the individual-safety input status turn off for both channels. In Dual-channel Complimentary mode, the safety input data goes to off/on for input channels n/n+1 respectively as described in Table 3 .

## IMPORTANT

The dual-channel function is used with two consecutive inputs that are paired together, and start at an even input number, such as inputs 0 and 1, 2 and 3.

## IMPORTANT

If you use the safety application instructions with a GuardLogix® controller, set the inputs of the module inputs to Single (default). Do not use the dual-channel mode of the module, as this functionality is provided by the safety application instructions.

This table shows the relation between input terminal states and controller input data and status.

Table 3 - Terminal Input Status and Controller I/O Data

| Dual-channel Mode Input Terminal Controller Input Data and Status Dual-channel   |                                                        | Dual-channel Resultant         |
|----------------------------------------------------------------------------------|--------------------------------------------------------|--------------------------------|
| Dual-channel Mode Input Terminal Controller Input Data and Status Dual-channel   | IN0 IN1 Safety Input 0 Data Safety Input 1 Data Safety | Dual-channel Resultant         |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                       |                                                        |                                |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                       | OFF ON OFF OFF OFF OFF OFF Fault                       |                                |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                       | ON OFF OFF OFF OFF OFF OFF Fault                       |                                |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                       |                                                        | ON ON ON ON ON ON ON Normal    |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                    |                                                        |                                |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                    |                                                        | OFF ON OFF ON ON ON OFF Normal |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                    |                                                        | ON OFF ON OFF ON ON ON Normal  |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                    |                                                        | ON ON OFF ON OFF OFF OFF Fault |

## Dual-channel, Equivalent

In Equivalent mode, both inputs of a pair must be in the same (equivalent) state. When a transition occurs in one channel of the pair before the transition of the second channel of the pair, a discrepancy occurs. If the second channel transitions to the appropriate state before the discrepancy time elapses, the inputs are considered equivalent. If the second transition does not occur before the discrepancy time elapses, the channels will fault. In the fault state, the input and status for both channels are set low (OFF). When configured as an equivalent dual pair, the data bits for both channels are sent to the controller as equivalent, both high or both low.

Figure 8 - Equivalent, Normal Operation and Fault Detection (Not to Scale)

<!-- image -->

## Dual-channels, Complementary

In Complementary mode, the inputs of a pair must be in the opposite (complementary) state. When a transition occurs in one channel of the pair before the transition of the second channel of the pair, a discrepancy occurs. If the second channel transitions to the appropriate state before the discrepancy time elapses, the inputs are considered complementary.

If the second transition does not occur before the discrepancy time elapses, the channels will fault. The fault state of complementary inputs is the even-numbered input that is turned off and the odd-numbered input turned ON. Note that if faulted, both channel status bits are set low. When configured as a complementary dual-channel pair, the data bits for both channels are sent to the controller in complementary, or opposite states.

Figure 9 - Complementary, Normal Operation and Fault Detection (Not to Scale)

<!-- image -->

## Safety Input Fault Recovery

If an error is detected, the safety input data remains in the OFF state. Follow this procedure to activate the safety input data again.

1. Remove the cause of the error.
2. Place the safety input (or safety inputs) into the safe state.
3. Allow the input-error latch time to elapse.

After these steps are completed, the I/O indicator (red) turns off. The input data is now active.

## Input Delays

On-delay - An input signal is treated as Logic 0 in the on-delay time (0…126 ms, in increments of 6 ms) after the rising edge of the input contact. The input turns on only if the input contact remains on after the on-delay time has elapsed. This setting helps prevent rapid changes of the input data due to contact bounce.

Figure 10 - On-delay

<!-- image -->

Off-delay - An input signal is treated as Logic 1 in the off-delay time (0…126 ms, in increments of 6 ms) after the falling edge of the input contact. The input turns off only if the input contact remains off after the off delay time has elapsed. This setting helps prevent rapid changes of the input data due to contact bounce.

<!-- image -->

## Safety Analog Inputs 1734-IE4S

Safety analog-input channels can be configured for current, voltage, or tachometer inputs, and for input type: single-channel or dual-channel equivalent.

## IMPORTANT

If you use the module with a GuardLogix controller, set the inputs of the module to Single (default). Do not use the dual-channel equivalent mode of the modules with the GuardLogix dual channel safety application instructions, as dual-channel functionality is provided by the GuardLogix instructions.

## Input Range

You can configure the module for these voltage or current input ranges, or for tachometer inputs.

- ±10V
- ±5V
- 0…5V
- 0…10V
- 4…20 mA
- 0…20 mA
- Tachometer (1…1000 Hz)

## IMPORTANT

When ±10V and ±5V ranges are selected, you must make sure that a broken-wire condition is not a safety hazard. A broken wire causes the analog value to transition to 0, which is within the valid input range. Therefore, status bits do not indicate the broken-wire condition.

## Scale the Input Signals

The module converts input signals to the engineering units specified when you configure the module. You set the High Engineering value and the Low Engineering value to which the module scales the input signal before the data is sent to the application program of the controller.

## EXAMPLE

The module is configured as follows:

- Input Range = 0…10V
- Low Engineering value = 0
- High Engineering value = 10,000

If the incoming signal is 1V, the data is 1000.

If the incoming signal is 5.5V, the data is 5500.

## Digital Input Filter

A single-pole, anti-alias filter of 10 Hz is followed by a four-pole digital filter. Choose from these available corner frequencies.

- 1 Hz
- 5 Hz
- 10 Hz
- 50 Hz

The default input filter setting is 1 Hz.

Figure 12 - Filter Operation

<!-- image -->

The filter setting affects the step response of the module. For more information, see the Point I/O Selection Guide, publication 1734-SG001 .

For the analog input modes, the input filter settings set the low-pass filter to filter out noise that can be present on the signal. In Tachometer mode, the input filter removes noise that can be present on the calculated frequency, this effectively changes how rapidly the tachometer frequency changes to provide a value with less jitter.

## Sensor Power Supply

You can configure the module to supply power to the connected sensors, or you can supply power to the sensors from an external power supply. To comply with UL restrictions, you must power the field power and connected devices with one, Class 2-complaint power supply.

We recommend that you configure the module to supply power to the sensors. This configuration lets the module detect if a sensor loses power, if the sensor draws too much power, or if there is a short in the power wiring to the sensor.

At powerup or after a reconfiguration, each sensor power supply is turned on for 500 ms to test them.

When a channel is configured for module sensor power, a sensor power diagnostic is executed on that channel at powerup. The diagnostic is used to make sure that the sensors do not draw over- or undercurrent and that channel-to-channel shorts are not present.

<!-- image -->

When a sensor power overcurrent condition occurs, it can take as much as 15 seconds longer than the configured latch time for channel status to recover after the overcurrent condition is cleared.

## IMPORTANT

If you use an external power supply, you must monitor the system for the following:

- The supply voltage must be within the operating range of the sensor.
- The current draw of the sensors must not be over- or undercurrent-current, which could indicate a problem with the components of the sensor.
- Channel-to-channel shorts must be detected, if they occur.

## Channel Offset

You can configure an offset if differences of the nominal input signal in the sensor exceed the desired discrepancy deadband. Use the Channel Offset if you use two sensors of different types to measure the same variable. Sensors from two different vendors potentially give slightly different data values for a given temperature or pressure. Use the Channel Offset to bring the data values back together. You can also use the Channel Offset with two identical sensors that are physically offset from each other.

The channel offset is applied before the channel discrepancy is evaluated.

<!-- image -->

The Channel Offset is applied only during the evaluation of discrepancy between two channels that are configured for Dual Channel and is not applied to any of the Process Alarms. Therefore, if you use two sensors to measure the same process variable, and these sensors read different values, you may need to set the Process Alarms to different values based on the sensor readings.

## Process Alarms

Process alarms alert you when an analog input value has exceeded the configured high or low limits for each channel. Process alarms are set at four configurable trigger points.

- High High alarm
- High alarm
- Low alarm
- Low Low alarm

You can configure a tolerance range, called a deadband, to work with process alarms. This deadband lets the process alarm status bit remain set, despite the disappearance of the alarm condition, as long as the data remains within the deadband of the process alarm.

## IMPORTANT

If you use the safety application instructions with a GuardLogix controller, do not use the process alarm of the module. Instead, check the analog range in your application logic.

Figure 13 - Alarms

<!-- image -->

## Use a Single-channel Sensor

You must address these requirements to meet SIL 3 with a single-channel sensor.

- The module's ±10V and ±5V analog input modes must not be used for SIL 3 with a single-channel sensor because 0V falls within the valid input range. Therefore, a stuck at ground fault cannot be detected.
- In a single-channel sensor system, you must use other methods to make sure a channel-to-channel short cannot occur because these faults cannot be detected.
- If you use a 3-wire sensor, you must verify its behavior to make sure that if it loses its ground connection, the signal is 0 (safe state) at the module input when the fault occurs.

## Dual-channel Equivalent Mode

## IMPORTANT

If you use the module with a GuardLogix controller, set the inputs of the module to Single (default). Do not use the dual-channel mode of the module as this functionality is provided by the GuardLogix safety application instructions.

The 1734-IE4S module supports Dual-channel Equivalent mode. In Dual-channel Equivalent mode, the values of both inputs of a pair must be within a configured tolerance range (discrepancy deadband). If the difference between the channel values exceeds the deadband for longer than the configured discrepancy time, a discrepancy fault is declared. When a dual-channel discrepancy fault occurs, the input status values for both channels are set low (off ) and the actual input values are reported. The fault is cleared when the difference between the values of the channel fall back within the discrepancy deadband tolerance range for the discrepancy time.

Figure 14 illustrates module operation in dual-channel equivalent mode. At A, the difference between the channel values exceeds the discrepancy deadband tolerance range and the discrepancy timer starts. When the timer expires at B, a dual-channel discrepancy fault occurs and the status bits of the input are set low. At C, the values fall back within the discrepancy deadband and the discrepancy timer starts again. When the timer expires at D, and the values are still within the discrepancy deadband, the fault is cleared. At E, the difference between the channels exceeds the discrepancy deadband and the discrepancy timer starts. A discrepancy fault occurs again at F, when the timer expires and the difference between the channel values remains greater than the discrepancy deadband.

Figure 14 - Timing Diagram

<!-- image -->

## Tachometer Mode

In Tachometer mode, the module measures digital pulses from 0V…24V DC, and converts them into a frequency or pulses per second. Therefore, you can use 24V DC proximity sensors or 5V DC encoders, for example. The Tachometer function does not sense direction, so the use of a differential encoder does not yield direction data. Tachometer mode could be used, for example, to measure the rotational speed of an axis that is connected to a gear.

Tachometer mode can operate as SIL 2 single-channel. Use two sensors, the dual-low detection parameter, and user program logic to achieve SIL 3. Safety reaction time is dependent on the signal frequency.

## IMPORTANT

When you use two sensors in a dual-channel configuration, position the sensors to make sure that the low pulses occur at different times. If you have configured the module for dual low detection and both sensors are low simultaneously, a fault is declared.

Figure 15 - Sensor Pulses in Dual-channel Configuration

<!-- image -->

## Signal Measurement

The edge-to-edge time of the pulse determines the frequency of the signal in pulses per second. The frequency range is 1 Hz…1 kHz.

In Tachometer mode, you define how the signal is measured, either on the falling (non-inverted) or rising (inverted) edge. For NPN-style sensors (sensor sinks), use the falling edge. For PNP-style sensors (sensor sources), use the rising edge. Depending on your application, you may need to install an appropriately sized pull-up resistor for falling-edge signal measurements, or a pull-down resistor for rising-edge signal measurements.

Figure 16 - Pulse Trains

<!-- image -->

## Off and On Signal Levels

You configure the Off and On levels, in 1V increments, for the signal. When you select these levels, assume a tolerance of at least ±0.5V. For example, if you set the On Level to 10V, you can expect the module to recognize a signal from 9.5V…10.5V as On. While the accuracy of the module when it measures the analog signal is good, Tachometer mode emphasizes a wider voltage range and speed to be able to measure pulse widths accurately.

Also consider the variance of the voltage output from your sensor when you make the On and Off Level settings. If possible, we recommend that you select On Levels that are 2V below and Off Levels that are 2V above the actual thresholds of the expected output voltage level of your device.

## Determine Frequency in Pulses per Second

The edge-to-edge time of either the falling or rising edge of the pulse determines the frequency in pulses per second.

<!-- image -->

One pulse, by itself, does not generate a nonzero frequency. To report a frequency of 1 Hz, two falling or rising edge pulses must be detected within 1 second. The module reports 0 Hz until 1 Hz is detected. For example, if a falling or rising edge is not detected for 1.02 seconds after the previous edge, the module reports 0 Hz.

## Overfrequency Bit Operation

When the frequency exceeds 1 kHz, the module reports a data value of 1 kHz, sets the Overfrequency status bit to 0, and latches it. While the Overfrequency bit is set to 0, you must use an alternate method to monitor the frequency of the system because the value reported by the module is latched at 1 kHz. Once you have verified that the frequency is lower than 1 kHz, you can reset the Overfrequency condition by setting the Reset Tach bit, which lets the module begin to measure the frequency of field pulses again.

If you set the Reset Tach bit while the frequency is still above 1 kHz, the Tachometer Overfrequency bit transitions to 1 (within range) momentarily. However, as soon as the module begins to measure pulses, it detects another overfrequency condition and immediately set the Tachometer Overfrequency bit to 0 again. The Reset Tach bit is edge-sensitive.

<!-- image -->

ATTENTION: Before you reset the Overfrequency condition, you must use another method to verify that the actual frequency is lower than 1 kHz.

See Output Assemblies on page 171 for more information on how to reset the Overfrequency bit.

Figure 17 - Overfrequency Operation

<!-- image -->

In Figure 17, the module reports a frequency of 0 Hz until the frequency of the system reaches 1 Hz at A, when the module begins to report the actual value. At B, the frequency exceeds 1 kHz, the Overfrequency bit is set to 0, and the module continues to report a data value of 1 kHz. Between B and C, you must monitor the frequency by an alternate method because the value that is reported by the module is not always accurate. After C, the Overfrequency condition can be cleared, provided you have used an alternate method to verify that the actual frequency is below 1 kHz.

## Safety Outputs 1734-OB8S, 1734-OBV2S

Read this section for information about safety outputs.

## Safety Output with Test Pulse

When the safety output is on, the safety output can be configured to pulse test the safety output channel. This function lets you continuously test the ability of the safety output to remove power from the output terminals of the module. If an error is detected, the safety output data and individual safety output status turn off.

Figure 18 - Test Pulse in a Cycle

<!-- image -->

For the 1734-OB8S and 1734-OBV2S modules, the pulse width (X) is typically 475 μs; the pulse period (Y) is typically 575 ms.

IMPORTANT

To help prevent a malfunction in the connected device because of the test pulse, pay careful attention to the input response time of the output device.

## Dual-channel Mode

When the data of both channels is in the on state, and neither channel has a fault, the outputs are turned on. The status is normal. If a fault is detected on one channel, the safety output data and individual safety output status turn off for both channels.

Figure 19 - Set the Dual-channel Mode (Not to Scale)

<!-- image -->

## Single-channel Mode, 1734-OB8S Only

When the data of the channel is in the on state, and does not have a fault, the output is turned on. The status is normal. If a fault is detected on the channel, the safety output data and individual safety output status turn off.

Figure 20 - Set the Single-channel Mode (Not to Scale)

<!-- image -->

## Safety Output Fault Recovery

If a fault is detected, the safety outputs are switched off and remain in the off state. Follow this procedure to activate the safety output data again.

1. Remove the cause of the error.
2. Command the safety output (or safety outputs) into the safe state.
3. Allow the output-error latch time to elapse.

After these steps are completed, the I/O indicator (red) turns off. The output data can now be controlled.

IMPORTANT

Stuck high faults require a module power reset to clear the error.

## Muting Lamp Operation 1734-IB8S

With firmware revision 1.002 and later, the operation of the muting status bits for test outputs T1 and T3 has changed. Your PLC processor program controls test outputs T1 and T3 to illuminate a muting lamp. Muting lamp status is monitored with a test that runs periodically during every test interval to detect a burned-out lamp. The test runs repeatedly when the test output is commanded on. Figure 21 explains how muting lamp operation, status, and fault detection are monitored.

<!-- image -->

The lamp test interval is 3 seconds. Two consecutive failed lamp tests are required to declare a burned-out lamp condition. The lamp test does not always run immediately after the test output is energized. It starts at the next 3-second interval. To allow time for two consecutive test intervals, program a minimum Test Output On Time of 6 seconds.

Figure 21 - Muting Lamp Timing Diagram

<!-- image -->

*NOTE: Output controlled by User's program, not by Muting Status bit.

Table 4 shows the expected behavior of the muting status for test outputs T1 and T3. Keep these points in mind as well:

- When power is applied to the 1734-IB8S module, and T1 or T3 remains commanded off, the muting status defaults to on.

## I/O Status Data

This bit operation is designed to help prevent erroneous muting instruction faults from the GuardLogix controller. This bit status is not always the true indication of a burned-out lamp.

## IMPORTANT

Before you check the state of the corresponding muting status, be sure that the test output is commanded on. Once the test output is commanded on, a maximum time of 6 seconds is required for the module to detect a burned-out lamp.

- If a muting lamp circuit is open when power is applied to the module, the condition is detected when the test output is commanded on.
- When a lamp burns out and is replaced, the fault (muting status bit) returns to the normal condition, independent of the state of the test output.

## Table 4 - Muting Status Bit Operation

| Test Output Commanded State   | Lamp Condition Muting Status Bit   | Description                                                                                            |
|-------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------|
|                               |                                    | ON Bad (open circuit) 0 Repair the lamp.                                                               |
|                               |                                    | ON Good 1 Normal condition. The lamp is operating properly.                                            |
|                               |                                    | OFF Bad (open circuit) 0 If the lamp remains OFF after you cycle the T1 or T3 output, repair the lamp. |
|                               |                                    | OFF Good 1 Normal condition.                                                                           |

In addition to I/O data, the module also provides status data to monitor the I/O circuits. The status includes diagnostic data that the controllers read with 1 = ON/Normal and 0 = OFF/Fault/Alarm.

## Digital I/O Status Data

This status data is monitored:

- Individual Point Input Status
- Combined Input Status
- Individual Point Output Status
- Combined Output Status
- Individual Test Output Status
- Individual Output Monitor (actual ON/OFF state of the outputs)

Individual Point status indicates whether each safety input, safety output, or test output is normal (normal: ON, faulted: OFF). For fatal errors, communication connections can be broken, so the status data cannot be read. Status bits are OFF in the controller data table when the connection is lost.

Combined status is provided by an AND of the status of all safety inputs or all safety outputs. When all inputs or outputs are normal, the respective combined status is ON. When one or more of them has an error, the respective combined status is OFF. This status is known as the combined safety input status or combined safety output status.

## Analog I/O Status Data

Individual input status indicates whether each analog input point is normal (ON) or faulted (OFF). In addition, this diagnostic data is monitored:

- User 24V Supply Overrange or Underrange
- Sensor Power Overcurrent or Undercurrent
- Channel Signal Overrange or Underrange
- Broken Wire Detected (4…20 mA current mode)
- ·

Single-channel Discrepancy Error (channel fault) In SIL 2 or SIL 3 operation, a single-channel discrepancy error occurs when both measurements (internal to the module) of the same input signal are not within tolerance. If a single-channel discrepancy occurs, this indicates a problem with the module. Input status is set to zero and a zero input value is reported for that channel.

- SIL 3 Dual-channel Discrepancy Error (channel fault)
- Alarms
- – High High and Low Low Alarm Overrange or Underrange
- – High and Low Alarms Overrange or Underrange
- – Dual-channel Tachometer Dual Low Inputs Detected
- – Tachometer Frequency Overrange or Underrange

The alarm status is reported in the Alarm Status attribute for each channel.

## Choose a Power Supply

<!-- image -->

## Place Power Supplies and Modules in a System

| Topic Page                                   |
|----------------------------------------------|
| Choose a Power Supply 41                     |
| Power Supply Examples 43                     |
| Place Series A Digital and Analog Modules 45 |
| Place Series B Digital Modules 46            |

The POINTBus™ backplane includes a 5V communication bus and field power bus that get their power from a communication adapter or expansion power supplies. All POINT I/O™ modules are powered from the POINTBus backplane by either the adapter or expansion power supply. POINT I/O adapters have built-in power supplies. Use the information and examples in this chapter to determine if you need an expansion power supply in your system.

<!-- image -->

ATTENTION: To comply with the CE Low Voltage Directive (LVD), this equipment, and all connected I/O, must be powered from a safety extra low voltage (SELV) or protected extra low voltage (PELV) compliant source.

For UL-compliant applications, the 1734-IB8S, 1734-OB8S, and 1734-OBV2S modules, and all connected I/O, must be powered from a SELV- or PELV-compliant power source that is rated 150VA maximum.

For UL-compliant applications, the 1734-IE4S module, the module's field power and connected I/O devices must be powered from a Class 2-compliant, limited voltage/limited current power source.

<!-- image -->

These Rockwell Automation® 1606 power supplies are SELV- and PELV-compliant, and they meet the isolation and output hold-off time requirements of the SmartGuard™ 600 controller:

- 1606-XLP30E
- 1606-XLP50E
- 1606-XLP50EZ
- 1606-XLP72E
- 1606-XLP95E
- 1606-XLDNET4
- 1606-XLSDNET4

Follow the safety precautions that are listed in Chapter 1 and the wiring guidelines that are described in Chapter 4 before you connect a power supply to the system.

To choose which types of power supplies meet the system requirements, you must consider the power consumption requirements for the 5V and 24V bus when you design a POINTBus backplane.

Choose from these power supplies for the POINTBus backplane and field power:

- The 1734-EP24DC expansion power supply provides an additional 10 A of 24V DC field power and provides an additional 1.3 A of 5V current to the I/O modules to the right of the power supply.
- The 1734-FPD field power distributor provides an additional 10 A of 24V DC field power, and passes through all POINT I/O backplane signals and the 5V bus supplied to the left. It does not provide additional POINTBus backplane power which lets you isolate field power segments.
- The 1734-EPAC expansion power supply (for standard I/O modules) provides an additional 10 A of 120/240V AC field power and provides an additional 1.3 A of 5V current to the I/O modules to the right of the power supply.

## IMPORTANT

If you use the 1734-EPAC expansion power supply to the left of the POINT Guard I/O™ modules, you must use a 1734-FPD field power distributor or 1734-EP24DC expansion power supply. These distributors are used to isolate POINT Guard I/O field power from the AC field supply.

5V POINTBus power is required to establish and maintain communication (connection) between the module and the controller.

See the POINT I/O Selection Guide, publication 1734-SG001, for more information on compatible power supplies.

## Power Supply Examples

Use these valid power-supply example configurations to help you understand the combinations of power supplies that can fit your system:

- Example 1: Isolate Field Power Segments on page 43
- Example 2: POINT Guard I/O Used with AC I/O Modules on page 44

These examples are for illustrative purposes only, to help you understand various power supply concepts.

## IMPORTANT

- You must define the requirements for field and bus power segments in your application.
- The POINT Guard I/O modules DO NOT require separate field bus power usage, that is, separate power supplies. This step is optional.
- The POINT Guard I/O modules DO NOT require a separate POINTBus power-supply, which separates a module from other POINT I/O modules, except when additional POINTBus power is required.
- Do not apply AC voltage to POINT Guard I/O modules.

## Example 1: Isolate Field Power Segments

This power supply example uses a 1734-EP24DC expansion power supply and 1734-FPD field power distributor to illustrate a combination of standard POINT I/O and POINT Guard I/O modules. The example illustrates how you can mix the modules and create separate groups for input and output modules, along with digital and analog modules.

<!-- image -->

## Example 2: POINT Guard I/O Used with AC I/O Modules

This power supply example uses 1734-EP24DC and 1734-EPAC expansion power supplies to illustrate how you can mix POINT I/O and POINT Guard I/O modules, and create a separate power group for AC I/O modules.

<!-- image -->

## Place Series A Digital and Analog Modules

Always install modules in accordance with their specified operating temperature ratings, and provide a minimum of 5.08 CM (2 in.) clearance above the modules. For more information, see the Point I/O Selection Guide, publication 1734-SG001 .

- Limit ambient temperature operation to 40 °C (104 °F) if Series A POINT Guard I/O modules are used without 1734-CTM spacer modules.
- In any system where you have any Series A POINT Guard I/O modules, use a 1734-CTM spacer between every POINT Guard I/O module with ambient operation between 40 °C (104 °F) and 55 °C (131 °F).

Figure 22 - Series A Digital Modules in Operating Temperatures Less than 40 °C (104 °F)

<!-- image -->

Insert a 1734-CTM module next to each standard I/O module (gray) if the thermal dissipation specification of that module is more than 1 W.

Figure 23 - Series A Digital and Analog Modules in Operating Temperatures from 40 °C (104 °F)…55 °C (131 °F)

<!-- image -->

- When you use Series A POINT Guard I/O modules in your system limit the power supply to 24V DC maximum, to limit the Series A POINT Guard I/O thermal dissipation of the module.

For more information, see the Point I/O Selection Guide, publication 1734-SG001 .

<!-- image -->

ATTENTION: Vertical orientation requires careful attention to design details and panel layout so that all modules in the stack must operate within their rated operating temperature range.

For Vertical installations, be sure that 1734-CTM spacer modules are installed next to any Series A POINT Guard I/O modules operating above 40 °C (104 °F) ambient.

## Place Series B Digital Modules

Always install modules in accordance with their specified operating temperature ratings, and provide a minimum of 5.08 CM (2 in.) clearance above the modules.

When used in a system that contains only Series B Guard I/O™ modules, series B Guard I/O modules are used without 1734-CTM spacer modules in environments with ambient operation up to 55 °C (131 °F).

For Series B POINT Guard I/O module derating requirements for every module with ambient operation between 40 °C (104 °F) and 55 °C (131 °F), see the specifications in the Point I/O Selection Guide, publication 1734-SG001 .

Figure 24 - Series B Digital Modules in Operating Temperatures Less than 55 °C (131 °F)

<!-- image -->

| 5.08 cm (2 in.)   | 5.08 cm (2 in.)                                                               | 5.08 cm (2 in.)   | 5.08 cm (2 in.)   | 5.08 cm (2 in.)   | 5.08 cm (2 in.)   |
|-------------------|-------------------------------------------------------------------------------|-------------------|-------------------|-------------------|-------------------|
|                   | 1734-AENT 1734-IB8S/B 1734-OB8S/B1734-IB8S/B1734-OB8S/B1734-IB8S/B1734-OB8S/B |                   |                   |                   |                   |

<!-- image -->

ATTENTION: Vertical orientation requires careful attention to design details and panel layout so that all modules in the stack operate within their rated operating temperature range.

## Install the Module

| Topic Page            |
|-----------------------|
| Wire the Modules 48   |
| Connection Details 50 |
| Wiring Examples 51    |

See the POINT Guard I/O™ Safety Modules Installation Instructions, publication 1734-IN016, for information about terminal base installation and how to insert the I/O modules into the terminal bases.

<!-- image -->

Figure 25 - POINT Guard I/O Modules

<!-- image -->

31867-M

## Wire the Modules

Follow these guidelines when you wire the modules.

- Do not route communication, input, or output wiring with conduit that contains high voltage. See the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .
- Wire correctly after confirming the signal names of all terminals.
- Use shielded cable for analog and tachometer inputs.
- When using the sensor power supply on the 1734-IE4S module, do not connect an external power supply to the sensor.
- If you use the 1734-IE4S sensor power supply of the module to power your input devices, you are responsible for verifying that your application operates properly with the diagnostic features of this output.
- Tighten screws for communication and I/O connectors correctly.
- When using analog inputs, wire only to voltage or only to current inputs, not both. If you mix input types, it can induce noise on the input measurements.

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Wire the POINT Guard I/O modules properly so that the 24V DC line does not touch the safety outputs accidentally or unintentionally.

Do not connect loads beyond the rated value to safety outputs.

Wire conductors correctly and verify operation of the module before placing the system into operation. Incorrect wiring can lead to loss of safety function.

Do not apply DC voltages that exceed the rated voltages to the module.

Do not connect a power source to the sensor power supply in the 1734-IE4S module or you could blow an internal fuse. When an internal fuse is blown, the module is inoperative.

Disconnect the module from the power supply before wiring. If wiring is performed while power is supplied, devices that are connected to the module can operate unexpectedly.

WARNING: If you connect or disconnect wiring while the field-side power is on, an electric arc can occur. This arc could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

This equipment must be used within its specified ratings that Rockwell Automation has defined.

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc plated chromate-passivated steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum or plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately. Be sure to ground the DIN rail properly. Refer to Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for more information.

## Terminal Layout

These figures show the terminal layouts for the POINT Guard I/O modules.

Figure 26 - 1734-IB8S Field Connections

<!-- image -->

Where: T0 = Test Output 0 T1M = Test Output 1 with Muting T2 = Test Output 2 T3M = Test Output 3 with Muting I0…I7 = Inputs 0…7 COM = Supply Common

1734-TOP and 1734-TB Terminal Bases

Figure 27 - 1734-OB8S Field Connections

<!-- image -->

Where: O0…O7 = Safety Outputs 0…7 COM = Supply Common

1734-TOP and 1734-TB Terminal Bases

Figure 28 - 1734-OBV2S Field Connections

<!-- image -->

## Where:

Channels O0 and O1 = safety output bipolar pair

Channels O2 and O3 = safety output bipolar pair

Channels O0 and O2 = sourcing outputs

Channels O1 and O3 = sinking outputs

COM = Sensor Power supply common

V = Sensor Power supply

1734-TOP and 1734-TB Terminal Bases

Figure 29 - 1734-IE4S Field Connections

<!-- image -->

1734-TOP3 Terminal Base

## Where:

V0…V3 = Voltage inputs 0…3

I0…I3 = Current inputs 0…3

COM = Supply Common

S0…S3 = Sensor power terminals

## Connection Details

See the tables that show input device connection methods and their safety categories.

<!-- image -->

| Connected Device Test Pulse from                                                  |                                                                                                    | Connection Schematic Diagram Safety   |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------|
| Push Button No Connect the push button between 24V DC and I0.                     | I0  I1  T0  T1                                                                                     | 1                                     |
| Push Button No Connect the push button between 24V DC and I0.                     | Yes Connect the push button between I0 and T0. T0 must be configured as test I0  I1  T0  T1        | 2                                     |
| Emergency stop button Door monitor switch                                         | No Connect the devices between T0 and I0 and I1, note that T0 is configured for 24V I0  I1  T0  T1 | 3                                     |
| Emergency stop button Door monitor switch                                         | Connect the devices between 24V DC and I0 and I1.                                                  | I0  I1  T0  T1                        |
| Emergency stop button Door monitor switch                                         | Yes Connect the device between I0 and T0, and I1 and T1.                                           | 4 I0  I1  T0  T1                      |
| Light Curtain No Connect the OSSD1 and OSSD2 to I0 and supply commons. OSSD1OSSD2 | I1, respectively. Connect the 24V power In -  I0  I1  T0  T1                                       | 3 or 4 based on light curtain used    |

## Wiring Examples

Read this section for examples of wiring by application. See catalog number details for the appropriate module.

## Emergency Stop Dual-channel Devices

This example shows how to configure the controller and wire a digital POINT Guard I/O module with an emergency stop button and gate monitoring switch that have dual-channel contacts. When used in combination with the programs in a safety controller, this wiring is safety Category 4 (emergency stop button) and safety Category 3 (gate monitoring switch).

<!-- image -->

Figure 30 - 1734-IB8S POINT Guard I/O Module Wiring (Dual-channel Contacts)

| Controller Parameter Name Configuration Setting                               |
|-------------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output        |
| Safety Input 0 Test Source Test Output 0                                      |
| Dual-channel Safety Input 0/1 Mode Dual-channel Equivalent                    |
| Dual-channel Safety Input 0/1 Discrepancy Time 100 ms (application dependent) |
| Safety Input 1 Safety Input 1 Channel Mode Test Pulse from Test Output        |
| Safety Input 1 Test Source Test Output 1                                      |
| Safety Input 2 Safety Input 2 Channel Mode Safety Input                       |
| Safety Input 2 Test Source Test Output 2                                      |
| Dual-channel Safety Input 2/3 Mode Dual-channel Equivalent                    |
| Safety Input 3 Safety Input 3 Channel Mode Safety Input                       |
| Safety Input 3 Test Source Test Output 3                                      |
| Test Output 0 Test Output 0 Mode Pulse Test Output                            |
| Test Output 1 Test Output 1 Mode Pulse Test Output                            |
| Test Output 2 Test Output 2 Mode Power Supply Output                          |
| Test Output 3 Test Output 3 Mode Power Supply Output                          |

## Single-channel Safety Contactor

This example shows how to configure the controller and wire a1734-OB8S module with one safety contactor. When used in combination with the programs of the safety controller, this circuit configuration is safety Category 2.

Figure 31 - 1734-OB8S POINT Guard I/O Module Wiring (Single Safety Contact)

<!-- image -->

Where: O0…O7 = Safety Outputs COM = Common

| Controller Configuration Parameter Name Configuration Setting   | Controller Configuration Parameter Name Configuration Setting   |
|-----------------------------------------------------------------|-----------------------------------------------------------------|
|                                                                 | Safety Output 0 Safety Output 0 Point Mode Safety Pulse Test    |
|                                                                 | Point Operation Type Single Channel                             |

## Dual-channel Safety Contactors

This example shows how to configure the controller and wire a 1734-OB8S module with redundant safety contactors.

When the module is wired as shown, and the listed requirements are met in the project of the safety controller, it is suitable for applications that are rated up to, and including, Category 4 as defined in ISO 13849-1. To achieve that suitability rating, diagnostic testing and monitoring of the safety function can be required.

One diagnostic test method is to configure the safety input channel for Safety Pulse Test to test the circuit for short circuits to 24V DC.

Figure 32 - 1734-OB8S POINT Guard I/O Module Wiring (Redundant Safety Contacts)

<!-- image -->

Where: O0…O7 = Safety Outputs COM = Common

| Controller Configuration   | Parameter Name Configuration Setting                         |
|----------------------------|--------------------------------------------------------------|
|                            | Safety Output 0 Safety Output 0 Point Mode Safety Pulse Test |
|                            | Point Operation Type Dual-channel                            |
|                            | Safety Output 1 Safety Output 1 Point Mode Safety Pulse Test |

## Bipolar Safety Outputs

These examples show how to wire a 1734-OBV2S output module with an input module to meet PLe and PLd safety requirements.

<!-- image -->

Figure 33 - 1734-OBV2S Dual Safety Output Wiring - PLe

| Controller Configuration Parameter Name Configuration Setting   |
|-----------------------------------------------------------------|
| Safety output 0 Safety output 0 point mode Safety pulse test    |
| Safety output 1 Safety output 1 point mode Safety pulse test    |
| Safety input 1 Safety input 1 point operation type Single       |
| Test output 1 Test output 1 point mode Pulse test               |

<!-- image -->

Figure 34 - 1734-OBV2S Dual Safety Output Wiring - PLd

| Controller Configuration Parameter Name Configuration Setting   |
|-----------------------------------------------------------------|
| Safety output 0 Safety output 0 point mode Safety pulse test    |
| Safety output 1 Safety output 1 point mode Safety pulse test    |
| Safety input 1 Safety input 1 point operation type Single       |
| Test output 1 Test output 1 point mode Pulse test               |

## Safety Analog Input Wiring

The following sections contain important guidelines for wiring safety analog inputs and wiring examples for the 1734-IE4S module. See page 60 for examples.

## Guidelines for Wiring Safety Analog Inputs

Follow these guidelines when wiring your safety analog inputs.

- For eight terminal connections, use the 1734-TOP or 1734-TB terminal bases.
- For all 12 terminal connections, use the 1734-TOP3 terminal base. When using a 1734-TOP3 base, both of the COM terminals and both of the Sensor Power terminals for each channel are internally connected. The FE terminal connection that is shown on the diagrams represents a grounding lug on the panel or terminal connection to the DIN rail.
- If the sensor has a digital output for use with Tachometer mode, it must be either a push-pull type output or have appropriate pull-up or pull-down resistors for NPN or PNP sensors. The analog input module does not provide the low impedance of these pull-up or pull-down resistors.

## IMPORTANT

You must verify the behavior of your 3-wire sensor to make sure that if it loses its ground connection, the signal is 0 (safe state) at the module input when the fault occurs.

## IMPORTANT

To obtain SIL 3, Cat. 3 or Cat.4, you must make sure that the analog input signals do not short together or that the two sensors are installed to provide signals that are offset from one another. When the module is configured as the source for sensor power, a short-circuit is detected at powerup (Cat. 2). However, when an external power supply is used, another means must detect this fault.

## Safety Analog Input Wiring Examples

Follow the Guidelines for Wiring Safety Analog Inputs on page 55 .

Figure 35 - 2-wire Current (4…20 mA) Sensor (SIL2 or SIL 3)

1734-TB Terminal Bases

Figure 36 - 3-wire Voltage or Tachometer Sensor (SIL 2)

<!-- image -->

- For analog voltage-output sensors, the signal levels for operation for the application must be outside the signal level when the signal is not present, for example, when the wire is broken.
- See the figures on page 60 for tachometer wiring detail.
- For 0…20 mA analog current-output sensors, the signal levels for operation for the application must be outside the signal level when the signal is not present, for example, when the wire is broken.

Figure 37 - 3-wire Current Sensor (SIL 2)

<!-- image -->

<!-- image -->

- Signal Return and Common are at the same potential.
- See the figures on page 60 for tachometer wiring detail.
- Signal Return and Common are at the same potential.

Figure 38 - 4-wire Voltage or Tachometer Sensor (SIL 2)

## 1734-TOP3 Terminal Bases

Figure 39 - 4-wire Current Sensor (SIL 2)

<!-- image -->

## 1734-TOP3 Terminal Bases

Figure 40 - 2-wire Current (4…20 mA) Sensor (SIL 3)

<!-- image -->

- Field sensors are monitoring the same signal in a redundant configuration.
- You must configure a safety deadband between the two signals to achieve SIL 3.

<!-- image -->

1734-TB Terminal Bases

Figure 41 - 3-wire Voltage or Tachometer Sensor (SIL 3)

- This wiring configuration can also be used for SIL 2 redundant Tachometer mode.
- For analog voltage-output sensors, the signal levels for operation for the application must be outside the signal level when the signal is not present, for example, when the wire is broken.
- Field sensors are monitoring the same signal in a redundant configuration.
- You must configure a safety discrepancy deadband between the two signals to achieve SIL 3.
- See the figures on page 60 for tachometer wiring detail.
- For 0…20 mA analog current-output sensors, the signal levels for operation for the application must be outside the signal level when the signal is not present, for example, when the wire is broken.
- Field sensors are monitoring the same signal in a redundant configuration.
- You must configure a safety discrepancy deadband between the two signals to achieve SIL 3.
- This wiring configuration may also be used for SIL 2 redundant Tachometer mode.
- Signal Return and Common are at the same potential.
- Field sensors are monitoring the same signal in a redundant configuration.
- You must configure a safety discrepancy deadband between the two signals to achieve SIL 3.
- See the figures on page 60 for tachometer wiring detail.

Figure 42 - 3-wire Current Sensor (SIL 3)

<!-- image -->

Figure 43 - 4-wire Voltage or Tachometer Sensor (SIL 3)

<!-- image -->

<!-- image -->

1734-TB Terminal Bases

1734-TOP3 Terminal Bases

- Signal Return and Common are at the same potential.
- Field sensors are monitoring the same signal in a redundant configuration.
- You must configure a safety discrepancy deadband between the two signals to achieve SIL 3.
- Signal Return and Common are at the same potential.
- See the figures on page 60 for tachometer wiring detail.
- Signal Return and Common are at the same potential.

Figure 44 - 4-wire Current Sensor (SIL 3)

<!-- image -->

## IMPORTANT

For the following two examples, follow these guidelines:

- The negative terminal of the sensor power supply and that of the 1734 terminal base COMMON must be at the same potential.
- Use of an external power supply limits diagnostics and increases susceptibility to noise.
- You must verify that the sensor is receiving appropriate power. Safety sensors that are not properly powered do not always deliver accurate signals to the analog input module.
- Follow the Guidelines for Wiring Safety Analog Inputs on page 55 .

Figure 45 - 4-wire Voltage or Tachometer Sensor (SIL 2) with External Power Supply

<!-- image -->

Figure 46 - 4-wire Current Sensor (SIL 2) with External Power Supply

<!-- image -->

Figure 47 - Safety Analog Input Wiring for Sinking Tachometer Sensor

1734-TOP3 Terminal Bases

<!-- image -->

Figure 48 - Safety Analog Input Wiring for Sourcing Tachometer Sensor

<!-- image -->

## Install the Module on an EtherNet/IP Network

<!-- image -->

## Configure the Module in a GuardLogix Controller System

| Topic Page                                      |
|-------------------------------------------------|
| Install the Module on an EtherNet/IP Network 61 |
| Values and States of Tags 89                    |
| Configure Safety Connections 91                 |
| Configuration Ownership 92                      |
| Save and Download the Module Configuration 93   |

When you use a GuardLogix® controller on an EtherNet/IP™ network, configure the POINT Guard I/O™ modules with the Studio 5000 Studio 5000 Logix Designer application.

## IMPORTANT

You must configure each point that is used as a safety input or output. By default, all safety input and output points are disabled.

To install the POINT Guard I/O modules on an EtherNet/IP network, complete these steps.

1. Add and Configure the Ethernet Bridge .
2. Add and Configure the Point I/O Ethernet Adapter .
3. Add and Configure Safety Digital Input Modules .
4. Add and Configure Safety Digital Output Modules .
5. Add and Configure Safety Analog Input Modules .

## Add and Configure the Ethernet Bridge

Follow this procedure to add and configure the Ethernet bridge. In this example, we use a 1756 GuardLogix controller.

1. From the I/O Configuration tree, right-click 1756 Backplane, 1756-Axx, and choose New Module.
2. In the Select Modules dialog box, check Communication and Allen-Bradley®.
3. Choose an Ethernet module from the list and click Create.

<!-- image -->

In this example, we chose the 1756-EN2T bridge. These module revisions support CIP Safety™.

| Cat. No. Compatible Major Revision   |
|--------------------------------------|
| 1756-EN2F 1 or later                 |
| 1756-EN2T 1 or later                 |
| 1756-ENBT 3 or later                 |
| 1756-EN2TR 3 or later                |
| 1756-EN3TR 3 or later                |
| 1768-ENBT 3 or later                 |

4. Specify the properties for the new module.
- a. In the Name field of the New Module dialog box, type the name of the Ethernet bridge.
- b. In the Description field, type an optional description.
- c. In the IP address field, type the IP address.
- d. In the Slot field, choose the slot number.

<!-- image -->

5. To edit the Module Definition, click Change.
- a. In the Revision fields, choose the major and minor revisions.
- b. From the Electronic Keying dropdown menu, choose the appropriate keying method.

| Choose Description                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatible Module Allows a module to determine whether it can emulate the module that is defined in the configuration that is sent from the controller. |
| Disable Keying None of the parameters in the physical module and module that is configured in the software must match. Do not choose Disable Keying.    |
| Exact Match All parameters must match or the inserted module rejects a connection to the controller.                                                    |

## 6. Click OK.

The I/O Configuration tree displays the Ethernet connection.

<!-- image -->

## Add and Configure the Point I/O Ethernet Adapter

1. Right-click the Ethernet connection and choose New Module.
2. On the Select Module dialog box, check Communication and Allen-Bradley.
3. Choose an Ethernet adapter from the list and click Create.

<!-- image -->

.

4. Specify the general properties of the Ethernet adapter.
- a. In the Name field of the New Module dialog box, type the name of the 1734 Ethernet adapter.
- b. In the Description field, type a description, if desired.
- c. In the IP address field, type the IP address.
5. To edit the Ethernet adapter Definition, click Change.
- a. In the Revision fields, choose the major and minor revisions.

<!-- image -->

<!-- image -->

IMPORTANT 1734-AENT adapter firmware must be major revision 3 or later to support POINT Guard I/O modules.

- b. From the Electronic Keying dropdown menu, choose the appropriate keying method.

| Choose Description                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------|
| Exact Match Module and type series must exactly match or the controller rejects the module.                                                |
| Compatible Module Controller checks module type and revision for compatibility. Compatible modules that match, or are newer, are accepted. |
| Disable Keying Controller checks module type, but accepts any version. Do not choose Disable Keying.                                       |

- c. From the Connection dropdown menu, choose the appropriate connection for the 1734 Ethernet adapter.

|                   | Choose Description                                                                                                                                                                                                  |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Listen Only Read or verify standard digital I/O data only, but does not control the modules. (When you have multiple controllers, one controller is used to control and the other controllers are used to monitor.) |
|                   | None The adapter makes a direct connection to each of the module’s listed under the 1734-AENT adapter in the I/O Configuration tree.                                                                                |
| Rack Optimization | Standard digital I/O data is collected into one rack image. NOTE: POINT specialty, analog, or safety (POINT Guard I/O) modules do not use rack optimization.                                                        |

<!-- image -->

If there are no standard digital I/O modules in your POINT I/O™ system, choose None.

- d. From the Chassis Size dropdown menu, choose the number of POINT I/O modules that are attached to the 1734 Ethernet adapter plus 1 for the 1734 Ethernet adapter.

## IMPORTANT

Do not count terminal bases. Enter only the number of physical modules that are installed, plus 1 for the adapter. This number must match exactly. You cannot enter a higher number to anticipate future expansion.

Each POINT Guard module that you configure can consume up to 2 connections of the 20 connection limit within the 1734-AENT or 1734-AENTR modules. Be sure that you are aware of and design your POINT system with these limits in mind.

6. To return to the Module Properties dialog box, click OK.
7. To apply your changes, click OK.

The I/O Configuration tree displays the 1734 Ethernet adapter.

<!-- image -->

## Add and Configure Safety Digital Input Modules

To include a safety digital input module in the project, add the module under the I/O chassis in the I/O Configuration tree. Then configure the general properties of the module, configure the digital inputs, and configure test outputs as described in these sections.

## Add the Safety Digital Input Module

To add the POINT Guard I/O safety digital input module, follow these steps.

1. Right-click the POINT I/O Chassis and choose New Module.
2. From the Select Module dialog box, check Digital and Allen-Bradley.
3. Select an input module and click Create.

<!-- image -->

<!-- image -->

4. Specify the general properties of the module.
- a. In the Name field of the New Module dialog box, type a unique name for the input module.
- b. From the Module Number dropdown menu, choose a unique module number that corresponds to the position of the module in the chassis.
- c. In the Description field, type a description, if desired.
- d. In the Safety Network Number field, use the default setting.

<!-- image -->

For a detailed explanation of the safety network number (SNN), see the GuardLogix Controller Systems Safety Reference Manuals that are listed in the Additional Resources on page 8. However, in most cases, you use the default that the Studio 5000 Logix Designer application sets.

The purpose of the safety network number (SNN) is to make sure that every module in a system can be uniquely identified. We suggest that all safety modules on a network have the same SNN, to make documentation easier. At configuration, the Studio 5000 Logix Designer application defaults to an SSN of a safety device to match the SNN of the lowest safety node on each network.

5. To edit the Module Definition, click Change.
- a. In the Series field, choose the input series letter of the module.
- b. In the Revision fields, choose the input revision number of the module.
- c. From the Electronic Keying dropdown menu, choose the appropriate keying method for the input module.
- d. From the Configured By dropdown menu, choose the configuration method.

<!-- image -->

|                   | Choose Description                                                                                                                         |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Exact Match All parameters must match or the inserted module rejects a connection to the controller.                                       |
| Compatible Module | Allows an I/O module to determine whether it can emulate the module that is defined in the configuration that is sent from the controller. |

| Choose Description                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This Controller This selection directs the controller to configure the module.                                                                                                 |
| External Means This selection directs the controller to establish a safety input connection only, and the controller doesn’t configure the module or control the Test Outputs. |

- e. From the Input Data dropdown menu, choose Safety or None.
- f. From the Output Data dropdown menu, choose from the following options.

<!-- image -->

|                                   | Choose Description                                                                                                                                                                | Choose Description                                                                                                                                                                | Choose Description                                                                                                                                                                | Choose Description                                                                                                                                                                | Choose Description                                                                                                                                                                |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Safety These tags are created for the target module:  •  RunMode for module mode  •  ConnectionFaulted for communication status  •  Safety Data for safety inputs from the module | Safety These tags are created for the target module:  •  RunMode for module mode  •  ConnectionFaulted for communication status  •  Safety Data for safety inputs from the module | Safety These tags are created for the target module:  •  RunMode for module mode  •  ConnectionFaulted for communication status  •  Safety Data for safety inputs from the module | Safety These tags are created for the target module:  •  RunMode for module mode  •  ConnectionFaulted for communication status  •  Safety Data for safety inputs from the module | Safety These tags are created for the target module:  •  RunMode for module mode  •  ConnectionFaulted for communication status  •  Safety Data for safety inputs from the module |
| AENT_Adapter:1:1                  | {...}                                                                                                                                                                             | {...}                                                                                                                                                                             |                                                                                                                                                                                   | AB:1734_IB8S_Safety2:1:0 Safety                                                                                                                                                   |                                                                                                                                                                                   |
| AENT_Adapter:1:1.RunMode          | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:l.ConnectionFaul.. | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt00D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt01Data         | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt02D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt03D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt04D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt05Data         | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt06D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |
| AENT_Adapter:1:1.Pt07D ata        | 0                                                                                                                                                                                 |                                                                                                                                                                                   | Decimal                                                                                                                                                                           | BOOL                                                                                                                                                                              | Safety                                                                                                                                                                            |

| Choose Description                                                                                                                                                                                                                                                                                   | Choose Description                                                                                                                                                                                                                                                                                   | Choose Description                                                                                                                                                                                                                                                                                   | Choose Description                                                                                                                                                                                                                                                                                   | Choose Description                                                                                                                                                                                                                                                                                   | Choose Description                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. | None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. | None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. | None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. | None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. | None Creates an input-only connection to the module. Inputs and status are read, but no outputs are written. You can still use the test outputs as pulse test outputs or a power supply. None is the recommended option if you do not control the test outputs of the module with application logic. |
| Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                | Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                | Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                | Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                | Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                | Test Creates these tags to enable application logic control of the test outputs on the module. This selection allows the test outputs to be used as standard outputs and muting outputs. Test is available only when This Controller is selected under Configured By.                                |
| AENT_Adapter:1:0                                                                                                                                                                                                                                                                                     | （...}                                                                                                                                                                                                                                                                                               | {...)                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                      | AB:1734_IB8S:0:0                                                                                                                                                                                                                                                                                     | Safety                                                                                                                                                                                                                                                                                               |
| AENT_Adapter:1:O.Test00Data                                                                                                                                                                                                                                                                          | 0                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      | Decimal                                                                                                                                                                                                                                                                                              | BOOL                                                                                                                                                                                                                                                                                                 | Safety                                                                                                                                                                                                                                                                                               |
| AENT_Adapter:1:O.Test01Data                                                                                                                                                                                                                                                                          | 0                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      | Decimal                                                                                                                                                                                                                                                                                              | BOOL                                                                                                                                                                                                                                                                                                 | Safety                                                                                                                                                                                                                                                                                               |
| AENT_Adapter:1:O.Test02D ata                                                                                                                                                                                                                                                                         | 0                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      | Decimal                                                                                                                                                                                                                                                                                              | BOOL                                                                                                                                                                                                                                                                                                 | Safety                                                                                                                                                                                                                                                                                               |
| AENT_Adapter:1:0.Test03D ata                                                                                                                                                                                                                                                                         | 0                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      | Decimal                                                                                                                                                                                                                                                                                              | BOOL                                                                                                                                                                                                                                                                                                 | Safety                                                                                                                                                                                                                                                                                               |

## IMPORTANT

When test outputs are configured as standard outputs, they must not be used for safety purposes.

- g. From the Input Status dropdown menu, choose from the following options.
- h. From the Data Format dropdown menu, use the default 'Integer'.

<!-- image -->

6. To return to the Module Properties dialog box, click OK.
7. To apply your changes, click OK.

The I/O Configuration tree displays the module.

<!-- image -->

## Configure the Safety Digital Inputs

To configure the safety digital inputs, follow this procedure.

1. From the Module Properties dialog box, click the Input Configuration tab.

<!-- image -->

## 2. Assign the Point Operation Type.

| Choose Description                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single Inputs are treated as single channels. Dual-channel safety inputs can be configured as two individual single channels. This configuration does not affect pulse tests because it is handled on an individual channel basis. IMPORTANT: Use single-channel mode when you intend to use the GuardLogix safety application instructions. |
| Equivalent Inputs are treated as a dual-channel pair. The channels must match within the discrepancy time or an error is generated.                                                                                                                                                                                                          |
| Complementary Inputs are treated as a dual-channel pair. They must be in opposite states within the discrepancy time or an error is generated.                                                                                                                                                                                               |

When you choose Equivalent or Complementary, you must also assign a Discrepancy Time.

A discrepancy time setting of 0 ms means that the channels in a dual configuration can be discrepant for an infinite amount of time without a fault being declared.

For a discrepancy time setting of 0 ms, the evaluated status of the inputs still goes to the safe state due to a 'cycle inputs' required condition. However, with a 0 ms discrepancy time setting, a fault is not declared.

A 'cycle inputs' required condition occurs when one input terminal goes from its normal Active-&gt;Inactive-&gt;Active state while the other input terminal remains in its normal Active state. Even though no fault is declared, the inputs must be cycled through the safe state before the evaluated status of the inputs can return to the Active state. When in a 'cycle inputs' required condition, the logical state does not necessarily match the voltage at the terminals.

## IMPORTANT

Configuring the discrepancy time on safety I/O modules masks input discrepancies that the controller safety instructions detect. The controller reads the status to obtain this fault information.

3. Assign the Point Mode.
4. Assign a Test Source for each safety input on the module that you want to pulse test.
5. Assign the Input Delay Time, Off -&gt; On (0…126 ms, in increments of 6 ms).

| Choose Description                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not Used The input is disabled. If 24V is applied to the input terminal, it remains logic 0.                                                                                                                                                                                                                            |
| Safety Pulse Test Pulse tests are performed on this input circuit. A test source on the POINT Guard I/O module must be used as the 24V source for this circuit. Use the test source dropdown menu to is configured the test source. The pulse test detects shorts to 24V and channel-to-channel shorts to other inputs. |
| Safety A safety input is connected but there is no requirement for the POINT Guard I/O module to perform a pulse test on this circuit. An example is a safety device that performs its own pulse tests on the input wires, such as a light curtain.                                                                     |
| Standard A standard device, such as a reset switch, is connected. This point cannot be used in dual-channel operation.                                                                                                                                                                                                  |

|                   | Choose Description                                                                                                                                                                                                                      |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None              | If pulse tests are performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit. |
| Test Output 0     | If pulse tests are performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit. |
| Test Output 1 (1) | If pulse tests are performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit. |
| Test Output 2     | If pulse tests are performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit. |
| Test Output 3 (1) | If pulse tests are performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit. |

Filter time is for OFF to ON transition. Input must be high after the input delay has elapsed before it is set logic 1. This delay time is configured per channel with each channel that is tuned to match the characteristics of the field device, for maximum performance.

6. Assign the Input Delay Time, Off -&gt; On (0…126 ms, in increments of 6 ms).

Filter time is ON to OFF transition. Input must be low after the input delay has elapsed before it is set logic 0. This delay time is configured per channel with each channel that is tuned to match the characteristics of the field device, for maximum performance.

7. From the Input Error Latch Time field, enter the time that the module holds an error to make sure that the controller can detect it (0…65,530 ms, in increments of 10 ms - default 1000 ms).

This setting provides more accurate diagnostics. The purpose for latching input errors is to make sure that intermittent faults that can exist only for a few milliseconds are latched long enough for the controller to read. The amount of time to latch the errors is based on the RPI, the safety task watchdog, and other application-specific variables.

8. Click Apply.

## Configure the Test Outputs

To complete the test output configuration, follow this procedure.

1. From the Module Properties dialog box, click the Test Output tab.
2. Assign the Point Mode.

<!-- image -->

| Choose Description                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not Used The test output is disabled (default for T2 and T3).                                                                                                                                                                                                                             |
| Standard The GuardLogix controller program controls the test output point.                                                                                                                                                                                                                |
| Pulse Test The test output is being used as a pulse test source (default for T0 and T1).                                                                                                                                                                                                  |
| Power Supply A constant 24V is placed on the output terminal. It can be used to provide power to a field device.                                                                                                                                                                          |
| Muting Lamp Output (terminals T1 and T3 only) An indicator lamp is connected to the output. When this lamp is energized, a burned-out bulb, broken wire, or short to GND error condition can be detected. Typically, the lamp is an indicator that is used in light curtain applications. |

There is also a Test Output Fault Action parameter that can only be read or written to via explicit messaging. If communication to the module times out, you can set the test outputs to Clear OFF (default) or Hold Last State. For more information, see Appendix B .

3. Click Apply.

## Add and Configure Safety Digital Output Modules

To include a POINT Guard safety digital-output module in the project, add the module to the POINT I/O chassis. Configure the general properties of the module, and configure the digital outputs as described in the following sections.

## Add the Safety Digital Output Module

To add the POINT Guard I/O safety digital output module, follow these steps.

To add and configure POINT Guard I/O safety modules, follow these steps.

1. Right-click the POINT I/O chassis and choose New Module.
2. On the Select Module dialog box, select a safety output module and click OK.

<!-- image -->

The 1734-OB8S module is shown in the examples.

<!-- image -->

3. Specify the general properties of the module.
- a. In the Name field of the New Module dialog box, type a unique name for the output module.
- b. From the Module Node dropdown menu, choose a unique module node number that corresponds to the position of the module in the chassis.
- c. In the Description field, type a description, if desired.
- d. In the Safety Network Number field, use the default setting.

<!-- image -->

For a detailed explanation of the safety network number (SNN), see the GuardLogix Controller Systems Safety Reference Manuals that are listed in the Additional Resources on page 8. In most cases, you use the default that the Studio 5000 Logix Designer application provides.

4. Under Module Definition, click Change to edit the settings of the module.
- a. In the Series field, choose the series letter of the output module.
- b. In the Revision fields, choose the revision numbers of the output module.

<!-- image -->

- c. From the Electronic Keying dropdown menu, choose the appropriate keying method from the following options.
- d. From the Configured By dropdown menu, choose the method by which this module is configured.
- e. From the Input Data dropdown menu, choose None.

| Choose Description                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exact Match All parameters must match or the inserted module rejects a connection to the controller.                                                    |
| Compatible Module Lets an I/O module determine whether it can emulate the module that is defined in the configuration that is sent from the controller. |

| Choose Description                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This Controller This selection directs the controller to configure and control the safety outputs. The Output Data selection is set to Safety.                                                                                         |
| External Means This selection directs the controller to establish a safety input connection only, and the controller does not configure the module or be able to control the safety outputs. The Output Data selection is set to None. |

None is the only valid selection, as this module is an output-only safety module.

- f. From the Output Data dropdown menu, choose from the following:

|                          | Choose Description                                                                                                                                                                                                             | Choose Description                                                                                                                                                                                                             | Choose Description                                                                                                                                                                                                             | Choose Description                                                                                                                                                                                                             | Choose Description                                                                                                                                                                                                             |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | Safety Automatically selected when Configured By = This controller. Creates an output connection. When you select Safety, an output tag is created for each output point and enables these outputs for use in the Safety Task. | Safety Automatically selected when Configured By = This controller. Creates an output connection. When you select Safety, an output tag is created for each output point and enables these outputs for use in the Safety Task. | Safety Automatically selected when Configured By = This controller. Creates an output connection. When you select Safety, an output tag is created for each output point and enables these outputs for use in the Safety Task. | Safety Automatically selected when Configured By = This controller. Creates an output connection. When you select Safety, an output tag is created for each output point and enables these outputs for use in the Safety Task. | Safety Automatically selected when Configured By = This controller. Creates an output connection. When you select Safety, an output tag is created for each output point and enables these outputs for use in the Safety Task. |
| -POINT_Guard:1:0         | -POINT_Guard:1:0                                                                                                                                                                                                               | (...)                                                                                                                                                                                                                          | (...}                                                                                                                                                                                                                          | AB:1734_0B8S:0:0 Safety                                                                                                                                                                                                        | AB:1734_0B8S:0:0 Safety                                                                                                                                                                                                        |
| POINT_Guard:1:0.Pt00Data | POINT_Guard:1:0.Pt00Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:O.Pt01Data | POINT_Guard:1:O.Pt01Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:0.Pt02Data | POINT_Guard:1:0.Pt02Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:0.Pt03Data | POINT_Guard:1:0.Pt03Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:O.Pt04Data | POINT_Guard:1:O.Pt04Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:0.Pt05Data | POINT_Guard:1:0.Pt05Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:O.Pt06Data | POINT_Guard:1:O.Pt06Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
| POINT_Guard:1:O.Pt07Data | POINT_Guard:1:O.Pt07Data                                                                                                                                                                                                       | 0                                                                                                                                                                                                                              | Decimal                                                                                                                                                                                                                        | BOOL                                                                                                                                                                                                                           | Safety                                                                                                                                                                                                                         |
|                          | None Automatically selected when Configured By = External. When you select None, it results                                                                                                                                    | None Automatically selected when Configured By = External. When you select None, it results                                                                                                                                    | None Automatically selected when Configured By = External. When you select None, it results                                                                                                                                    | None Automatically selected when Configured By = External. When you select None, it results                                                                                                                                    | None Automatically selected when Configured By = External. When you select None, it results                                                                                                                                    |

- g. From the Input Status dropdown menu, choose from the following.
- (1) When using combined status, use explicit messaging to read individual point status for diagnostic purposes.
- h. From the Data Format dropdown menu, use the default 'Integer'.
5. To return to the Module Properties dialog box, click OK.

| Choose Description                                        |
|-----------------------------------------------------------|
| None There are no status tags, only data for the outputs. |
| Pt. Status There is one status tag for each output point. |

| AENT_Adapter:1:1.Pt00OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
|-------------------------------------|-----|-----------|--------|----------|
| AENT_Adapter:1:1.Pt01OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt02OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt03OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt04OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt050utputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt06OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| AENT_Adapter:1:1.Pt07OutputStatus   |   0 | Decimal   | BOOL   | Safety   |

<!-- image -->

6. To apply your changes, click OK.

The I/O Configuration tree displays the output module.

<!-- image -->

## Configure the Safety Digital Outputs

To configure the safety digital outputs, follow this procedure.

1. From the Module Properties dialog box, click the Output Configuration tab.
2. Assign the Point Operation Type.
3. Assign the Point Mode.

<!-- image -->

<!-- image -->

| Choose Description                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single The output is treated as one channel.                                                                                                                                                                                         |
| Dual (default) The POINT Guard I/O module treats the outputs as a pair. It always sets them HI or LO as a matched pair. Safety logic must set both of these outputs ON or OFF simultaneously or the module declares a channel fault. |

|                   | Choose Description                                                                                                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Not Used The output is disabled.                                                                                                                                                                     |
|                   | Safety The output point is enabled and does not perform a pulse test on the output.                                                                                                                  |
| Safety Pulse Test | The output point is enabled and performs a pulse test on the output. When the output is energized, the output pulses low briefly. The pulse test detects whether the output is functioning properly. |

4. In the Output Error Latch Time field, enter the time that the module holds an error to make sure that the controller can detect it (0…65,530 ms, in increments of 10 ms - default 1000 ms).

This action provides more accurate diagnostics. The purpose for latching output errors is to make sure that intermittent faults that can exist only for a few milliseconds are latched long enough for the controller to read. The amount of time to latch the errors is based on the RPI, the safety task watchdog, and other application-specific variables.

5. Click Apply.

## Add and Configure Safety Analog Input Modules

To include a POINT Guard safety analog input module in the project, you add the module to the POINT I/O chassis, configure the general properties of the module, and configure the analog inputs as described in the following sections.

## Add the Safety Analog Input Module

Follow these steps to add the POINT Guard I/O safety analog input module.

1. Right-click the POINT I/O chassis and choose New Module.
2. From the Select Module dialog box, select an analog input module and click Create.

<!-- image -->

<!-- image -->

3. Specify the general properties of the module.
- a. In the Name field of the New Module dialog box, type a unique name for the analog input module.
- b. From the Module Number dropdown menu, choose a unique module number that corresponds to the position of the module in the chassis.
- c. In the Description field, type a description, if desired.
- d. In the Safety Network Number field, use the default setting.

<!-- image -->

For a detailed explanation of the safety network number (SNN), see the GuardLogix Controller Systems Safety Reference Manuals that are listed in the Additional Resources on page 8. In most cases, you use the default that is provided by the Studio 5000 Logix Designer application.

The safety network number (SNN) is a unique number that identifies a safety subnet. We suggest that all safety modules on a network have the same SNN, to make documentation easier. During configuration, the Studio 5000 Logix Designer application defaults the SNN of a safety device to match the SNN of the lowest safety node on the network.

4. To open the Module Definition dialog box, click Change.
- a. In the Series field, choose the series letter of the analog input module.
- b. In the Revision fields, choose the revision number of the module.

<!-- image -->

- c. From the Electronic Keying dropdown menu, choose the appropriate keying method for the input module.
- d. From the Configured By dropdown menu, choose the appropriate method by which this module is configured.
- e. From the Input Data dropdown menu, choose Safety.
- f. From the Output Data dropdown menu, choose from the following.
- g. From the Process Data dropdown menu, choose from the following.
- h. From the Data Format dropdown menu, use the default 'Integer'.
5. To return to the Module Properties dialog box, click OK.
6. To apply your changes, click OK.

|                   | Choose Description                                                                                                                         |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Exact Match All parameters must match or the inserted module rejects a connection to the controller.                                       |
| Compatible Module | Allows an I/O module to determine whether it can emulate the module that is defined in the configuration that is sent from the controller. |

| Choose Description                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| This Controller This selection directs the controller to configure the Inputs.                                                                      |
| External Means This selection directs the controller to establish a safety input connection only, and the controller does not configure the module. |

| Choose Description                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None An output tag is not generated.                                                                                                                                                                                                                                                                                            |
| Safety-Tachometer This option is available when the Configured By selection is This Controller. The output tag contains data members for safety output data that is needed for Tachometer mode. If you use Tachometer mode, you must choose this setting; otherwise, you are not able to configure other Tachometer parameters. |

| Choose Description                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status The input tag contains safety analog input data from the module.                                                                                                                                |
| Status - Alarms These tags are created for the target module: •  Safety data for individual process alarms •  Safety data for safety analog inputs from the module                                     |
| Status - Alarms - Faults These tags are created for the target module: •  Safety data for individual process alarms  •  Safety data for faults •  Safety data for safety analog inputs from the module |

The I/O Configuration tree displays the 1734-IE4S module.

<!-- image -->

## Configure the Safety Analog Input Channel Operation

To configure the safety analog input channels, follow this procedure.

1. From the Module Properties dialog box, click the Safety Input Configuration tab.
2. Assign the Operation Type.

<!-- image -->

| Choose Description                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single Inputs are treated as single channels. Dual-channel safety inputs can be configured as two individual, single channels. IMPORTANT: Use single-channel mode when you intend to use the GuardLogix safety application instructions. |
| Equivalent Inputs are treated as a dual-channel equivalent pair. The channels must match within the discrepancy time or an error is generated.                                                                                           |

## IMPORTANT

If you use a Dual-channel Analog (DCA) safety instruction in your application program, you must configure the 1734-IE4S module for single-channel operation. Analog input pairs are then evaluated as pairs and compared to each other in the application logic.

3. If you chose Equivalent, you must also assign a Discrepancy Time, from 0…65,530 ms in 10 ms increments.

This measurement is the amount of time the two channels can differ from each other (larger than the deadband value) before a discrepancy error is declared. A discrepancy time setting of 0 ms means that the channels in a dual configuration can be discrepant for an infinite amount of time without a fault being declared. This setting effectively removes the usefulness of dual-channel mode.

4. Configure a deadband for the paired safety analog inputs.

The deadband can be any value from 0…32767 (engineering units) in increments of 1. When the paired input values exceed the deadband tolerance for longer than the Discrepancy Time, a discrepancy fault occurs.

<!-- image -->

Configure a deadband value for applications that use two sensors to measure the same variable; otherwise, spurious trips can occur.

5. If desired, configure a Channel Offset for the paired safety analog inputs.

The channel offset can be any value from -32768…+32767 (engineering units) in increments of 1. Configure an offset when differences in the sensors nominal input signals exceed the desired deadband. The channel offset is applied from the second to the first member of the channel pair, that is, from channel 1 to channel 0 or from channel 3 to channel 2.

6. In the Input Error Latch Time field, enter the time that the module holds an error to make sure that the controller can detect it (0…65,530 ms, in increments of 10 ms - default 1000 ms).

This setting provides more accurate diagnostics. The purpose for latching input errors is to make sure that intermittent faults that can exist only for a few milliseconds are latched long enough for the controller to read. The amount of time to latch the errors must be based on the RPI, the safety task watchdog, and other application-specific variables.

7. Click Apply.

## Configure the Safety Analog Inputs

To configure the analog input points, follow these steps.

1. From the Module Properties dialog box, click the Input Configuration tab.
2. Assign the Point Mode.

<!-- image -->

| Choose Description                                                         |
|----------------------------------------------------------------------------|
| Not Used The input is disabled.                                            |
| Safety Safety-related analog input value                                   |
| Standard Standard analog input value, not being used for a safety function |

If the channel operation is configured as dual-channel equivalent, when you click Apply, channel 1 is set to the same value as channel 0 and channel 3 is set to the same value as channel 2.

3. Configure the module for current, voltage, or tachometer inputs.

4. Configure an input filter.

A single-pole, anti-aliasing filter of 10 Hz is followed by a four-pole digital filter. Choose from the following available corner frequencies.

- 1 Hz (recommended for Tachometer mode)
- 5 Hz
- 10 Hz
- 50 Hz

For more information on the filter frequencies and step response, see the Point I/O Selection Guide, publication 1734-SG001 .

5. Assign High and Low Engineering scaling values for the inputs, if desired.

The valid range for both the High and Low Engineering settings is -30000…+30000, in increments of 1. Scaling lets the module report in engineering units such as degrees, PSI, CFM, and percent, rather than in raw counts.

If the channel operation is configured as dual channel equivalent, when you click Apply, channel 1 is set to the same value as channel 0 and channel 3 is set to the same value as channel 2 if the channel operation is configured as dual channel equivalent.

6. To indicate how each sensor is powered, set the Sensor Power Supply value to External or Module.

<!-- image -->

To supply power to the sensors connected to the POINT Guard Analog Input module, set this value to Module. This setting allows the module to detect a loss of sensor power.

## Configure Safety Analog Input Alarms (Optional)

<!-- image -->

If you use a Dual-channel Analog (DCA) safety instruction in your application program, we recommend that you do not configure these values on the module. Instead, to facilitate troubleshooting, use the application program to check for high and low alarm values via the Dual-Channel Analog Input instruction or other data comparison instructions.

To configure alarms for each of the safety analog input channels, follow these steps.

1. From the Module Properties dialog box, click the Alarm tab.
2. To configure each channel, click 0, 1, 2, or 3, as appropriate.
3. To enable the alarm, check the boxes:
- Enable High High - Low Low Alarms
- Enable High - Low Alarms
4. Use these guidelines to enter the alarm values from -32768…+32767 in the appropriate fields.
- The High High alarm value must be greater than or equal to the High alarm value.
- The High alarm value must be greater that the Low alarm value.
- The Low Low alarm value must be less than or equal to the Low alarm value.
- These values are based on the engineering units that are configured on page 85 .
5. Configure a deadband value for the High High - Low Low alarms and High - Low alarms, if desired.

<!-- image -->

The valid range is 0…32767. The deadband lets the alarm status bit remain set, despite the removal of the alarm condition, as long as the input data remains within the deadband of the alarm. These values are based on the engineering units that are configured on page 85 .

For more information on this feature, see Process Alarms on page 29

## Configure Tachometer Operation

You can only configure the module for tachometer operation if your Module Definition includes Output Data for Safety-Tachometer.

<!-- image -->

Follow these steps to define how the module operates in Tachometer mode.

1. From the Module Properties dialog box, click the Tachometer Configuration tab.
2. Turn Dual Low Detection ON or OFF for each channel pair.

<!-- image -->

To increase the diagnostic coverage of your speed sensing loop, you must determine whether the two tachometer sensors you use to sense speed are shorted together. That is, you must be able to detect a channel-to-channel fault. One method is to implement two tachometer sensors so that, during normal operation, their pulse trains are never low simultaneously. When Dual Low Detection is ON, the module detects this condition as a fault. This fault indicates that the two sensors are shorted together.

To use this feature, you must use Channels 0 and 1 together, and Channels 2 and 3 together. Channels 0 and 1 have the same setting and channels 2 and 3 have the same setting.

3. Configure the Trigger to indicate if the module channels must count pulses on the rising edge or falling edge.

When the module is configured as Dual, channels 0 and 1 have the same setting and channels 2 and 3 have the same setting.

4. Specify a tachometer Off Level in volts for each channel.

This level is the voltage at which the module considers the tachometer sensor to be OFF for tachometer speed calculation purposes.

The valid range is 0…23V in increments of 1V. The default setting of 5V must be satisfactory for a 0...24V DC signal. For a 0...5V DC signal, a setting of 1V is recommended.

See Off and On Signal Levels on page 33 for more information on the Off and On Levels.

When the module is configured as Dual Channel Equivalent, channels 0 and 1 have the same setting and channels 2 and 3 have the same setting.

5. Specify a tachometer On Level in volts for each channel.

This level is the voltage at which the module considers the tachometer sensor to be ON for tachometer speed calculation purposes

The valid range is 1…24V in increments of 1V. The default setting of 11V must be satisfactory for a 0...24V DC signal. For a 0...5V DC signal, a setting of 4V is recommended.

See Off and On Signal Levels on page 33 for more information about the Off and On Levels.

When the module is configured as dual-channel Equivalent, channels 0 and 1 have the same setting and channels 2 and 3 have the same setting. The tachometer On Level must be greater than the tachometer Off Level.

## Values and States of Tags

Table 5 - Tag Values and States

|                     | Data Description                       |                                                                                                                                                   |
|---------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|                     | Run Mode STANDARD                      | Indicates whether consumed data is actively being updated by a device that is in one of these states: •  Run mode: 1 Idle State: 0                |
|                     | Connection Faulted STANDARD            | Indicates the validity of the safety connection between the safety producer and the safety consumer. •  Valid: 0 Faulted: 1                       |
|                     | Safety Input Data SAFETY               | Indicates the ON/OFF state of each input circuit. •  ON: 1 OFF: 0                                                                                 |
|                     | Combined Safety Input Status SAFETY    | An AND of the status of all input circuits. •  All circuits are normal: 1 •  An error was detected in one or more input circuits: 0               |
|                     | Individual Safety Input Status SAFETY  | Indicates the status of each input circuit. •  Normal: 1 Fault (Alarm): 0                                                                         |
|                     | Combined Safety Output Status SAFETY   | An AND of the status of all safety output circuits. •  All circuits are normal: 1 •  An error has been detected in one or more output circuits: 0 |
|                     | Individual Safety Output Status SAFETY | Indicates the status of each safety output circuit. •  Normal: 1 Fault (Alarm): 0                                                                 |
|                     | Muting Lamp Status SAFETY              | Indicates the status when circuits T1 and T3 are configured as the muting lamp output. •  Normal: 1 Fault (Alarm): 0                              |
|                     | Output Readback STANDARD               | Monitors the presence of 24V on the output circuit. Readback is ON (1) if 24V is on the output terminal. •  ON: 1 OFF: 0                          |
|                     | Individual Test Output Status STANDARD | Indicates the status of each of the test output circuits. •  Normal: 1 Fault (Alarm): 0                                                           |
|                     | Input Power Error Bit STANDARD         | Indicates that the field power that is supplied is within specification. •  Power error: 1 Power OK: 0                                            |
|                     | Output Power Error Bit STANDARD        | Indicates that the field power that is supplied is within specification. •  Power error: 1 Power OK: 0                                            |
| Digital Output Data | Safety Output Data SAFETY              | Controls the safety output. •  ON: 1 OFF: 0                                                                                                       |
| Digital Output Data | Standard Output Data STANDARD          | Controls the test output when Test Output mode is set to a standard output. •  ON: 1 OFF: 0                                                       |

This table shows the values and states of the tags.

## IMPORTANT

In this table, 'SAFETY' denotes information the controller can use in safety-related functions. 'STANDARD' denotes additional information that must not be directly used for safety functions.

<!-- image -->

ATTENTION: Do not rely on data readback to detect faults. You must monitor the status bits to detect faults.

## Table 5 - Tag Values and States

| Data Description                                     |                                                                                                                                                                    |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run Mode STANDARD                                    | Indicates whether consumed data is actively being updated by a device that is in one of these states: •  Run mode: 1 Idle State: 0                                 |
| Connection Faulted STANDARD                          | Indicates the validity of the safety connection between the safety producer and the safety consumer. •  Valid: 0 Faulted: 1                                        |
| Safety Input Data SAFETY                             | Value of analog input data                                                                                                                                         |
| Individual Safety Input Status SAFETY                | Indicates the status of each safety input circuit. Normal: 1 Fault (Alarm): 0                                                                                      |
| Individual Status - Process Alarms STANDARD          | Indicates whether each Safety Input Data value of a channel is between the configured High and Low Alarm values. Normal: 1 Alarm: 0                                |
| Individual Status - Fault Reason STANDARD            | Input Point Fault Reason                                                                                                                                           |
| Individual HH Alarm Status STANDARD                  | Individual High High Alarm Status Normal: 1 Alarm: 0                                                                                                               |
| Analog Input Data Individual H Alarm Status STANDARD | Individual High Alarm Status Normal: 1 Alarm: 0                                                                                                                    |
| Individual L Alarm Status STANDARD                   | Individual Low Alarm Status Normal: 1 Alarm: 0                                                                                                                     |
| Individual LL Alarm Status STANDARD                  | Individual Low Low Alarm Status Normal: 1 Alarm: 0                                                                                                                 |
| Individual Tachometer Overfrequency SAFETY           | When the input is configured for Tachometer mode, this data indicates an overfrequency condition; that is, when pulses are faster than 1000 Hz. Normal: 1 Fault: 0 |
| Individual Tachometer Under-frequency SAFETY         | When the input is configured for Tachometer mode, this data indicates an under-frequency condition; that is, when pulses are slower than 1 Hz. Normal: 1 Fault: 0  |
| Individual Tachometer Dual Low SAFETY                | Indicates that both channels are low when the input is configured for Tachometer mode. Normal: 1 Fault: 0                                                          |
| Input Power STANDARD                                 | Indicates that input power over- or underrange. Normal: 1 Fault: 0                                                                                                 |
| Analog Output Data Reset Tachometer SAFETY           | Resets a latched overfrequency condition and enables the module to begin to calculate frequency again. •  No reset: 0 Reset: 1                                     |

## Configure Safety Connections

To configure the safety input connection of the module, follow these steps.

1. From the Module Properties dialog box, click the Safety tab.

<!-- image -->

## 2. Click Advanced.

The Advanced Connection Reaction Time Limit Configuration dialog box opens.

<!-- image -->

- a. In the Requested Packet Interval (RPI) field, enter the input connection RPI to support your application (6…500 ms).

The smallest input RPI allowed is 6 ms. When you select small RPIs, it consumes network bandwidth and can cause spurious trips because other devices cannot get access to the network.

As an example, a safety input module with only E-stop switches connected works well with settings of 50…100 ms. An input module with a light curtain guarding a hazard needs the fastest response possible. When you select the appropriate RPIs, the system has maximum performance.

## Configuration Ownership

- b. Use the default values for Timeout Multiplier (2) and Network Delay Multiplier (200).

## IMPORTANT

To determine what is appropriate, analyze each safety channel. The default Timeout Multiplier of 2 and Network Delay Multiplier of 200 creates a worst-case input connection-reaction time limit of 4 times the RPI, and an output connection-reaction time limit of 3 times the RPI. A safety administrator must approve these changes only after a thorough review.

A connection status tag exists for every connection.

<!-- image -->

If the RPI and connection reaction time limit for the network are set appropriately, then this status tag must always remain low. Monitor all connection status bits to verify that they are not going high intermittently due to timeouts.

For more information about the Advanced Connection Reaction Time Limit Configuration dialog box, see the user manual for your controller. See Additional Resources on page 8 .

The connection between the owner and the POINT Guard I/O module is based on the following:

- POINT Guard I/O module number
- POINT Guard I/O safety network number
- GuardLogix slot number
- GuardLogix safety network number
- Path from the GuardLogix controller to the POINT Guard I/O module
- Configuration signature

If any differences are detected, the connection between the GuardLogix controller and the POINT Guard I/O module is lost, and the yellow yield icon appears in the controller project tree.

For more information, see Replace POINT Guard I/O Modules on page 131 .

## Save and Download the Module Configuration

## Update POINT Guard I/O Modules

After you configure a module, it is recommended that you save and download the configuration.

If, after you download the program, the MS and NS status indicators on the POINT Guard I/O module are not both steady green, there is a potential loss of ownership. A yellow yield icon in the project tree also indicates a loss of ownership. For more information, see Chapter 8 .

## IMPORTANT

When you use ControlFLASH™ software to update a module, the software stops a running safety I/O connection. You must inhibit I/O connections before updating a POINT Guard I/O module.

In addition, the 1734-IE4S safety analog input module requires field power to be applied while updating the firmware of the module. If a ControlFLASH update fails, click View Log on the Update Status dialog box to check the ControlFLASH log.

If the last message is '[FAILURE] Update: Error #11001: Unknown General Status error code received. GS = 0xD0, ES = 0x0001,' verify that field power is connected to the module and restart the download.

<!-- image -->

The module receives field power from the 24V DC connection to the power supply, for example a 1734-AENT, 1734-FPD, or 1734-EP24DC module. Make sure that 24V DC power is connected to these modules before performing a firmware update for the 1734-IE4S module.

## Notes:

<!-- image -->

## Configure the Module and a SmartGuard Controller

| Topic Page                                        |
|---------------------------------------------------|
| Before You Begin 96                               |
| Set the Node Address 96                           |
| Auto-address the Nodes with a 1734-PDN Adapter 98 |
| Set Up the DeviceNet Network 100                  |
| Configure the POINT Guard I/O Modules 101         |
| Configure the SmartGuard Controller 110           |
| Save and Download Module Configuration 115        |

This chapter provides information about how to configure a SmartGuard™ controller and POINT Guard I/O™ modules with USB (Universal Serial Bus) connectivity. See the RSNetWorx™ for DeviceNet® software help files for network-configurator operation procedures.

<!-- image -->

- For information about RSNetWorx for DeviceNet software, from the Help menu, choose RSNetWorx Help.

<!-- image -->

## Before You Begin

## Set the Node Address

Confirm that you have these required items:

- RSNetWorx for DeviceNet software
- RSLinx® software, version 2.51 or later
- SmartGuard USB driver

| Cat. No. Required Version       |
|---------------------------------|
| 1734-IB8S, 1734-OB8S 9 or later |
| 1734-IE4S 10 or later           |
| 1734-OBV2S 21 or later          |

The SmartGuard USB driver is already in your RSLinx software. If it is not, load the driver onto your computer. Note the folder location because you have to browse to it later.

- 1734-PDN adapter
- SmartGuard controller and POINT Guard I/O module EDS files

Download EDS files from Rockwell Automation's Product Compatibility and Download Center. Use the EDS Hardware Installation Tool to load the EDS files. You can also upload the EDS file from the device with either FactoryTalk® Linx or RSLinx® Classic.

Use RSNetWorx for DeviceNet software to set the node address of POINT Guard I/O modules. The module has an out-of-box preset node address of 63. We suggest that you connect and set the node address one module at a time. Otherwise, the address conflicts can prevent communication with some of the modules.

## IMPORTANT

The unique identifier for a safety node is a combination of the safety network number (SNN) and node address. When the SNN is set, the current node address is used to generate and store this identifier in nonvolatile memory. Once the identifier is set, for safety reasons, the node address cannot be changed unless specific action is taken to reset the POINT Guard I/O SSN of the module. For this reason, you are required to set the node address before the application of an SNN.

Follow these steps to set the node address with the node commissioning tool.

1. Choose Start&gt;Programs&gt;Rockwell Software&gt;RSNetWorx&gt;DeviceNet Node Commissioning Tool.
2. Click Browse.
3. Check 'I want to input the address for the device on the selected network'.
4. Browse to the DeviceNet network, and do not click OK when the browse is complete.

<!-- image -->

<!-- image -->

If you are unable to browse the DeviceNet network and see the POINT Guard modules, the modules were potentially configured to an incompatible data rate or node address. Attempt to add these modules on an isolated network to determine the node address and data rate.

5. Enter the current address for the device.

An out-of-box device uses address 63.

## Auto-address the Nodes with a 1734-PDN Adapter

## 6. Click OK

<!-- image -->

7. Enter the new address for the device.
8. Click Apply.
9. Look for confirmation in the messages section.

When sequential auto-addressing is used, the leftmost node address is configured and a parameter is set in the module that assigns addresses automatically to the nodes that reside to the right of the module. The leftmost node can be a POINT Guard I/O module or a standard POINT I/O module.

Follow these steps to use the auto-address feature.

1. Reset any modules that you are not sure are out-of-box.
2. Attach the first module to the 1734-PDN adapter.
3. Use the node commissioning tool to set the node address of this module.
4. Attach the additional nodes to the right of the module that is used in steps 2 and 3 .
5. Perform the auto-address feature on the module that is used in steps 2 and 3 .

<!-- image -->

## Set Up the DeviceNet Network

Before you begin to design a project with RSNetWorx for DeviceNet software, follow these procedures.

1. From RSLinx software, open RSWho and select the SmartGuard driver. RSWho browses the DeviceNet network that is connected to the SmartGuard controller.

In this example, three POINT Guard I/O modules are connected to the SmartGuard controller.

<!-- image -->

If the RSLinx software finds the nodes on the DeviceNet network, RSNetWorx for DeviceNet software also finds the nodes.

2. Open RSNetWorx for DeviceNet software.
3. From the Networks menu, choose Online.
4. Select the SmartGuard driver and click OK.

<!-- image -->

<!-- image -->

Configure the POINT Guard I/O Modules

## 5. Click OK.

RSNetWorx for DeviceNet software finds the SmartGuard and POINT Guard I/O modules on the DeviceNet network.

<!-- image -->

6. Click the online icon again to go offline.

From the Safety Configuration tab, you can configure the safety inputs and outputs of the module.

## Configure Digital Safety Inputs and Test Outputs

1. To open the Properties dialog box, double-click the POINT Guard I/O digital input module.

<!-- image -->

2. Click the Safety Configuration tab.
3. To configure the input points, double-click each set.

<!-- image -->

<!-- image -->

| Parameter Name Value Description Default                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Point Operation Type Single Channel Use as a single channel. Single                                                                                                                                                                                          |
| Dual-channel Equivalent Use as a dual-channel. Normal when both channels are ON or OFF.                                                                                                                                                                            |
| Dual-channel Complementary Use as a dual-channel. Normal when one channel is ON and the other channel is OFF.                                                                                                                                                      |
| Input Point Mode Not Used External input device is not connected. Not Used                                                                                                                                                                                         |
| Safety Pulse Test Use with a contact output device and in combination with a test output. When you use this setting, short-circuits between input signal lines and the power supply (positive side) and short-circuits between input signal lines can be detected. |
| Safety A solid-state output safety sensor is connected.                                                                                                                                                                                                            |
| Standard A standard device, such as a reset switch, is connected.                                                                                                                                                                                                  |

|               | Parameter Name Value Description Default                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
|               | Safety Input Test Source None The test output that is used with the input. None                     |
| Test Output 0 | Safety Input Test Source None The test output that is used with the input. None                     |
| Test Output 1 | Safety Input Test Source None The test output that is used with the input. None                     |
| Test Output 2 | Safety Input Test Source None The test output that is used with the input. None                     |
| Test Output 3 | Safety Input Test Source None The test output that is used with the input. None                     |
|               | Input Delay Time Off -> On 0…126 ms (in 6 ms increments) Filter time for OFF to ON transition. 0 ms |
|               | Input Delay Time On -> Off 0…126 ms (in 6 ms increments) Filter time for ON to OFF transition. 0 ms |

4. To pulse test the module, edit the parameters so that the channels are pulse tested by Test sources 0 and 1, respectively.
5. To edit the Input Error Latch Time, double-click the General folder.

<!-- image -->

The default value is 1000 ms.

<!-- image -->

6. To configure the test output points, double-click the Test Output Points folder.
7. Click Apply and OK.

| Parameter Name Value Description Default                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test Output Mode Not Used An external device is not connected. Not Used                                                                                  |
| Standard The output is connected to a standard device.                                                                                                   |
| Pulse Test A contact output device is connected. Use in combination with a safety input.                                                                 |
| Power Supply The power supply of a Safety Sensor is connected. The voltage that is supplied to I/O power (V, G) is output from the test output terminal. |
| Muting Lamp Output An indicator is connected and turned ON to detect broken lines in an external indicator.                                              |

## Configure Digital Safety Outputs

1. To display the parameters for editing, double-click each group of Outputs Points.

<!-- image -->

| Parameter Name Value Description Default                         |                                                                                                                                                                                               |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                  | Output Point Mode Not Used An external output device is not connected. Not Used                                                                                                               |
|                                                                  | Safety When the output is ON, the test pulse is not output (remains ON).                                                                                                                      |
|                                                                  | Safety Pulse Test When you use this function, short-circuits between output signal lines and the power supply (positive side) and short-circuits between output signal lines can be detected. |
| Output Point Operation Type                                      | Single Channel Use as a single channel. Dual-channel                                                                                                                                          |
| Output Point Operation Type                                      | Dual-channel Use as a dual-channel. When both channels are normal, outputs can be turned ON.                                                                                                  |
| Safety Output Error Latch Time 0…65,530 ms (in 10 ms increments) | Safety output errors are latched for this time. 1000 ms                                                                                                                                       |

2. To change from the default value (1000 ms), if desired, double-click Output Error Latch Time.
3. Click Apply and OK to return to the main RSNetWorx for DeviceNet dialog box.

<!-- image -->

## Configure Safety Analog Inputs

To configure a 1734-IE4S module, follow these steps.

1. To open the Properties dialog box, double-click the POINT Guard I/O analog module.
2. Click the Safety Configuration tab.

<!-- image -->

3. To display the parameters for editing, double-click each group of Dual Channel Safety Inputs.

<!-- image -->

|                                                     | Parameter Name Value Description Default                                                                                                                                                                                                                                                                                                                                                                         |        |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|                                                     | Channel type Single Inputs are treated as single channels. Dual-channel safety inputs can be configured as two individual, single channels.                                                                                                                                                                                                                                                                      | Single |
|                                                     | Equivalent Inputs are treated as a dual-channel equivalent pair. The channels must match within the discrepancy time or an error is generated.                                                                                                                                                                                                                                                                   | Single |
| Discrepancy time 0…65,530 (in 10 ms increments)     | When Dual Channel mode is selected, this value is the amount of time the two channels can differ from each other (larger than the deadband value) before a discrepancy error is declared. A discrepancy time of 0 ms means that the channels in a dual configuration can be discrepant for an infinite amount of time without an indicated fault, which effectively removes the usefulness of dual channel mode. | 100 ms |
| Discrepancy deadband 0…32767 (in engineering units) | In Dual Channel mode, when the paired input values exceed the deadband tolerance for longer than the Discrepancy Time, a discrepancy fault occurs. Configure a deadband value for applications that use two sensors to measure the same variable; otherwise, spurious trips can occur.                                                                                                                           | 0      |
| Channel offset -32768…+32767 (in engineering units) | Offset value for dual channel mode only. Configure an offset when differences in the sensors nominal input signals exceed the desired deadband.                                                                                                                                                                                                                                                                  | 0      |

<!-- image -->

4. To display the parameters for editing, double-click each Channel Safety Configuration group.

<!-- image -->

|                                              | Parameter Name Value Description Default                                                                                                                                                                                                              |          |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|                                              | Input Mode Not Used External input device is not connected.                                                                                                                                                                                           | Not Used |
|                                              | Safety A solid-state safety sensor is connected.                                                                                                                                                                                                      | Not Used |
|                                              | Standard A standard device is connected.                                                                                                                                                                                                              | Not Used |
| Input Range ±10V                             | Input voltage range.                                                                                                                                                                                                                                  | 4…20 mA  |
| 0…5V                                         | Input voltage range.                                                                                                                                                                                                                                  | 4…20 mA  |
| 0…10V                                        | Input voltage range.                                                                                                                                                                                                                                  | 4…20 mA  |
| ±5V                                          | Input voltage range.                                                                                                                                                                                                                                  | 4…20 mA  |
| 4…20 mA                                      | Input current range.                                                                                                                                                                                                                                  | 4…20 mA  |
| 0…20 mA                                      | Input current range.                                                                                                                                                                                                                                  | 4…20 mA  |
|                                              | Tachometer Tachometer mode.                                                                                                                                                                                                                           | 4…20 mA  |
| Latch Time 0…65,530 ms (in 10 ms increments) | Safety input errors are latched for this time so that the controller can read them and they are not missed if they clear themselves too quickly. One value for all channels.                                                                          | 1000     |
|                                              | Filter Setting 1 Hz A single-pole, anti-aliasing filter of 10 Hz is followed by a four-pole digital filter with these (1) available frequencies. (1)                                                                                                                                                                                                                                                       | 1 Hz     |
| 5 Hz                                         | Filter Setting 1 Hz A single-pole, anti-aliasing filter of 10 Hz is followed by a four-pole digital filter with these (1) available frequencies. (1)                                                                                                                                                                                                                                                       | 1 Hz     |
| 10 Hz                                        | Filter Setting 1 Hz A single-pole, anti-aliasing filter of 10 Hz is followed by a four-pole digital filter with these (1) available frequencies. (1)                                                                                                                                                                                                                                                       | 1 Hz     |
| 50 Hz                                        | Filter Setting 1 Hz A single-pole, anti-aliasing filter of 10 Hz is followed by a four-pole digital filter with these (1) available frequencies. (1)                                                                                                                                                                                                                                                       | 1 Hz     |
|                                              | High Engineering -30000…+30000 Scaling value for inputs 10000                                                                                                                                                                                         | (2)      |
|                                              | Low Engineering -30000…+30000 Scaling value for inputs 0                                                                                                                                                                                              |          |
|                                              | Sensor Power Source External An external power supply is used to power the analog sensors. Terminals S0…S3 on the module are not used.                                                                                                                | Module   |
|                                              | Module Terminals S0…S3 on the module are used to power the analog sensors. Set this value to Module to supply power to the sensors connected to the POINT Guard Analog Input module. This setting allows the module to detect a loss of sensor power. | Module   |

<!-- image -->

5. To display parameters for editing, double-click each engineering units Alarms group.

<!-- image -->

| Parameter Name Value Description Default   |                             |                                                                                                                                                                                                                                                                                                                                                                            |         |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| High High/Low Low Alarm Enable             |                             | Disable Enable or disable alarms.                                                                                                                                                                                                                                                                                                                                          | Disable |
| High High/Low Low Alarm Enable             | Enable                      | Disable Enable or disable alarms.                                                                                                                                                                                                                                                                                                                                          | Disable |
|                                            |                             | High High Alarm -32768…+32767 Follow these guidelines when to set the alarm values. •  The High High alarm value must be greater than or equal to the High alarm value. •  The High alarm value must be greater that the Low alarm value. •  The Low Low alarm value must be less than or equal to the Low alarm value. •  These values are based on the engineering units | 32767   |
|                                            | Low Low Alarm -32768…+32767 | High High Alarm -32768…+32767 Follow these guidelines when to set the alarm values. •  The High High alarm value must be greater than or equal to the High alarm value. •  The High alarm value must be greater that the Low alarm value. •  The Low Low alarm value must be less than or equal to the Low alarm value. •  These values are based on the engineering units | 0       |
|                                            | High Alarm -32768…+32767    | High High Alarm -32768…+32767 Follow these guidelines when to set the alarm values. •  The High High alarm value must be greater than or equal to the High alarm value. •  The High alarm value must be greater that the Low alarm value. •  The Low Low alarm value must be less than or equal to the Low alarm value. •  These values are based on the engineering units | 32767   |
|                                            | Low Alarm -32768…+32767     | High High Alarm -32768…+32767 Follow these guidelines when to set the alarm values. •  The High High alarm value must be greater than or equal to the High alarm value. •  The High alarm value must be greater that the Low alarm value. •  The Low Low alarm value must be less than or equal to the Low alarm value. •  These values are based on the engineering units | 0       |
| High High/Low Low Alarm deadband           |                             | 0…32767 Deadband on the High High and Low Low alarms. 0                                                                                                                                                                                                                                                                                                                    |         |
|                                            |                             | High/Low Alarm deadband 0…32767 Deadband on the High and Low alarms. 0                                                                                                                                                                                                                                                                                                     |         |

6. To display parameters for editing, double-click each Channel Tachometer Configuration group.

<!-- image -->

|                                         | Parameter Name Value Description Default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |          |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|                                         | Tach Dual Low Detection On To increase the diagnostic coverage of your speed sensing loop, you must determine whether the two tachometer sensors you are using to sense speed are shorted together. That is, you must be able to detect a channel-to-channel fault. One method is to implement two tachometer sensors so that, during normal operation, their pulse trains are never low simultaneously. When Dual Low Detection is enabled, the module detects this condition as a fault, which indicates that the two sensors are shorted together. To use this feature, you must use Channels 0 and 1 together, and Channels 2 and 3 together. Channels 0 and 1 have the same setting and channels 2 and 3 have the same setting. Both channels in the pair must use tachometer mode and the dual low detection diagnostic. | Disabled |
| Off                                     | Tach Dual Low Detection On To increase the diagnostic coverage of your speed sensing loop, you must determine whether the two tachometer sensors you are using to sense speed are shorted together. That is, you must be able to detect a channel-to-channel fault. One method is to implement two tachometer sensors so that, during normal operation, their pulse trains are never low simultaneously. When Dual Low Detection is enabled, the module detects this condition as a fault, which indicates that the two sensors are shorted together. To use this feature, you must use Channels 0 and 1 together, and Channels 2 and 3 together. Channels 0 and 1 have the same setting and channels 2 and 3 have the same setting. Both channels in the pair must use tachometer mode and the dual low detection diagnostic. | Disabled |
|                                         | Tach Trigger Type Falling edge (NPN) Non-inverted input signal. Falling edge                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          |
|                                         | Rising edge (PNP) Inverted input signal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |          |
| Tach Off Level 0…23V (in 1V increments) | This value is the voltage at which the module considers the tachometer sensor to be OFF for tachometer speed calculation purposes. The Tachometer Off Level must be less than the Tachometer On Level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 5V       |
| Tach On Level 1…24V (in 1V increments)  | This value is the voltage at which the module considers the tachometer sensor to be ON for tachometer speed calculation purposes. The Tachometer On Level must be greater than the Tachometer Off Level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 11V      |

## Configure the SmartGuard Controller

To configure input and output connections to the controller and complete the setup of the controller, follow the procedures in these sections.

## Set Up the Input and Output Connections

1. In RSNetWorx for DeviceNet software, right-click the SmartGuard controller and choose Properties.
2. For a list of all the Safety I/O modules in your project, click the Safety Connection tab.

<!-- image -->

<!-- image -->

3. Right-click the POINT Guard I/O module and choose Add Connection.

<!-- image -->

The Add Safety Connection dialog box appears.

<!-- image -->

You can add individual safety connections for the inputs and outputs. The SmartGuard 600 controller can have up to 32 connections.

4. To add a safety connection, from the Connection Name dropdown menu, choose one of these options.

|            |                                               | Choose Description                                                                                                               |
|------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1734-IB8S  |                                               | [IN] Safety Control of safety inputs                                                                                             |
| 1734-IB8S  | [IN] Safety + [] y  Combined Status(1) - Muting                                               | •  Control of safety inputs •  Status combined into 1 bit for all inputs •  Muting status is available                           |
| 1734-IB8S  | [IN] Safety + Pt. Status                      | •  Control of safety inputs •  Individual status for each input point                                                            |
| 1734-IB8S  | [IN] Safety + Pt. Status - Muting             | •  Control of safety inputs •  Individual status for each input point •  Muting status available                                 |
| 1734-IB8S  | [IN] Safety + Pt. Status Muting - Test Output                                               | •  Control of safety inputs •  Individual status for each input point •  Muting status available •  Test output status available |
| 1734-OB8S  |                                               | [OUT] Test Control of test outputs                                                                                               |
| 1734-OB8S  | [IN] Safety Monitor - Combined Status - Power | •  Monitor safety outputs •  Status combined into 1 bit for all outputs •  Power status available                                |
| 1734-OB8S  | [IN] Safety Output Status                     | •  Individual status for each output point                                                                                       |
| 1734-OB8S  | [IN] Safety Output Status+ Monitor            | •  Individual status for each output point •  Monitor safety outputs                                                             |
| 1734-OB8S  |                                               | [OUT] Safety Control of safety outputs                                                                                           |
| 1734-OBV2S | [IN] Safety Monitor - Combined Status - Power | •  Monitor safety outputs •  Status combined into 1 bit for all outputs •  Power status available                                |
| 1734-OBV2S | [IN] Safety Output Status                     | •  Individual status for each output point                                                                                       |
| 1734-OBV2S | [IN] Safety Output Status+ Monitor            | •  Individual status for each output point  •  Monitor safety outputs                                                            |
| 1734-OBV2S |                                               | [OUT] Safety Control of safety outputs                                                                                           |
| 1734-IE4S  | [IN] Channel and Combined Alarm Status        | Combined channel status and alarm status for each input point                                                                    |
| 1734-IE4S  | [IN] Channel Status, Alarm Status             | •  Individual status for each input point •  Combined alarm status for each input point •  Power status                          |
| 1734-IE4S  |                                               | [OUT] Tach Reset Resets a latched overfrequency condition and enables the module to begin to calculate frequency again.          |

The more status that is read, the larger the packet size.

5. From the Connection Type dropdown menu, for this example choose Multicast.
6. From the Configuration dropdown menu, for this example choose Configuration signature must match.

7. In the Requested Packet Interval (RPI) box, enter 10 ms.
8. In the Connection Reaction Time Limit (CRTL), enter 40.1 ms.
9. Click Add.

This value limits the packet size for normal communication. If detailed status is required when a fault occurs, the data can be read explicitly with MSG instructions.

10. Repeat steps 3…9 for each connection, be sure to assign input and output connections.

Note that the connections for the 1734-IB8S module have 2 bytes. If you select individual point status, the input connection is 5 bytes.

<!-- image -->

## 11. Click Apply.

For further details, see the SmartGuard 600 Controllers User Manual, publication 1752-UM001, and SmartGuard 600 Controllers Safety Reference Manual, publication 1752-RM001 .

## Complete the Set Up of the SmartGuard Controller

1. From the 1752-L24BBB dialog box, click Apply and then OK to accept the connection.
2. Place RSNetWorx from DeviceNet software back into Online mode.
- a. If you see this dialog box, click Yes to save changes.
- b. To upload or download the device information, click OK.

<!-- image -->

<!-- image -->

You see these nodes after the browse.

<!-- image -->

## Save and Download Module Configuration

We recommend that after a module is configured you save your work

| IMPORTANT   | If you have not followed the configuration guidelines in the parameter tables that are found in Configure Safety Analog Inputs on page 105, the error message “Invalid Configuration Parameter occurred while attempting to configure the safety device” appears in the Error Log during download.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

If the MS and NS status indicators on the POINT Guard I/O module are not both steady green after download, ownership has the potential to have been lost. The ownership is based on the following:

- POINT Guard I/O module number
- POINT Guard I/O safety network number
- SmartGuard slot number
- SmartGuard safety network number
- Path from SmartGuard controller to POINT Guard I/O module
- Configuration signature

If any of these parameters change, the connection between the SmartGuard controller and the POINT Guard I/O module is lost, and a yellow yield icon appears in the RSNetWorx for DeviceNet tree. For more information, see Chapter 8 .

## Notes:

## Configure the Module in RSNetWorx for DeviceNet Software

<!-- image -->

## Configure Safety Connections between a GuardLogix Controller and POINT Guard I/O Modules on a DeviceNet Network

| Topic Page                                                   |
|--------------------------------------------------------------|
| Configure the Module in RSNetWorx for DeviceNet Software 117 |
| Add the POINT Guard I/O Module to the Controller Project 118 |
| Complete the Safety Configuration 122                        |
| Download the DeviceNet Network Configuration 124             |
| Verify Your DeviceNet Safety Configuration 125               |

To use POINT Guard I/O™ modules with a GuardLogix® controller on a DeviceNet® network, you must use a 1734-PDN DeviceNet Communication Interface module. When you use a 1734-PDN module, you must use RSNetWorx™ for DeviceNet software to configure the POINT Guard I/O modules. The Generic DeviceNet Safety Module profile in the Studio 5000 Logix Designer application to use the module data inside of the safety task.

You must complete these steps in RSNetWorx for DeviceNet software before you can add the module to the GuardLogix controller project.

1. Use the Node Commissioning Tool to set the node address of the module. See Set the Node Address on page 96 .
2. Configure the inputs and outputs of the module. See Configure the POINT Guard I/O Modules on page 101 .

## Add the POINT Guard I/O Module to the Controller Project

Follow these steps to connect to the controller.

1. In the Studio 5000 Logix Designer application, right-click the DeviceNet network and choose New Module.
2. In the Select Module Type dialog box, check Safety and Allen-Bradley.
3. Select the Generic DeviceNet Safety Module and click Create.
4. On the New Module dialog box, click Change.

<!-- image -->

<!-- image -->

5. On the Module Definition dialog box, set these parameters for your module.

| Cat. No. Product Type Product Code   |
|--------------------------------------|
| 1734-IB8S 35 15                      |
| 1734-OB8S 35 16                      |
| 1734-OBV2S 35 32                     |
| 1734-IE4S 42 1                       |

## 1734-IB8S Module 1734-IE4S Module

<!-- image -->

<!-- image -->

6. Click the Connection tab.
7. Set the Configuration Assembly Instance to 864 for all POINT Guard modules.

<!-- image -->

8. Use theses tables to determine which assemblies you want to connect to and set the safety input and output assemblies.

Table 6 - 1734-IB8S Input Assemblies

| Safety Input Connection Input Assembly Safety Input Number   | Input Assembly Safety Output Number Size   |
|--------------------------------------------------------------|--------------------------------------------|
|                                                              | Safety 516 (204 h) 199 (C7h) 1             |
| Safety + Combined Status – Muting 788 (314 h) 199 (C7h) 2    |                                            |
| Safety + Pt. Status 548 (224 h) 199 (C7h) 2                  |                                            |
| Safety + Pt. Status – Muting 820 (334 h) 199 (C7h) 3         |                                            |
| Safety + Pt. Status – Muting – Test Output                   | 868 (364 h) 199 (C7h) 4                    |

## Table 7 - 1734-IB8S Output Assemblies

| Safety Output Connection Output Assembly Safety Input Number   | Output Assembly Safety Output Number   | Size   |
|----------------------------------------------------------------|----------------------------------------|--------|
| Test 199 (C7h) 33 (21 h) 1                                     |                                        |        |

## Table 8 - 1734-OB8S Input Assemblies

| Safety Input Connection Input Assembly Safety    | Input Number             | Input Assembly Safety Output Number   | Size   |
|--------------------------------------------------|--------------------------|---------------------------------------|--------|
| Safety Output Status 580 (244 h) 199 (C7h) 1     |                          |                                       |        |
| Output Status + Monitor 1028 (404 h) 199 (C7h) 2 |                          |                                       |        |
| Safety Monitor + Combined Status + Power         | 1044 (414 h) 199 (C7h) 2 |                                       |        |

## Table 9 - 1734-OB8S Output Assemblies

| Safety Output Connection Output Assembly Safety Input Number   | Output Assembly Safety Output Number   | Size   |
|----------------------------------------------------------------|----------------------------------------|--------|
|                                                                | Safety 199 (C7h) 564 (234 h) 1         |        |

Table 10 - 1734-OBV2S Input Assemblies

| Safety Input Connection Input Assembly Safety    | Input Number             | Input Assembly Safety Output Number   | Size   |
|--------------------------------------------------|--------------------------|---------------------------------------|--------|
| Safety Output Status 579 (243 h) 199 (C7h) 1     |                          |                                       |        |
| Output Status + Monitor 1027 (403 h) 199 (C7h) 1 |                          |                                       |        |
| Safety Monitor + Combined Status + Power         | 1043 (413 h) 199 (C7h) 2 |                                       |        |

Table 11 - 1734-OBV2S Output Assemblies

| Safety Output Connection Output Assembly Safety Input Number   | Output Assembly Safety Output Number   | Size   |
|----------------------------------------------------------------|----------------------------------------|--------|
|                                                                | Safety 199 (C7h) 563 (233 h) 1         |        |

Table 12 - 1734-IE4S Input Assemblies

| Safety Input Connection Input Assembly Safety            | Input Number             | Input Assembly Safety Output Number   | Size   |
|----------------------------------------------------------|--------------------------|---------------------------------------|--------|
| Safety + Status 402 (192 h) 199 (C7h) 9                  |                          |                                       |        |
| Safety + Status + Alarms 786 (312 h) 199 (C7h) 13        |                          |                                       |        |
| Safety + Status + Process Status + Fault Reason + Alarms | 802 (322 h) 199 (C7h) 18 |                                       |        |

Table 13 - 1734-IE4S Output Assemblies

| Safety Output Connection Output Assembly Safety Input Number   | Output Assembly Safety Output Number      | Size   |
|----------------------------------------------------------------|-------------------------------------------|--------|
|                                                                | Safety Tachometer 199 (C7h) 770 (302 h) 1 |        |

Individual members of each assembly are listed in Appendix E .

## IMPORTANT

If you use the 1734-IE4S module with a GuardLogix system, use the application program to evaluate any dual channel requirements and determine any process alarms.

9. Click OK.
10. On the Safety Tab, uncheck the Configuration Signature checkbox.
11. Click OK and OK again to add the module to the I/O Configuration tree.

## Complete the Safety Configuration

Follow these steps to copy the configuration signature and safety network number from RSNetWorx for DeviceNet software to the generic profile you configure in the Studio 5000 Logix Designer application.

1. In RSNetWorx for DeviceNet software, double-click the module.
2. On the Safety tab, click Copy Signature.
3. In the Studio 5000 Logix Designer application, right-click the DEVICENET-SAFETYMODULE and choose Properties.

<!-- image -->

4. On the Safety tab, check the Configuration Signature checkbox.
5. Click Paste.
6. In RSNetWorx for DeviceNet software, click Copy to copy the safety network number.

<!-- image -->

<!-- image -->

## Download the DeviceNet Network Configuration

7. On the General tab in the Studio 5000 Logix Designer application, click next to the safety network number field.
8. Click Paste.

<!-- image -->

Before you download, you must go online to the DeviceNet network with RSNetWorx for DeviceNet software. Your computer and the devices you wish to communicate with must be connected to the DeviceNet network.

When you go online to a DeviceNet network, RSNetWorx for DeviceNet software browses the network one time and shows you the devices on the network. If you go online, this action does not upload (read) or download (change) the parameters of any of the devices.

To download the DeviceNet network configuration, follow these steps.

<!-- image -->

1. Click the online button.
2. Browse to the DeviceNet network and click OK at the prompt.
3. To download your configuration to the network, right-click the device and choose Download to Device.
4. To download, click yes.

## Verify Your DeviceNet Safety Configuration

## IMPORTANT

Before running the Safety Device Verification Wizard, you must browse and upload your network and test the safety devices and all of their safety functions on your network to verify that they are operating properly. You must fully test your application before you safety-lock your devices.

The Safety Device Verification Wizard, which is accessed from RSNetWorx for DeviceNet software, guides you through the verification of the configuration of your safety devices and provides the means for safety-locking those devices. The verification process includes upload and comparison of the configuration that is stored in the device and the configuration that is stored in the RSNetWorx for DeviceNet software configuration file. The configuration is displayed in a report to facilitate visual verification and record keeping.

## IMPORTANT

Some devices on your network may not support verification by the Safety Device Verification Wizard. To determine the method that is required for verifying these devices, consult the user documentation.

To run the Safety Device Verification Wizard, follow these steps.

1. Choose Network &gt;Safety Device Verification Wizard.
2. On the Welcome dialog box, click Next.

## Determine If Devices Can Be Verified

When the Safety Device Verification Wizard browses the network, it checks the safety status of the devices on the network to determine if the devices can be verified.

If any devices are in a state that prevents the wizard from continuing the verification process, the 'unable to verify that the listed devices dialog box' appears. The box lists those devices and their status, including a device icon that is overlaid with a status icon.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| Message Icon                | Overlay   | Description                                                                                                                                                 |
|-----------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Missing                     |           | The device is part of the network configuration, but was not found during the browse operation.                                                             |
| Mismatch                    |           | The device identity in the network configuration does not match the identity of the online device.                                                          |
| Unknown                     |           | The device is in the configuration, but has not been detected on the network yet.                                                                           |
| Safety Network Number Error |           | The safety network number (SNN) in the device is either invalid or does not match the SNN for the device in the RSNetWorx for DeviceNet configuration file. |
| Signature Mismatch          | None      | The configuration signature in the device does not match the configuration signature in the RSNetWorx for DeviceNet configuration file.                     |
| Safety Locked               |           | The device is already locked.                                                                                                                               |

To return to RSNetWorx for DeviceNet software so that you can correct the status of the indicated devices, close the Safety Device Verification Wizard by clicking Cancel.

To skip the devices that are listed and continue the verification process for other safety devices on the network, click Next.

## Select Devices to Verify

Choose which devices to verify by using the checkboxes in the Verify column on the Verify Safety Device Configuration dialog box. You can select only the devices whose status is Ready to be verified.

<!-- image -->

If the Show all safety devices checkbox is checked, the dialog box lists all safety devices on the network and shows their status. If it is unchecked, which is the default, only devices with the following status are shown:

- Verify FAILED

The upload and compare operation indicated that the configuration in the device does not match the configuration in the RSNetWorx for DeviceNet configuration file.

- Ready to be verified

The device is not safety-locked and can be selected for verification.

- Verify not supported

The device is not safety-locked, but the device does not support verification via the Safety Device Verification Wizard. Consult your user documentation for information on how to verify this device. Once the device has been verified, the wizard can safety-lock it.

## To begin the upload and compare process, click Next.

<!-- image -->

<!-- image -->

- If you click Next without selecting a device to verify, the wizard checks whether any devices were verified or are ready to be locked in this execution of the wizard.

|                                                 | If Then the wizard displays                                           |
|-------------------------------------------------|-----------------------------------------------------------------------|
|                                                 | Devices were verified The Review dialog box that lists those devices. |
| Devices are ready to be safety locked                                                 | The Lock dialog box that lists those devices.                         |
| No devices were verified The Finish dialog box. |                                                                       |
| No devices are ready to be safety-locked        | The Finish dialog box.                                                |

## Review the Safety Device Verification Reports

The Review page displays safety devices with a status of either Verify FAILED or Ready to be Safety Locked.

<!-- image -->

1. To launch the HTML report of the device in your default browser, click Review in the Report column.
2. To generate an HTML verification report for all devices listed, click Review All.

<!-- image -->

If the status of a device is Verify FAILED, more information is provided in the verification failure report.

3. Review and print the verification reports for your records.

## IMPORTANT

You must review the device configurations and record the configuration signatures before operating a safety application.

## Lock Safety Devices

IMPORTANT

Before you lock your safety device configurations, you must perform all verification steps that are required for your application.

1. Choose which devices to safety-lock by checking the checkbox in the Lock column for each device that is ready to be safety-locked.
2. Check the acknowledgment checkbox so the locking process can continue.
3. Click Next.

<!-- image -->

The wizard performs a final comparison of the configuration signature in each safety device to its configuration signature in RSNetWorx for DeviceNet software before locking the device.

- 4.

Before closing, the wizard displays a summary of all safety devices that were safety-locked. It also displays the number of safety devices that are still safety-locked, and lets you display the verified and safety-locked state of all

- View the Safety Device Verification Wizard Summary safety devices on the network.
5. To close the wizard, click Finish.

## The Safety Network Number

<!-- image -->

## Replace POINT Guard I/O Modules

| Topic Page                                                                               |
|------------------------------------------------------------------------------------------|
| The Safety Network Number 131                                                            |
| Set the Safety Network Number 132                                                        |
| Reset a Module to Out-of-box Condition 133                                               |
| Replace a Module in a GuardLogix System on an EtherNet/IP Network 136                    |
| Use a SmartGuard or GuardLogix Controller on a DeviceNet Network to Replace a Module 143 |

This chapter provides information on how to replace POINT Guard I/O™ modules when they are connected to GuardLogix® or SmartGuard™ controllers. For more information on these controllers, refer to the controller publications listed in the Additional Resources on page 8 .

A major difference in functionality between the GuardLogix and SmartGuard safety controllers affects the replacement of safety I/O modules. GuardLogix controllers retain the I/O module configuration and are able to download the configuration to the replacement module. SmartGuard controllers do not retain the I/O module configuration, so you must use RSNetWorx™ for DeviceNet® software to download the configuration to the replacement module.

Replacing a safety I/O module that sits on a CIP Safety™ network is more complicated than replacing standard devices because of the safety network number (SNN). The DeviceID of the safety module is composed of the module number and SNN. Safety devices require this more complex identifier to make sure that duplicate module numbers do not compromise communication between the correct safety devices.

## EXAMPLE

This simplified example shows Guard I/O™ modules on a DeviceNet network. Your products can differ, but the function is the same.

The DeviceNet network supports 64 node numbers, so if you have 100 devices on multiple DeviceNet networks, there are at least 36 duplicate node numbers being used. Even though the duplicate nodes are on separate DeviceNet networks, it must still be considered in a safety system.

In this example, the DNB scanner #1 is connected to node 5. The DNB scanner #2 is connected to another node 5. If the cables get inadvertently crossed, the scanners can be communicating with the incorrect node 5.

## Crossed Cables

<!-- image -->

This crossed-cable scenario is unacceptable for a safety system. The SNN provides unique identification of every safety device. In this next example, all devices that are connected to DNB scanner #1 have an SNN of 100. All devices that are connected to DNB scanner #2 have an SNN of 101. If the cables get inadvertently crossed, the node connected to DNB scanner #1 changes from 100/5 to 101/5. The node that is connected to DNB scanner #2 changes from 101/5 to 100/5. Therefore, the safety connections are not made if the cables get crossed.

## Connections Not Made

<!-- image -->

## Set the Safety Network Number

The previous examples showed how the SNN is used to provide safetyconnection integrity after the system is operational. But the SNN is also used to provide integrity on the initial download to the POINT Guard I/O module.

If a safety signature exists, then the POINT Guard I/O module must have a proper SNN/node number identification that matches the module within the safety controller project, before it can receive its configuration. And to keep integrity, the SNN setting of the module is required to be a manual action. This manual action is to use the 'set' function on an out-of-box POINT Guard I/O module.

## Reset a Module to Out-of-box Condition

Figure 49 - Set the SNN with a GuardLogix Controller

<!-- image -->

Figure 50 - Setting the SNN with a SmartGuard Controller

<!-- image -->

If a POINT Guard I/O module was used previously, clear the existing configuration before installing it on a safety network.

| To use POINT Guard I/O with a See                                 |                                                            |
|-------------------------------------------------------------------|------------------------------------------------------------|
| GuardLogix controller on an EtherNet/IP™ network                  | Use the Studio 5000 Logix Designer Application on page 134 |
| GuardLogix controller with 1734-PDN module on a DeviceNet network | Use RSNetWorx for DeviceNet Software on page 135           |
| SmartGuard controller on a DeviceNet network                      | Use RSNetWorx for DeviceNet Software on page 135           |

## Use the Studio 5000 Logix Designer Application

When the Studio 5000 Logix Designer application is online, the Safety tab of the Module Properties dialog box displays the current configuration ownership. When the opened project owns the configuration, Local is displayed. When a second device owns the configuration, Remote is displayed, along with the safety network number (SNN), and node address or slot number of the configuration owner. If the module read fails, Communication error is displayed.

If the connection is Local, you must inhibit the module connection before you reset ownership. To inhibit the module:

1. Right-click the module and choose Properties.
2. Click the Connection tab.
3. Select the Inhibit Module checkbox.
4. Click Apply and then OK.

Follow these steps to reset the module to its out-of-box configuration when online.

1. Right-click the module and choose Properties.
2. Click the Safety tab.
3. Click Reset Ownership.

## Use RSNetWorx for DeviceNet Software

Follow these steps to reset the module to an out-of-box condition.

1. Right-click the module and choose Reset Safety Device.
2. Check all options.
3. Click Reset.

<!-- image -->

<!-- image -->

## Replace a Module in a GuardLogix System on an EtherNet/IP Network

If you are relying on a portion of the CIP Safety system to maintain SIL 3 behavior during module replacement and functional testing, you must not use the Configure Always feature. Go to Replace a Module with 'Configure Only When No Safety Signature Exists' Enabled on page 137 .

If you are not relying on the entire routable CIP Safety control system to maintain SIL 3/PLe during the replacement and functional testing of a module, you can use the Configure Always feature. Go to Replace a Module with 'Configure Always' Enabled on page 142 .

Module replacement is configured on the Safety tab of the GuardLogix controller.

<!-- image -->

## Replace a Module with 'Configure Only When No Safety Signature Exists' Enabled

When a module is replaced, the configuration downloads from the safety controller if the DeviceID of the new module matches the original. The DeviceID is a combination of the node/IP address and the safety network number (SNN) and is updated whenever the SNN is set.

If the project is configured as 'Configure Only When No Safety Signature Exists', follow the appropriate instructions in Table 14 to replace a POINT Guard I/O module that is based on your scenario. Once you have completed the steps in the scenario correctly, the DeviceID matches the original. This match enables the safety controller to download the proper module configuration, and re-establish the safety connection.

Table 14 - Replace a Module

| GuardLogix Safety Signature Exists   | Replacement Module Condition                             | Action Required                                                                                                |
|--------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|                                      | No No SNN (Out-of-box)                                   | None. The module is ready for use.                                                                             |
|                                      | Yes or No Same SNN as original safety task configuration | None. The module is ready for use.                                                                             |
|                                      | Yes No SNN (Out-of-box)                                  | See Scenario 1 - Replacement Module Is Out-of-box and a Safety Signature Exists on page 137 .                  |
| Yes                                  | Different SNN from original safety task configuration    | See Scenario 2 - Replacement Module SNN Is Different from Original and a Safety Signature Exists on page 139 . |
|                                      | Different SNN from original safety task configuration    | gy  configuration No See Scenario 3 - Replacement Module SNN Is Different from Original and No Safety Signature Exists on page 141 .                                                                                                                |

Scenario 1 - Replacement Module Is Out-of-box and a Safety Signature Exists

1. Remove the old I/O module and install the new module.
2. Right-click the replacement POINT Guard I/O module and choose Properties.
3. To open the Safety Network Number dialog box, click to the right of the safety network number.

<!-- image -->

## 4. Click Set.

<!-- image -->

5. Verify that the Network Status (NS) status indicator is alternating red/ green on the correct module before clicking yes on the confirmation dialog box to set the SNN and accept the replacement module.
6. To test the replaced I/O module and system for functionality and authorize the system for use, follow your company-prescribed procedures.

<!-- image -->

## Scenario 2 - Replacement Module SNN Is Different from Original and a Safety Signature Exists

1. Remove the old I/O module and install the new module.
2. Right-click your POINT Guard I/O module and choose Properties.
3. Click the Safety tab.
4. Click Reset Ownership.
5. Click OK.
6. Right-click your module and choose Properties.
7. To open the Safety Network Number dialog box, click to the right of the safety network number.

<!-- image -->

<!-- image -->

## 8. Click Set.

<!-- image -->

9. Verify that the Network Status (NS) status indicator is alternating red/ green on the correct module before clicking yes on the confirmation dialog box to set the SNN and accept the replacement module.
10. To test the replaced I/O module and system for functionality and authorize the system for use, follow your company-prescribed procedures.

<!-- image -->

## Scenario 3 - Replacement Module SNN Is Different from Original and No Safety Signature Exists

1. Remove the old I/O module and install the new module.
2. Right-click your POINT Guard I/O module and choose Properties.
3. Click the Safety tab.
4. Click Reset Ownership.
5. Click OK.
6. To test the replaced I/O module and system for functionality and authorize the system for use, follow your company-prescribed procedures.

<!-- image -->

## Replace a Module with 'Configure Always' Enabled

<!-- image -->

ATTENTION: Enable the Configure Always feature only if the entire CIP Safety Control System is not being relied on to maintain SIL 3 behavior during the replacement and functional testing of a module.

Do not place modules that are in the out-of-box condition on a CIP Safety network when the Configure Always feature is enabled, except while following this replacement procedure.

When the 'Configure Always feature is enabled, the controller automatically checks for and connects to a replacement module that meets these requirements.

- The controller has configuration data for a compatible module at that network address.
- The module is in out-of-box condition or has an SNN that matches the configuration.

If the project is configured for 'Configure Always', follow the appropriate steps to replace a POINT Guard I/O module.

1. Remove the old I/O module and install the new module.
2. Right-click your POINT Guard I/O module and choose Properties.
3. Click the Safety tab.
4. Click Reset Ownership.
5. Click OK.
6. To test the replaced I/O module and system for functionality and authorize the system for use, follow your company-prescribed procedures.

| If Then                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| the module is in out-of-box condition go to step 6 . No action is needed for the GuardLogix controller to take ownership of the module. |
| an SNN mismatch error occurs go to the next step to reset the module to out-of-box condition.                                           |

<!-- image -->

## Use a SmartGuard or GuardLogix Controller on a DeviceNet Network to Replace a Module

To replace an I/O module when the module and the controller are on a DeviceNet network, follow these steps.

1. Replace the module and match the node number of the original module.
2. In RSNetWorx for DeviceNet software, open your project. If the replacement module is out-of-box or has an SNN that does not match the original module, the module appears with an exclamation mark.
3. Right-click the module and choose Download to Device.
4. Click Yes to confirm.
5. To set the SNN on the replacement module, click Download on the Safety Network Number Mismatch dialog box.

<!-- image -->

<!-- image -->

<!-- image -->

6. Verify that the (NS) Network status indicator is flashing on the correct module and click OK to set the SNN on that device.

<!-- image -->

RSNetWorx for DeviceNet software confirms that the SNN has been set.

<!-- image -->

Once the download successfully completes, the main project view displays this message: 'The device at address xx has been downloaded. Any devicespecific messages that are related to the download operation are displayed separately.'

<!-- image -->

If the configuration matches the original DNT file, the SNN and configuration signature now match that of the original. If you are already connected to the controller, a connection is made. The controller does not need to be taken out of Run mode to download to the replacement module.

If you download this configuration to a temporary setup, place the module on the network and it automatically connects to the controller.

If the configuration downloaded to the module was not from the original DNT file, the configuration signature does not match the original. Even if you recreate the same parameters in a new DNT file, the time and date portions of the signature are different so the connection to the controller is not made. If this situation occurs, click the Safety Connection tab for the controller that prompted you that the configuration signature is different and provides you with the option to match the new configuration signature. However, you must first revalidate the safety system because it is not using the original DNT file.

<!-- image -->

7. Click Yes.

This selection takes the controller out of Run mode and prompts you to download the changes.

<!-- image -->

8. Click Yes to download the new connection configuration to the SmartGuard controller.

After the download is complete, place the controller back in Run mode and the connection to the replacement module is established.

9. To test the replaced I/O module and system for functionality and authorize the system for use, follow your company-prescribed procedures.

## Notes:

Figure 51 - Status Indicators

<!-- image -->

## Troubleshoot the Module

| Topic Page                                          |
|-----------------------------------------------------|
| Module Status Indicator - MS 148                    |
| Network Status Indicator - NS 148                   |
| Configuration Lock Indicator - LK 148               |
| Power - PWR 149                                     |
| 1734-IE4S Sensor Power Indicator - S0…S3 149        |
| 1734-IE4S Safety Analog Input Status Indicators 149 |
| 1734-IB8S Safety Input Status Indicators 149        |
| 1734-OB8S Safety Output Status Indicators 149       |
| 1734-OBV2S Safety Output Status Indicators 150      |

Use the status indicators to troubleshoot the modules.

<!-- image -->

Table 15 - Module Status Indicator - MS

|                                                      | State Description Recommended Action                                                                                           |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|                                                      | Off No power is applied to the module. Apply power to this connector.                                                          |
| Steady green The module is operating normally. None. |                                                                                                                                |
|                                                      | Steady red The module detected an unrecoverable fault. Cycle power to the module. If the problem persists, replace the module. |
|                                                      | Flashing green The device is in the Idle or Standby state. Configure the module and establish a connection.                    |
|                                                      | Flashing red The module has detected a recoverable fault. Cycle power to the module or reset the module.                       |
|                                                      | A user-initiated firmware update is in progress. Wait for the firmware update to complete.                                     |
| Flashing red and green                               | The module is not configured. Reconfigure the module. For additional troubleshooting, use the Network status indicator.        |
| Flashing red and green                               | The module is performing its power-cycle diagnostic tests. Wait for the module to complete its power-cycle diagnostics.        |

## Table 16 - Network Status Indicator - NS

|                                                                                                                                                      | State Description Recommended Action              |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Off The module is not online with the network or there is no power. Verify that your network is working properly.                                    |                                                   |
| Flashing green The module is online with no connections in the established state. Verify your network and module configuration.                      |                                                   |
| The module identified the communication rate of the network but no connections are established.                                                      |                                                   |
| Steady green The module is online with connections in the established state. The module is operating normally.                                       | None.                                             |
| Flashing red One or more I/O connections are in a timed-out state. Verify your network and module configuration.                                     |                                                   |
| A user-initiated firmware update is in progress. Wait for the firmware update to complete.                                                           |                                                   |
| Steady red Critical link failure. The module detected an error that prevents it from communicating on the network, such as a duplicate node address. | Cycle power to the module. Check node addressing. |

## Table 17 - Configuration Lock Indicator - LK

|                                                                                           | State Description Recommended Action                                                                                                                 |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                           | Off No configuration or configured by a GuardLogix® originator. Validate configuration by a network configuration tool, such as RSNetWorx™ software. |
| Invalid configuration data.                                                               | Off No configuration or configured by a GuardLogix® originator. Validate configuration by a network configuration tool, such as RSNetWorx™ software. |
| Steady yellow Locked. None.                                                               |                                                                                                                                                      |
| Valid configuration, locked by a network configuration tool, such as RSNetWorx™ software. |                                                                                                                                                      |
| Flashing yellow Not locked.                                                               |                                                                                                                                                      |
| Valid configuration by a network configuration tool, such as RSNetWorx software.          |                                                                                                                                                      |

The configuration lock is not available when you use GuardLogix controllers.

## Table 18 - Power - PWR

|                                                                                                          | State Description Recommended Action                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off No field power applied (all modules) or severe 24V DC power over voltage condition (1734-OBV2S only) | Apply field power that is within the specifications.                                                                                                                                                                                                                                                                                                                                 |
| Green Normal condition, field power supplied and within specification. None.                             |                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                          | Yellow Field power is out of specification. The supplied field power is outside the specifications (all modules) or the module is configured to use sensor power, and either the sensor is drawing too much current (short in the wiring or sensor), or the sensor is not drawing any current (broken wire or sensor) (1734-IE4S only). Check your connectors, wiring, and voltages. |

## Table 19 - 1734-IE4S Sensor Power Indicator - S0…S3

| State Description Recommended Action                                                            |
|-------------------------------------------------------------------------------------------------|
| Off Sensor power is not used. None.                                                             |
| Green Sensor power is used.                                                                     |
| Red Overcurrent or undercurrent sensor power fault. Check connectors, wiring, and power supply. |

## Table 20 - 1734-IE4S Safety Analog Input Status Indicators

|                                                                                                        | State Description Recommended Action                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Safety analog input is not used or the module is being configured.                                 | Reconfigure the channel, if desired.                                                                                                                                                                                                                                                           |
| Yellow Safety analog input is configured for use and no faults exist. None.                            |                                                                                                                                                                                                                                                                                                |
|                                                                                                        | Red A fault has been detected in the analog input signal path. Check the fault code in the module that uses one of the data assemblies that contains the Fault Reason. See Appendix B for details. Check configuration, field wiring, and devices. If no problem is found, replace the module. |
| Flashing red A fault has been detected in the partner input signal path of a dual-input configuration. | Check the field wiring and verify your configuration for the partner circuit. If no problem is found, replace the module.                                                                                                                                                                      |

Indicator behavior in Tachometer mode facilitates machine setup and troubleshooting. When the tachometer signal is below the configured OFF threshold, the indicator is off. When the tachometer signal is above the ON threshold, the indicator is yellow. Status indicator behavior during normal operation is dependent upon the module update rate and is not intended to indicate the actual tachometer input. When the input rate is above 30 Hz, the status indicator is steady yellow. When the input rate is below 30 Hz, the status indicator is flashing yellow as the signal turns on and off.

## Table 21 - 1734-IB8S Safety Input Status Indicators

| State Description Recommended Action                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Safety input is off, or the module configuration is in progress. Turn on the safety input or reconfigure the channel, if desired.                                                                                        |
| Yellow Safety input is on. None.                                                                                                                                                                                             |
| Red A fault in the external wiring or input circuit has been detected. Check configuration, field wiring, and devices. If no problem is found, replace the module.                                                           |
| Flashing red A fault in the partner input circuit of a dual-input configuration has been detected. Check the field wiring and verify your configuration for the partner circuit. If no problem is found, replace the module. |

## Table 22 - 1734-OB8S Safety Output Status Indicators

| State Description Recommended Action                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------|
| Off Safety output is off, or the module is being configured. Turn on the safety output or reconfigure the channel, if desired. |
| Yellow Safety output is on. None.                                                                                              |

Indicators

Appendix A

## Table 22 - 1734-OB8S Safety Output Status Indicators

|                                                                                                                                                     | State Description Recommended Action                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                     | Red A fault in the output circuit has been detected. Check the circuit wiring and end device. If no problem is found, replace the module. |
| The tag values in a dual output configuration do not have the same value. Make sure that logic is driving tag values to the same state (off or on). |                                                                                                                                           |
| Flashing red A fault in the partner output circuit of a dual-output configuration has been detected.                                                | Check the circuit wiring and end device of the partner. If no problem is found, replace the module.                                       |

## Table 23 - 1734-OBV2S Safety Output Status Indicators

| State Description Recommended Action                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Safety output is off, or the module is being configured. Turn on the safety output or reconfigure the channel, if desired.                                            |
| Yellow Safety output is on. None.                                                                                                                                         |
| Red A fault in the output circuit has been detected. Check the circuit wiring and end device. If no problem is found, replace the module.                                 |
| The tag values do not have the same value. Make sure that logic is driving tag values to the same state (off or on).                                                      |
| Flashing red A fault in the partner output circuit has been detected. Check the circuit wiring and end device of the partner. If no problem is found, replace the module. |

## Message Instructions

<!-- image -->

## Get I/O Diagnostic Status from Modules in Logix Systems

| Topic Page                                              |
|---------------------------------------------------------|
| Message Instructions 151                                |
| Configure the Message Instruction 152                   |
| Class, Instance, and Attribute Data for I/O Modules 153 |

You can use message instructions in a Logix system to determine the cause of input point or output point faults.

When the controller detects a fault on an input or output point, you can use a message instruction to retrieve the cause of the fault.

In this example, we use a 1734-OB8S module with the Input Status set to return Point Status. This table illustrates the controller tags that you can monitor for this module.

<!-- image -->

| Adapter:2:1.Pt00OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
|--------------------------------|-----|-----------|--------|----------|
| Adapter:2:1.Pt01OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adapter:2:1.Pt020utputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adapter:2:1.Pt03OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adapter:2:1.Pt040utputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adapter:2:1.Pt05OutputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adapter:2:1.Pt060utputStatus   |   0 | Decimal   | BOOL   | Safety   |
| Adaoter:2:1.Pt070utoutStatus   |   0 | Decimal   | BOOL   | Safety   |

Use the Point Output Status bits to detect if one or more of the output points on the module have a fault:

- If any status bit goes to a value of 0 (0 = error, 1 = no error), use the status bit to condition your message instruction as follows.
- Place these rungs in the standard task.

This sample ladder logic is monitoring the status of output point 3. This ladder logic rung examines the Output Point Status and, when a fault is detected (0 = error), the message instruction is executed.

<!-- image -->

## Configure the Message Instruction

Follow this procedure to edit the Message Configuration in the ladder logic.

1. In the Message instruction, click the icon.
2. On the Configuration tab, enter the appropriate data for what you want to monitor.
- a. From the Service Type dropdown menu, choose Get Attribute Single.
- b. Enter the Class, Instance, and Attribute data that refer to the appropriate tables on pages 153 … 154 .
3. On the Communication tab, specify the path for the message.

This example illustrates the values that you enter to determine the reason for the fault on Output 3.

Figure 52 - Message Instruction Configuration Example

<!-- image -->

<!-- image -->

- When entering the Instance value, enter the input/output point plus 1. In this example, Output Point 3 is Instance 4.

## Class, Instance, and Attribute Data for I/O Modules

## Table 24 - Digital Safety Input Module - 1734-IB8S

|                      |                                                                                          | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)                                                                                                                             | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   |
|----------------------|------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|                      |                                                                                          | Service Code Class ID Instance ID Attribute ID Data  | Size                                                 |                                                                                                                                                                                |                                                      |                                                      |
| Get Attribute Single | Reads the cause for the safety digital input fault that the Instance ID (1…8) specifies. |                                                      |                                                      | 0E 3D 01…08 6E - 0: No error 01: Configuration invalid 02: External test signal error 03: Internal input error 04: Discrepancy error 05: Error in the other dual channel input |                                                      |                                                      |

Table 25 - Digital Safety Input Module Test Outputs - 1734-IB8S

|                      |                                                                                                                                         | Service Type Function Command (hex) Response (hex)       | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)                                                                                                                     | Service Type Function Command (hex) Response (hex)   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
|                      |                                                                                                                                         | Service Code Class ID Instance ID Attribute ID Data Size |                                                      |                                                      |                                                                                                                                                                        |                                                      |
| Get Attribute Single | Reads the cause of the test output fault that the Instance ID (1…4) specifies.                                                          |                                                          |                                                      |                                                      | 0E 09 01…04 76 - 0 = No error 01: Configuration invalid 02: Overload detected 03: Cross circuit detected 05: Output ON error 06: Undercurrent detected for muting lamp |                                                      |
| Set Attribute Single | Configures the test output to turn off or hold its last state after a communication error for an output that the Instance ID specifies. |                                                          | 10 09 01…04 05 1 byte                                | 00: Clear 01: Hold                                   | -                                                                                                                                                                      |                                                      |

## Table 26 - Digital Safety Output Module - 1734-OB8S

|                      |                                                                                           | Service Type Function Command (hex) Response (hex)       | Service Type Function Command (hex) Response (hex)                                                                                                                                                                                                                | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   |
|----------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|                      |                                                                                           | Service Code Class ID Instance ID Attribute ID Data Size |                                                                                                                                                                                                                                                                   |                                                      |                                                      |                                                      |
| Get Attribute Single | Reads the cause for the safety digital output fault that the Instance ID (1…8) specifies. |                                                          | 0E 3B 01…08 6E - 0: No error 01: Configuration invalid 02: Over current detected 03: Short circuit detected 04: Output ON error 05: Error in the other dual channel output 06: N/A 07: N/A 08: Dual channel violation 09: Short circuit detected at safety output |                                                      |                                                      |                                                      |

## Table 27 - Digital Safety Discrete Output Module - 1734-OBV2S

|                      |                                                                                           | Service Type Function Command (hex) Response (hex)       | Service Type Function Command (hex) Response (hex)                                                                                                                                                                                                                  | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   |
|----------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|                      |                                                                                           | Service Code Class ID Instance ID Attribute ID Data Size |                                                                                                                                                                                                                                                                     |                                                      |                                                      |                                                      |
| Get Attribute Single | Reads the cause for the safety digital output fault that the Instance ID (1…4) specifies. |                                                          | 0E 3B 01…04 6E - 0: No alarm 01: Configuration invalid 02: Over current detected 03: Short circuit detected 04: Output ON error 05: Error in the partner dual channel output 06: N/A 07: N/A 08: Dual channel violation 09: Short circuit detected at safety output |                                                      |                                                      |                                                      |

Use the information in the following tables to configure your message instruction.

Table 28 - Safety Analog Input Module (1734-IE4S)

|                      |                                                                                        | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   | (1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Service Type Function Command (hex) Response (hex)   | Service Type Function Command (hex) Response (hex)   |
|----------------------|----------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|                      |                                                                                        | Service Code                                         | Class ID Instance ID Attribute ID Data Size          | (1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                      |                                                      |
| Get Attribute Single | Reads the cause of the safety analog input fault that the Instance ID (1…4) specifies. |                                                      |                                                      | 0E 49 01…04 6 - 00: Reserved 01: No error 02: Signal overrange 03: Signal underrange 04: Signal test failure 05: Dual-channel discrepancy 06: Error in the other dual-channel input 08: Reserved 100: Sensor supply overcurrent 101: Sensor supply undercurrent 102: Analog-digital converter (ADC) CPU Timing Fault (2) 103: 3.3V undervoltage 104: 3.3V overvoltage 105: CPU fault 106: Flash fault 107: RAM fault 108: Single-channel discrepancy 109: Tach Dual Low 110: Undefined error 111: Flash enable fault 112: Serial pattern fault 113: Channel uniqueness fault 114: Watchdog fault 115: Sync timeout fault 116: Missing clock fault 117: SCI Tx fault 118: ADC fault 119: ADC neighbor 1.8V fault 120: ADC channel configuration mismatch 121: SPI sequence number mismatch 122: Runtime 3.3V over- or undervoltage error 123: Reserved 124: Reserved 125: Field I/O power is missing 126: Startup 3.3V over- or undervoltage error 127: Sensor power/input wiring error |                                                      |                                                      |
| Get Attribute Single | Reads the data that is associated with the given instance of the defined assembly      |                                                      | 0E 4 946 3 6(3)                                      | Input power                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                      |                                                      |

Table 29 - Fault Code Definitions for 1734-IE4S Modules

| Fault Code Description Definition Recommended Action                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2 Signal Over Range Exceeded configured range. Check field wiring and/or power.                                                                                                                                                               |
| 3 Signal Under Range Under configured range. Check field wiring and/or power.                                                                                                                                                                 |
| 4 Signal Test Failure Undefined error for IE4S.  If the problem persists, replace the module.                                                                                                                                                 |
| 5 Dual Channel Discrepancy Exceeded tolerance between dual channels. Check field sensors to determine the cause of discrepancy.                                                                                                               |
| 6 Error in other Dual Channel Input Partner channel faulted. Troubleshoot partner channel fault.                                                                                                                                              |
| 100 Sensor Supply Overcurrent Exceeded specification. Check field wiring and sensor power draw.                                                                                                                                               |
| 101 Sensor Undercurrent Too little current drawn from sensor power. Check field wiring and sensor power draw.                                                                                                                                 |
| 102 ADC CPU Timing Fault ADC missed a clock, failed a sync, or watchdog If the problem persists, replace the module.                                                                                                                          |
| 103 3.3V Undervoltage The supplied voltage is too low. If the problem persists, replace the module.                                                                                                                                           |
| 104 3.3V Overvoltage The supplied voltage is too high. If the problem persists, replace the module.                                                                                                                                           |
| 105 CPU Fault ADC failed register, instruction, or flag diagnostic. If the problem persists, replace the module.                                                                                                                              |
| 106 Flash Fault FLASH test detected bit errors. If the problem persists, replace the module.                                                                                                                                                  |
| 107 RAM fault RAM test detected bit errors. If the problem persists, replace the module.                                                                                                                                                      |
| 108 Single Channel Discrepancy Dual measurements of a single channel disagree. If the problem persists, replace the module.                                                                                                                   |
| 109 Tach Dual Low Both channels are LO at the same time. Check sensor signal timing.                                                                                                                                                          |
| 110 Undefined Error Undefined error. If the problem persists, replace the module.                                                                                                                                                             |
| 111 Flash Enable Fault ADC's nonvolatile memory is drawing too much current If the problem persists, replace the module.                                                                                                                      |
| 112 Serial Pattern Fault Serial communication pattern errors are detected. Check field wiring for proper grounding/shielding. Verify that the temperature within the enclosure is not excessive. If the problem persists, replace the module. |
| 113 Channel Uniqueness Fault Pulse test of an ADC multiplexor revealed an improper If the problem persists, replace the module.                                                                                                               |
| 114 Watchdog Fault ADC watchdog timed out. If the problem persists, replace the module.                                                                                                                                                       |
| 115 Sync Timeout Fault ADC conversion is out of sync. If the problem persists, replace the module.                                                                                                                                            |
| 116 Missing Clock fault ADC detected a missing clock. If the problem persists, replace the module.                                                                                                                                            |
| 117 SCI Tx fault Serial communication bit errors are detected. Check field wiring for proper grounding/shielding. Verify that the temperature within the enclosure is not excessive. If the problem persists, replace the module.             |
| 118 ADC fault ADC test pattern failure. If the problem persists, replace the module.                                                                                                                                                          |
| 119 ADC neighbor 1.8V fault ADC detected an out-of-range voltage on its partner. If the problem persists, replace the module.                                                                                                                 |
| 120 ADC channel config mismatch Dual ADCs are not configured the same. If the problem persists, replace the module.                                                                                                                           |
| 121 SPI sequence number mismatch Serial communication state machines are out of sync. If the problem persists, replace the module.                                                                                                            |
| 122 Runtime 3.3V over/under error The supplied voltage too high or too low. If the problem persists, replace the module.                                                                                                                      |
| 125 Field I/O power is missing 24V power is not within the specification. Check field power supply and wiring.                                                                                                                                |
| 126 Startup 3.3V over/under error OV-UV detector failed startup test. If the problem persists, replace the module.                                                                                                                            |
| 127 Sensor power/input wiring error Sensor power to input signal violation detected. Check field wiring.                                                                                                                                      |

## Notes:

## Safety Data

This appendix lists calculated values for probability of a dangerous failure (PFD), average frequency of a dangerous failure per hour (PFH), and mean time to failure (MTTF). PFD and PFH calculations comply with IEC61508, edition 2, 2010.

Calculated values of PFD and PFH appear in the table. Both must be calculated for the devices within the system to comply with the SIL level that is required for application.

To assess Performance Levels in their safety system, you must be responsible for following the requirements of ISO 13849-1:2008.

You must functionally test every I/O module by individually toggling each input point and also verify that the controller detects it within the safety reaction time.

Additionally, you must individually toggle each output point by the controller and user-verified that the output point changes state.

For more information, see these publications.

|                                                                                    | Resource Description                                                                                                              |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| GuardLogix 5570 Controller Systems Safety Reference Manual, publication 1756-RM099 | Provides information on safety application requirements for GuardLogix® 5570 controllers in Studio 5000 Logix Designer® projects. |
| GuardLogix Controller Systems Safety Reference Manual, publication 1756-RM093      | Provides information on safety application requirements for GuardLogix 5560 and 5570 controllers in RSLogix 5000® projects.       |

<!-- image -->

## Series A Safety Data

Figure 53 PFD vs. Proof Test Interval 1734-IB8S Series A

<!-- image -->

Figure 54 - PFD vs. Proof Test Interval 1734-OB8S Series A

<!-- image -->

Figure 55 - PFD vs. Proof Test Interval 1734-IE4S Series A Single Channel

<!-- image -->

Figure 56 - PFD vs. Proof Test Interval 1734-IE4S Series A Dual Channel

<!-- image -->

Table 30 - Series A Proof vs. PFD Data

| Cat. No. Proof Test Interval      | PFD PFH                                   | (1/hour)   | Spurious Trip Rate () (STR)  (1)                                          | MTTF spurious (2) (years)   |
|-----------------------------------|-------------------------------------------|------------|------------------------------------------|-----------------------------|
| 1734-IB8S Series A                | PFD PFH                                   | (1/hour)   | 1 8760 2.11E-06 5.10E-10 2.666E-06 42.78 | MTTF spurious (2) (years)   |
| 1734-IB8S Series A                | 2 17520 4.23E-06                          |            | 1 8760 2.11E-06 5.10E-10 2.666E-06 42.78 |                             |
| 1734-IB8S Series A                | 5 43800 1.06E-05                          |            | 1 8760 2.11E-06 5.10E-10 2.666E-06 42.78 |                             |
| 1734-IB8S Series A                | 10 87600 2.11E-05                         |            | 1 8760 2.11E-06 5.10E-10 2.666E-06 42.78 |                             |
| 1734-IB8S Series A                | 20 175200 4.23E-05                        |            | 1 8760 2.11E-06 5.10E-10 2.666E-06 42.78 |                             |
| 1734-OB8S Series A                | 1 8760 2.13E-06 5.14E-10 3.229E-06 35.33  |            |                                          |                             |
| 1734-OB8S Series A                | 2 17520 4.27E-06                          |            |                                          |                             |
| 1734-OB8S Series A                | 5 43800 1.07E-05                          |            |                                          |                             |
| 1734-OB8S Series A                | 10 87600 2.13E-05                         |            |                                          |                             |
| 1734-OB8S Series A                | 20 175200 4.27E-05                        |            |                                          |                             |
| 1734-IE4S Series A Single Channel | 1 8760 2.30E-07 5.30E-11 9.402E-07 121.42 |            |                                          |                             |
| 1734-IE4S Series A Single Channel | 2 17520 4.70E-07                          |            |                                          |                             |
| 1734-IE4S Series A Single Channel | 5 43800 1.20E-06 5.40E-11                 |            |                                          |                             |
| 1734-IE4S Series A Single Channel | 10 87600 2.40E-06 5.50E-11                |            |                                          |                             |
| 1734-IE4S Series A Single Channel | 20 175200 4.80E-06 5.60E-11               |            |                                          |                             |
| 1734-IE4S Series A Dual Channel   | 1 8760 1.60E-07 3.70E-11 9.402E-07 121.42 |            |                                          |                             |
| 1734-IE4S Series A Dual Channel   | 2 17520 3.20E-07                          |            |                                          |                             |
| 1734-IE4S Series A Dual Channel   | 5 43800 8.10E-07                          |            |                                          |                             |
| 1734-IE4S Series A Dual Channel   | 10 87600 1.60E-06 3.80E-11                |            |                                          |                             |
| 1734-IE4S Series A Dual Channel   | 20 175200 3.30E-06 3.90E-11               |            |                                          |                             |

(1) Calculated based on the ISA TR-84 method.

(2) Mean time to failure (Spurious).

Mission Time for all modules is 20 years.

When you use the 1734-IB8S module or the 1734-OB8S module in Functional Safety applications, to increase the diagnostic coverage you can enable pulse testing, which allows the modules to detect more faults.

The safety Category, Performance Level, or SIL level requirements determine the level of diagnostic coverage that is required. For example, to provide more diagnostic coverage in a Category 4 system with simple devices, pulse testing is typically required.

## Series B Safety Data

Figure 57 - PFD vs. Proof Test Interval 1734-IB8S Series B Single Channel

<!-- image -->

Figure 58 - PFD vs. Proof Test Interval 1734-OB8S Series B Single Channel (1)

<!-- image -->

Figure 59 - PFD vs. Proof Test Interval 1734-IB8S Series B Dual Channel

<!-- image -->

(1) 1734-OB8S single channel mode is only certified for functional safety applications with Process Safety Times ≥ 600 msec OR with Demand Rates ≤ 1 Demand per Minute.

Figure 60 - PFD vs. Proof Test Interval 1734-OB8S Series B Dual Channel

<!-- image -->

Figure 61 - PFD vs. Proof Test Interval 1734-OBV2S Series B Dual Channel

<!-- image -->

Table 31 - Series B PFD vs. Proof Test Data

| Catalog Number                       | PFD PFH (1/hour) Spurious Trip ()                                          | MTTF spurious () (years) p (3)   |
|--------------------------------------|------------------------------------------|---|
| 1734-IB8S Series B Single Channel    | 1 8760 2.42E-06 5.61E-10 2.709E-06 42.14 | MTTF spurious () (years) p (3)   |
| 1734-IB8S Series B Single Channel    | 2 17520 4.85E-06                         |   |
| 1734-IB8S Series B Single Channel    | 5 43800 1.21-05                          |   |
| 1734-IB8S Series B Single Channel    | 10 87600 2.43E-05                        |   |
| 1734-IB8S Series B Single Channel    | 20 175200 4.89E-05                       |   |
| 1734-OB8S Series B(1) Single Channel | 1 8760 2.02E-05 4.62E-09 3.243E-06 35.20 |   |
| 1734-OB8S Series B(1) Single Channel | 2 17520 4.04E-05                         |   |
| 1734-OB8S Series B(1) Single Channel | 5 43800 1.01E-04                         |   |
| 1734-OB8S Series B(1) Single Channel | 10 87600 2.02E-04                        |   |
| 1734-OB8S Series B(1) Single Channel | 20 175200 4.04E-04                       |   |
| 1734-IB8S Series B Dual Channel      | 1 8760 4.89E-07 1.20E-10 2.709E-06 42.14 |   |
| 1734-IB8S Series B Dual Channel      | 2 17520 9.80E-07                         |   |
| 1734-IB8S Series B Dual Channel      | 5 43800 2.47E-06                         |   |
| 1734-IB8S Series B Dual Channel      | 10 87600 5.00E-06                        |   |
| 1734-IB8S Series B Dual Channel      | 20 175200 1.02E-05                       |   |
| 1734-0B8S Series B Dual Channel      | 1 8760 4.89E-07 1.20E-10 3.243E-06 35.20 |   |
| 1734-0B8S Series B Dual Channel      | 2 17520 9.81E-07                         |   |
| 1734-0B8S Series B Dual Channel      | 5 43800 2.47E-06                         |   |
| 1734-0B8S Series B Dual Channel      | 10 87600 5.00E-06                        |   |
| 1734-0B8S Series B Dual Channel      | 20 175200 1.02E-05                       |   |
| 1734-OBV2S Series B Dual Channel     | 1 8760 6.45E-07 1.64E-10 2.969E-06 38.45 |   |
| 1734-OBV2S Series B Dual Channel     | 2 17520 1.29E-06                         |   |
| 1734-OBV2S Series B Dual Channel     | 5 43800 3.26E-06                         |   |
| 1734-OBV2S Series B Dual Channel     | 10 87600 6.63E-06                        |   |
| 1734-OBV2S Series B Dual Channel     | 20 175200 1.37E-05                       |   |

Mission Time for all modules is 20 years.

When you use the 1734-IB8S module, the 1734-OB8S module, or the 1734-OBV2S module in Functional Safety applications, to increase the diagnostic coverage you can enable pulse testing, which allows the modules to detect more faults.

The safety Category, Performance Level, or SIL level requirements determine the level of diagnostic coverage that is required. For example, to provide more diagnostic coverage in a Category 4 system with simple devices, pulse testing is typically required.

## Product Failure Rates

Table 32 - Product Failure Rates (failures per hour) (1)

| Catalog Number Series Module I/O   | Configuration λ DD                                           | λ S         | λ DU        |
|------------------------------------|--------------------------------------------------------------|-------------|-------------|
|                                    | 1734-IB8S B Single Channel Inputs 2.56E-07 2.55E-07 6.02E-10 |             |             |
|                                    | 1734-OB8S B Single Channel Outputs (2) 2.52E-07(2)           | 2.52E-07(2) | 4.47E-09(2) |
|                                    | 1734-IE4S A Single Channel Inputs 4.23E-07 4.23E-07 1.01E-10 |             |             |
|                                    | 1734-IB8S B Dual Channel Inputs 2.96E-07 2.94E-07 1.84E-10   |             |             |
|                                    | 1734-OB8S B Dual Channel Outputs 2.95E-07 2.95E-07 1.84E-10  |             |             |
|                                    | 1734-OBV2S B Dual Channel Outputs 4.08E-07 4.08E-07 2.41E-10 |             |             |
|                                    | 1734-IE4S A Dual Channel Inputs 6.56E-07 6.56E-07 6.67E-11   |             |             |

(1) These failure rates assume that one block represents the module in a reliability block diagram. The single channel rates must be applied to the reliability block if the module is configured in Single Channel mode. The dual channel rates must be applied to the reliability block if the module is configured in Dual Channel mode.

(2) 1734-OB8S single channel mode is only certified for functional safety applications with Process Safety Times ≥ 600 msec or with Demand Rates ≤ 1 Demand per Minute.

When you use the 1734-IB8S module, the 1734-OB8S module, or the 1734-OBV2S module in Functional Safety applications, to increase the diagnostic coverage you can enable pulse testing, which allows the modules to detect more faults.

The safety Category, Performance Level, or SIL level requirements determine the level of diagnostic coverage that is required. For example, to provide more diagnostic coverage in a Category 4 system with simple devices, pulse testing is typically required.

## Notes:

Table 33 - Safety Digital Input Parameters

| Parameter Name(1)                                                    |                                  | Value Description Default                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x Input Delay Time Off -> On                                         | 0…126 ms (in increments of 6 ms) | Filter time for OFF to ON transition.                                                                                                                                                                                                                                 |
| x Input Delay Time On -> Off                                         | 0…126 ms (in increments of 6 ms) | Filter time for ON to OFF transition.                                                                                                                                                                                                                                 |
|                                                                      |                                  | x Input Point Mode Not Used External input device is not connected.                                                                                                                                                                                                   |
|                                                                      |                                  | Safety Pulse Test Use with a contact output device and in combination with a test output. With the use of this setting, short-circuits between input signal lines and the power supply (positive side) and short-circuits between input signal lines can be detected. |
|                                                                      |                                  | Safety A solid-state output safety sensor is connected.                                                                                                                                                                                                               |
|                                                                      |                                  | Standard A standard device, such as a reset switch, is connected.                                                                                                                                                                                                     |
|                                                                      |                                  | x Safety Input Test Source Not Used The test output that is used with the input.                                                                                                                                                                                      |
|                                                                      | Test Output 0                    |                                                                                                                                                                                                                                                                       |
|                                                                      | Test Output 1                    |                                                                                                                                                                                                                                                                       |
|                                                                      | Test Output 2                    |                                                                                                                                                                                                                                                                       |
|                                                                      | Test Output 3                    |                                                                                                                                                                                                                                                                       |
| x Input Point Operation Type Single Channel Use as a single channel. |                                  |                                                                                                                                                                                                                                                                       |
|                                                                      |                                  | Dual-channel Equivalent Use as dual-channel. Normal when both channels are ON or OFF.                                                                                                                                                                                 |
|                                                                      |                                  | Dual-channel Complementary Use as dual-channel. Normal when one channel is ON and the other channel is OFF.                                                                                                                                                           |
| x Safety Input Error Latch Time 0…65,530 ms                          | (in increments of 10 ms)         | Safety input or test output errors are latched for this time. 1000 ms                                                                                                                                                                                                 |

## Configuration Parameters

| Topic Page                                    |
|-----------------------------------------------|
| Table 33 Safety Digital Input Parameters 165  |
| Table 34 Test Output Parameters 166           |
| Table 35 Safety Digital Output Parameters 166 |
| Table 36 Safety Analog Input Parameters 166   |

This appendix lists parameters that can be configured via the Studio 5000 Logix Designer application.

<!-- image -->

## Table 34 - Test Output Parameters

| Parameter Name(1)   | Value Description Default                                                                                                                                |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     | x Test Output Mode Not Used An external device is not connected. Not Used                                                                                |
|                     | Standard The output is connected to a standard device.                                                                                                   |
|                     | Pulse Test A contact output device is connected. Use in combination with a safety input.                                                                 |
|                     | Power Supply The power supply of a Safety Sensor is connected. The voltage that is supplied to I/O power (V, G) is output from the test output terminal. |
|                     | Muting Lamp Output (Terminal T1 or T3 only) An indicator is connected and turned ON to detect broken lines in an external indicator.                     |
|                     | Test Output Fault Action Clear OFF Action to perform when a communication error is detected. Clear OFF                                                   |
|                     | Test Output Fault Action Clear OFF Action to perform when a communication error is detected. Clear OFF                                                   |

## Table 35 - Safety Digital Output Parameters

| Parameter Name(1)                                                                  | Value Description Default                                                                                                                                                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                    | x Output Point Mode Not Used An external output device is not connected. Not Used                                                                                                            |
|                                                                                    | Safety When the output is ON, the test pulse is not output (remains ON).                                                                                                                     |
|                                                                                    | Safety Pulse Test With use of this function, short-circuits between output signal lines and the power supply (positive side) and short-circuits between output signal lines can be detected. |
| x Output Point Operation Type Single Channel Use as a single channel. Dual-channel |                                                                                                                                                                                              |
| x Output Point Operation Type Single Channel Use as a single channel. Dual-channel | Dual-channel Use as dual-channel. When both channels are normal, outputs can be turned ON.                                                                                                   |
| x Safety Output Error Latch Time                                                   | 0…65,530 ms (in increments of 10 ms) Safety output errors are latched for this time. 1000 ms                                                                                                 |

| Parameter Name Value Description Default   |                                                                                        |
|--------------------------------------------|----------------------------------------------------------------------------------------|
| Test Output Idle State (1)                 | Clear OFF or Keep Output Data Definition of output data is in an idle state. Clear OFF |

## Table 36 - Safety Analog Input Parameters

| Parameter Name(1)   | Parameter Name(1)   | Value Description Default                                           |          |
|---------------------|---------------------|---------------------------------------------------------------------|----------|
|                     |                     | x Input Point Mode Not Used External input device is not connected. | Not Used |
|                     |                     | Safety A solid-state safety sensor is connected.                    | Not Used |
|                     |                     | Standard A device that is not used in the safety loop is connected. | Not Used |
|                     | Range ±10V          | Input voltage range.                                                | 4…20 mA  |
|                     | 0…5V                | Input voltage range.                                                | 4…20 mA  |
|                     | 0…10V               | Input voltage range.                                                | 4…20 mA  |
|                     | ±5V                 | Input voltage range.                                                | 4…20 mA  |
|                     | 4…20 mA             | Input current range.                                                | 4…20 mA  |
|                     | 0…20 mA             | Input current range.                                                | 4…20 mA  |
|                     |                     | Tachometer Tachometer mode.                                         | 4…20 mA  |

Table 36 - Safety Analog Input Parameters (Continued)

| Parameter Name(1)  Value Description Default                                                                                                                                                                                              |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| x Input Point Operation Type Single channel Use as a single channel.                                                                                                                                                                      |        |
| Single Dual channel Use as a dual-channel equivalent. This setting must be used only with SmartGuard™ controllers.                                                                                                                        |        |
| Filter 1 Hz Input filter                                                                                                                                                                                                                  | 1 Hz   |
| x Safety Input Error Latch Time 0…65,530 ms (in 10 ms increments) Safety input errors are latched for this time so that the controller can them and they are not missed if they clear themselves too quickly. One value for all channels. | 1000   |
| Low Engineering -30000…+30000 Scaling value for inputs 0                                                                                                                                                                                  | 1 Hz   |
| High Engineering -30000…+30000 Scaling value for inputs 10,000                                                                                                                                                                            | (2)    |
| x Tachometer Dual Low Diagnostic ON/OFF Diagnostic that indicates if both channels are low. Channels 0 and 1 share value and channels 2 and 3 share value.                                                                                | Off    |
| Tachometer Trigger Falling edge (NPN) Non-inverted input signal. Falling edge                                                                                                                                                             |        |
| Rising edge (PNP) Inverted input signal.                                                                                                                                                                                                  |        |
| Tachometer Off Level 0…23V Off-level for the Tachometer mode input signal. 5V                                                                                                                                                             |        |
| Tachometer On Level 1…24V On-level for the Tachometer mode input signal. 11V                                                                                                                                                              |        |
| Sensor Power Mode External Sensors are getting their power from a separate power supply. Module                                                                                                                                           |        |
| x Module Sensors are getting their power from the module (recommended).                                                                                                                                                                   |        |
| Alarm Enable Disable Enable or disable alarms. We recommend disabling this feature when using the module in a GuardLogix® system (evaluate alarms with the use of the application program). Enable this feature when using the module in a SmartGuard system. We recommend disabling this feature when using the module in a GuardLogix system (evaluate alarms with the use of the application program)Enable this Disable Enable                                                                                                                                                                                                                                           |        |
| High High Alarm Level -32768…+32767 High High alarm trip point. 32767                                                                                                                                                                     |        |
| Low Low Alarm Level -32768…+32767 Low Low alarm trip point. -32767                                                                                                                                                                        |        |
| High High - Low Low 0…32767 Deadband on the High High and Low Low alarms. 0                                                                                                                                                               |        |
| High Alarm -32768…+32767 High alarm trip point. 332767                                                                                                                                                                                    |        |
| Low Alarm -32768…+32767 Low alarm trip point. 0                                                                                                                                                                                           |        |
| High - Low deadband 0…32767 Deadband on the High and Low alarms. 0                                                                                                                                                                        |        |
| x Discrepancy Time 0…65,530 (in 10 ms increments) The time period during which the channel values can be discrepant before an error is reported.                                                                                          | 100 ms |
| x Discrepancy deadband 0…32767 Tolerance range between channels in dual-channel mode (in engineering units) 0                                                                                                                             |        |
| x Channel Offset -32768…+32767 Offset value for dual channel mode only (in engineering units). 0                                                                                                                                          |        |

## Notes:

## Input Assemblies

Table 37 - 1734-IB8S Input Assemblies

| Instance Decimal Connection Type       | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                  |                                                  |                                                                                                                           |                                                  |                                                                                           |                                                  |                       |
|----------------------------------------|--------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------|-----------------------|
| 516 (204 h) Safety and Standard        | 0 Safety Input 7                                       | Safety Input 6                                   |                                                  | Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0                                 |                                                  |                                                                                           |                                                  |                       |
| 548 (224 h) Safety Only 0 Safety Input | 7                                                      | Safety Input 6                                   |                                                  | Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0                                 |                                                  |                                                                                           |                                                  |                       |
| 548 (224 h) Safety Only 0 Safety Input | 1 Safety Input 7 Status                                | Safety Input 6 Status                            | Safety Input 5 Status                            | Safety Input 4 Status                                                                                                     | Safety Input 3 Status                            | Safety Input 2 Status                                                                     | Safety Input 1 Status                            | Safety Input 0 Status |
|                                        | 768 (300 h) Standard Only 0 Reserved Input Power       | 768 (300 h) Standard Only 0 Reserved Input Power | 768 (300 h) Standard Only 0 Reserved Input Power | 768 (300 h) Standard Only 0 Reserved Input Power                                                                          | 768 (300 h) Standard Only 0 Reserved Input Power | 768 (300 h) Standard Only 0 Reserved Input Power                                          | 768 (300 h) Standard Only 0 Reserved Input Power | Error                 |
| 788 (314 h) Safety and Standard        | 0 Safety Input 7                                       | Safety Input 6                                   |                                                  | Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0                                 |                                                  |                                                                                           |                                                  |                       |
| 788 (314 h) Safety and Standard        | 1 Combined Safety Input Status                         |                                                  | Reserved Input Power (1)  p Error(1)                                                  |                                                                                                                           |                                                  |                                                                                           | Reserved Reserved Reserved Muting Lamp 3 Status  | Muting Lamp 1 Status  |
| 820 (334 h) Safety and Standard        | 0 Safety Input 7                                       | Safety Input 6                                   |                                                  |                                                                                                                           |                                                  | Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                                                  |                       |
| 820 (334 h) Safety and Standard        | 1 Safety Input 7 Status                                | Safety Input 6 Status                            | Safety Input 5 Status                            | Safety Input 4 Status                                                                                                     | Safety Input 3 Status                            | Safety Input 2 Status                                                                     | Safety Input 1 Status                            | Safety Input 0 Status |
| 820 (334 h) Safety and Standard        | 2 Reserved Input Power (1)                                                        | 2 Reserved Input Power (1)                                                  | p Error(1)                                                  | Reserved Muting Lamp 3                                                                                                    | Reserved Muting Lamp 3                           | Reserved Muting Lamp 3                                                                    | Status                                           | Muting Lamp 1 Status  |
| 868 (364 h) Safety and Standard        |                                                        |                                                  |                                                  | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                                                  |                                                                                           |                                                  |                       |
| 868 (364 h) Safety and Standard        | 1 Safety Input 7 Status                                | Safety Input 6 Status                            | Safety Input 5 Status                            | Safety Input 4 Status                                                                                                     | Safety Input 3 Status                            | Safety Input 2 Status                                                                     | Safety Input 1 Status                            | Safety Input 0 Status |
| 868 (364 h) Safety and Standard        | 2 Reserved Test Output 3                               | 2 Reserved Test Output 3                         | 2 Reserved Test Output 3                         | 2 Reserved Test Output 3                                                                                                  | Status                                           | Test Output 2 Status                                                                      | Test Output 1 Status                             | Test Output 0 Status  |
| 868 (364 h) Safety and Standard        | 3 Reserved Input Power (1)                                                        | 3 Reserved Input Power (1)                                                  | p Error(1)                                                  |                                                                                                                           |                                                  | Reserved Muting Lamp 3                                                                    | Status                                           | Muting Lamp 1 Status  |
|                                        | 899 (383 h) Standard 0 Reserved Input Power            | 899 (383 h) Standard 0 Reserved Input Power      | 899 (383 h) Standard 0 Reserved Input Power      | 899 (383 h) Standard 0 Reserved Input Power                                                                               | 899 (383 h) Standard 0 Reserved Input Power      | 899 (383 h) Standard 0 Reserved Input Power                                               | 899 (383 h) Standard 0 Reserved Input Power      | Error                 |
|                                        | 1 Reserved Test Output 3                               | 1 Reserved Test Output 3                         | 1 Reserved Test Output 3                         | 1 Reserved Test Output 3                                                                                                  | Status                                           | Test Output 2 Status                                                                      | Test Output 1 Status                             | Test Output 0 Status  |

## I/O Assemblies

| Topic Page                                                   |
|--------------------------------------------------------------|
| Input Assemblies 169                                         |
| Output Assemblies 171                                        |
| Analog Input Assemblies 171                                  |
| Configuration Assemblies 173                                 |
| Use Data from Modules Configured Via the Generic Profile 179 |

<!-- image -->

Table 38 - 1734-OB8S Input Assemblies

| Instance Decimal (hex)   | Connection Type                 |                           |                                   |                         |                         |                         | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                         |                         |
|--------------------------|---------------------------------|---------------------------|-----------------------------------|-------------------------|-------------------------|-------------------------|--------------------------------------------------------|-------------------------|-------------------------|
|                          | 580 (244 h) Safety and Standard | 0 Safety Output 7 Status  | Safety Output 6 Status            | Safety Output 5 Status  | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                 | Safety Output 1 Status  | Safety Output 0 Status  |
| 1028 (404 h) Safety and  | Standard                        | 0 Safety Output 7 Status  | Safety Output 6 Status            | Safety Output 5 Status  | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                 | Safety Output 1 Status  | Safety Output 0 Status  |
| 1028 (404 h) Safety and  | Standard                        | 1 Safety Output Monitor 7 | Safety Output Monitor 6           | Safety Output Monitor 5 | Safety Output Monitor 4 | Safety Output Monitor 3 | Safety Output Monitor 2                                | Safety Output Monitor 1 | Safety Output Monitor 0 |
| 1044 (414 h) Safety and  | Standard                        | 0 Safety Output Monitor 7 | Safety Output Monitor 6           | Safety Output Monitor 5 | Safety Output Monitor 4 | Safety Output Monitor 3 | Safety Output Monitor 2                                | Safety Output Monitor 1 | Safety Output Monitor 0 |
| 1044 (414 h) Safety and  | Standard                        |                           | 1 Reserved Combined Output Status |                         | Reserved Output Power (1) p Error(1)                         | Reserved                | Reserved                                               | Reserved                | Reserved                |

Table 39 - 1734-OBV2S Input Assemblies

| Instance Decimal (hex)   | Connection Type   |                                                     | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                                                 |                          |                          |                          |
|--------------------------|-------------------|-----------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------|--------------------------|--------------------------|
|                          |                   |                                                     |                                                        | 579 (243 h) Safety 0 Reserved Reserved Reserved Reserved Safety Output 3 Status | Safety Output 2 Status   | Safety Output 1 Status   | Safety Output 0 Status   |
| 1027 (403 h) Safety and  | Standard          | 0 Safety Output 3 Readback Safety Output 2 Readback | Safety Output 1 Readback Safety Output 0 Readback      | Safety Output 3 Status                                                          | Safety Output 2 Status   | Safety Output 1 Status   | Safety Output 0 Status   |
| 1043 (413 h) Safety and  | Standard          |                                                     |                                                        | 0 Reserved Reserved Reserved Reserved Safety Output 3 Readback                  | Safety Output 2 Readback | Safety Output 1 Readback | Safety Output 0 Readback |
| 1043 (413 h) Safety and  |                   | 1 Reserved Combined Output Status                   | Reserved Output Power (1) p Error(1)                                                        | Reserved                                                                        | Reserved                 | Reserved                 | Reserved                 |

## Output Assemblies

Table 40 - Output Assemblies for all POINT Guard I/O™ Modules

| Instance Decimal (hex)     | Module Connection Type                                                          | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                 |                 |                 |                   |                   |                   |                   |
|----------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------|-----------------|-----------------|-----------------|-------------------|-------------------|-------------------|-------------------|
| 33 (21 h) 1734-IB8S Safety | (1)  0                                                                          | Reserved                                               | Reserved        | Reserved        | Reserved        | Standard Output 3 | Standard Output 2 | Standard Output 1 | Standard Output 0 |
|                            | 564 (234 h) 1734-OB8S Safety Only 0 Safety                                      | Output 7                                               | Safety Output 6 | Safety Output 5 | Safety Output 4 | Safety Output 3   | Safety Output 2   | Safety Output 1   | Safety Output 0   |
|                            | 563 (233 h) 1734-OBV2S Safety Only 0 Reserved Reserved Reserved Reserved Safety |                                                        |                 |                 |                 | Output 3          | Safety Output 2   | Safety Output 1   | Safety Output 0   |
| 770 (302 h) 1734-IE4S Safety 0 Reserved Reserved Reserved Reserved Reset Tach (2)                            |                                                                                 |                                                        |                 |                 |                 | 3 (2)                   | Reset Tach 2 (2)                   | Reset Tach 1 (2)                   | Reset Tach 0 (2)                   |

## Analog Input Assemblies

## Table 41 - 1734-IE4S Input Assemblies

| Instance Decimal (hex)   | Connection Type     |             |                              |                                                  |                          | Byte High Byte Low Byte                                 | Byte High Byte Low Byte   | Byte High Byte Low Byte                         | Byte High Byte Low Byte   |             |
|--------------------------|---------------------|-------------|------------------------------|--------------------------------------------------|--------------------------|---------------------------------------------------------|---------------------------|-------------------------------------------------|---------------------------|-------------|
| 402 (192 h)              | Safety and Standard |             |                              |                                                  |                          | 0, 1 Input 0 Input 0                                    | 0, 1 Input 0 Input 0      | 0, 1 Input 0 Input 0                            | 0, 1 Input 0 Input 0      |             |
| 402 (192 h)              | Safety and Standard |             |                              |                                                  |                          | 2, 3 Input 1 Input 1                                    | 2, 3 Input 1 Input 1      | 2, 3 Input 1 Input 1                            | 2, 3 Input 1 Input 1      |             |
| 402 (192 h)              | Safety and Standard |             |                              |                                                  |                          | 4, 5 Input 2 Input 2                                    | 4, 5 Input 2 Input 2      | 4, 5 Input 2 Input 2                            | 4, 5 Input 2 Input 2      |             |
| 402 (192 h)              | Safety and Standard |             |                              |                                                  |                          | 6, 7 Input 3 Input 3                                    | 6, 7 Input 3 Input 3      | 6, 7 Input 3 Input 3                            | 6, 7 Input 3 Input 3      |             |
| 402 (192 h)              | Safety and Standard |             |                              |                                                  |                          | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0         |                           |                                                 |                           |             |
| 402 (192 h)              | Safety and Standard |             |                              | 8 Reserved Reserved Reserved Reserved Ch 3 Input |                          | Status                                                  | Ch 2 Input Status         | Ch 1 Input Status                               | Ch 0 Input Status         |             |
| Instance Decimal (hex)   | Connection Type     |             |                              |                                                  |                          | Byte High Byte Low Byte                                 | Byte High Byte Low Byte   | Byte High Byte Low Byte                         | Byte High Byte Low Byte   |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          | 0, 1 Input 0 Input 0                                    | 0, 1 Input 0 Input 0      | 0, 1 Input 0 Input 0                            | 0, 1 Input 0 Input 0      |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          | 2, 3 Input 1 Input 1                                    | 2, 3 Input 1 Input 1      | 2, 3 Input 1 Input 1                            | 2, 3 Input 1 Input 1      |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          | 4, 5 Input 2 Input 2                                    | 4, 5 Input 2 Input 2      | 4, 5 Input 2 Input 2                            | 4, 5 Input 2 Input 2      |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          | 6, 7 Input 3 Input 3                                    | 6, 7 Input 3 Input 3      | 6, 7 Input 3 Input 3                            | 6, 7 Input 3 Input 3      |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          |                                                         |                           | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                           |             |
| 786 (312 h)              | Safety and          |             |                              |                                                  |                          | 8 Reserved Reserved Reserved Reserved Ch 3 Input Status | Ch 2 Input Status         | Ch 1 Input Status                               | Ch 0 Input Status         |             |
| 786 (312 h)              | Safety and          | Alarms 0(1) | Alarms 0(1)                  | Alarms 0(1)                                      | Alarms 0(1)              | Alarms 0(1)                                             | Alarms 0(1)               | Alarms 0(1)                                     | Alarms 0(1)               | Alarms 0(1) |
| 786 (312 h)              | Standard            | 9           | Reserved Tachometer Dual Low | Tachometer Underfrequency                        | Tachometer Overfrequency | Low Alarm Status                                        | High Alarm Status         | Low Low Alarm Status                            | High High Alarm Status    |             |
| 786 (312 h)              | Safety and          | Alarms 1(1) | Alarms 1(1)                  | Alarms 1(1)                                      | Alarms 1(1)              | Alarms 1(1)                                             | Alarms 1(1)               | Alarms 1(1)                                     | Alarms 1(1)               | Alarms 1(1) |
| 786 (312 h)              | Safety and          | 10          | Reserved Tachometer Dual Low | Tachometer Underfrequency                        | Tachometer Overfrequency | Low Alarm Status                                        | High Alarm Status         | Low Low Alarm Status                            | High High Alarm Status    |             |
| 786 (312 h)              | Safety and          | Alarms 2(1) | Alarms 2(1)                  | Alarms 2(1)                                      | Alarms 2(1)              | Alarms 2(1)                                             | Alarms 2(1)               | Alarms 2(1)                                     | Alarms 2(1)               | Alarms 2(1) |
| 786 (312 h)              | Safety and          | 11          | Reserved Tachometer Dual Low | Tachometer Underfrequency                        | Tachometer Overfrequency | Low Alarm Status                                        | High Alarm Status         | Low Low Alarm Status                            | High High Alarm Status    |             |
| 786 (312 h)              | Safety and          | Alarms 3(1) | Alarms 3(1)                  | Alarms 3(1)                                      | Alarms 3(1)              | Alarms 3(1)                                             | Alarms 3(1)               | Alarms 3(1)                                     | Alarms 3(1)               | Alarms 3(1) |
| 786 (312 h)              | Safety and          | 12          | Reserved Tachometer Dual Low | Tachometer Underfrequency                        | Tachometer Overfrequency | Low Alarm Status                                        | High Alarm Status         | Low Low Alarm Status                            | High High Alarm Status    |             |
| Instance Decimal (hex)   | Connection Type     |             |                              |                                                  |                          | Byte High Byte Low Byte                                 | Byte High Byte Low Byte   | Byte High Byte Low Byte                         | Byte High Byte Low Byte   |             |

Table 41 - 1734-IE4S Input Assemblies (Continued)

|                        |                     | 0, 1 Input 0 Input 0                                 | 0, 1 Input 0 Input 0         | 0, 1 Input 0 Input 0                                                          | 0, 1 Input 0 Input 0       |                   |                   |                                                 |                                                      |
|------------------------|---------------------|------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------|----------------------------|-------------------|-------------------|-------------------------------------------------|------------------------------------------------------|
|                        |                     | 2, 3 Input 1 Input 1                                 | 2, 3 Input 1 Input 1         | 2, 3 Input 1 Input 1                                                          | 2, 3 Input 1 Input 1       |                   |                   |                                                 |                                                      |
|                        |                     | 4, 5 Input 2 Input 2                                 | 4, 5 Input 2 Input 2         | 4, 5 Input 2 Input 2                                                          | 4, 5 Input 2 Input 2       |                   |                   |                                                 |                                                      |
|                        |                     | 6, 7 Input 3 Input 3                                 | 6, 7 Input 3 Input 3         | 6, 7 Input 3 Input 3                                                          | 6, 7 Input 3 Input 3       |                   |                   |                                                 |                                                      |
|                        |                     |                                                      |                              |                                                                               |                            |                   |                   | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                                                      |
|                        |                     | 8 Ch 3 Combined Alarm Status                         | Ch 2 Combined Alarm Status   | Ch 1 Combined Alarm Status                                                    | Ch 0 Combined Alarm Status | Ch 3 Input Status | Ch 2 Input Status | Ch 1 Input Status                               | Ch 0 Input Status                                    |
|                        |                     | 9 Fault Reason 0                                     | 9 Fault Reason 0             | 9 Fault Reason 0                                                              | 9 Fault Reason 0           | 9 Fault Reason 0  | 9 Fault Reason 0  | 9 Fault Reason 0                                | 9 Fault Reason 0                                     |
|                        |                     | 10 Fault Reason 1                                    | 10 Fault Reason 1            | 10 Fault Reason 1                                                             | 10 Fault Reason 1          | 10 Fault Reason 1 | 10 Fault Reason 1 | 10 Fault Reason 1                               | 10 Fault Reason 1                                    |
|                        |                     | 11 Fault Reason 2                                    | 11 Fault Reason 2            | 11 Fault Reason 2                                                             | 11 Fault Reason 2          | 11 Fault Reason 2 | 11 Fault Reason 2 | 11 Fault Reason 2                               | 11 Fault Reason 2                                    |
|                        |                     | 12 Fault Reason 3                                    | 12 Fault Reason 3            | 12 Fault Reason 3                                                             | 12 Fault Reason 3          | 12 Fault Reason 3 | 12 Fault Reason 3 | 12 Fault Reason 3                               | 12 Fault Reason 3                                    |
|                        |                     | Alarms 0(1)                                          | Alarms 0(1)                  | Alarms 0(1)                                                                   | Alarms 0(1)                | Alarms 0(1)       | Alarms 0(1)       | Alarms 0(1)                                     | Alarms 0(1)                                          |
|                        |                     | 13                                                   | Reserved Tachometer Dual Low | Tachometer Underfrequency                                                     | Tachometer Overfrequency   | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
|                        |                     | Alarms 1(1)                                          | Alarms 1(1)                  | Alarms 1(1)                                                                   | Alarms 1(1)                | Alarms 1(1)       | Alarms 1(1)       | Alarms 1(1)                                     | Alarms 1(1)                                          |
|                        |                     | 14                                                   | Reserved Tachometer Dual Low | Tachometer Underfrequency                                                     | Tachometer Overfrequency   | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
|                        |                     | Alarms 2(1)                                          | Alarms 2(1)                  | Alarms 2(1)                                                                   | Alarms 2(1)                | Alarms 2(1)       | Alarms 2(1)       | Alarms 2(1)                                     | Alarms 2(1)                                          |
|                        |                     | 15                                                   | Reserved Tachometer Dual Low | Tachometer Underfrequency                                                     | Tachometer Overfrequency   | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
|                        |                     | Alarms 3(1)                                          | Alarms 3(1)                  | Alarms 3(1)                                                                   | Alarms 3(1)                | Alarms 3(1)       | Alarms 3(1)       | Alarms 3(1)                                     | Alarms 3(1)                                          |
|                        |                     | 16                                                   | Reserved Tachometer Dual Low | Tachometer Underfrequency                                                     | Tachometer Overfrequency   | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
|                        |                     |                                                      |                              | 17 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power |                            |                   |                   |                                                 |                                                      |
| Instance Decimal (hex) | Connection Type     |                                                      |                              |                                                                               |                            |                   |                   |                                                 | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |
| 930 (3A2h) Safety and  | Standard            | 0 Ch 3Combined Alarm Status                          | Ch 2 Combined Alarm Status   | Ch 1 Combined Alarm Status                                                    | Ch 0 Combined Alarm Status | Ch 3 Input Status | Ch 2 Input Status | Ch 1 Input Status                               | Ch 0 Input Status                                    |
| Instance Decimal (hex) | Connection Type     | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                              |                                                                               |                            |                   |                   |                                                 |                                                      |
| 946 (3B2h)             | Safety and Standard | 0  Ch 3Combined Alarm Status                         | Ch 2 Combined Alarm Status   | Ch 1 Combined Alarm Status                                                    | Ch 0 Combined Alarm Status | Ch 3 Input Status | Ch 2 Input Status | Ch 1 Input Status                               | Ch 0 Input Status                                    |
| 946 (3B2h)             | Safety and Standard | Alarms 0(1)                                          | Alarms 0(1)                  | Alarms 0(1)                                                                   | Alarms 0(1)                | Alarms 0(1)       | Alarms 0(1)       | Alarms 0(1)                                     | Alarms 0(1)                                          |
| 946 (3B2h)             | Safety and Standard | 1                                                    | Reserved Tachometer Dual Low | Tachometer Underfrequency                                                     | Tachometer Overfrequency   | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
| 946 (3B2h)             | Safety and Standard | Alarms 1(1)                                          | Alarms 1(1)                  | Alarms 1(1)                                                                   | Alarms 1(1)                | Alarms 1(1)       | Alarms 1(1)       | Alarms 1(1)                                     | Alarms 1(1)                                          |
| 946 (3B2h)             | Safety and Standard | 2                                                    | Reserved Tachometer Dual Low | Tachometer Underrange                                                         | Tachometer Overrange       | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
| 946 (3B2h)             | Safety and Standard | Alarms 2(1)                                          | Alarms 2(1)                  | Alarms 2(1)                                                                   | Alarms 2(1)                | Alarms 2(1)       | Alarms 2(1)       | Alarms 2(1)                                     | Alarms 2(1)                                          |
| 946 (3B2h)             | Safety and Standard | 3                                                    | Reserved Tachometer Dual Low | Tachometer Underrange                                                         | Tachometer Overrange       | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
| 946 (3B2h)             | Safety and Standard | Alarms 3(1)                                          | Alarms 3(1)                  | Alarms 3(1)                                                                   | Alarms 3(1)                | Alarms 3(1)       | Alarms 3(1)       | Alarms 3(1)                                     | Alarms 3(1)                                          |
| 946 (3B2h)             | Safety and Standard | 4                                                    | Reserved Tachometer Dual Low | Tachometer Underrange                                                         | Tachometer Overrange       | Low Alarm Status  | High Alarm Status | Low Low Alarm Status                            | High High Alarm Status                               |
| 946 (3B2h)             | Safety and Standard |                                                      |                              | 5 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power  |                            |                   |                   |                                                 | (1)                                                  |

(1) 0 = fault; 1 = within range.

## Configuration Assemblies

See the appropriate table for 1734-IB8S, 1734-OB8S, and 1734-IE4S configuration assembly data.

Table 42 - Configuration Assemblies for 1734-OB8S Output Modules

| Instance Decimal (hex)   |                                                                | Byte Field Class (hex) Instance (decimal)   | Attribute (decimal)   |
|--------------------------|----------------------------------------------------------------|---------------------------------------------|-----------------------|
|                          | 864 (360 h) 0 Safety Output Latch Error Time (low byte) 3B 0 8 |                                             |                       |
|                          | 1 Safety Output Latch Error Time (high byte)                   |                                             |                       |
|                          | 2 Safety Output 0 Channel Mode 3B 1 6                          |                                             |                       |
|                          | 3 Safety Output 1 Channel Mode 2                               |                                             |                       |
|                          | 4 Safety Output 2 Channel Mode 3                               |                                             |                       |
|                          | 5 Safety Output 3 Channel Mode 4                               |                                             |                       |
|                          | 6 Safety Output 4 Channel Mode 5                               |                                             |                       |
|                          | 7 Safety Output 5 Channel Mode 6                               |                                             |                       |
|                          | 8 Safety Output 6 Channel Mode 7                               |                                             |                       |
|                          | 9 Safety Output 7 Channel Mode 8                               |                                             |                       |
|                          | 10 Dual-channel Safety Output 0 Mode 3F 1 3                    |                                             |                       |
|                          | 11 Dual-channel Safety Output 1 Mode 2                         |                                             |                       |
|                          | 12 Dual-channel Safety Output 2 Mode 3                         |                                             |                       |
|                          | 13 Dual-channel Safety Output 3 Mode 4                         |                                             |                       |

Table 43 - Configuration Assemblies for 1734-OBV2S Bipolar Modules

| Instance Decimal (hex)   |                                                                | Byte Field Class (hex) Instance (decimal)   | Attribute (decimal)   |
|--------------------------|----------------------------------------------------------------|---------------------------------------------|-----------------------|
|                          | 864 (360 h) 0 Safety Output Latch Error Time (low byte) 3B 0 8 |                                             |                       |
|                          | 1 Safety Output Latch Error Time (high byte)                   |                                             |                       |
|                          | 2 Safety Output 0 Channel Mode 1 6                             |                                             |                       |
|                          | 3 Safety Output 1 Channel Mode 2                               |                                             |                       |
|                          | 4 Safety Output 2 Channel Mode 3                               |                                             |                       |
|                          | 5 Safety Output 3 Channel Mode 4                               |                                             |                       |
|                          | 6 Dual Channel Safety Out0 Mode 3F 1 3                         |                                             |                       |
|                          | 7 Dual Channel Safety Out1 Mode 2                              |                                             |                       |

Table 44 - Configuration Assemblies for 1734-IB8S Input Modules

| Instance Decimal (hex)   | Byte Field Class (hex) Instance (decimal)                          | Attribute (decimal)   |
|--------------------------|--------------------------------------------------------------------|-----------------------|
|                          | 864 (360 h) 0 Test Output 0 Mode 9 1 13                            |                       |
|                          | 1 Test Output 1 Mode 2                                             |                       |
|                          | 2 Test Output 2 Mode 3                                             |                       |
|                          | 3 Test Output 3 Mode 4                                             |                       |
|                          | 4 Safety Input Latch Error Time (low byte) 3D 0 8                  |                       |
|                          | 5 Safety Input Latch Error Time (high byte)                        |                       |
|                          | 6 Safety Input 0 Off_On_Delay (low byte) 1 5                       |                       |
|                          | 7 Safety Input 1 Off_On_Delay (high byte)                          |                       |
|                          | 8 Safety Input 0 On_Off_Delay (low byte) 6                         |                       |
|                          | 9 Safety Input 0 On_Off_Delay (high byte)                          |                       |
|                          | 10 Safety Input 0 Channel Mode 8                                   |                       |
|                          | 11 Safety Input 0 Test Source 9                                    |                       |
|                          | … Safety Input 1…6 Configuration Data … …                          |                       |
|                          | 48 Safety Input 7 Off_On_Delay (low byte) 8 5                      |                       |
|                          | 49 Safety Input 7 Off_On_Delay (high byte)                         |                       |
|                          | 50 Safety Input On_Off_Delay (low byte) 6                          |                       |
|                          | 51 Safety Input On_Off_Delay (high byte)                           |                       |
|                          | 52 Safety Input 7 Channel Mode 8                                   |                       |
|                          | 53 Safety Input 7 Test Source 9                                    |                       |
|                          | 54 Dual-channel Safety Input 0 Mode 348 1 3                        |                       |
|                          | 55 Pad Byte (0x00) … … …                                           |                       |
|                          | 56 Dual-channel Safety Input 0 Discrepancy Time (low byte) 348 1 5 |                       |
|                          | 57 Dual-channel Safety Input 0 Discrepancy Time (high byte)        |                       |
|                          | … Dual-channel Safety Input 1…2 Configuration … … …                |                       |
|                          | 66 Dual-channel Safety Input 3 Mode 348 4 3                        |                       |
|                          | 67 Pad Byte (0x00) … … …                                           |                       |
|                          | 68 Dual-channel Safety Input 3 Discrepancy Time (low byte) 348 4 5 |                       |
|                          | 69 Dual-channel Safety Input 3 Discrepancy Time (high byte)        |                       |

Table 45 - Configuration Assemblies for 1734-IE4S Input Modules

| Instance Decimal (hex)                              | Byte Field Class (hex)                                     | Instance (decimal)   | Attribute (decimal)   | Description                       |
|-----------------------------------------------------|------------------------------------------------------------|----------------------|-----------------------|-----------------------------------|
| 864 (360 h) 0 Input Type (Dual Channel Mode) 4B 1 1 |                                                            |                      |                       | Safety Input 0 Configuration Data |
|                                                     | 1 Input Range 49 1 3                                       |                      |                       |                                   |
|                                                     | 2 Input Channel Mode 49 1 4                                |                      |                       |                                   |
|                                                     | 3 Filter Setting 49 1                                      |                      |                       |                                   |
|                                                     | 4 Input Error Latch Time (Low Byte) 49 1 8                 |                      |                       |                                   |
|                                                     | 5 Input Error Latch Time (High Byte) 49 1 8                |                      |                       |                                   |
|                                                     | 6 Low Engineering (Low Byte) 49 1 14                       |                      |                       |                                   |
|                                                     | 7 Low Engineering (High Byte) 49 1 14                      |                      |                       |                                   |
|                                                     | 8 High Engineering (Low Byte) 49 1 15                      |                      |                       |                                   |
|                                                     | 9 High Engineering (High Byte) 49 1 15                     |                      |                       |                                   |
|                                                     | 10 Tach Dual Low Check 49 1 104                            |                      |                       |                                   |
|                                                     | 11 Tach Trigger 49 1 105                                   |                      |                       |                                   |
|                                                     | 12 Tach OFF Level 49 1 106                                 |                      |                       |                                   |
|                                                     | 13 Tach ON Level 49 1 107                                  |                      |                       |                                   |
|                                                     | 14 Sensor Power Mode 49 1 103                              |                      |                       |                                   |
|                                                     | 15 High High/Low Low Alarm Enable 49 1 17                  |                      |                       |                                   |
|                                                     | 16 High High/Low Low Alarm Trip High (Low Byte) 49 1 18    |                      |                       |                                   |
|                                                     | 17 High High/Low Low Alarm Trip High (High Byte) 49 1 18   |                      |                       |                                   |
|                                                     | 18 High High/Low Low Alarm Trip Low Low(Low Byte) 49 1 19  |                      |                       |                                   |
|                                                     | 19 High High/Low Low Alarm Trip Low Low(High Byte) 49 1 19 |                      |                       |                                   |
|                                                     | 20 High High/Low Low Alarm Deadband (Low Byte) 49 1 20     |                      |                       |                                   |
|                                                     | 21 High High/Low Low Deadband (High Byte) 49 1 20          |                      |                       |                                   |
|                                                     | 22 Pad Byte (Reserved) 49 … …                              |                      |                       |                                   |
|                                                     | 23 High/Low Alarm Enable 49 1 22                           |                      |                       |                                   |
|                                                     | 24 High/Low Alarm Trip High (Low Byte) 49 1 23             |                      |                       |                                   |
|                                                     | 25 High/Low Alarm Trip High (High Byte) 49 1 23            |                      |                       |                                   |
|                                                     | 26 High/Low Alarm Trip Low (Low Byte) 49 1 24              |                      |                       |                                   |
|                                                     | 27 High/Low Alarm Trip Low (High Byte) 49 1 24             |                      |                       |                                   |
|                                                     | 28 High/Low Alarm Deadband (Low Byte) 49 1 25              |                      |                       |                                   |
|                                                     | 29 High/Low Alarm Deadband High Byte) 49 1 25              |                      |                       |                                   |
|                                                     | 30 Pad Byte 1 … … …                                        |                      |                       |                                   |
|                                                     | 31 Pad Byte 2 … … …                                        |                      |                       |                                   |

Table 45 - Configuration Assemblies for 1734-IE4S Input Modules (Continued)

| Instance Decimal (hex)   | Byte Field Class (hex)                                     | Instance (decimal)   | Attribute (decimal)   | Description                       |
|--------------------------|------------------------------------------------------------|----------------------|-----------------------|-----------------------------------|
|                          | 864 (360 h) 32 Input Type (Dual Channel Mode) 4B 2 1       |                      |                       | Safety Input 1 Configuration Data |
|                          | 33 Input Range 49 2 3                                      |                      |                       |                                   |
|                          | 34 Input Channel Mode 49 2 4                               |                      |                       |                                   |
|                          | 35 Filter Setting 49 2                                     |                      |                       |                                   |
|                          | 36 Input Error Latch Time (Low Byte) 49 2 8                |                      |                       |                                   |
|                          | 37 Input Error Latch Time (High Byte) 49 2 8               |                      |                       |                                   |
|                          | 38 Low Engineering (Low Byte) 49 2 14                      |                      |                       |                                   |
|                          | 39 Low Engineering (High Byte) 49 2 14                     |                      |                       |                                   |
|                          | 40 High Engineering (Low Byte) 49 2 15                     |                      |                       |                                   |
|                          | 41 High Engineering (High Byte) 49 2 15                    |                      |                       |                                   |
|                          | 42 Tach Dual Low Check 49 2 104                            |                      |                       |                                   |
|                          | 43 Tach Trigger 49 2 105                                   |                      |                       |                                   |
|                          | 44 Tach OFF Level 49 2 106                                 |                      |                       |                                   |
|                          | 45 Tach ON Level 49 2 107                                  |                      |                       |                                   |
|                          | 46 Sensor Power Mode 49 2 103                              |                      |                       |                                   |
|                          | 47 High High/Low Low Alarm Enable 49 2 17                  |                      |                       |                                   |
|                          | 48 High High/Low Low Alarm Trip High (Low Byte) 49 2 18    |                      |                       |                                   |
|                          | 49 High High/Low Low Alarm Trip High (High Byte) 49 2 18   |                      |                       |                                   |
|                          | 50 High High/Low Low Alarm Trip Low Low(Low Byte) 49 2 19  |                      |                       |                                   |
|                          | 51 High High/Low Low Alarm Trip Low Low(High Byte) 49 2 19 |                      |                       |                                   |
|                          | 52 High High/Low Low Alarm Deadband (Low Byte) 49 2 20     |                      |                       |                                   |
|                          | 53 High High/Low Low Deadband (High Byte) 49 2 20          |                      |                       |                                   |
|                          | 54 Pad Byte (Reserved) 49 … …                              |                      |                       |                                   |
|                          | 55 High/Low Alarm Enable 49 2 22                           |                      |                       |                                   |
|                          | 56 High/Low Alarm Trip High (Low Byte) 49 2 23             |                      |                       |                                   |
|                          | 57 High/Low Alarm Trip High (High Byte) 49 2 23            |                      |                       |                                   |
|                          | 58 High/Low Alarm Trip Low (Low Byte) 49 2 24              |                      |                       |                                   |
|                          | 59 High/Low Alarm Trip Low (High Byte) 49 2 24             |                      |                       |                                   |
|                          | 60 High/Low Alarm Deadband (Low Byte) 49 2 25              |                      |                       |                                   |
|                          | 61 High/Low Alarm Deadband High Byte) 49 2 25              |                      |                       |                                   |
|                          | 62 Pad Byte 1 … … …                                        |                      |                       |                                   |
|                          | 63 Pad Byte 2 … … …                                        |                      |                       |                                   |

Table 45 - Configuration Assemblies for 1734-IE4S Input Modules (Continued)

| Instance Decimal (hex)   | Byte Field Class (hex)                                     | Instance (decimal)   | Attribute (decimal)   | Description                       |
|--------------------------|------------------------------------------------------------|----------------------|-----------------------|-----------------------------------|
|                          | 864 (360 h) 64 Input Type (Dual Channel Mode) 4B 3 1       |                      |                       | Safety Input 2 Configuration Data |
|                          | 65 Input Range 49 3 3                                      |                      |                       |                                   |
|                          | 66 Input Channel Mode 49 3 4                               |                      |                       |                                   |
|                          | 67 Filter Setting 49 3                                     |                      |                       |                                   |
|                          | 68 Input Error Latch Time (Low Byte) 49 3 8                |                      |                       |                                   |
|                          | 69 Input Error Latch Time (High Byte) 49 3 8               |                      |                       |                                   |
|                          | 70 Low Engineering (Low Byte) 49 3 14                      |                      |                       |                                   |
|                          | 71 Low Engineering (High Byte) 49 3 14                     |                      |                       |                                   |
|                          | 72 High Engineering (Low Byte) 49 3 15                     |                      |                       |                                   |
|                          | 73 High Engineering (High Byte) 49 3 15                    |                      |                       |                                   |
|                          | 74 Tach Dual Low Check 49 3 104                            |                      |                       |                                   |
|                          | 75 Tach Trigger 49 3 105                                   |                      |                       |                                   |
|                          | 76 Tach OFF Level 49 3 106                                 |                      |                       |                                   |
|                          | 77 Tach ON Level 49 3 107                                  |                      |                       |                                   |
|                          | 78 Sensor Power Mode 49 3 103                              |                      |                       |                                   |
|                          | 79 High High/Low Low Alarm Enable 49 3 17                  |                      |                       |                                   |
|                          | 80 High High/Low Low Alarm Trip High (Low Byte) 49 3 18    |                      |                       |                                   |
|                          | 81 High High/Low Low Alarm Trip High (High Byte) 49 3 18   |                      |                       |                                   |
|                          | 82 High High/Low Low Alarm Trip Low Low(Low Byte) 49 3 19  |                      |                       |                                   |
|                          | 83 High High/Low Low Alarm Trip Low Low(High Byte) 49 3 19 |                      |                       |                                   |
|                          | 84 High High/Low Low Alarm Deadband (Low Byte) 49 3 20     |                      |                       |                                   |
|                          | 85 High High/Low Low Deadband (High Byte) 49 3 20          |                      |                       |                                   |
|                          | 86 Pad Byte (Reserved) 49 … …                              |                      |                       |                                   |
|                          | 87 High/Low Alarm Enable 49 3 22                           |                      |                       |                                   |
|                          | 88 High/Low Alarm Trip High (Low Byte) 49 3 23             |                      |                       |                                   |
|                          | 89 High/Low Alarm Trip High (High Byte) 49 3 23            |                      |                       |                                   |
|                          | 90 High/Low Alarm Trip Low (Low Byte) 49 3 24              |                      |                       |                                   |
|                          | 91 High/Low Alarm Trip Low (High Byte) 49 3 24             |                      |                       |                                   |
|                          | 92 High/Low Alarm Deadband (Low Byte) 49 3 25              |                      |                       |                                   |
|                          | 93 High/Low Alarm Deadband High Byte) 49 3 25              |                      |                       |                                   |
|                          | 94 Pad Byte 1 … … …                                        |                      |                       |                                   |
|                          | 95 Pad Byte 2 … … …                                        |                      |                       |                                   |

Table 45 - Configuration Assemblies for 1734-IE4S Input Modules (Continued)

| Instance Decimal (hex)   | Byte Field Class                                            | (hex) Instance (decimal)                      | Attribute (decimal)                         | Description                   |
|--------------------------|-------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|-------------------------------|
|                          | 864 (360 h) 96 Input Type (Dual Channel Mode) 49 4 1        |                                               | Safety Input 3 Configuration Data           |                               |
|                          | 97 Input Range 49 4 3                                       |                                               |                                             |                               |
|                          | 98 Input Channel Mode 49 4 4                                |                                               |                                             |                               |
|                          | 99 Filter Setting 49 4                                      |                                               |                                             |                               |
|                          | 100 Input Error Latch Time (Low Byte) 49 4 8                |                                               |                                             |                               |
|                          | 101 Input Error Latch Time (High Byte) 49 4 8               |                                               |                                             |                               |
|                          | 102 Low Engineering (Low Byte) 49 4 14                      |                                               |                                             |                               |
|                          | 103 Low Engineering (High Byte) 49 4 14                     |                                               |                                             |                               |
|                          | 104 High Engineering (Low Byte) 49 4 15                     |                                               |                                             |                               |
|                          | 105 High Engineering (High Byte) 49 4 15                    |                                               |                                             |                               |
|                          | 106 Tach Dual Low Check 49 4 104                            |                                               |                                             |                               |
|                          | 107 Tach Trigger 49 4 105                                   |                                               |                                             |                               |
|                          | 108 Tach OFF Level 49 4 106                                 |                                               |                                             |                               |
|                          | 109 Tach ON Level 49 4 107                                  |                                               |                                             |                               |
|                          | 110 Sensor Power Mode 49 4 103                              |                                               |                                             |                               |
|                          | 111 High High/Low Low Alarm Enable 49 4 17                  |                                               |                                             |                               |
|                          | 112 High High/Low Low Alarm Trip High (Low Byte) 49 4 18    |                                               |                                             |                               |
|                          | 113 High High/Low Low Alarm Trip High (High Byte) 49 4 18   |                                               |                                             |                               |
|                          | 114 High High/Low Low Alarm Trip Low Low(Low Byte) 49 4 19  |                                               |                                             |                               |
|                          | 115 High High/Low Low Alarm Trip Low Low(High Byte) 49 4 19 |                                               |                                             |                               |
|                          | 116 High High/Low Low Alarm Deadband (Low Byte) 49 4 20     |                                               |                                             |                               |
|                          | 117 High High/Low Low Deadband (High Byte) 49 4 20          |                                               |                                             |                               |
|                          | 118 Pad Byte (Reserved) 49 … …                              |                                               |                                             |                               |
|                          | 119 High/Low Alarm Enable 49 4 22                           |                                               |                                             |                               |
|                          | 120 High/Low Alarm Trip High (Low Byte) 49 4 23             |                                               |                                             |                               |
|                          | 121 High/Low Alarm Trip High (High Byte) 49 4 23            |                                               |                                             |                               |
|                          | 122 High/Low Alarm Trip Low (Low Byte) 49 4 24              |                                               |                                             |                               |
|                          | 123 High/Low Alarm Trip Low (High Byte) 49 4 24             |                                               |                                             |                               |
|                          | 124 High/Low Alarm Deadband (Low Byte) 49 4 25              |                                               |                                             |                               |
|                          | 125 High/Low Alarm Deadband High Byte) 49 4 25              |                                               |                                             |                               |
|                          | 126 Pad Byte 1 … … …                                        |                                               |                                             |                               |
|                          | 127 Pad Byte 2 … … …                                        |                                               |                                             |                               |
|                          | 864 (360 h) 128 Ch 0_1 Discrepancy Time (Low Byte) 4B 1 3   |                                               | Dual Channel Safety Input 0_1 Configuration |                               |
|                          | 129 Ch 0_1 Discrepancy Time (High Byte) 4B 1 3              |                                               | Dual Channel Safety Input 0_1 Configuration |                               |
|                          | 130 Ch 0_1 Discrepancy Deadband (Low Byte) 4B 1 6           |                                               | Dual Channel Safety Input 0_1 Configuration |                               |
|                          | 131 Ch 0_1 Discrepancy Deadband (High Byte) 4B 1 6          |                                               | Dual Channel Safety Input 0_1 Configuration |                               |
|                          |                                                             | 132 Ch 0_1 Channel Offset (Low Byte) 4B 1 100 | Dual Channel Safety Input 0_1 Configuration |                               |
|                          | 133 Ch 0_1 Channel Offset (High Byte) 4B 1 100              |                                               | Dual Channel Safety Input 0_1 Configuration |                               |
|                          | 134 Ch 2_3 Discrepancy Time (Low Byte) 4B 2 3               |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          | 135 Ch 2_3 Discrepancy Time (High Byte) 4B 2 3              |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          | 136 Ch 2_3 Discrepancy Deadband (Low Byte) 4B 2 6           |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          | 137 Ch 2_3 Discrepancy Deadband (High Byte) 4B 2 6          |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          | 138 Ch 2_3 Channel Offset (Low Byte) 4B 2 100               |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          | 139 Ch 2_3 Channel Offset (High Byte) 4B 2 100              |                                               | Configuration                               | Dual Channel Safety Input 2_3 |
|                          |                                                             |                                               | Configuration                               | Dual Channel Safety Input 2_3 |

## Use Data from Modules Configured Via the Generic Profile

To use I/O assembly data from a 1734-IE4S module that is configured via the Generic Profile in your application program, you must first combine the input data from two SINTs into one INT. The following example shows one method for converting the data by using a Move instruction and a Bit Field Distribute instruction.

## EXAMPLE

This example uses Input Assembly Instance 802, which is described on page172 .

- POINTGuardAnalogMod.I.Data[0] = Channel 0 Low Byte (SINT)
- POINTGuardAnalogMod.I.Data[1] = Channel 0 High Byte (SINT)
- CH0\_Data = Combined Channel 0 data (INT) that can be used in an application program

<!-- image -->

## Notes:

## Numerics

## B

tags 89 , 90 , 92

| 1734-AENT  13                                           | broken wire  27                               |
|---------------------------------------------------------|-----------------------------------------------|
| add and configure  63                                   | detection  14 40 ,  74                        |
| firmware revision  64                                   | ,  Bulletin 100S  10                          |
| 1734-AENTR  13                                          | Bulletin 440G  10                             |
| 1734-EP24DC  42 ,  43 ,  44                             | Bulletin 440H  10                             |
| 1734-EPAC  42                                           | Bulletin 440K  10                             |
| 1734-FPD  42 ,  43                                      | Bulletin 440P  10                             |
| 1734-IB8S                                               | Bulletin 700S  10                             |
| field connections  49                                   | Bulletin 800F  10                             |
| muting lamp operation  38 1734-IB8S input assembly  120 | Bulletin 800T  10                             |
| y  1734-IB8S output assembly  y  120                    | Bulletin 802T  10                             |
| 1734-IE4S                                               |                                               |
| field connections  49                                   | C                                             |
| input range  27 power supply  48                        | Category  14                                  |
| 1734-IE4S input assembly  y  121                        | Category, safety  13 ,  14 ,  15 ,  17        |
| 1734-OB8S                                               | certification body  10                        |
| field connections  49                                   | channel offset  84                            |
| single channel mode  37                                 | chassis size  65                              |
| 1734-OB8S input assembly  120                           | CIP safety  y  131                            |
| 1734-OB8S output assembly  y  120 ,  121 1734-OBV2S  35 | architectures  16 protocol  13 ,  142         |
| field connections  49                                   | clean a module  11                            |
| 1734-PDN  13 ,  96                                      | combined input status  40 ,  112              |
| auto-address the nodes  98 1734-TB                      | tag  70 tags  89                              |
| 55                                                      | combined output status  40 ,                  |
| 1734-TOP  55                                            | 112                                           |
| 1734-TOP3  55                                           | tags  89                                      |
| 1756-EN2T/A  62                                         | common terms  8 communication connections  40 |
| activate safety input data  26                          | conductors  48 configuration                  |
| Active state  72                                        |                                               |
| adapter  63                                             | assemblies  173                               |
| add safety connection  111                              | download  93 ,  115 134                       |
| Advanced Connection Reaction Time Limit                 | ownership  92 ,  safety  101                  |
| alarm  29 ,  86                                         | save  93 ,  115                               |
| configuration  86                                       | settings  165                                 |
| deadband  30 ,  86                                      | verify  125 - 130                             |
| over-range  40                                          | configuration lock                            |
| under-range  40                                         | status indicator  148                         |
| Alarm tab  86                                           | configuration signature  92                   |
| analog input  15                                        |                                               |
| configuration tab  83                                   | comparison  130 copy  122                     |
| configure  80 data  90                                  | mismatch  126 configure                       |
| status indicator  48                                    | always  142 connection  8                     |
| 149 wiring  ,  55 - 59                                  |                                               |
| architectures  16 98                                    | example  lost  40                             |
|                                                         | 132 safety input                              |
| auto-addressing                                         |                                               |
|                                                         | 91 connection faulted                         |

connection reaction time limit 113

contactors 10

control devices 10

controller I/O data 23

copy

configuration signature 122

safety network number 123

crossed cable example 132

current input range 27

cycle inputs 72

## D

DC voltages 48

DCA

see Dual-channel Analog safety instruction

DCAF

see Dual-channel Analog safety instruction deadband 30 , 83

alarm 86

tolerance 31

delay time 73

device status

Safety Device Verification Wizard 126

verification 127

## DeviceNet safety

architecture 16

devices, safety 13

diagnostic data 40

digital input 13

modules 66

status indicator 149

digital output 14

status indicator 149 , 150

DIN rail 48

disable keying 63 , 64

discrepancy fault 83 , 106

discrepancy time 13 , 15 , 23 , 24 , 25 , 72 , 83

door interlocking switch 10

door monitoring switch 50

download configuration 93 , 115

download DeviceNet configuration 124 - 130

dual low inputs detection 87

dual-channel 79

complementary 19 , 23 , 25 , 72

discrepancy error 40

discrepancy fault 31

equivalent 19 , 20 , 23 , 24 , 27 , 31 , 72 , 83 , 84 ,

106

mode 13 , 14 , 15 , 23 , 36 , 37

safety contactors 53

wiring 51 , 53

Dual-channel Analog safety instruction 83 , 86

## EDS

See electronic data sheet.

electronic data sheet 8

electronic keying 77 , 82

emergency stop switch 10 , 50 , 91

wiring 51

equivalent 24

E-stop

See emergency stop switch

## EtherNet/IP

module 62

safety architecture 16

exact match 63 , 64 , 68 , 77 , 82

example connections not made 132

crossed cable 132

explicit messaging 70 , 74

external means 68 , 77 , 82

## F

falling edge 88

fault detection 22 , 24 , 36 , 37

monitoring 13

reason 90 , 153

recovery 26 , 37

fault detection 25

field connection 49

power 42

field power distributor 42 , 43

filter 85

firmware 10

followers 8

functional verification test 17

## G

gate monitoring switch

wiring 51

generic DeviceNet safety module profile 117 ,

118

glossary 8

grounding 48

GuardLogix controller 117

SNN 133

Guardmaster product 10

## E

## H

High alarm 29 , 40 , 86

status 90

High Engineering value 27 , 85

High High alarm 29 , 40 , 86

status 90

hold last state 74

## I

I/O

icon

IEC

assemblies 169

replacement 142

status data 13

device status 126

61508 9

61511 9

62061 9

## input

assemblies 169

signal lines 21

input assembly

1734-IB8S 120

1734-IE4S 121

1734-OB8S 120

input configuration tab 71

input data 69 , 89

input delay time 73

input delays

See on-delay and off-delay input error latch time 74 , 84

input filter 85

input power error bit 89

input status analog 40

combined 40

point 40

tags 70

ISO 13849-1 9

## L

leaders 8

light curtain 50

limit switches 10

listen only 65

lock

See safety-lock lost connection 40

Low alarm 29 , 40 , 86

status 90

Low Engineering value 27 , 85

Low Low alarm 29 , 40 , 86

status 90

Low Voltage Directive 41

LVD 41

## M

mean time between failure 157

message instructions 151

configure 152

mismatch

configuration signature 126

missing device

icon 126

module

guidelines 7 , 9

precautions 11

status indicator 148

MS status indicator 93 , 115

muting lamp 14 , 38 , 74

status 89

muting status 112

tag 70

## N

network adapters 13

network delay multiplier 92

network status indicator

See NS status indicator node address 96

node conditioning tool 97

NPN-style sensors 32 , 55

NS status indicator 93 , 115 , 138 , 140 , 144 , 148

## O

off-delay 13 , 26 , 73

off-level 33

on-delay 13 , 26 , 73

on-level 33

online button 124

out-of-box 137

reset module 133

## output

assemblies 171

monitor 40

safe state 19

signals 14

output assembly

1734-IB8S 120

1734-OB8S 120 , 121

Output Configuration tab 79

output data 89

menu 69

tag 89

tags 69

Output Error Latch Time 80

output power error bit 89

output readback

tags 89

## output status

combined 40

monitor 40

point 40

test outputs 40

overfrequency bit 34

ownership 92 , 115

## P

packet size 112 , 113

parameters safety configuration 103 , 106

PELV 41

Performance Level 13 , 14

PFD 17

See probability of failure on demand.

PFH 17

See probability of failure per hour.

PL 17

PLC controllers 16

PLd 14 , 54

PLe 9 , 14 , 15 , 54

PNP-style sensors 32 , 55

point input status 40 , 89 , 112

Point mode digital input 73

test output 74

point operation type 72

point output status 40

tags 89

POINTBus backplane 41 , 42

power field 42

status 112

status indicator 148

power supply 41 , 42

examples 43 - 44

external 48

probability of failure on demand 8 , 157

per hour 8 , 157

process alarms 29

configuration 86

tags 90

proof test 8

protected extra-low voltage 41

publications, related 8

pulse count 88

pulse period 21 , 35

pulse test 14 , 73 , 79

pulse testing 73

pulse width 21 , 35

push button 50

## R

rack optimization 65

readback 89

tags 89

ready to be safety locked 129

ready to be verified 127

redundant control 14

related publications 8

relays with focibly-guided contacts 10

replace configure always enabled 142

configure only enabled 137

modules 11 , 143

requested packet interval 91

reset module 133

ownership 134

resistors

55

response time 35

rising edge 88

risk assessment 10

RPI 91

RSLinx software 96 , 100

RSLogix 5000 software version 15

RSNetWorx for DeviceNet software 9 , 95 , 100 ,

131

reset module 135 version 15

RSWho

100

run mode tag 89 , 90

S

safe state 19 , 20

## safety

administrator 7 11

## safety network number 8 , 17 , 67 , 76 , 81 , 92 ,

, analog input 15 analog inputs 27 application requirements 17 configuration 101 configuration tab 101 , 105 devices 13 digital input data 22 digital input modules 66 digital inputs 13 , 20 digital outputs 14 , 35 , 37 extra-low voltage 41 input connection 91 input data 26 input fault recovery 26 input status 22 inputs 112 monitor 112 output modules 75 output with test pulse 35 outputs 11 , 19 , 112 sensors 10 system architecture 16 tab 91 safety Category 13 , 14 , 15 , 17 safety connection tab 110 safety contactor wiring 52 , 53 Safety Device Verification Wizard definition 125 device status 126 reports 129 run 125 safety-lock select devices 127 summary 130 upload and compare 128 Welcome page 125 safety extra-low voltage 41 safety instruction 83 , 86 131 , 132 copy 123 error icon 126 mismatch 143 set 132 safety signature 17 , 132 safety task watchdog 80 , 84 safety-lock devices icon 126 save 93 , 115 scale analog inputs 27 schematic diagrams 50 SELV 41 sensor power outputs 48

over-range 40

status indicator 149

under-range 40

## sensors

NPN-style 32

PNP-style 32

power supply 85

wiring 55

## sequential auto-addressing 98

## short-circuit

between input signal lines 21

detection 13

## short-circuit detection 14

SIL 3 15

SIL CL2 13 , 14

SIL CL3 9 , 14 , 15 , 17

single-channel

19

,

20

,

72

discrepancy error 40

mode 13 , 15 , 22 , 27

safety contactor 52

wiring 52

## SmartGuard controller

SNN 133

SNN 17

See safety network number.

standard 8

output data 89

outputs 14

## states of tags 89

## status bits

input power error 89

muting 38 , 39

output power error 89

status data

39

,

89

,

90

input and controller 23

## status indicators 93

analog inputs 149

configuration 148

module 148

network 148

safety input 149

safety output 149 , 150

sensor power 149

## stuck high faults 37

Studio 5000 environment 8

version 15

## Studio 5000 Logix Designer application 61

reset module 134

## suitability for use 10

## switch

door interlocking 10

door monitoring 50

emergency stop 91

gate monitoring 51

limit 10

## system reaction time 17

,

79

,

83

,

106

## T

## tachometer

dual low inputs detection 40 , 87 , 90 frequency 32 frequency over-range 40 frequency under-range 40 input wiring 48 mode 27 , 32 , 87 off-level 33 , 88 on-level 33 , 88 overfrequency 90 reset 90 under-frequency 90 wiring 55 tags 89 combined input status 70 input data 69 input status 70 muting status 70 output data 69 , 77 output status 78 status and alarms 82 status, alarms, fault 82 values 89 , 90 terminology 8 Test Output Fault Action parameter 74 test outputs 11 , 13 , 14 , 20 , 38 , 69 , 70 , 73 clear off f 74 configure 74 hold last state 74 status 40 , 112 status tags 89 tab 74 test pulse 21 , 35 test source 73

this controller r 68 , 77 , 82

92

## timeout multiplier U unknown device icon 126 upload and compare

Safety Device Verification Wizard

USB 95 , 96

128

## V

## verification reports

failure report 129

Safety Device Verification Wizard 129

## verify

DeviceNet Safety configuration 125 - 130

FAILED

129

select devices

127

verify failed 127

verify not supported 127

voltage input range 27

## W

## warning

configuration 86

welcome page 125

wiring analog inputs 55 - 59

conductors 48

dual-channel devices 51

emergency stop switch 51

examples 51 - 59

gate monitoring switch 51

modules 48 - 59

redundant safety contactor 53

safety contactor 52

sensors 55

single-channel 52

tachometer inputs 55

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

Allen-Bradley, CompactBlock, ControlFLASH, expanding human possibility, FactoryTalk, Guard I/O, GuardLogix, Guardmaster, POINTBus, POINT Guard I/O, POINT I/O, Rockwell Automation, RSLinx, RSLogix 5000, RSNetWorx, SmartGuard, Stratix, Studio 5000, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

CIP Safety, ControlNet, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800