<!-- image -->

## Guardmaster Configurable Safety Relay

Catalog Number 440C-CR30-22BBB

<!-- image -->

<!-- image -->

<!-- image -->

Original Instructions

## Important User Information
R I
R

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

Labels may also be on or inside the equipment to provide specific precautions.

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

|                         | Who Should Use this Manual. . . .                                                                                | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 7                |
|-------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|                         | Purpose of this Manual  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . 7                                                           |
|                         | Definitions . . . . . . . . . . . . . . .                                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . 8      |
|                         | Summary of Changes. . . . . . . . .                                                                              | . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 8            |
|                         | Additional Resources . . . .                                                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 9  |
|                         | Chapter 1                                                                                                        |                                                                                       |
| Overview                | Intended Use . . . . . . . . . . . . .                                                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 11       |
|                         | Hardware Features. . . . . . . . . .                                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 11           |
|                         | Software . . . . . . . . . . . . . . . . .                                                                       | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 13       |
|                         | Communication Connection . . . . .                                                                               | . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 13                   |
|                         | Chapter 2                                                                                                        |                                                                                       |
| Installation            | Mounting Dimensions . . .                                                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 15     |
|                         | Enclosure Considerations. . . . . .                                                                              | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 16               |
|                         | Help Prevent Excessive Heat . . .                                                                                | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 17               |
|                         | Chapter 3                                                                                                        |                                                                                       |
| Power, Ground, and Wire | Wiring Requirements and Recommendation . . . . . . . . . . . . . . . . . . . . . . 19                            |                                                                                       |
|                         | Ground the Configurable Safety Relay . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                  |                                                                                       |
|                         | Connect a Power Supply . . . . . . .                                                                             | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 21               |
|                         | Wire Input Devices. . . . . . . . .                                                                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 22         |
|                         | Wire Output Devices . . .                                                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 23 |
|                         | Wire Embedded Serial Port . . . .                                                                                | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 23               |
|                         | Power Cycle . . . . . . . . . . . . . .                                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 24       |
|                         | Chapter 4                                                                                                        |                                                                                       |
|                         | Configure the CR30 Safety Relay Start Connected Components Workbench Software . . . . . . . . . . . . . . . . 25 |                                                                                       |
|                         | Start Page . . . . . . . . . . . . . . .                                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 25     |
|                         | New Project . . . . . . . . . . . . . .                                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 26       |
|                         | The Workspace . . . . . . . . . . . .                                                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 29         |
|                         | Build and Download the Configuration . . . . .                                                                   | . . . . . . . . . . . .  . . . . . . . . . . 30                                       |
|                         | Verification . . . . . . . . . . . . . .                                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 33       |
|                         | Multiple Block Connections . . . .                                                                               | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 38               |
|                         | Chapter 5                                                                                                        |                                                                                       |
| Pulse Testing           | Normally Open Input Pulse Testing. . . . . . . .                                                                 | . . . . . . . . . . . . .  . . . . . . . . . . 39                                     |
|                         | Normally Closed Input Pulse Testing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                |                                                                                       |
|                         | Output Pulse Testing . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . 41                                                  |
|                         | Output Pulse Testing on Multi-Purpose Terminals . . . . . . . . . . . . . . . . . 42                             |                                                                                       |

|                               | Chapter 6                                                                                        |                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Input Filter                  | Function . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 45       |
|                               | Chapter 7                                                                                        |                                                                                         |
| Channel and Discrepancy Tests | Channel Tests . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 47           |
|                               | Discrepancy Tests . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 47             |
|                               | Chapter 8                                                                                        |                                                                                         |
| Safety Block Renaming         | General . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 53       |
|                               | Naming Error Indication . . . . . .                                                              | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 54                 |
|                               | Chapter 9                                                                                        |                                                                                         |
| Safety Monitoring Functions   | Emergency Stop . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 55                                                    |
|                               | Enabling Switch . . . . . . .                                                                    | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 56   |
|                               | Feedback Monitoring. . . . .                                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 57       |
|                               | Gate Switch . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 59         |
|                               | Safety Light Curtain. . . .                                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 60   |
|                               | Lock Control. . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 61         |
|                               | Mode Selection . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 62           |
|                               | Muting. . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 62       |
|                               | Reset . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 71     |
|                               | Restart . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 72     |
|                               | Safety Mat. . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 74       |
|                               | SensaGuard . . . . . . . . . .                                                                   | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 75 |
|                               | Single Wire Safety Input. . . . .  . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 76                                                    |
|                               | Status In . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 77       |
|                               | Two-Hand Control . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 78                                                    |
|                               | Alternate Device . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . . . 81                                                    |
|                               | Output Loop . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 86         |
|                               | Chapter 10                                                                                       |                                                                                         |
| Logic Levels A and B          | Pass Through . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 87           |
|                               | AND . . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 88     |
|                               | OR. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 88                                                          |
|                               | XOR . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . 88                                                          |
|                               | NAND . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . . . . . . . 89                                                          |
|                               | NOR . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . 89                                                          |
|                               | NOT . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . 89                                                          |
|                               | AND with Restart . . . . . .                                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 89   |
|                               | OR with Restart. . . . . . . . . . .                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 91         |
|                               | Nesting . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 92       |
|                               | Invert . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 93     |
|                               | Reset Set Flip Flop. . . . .                                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 93 |
|                               | Chapter 11                                                                                       |                                                                                         |
| Safety Outputs                | Input Connection . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 95                                                    |

|                          | Reset . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . 95                       |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
|                          | Timing . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . 95                       |
|                          | Output Connections. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                       | . . . . . . . . . . . . 95                       |
|                          | Immediate Off. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                          | . . . . . . . . 96                               |
|                          | On Delay . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . 97                       |
|                          | Off Delay . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . 98                       |
|                          | Jog. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . . . 99                 |
|                          | Muting Lamp . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                         | . . . . . . . . 99                               |
|                          | Status Out. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                             | . . . . . . . . . . . 100                        |
|                          | Chapter 12                                                                                                                                                 |                                                  |
| Micro800 Plug-in Modules | Insert Module into Controller . .  . . . . . . . . . . . . . . . . . .                                                                                     | . . . . . . . . . . . . . . . 101                |
|                          | Install a Guardmaster 440C-ENET EtherNet/IP Plug-in Module . . . . 104                                                                                     |                                                  |
|                          | Chapter 13                                                                                                                                                 |                                                  |
| Automation Controller    | Introduction. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . 109                                |
| Communications           | Ethernet Messaging . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                      | . . . . . . . . . . . 109                        |
|                          | I/O Messaging . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                         | . . . . . . . 109                                |
|                          | Explicit Messaging . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                            | . . . . . . . 120                                |
|                          | Chapter 14                                                                                                                                                 |                                                  |
| Status Indicators        | Input and Output Status Indicators. . . . . . . .                                                                                                          | . . . . . . . . . . . . .  . . . . . . . . . 124 |
|                          | Controller Status Indicators. . . . .  . . . . . . . . . . . . . . . . . .                                                                                 | . . . . . . . . . . . . . . 125                  |
|                          | Chapter 15                                                                                                                                                 |                                                  |
| Modbus Communication     | Modbus Mapping . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                      | . . . . . . . . . . . 127                        |
|                          | Example Architectures . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                   | . . . . . . . . . . . . . . . . 128              |
|                          | Read CR30 Safety Relay Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                                                      |                                                  |
|                          | Send Reset to CR30 Safety Relay .   . . . . . . . . . . . . . . . . .                                                                                      | . . . . . . . . . . . . . . . 131                |
|                          | Chapter 16                                                                                                                                                 |                                                  |
| Troubleshooting          | Recoverable Faults . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                              | . . . . . . . . . . . . . . . . 133              |
|                          | Status Indicators. . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                  | . . . . . . . . . . . 133                        |
|                          | Nonrecoverable Faults. . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                        | . . . . . . . . . . . 134                        |
|                          | Troubleshoot with the Connected Components Workbench Logic Editor . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . 134                                |
|                          | Troubleshooting with Modbus . . .  . . . . . . . . . . . . . . . . .                                                                                       | . . . . . . . . . . . . . . 136                  |
|                          | Example Fault Analysis – Cross Fault. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                                                          |                                                  |
|                          | Chapter 17                                                                                                                                                 |                                                  |
| Security and Password    | Exclusive Access . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                            | . . . . . . . . . . . . . . . . 139              |
|                          | Password Protection . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                               | . . . . . . . . . . . . . . . 139                |
|                          | Compatibility. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . 139                                |
|                          | Work with a Locked Safety Relay  . . . . . . . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . 140                |
|                          | Password Configuration . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                  | . . . . . . . . . . . . . . . 140                |

|                              | Chapter 18                                                                                        |                                                                                  |
|------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Use the Memory Module        | Overview . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 145   |
|                              | Project Back Up and Restore . . .                                                                 | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 145           |
|                              | Chapter 19                                                                                        |                                                                                  |
| Reports                      | Overview . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 149   |
|                              | Report Generator . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . . . . 149                                                        |
|                              | Appendix A                                                                                        |                                                                                  |
| Specifications               | SIL Rating. . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 151   |
|                              | Performance Level/Category . . . . .                                                              | . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 151               |
|                              | General . . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . 152 |
|                              | Environmental . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . . . . 152                                                        |
|                              | Inputs . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 152                                                        |
|                              | Outputs . . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . 153 |
|                              | Reaction Times . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . . . 153                                                        |
|                              | Recovery Times . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . . . . 153                                              |
|                              | Response Times. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . . . . . . 153                                                      |
|                              | System Response Time Calculation                                                                  | . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 153                 |
|                              | Reaction Time . . . . . . . . . . . .                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 162   |
|                              | 440C-ENET Plug-in module Specifications . . .                                                     | . . . . . . . . . . . .  . . . . . . . . 165                                     |
|                              | Appendix B                                                                                        |                                                                                  |
| Regulatory Approvals         | Agency Certifications. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . . . . . 167                                                        |
|                              | Declaration of Conformity . . . . .                                                               | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 167           |
|                              | Appendix C                                                                                        |                                                                                  |
| Configuration Reference      | Appendix D                                                                                        |                                                                                  |
| ControlFLASH Firmware Update | DMK Extraction . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 171       |
|                              | ControlFLASH . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . . . 172                                                        |
|                              | Appendix E                                                                                        |                                                                                  |
| EtherNet/IP I/O Assemblies   | Input Assemblies. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . . . . . . 175                                                      |
|                              | Output Assemblies . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . . . . . 176                                                        |
|                              | Appendix F                                                                                        |                                                                                  |
| Tag Definitions              | Input Tags . . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 177   |
|                              | Output Tags . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 178   |
|                              | Major Faults . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 179   |
|                              | Minor Faults. . . . . . . . . . . . . .                                                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 181   |
|                              | Index . . . . . . . . . . . . . . . .                                                             | . . . . . . . . . . . . . . . . 183                                              |

. . . . . . . . . . . . . . . . . . .

Who Should Use this Manual Use this manual if you design, install, configure, or troubleshoot control systems that use the CR30 safety relay.

You must have a basic understanding of electrical circuitry and familiarity with safety-related control systems. If you do not, obtain the proper training before using this product.

This manual is a reference guide for the CR30 safety relay, plug-in modules, and accessories. It describes the procedures that you use to install, wire, and troubleshoot your relay. This manual:

- Explains how to install and wire your relay.
- Gives an overview of the CR30 safety relay system.

See the Online Help provided with Connected Components Workbench™ software for more information on how to configure your CR30 safety relay.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes. Translated versions are not always available for each revision.

| Topic                                 | Page   |
|---------------------------------------|--------|
| Updated Table 42                      | 166    |
| Updated Agency Certifications 167     |        |
| Updated Declaration of Conformity 167 |        |

## Purpose of this Manual

## Summary of Changes

## Definitions

Publication AG-7.1 contains a glossary of terms and abbreviations that are used by Rockwell Automation to describe industrial automation systems. The following is a list of specific terms and abbreviations that are used in this manual.

|                                         | Term Definition                                                                                                                                                                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connected Components Workbench software | This software package allows you to configure a CR30 safety relay, program a Micro800™ controller, and configure a PanelView™ HMI.                                                                                                  |
| CR30 safety relay                       | The catalog number 440R-CR30-22BBB software configurable safety relay, described in this user manual.                                                                                                                               |
|                                         | HI Logic state of being on.                                                                                                                                                                                                         |
|                                         | LO Logic state of being off.                                                                                                                                                                                                        |
| Logic block                             | On the Connected Components Workbench software grid, a logic block resides in any of the four columns. A logic block is one of the following. • Safety monitoring function • Logic Level A • Logic Level B • Safety output function |
| Logic Level A (LLA)                     | This column is used to perform logic processes on a number of inputs to create a desired output state.                                                                                                                              |
| Logic Level B (LLB)                     | This column is used to perform logic processes on a number of inputs to create a desired output state.                                                                                                                              |
| N.C. (Normally Closed)                  | An electrical contact whose normal state (that is, no pressure or electrical potential applied) is in the closed position.                                                                                                          |
| N.O. (Normally Open)                    | An electrical contact whose normal state (that is, no pressure or electrical potential applied) is in the open position.                                                                                                            |
| OSSD (Output Signal Switching Device)   | Typically a pair of solid-state signals that are pulled up to the DC source supply. The signals are tested for short circuits to the DC power supply, short circuits to the DC common and shorts circuits between the two signals.  |
| Reaction time                           | Describes the time between the true states of one input to the on-state of the output.                                                                                                                                              |
| Recovery time                           | Describes the time that is required for the input to be in the LO state before returning to the HI state.                                                                                                                           |
| Response time                           | Describes the time between the trigger of one input to the off-state of the output.                                                                                                                                                 |
| Safety function                         | Describes the complete sensing of the action (for example, open a safety gate) to execution the final output device (for example, turn off a pair of contactors).                                                                   |
| Safety Monitoring Function (SMF)        | The input block on the Connected Components Workbench software for the CR30 safety relay.                                                                                                                                           |
| Safety Output Function (SOF)            | The output block on the Connected Components Workbench software for the CR30 safety relay.                                                                                                                                          |
| Single Wire Safety (SWS)                | A unique, safety-rated signal that is sent over one wire to indicate a safety status. The SWS can be used in Category 4, Performance Level e, per ISO 13849-1 and Safety Integrity Level (SIL) 3, per IEC 62061 and IEC 61508.      |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PanelView Component HMI Terminal User Manual, publication 2711C-UM001                                              | Provides information about operating or troubleshooting PanelView Component terminals.                                                                                                                                                                                             |
| Guardmaster 440C-CR30 Software Configurable Safety Relay Quick Start Guide, publication 440C-QS001                 | Provides information about the configuration of CR30 safety relays.                                                                                                                                                                                                                |
| Product Compatibility and Download Center (PCDC), rok.auto/pcdc                                                    | You can download the latest version of Connected Components Workbench application for your CR30 safety relay at https://compatibility.rockwellautomation.com/Pages/ MultiProductDownload.aspx?Keyword=Free&crumb=112                                                               |
| ControlFLASH User Manual, publication 1756-UM105                                                                   | Describes how to use ControlFLASH™ software to upgrade device firmware.                                                                                                                                                                                                            |
| EtherNet/IP Network Devices User Manual, ENET-UM006                                                                | Describes how to configure and use EtherNet/IP™ devices to communicate on the EtherNet/IP network.                                                                                                                                                                                 |
| Ethernet Reference Manual, ENET-RM002                                                                              | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                         |
| System Security Design Guidelines Reference Manual, SECURE-RM001                                                   | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                      |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                   |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid State Control, publication SGI-1.1                                                                                                                    | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies that incorporate solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                                |
|                                                                                                                    | Product Certifications website, rok.auto/certifications. Provides declarations of conformity, certificates, and other certification details.                                                                                                                                       |

You can view or download publications at rok.auto/literature .

## Notes:

## Intended Use

## Hardware Features

## Overview

The 440C-CR30-22BBB (CR30) safety relay is a software configurable safety relay. This device is intended to be part of the safety-related control system of a machine. Configure the CR30 safety relay with a personal computer (PC) and the Allen-Bradley® Connected Components Workbench™ software. The CR30 safety relay accommodates up to 24 safety monitoring functions. Examples of safety monitoring functions are singlechannel input, dual-channel input, two hand control, reset, and feedback.

It is based on the Micro800™ platform. The housing is red to signify it as a safety device and to distinguish it from the gray-colored standard controllers.

Figure 1 - CR30 Safety Relay

<!-- image -->

The CR30 safety relay has 22 embedded safety rated inputs and outputs and accepts up to two plug-in modules, each of which has four standard inputs and four standard outputs.

You can configure the CR30 safety relay to accept two single-wire safety inputs and to provide two single-wire safety outputs. This feature allows the CR30 safety relay to be a part of an extensive machine safeguarding system.

<!-- image -->

## CR30 Safety Relay Hardware Details

| Description Description                                           |
|-------------------------------------------------------------------|
| 1 Status indicators 10 Verification button                        |
| 2 Plug-in latch 11 DIN rail mounting latch                        |
| 3 Plug-in screw hole 12 Input status                              |
| 4 40-pin high-speed plug-in connector 13 Power status             |
| 5 I/O and power terminal blocks 14 Run status                     |
| 6 Mounting screw hole/mounting foot 15 Fault status               |
| 7 Right-side cover 16 Lock status                                 |
| 8 RS-232 non-isolated serial port 17 Serial communications status |
| 9 Type B connector USB 18 Output status                           |

<!-- image -->

## Maximum Number of Inputs and Outputs

Many of the inputs and outputs can be configured for different roles. Table 1 shows the maximum number of terminals for a specific function. A configurable terminal that is assigned to one role reduces the risks of its use as another role and reduces the allowed maximum number of terminals for other functions.

Table 1 - Maximum Terminals Allowed

Function Max Allowed Function Max Allowed

Safety inputs N.C. 18 Pulse test outputs 6

Safety inputs N.O. 6 OSSD safety outputs 10

Single-wire safety input 2 Non-pulsed (standard) outputs 6

| Single-wire safety output 2   |
|-------------------------------|

## Software

## Communication Connection

The CR30 safety relay is configurable with the Connected Components Workbench software. This software is a set of collaborative tools that supports the CR30 safety relay. It is based on Rockwell Automation and Microsoft® Visual Studio® technology. Connected Components Workbench software is used to configure the CR30 safety relay, program the Micro800 controllers, and configure many PowerFlex® drives and PanelView™ graphic display terminals.

## Obtain Connected Components Workbench Software

The Connected Components Workbench software is free. Download from https://compatibility.rockwellautomation.com/Pages/ MultiProductDownload.aspx?Keyword=Free&amp;crumb=112

To help you configure your safety relay through the Connected Components Workbench software, refer to the Connected Components Workbench Online Help (provided with the software).

The CR30 safety relay has three potential communication connections:

- USB port
- RS-232 port
- EtherNet/IP™ plug-in module

Figure 3 - Communication Connections

<!-- image -->

## USB Connection

The CR30 safety relay has a USB interface for connection to a personal computer for configuration. Use a standard USB convex (A) to convex (B) cable to connect to the safety relay.

<!-- image -->

The USB port is always available. When a USB connection is made, the CR30 safety relay appears as address 16 under the Virtual Backplane Chassis (AB\_VBP-1) in RSLinx® software (Figure 4 on page 14).

Figure 4 - CR30 Safety Relay Listed Under the Virtual Backplane

<!-- image -->

## Serial Port Connection

The embedded serial port is used to transfer control and status to other Allen-Bradley® products. The CR30 safety relay only supports the RS-232 protocol. The connection is not isolated. The RS-232 signals are referenced to the safety relay power ground.

The RS-232 port is available if an Ethernet I/P™ module is not used.

## EtherNet/IP Connection

When an EtherNet/IP module is installed, the CR30 safety relay appears under the AB\_ETHIP-n or AB\_ETH-n node, where (n) is an integer. If an EtherNet/IP plug-in module is installed, the RS-232 port is disabled.

Figure 5 shows two CR30 safety relays; one with address 30 and a second with address 47. Devices with an X over their icons are not available.

Figure 5 - CR30 Listed Under EtherNet/IP

<!-- image -->

## Mounting Dimensions

## Installation

## DIN Rail Mounting

Mounting dimensions exclude mounting feet or DIN rail latches.

Figure 6 - DIN Rail Mounting [mm (in.)]

<!-- image -->

Maintain spacing from objects such as enclosure walls, wireways, and adjacent equipment. Allow 50.8 mm (2 in.) of space on all sides for adequate ventilation. If optional accessories/modules are attached to the safety relay, such as the 2080-PS120-240VAC power supply, make sure that there is 50.8 mm (2 in.) of space on all sides after attaching the optional parts.

Mount the module with the DIN rail 35 x 7.5 x 1 mm (EN 50 022 - 35 x 7.5).

To mount the module on a DIN rail:

1. Use a screwdriver in the DIN rail latch and pry it downwards until it is in the unlatched position.
2. Hook the top of the DIN rail mounting area of the safety relay onto the DIN rail, and then press the bottom until the safety relay snaps onto the DIN rail.
3. Push the DIN rail latch back into the latched position.

Use DIN rail end anchors 1492-EAJ35 or 1492-EAHJ35 for vibration or shock environments.

To remove the module from the DIN rail, pry the DIN rail latch downwards until it is in the unlatched position.

For environments with greater vibration and shock concerns, follow Panel Mounting on page 16 instead of DIN rail mounting.

<!-- image -->

## Enclosure Considerations

## Panel Mounting

Figure 7 - Panel Mounting [mm (in.)]

<!-- image -->

The preferred mounting method is to use four M4 (#8) screws per module. Hole spacing tolerance: ±0.4 mm (0.016 in.).

Follow these steps to install your safety relay with mounting screws.

1. Place the safety relay against the panel where you are mounting it. Make sure that the safety relay is spaced properly.
2. Mark holes to be drilled through the mounting screw holes and mounting feet then remove the safety relay.
3. Drill the holes at the markings, then replace the safety relay and mount it.

Leave the protective debris strip in place until you are finished wiring the safety relay and any other devices.

Most applications require installation in an industrial enclosure to reduce the effects of electrical interference and environmental exposure. Pollution Degree 2 is an environment where normally only non-conductive pollution occurs except that occasionally temporary conductivity that condensation causes can be expected. Overvoltage Category II is the load level section of the electrical distribution system. At this level, transient voltages are controlled and do not exceed the impulse voltage capability of the product insulation.

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating. This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR 11. Without appropriate precautions, there could be difficulties with electromagnetic compatibility in residential and other environments due to conducted and radiated disturbances.

## Help Prevent Excessive Heat

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that are present. It must also be appropriately designed to help prevent personal injury as a result of accessibility to live parts. The enclosure must have suitable flame-retardant properties to help prevent or minimize the spread of flame, which complies with a flame spread rating of 5VA, V2, V1, V0 (or equivalent) if non-metallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication contain more information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

## For more information, see:

- Publication 1770-4.1 for more installation requirements.
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection that is provided by different types of enclosure.

For most applications, normal convective cooling keeps the controller within the specified operating range. Verify that the specified temperature range is maintained. For most applications, proper spacing of components within an enclosure is sufficient for heat dissipation.

In some applications, other equipment inside or outside the enclosure produce a substantial amount of heat. In this case, place blower fans inside the enclosure to help with air circulation and to reduce hot spots near the controller.

More cooling provisions are necessary when high ambient temperatures are encountered. Do not bring in unfiltered outside air. Place the controller in an enclosure to help protect it from a corrosive atmosphere. Harmful contaminants or dirt could lead to improper operation or damage to components. In extreme cases, use air conditioning to help protect against heat buildup within the enclosure.

## Notes:

## Wiring Requirements and Recommendation

## Power, Ground, and Wire

<!-- image -->

WARNING: Before you install and wire any device, disconnect power to the system.

<!-- image -->

WARNING: Calculate the maximum current in each power and common wire. Observe all electrical codes that dictate the maximum current allowable for each wire size. Current above the maximum ratings can cause wiring to overheat, which can cause damage.

- Allow for at least 50 mm (2 in.) between I/O wire ducts or terminal strips and the safety relay.
- Route incoming power to the safety relay by a path separate from the device wiring. The intersection of crossed paths must be perpendicular.
- Do not run signal or communications wiring and power wiring in the same conduit. Route wires with different signal characteristics by separate paths.
- Separate wiring by signal type. Bundle wiring with similar electrical characteristics together.
- Separate input wiring from output wiring.
- Label wiring to all devices in the system. Use tape, shrink-tubing, or other means to label wires. Also use colored insulation to identify wires based on signal characteristics. For example, you can use blue for DC wiring and red for AC wiring.
- To disable pulse testing on safety-related terminals, including dedicated safety outputs and test-pulse source-evaluating input signals, requires protection (for example, cable conduit) and separated wiring of safety signals to exclude potential cross loop faults.

## IMPORTANT

Fault exclusions for conductors and wiring must follow the requirements according to EN ISO 13849-2 Table D.3 and D.4. A fault exclusion can reduce the overall safety rating of the related safety function to a maximum of PL d per EN ISO 13849-1

## Wire Size

Table 2 - Wiring Requirements

| Wire Size   | Type Min Max   |                                         |
|-------------|----------------|-----------------------------------------|
|             | Copper Stranded 0.326 mm² (22 AWG) 1.31 mm² (16 AWG)                | Rated at 90 °C (194 °F) insulation, min |

<!-- image -->

## Ground the Configurable Safety Relay

## Terminal Assignments

Some terminals are designed to have one specific function. Some terminals can perform multiple functions; configure these terminals in the application software.

Table 3 - Terminal Assignments

| Terminal Function                                                                                      |
|--------------------------------------------------------------------------------------------------------|
| 00 Safety input (N.C.)                                                                                 |
| 01 Safety input (N.C.)                                                                                 |
| 02 Safety input (N.C.)                                                                                 |
| 03 Safety input (N.C.)                                                                                 |
| 04 Safety input (N.C.)                                                                                 |
| 05 Safety input (N.C.)                                                                                 |
| 06 Safety input (N.C.)                                                                                 |
| 07 Safety input (N.C.)                                                                                 |
| 08 Safety input (N.C.)                                                                                 |
| 09 Safety input (N.C.)                                                                                 |
| 10 Safety input (N.C.) or single wire safety input                                                     |
| 11 Safety input (N.C.) or single wire safety input                                                     |
| +24V DC A1 power supply (+24V, -15%, +10%)                                                             |
| COM 0V A2 power supply (0V)                                                                            |
| 12 Test output or OSSD high side or safety input (N.C.) or safety input (N.O). or standard diagnostic. |
| 13 Test output or OSSD high side or safety input (N.C.) or safety input (N.O.) or standard diagnostic. |
| 14 Test output or OSSD high side or safety input (N.C.) or safety input (N.O.) or standard diagnostic. |
| 15 Test output or OSSD high side or safety input (N.C.) or safety input (N.O.) or standard diagnostic. |
| 16 Test output or OSSD high side or safety input (N.C.) or safety input (N.O.) or standard diagnostic. |
| 17 Test output or OSSD high side or safety input (N.C.) or safety input (N.O.) or standard diagnostic. |
| 18 OSSD high side                                                                                      |
| 19 OSSD high side                                                                                      |
| 20 OSSD high side or single-wire safety output                                                         |
| 21 OSSD High Side or Single-wire Safety Output                                                         |

<!-- image -->

WARNING: All devices that connect to the RS-232 communication port must reference to controller ground, or float (no reference to a potential other than ground). Failure to follow this procedure can result in property damage or personal injury.

This product is intended to mount to a grounded mounting surface such as a metal panel. See publication 1770-4.1 for more information.

## Connect a Power Supply

An external 24V DC power supply source provides power for the safety relay.

To comply with the CE Low Voltage Directive (LVD), I/O power must come from a DC source compliant with Safety Extra Low Voltage (SELV) or protected extra low voltage (PELV).

To comply with UL restrictions, I/O power must come from DC sources with double insulation or reinforced insulation that isolates the secondary circuits from the primary circuit. The DC power supply must satisfy the requirements for Class 2.

The following Rockwell Automation power supply catalog numbers are SELV and PELV-compliant, and meet the isolation and output hold-off time requirements of the CR30 safety relay.

- 2080-PS120-240VAC
- 1606-XLP30E
- 1606-XLP50E
- 1606-XLP50EZ
- 1606-XLP72E
- 1606-XLP95E
- 1606-XLDNET4
- 1606-XLSDNET4

Figure 8 - Power Supply

<!-- image -->

## Wire Input Devices

## Input Devices with Mechanical Contacts

<!-- image -->

WARNING: The application of an inappropriate DC or any AC voltage can result in a loss of safety function, product damage, or serious injury. Properly apply only the specified voltage to safety relay inputs.

Input devices with mechanical contact outputs, such as Emergency Stop (E-stop) buttons and safety limit switches, use both a safety input terminal and a test output terminal. This setup enables the circuit to achieve a Category 4 rating.

When safety devices connect through test outputs to an input circuit on the CR30 safety relay, the recommended wire length is 30 m (98.4 ft) or less.

Figure 9 - Input Devices with Mechanical Contacts

<!-- image -->

## Input Devices with OSSD Outputs

Devices, such as safety light curtains, laser scanners, and solid-state interlocks, having current-sourcing PNP semiconductor outputs (OSSD) have built-in test pulses (or other method of fault detection). These devices connect directly to the inputs of the CR30 safety relay and do not use a test output. These devices must have a common reference with the CR30 safety relay.

Figure 10 - Input Devices with OSSD Outputs

<!-- image -->

## Wire Output Devices

## Wire Embedded Serial Port

## Use Surge Suppressors

You must use some type of surge suppression to help protect and extend the operating life of the safety relays output. This requirement is due to the potentially high current surges that occur when switching inductive load devices, such as motor starters and solenoids. By adding a suppression device directly across the coil of an inductive device, you prolong the life of the outputs. You also reduce the effects of voltage transients and electrical noise from radiating into adjacent systems.

The following diagram shows an output with a suppression device. We recommend that you locate the suppression device as close as possible to the load device. Since the outputs are 24V DC, we recommend 1N4001 (50V reverse voltage) to 1N4007 (1000V reverse voltage) diodes for surge suppression for the OSSD safety outputs, as shown in Figure 11. Connect the diode as close as possible to the load coil.

## Figure 11 - Surge Suppressors

<!-- image -->

Example suppressor catalog numbers include:

- 100-FSD250 for Bulletin 100S contactors
- 1492-LD4DF terminal block with built-in 1N4007 diode

The embedded serial port is a non-isolated RS-232 serial port with a target for use for short distances (&lt; 3 m [&lt; 9.8 ft]) to devices such as HMIs (for example, the PanelView™ terminal). Pin 2 and the shield both internally connect to the -24V common (A2) terminal of the CR30 safety relay.

The CR30 safety relay uses the minimal RS-232 connection; only transmit (TxD), receive (RxD) and ground connections are required. The CR30 safety relay does not require nor perform any handshake, and therefore does not use the Request to Send (RTS), Clear to Send (CTS), and Carrier Detect (DCD).

The CR30 safety relay only supports RS-232. The CR30 safety relay does not use RS-485 signals, which some products with an 8-pin mini DIN connector do use.

## Power Cycle

Figure 12 - Pinouts

<!-- image -->

Pin RS-232 Example Pin RS-232 Example

1 RS-485 (not used) 5 DCD (not used, yellow)

2 GND (green) 6 CTS (not used, white)

3 RTS (not used, red) 7 TxD (brown)

4 RxD (orange) 8 RS-485 (not used)

Table 4 shows a recommended list of cables for the serial connection between the CR30 safety relay and other Allen-Bradley® products. These cables are also suitable for third-party products.

The Deutsches Institut für Normung (DIN), the German national standards organization, standardized DIN connectors originally. Many variations of this connector exist. Select a compatible cable from Table 4 for use with the CR30 safety relay.

Table 4 - Cables

| Cat. No. Description Length                                   |
|---------------------------------------------------------------|
| 1761-CBL-AM00 8-pin mini DIN to 8-pin mini DIN 0.5 m (1.5 ft) |
| 1761-CBL-HM02 8-pin mini DIN to 8-pin mini DIN 2 m (6.5 ft)   |
| 1761-CBL-AP00 8-pin mini DIN to 9-pin D-shell 0.5 m (1.5 ft)  |
| 1761-CBL-PM02 8-pin mini DIN to 9-pin D-shell 2 m (6.5 ft)    |

The CR30 safety relay is categorized as Data Communications Equipment (DCE). The PanelView HMIs are Data Terminal Equipment (DTE). These categorizations are important when you make point-to-point wiring connections. When DTE communicates with DCE, the connections are pin X to pin X. When DTE communicates with other DTE, a crossover is required (for example, TxD must connect to RxD).

The state of the CR30 safety relay upon power-up depends on its state when power was turned off. The Run status indicator shows the state of the CR30 safety relay.

1. Program mode (Run status indicator off) The CR30 safety relay is in Program mode upon power-up.
2. Run mode with program not verified (Run status indicator flashes) The CR30 safety relay returns to Run mode. Run mode without verification is operable for only 24 hours on continuous running.
3. Run mode with program verified (Run status indicator is steady green) The CR30 safety relay returns to Run mode with no limitation on the run duration.

## Start Connected Components Workbench Software

## Start Page

## Configure the CR30 Safety Relay

This manual assumes that the Connected Components Workbench™ software is loaded and describes its basic operations. Use the online help for configuring the safety functions.

<!-- image -->

ATTENTION: Suitably trained personnel must conduct activities such as installation, adjustments, commissioning, use, assembly, disassembly, and maintenance in accordance with the applicable code of practice. If this equipment is used in a manner that the manufacture does not specify, the protection that the equipment provides can be impaired.

1. Click the Windows® Start menu in the lower left corner.
2. Click Connected Components Workbench.

<!-- image -->

The Start Page allows you to:

- Create a project
- Open an existing project
- Open a recent project
- Open online training videos (requires an internet connection)

The Discover feature is not supported with CR30 safety relays.

You can bypass this page by clearing the Show page on the startup checkbox.

<!-- image -->

## New Project

1. Start a new project three ways:
- Click New… under the Project heading
- Click File in the main menu, then click New…
- Press Ctrl-N on your keyboard

<!-- image -->

The Connected Components Workbench software maintains a list of projects to help prevent you from overwriting an existing project. The name of each new project increments by one (for example, Project90). This window allows you to select a name and a location for the file.

2. Type a new name, for example, My CR30 Project1.
3. Click Create.

<!-- image -->

The Add Device window appears.

4. Expand the Safety listing.
5. Click the catalog number 440C-CR30-22BBB.

4

<!-- image -->

You now have the opportunity to select the firmware revision of the CR30 safety relay.

6. To reveal the options, click the Version pull-down menu.
7. Click the firmware revision that resides in the CR30 safety relay. In this example, 10 is selected.

8. Click Select.

<!-- image -->

8

- To determine the current firmware revision, open the RSLinx® software, right-click the CR30 safety relay, and click Device Properties.

<!-- image -->

The firmware selection process is confirmed in the next window.

9. Confirm that the firmware revision is correct and click Add to Project.
10. The project name appears in the title of the window and in the Project Organizer. The CR30 safety relay appears in the Project Organizer with the default name Guardmaster\_440C\_CR30.

<!-- image -->

7

6

If desired, click the name (or right-click and select Rename) to change the name of the safety controller. This step is not required to complete the configuration or the run the CR30 safety relay. The name that you choose must follow these rules:

- No special characters, except underscore
- Cannot start with an underscore
- No double underscore
- 1…32 characters

In this example, the safety controller name is My\_CR30\_Project1.

<!-- image -->

<!-- image -->

An asterisk appears after the controller name and project name to indicate that a valid project has not yet been saved.

11. In the Project Organizer, double-click the safety controller name or icon to open the product configuration tab.

<!-- image -->

You can configure the following part of the CR30 safety relay:

- Plug-in modules
- Status indicator assignment
- Fault codes
- Edit the logic

## The Workspace

12. To open the workspace to create a logic configuration, click Edit Logic.

<!-- image -->

The workspace is split into a grid of four columns: Safety Monitoring (the inputs), Logic Level A, Logic Level B, and Safety Output.

Select optional panes under the View menu option to customize the workplace view.

1. Click the Toolbox icon in the upper right. Then, click and drag the pane to the desired location with the workspace.
2. Click and drag the E-stop function block to the first block in the work space.
3. The Connected Components Workbench software automatically assigns embedded input terminals EI\_00 and EI\_01 to the function block. You can change the terminal connection parameters.

<!-- image -->

3. Click and drag the immediate output to the first safety output block in the workspace.
2. The Connected Components Workbench software automatically assigns embedded output terminals EO\_18 and EO\_19 to the output block. In addition, the output terminals are pulse tested (PT). You can change the terminal connection parameters.
4. Use the pull-down menu to change the Immediate Output Reset from Manual to Automatic.
5. Click the input connection (shown in blue when no connection is made) of the immediate off output block.
6. Click the output connection of the Emergency Stop button (shown in blue when no connection is made). The Connected Components Workbench software automatically creates two pass through blocks in logic level A and logic level B and makes the connection.
7. Click the Product Setup tab.

<!-- image -->

## Build and Download the Configuration

Download initiates the transfer of the configuration file of your CR30 safety relay project to the CR30 safety relay. The download process automatically performs a file transfer verification to verify that the project configuration and configuration in the CR30 safety relay is valid and equal. Successful file transfer verification allows you to change the CR30 safety relay operation mode to Run and execute the safety function.

## IMPORTANT

Transfer file verification only checks the inconsistency of the configuration in the project and the safety relay such as connection errors and corrupted files.

After file transfer, the configured safety function itself is still not verified. The responsible personnel must check whether the configured safety function meets the safety requirements according to the risk assessment and fulfills all applicable standard and regulations

1. Click the Download icon to build and download the configuration to the CR30 safety relay.

<!-- image -->

The configuration is built and the results appear in the Output pane. The Connection Browser window appears.

2. Expand the AB\_VBP-1 branch.
3. Select node 16 (CR30).
4. Click OK.

<!-- image -->

The configuration downloads to the CR30 safety relay. A dialog box appears that shows the Configuration CRC that was downloaded and the Configuration CRC that was uploaded as part of the verification process.

5. Click Yes to change the safety relay to Run mode.

<!-- image -->

You can view the confirmation of a successful download on the Output pane. If the application is wired, you can monitor the performance of the logic with the host computer.

6. Click Edit Logic.
7. The function blocks are colored to indicate their status. All blocks are green, which indicates the dual E-stop circuits are closed and the output terminals are on.

<!-- image -->

<!-- image -->

## Verification

To complete the safety system requirements, the configuration of the CR30 safety relay must be verified. If the configuration is not verified, you can place the CR30 safety relay in Run mode for only 24 hours. When not verified, the Run status indicator flashes green at a 2 Hz rate.

<!-- image -->

After 24 hours, the CR30 safety relay reverts to a nonrecoverable fault state with a steady red Fault status indicator. The Connected Components Workbench software shows a Type 06 Code 07 fault.

The power to the CR30 safety relay must be cycled to restore operation for another 24 hours.

## Figure 13 - Non-verified Fault

<!-- image -->

If the safety system is verified, the CR30 safety relay assigns a four-digit number and allows the safety relay to operate in Run mode beyond the 24-hour limit. After verification, the Run status indicator remains steady green.

The Connected Components Workbench software must connect to the CR30 safety relay during verification.

## IMPORTANT

Document the verification process in the technical file of the safety system.

1. Click the product setup tab.
2. The CR30 safety relay must be in Program mode for verification.
3. Click Verify to make the Safety Verification window appear.
4. Answer all questions and check each box, if completed.
5. Generate enables only after all checkboxes are checked. Click Generate.

<!-- image -->

6. Click Yes to change the CR30 safety relay back to Run mode.
7. A four-digit verification ID generates.
8. Click OK.

<!-- image -->

<!-- image -->

The ID stores in the CR30 safety relay. During power-up, the CR30 safety relay uses this number during its self-testing to verify that its internal processors function properly. When the configuration uploads from the CR30 safety relay, the Connected Component Workbench software shows the Verification ID.

The ID does not store with the Connected Component Workbench project file.

<!-- image -->

## Example of CRC and Verification ID

The following steps show an example of the CRC and verification ID. The CRC for each logic program depends on the contents and are unique to that program. The verification ID is a randomly generated number that changes whenever the logic is verified.

| Step CRC Verification ID Comments   |                                                                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 83A6 4693                         | Each logic program generates a unique CRC. In this case, 83A6. The verification ID is randomly generated.                                        |
| 2 6F57 8669                         | A minor change was made to the logic program. This change generates a new CRC, 6F57. The verification process generates a new ID.                |
| 3 83A6 6331                         | The minor change was reversed; the logic is the same as in Step 1. Notice that the CRC is the same as in Step 1, and the verification ID is new. |
| 4 6F57 6854                         | The same minor change was made to the logic program as in Step 2. The CRC is the same as in Step 2 (6F57), and the verification ID is new.       |
| 5 83A6 7423                         | The minor change was reversed; the logic is the same as in Step 1. Notice that the CRC is the same as in Step 1, and the verification ID is new. |
| 6 6F57 3101                         | The same minor change was made to the logic program as in Step 2. The CRC is the same as in Step 2 (6F57), and the verification ID is new.       |

If you build multiple machines of the same design (the same logic in the CR30 safety relay), the CRC is the same for each machine, and the verification ID is different for each machine.

## View the Verification ID without the Connected Components Workbench Software

During the machine lifecycle, you must check whether the system requirements are still valid. Use the status indicators to view the verification ID without the use of the Connected Components Workbench software, and compare the documented verification ID of the technical file of the machine.

If the CR30 safety relay configuration is not verified, the ID is 0000. Press and release the Verification button. The IN 0 status indicator is green. The OUT 1, 2, 3, and 4 status indicators are green. After 5 seconds, the status indicators revert to show the status of the inputs and outputs as configured in the software.

Figure 14 - Verification ID is 0000 (Not Verified)

<!-- image -->

If the CR30 safety relay configuration is verified, press the Verification button to cycle the status indicators through each verification digit. In Figure 15 … Figure 18 on page 37, the Verification ID is 7916.

Press and release the Verification button once.

Figure 15 - First Verification Digit

<!-- image -->

Press the Verification button within 5 seconds.

Figure 16 - Second Verification Digit

<!-- image -->

Press the Verification button within 5 seconds.

Figure 17 - Third Verification Digit

<!-- image -->

Press the Verification button within 5 seconds.

Figure 18 - Fourth Verification Digit

<!-- image -->

After 5 seconds, the status indicator reverts to show the status of the inputs and outputs as configured in the Connected Components Workbench software.

## Multiple Block Connections

Multiple blocks can connect between:

- Safety monitoring functions and logic level A
- Logic level A and logic level B, and
- Logic level B and safety outputs

This connection is done by clicking the desired input and output connection points. The Connected Components Workbench software automatically determines whether the connection can be made.

Figure 19 - Multiple Block Connections

<!-- image -->

## N.O. Input Pulse Testing

## Pulse Testing

The CR30 safety relay performs three types of pulse test functions:

- N.O. inputs
- N.C. inputs
- Outputs

When a safety input is configured for normally open (N.O.) operation, the CR30 safety relay periodically checks the status of the input. The purpose of the test pulse is to detect short circuits in the wiring to 24V DC, 0V and between two channels. This test is independent of the input test pulses. You can configure six terminals (12…17) for normally open operation.

When a terminal is configured for N.O. operation, the CR30 safety relay generates a test pulse, as shown in Figure 20, to test the status of each terminal.

The N.O. input pulse tests cannot be configured on or off. If the terminal is configured to be N.O., the CR30 safety relay performs pulse tests.

## Figure 20 - N.O. Terminal Test Pulse

<!-- image -->

When multiple terminals are configured for N.O. operation, the CR30 safety relay tests each one at 500 ms intervals. This test sequence repeats every 6.4 seconds.

In Figure 21 on page 40, terminals 12, 14, 15, and 17 are configured for N.O. operation, and are tested. Terminals 13 and 16 are configured for N.C. operation, therefore the test pulse does not occur on these two terminals.

<!-- image -->

## N.C. Input Pulse Testing

<!-- image -->

Terminals 12…17 can be configured to generate test pulse outputs. These signals are used to test for short circuits in the wiring to 24V DC, 0V and between two channels that are wired to separate test pulse sources (one channel that is sourced from an odd number terminal [13, 15, and 17], and the other one from an even number terminal [12, 14, and 16]).

| IMPORTANT   | Safety systems that require a Category 4 structure per ISO13849-1 and SIL 3 rating per IEC61508 must use pulse tests for the dual-channel N.C. contacts. Pulse tests for Category 3, 2, and 1 structures and SIL 2 and 1 ratings are recommended.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The CR30 safety relay generates three distinct pulses, called A, B, and C. Each pulse is 1.7 ms wide. Pulse Test B immediately follows Pulse Test A. Pulse Test C immediately follows Pulse Test B. The pulse tests repeat every 25 ms.

The timing diagram in Figure 22 shows an example of the pulse tests when the respective terminals are configured for A, B, and C.

Figure 22 - Timing Diagram

<!-- image -->

## Output Pulse Testing

The purpose of the test pulses is to detect short circuits from the input signal to 24V DC, 24V common, and shorts from one input signal to another input signal. If one input signal is assigned to Test Pulse A and another signal is assigned to Test Pulse B (or C), then the CR30 safety relay detects a short circuit from one input to the other. The CR30 safety relay then de-energizes the outputs of those safety functions that use the two inputs. In this example, you cannot select terminal 12 as one test pulse source and terminal 15 as the second test pulse source, as both of these terminals produce the A pulse.

The Connected Components Workbench™ software automatically helps prevent the selection of two of the same pulses when dual-channel inputs and two test sources are selected.

Internally, the CR30 safety relay provides dual-channel capability to turn off its safety outputs. Conceptually, the safety relay is a main output transistor that feeds individual output transistors. The CR30 safety relay repeats a test process where it tests the main transistor twice and then sequentially tests each individual output twice. After successful completion of the tests, the CR30 safety relay repeats the test sequence.

## IMPORTANT

Safety systems that require a Category 4 structure per ISO13849-1 and SIL 3 rating per IEC61508 must use pulse tests for the dual-channel outputs. Pulse tests for Category 3, 2, and 1 structures and SIL 2 and 1 ratings is recommended.

## Figure 23 - Output Pulse Tests

<!-- image -->

When the main transistor is tested, a 50 μs test pulse appears simultaneously on all outputs. The main transistor is tested again 125 ms later.

Figure 24 - Main Transistor Test

<!-- image -->

## Output Pulse Testing on Multi-purpose Terminals

Then a sequence occurs in which each output is individually tested twice. The test pulse is 50 μs wide. The test pulses occur every 250 ms and switch to the next output configured with testing.

Figure 25 - Test Pulse Sequence

<!-- image -->

| Terminal 12   | 24V 0V       |
|---------------|--------------|
| Terminal 13   | 24V 0V       |
| Terminal 20   | 24V 0V       |
| Terminal 21   | 24V 0V       |
|               | 0 250 500 ms |

When a multi-purpose terminal (12…17) is configured for use as an output with pulse testing, a 340 μs test pulse generates on the terminal. The length of the pulse is typically 340 μs, but can be as long as 700 μs, depending on the logic and the number of plug-in modules. The pulse test detects short circuits to other terminals, 24V, and 0V.

Figure 26 shows the pattern for the output test pulses. If the terminal is not configured for pulse testing, the 340 μs pulse does not appear. The pulses occur on sequential terminals at 500 ms increments. The sequence repeats approximately every 5900 ms.

Figure 26 - Multi-purpose Output Test Pulses

<!-- image -->

Figure 27 on page 43 shows an example of pulse tests with multi-purpose terminals. Terminals 12…15 are configured for no pulse testing (No PT), and terminals 16…17 are configured to use pulse testing (PT).

The 50 μs pulse tests appear on all terminals. Terminals 12…15 do not use the 50 μs pulse tests to detect short circuits to each other or short circuits to 24V. Short circuits to 0V are detected and result in a fault.

Terminals 16…17 generate the 340 μs test pulses and detect short circuits to each other, to 24V, and to 0V.

## Figure 27 - Pulse Testing Example

<!-- image -->

## Notes:

## Function

## Input Filter

Input filtering gives the CR30 safety relay the ability to filter out slow operating contacts, contact bounce, and inadvertent switching that might occur, for example, in three-position enabling devices.

When an input filter time is specified, an input channel is allowed to change state and return to its original state while the second input channel remains in the same state. The input filter works on the transition from LO to HI and from HI to LO.

You can set input filtering in 25 ms increments from 0…1000 ms. The default value is 0 ms. Typically, the input filter is set to a shorter time than the discrepancy time.

Figure 28 shows a graphical description of the input filter.

<!-- image -->

ATTENTION: If the input filter time is set to a nonzero value, add the filter time to the response time of the safety function. A response time greater than 90 ms can allow a person to walk through a safety light curtain undetected. Adjust safety distance/physical barriers accordingly.

## Figure 28 - Input Filtering

<!-- image -->

| Item Description                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 Input 2 goes LO and then HI within the filter time, while Input 1 remains HI. The SMF output remains HI.                                                                                                                     |
| 2 Input 2 goes LO and stays LO, while Input 1 remains HI.                                                                                                                                                                      |
| 3 When the input filter time expires, the SMF output goes LO.                                                                                                                                                                  |
| 4 Input 1 goes LO. Both inputs are LO during the input filter time.                                                                                                                                                            |
| 5  Both Inputs 1 and 2 go HI but Input 1 bounces. Each time the input transitions, the filter timer gets reset. Continued instability of an input leads to a discrepancy fault, if discrepancy time is set to a nonzero value. |
| 6 Input 1 has stabilized during the input filter time, and the SMF output goes HI.                                                                                                                                             |
| 7 Both inputs go LO and HI and then LO and HI again within the input filter time. The SMF output remains HI.                                                                                                                   |

<!-- image -->

Figure 29 shows that the input filtering is set in the Advanced Settings of each safety monitoring block. In this example, the Enabling Switch function has its input filter is set to 4 (4 x 25 = 100 ms).

Figure 29 - Enabling Switch

<!-- image -->

## Channel Tests

## Discrepancy Tests

## Channel and Discrepancy Tests

The CR30 safety relay performs channel and discrepancy tests when the discrepancy time is set to a nonzero value.

The CR30 safety relay performs the channel test to the individual channel inputs. The channel test happens only if the discrepancy time is set to a nonzero value. The channel tests for conditions like the following:

- Slow-moving doors or gates that use nonsnap-acting contacts
- Two independently operated inputs that go to one safety monitoring function block
- Contact bounce

If both inputs are HI and one input goes LO and returns HI, without the other channel changing to the same state, the CR30 safety relay exhibits a channel fault. The output of the safety monitoring function block turns off. You can adjust the input filter to ignore some channel faults (see Input Filter on page 45).

The CR30 safety relay shows a channel fault by a flashing Fault status indicator. In the Connected Components Workbench™ software, the SMF block is red with a channel fault message box. In the Studio 5000® application, a channel fault shows as a minor fault type 10H and fault code 08H. To clear the fault, set both inputs LO until the input filter time expires. The channel fault clears when both inputs go HI again.

Safety monitoring functions, which use two inputs, have a feature that allows the CR30 safety relay to test for the timing between the operation of both inputs. This feature is the discrepancy time. You can set the discrepancy time from 0…3 seconds, in 50 ms increments. The default value is 2, which translates to 100 ms (2 x 50 = 100 ms). If the discrepancy time is set to 0, the discrepancy test does not occur.

When the discrepancy time is set to a nonzero value, both inputs must go to the same state within the discrepancy time. This action applies when the inputs go to the LO state and the HI state. If both inputs do not go to the same state within the discrepancy time, the CR30 safety relay goes to a recoverable fault state. The Fault status indicator flashes red, and you can see the fault in the Connected Components Workbench software as a discrepancy fault. In the Studio 5000 application, a discrepancy fault shows as a minor fault type 10H and fault code 20H. The discrepancy test applies to all two-channel configurations, including two N.C. with and without pulse testing and two OSSD.

<!-- image -->

To clear the fault, set both inputs LO. The discrepancy fault clears when both inputs go HI within the discrepancy time.

Figure 30 shows a graphical example of how the safety monitoring function block performs the discrepancy and channel tests.

<!-- image -->

Figure 30 - Discrepancy and Channel Timing Examples

| Item Description                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 With both inputs HI, Input 2 goes LO.                                                                                                                                         |
| 2 After the input filter time expires, the SMF output goes LO.                                                                                                                  |
| 3 While Input 1 remains HI, Input 2 goes HI. This action generates a channel fault.                                                                                             |
| 4 Both inputs go LO in preparation to clear the fault.                                                                                                                          |
| 5  After the inputs remain LO for a duration that exceeds the filter time, both inputs go HI. The SMF output goes HI, and the channel fault is cleared.                         |
| 6 With both inputs HI, Input 1 goes LO.                                                                                                                                         |
| 7 After the input filter time expires, the SMF output goes LO.                                                                                                                  |
| 8  While Input 2 remains HI, Input 1 goes HI after the discrepancy time expired. This action generates a channel fault and a discrepancy fault.                                 |
| 9 Both inputs go LO in preparation to clear the fault.                                                                                                                          |
| 10  After the inputs remain LO for a duration that exceeds the filter time, both inputs go HI. The SMF output goes HI, and both the channel and discrepancy faults are cleared. |

Figure 31 shows where the discrepancy time sets and an example of the fault message that appears in the Connected Components Workbench software. The discrepancy sets in the advanced settings of each safety monitoring function block, when the number of inputs is 2. When a discrepancy fault occurs, the safety monitoring block shows in red with a discrepancy fault message box.

Figure 31 - Setting Discrepancy Time and Fault Message

<!-- image -->

Set Discrepancy in Advanced Settings

## Initial Transition to Run Mode

Upon power-up, the CR30 safety relay performs internal self-tests. After the unit successfully passes the self-tests, the CR30 safety relay transitions to Run mode. In firmware up to 10.010, the CR30 safety relay immediately (on the first logic scan) performs a channel test on safety monitoring function blocks with dual-channel inputs. The channel test does not consider the discrepancy time setting. If an inconsistency exists (input 1 is HI and input 2 is LO, or vice versa), the CR30 safety relay would go to a channel fault state.

Safeguarding devices with pulse checking OSSD outputs, like the SensaGuard™ interlock, can occasionally experience this condition, depending upon when the pulse test occurred. The CR30 safety relay observes the test pulse as an off-state on one channel and an on-state of the second channel. To clear this fault, open and close the safety gate after the first logic scan of the CR30 safety relay completes.

In firmware 10.011, the first scan channel test is removed. The discrepancy test detects and reports potential inconsistencies as a fault, if the discrepancy time is set to a nonzero value and the discrepancy still exists.

Example of discrepancy fault message

Figure 32 and Figure 33 compare the results of the firmware change when the CR30 safety relay initially transitions to Run mode. Dual-channel E-stop function blocks without pulse testing demonstrate the functionality. This transition occurs after the internal self-checks complete upon power-up or after downloading a program change and changing to Run mode. In the examples in Figures 30 and 31, the CR30 safety relay has the EI\_00 input LO and the EI\_01 input HI at the transition to Run mode.

In Figure 32, the discrepancy time is set to 0 (disabled).

## Figure 32 - Discrepancy = 0 (disabled) on Initial Transition to Run Mode

Firmware up to 10.010

The CR30 safety relay reports a channel fault if one channel is on and the other is off. The SMF1 output remains off.

<!-- image -->

Firmware 10.011 and later The CR30 safety relay does not report a channel fault if one channel is on and the other is off. The SMF1 output remains off.

<!-- image -->

In Figure 33, the discrepancy time is set to a nonzero value (enabled).

## Figure 33 - Discrepancy = Nonzero (enabled) on Initial Transition to Run Mode

Firmware up to 10.010

The CR30 safety relay reports both a channel fault and a discrepancy fault if one channel is on and the other is off. The SMF1 output remains off.

<!-- image -->

Firmware 10.011 and later

The CR30 safety relay reports only a discrepancy fault if one channel is on and the other is off. The SMF1 output remains off.

<!-- image -->

This condition also applies to OSSD devices that use pulse testing. In firmware up to revision 10.010, the CR30 safety relay can potentially detect one OSSD channel that is off; the CR30 safety relay evaluates the input during the pulse test, and the second OSSD channel while it was not executing its pulse test. This condition results in an occasional channel fault. Firmware 10.011 removes the channel test, and devices do not experience channel faults when the CR30 safety relay initially transitions to the Run mode. In the subsequent logic scans, the safety monitoring function block goes to a HI state.

Both channels start from a HI state. One input goes LO and then back HI quickly. Notice that both inputs are green. The SMF1 output is off, and no fault is present.

To detect this state, configure the status indicators to show the terminal or SMF status. Cycle both inputs LO and then back HI to get SMF output HI.

<!-- image -->

Both channels start from a HI state. One input goes LO and then returns to HI within the discrepancy time. This action generates a channel fault.

Cycle both inputs LO longer than the input filter time and then back HI to clear the fault and turn the SMF output HI.

<!-- image -->

## Figure 34 shows an example of the results with a SensaGuard function block.

## Figure 34 - Example with Devices with Pulse Testing OSSD Outputs

Firmware up to 10.010 Potential channel fault if either input is tested during the pulse test. This fault is independent of the discrepancy time.

Firmware 10.011 and later With the channel test removed on the initial transition, the SensaGuard function block goes to the on state on subsequent logic scans.

<!-- image -->

<!-- image -->

## After Initial Transition to Run Mode

Figure 35 and Figure 36 show examples of faults that can occur after the initial transition to Run mode. These examples apply to all firmware revisions.

## Figure 35 - Discrepancy = 0 (Disabled) After the Initial Transition to Run Mode

Both channels start from a HI state. One input goes LO and stays LO. Notice that one input is gray and the second input is green. The SMF1 output is off, and no fault is present.

To detect this state, configure the status indicators to show the terminal or SMF status. Cycle both inputs LO and then back HI to get SMF output HI.

<!-- image -->

Both channels start from a HI state. One input goes LO and then, after an extended time, returns HI. Notice that both inputs are green, and the SMF1 output is off, and no fault is present. To detect this state, configure the status indicators to show the terminal or SMF status. Cycle both inputs LO and then back HI to get SMF output HI.

Figure 36 - Discrepancy = Nonzero (Enabled) After the Initial Transition to Run Mode

<!-- image -->

Both channels start from a HI state. One input goes LO and stays LO after the discrepancy time. This action generates a Discrepancy Fault.

Cycle both inputs LO longer than the discrepancy time and then back HI to clear the fault and turn the SMF output HI.

<!-- image -->

Both channels start from a HI state. One input goes LO and then returns to HI after the discrepancy time. Notice two faults are shown.

Cycle both inputs LO longer than the input filter time and then back HI to clear both faults and turn the SMF output HI.

<!-- image -->

## Notes:

## General

## Safety Block Renaming

With revision 7 of the Connected Components Workbench™ software and revision 7 of the CR30 safety relay firmware, you can edit the names of both the safety monitoring functions and safety output functions. The editing rules follow IEC 61131-3, section 2.1.2.

This feature allows you to distinguish between multiple occurrences of the same function blocks during the design, wiring, and troubleshooting phases.

The name change is initiated in one of two ways.

- Double-click the name inside the block
- Highlight the block and press F2

Use the typical editing keys (Home, End, Backspace, Delete, Left Arrow, Right Arrow, Page Up, Page Down, and Mouse Click) to edit the name.

When you select the block for editing, the name appears in a light blue box, and the name highlights in a light blue background, as shown in Figure 37 .

Figure 37 - Block Name Selected for Editing

<!-- image -->

Follow these simple rules for block names.

- Names must begin with a letter (upper or lower case) or an underscore
- Names cannot have spaces
- Names can contain letters, numbers, and underscores (no special characters)
- Name length can be anywhere from 1…30 characters
- Letter case is not significant
- Multiple leading or consecutive embedded underscores are not allowed
- Trailing underscores are not allowed

<!-- image -->

## Naming Error Indication

After you tab off, press Enter, or move your cursor off the block, the Connected Components Workbench software evaluates the integrity of the name. If valid, the name appears in black letters. If invalid, the software shows a naming error in two ways.

- A red box around the name
- An error message in the build results

## Figure 38 - Red Box Indicates Naming Error

<!-- image -->

The example block in Figure 39 has two errors.

- The name starts with a period (.)
- The name contains a space

## Figure 39 - Build Error List

<!-- image -->

After you click the Build button, the Error List shows the naming errors. In the example in Figure 39, SMF1 and SOF1 have naming errors.

When a naming error occurs, the project cannot be built and downloaded to the CR30 safety relay until you correct the naming errors. However, you can save and reopen the project with the naming errors.

## Emergency Stop

## Safety Monitoring Functions

Many types of safeguarding/safety devices and safety-related signals can connect as inputs to the CR30 safety relay. The Connected Components Workbench™ software facilitates the selection and connection of the device. Each block is assigned the next available settings for input terminals, test sources number of inputs, pulse testing, discrepancy time, and input filter.

The emergency stop function block sets the parameters for typical E-stop push buttons. In the Connected Components Workbench software, click and drag (or double-click) the block to an available safety monitoring function spot. When you use mechanical operated contacts, these contacts must be direct-acting contacts.

Figure 40 - Emergency Stop Function Block

<!-- image -->

The available input selections for the emergency stop inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can modify the number and types of inputs:

- 2 N.C.
- 2 OSSD
- 1 N.C.

You can disable or set pulse testing to 2 Sources. When you select 2 Sources, the next available test sources are automatically selected. You can modify the sources afterward.

<!-- image -->

## Enabling Switch

You can use the default discrepancy time and input filter or choose to modify these settings.

Figure 41 - Example Schematic of a Dual-Channel E-stop Without Test Pulses

<!-- image -->

Figure 42 - Example Schematic of a Dual-Channel E-stop Using Test Pulses A and B

<!-- image -->

The enabling switch function block sets the parameters for typical enabling (or hold-to-run) devices. In the Connected Components Workbench software, click and drag (or double-click) the block to an available safety monitoring function spot. When you use mechanical operated, these contacts must be direct-acting contacts.

<!-- image -->

Only use this function block in applications with a 3-position enabling switch that only allows the activation of its outputs (closed contacts) when you press and hold the switch into its middle position. The switch must be designed using a mechanical force to reset to its default off (contact open) position.

Figure 43 - Enabling Switch Function Block

<!-- image -->

The available input selections for the enabling switch inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

## Feedback Monitoring

You can modify the number and types of inputs:

- 2 N.C.
- 2 OSSD
- 1 N.C.

You can disable pulse testing or set to 2 Sources. When you select 2 Sources, the next available test sources are automatically selected. You can modify the sources afterward.

You can use the default discrepancy time and input filter or choose to modify these settings.

Figure 44 - Example Schematic of a Dual-channel Enabling Switch Without Test Pulses

<!-- image -->

Figure 45 - Example Schematic of a Dual-channel Enabling Switch Using Test Pulses A and B

<!-- image -->

Safety systems use the feedback function block to monitor the status of output devices (like safety contactors). When the output device is off, a HI signal feeds back to the input of the CR30 safety relay to indicate that the device is indeed off. When the output device energizes, the feedback signal goes LO. If the output device remains energized, the feedback signal remains LO and the CR30 safety relay does not energize the output. The feedback contacts can be positive-guided, mechanically linked, or mirrored contacts.

The CR30 safety relay accepts one, two, three, or four inputs into each feedback block. All inputs must be HI for the output of the block to go HI.

In the Connected Components Workbench software, click and drag (or double-click) the block to an available safety monitoring function spot.

Figure 46 - Feedback Monitoring Function Block

<!-- image -->

The available input selections for the feedback monitoring are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)
- P1\_00…P1\_03 (plug-in 1 terminals 00…03)
- P2\_00…P2\_03 (plug-in 2 terminals 00…03)
- SP\_00…SP\_15 (Modbus inputs 00…05)

You can modify the number of inputs within the range of 1…4.

You can use the default input filter or choose to modify this setting.

In firmware revision 10 and later, multiple output blocks can use each feedback block.

Figure 47 - Example Feedback Schematic with Two Feedback Contacts Connected in Series to One Input Terminal

<!-- image -->

Figure 48 - Example Feedback Schematic with Four Feedback Contacts Connected Individually to Four Input Terminals

<!-- image -->

## Gate Switch

The gate switch function block sets the parameters for typical safety-gate interlock switches. In the Connected Components Workbench software, click and drag (or double-click) the block to an available safety monitoring function spot.

Figure 49 - Gate Switch Function Block

<!-- image -->

The available input selections for the gate switch inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can modify the number and types of inputs:

- 2 N.C.
- 2 OSSD
- 1 N.C.

You can disable pulse testing or set to 2 Sources. When you select 2 Sources, the next available test sources are automatically selected. You can modify the sources afterward.

You can use the default discrepancy time and input filter or choose to modify these settings.

Figure 50 - Example Schematic of a Dual-channel Safety Gate Switch Without Test Pulses

<!-- image -->

## Safety Light Curtain

Figure 51 - Example Schematic of a Dual-channel Safety Gate Switch Using Test Pulses A and B

<!-- image -->

Figure 52 - Example Schematic of a Dual-channel Safety Gate Switch Using OSSD Outputs

<!-- image -->

The safety light curtain function block sets the parameters for safety light curtains that have dual OSSD outputs. In the Connected Components Workbench software, click and drag (or double-click) the block to an available safety monitoring function spot. You can use this block for other devices, like laser scanners, with OSSD outputs.

Figure 53 - Safety Light Curtain Function Block

<!-- image -->

The available input selections for the safety light curtain inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can use the default discrepancy time and input filter or choose to modify these settings.

## Lock Control

Figure 54 - Example Schematic of a Safety Light Curtain

<!-- image -->

The lock control function block is designed to issue an unlock request to a guard locking safety device. Example devices include the Guardmaster® TLS-ZR, TLS-ZL, 440G-LZ, TLS1, TLS2, TLS3, 440G-MT, and Atlas™ Guard Locking Switches. This function controls both Power to Lock and Power to Release switches.

Figure 55 - Lock Control Function Block

<!-- image -->

- LR: The lock request input turns off the ULC (Unlock Control Output).
- ULR: The Unlock Request input is used to request a Power to Release electromagnetic solenoid (or similar device) to unlock. It turns on the UCL output when two conditions are met.
- The hazard feedback signal is on.
- The stop time has expired.
- ULR Latch: Set to off or on by a mouse click. When the ULR Latch configuration is set to off, the unlock request input is ignored during hazardous motion, that is, when the hazard feedback input is off.

When the ULR Latch configuration is set to on, the unlock request input is latched even during hazardous motion, that is, when the hazard feedback input is off. When the hazard feedback turns on, the Unlock Command (ULC) goes active after the stop time expires.

- Stop Time: The Stop Time is a preset time delay that begins timing when the hazard feedback transitions to on. After the timer expires, the unlock request signal can be used to energize the unlock command. You must set the stop time to a value that allows the hazard to stop before sending the unlock request.
- The input terminals can also be assigned to another function block.

## Mode Selection

## Muting

The mode selection function block allows easy configuration for a 2 or 3-position selector switch. The Positions field determines the number of positions.

Figure 56 - Mode Selection Function Block

<!-- image -->

Place the mode selector on the workspace where there are three consecutive unassigned safety monitoring blocks.

Only one input can be on at any given time, and at least one input must be on. The transition from one position to another position must be completed with 250 milliseconds.

The first input turns on the first output. The second input turns on the second output. The third input turns on the third output.

IMPORTANT

Recoverable faults include No Input Selected or Multiple Inputs Selected. To clear recoverable faults, cycle through each mode.

Muting is the temporary automatic suspension of the protective function of a safeguarding device like a safety light curtain. The muting function allows the transport of material through a safety light curtain without stopping a conveyor. To distinguish between material and persons, a certain sequence of events and timings are used.

Muting sensors mount in a certain pattern, and the material must pass by the sensors and safety light curtain within specified time limits. If the muting sensor sequence is incorrect or the timing parameters are violated, the conveyor is turned off. An override signal moves the material through the safety light curtain after a violation.

Figure 57 - Muting Function Block

<!-- image -->

The safety light curtain (LC) signals can use the following terminals:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

The muting (S1…S4) and override (OV) signals can use the following terminals:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)
- P1\_00…P1\_03 (plug-in 1 terminals 00…03)
- P2\_00…P2\_03 (plug-in 2 terminals 00…03)

You can use the default discrepancy time and input filters or choose to modify these settings.

The CR30 safety relay has three distinct types of muting, where the sequence and timing of signals that the CR30 safety relay monitors allows objects to pass through the safety light curtain without shutting down the machine process. The three types are:

- 2-sensor T-type
- 2-sensor L-type
- 4-sensor

## Override Settings

- Override: When the Override configuration is set to on, the override settings are exposed. To hide the settings, set the configuration to off.
- OV O2: When the OV O2 configuration is set to on, an additional output is shown in the function block; this output is labeled O2. If the O1 output is off, the Override input turns both the O1 and O2 outputs on for the max override time as long the OV input is held on. If the OV input is turned off before the time expires, the O1 and O2 outputs turn off. If additional time is needed, the Override input can be cycled on again. If the O1 output is on, the Override input is ignored.
- Exit Ends Override: When configured to on, the O2 override output turns off when the material successfully moves through the safety light curtain and pass the sensors. When configured to off, the O2 output remains on during the override time.
- Max Override Time: Set the maximum duration of the override time in increments of 5 seconds. The time can be set from 1…255 (1…1275 s). A setting of 0 turns on the O1 and O2 outputs for 0.5 seconds.
- Inputs: Set the desired number of input terminals to execute the override function.
- Pulse Testing: Creates or removes pulse testing for the override inputs. If pulse testing is selected, then the terminals that are used for Test Source A and B must be selected.

## Advanced Settings

- Mute Enable: When the Mute Enable configuration is set to on, an input terminal is added to the mute function block; this input is labeled ME. When the mute enable configuration is set to off, the input terminal is removed.
- When mute enable is set to on, a 24V DC signal must be provided to the specified terminal to allow the use of the sensor inputs to mute the safety light curtain inputs. When the signal is 0V, two conditions can happen.
- Blocked sensors cause the function block and the fault indicator to show a recoverable fault, but does not turn off the O1 output. The Fault Reset button clears the fault after the sensor is cleared.
- A blocked the safety light curtain causes the O1 output to turn off. The O1 output to turns on, when the safety light curtain is cleared.

When mute enable is set to off, the muting function is always active.

- Mute Fault Reset: When the Mute Fault Reset configuration is set to on, a new input terminal is added to the mute function; this input is labeled FR. To remove the input terminal, set the mute fault reset
- configuration to off.
- After a recoverable fault occurs, the FR input must be cycled on and then off. Reset occurs on the trailing edge of the signal. The reset cycle must be completed within 3 seconds.

## Two-sensor T-type Muting

The sensors and safety light curtain form the shape of an upside down T, when viewed from the side. The muting sensors (MS) are mounted to form an X sensing pattern where the sensing beams cross near the center of the safety light curtain (LC).

The muting sensors must mount asymmetrically (unequal distance from the safety light curtain), such that the material breaks one muting sensor and then the other muting sensor as it moves along the conveyor.

Figure 58 - Two-sensor T-type Muting Arrangement

<!-- image -->

The material can break either MS1 first (or MS2 first), then the other sensor, and then the safety light curtain. As the material clears the safety light curtain, it must then clear MS2 (or MS1) first and then the other sensor. The muting lamp turns on shortly after the second sensor is blocked, and the safety light curtain is muted.

Either of these two patterns is acceptable:

- MS1 MS2 LC LC MS2 MS1
- MS2 MS1 LC LC MS1 MS2

With proper arrangement of the sensors, the conveyor can move in the forward or reverse direction, and maintain safeguard integrity simultaneously.

In the example below, the OSSD outputs of the safety light curtain are connected to terminals 00 and 01. The two muting sensors are connected to terminals 02 and 03. The momentary, normally open override switch is connected between terminals 12 to 04 to take advantage of pulse testing. Contactors K1 and K2, which provide power to the conveyor (and to other hazards), are connected to terminals 18 and 19.

The muting lamp connects to terminal 13; this terminal must be configured with no pulse testing. Pulse testing does not affect filament lamps, but lightemitting diode (LED) lamps can appear to flicker if pulse testing is enabled.

Figure 59 - Example Schematic for Two-sensor T-type Muting

<!-- image -->

For simplicity, the power and ground connections of the safety light curtain and muting sensors are not shown. The safety light curtain and muting sensors must have the same reference (24V Com) as the CR30 safety relay for proper operation.

For proper operation, the muting sensors are on (normally closed) when not muting, and the safety light curtain OSSD outputs are also on (the safety light curtain is clear).

Figure 60 - Muting Time for Two-sensor T-type Muting

<!-- image -->

For proper operation, activate/deactivate MS1 and MS2 within the synchronization time, and the safety light curtain must clear before the muting time expires.

The minimum synchronization time is dependent on the connection of the muting sensors and is summarized in Table 5. When connected to the embedded terminals (00…11), you must maintain at least 50-ms delay for the most reliable operation. When the muting sensors are connected to a plug-in module, the synchronization delay must be at least 150 ms.

Table 5 - Minimum Synchronization Times

| Muting Sensor Connection Minimum Synchronization Time    |
|----------------------------------------------------------|
| Connected to embedded terminals 00…17 50 ms              |
| Connected to Plug-in module terminals Px_00…Px_03 150 ms |

<!-- image -->

The synchronization time also depends on the input filter time settings for the muting sensor inputs.

Synchronization time (total) = 2 x Input Filter Time + Synch Time

Table 6 shows the muting and synchronization times that are selectable in the Connected Components Workbench software. These times are linked. For example, if you select a 10-s muting time, then the synchronization time between MS1 and MS2 is 3 s. To use a synchronization time of 6 s, you must select a 60-s muting time.

Table 6 - Muting and Synchronization Timing Selections

|                                      | Muting Time Synchronization Time Muting Time Synchronization Time   |
|--------------------------------------|---------------------------------------------------------------------|
|                                      | 10 s 3 s 900 s (15 min) 90 s                                        |
|                                      | 20 s 3 s 1800 s (30 min) 180 s (3 min)                              |
|                                      | 30 s 3 s 3600 s (1 hr) 180 s (3 min)                                |
|                                      | 60 s (1 min) 6 s 28,800 s (8 hr) 180 s (3 min)                      |
| 300 s (5 min) 30 s Infinite Infinite |                                                                     |

If the synchronization time is exceeded, the Fault status indicator and the muting output flash. In the Connected Components Workbench software, the Muting Safety Monitoring Function turns red and the Mute Lamp flashes green. If the material is backed away from the sensors, the fault is cleared and the muting lamp turns off. If the material proceeds to break the safety light curtain, the output of the Muting Safety Monitoring Function turns off. The Fault status indicator and Mute continue to flash. Use the muting override command to turn on the output of the Safety Monitoring Function temporarily and clear the material from the safety light curtain and muting sensors. The fault condition is cleared.

## Two-sensor L-type Muting

The sensors and safety light curtain form the shape of the letter L, when viewed from the side. The muting sensors (MS) are mounted on one side of the safety light curtain (LC).

Figure 61 - Two-sensor L-type Muting Arrangement

<!-- image -->

The material must first break MS1, then MS2 and then the safety light curtain. As the material progresses, the material must clear MS1 and then MS2. The muting lamp turns on and the safety light curtain is muted after MS2 is blocked. The conveyor can only move one direction.

## IMPORTANT

Only use the 2L muting arrangement for material that exits the hazardous area. Do not use the 2L muting arrangement for material that enters the hazardous area.

In the example below, the OSSD outputs of the safety light curtain are connected to terminals 00 and 01. The two muting sensors are connected to terminals 02 and 03. The momentary, normally open override switch is connected between terminals 12 to 04 to take advantage of pulse testing. Contactor K1 and K2, which provide power to the conveyor (and other hazards if necessary), are connected to terminals 18 and 19.

The muting lamp connects to terminal 13; this terminal must be configured with no pulse testing. Pulse testing does not affect filament lamps, but lightemitting diode (LED) lamps can appear to flicker if pulse testing is enabled.

Figure 62 - Example Schematic for Two-sensor L-type Muting

<!-- image -->

For simplicity, the power and ground connections of the safety light curtain and muting sensors are not shown. The safety light curtain and muting sensors must have the same reference (24V Com) as the CR30 safety relay for proper operation.

For proper operation, the muting sensors are on (normally closed) when not muting, and the safety light curtain OSSD outputs are also on (the safety light curtain is clear).

Figure 63 - Muting Time for Two-sensor L-type Muting

<!-- image -->

Table 7 shows the muting and synchronization times that are selectable in the Connected Components Workbench software. These times are selected independently. For example, you can select two-minute muting time, a 500-ms synchronization time between MS1 and MS2, and a 1000-ms synchronization time between MS2 and the safety light curtain.

<!-- image -->

The synchronization time also depends on the input filter time settings for the muting sensor inputs.

Synchronization time (total) = 2 x Input Filter Time + Synch Time

Table 7 - Muting and Synchronization Times for 2L Muting

Muting Time Units Available Values Synchronization Time Available Values

Seconds 1…59 MS1 to MS2

Minutes 1…59 MS2 to LC

| Hours 1…23   |
|--------------|
| Days 1…10    |

## Four-sensor Muting

The sensors and safety light curtain form the shape of an upside down T, when viewed from the side. Two muting sensors (MS) are mounted on either side of the safety light curtain (LC).

Figure 64 - Four-sensor Muting

<!-- image -->

The material can travel in either direction; which breaks MS1 first and MS4 last or breaks MS4 first and MS1 last. The muting lamp turns on and the safety light curtain is muted after the second sensor is blocked. The object must be large enough to break all four sensors.

In the example below, the OSSD outputs of the safety light curtain are connected to terminals 00 and 01. The four muting sensors are connected to terminals 02 to 05. The momentary, normally open override switch is connected between terminals 12 to 06 to take advantage of pulse testing. Contactor K1 and K2, which provide power to the conveyor (and other hazards if necessary), are connected to terminals 18 and 19.

The muting lamp is connected to terminal 13; this terminal must be configured with no pulse testing. Pulse testing does not affect filament lamps, but lightemitting diode (LED) lamps can appear to flicker if pulse testing is enabled.

| 50…10,000 ms in 50 ms increments   |
|------------------------------------|
| 50…10,000 ms in 50 ms increments   |

Figure 65 - Example Schematic for Four-sensor Muting

<!-- image -->

For simplicity, the power and ground connections of the safety light curtain and muting sensors are not shown. The safety light curtain and muting sensors must have the same reference (24V Com) as the CR30 safety relay for proper operation.

For proper operation, the muting sensors are on (normally closed) when not muting, and the safety light curtain OSSD outputs are also on (the safety light curtain is clear).

Figure 66 - Muting Time for Four-sensor Muting

<!-- image -->

Table 8 on page 71 shows the muting and synchronization times that are selectable in the Connected Components Workbench software. These times are linked. For example, if you select a 10-s muting time, then the synchronization time between MS1 and MS2 is 3 s. To use a synchronization time of 6 s, you must select a 60-s muting time.

<!-- image -->

The synchronization time also depends on the input filter time settings for the muting sensor inputs.

Synchronization time (total) = 2 x Input Filter Time + Synch Time

## Reset

Table 8 - Muting and Synchronization Times for Four-sensor Muting

| Muting Time Synchronization Time   |
|------------------------------------|
| 10 s 3 s                           |
| 20 s 3 s                           |
| 30 s 3 s                           |
| 60 s (1 min) 6 s                   |
| 300 s (5 min) 30 s                 |
| 900 s (15 min) 90 s                |
| 1800 s (30 min) 180 s (3 min)      |
| 3600 s (1 hr) 180 s (3 min)        |
| 28,800 s (8 hr) 180 s (3 min)      |
| Infinite Infinite                  |

## Muting Lamp

The muting lamp shows four states.

- Off – safety light curtain is not muted.
- On – safety light curtain is muted.
- 1 Hz flash rate – muting sequence fault.
- 3 Hz flash rate – muting is overridden (the Override input is on).

The muting lamp is not monitored. If the lamp burns out, the muting function continues to work properly.

The reset block is used in safety functions that require a manual intervention to turn on the safety system.

Figure 67 - Reset Function Block

<!-- image -->

To help prevent inadvertent actuation of the reset block, the reset requires a leading and trailing edge within a specific time frame. The pulse width must be between 250…3000 ms. If the pulse width is too short or too long, the reset function is not executed.

## Restart

## Figure 68 - Reset Timing

<!-- image -->

The reset block is a safety monitoring function in the Connected Components Workbench software. For a valid reset operation, according to the requirements specified in the approved safety concept, you must use the default reset timing and leave the input filter setting 0.

The filter setting is enabled in Connected Components Workbench software versions previous to Rev 7. A filter time setting greater than 0 extends the Reset Timing by 2 x Filter Time.

The reset input signal can come from either one input wiring terminal or over the Modbus communication input. The available input selections are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)
- P1\_00…P1\_03 (plug-in 1 terminals 00…03)
- P2\_00…P2\_03 (plug-in 2 terminals 00…03)
- SP\_00…SP\_15 (Modbus inputs 00…15)

## Figure 69 - Wiring Connection for a Reset Signal to Terminal 00

<!-- image -->

The reset block works with one or more output blocks. When an output block requires a manual reset, the Connected Components Workbench software shows all available reset inputs that can be used.

The Restart function works with an AND or OR logic block in logic level A and logic level B. When all inputs are satisfied and when the restart input is exercised, the restart function is effective. If the restart function is already effective, the restart input has no effect.

You can only use the restart with one AND or OR logic block.

Figure 70 - Restart Function Block

<!-- image -->

The Restart Function requires a leading and trailing edge within a specific time frame. The pulse width must be between 250…3000 ms. If the pulse width is too short or too long, the Restart function is not executed.

<!-- image -->

The available input selections for the Restart are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)
- P1\_00…P1\_03 (plug-in 1 terminals 00…03)
- P2\_00…P2\_03 (plug-in 2 terminals 00…03)
- SP\_00…SP\_15 (Modbus inputs 00…15)

For a valid Restart operation, according to the requirements specified in the approved safety concept, you must use the default Restart timing and leave the input filter setting 0.

The filter setting is enabled in Connected Components Workbench software versions smaller than Rev 7. A filter time setting greater than 0 extends the Reset Timing by 2 x Filter Time.

Figure 72 - Wiring Connection for a Restart Signal to Terminal 02 with Inputs on Terminals 00 and 01

<!-- image -->

## Safety Mat

Four-wire safety mats can connect to the CR30 safety relay. The four wires create two channels. When the safety mat is stepped on, it creates a short circuit between channel 1 and 2. To detect the short circuit, input pulse testing is used. The mats must connect to the input test pulses.

Figure 73 - Safety Mat Function Block

<!-- image -->

The safety mat can connect to the following terminals:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can use the default Discrepancy Time and Input Filter or choose to modify these settings.

For input test pulses, terminals 12…17 are available. The Connected Components Workbench software automatically selects another test pulse pattern for each input.

An example schematic shows a safety mat that is connected to terminals 0 and 1. The mat uses test pulses that are generated at terminals 12 and 13.

Figure 74 - Example Schematic for a Safety Mat

<!-- image -->

## SensaGuard

The SensaGuard™ function block sets the parameters for interlocks having dual OSSD outputs. In the Connected Components Workbench software, click and drag (or double-click) the block to an available Safety Monitoring Function spot. Use this block for other devices with OSSD outputs.

Figure 75 - SensaGuard Function Block

<!-- image -->

The available input selections for the SensaGuard inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can use the default Discrepancy Tests on page 47 and Input Filter on page 45 or choose to modify these settings.

Figure 76 - Example Schematic of a SensaGuard Interlock

<!-- image -->

## Single Wire Safety Input

When configured for this type of input, the CR30 safety relay expects a Single Wire Safety (SWS) input signal from a GSR safety relay or a safeguarding device that has an SWS output signal. The GSR safety relay family includes the CI, SI, DI, DIS, GLP, GLT, EM, and EMD modules. Each of these modules provides the SWS signal on terminal L11.

Figure 77 - Single Wire Safety Input Function Block

<!-- image -->

Only terminals 10 and 11 of the CR30 safety relay can be configured to receive the SWS signal.

- EI\_10…EI\_11 (embedded input terminals 10…11)

The SWS signal is a long pulse followed by a short pulse, which is repeated while the signal is active. The SWS is active when the safety outputs of a GSR safety relay are on. When the SWS is inactive, the SWS signal is 0V. The timing and voltage characteristics of the SWS waveform are shown in Figure 78 .

Figure 78 - SWS Waveform

<!-- image -->

Figure 79 shows an example schematic of the connection of the SWS from other modules in the GSR family of safety relays. The CR30 safety relay and GSR modules must connect to the same 24V common.

Figure 79 - SWS Connection Schematic

<!-- image -->

## Status In

The Status In is a safety monitoring function that can detect either a ready-for-reset on an output function block or a fault present status on a safety monitoring function block.

Figure 80 - Status In Function Block

<!-- image -->

Ready-for-reset - In the Type field, select the SOF RR option. Then, assign an input to the desired safety output block.

## Example 1 - Ready for Reset

In Figure 81, the Status\_In\_1 block is monitoring the safety output function block SOF1. When the E-stop is closed, the SOF1 block is waiting for reset. The SMF2 block detects this status and sends a command to SOF2 to turn on its output. SOF2 is configured to pulse, so it flashes its output.

Figure 81 - Ready-for-reset Example

<!-- image -->

## Example 2 - Fault Present

In Figure 82, the Status\_In\_1 block is monitoring the SMF1, SMF2, and SOF1 blocks for faults. If a fault occurs on any of these blocks, the Status\_In\_1 block sends a command to the Status\_Out\_1 block, and the Status\_Out\_1 block pulses its output. The status in block reports that the SMF1 block has a fault.

Figure 82 - Fault Present Example

<!-- image -->

## Two-hand Control

The CR30 safety relay can be configured to operate in two different types of two-hand control, which are specified in ISO 13851. The two types are:

- Type IIIA (for low-risk safety systems)
- Type IIIC (for high-risk safety systems)

Use mechanically palm-operated buttons (Bulletin 800P) or the electronic output push buttons (Bulletin 800Z Zero-Force Touch Buttons™) as actuation devices for two-hand control. The CR30 safety relay requires two buttons to be actuated simultaneously and maintained to turn on the two-hand safety monitoring function. To meet the simultaneity requirement, the two buttons must actuate within 500 ms of each other.

Figure 83 - Two-Hand Control Function Block

<!-- image -->

The two-hand controls can connect to the following terminals.

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can use the default Input Filter or choose to modify these settings.

When test pulses are used, the Connected Components Workbench software automatically selects another test pulse pattern for each input. The two-hand control can use input test pulses from the following terminals:

- MP\_12…MP\_17 (multi-purpose terminals 12…17)

## Type IIIA Two-hand Control

The Type IIIA uses only one normally open contact for each hand. You can build this configuration with or without the use of test pulses. The test pulses provide short circuit fault detect between channels and between channel and 24V.

Figure 84 - Example Wiring Connection for a Type IIIA Two-hand Control without Test Pulses

<!-- image -->

Figure 85 - Wiring Connection for a Type IIIA Two-hand Control with the Test Pulses

<!-- image -->

## Type IIIC Two-Hand Control

The Type IIIC uses a normally open and a normally closed contact for each hand.

Figure 86 - Example Wiring Connection for a Type IIIC Two-hand Control without Test Pulses

<!-- image -->

When test pulses are used, the CR30 safety relay detects a short from Channel 1 to Channel 2 after 3.7 seconds and turn off the output. To clear the fault, release both buttons.

Figure 87 - Wiring Connection for a Type IIIC Two-hand Control with Test Pulses

<!-- image -->

The timing diagram for the two-hand control is shown in Figure 88. The Type IIIA uses only the N.O. contact of the button. The Type IIIC uses both the N.C. and the N.O. contacts.

<!-- image -->

Figure 88 - Two-hand Control Timing Diagram

|    |                                                                              |    | Description Description                                                      |
|----|------------------------------------------------------------------------------|----|------------------------------------------------------------------------------|
|    | 1 Hand 1 button is pressed. 5 Hand 2 button is pressed.                      |    |                                                                              |
| 2  | Hand 2 button must be pressed within 500 ms for the output logic to turn on. | 6  | Hand 1 button must be pressed within 500 ms for the output logic to turn on. |
| 3  | Releasing either hand button causes the logic output to turn off.            | 7  | Releasing either hand button causes the logic output to turn off.            |
| 4  | Both hand buttons must be released to start a new cycle.                     | 8  | Both hand buttons must be released to start a new cycle.                     |

## Alternate Device

The alternate device provides the flexibility to create other types of input monitoring blocks. Use this block for the following types of input functions:

| • Single-channel OSSD • Dual-channel OSSD • Three-channel N.C.   |                                                    |                      |
|------------------------------------------------------------------|----------------------------------------------------|----------------------|
| • Single-channel N.C.                                            | • Dual-channel 2 N.C. • Dual-channel 1 N.C./1 N.O. | • Three-channel OSSD |

Figure 89 - Alternate Device Function Block

<!-- image -->

## Single-channel

Single-channel safety monitoring functions require only one connection to an input terminal. Only use the single-channel input in low-risk safety systems.

The available input terminals are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can use the default Input Filter or choose to modify this setting.

When test pulses are used, the Connected Components Workbench software automatically selects the test pulse pattern. The single-channel N.C. can use input test pulses from the following terminals:

- MP\_12…MP\_17 (multi-purpose terminals 12…17)

Figure 90 - Example Schematic for Single-channel N.C. without Test Pulse

<!-- image -->

Figure 91 - Example Schematic for Single-Channel N.C. with Test Pulse

<!-- image -->

Figure 92 - Example Schematic for Single-channel OSSD

<!-- image -->

## Dual-channel

Dual-channel safety monitoring functions require two independent circuit connections to the CR30 safety relay. Dual-channel inputs are used for medium and high risk applications.

You can modify the number and types of inputs:

- 2 N.C.
- 2 OSSD
- 1 N.C./1 N.O.

The available input selections for the dual-channel OSSD and two N.C. inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

The available input selections for the N.O. contact are:

- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can set pulse testing to 1 Source, 2 Sources, or Disabled. When 1 Source or 2 Sources is selected, the Connected Components Workbench software assigns the next available test sources automatically. You can modify the sources afterward.

You can use the default Discrepancy Time and Input Filter or choose to modify these settings.

The two terminals do not necessarily need to be consecutive.

Figure 93 - Example Schematic for 2 N.C. without Test Pulse

<!-- image -->

Figure 94 - Example Schematic for 2 N.C. with Two Test Pulses Sources

<!-- image -->

## Dual-channel OSSD

Safeguarding devices with OSSD outputs generate their own test pulses to detect for short circuit conditions or have other methods of detecting short circuit conditions. When configured for dual-channel OSSD, the CR30 safety relay ignores the test pulses.

Table 9 shows examples of products that use dual-channel OSSD outputs:

Table 9 - Products Using Dual-channel OSSD Outputs

| Product Types Product Name                                   |
|--------------------------------------------------------------|
| Safety light curtains GuardShield™                           |
| Laser scanners SafeZone™, SafeZone Multizone                 |
| Gate interlocks SensaGuard, SensaGuard with Integrated Latch |
| Guard locking interlocks TLS-ZR, 440G-LZ                     |

The safeguarding device detects short circuits, and the safeguarding device turns off its safety outputs. Devices with OSSD outputs can operate in highrisk applications.

Figure 95 - Example Schematic for Two OSSD

<!-- image -->

## Dual-channel N.C./N.O.

The N.C./N.O. configuration applies the diversity concepts, where one contact is open and the other contact is closed. The contact, while in an open state, cannot be welded closed. The CR30 safety relay turns off its safety outputs when either channel changes state. Both channels must change state for proper performance.

Figure 96 - Example Schematic for N.C./N.O. without Test Pulse

<!-- image -->

Figure 97 - Example Schematic for N.C./N.O. with One Test Pulse

<!-- image -->

Figure 98 - Example Schematic for N.C./N.O. with Two Test Pulses

<!-- image -->

If a short circuit occurs on terminal 12 to 24V, the CR30 safety relay turns off its safety outputs within 35 ms. Remove the fault and cycle the contacts to clear the fault.

If a short circuit occurs on terminal 12 to ground, the CR30 safety relay turns off its safety outputs within 3.3 seconds. Remove the fault and cycle the contacts to clear the fault.

If a short circuit occurs from terminal 12 to terminal 13, the CR30 safety relay turns off its safety outputs within 35 ms. Remove the fault and cycle the contacts to clear the fault.

## Three-channel

The CR30 safety relay can accept three channels into one safety monitoring function. All three inputs must be HI to satisfy the input. If any one of the inputs goes LO, the output of safety monitoring function goes LO and turns off its associated output devices. The three N.C. inputs can operate without input test pulses, with one input test pulse, with only two input test pulses, or with three input test pulses.

The available input selections for the three channel inputs are:

- EI\_00…EI\_11 (embedded input terminals 00…11)
- MP\_12…MP\_17 (multi-purpose terminals 12…17)

You can set pulse testing to 1 Source, 2 Sources, 3 Sources, or Disabled. When 1 Source, 2 Sources, or 3 Sources are selected, the Connected Components Workbench software assigns the next available test sources automatically. You can modify the sources afterward.

You can use the default Discrepancy Time and Input Filter or choose to modify these settings.

The three terminals do not necessarily need to be consecutive.

Figure 99 - Example Schematic for Three N.C. without Test Pulses

<!-- image -->

Figure 100 - Example Schematic for Three N.C. with One Test Pulse Source

<!-- image -->

Figure 101 - Example Schematic for Three N.C. with Three Test Pulse Sources

<!-- image -->

## Output Loop

Figure 102 - Example Schematic for Three OSSD

<!-- image -->

The output loop is a single-channel safety monitoring input block that uses the logical state of a Safety Output Function (SOF) as its input. This function block eliminates the need to connect a wire from an output terminal and feed it back into an input terminal. The CR30 safety relay completes the loop internally.

IMPORTANT

The use of the output loop in a safety function requires an additional 25 ms of response time.

In Figure 103, the output loop is selected from the Toolbox. Safety output function block 1 (SOF\_01) is the input to safety monitoring function 3 (SMF3).

Figure 103 - Example Output Loop Function Block

<!-- image -->

Any single SOF can be the input on multiple output-loop safety-monitoring functions.

During online monitoring, the input terminal state must be the same for the output loop function and the referenced output condition of the SOF.

If Auto-assign is enabled, the default value is the top SOF instance.

The input terminal and output must be defined for the output loop function. The input terminal list contains all instances of SOFs. The output terminal of an output loop cannot be an input condition to a safety output function monitored by that output loop function block.

## Logic Levels A and B

The Connected Components Workbench™ software has two levels that allow you to apply simple logic to create more sophisticated safety systems. The logic levels are labeled A and B on the software workspace. The logic functions are available in the Toolbox.

Figure 104 - Logic Levels A and B on the Connected Components Workbench Workspace

<!-- image -->

## Pass Through

When a logic level is not used, the Connected Components Workbench software automatically creates a pass through block.

<!-- image -->

## AND

OR

XOR

The AND block accepts 2…24 inputs. When all inputs are HI, the output of the block is HI. If any of the inputs is LO, the output of the block is LO.

The AND block is often used when multiple E-stops must be released and multiple safety gates must be closed for the safety system to be energized.

Table 10 - AND Logic Table for Two Inputs

| Logic Block Input 1 Input 2 Output   |     |
|--------------------------------------|-----|
| Logic Level A LLA1 D AND             | 000 |
| Logic Level A LLA1 D AND             | 010 |
| Logic Level A LLA1 D AND             | 100 |
| Inputs: 2                            | 111 |

The OR block accepts 2…24 inputs. If any of the inputs are HI, the output of the block is HI. If all inputs go LO, the output of the block goes LO.

The OR block is often used with enabling devices.

Table 11 - OR Logic Table for Two Inputs

| Logic Block Input 1 Input 2 Output   |     |
|--------------------------------------|-----|
| Logic Level A LLA1 D OR              | 000 |
| Logic Level A LLA1 D OR              | 011 |
| Logic Level A LLA1 D OR              | 101 |
| Inputs: 2                            | 111 |

The XOR block accepts 2…24 inputs. The output of the XOR block is HI when any input is HI. The output is LO when multiple inputs are HI or if all inputs are LO.

Table 12 - XOR Logic Table for Two Inputs

| Logic Block Input 1 Input 2 Output   |     |
|--------------------------------------|-----|
| Logic Level A LLA1 D XOR             | 000 |
| Logic Level A LLA1 D XOR             | 011 |
| Logic Level A LLA1 D XOR             | 101 |
| Inputs: 2                            | 110 |

## NAND

## NOR

## NOT

## AND with Restart

The NAND block accepts 2…24 inputs. The NAND performs the opposite of an AND block. The output of the NAND block is LO when all inputs are HI. When any input is LO, the output is HI.

Table 13 - NAND Logic Table for Two Inputs

| Logic Block Input 1 Input 2 Output   |     |
|--------------------------------------|-----|
| Logic Level A LLA1 NAND              | 001 |
| Logic Level A LLA1 NAND              | 011 |
| Logic Level A LLA1 NAND              | 101 |
| Inputs: 2                            | 110 |

The NOR block performs the opposite of the OR block. When any input is HI, the output is LO. When all inputs are LO, the output is HI.

Table 14 - NOR Logic Table for Two Inputs

| Logic Block Input 1 Input 2 Output   |     |
|--------------------------------------|-----|
| Logic Level A LLA1 NOR               | 001 |
| Logic Level A LLA1 NOR               | 010 |
| Logic Level A LLA1 NOR               | 100 |
| Inputs: 2                            | 110 |

The NOT block accepts only one input. The NOT inverts the input signal. When the input is LO, the output is HI. When the input is HI, the output is LO.

Table 15 - NOT Logic Table for Two Inputs

<!-- image -->

| Logic Block Input Output   |     |
|----------------------------|-----|
| Logic LevelA LLA1 NOT      | 0 1 |
|                            | 1 0 |

The AND with restart accepts 1…24 inputs and requires a restart input. All inputs must be HI when the Restart button is pressed.

The Connected Components Workbench software automatically recognizes the restart function blocks and allows you to select one. Once selected, the Restart is no longer available for other logic blocks.

Figure 105 shows an example with a gate switch and a safety light curtain. Both the gate must be closed and the safety light curtain clear. Then, the Restart input must be pressed. The output of the logic block goes HI on the trailing edge of the restart signal.

Figure 105 - Example of AND with Restart

<!-- image -->

Figure 106 - Logic of the Restart Function with Two Input AND

<!-- image -->

The timing diagram shows how the output of the logic block responds to the input signals and the Restart signal. Both inputs must be HI when the restart signal occurs for the output to go HI. If any of the inputs go LO, the output goes LO.

Figure 107 - AND with Restart Timing Diagram

<!-- image -->

## OR with Restart

The OR with restart accepts 2…24 inputs and requires a restart input. At least one input must be HI when the Restart button is pressed.

The Connected Components Workbench software automatically recognizes the restart function blocks and allows you to select one. Once selected, the restart is no longer available for other logic blocks.

Figure 108 shows an example with a gate switch and a safety light curtain. Either the gate must be closed or the safety light curtain clear. Then, the restart input must be pressed. The output of the logic block goes HI on the trailing edge of the restart signal.

Figure 108 - Example OR with Restart

<!-- image -->

Figure 109 - Logic of the Restart Function with Two Input OR

<!-- image -->

The timing diagram shows how the output of the logic block responds to the input signals and the restart signal. Either or both inputs can be HI when the restart signal occurs for the output to go HI. If all inputs go LO, the output goes LO.

Figure 110 - OR with Restart Timing Diagram

<!-- image -->

## Nesting

Nesting allows you to create more than two logic levels effectively. Nesting is accomplished by connecting the output of a logic level function block to the first input of a logic level immediately below it (in the same column). Nesting can be performed in logic column A or logic column B, but nesting cannot cross-over from column A to column B. The following logic level function blocks support Nesting: AND, OR, XOR, NAND, NOR, AND with restart, and OR with restart.

## IMPORTANT This feature is available in firmware revision 9 or later.

Use the following procedure to nest a logic level A function block. Figure 111 shows the results.

1. Add an AND function block in LLA1.
2. Add an OR function block in LLA2 (immediately below LLA1).
3. On the LLA1 function block, click the output.
4. On the LLA2 function block, place the cursor over the second input. Notice that the cursor becomes the forbidden style, meaning that the connection cannot be made to the second input.
5. On the LLA2 function block, place the cursor over the first input. Notice that the cursor becomes the hand style, meaning that the connection can be made to the first input.
6. On the LLA2function block, click the first input. LLA1 function block output connects to the LLA2 function block first input.
7. LLA2 function block becomes a nested OR.

Figure 111 - Steps to Create a Nesting Block

<!-- image -->

To delete a nesting line, you can either:

1. Right-click on the line that connects the output to the input, and select Delete from the context menu, or
2. Click the line and press the Delete key.

## Invert

## Reset Set Flip Flop

Inverting gives you the ability to reverse the state of an input or output without using a NOT function block. Inverting inputs can be applied to the AND, NAND, OR, NOR, XOR, AND with restart, OR with restart, and the RS Flip Flop logic functions. Inverting outputs can be applied to XOR, AND with restart, OR with restart, and the RS Flip Flop logic functions.

To invert, right-click the input or output connection and click Invert. When inverted, the connection point is hollow. To remove the invert, right-click the input and click Revert. When reverted, the connection point becomes solid.

Figure 112 shows an example of an inverted input and a reverted input. The same process can be applied to the output connection.

Figure 112 - Invert or Revert Input Connection Points

<!-- image -->

A reset set flip flop (RS-FF) function can be used in logic levels LLA and LLB. This function is useful when a momentary input must be used as the input signal. You can configure the flip-flop to invert the Set and/or reset inputs and/or the output.

Figure 113 - Example Selection of the RS Flip Flop to LLA1

<!-- image -->

Figure 114 on page 94 shows the timing diagram for the RS Flip-Flop.

1. When the Set input goes HI and the reset input is LO, the output turns on.
2. If the Set input goes LO, the output remains on.
3. When the reset input goes HI and the Set input is LO, the output turns off.
4. If the reset input goes HI while the output is off, the output remains off.

5. If the reset input goes HI while the set input is HI, the output turns off.
6. If the set input goes LO while the reset remains HI, the output remains off.
7. If the reset input goes LO while set input remains HI, the output turns on.

Figure 114 - Timing Diagram for the RS Flip Flop

<!-- image -->

## Input Connection

## Feedback

## Reset

## Timing

## Output Connections

## Safety Outputs

The safety output blocks are the fourth stage of the configuration. Many of the blocks have common features.

Each output block has one input connection. This input connection can be connected to only logic level B blocks.

The immediate off, on delay, and off delay blocks have a feedback parameter. To use the feedback parameter, a feedback input block must be declared. If a feedback input block is not available, the feedback parameter is set to None, and can be considered to be always HI.

The reset parameter must be set to either automatic or manual.

- If set to automatic, the output turns on when the input that is received from the logic level B block is HI.
- If the reset is set to manual, a reset input block must be declared. Before the Reset button is pressed, the input that is received from the logic level B block must be HI. Then, the output turns on if the Reset button must be pressed and held for at least 0.25 s and released within 3 s.

Timing is used in the on delay, off delay, and jog functions.

The timing can be set between 50…300,000 ms (5 minutes) in 50 ms increments.

The output of the block can be connected to one or more of the following wiring terminals:

- 12…17 Multi-purpose (MP)
- 18…21 Embedded Output (EO)
- 00…03 plug-in 1 module (not safety rated)
- 00…03 plug-in 2 module (not safety rated)

The multi-purpose outputs can be configured to operate with pulse test (PT) or without test pulses (No PT). The embedded terminals always operate with test pulses. Terminals 20 and 21 can be configured as single wire safety (SWS) output.

<!-- image -->

WARNING: The plug-in outputs must only be used for non-safety rated purposes.

<!-- image -->

## Immediate Off

The immediate off block is used to turn off output terminals immediately upon a demand that is placed on a safety function.

Figure 115 shows the immediate off output block that is connected to an E-stop block through logic level LLB1. The feedback signal is provided by SMF2 and manual reset by SMF3. The output is connected to:

- Terminals 18 and 19 for dual-channel safety switching of the machine hazards.
- Plug-in 1 terminal 00 for status indication.

## Figure 115 - Immediate Off Configuration

<!-- image -->

## On Delay

The on delay block turns on the output after the specified time delay expires.

Figure 116 shows the on delay output block that is connected to an E-stop block through logic level LLB1. The feedback signal is provided by SMF2 and manual reset by SMF3. The time delay is set to 2 minutes 8 seconds. The output turns on 1000 ms (20 x 50 ms) after the Reset button is released. The output is connected to:

- Terminals 18 and 19 for dual-channel safety switching of the machine hazards.
- Terminal 20, which is configured as one wire safety (SWS) output.
- Plug-in 2 terminal 00 for status indication.

## Figure 116 - On Delay Configuration

<!-- image -->

## Off Delay

The off delay block turns off the output after the specified time delay expires.

The retriggerable parameter can be set to enabled or disabled.

- When enabled, the input to the off delay block can go HI again during the timing cycle, and the output remains HI.
- When disabled, the timing cycle runs to completion, regardless of changes to the input.

Figure 117 shows the off delay output block that is connected to a gate switch block through logic level LLB1. The feedback signal is provided by SMF2 and manual reset by SMF3. The time delay is set to 1 minute, 5 seconds, and 400 milliseconds. The output turns off after the delay time has expired. The output is connected to:

- Terminals 18 and 19 for dual-channel safety switching of the machine hazards.
- Terminal 20, which is configured as one wire safety (SWS) output.
- Terminal 00 of Plug-in 2 for status reporting

## Figure 117 - Off Delay Configuration

<!-- image -->

## Jog

The jog block turns on the output for a specified duration while the jog input is held HI. If the jog input goes LO, the output immediately turns off.

Figure 118 shows the jog output block that is connected to an enabling switch block through logic level LLB1. The reset is set to automatic. The max jog time is set to 2 minutes, 5 seconds, and 250 milliseconds. After this time expires, the outputs turn off. The output is connected to:

- Terminals 18 and 19 for dual-channel safety switching of the machine hazards.
- Terminal 20, which is configured as one wire safety (SWS) output.
- Plug-in 1 terminal 03 for status indication.

## Figure 118 - Jog Configuration

<!-- image -->

## Muting Lamp

The muting lamp block works with the muting safety monitoring function.

The muting lamp is not monitored. If the lamp burns out or becomes disconnected, the muting function continues to function properly.

Figure 119 shows the muting lamp output block connected to the mute function in SMF1. The output is connected to:

- Terminal 14, a multi-purpose terminal with no pulse testing (No PT).
- Plug-in 1 terminal 00 for more status indication.
- The muting lamp must be connected to terminals without pulse testing. Pulse testing does not affect filament lamps, but light-emitting diode (LED) lamps can appear to flicker if pulse testing is enabled.

Figure 119 - Muting Lamp Configuration

<!-- image -->

## Status Out

The status out block provides either a steady output or a pulsing output. The Pulse type can be changed to on or off by a clicking the on/off field. The pulse is a 1 Hz frequency with a 50% duty cycle.

Figure 120 - Status Out Function Block

<!-- image -->

See Figure 81 on page 77 and Figure 82 on page 78 for examples of how the status out block works with the status in block. Figure 80 on page 77 shows how the status out block is used with other functions. In this example, the Status\_Out\_1 block pulses its output as soon as the E-stop button is pressed. When the E-stop button is released, the Status\_Out\_1 block turns off.

Figure 121 - Example Usage of the Status Out Block

<!-- image -->

## Insert Module into Controller

## Micro800 Plug-in Modules

The CR30 safety relay accepts up to two plug-in I/O modules. Table 16 shows which modules are available for the firmware that is installed in the CR30 safety relay.

Table 16 - Plug-in Modules for the CR30 Safety Relay

| Plug-in Modules Description Firmware Revision                 |
|---------------------------------------------------------------|
| 2080-IQ4OB4 4 sinking inputs + 4 sourcing outputs 6 and later |
| 2080-IQ4 4 sinking inputs 7 and later                         |
| 2080-OB4 4 sourcing outputs 7 and later                       |
| 2080-OW4I 4 electromechanical relay outputs 7 and later       |

<!-- image -->

ATTENTION: The input and output signals of these modules are not safety rated. They must only be used for standard control functions.

Follow the instructions to insert and secure the plug-in module to the controller.

Figure 122 - Plug-in Module

<!-- image -->

1. Position the plug-in module. Face the terminal block to the front of the controller as shown.
2. Snap the module into the module bay.
3. Tighten the 10…12 mm (0.39…0.47 in.) M3 self-tapping screw to 0.2 N·m (1.48 lb·in) torque.

<!-- image -->

## 2080-IQ4OB4 Plug-in Module

The 2080-IQ4OB4 plug-in module has four sinking inputs and four sourcing outputs. The COM connection B3 is internally connected to A3. This COM connection is for the inputs (without it, the inputs do not turn on). Terminal B4 must be connected to the +24V supply to provide power to the outputs terminals O-00…O-03.

Figure 123 - 2080-IQ4OB4 Plug-in Module Schematic Showing Four Standard Input Signals

<!-- image -->

Figure 124 - 2080-IQ4OB4 Plug-in Module Schematic Showing Four Standard Output Signals

<!-- image -->

## 2080-IQ4 Plug-in Module

The 2080-IQ4 plug-in module has four sinking inputs. The four COM connections, A3, A4, B3, and B4 are internally connected. At least one COM connection must be connected to 24V Com (without it, the inputs do not turn on).

Figure 125 - 2080-IQ4 Plug-in Module Schematic Showing Four Standard Input Signals

<!-- image -->

## 2080-OB4 Plug-in Module

The 2080-OB4 plug-in module has four sourcing outputs. Terminals B3 and B4 are internally connected; one of these terminals must be connected to +24V DC. Terminals A3 and A4 are internally connected; one of these terminals must be connected to 24V Com.

Figure 126 - 2080-OB4 Plug-in Module Schematic Showing Four Standard Output Signals

<!-- image -->

## 2080-OW4I Plug-in Module

The 2080-OW4I plug-in module has four electromechanical relays with normally open (Form A) contacts.

Figure 127 - 2080-OW4I Plug-in Module Schematic Showing Four Standard Output Signals

<!-- image -->

## Install a Guardmaster 440C-ENET EtherNet/IP Plug-in Module

<!-- image -->

<!-- image -->

## ATTENTION: Environment and enclosure.

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664­1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR 11. Without appropriate precautions, there can be difficulties with electromagnetic compatibility in residential and other environments due to conducted and radiated disturbances.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that are present and appropriately designed to help prevent personal injury that results from accessibility to live parts. The enclosure must have suitable flame-retardant properties to help prevent or minimize the spread of flame, and must comply with a flame spread rating of 5VA, V2, V1, V0 (or equivalent) if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication can contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications. Also see:

- For additional installation requirements, publication 1770-4.1 .
- NEMA 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by different types of enclosures.

## ATTENTION: Help prevent electrostatic discharge.

This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## Installation Summary

Do these steps to install the Ethernet plug-in module.

1. Mount the CR30 safety relay on a DIN rail or panel.
2. Install the plug-in module.

## About the Module

The module provides EtherNet/IP™ connectivity for CR30 safety relays.

Use Figure 128 to identify the external features of your module.

<!-- image -->

Figure 128 - External Features

| Description Description   |                                                                             |
|---------------------------|-----------------------------------------------------------------------------|
|                           | 1 Status indicators 3 Plug-in connector (on opposite side of circuit board) |
|                           | 2 MAC ID label 4 RJ45 (Ethernet) cable connector                            |

Software Requirements

You must have one of the following software versions.

Table 17 - Software Versions

|                                          | Software Description                                         |
|------------------------------------------|--------------------------------------------------------------|
| Studio 5000 Logix Designer® application  | 20 or later Download the Add-on Profile fromrok.auto/support |
| Connected Components Workbench™ software | 8 or later Download the software from rok.auto/pcdc          |

Firmware Requirements

You must have one of the following firmware revisions.

Table 18 - Firmware Revisions

|                 | Module Description                                      |
|-----------------|---------------------------------------------------------|
| 440C-CR30-22BBB | 8.001 or later Download the firmware from rok.auto/pcdc |

## Install the Module

To install the module, follow this procedure.

<!-- image -->

## ATTENTION:

- Do not insert or remove the plug-in module while power is applied, otherwise permanent damage to equipment can occur.
- This plug-in module is not compatible with Micro800™ controllers.
1. Position the plug-in module as shown in Figure 129 .
2. Snap the module into slot 1 of the module bay.
3. Tighten the 10…12 mm (0.39…0.4 in.) M3 self-tapping screw to torque specifications.

Figure 129 - Plug-in Module Positioning

<!-- image -->

## Wire the Ethernet Connector

Use an RJ45 connector to connect to the EtherNet/IP network. Wire the connector as shown.

## Figure 130 - Connector Wiring

<!-- image -->

For detailed EtherNet/IP connection information, see the EtherNet/IP Media Planning and Installation Manual, available from the Open DeviceNet® Vendor Association (ODVA) at http://www.odva.org .

## Grounding Considerations

The grounding and bonding must be of equal potential between all devices in the communication coverage area.

## Connect the Module to the EtherNet/IP Network

Connect the RJ45 connector of the Ethernet cable to the Ethernet port on the bottom of the plug-in module as shown.

Figure 131 - Ethernet Cable Connection

<!-- image -->

## Set the Network Address

The default setting for the CR30 safety relay is DHCP enabled for the Ethernet plug-in. You can set the network Internet Protocol (IP) address two ways.

- Use Dynamic Host Configuration Protocol (DHCP) server.
- Use Rockwell Automation RSLinx® Classic, Studio 5000®, or Connected Components Workbench software.

## Use a DHCP/BOOTP Server

If you do not have a large computer that can act as a boot server, download our DHCP/BOOTP software so you can use a personal computer as a DHCP/ BOOTP server.

To set the network address by using the Rockwell Automation DHCP/BOOTP server, follow these steps.

1. Access the DHCP/BOOTP utility at rok.auto/pcdc .
2. Download the version 2.3.1 DHCP/BOOTP utility.
3. Extract the zipped files to a temporary directory.
4. In the temporary directory, double-click setup.exe to install the DHCP/ BOOTP utility.
5. Run the utility.
6. See Table 19 on page 108, which describes what happens next, depending on whether DHCP/BOOTP is enabled on the module.

Table 19 - DHCP/BOOTP

| If DHCP/BOOTP is Description   |                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Enabled                        | Asks for an address from a DHCP/BOOTP server. The server also assigns other Transport Control Protocol (TCP) parameters. |
| Not enabled                    | Uses the IP address (along with other TCP configurable parameters) stored in nonvolatile memory.                         |

Use RSLinx Classic, Studio 5000, or Connected Components Workbench Software

Follow the procedures that are outlined in the online help that accompanies this software to set the network address.

## Status Indicators

The three status indicators on the module provide diagnostic information about the module and its connections to the network.

Table 20 - Status Indicators

|     |                     | Indicator Status Description                                                                                                                                                                                                |
|-----|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MS  | Off                 | The plug-in module does not have power. Check the safety relay power supply.                                                                                                                                                |
| MS  | Flashing green      | The port is in Standby mode; it does not have an IP address. Verify that the DHCP server is running.                                                                                                                        |
| MS  |                     | Green The port is operating correctly. No action is required.                                                                                                                                                               |
| MS  | Red                 | The safety relay is holding the port in reset or the safety relay has faulted. Clear the fault. If the fault does not clear, replace the plug-in.                                                                           |
| MS  | Flashing red/ green | The module is performing its power-up self-test. No action is required.                                                                                                                                                     |
| NS  | Off                 | The port is not initialized; it does not have an IP address. Verify that the DHCP server is running.                                                                                                                        |
| NS  | Flashing green      | The port has an IP address, but no CIP™ connections are established. If no connections are configured, no action is required. If connections are configured, check the connection originator for connection error code.     |
| NS  | Green               | The port has an IP address and CIP connections (Class 1 or Class 3) are established. No action is required.                                                                                                                 |
| NS  | Red                 | Duplicate IP - The device has detected that its IP address is being used by another device in the network. Change the devices IP address.                                                                                   |
| NS  | Flashing red/ green | The port is performing its power-up self-test. No action is required.                                                                                                                                                       |
| LNK | Off                 | The port is not connected to a powered Ethernet device. Therefore, the safety relay cannot communicate over an Ethernet network. Verify that all Ethernet cables are connected. Verify that the Ethernet switch is powered. |
| LNK | Flashing green      | The port is communicating on Ethernet. No action is required. The port is performing its power-up self-test. No action is required.                                                                                         |
| LNK | Green               | The port is connected to a powered Ethernet device. Therefore, the safety relay can communicate over an Ethernet network. No action is required.                                                                            |

## Introduction

## Ethernet Messaging

## I/O Messaging

<!-- image -->

## Automation Controller Communications

This chapter describes and gives examples of how each type of EtherNet/IP™ messaging, I/O messaging, and explicit messaging, is used.

The Guardmaster® 440C-CR30 safety relay with 440C-ENET plug-in module supports two types of EtherNet/IP messaging:

- I/O messaging - Used for deterministic EtherNet/IP communications with ControlLogix®, CompactLogix™, SoftLogix™, and EtherNet/IP scanners. Its primary use is to read and write I/O data for diagnostics and control purposes.
- Logic explicit messaging - Used for non-deterministic communications in which data is not critical for control. Logic explicit messages have a lower priority when compared to I/O messages and are used to read and write non-critical data.

Studio 5000 Logix Designer® application is used to configure I/O messaging between an automation controller and a CR30 safety relay on an EtherNet/IP network.

There are two ways to add the safety relay into the I/O configuration:

- CR30 safety relay Add-on Profile (AOP) RSLogix 5000® software, version 20.00 or later, Studio 5000 Logix Designer application, version 21.00 or later
- Generic profile - RSLogix 5000 software, all versions

These configuration methods are described in the following sections. If your version of RSLogix 5000 software supports safety relay AOP, we recommend that you use this method.

## Use RSLogix 5000 Safety Relay Add-on Profile

When compared to the generic profile (all versions), the RSLogix 5000 safety relay Add-on Profiles provide these advantages:

- Profile provides descriptive controller tags for data assemblies that are exchanged between the controller and safety relay. This profile minimizes potential mismatches between assembly data and tags and substantially reduces safety relay configuration time.
- New Logic Configuration tab (AOP version 2.01 or later) minimizes the need for a separate configuration tool.
- Monitor the configured safety relay logic directly from the AOP (AOP version 2.01 or later).
- Safety relay configuration settings are saved as part of the RSLogix 5000 software, version 20.00 or later, project file (.ACD) and also downloaded to the controller.
- Unicast connection option (RSLogix 5000 software, version 20.00 or later)
- The Add-on Profile can be added online while the controller is in Remote Run mode (ControlLogix only).
- The safety relay Add-on Profile can be updated anytime. Go to rok.auto/pcdc to download the latest safety relay Add-on Profile.

## Add the CR30 Safety Relay to the I/O Configuration

An existing project can be used or a new project can be created to configure EtherNet/IP I/O messaging. To create a project, perform the following steps.

1. Create, or open an existing, RSLogix 5000 or Studio 5000 Logix Designer project and verify that the Logix controller is offline.

<!-- image -->

<!-- image -->

For ControlLogix users who want to add a Guardmaster® 440C safety relay online manually, go online with the ControlLogix controller using the RSLogix 5000 or Studio 5000 Logix Designer application. The ControlLogix controller can be in Remote Run or Program mode.

2. To open the Select Module Type window, right-click on the Ethernet tree of the EtherNet/IP bridge within the I/O Configuration folder and select New Module.
3. Search for a Guardmaster 440C safety relay by typing 440C in the search field, select the 440C-CR30-22BBB, then click Create.

<!-- image -->

<!-- image -->

<!-- image -->

If the Guardmaster 440C safety relay is not shown, go to rok.auto/pcdc and download the latest RSLogix 5000 safety relay Add-on Profile. Add-on Profile

- version 2.01 (or later) includes support for the embedded configuration editor.

The New Module dialog box appears.

<!-- image -->

4. On the General tab, edit the following items about the safety relay:
5. Click Change… to configure the plug-in modules that are attached to the CR30 safety relay.
6. Right-click on the [2] &lt;Empty&gt; slot in the Module Definition dialog box and select the plug-in module that is physically in that slot, if any.
4. The 440C-ENET plug-in module is fixed in slot 1 as it is required to communicate with the Logix controller.

| Field Setting                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name A unique name to identify the safety relay. The name can contain as many as 40 characters; any mix of upper/lower case letters, number, and underscore characters. |
| Description Optional. A description of the safety relay.                                                                                                                |
| IP Address The IP address of the safety relay.                                                                                                                          |

<!-- image -->

<!-- image -->

<!-- image -->

7. In the Module Definition dialog box, edit the following information.
8. Click OK once you have added any plug-in module that is attached to the CR30 safety relay.
9. If you use Major Revision 8 in the AOP, click OK on the next window to have the Studio 5000 Logix Designer application create the predefined tags. The CR30 safety relay now appears as a module in the I/O Configuration folder.

<!-- image -->

|                      | Field Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Revision             | The major and minor revision of the firmware in the safety relay. The major revision selection determines the functionality available in the Add-on Profile: • Major revision 8 - I/O messaging only. The Add-on Profile does not configure the CR30 safety relay. The safety relay must be configured using Connected Components Workbench™ software, version 8.00 or later, when this selection is made. • Major revision 9 - Version 2.01 or later of the Add-on Profile only. This selection enables the Logic Configuration tab on the AOP that supports the setup and monitoring of the safety relay configuration. The configuration is stored in the ACD file of the controller project, which is downloaded and stored in the controller. |
| Revision             | IMPORTANT  The configuration consumes at least 300 KB of controller memory. You can monitor the controller memory usage from the Controller Properties dialog box, Memory tab. To help prevent the configuration from being stored in controller memory, choose Major Revision 8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Electronic KeyinChag | The settings for electronic keying determine whether a connection is successful between the controller and safety relay based on the following criteria. • Compatible - A successful connection is made when the defined settings match the values in the safety relay as follows. a. The device type and product code match. b. Same major revision or higher. c. Minor revision as follows. – If the major revision is the same, the minor revision must be the same or higher. – If the major revision is higher, the minor revision can be any number. • Disable - The keying attributes are not considered when attempting to communicate with the device. Other attributes, such as data size and format, are considered and                 |
| Electronic KeyinChag | ATTENTION: With Disable Keying, communication can occur with a device other than the type specified in the project with unpredictable results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Electronic KeyinChag | • Exact match - All keying attributes of the device that is defined (major revision, minor revision, device type, and product code) must precisely match the attributes of the installed device to establish communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Data Format          | The following data formats are supported: • Listen only - An input connection where another controller owns/provides configuration data for the safety relay. A controller with a listen-only connection does not write configuration to the safety relay nor does it write to the safety relay outputs. A listen only connection can only be established when the owner controller is actively controlling the safety relay. • Data - An I/O connection where this controller is the owner and controls the outputs to the safety relay and is able to write the configuration to the safety relay. The safety relay supports only one data connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Configure Safety Relay Logic

The safety relay logic can be configured in the CR30 safety relay Add-on Profile, version 2.01 or later. Firmware revisions 9.004 or later of the CR30 safety relay support this feature.

IMPORTANT

Major revision 9 (default selection) or later must be selected in the Module Definition Dialog box (access from General &gt; Change…) to enable the Logic Configuration tab.

To edit the Logic for the safety relay:

1. Click the Logic Configuration tab in the Add-on Profile.
2. Click Edit Logic.

<!-- image -->

The Edit Guardmaster 440C-CR30 Logic window launches.

<!-- image -->

<!-- image -->

For information about use of the Logic Editor, see Chapter 4 on page 25 .

3. After you have created your logic configuration, close the Edit Guardmaster 440C-CR30 Logic window.
4. If errors are present in your logic, you are notified that your changes are discarded if you exit the editor, click Cancel to continue to fix any errors.

<!-- image -->

The Error List pane appears at the bottom of the Edit Guardmaster 440C-CR30 Logic window to inform you of any errors in the logic.

<!-- image -->

5. After correcting the errors, close the window.
6. Click Apply.
7. Close the profile.

## Download the Configuration to the CR30 Safety Relay

A two-step process is required to apply the configuration to your CR30 safety relay. First, you must download the configuration to the Logix controller. The configuration is not automatically pushed to the CR30 safety relay, you must open the profile and select the Logic Configuration tab to initiate the download of the configuration to the CR30 safety relay. Since the configuration is not stored in safety-rated memory on the Logix controller nor is it transferred to the safety relay with a safety-rated protocol, you must manually trigger the download to the CR30 safety relay following these steps.

1. From the Communications menu, choose Who Active to open the Who Active dialog box.
2. From the navigation pane, find the path between your Workstation and the target Logix controller for this project.
3. Click Download to open the Download dialog box.

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Review the attention statements that are presented in the Download dialog box. Only proceed with the download if the conditions displayed do not present a hazard for your application.

After the download is complete, the I/O Not Responding indicator flashes. A warning icon appears on the CR30 safety relay in the I/O Configuration tree. The module fault is Code 16#0106 as the configuration in the Logix controller for the safety relay does not match

4. Click Download. what is in the physical device.
5. Double-click the safety relay profile.
6. Click the Logic Configuration tab. The Project Mismatch dialog box opens. Click Download the current project to the safety relay.
7. The Change to Program Mode dialog box appears. Click Yes.
8. The Download Success dialog box appears. Click Yes.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

IMPORTANT

If the Download Failed dialog box appears, confirm that the safety relay is physically present on the network and has the correct network address.

Once the download is complete, the I/O connection between the Logix controller and the safety relay is successful.

<!-- image -->

9. To monitor the safety relay logic online, click Edit Logic.

<!-- image -->

IMPORTANT

After a download, the safety relay runs with the configuration for 24 hours without being verified. To learn more about how to verify the safety relay, see Verification on page 33 .

## Online Changes to the CR30 Safety Relay Configuration

While connected to the Logix controller, the configuration to a CR30 safety relay can be modified without a separate download to the Logix controller. To modify the CR30 safety relay configuration, follow these steps.

1. While connected to the Logix controller, open the Guardmaster 440C-CR30 safety relay profile.
2. Click the Logic Configuration tab.
3. Select Go offline from the pull-down menu in the upper-right hand corner of the tab.

<!-- image -->

The status is now displayed as Edit.

<!-- image -->

4. To launch the Edit Guardmaster 440C-CR30 Logic window, click Edit Logic.

<!-- image -->

<!-- image -->

For information about use of the Logic Editor, see Chapter 4 on page 25 .

5. After completing your edits, close the Edit Guardmaster 440C-CR30 Logic window.
6. If errors are present in your logic, you are notified that your changes are discarded if you exit the editor, click Cancel to continue to fix any errors.

<!-- image -->

The Error List pane appears at the bottom of the Edit Guardmaster 440C-CR30 Logic window to inform you of any errors in the logic.

<!-- image -->

7. After correcting the errors, close the window.
8. Click Apply. The download begins. The Download Success dialog box appears.
9. Click Yes.

<!-- image -->

## IMPORTANT

After a download, the safety relay runs with the configuration for 24 hours without being verified. See Verification on page 31 to learn more about how to verify the safety relay.

## Access Module Data with Add-on Profiles

With configuration of the Logix controller and the CR30 safety relay complete, the Logix controller can exchange data with the safety relay.

1. After downloading to the Logix controller, open the Controller tags window.
2. Select the Monitor Tags tab.

<!-- image -->

In the following example, predefined input tags were created for the Guardmaster 440C-CR30 safety relay. For detailed information on the individual tag members and their meaning, see Tag Definitions on

## page 175 .

<!-- image -->

The Output tags are used to write signals to the CR30 safety relay. In this example, a reset signal is sent to the safety relay.

<!-- image -->

The signal can be used within the safety relay logic by selecting the corresponding communications input selection from a safety monitoring function that supports standard rated signals.

<!-- image -->

## Explicit Messaging

Data can be accessed from the CR30 safety relay with 440C-ENET plug-in module by non-Logix automation controllers that support EtherNet/IP Explicit Messaging.

This example shows the configuration of an explicit message to read data from the CR30 safety relay.

1. Configure the MSG instruction to read the data assembly from the Guardmaster EtherNet/IP network interface by editing these fields.
- Channel: 1 (Integral) (this channel is the Ethernet port)
- Communication Command: CIP Generic
- Data Table Address (Receive): N7:0 (choose an address that supports 28 bytes)
- Size in Bytes (Receive): 28
- Extended Routing Info File (RIX): RIX11:0
- Service: Read Assembly
- Class: 04
- Instance: 100 (64 h)
- Attribute: 03
2. Set the Ethernet network address of the Guardmaster 440C-ENET plug-in module as the target of the message instruction:

<!-- image -->

<!-- image -->

Appendix E on page 173 describes the individual members of the data that are returned from the message instruction.

This example shows the configuration of an explicit message to write data to the CR30 safety relay.

1. Configure the MSG instruction to read the data assembly from the Guardmaster EtherNet/IP network interface by editing these fields.
- Channel: 1 (Integral) (this channel is the Ethernet port)
- Communication Command: CIP Generic
- Data Table Address (Send): N7:0 (choose an address that supports 4 bytes)
- Size in Bytes (Send): 4
- Extended Routing Info File (RIX): RIX11:0
- Service: Write Assembly
- Class: 04
- Instance: 150 (96 h)
- Attribute: 03
2. Set the Ethernet network address of the Guardmaster 440C-ENET plug-in module as the target of the message instruction.

<!-- image -->

<!-- image -->

Appendix E on page 175 describes the individual members of the data that are returned from the message instruction.

## Notes:

## Status Indicators

The CR30 safety relay has 21 status indicators on the upper left front of the module. These status indicators fall into three categories:

- Input status
- Module status
- Output status

<!-- image -->

Figure 132 - Status Indicators

<!-- image -->

## Input and Output Status Indicators

To access and configure the status indicators in the Connected Components Workbench™ software,

1. In the Project Organizer, double-click Guardmaster\_440C-CR30*.
2. Click LED Configuration.
3. Configure the filter type and value for input and output status indicators.

<!-- image -->

First, select one of four filter types for each status indicator:

- Not Used
- Terminal Status
- Safety Monitoring Function Status
- Safety Output Function Status

Then, select the instance for each filter type.

Monitoring a function is advantageous when the input and output logic blocks have multiple inputs or outputs. One status indicator can provide status information about multiple inputs or outputs, when it provides the status of an input or output block.

In the previous example:

- Input LED 1 is monitoring a terminal status. In this case, it is monitoring terminal 01. When the signal to terminal 1 is HI, the status indicator is on. When the signal to terminal 1 is LO, the status indicator is off. If this case was one channel input, then the status indicator provides all information about the input.
- Input LED 2 is monitoring safety monitor function 1. If the status indicator is on, then we know that all inputs are satisfied for whatever function (for example, dual-channel input, muting, or two-hand control) is being monitored.

## Controller Status Indicators

- Output LED 3 is monitoring the status of a safety output function. In this case, SOF 1 is being monitored. If SOF 1 is driving four outputs (two safeties, one diagnostic, and one Modbus), we expect all four outputs to be HI when LED 3 is on.

The CR30 safety relay has five module status indicators that are described in Table 21 .

Table 21 - Status Indicators

| Status Indicator   | Color Indicates                                                |
|--------------------|----------------------------------------------------------------|
| POWER              | Off No input power or power error condition                    |
| POWER              | Green Power on                                                 |
| RUN                | Off Program mode                                               |
| RUN                | Green Run mode                                                 |
| RUN                | Flashing green [2 Hz] Application is running but not verified  |
| FAULT              | Off No fault is detected                                       |
| FAULT              | Flashing red [2 Hz] Application fault is detected, recoverable |
| FAULT              | Red Controller hardware is faulted, nonrecoverable             |
|                    | LOCK Off Not used                                              |
| COM                | Off No communication                                           |
| COM                | Green Communication by serial port or USB                      |

## Notes:

## Modbus Mapping

Table 22 - Modbus Addresses

| Modbus Address Parameter Modbus Address Parameter                                                                   |                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|                                                                                                                     | 000001…000016 Modbus serial input 000345…000360 State of Logic Level B Instance (LLB) 1…16                          |
| 000025…000028 Input Data for Plug-in 1 Terminals I-00…I-03 000361…000376 State of Safety Output Function (SOF) 1…16 |                                                                                                                     |
| 000033…000036 Output Data for Plug-in 1 Terminals O-00…O-03 000377…000392 Ready-to-start of SOF 1…16                |                                                                                                                     |
| 000265 Processor HW fault                                                                                           | Fault bit 0 of SMF 1…24 00: No error 01: 10: Simultaneity fault 11: One channel open after reset                    |
| 000266 Safety Input HW fault                                                                                        | Fault bit 0 of SMF 1…24 00: No error 01: 10: Simultaneity fault 11: One channel open after reset                    |
| 000267 Safety Output HW fault                                                                                       | Fault bit 0 of SMF 1…24 00: No error 01: 10: Simultaneity fault 11: One channel open after reset                    |
| 000268 Power supply fault / Main transistor fault                                                                   | Fault bit 0 of SMF 1…24 00: No error 01: 10: Simultaneity fault 11: One channel open after reset                    |
|                                                                                                                     | 000269 Communication fault 000417…000440 Fault bit 1 of SMF 1…24                                                    |
| 000270 Configuration fault (wrong revision, invalid configuration) 000441…000464 Fault bit 2 of SMF 1…24            |                                                                                                                     |
| 000271 Time out (Clock monitoring) 000465…000488 Fault bit 3 of SMF 1…24                                            |                                                                                                                     |
|                                                                                                                     | 000272 Plug-in fault 000489…000504 Retrigger Fault SOF 1…16                                                         |
| 000273…000294 State of Embedded Terminals 00…21 000505…000512 Cross Fault of Terminals 12…17                        |                                                                                                                     |
|                                                                                                                     | 000297…000300 Input of Plug-in 2 Terminals I-00…I-03 000521…000761 Input Assembly Data (see Appendix E on page 175) |
| 000301…000304 Output of Plug-in 2 Terminals O-00…O-03                                                               | 000513…000520, Reserved                                                                                             |
| 000305…000328 State of Safety Monitoring Function (SMF) 1…24                                                        | 000762…000848                                                                                                       |
| 000329…000344  State of Logic Level A Instance (LLA) 1…16  (1)                                                      | 000849…000860 Fault log                                                                                             |

## Modbus Communication

The CR30 safety relay uses Modbus RTU communications to transfer status information and control signals to Micro800™ controllers and human machine interfaces like PanelView™ monitors.

The Modbus configuration of the CR30 safety relay is fixed to the Modbus RTU secondary at address 1.

For more information on PanelView monitors, refer to the following publications:

- 2711C-UM001
- 440C-QS001

The CR30 safety relay Modbus addresses are mapped to the parameters shown in Table 22. The addresses in the range of 1…512 can be accessed as coils. The fault log can be accessed by holding register reads; each address contains 16 bits of data.

<!-- image -->

## Example Architectures

Figure 133 - Non-readable Pass-through Blocks

<!-- image -->

Some examples of how the CR30 safety relay is used with Modbus are shown in Figure 134 .

In Figure 134, a PanelView C600 graphic terminal is connected to the serial port of the CR30 safety relay. The C600 graphic terminal is configured over its Ethernet port. The C600 graphic terminal can read status information from the CR30 safety relay and can send reset and restart signals to the CR30 safety relay.

Figure 134 - Modbus RTU Communication — PanelView C600

<!-- image -->

In Figure 135 on page 129, a Micro830® programmable logic controller (PLC) is connected to the CR30 safety relay by the 8-pin DIN serial port connections. The Micro830 PLC can read/use status information from the CR30 safety relay and can send reset and restart signals to the CR30 safety relay.

## Read CR30 Safety Relay Status

Figure 135 - Modbus RTU Communication — Micro830

<!-- image -->

In Figure 136, a PanelView C600 graphic terminal is connector the serial port of the Micro830 PLC and the Micro830 PLC is connected to the CR30 safety relay through a SERIALISOL plug-in module. The Micro830 PLC can read/use status information from the CR30 safety relay and can send reset and restart signals to the CR30 safety relay.

Figure 136 - Modbus RTU Communication — PanelView C600 and Micro830

<!-- image -->

In the Micro800 family, the Msg\_Modbus block must be used.

In the example ladder diagram below, a Micro830 PLC reads the status of the first five input wiring terminals of the CR30 safety relay.

- Rung 1: When you press a push button that connects to terminal 03 of the Micro830 PLC, the Micro830 PLC sends a Modbus message to the CR30 safety relay.

- Rung 2: The format of the data in LocalAddr is a WORD. The first block ANY\_TO\_DINT converts the WORD to a DINT. The second block compares the DINT to the value of 1 with an AND\_MASK. The third block checks to see if the value is 1. If the value is 1, then the output terminal \_IO\_EM\_DO\_00 goes HI.

Figure 137 - Read Ladder Diagram

<!-- image -->

You must configure local variables. In this example, they are labeled LocalCfg, TargetCfg, and LocalAddr.

- LocalCfg must be configured as a MODBUSLOCPARA data type. TargetCfg must be configured as a MODBUSTARPARA data type. LocalAddr must be configured as a MODBUSLOCADDR data type.
- TargetCfg.Addr - Select the first value from the Modbus-mapping table for the CR30 safety relay. In this case, the initial value is set to 000273 (leading zeros must be included), which is mapped to terminal 00 of the CR30 safety relay.
- TargetCfg.Node - Enter a value of 1. The CR30 safety relay is fixed at Node 1.
- LocalCfg.Channel - Select the serial port location. Enter a 2 if the embedded serial port is used. Enter a 5 to use the serial port in the fist plug-in slot.
- LocatCfg.TriggerType - Enter a 0 to have the block execute only once. Each time the push button that is connected to terminal \_IO\_EM-DI-00 is pressed, the message sends once.
- LocalCfg.Cmd - Enter a 1 to instruct the block to read a coil (which is mapped to the CR30 safety relay).
- LocalCfg.ElementCnt - Enter a 5 to read the status of five inputs (starts at 000273 and ends at 000277).
- LocalAddr - The results are placed in LocalAddr. There is no need to change.

Figure 138 - Read Local Variables

<!-- image -->

## Send Reset to CR30 Safety Relay

The Reset function must use a separate Modbus message block. Another constraint that must be considered is a reset signal must be between 0.5…3 s long. In the example below, a momentary button connects to the embedded terminal \_IO\_EM\_DI\_02.

- Rung 3: The push button initiates a TONOFF timer. The timer is set for a 100 ms delay on and a 1100-ms delay off, which provides a reset signal of 1 s.
- Rung 4: The Modbus message is sent with every scan of the ladder. The reset is executed because the reset value goes from 0 to 1 and back to 0 within the acceptable range of 0.5…3 s.
- Rung 5: When the TONOFF block goes LO, embedded output \_IO\_EM\_DO\_01 goes LO and moves the value of 0 into Reset Addr.
- Rung 6: When the TONOFF block goes HI, the embedded output \_IO\_EM\_DO\_01 goes HI and moves the value of 1 into Reset Addr.

Figure 139 - Reset Ladder Diagram

<!-- image -->

You must configure a second set of local variables. In this example, they are labeled ResetCfg, ResetTrgt, and ResetAddr.

- ResetCfg must be configured as a MODBUSLOCPARA data type. ResetTrgt must be configured as a MODBUSTARPARA data type. ResetAddr must be configured as a MODBUSLOCADDR data type.
- ResetTrgt.Addr - Enter a value of 1, which is the Modbus-mapping of the CR30 safety relay.
- ResetTrgt.Node - Enter a value of 1. The CR30 safety relay is fixed at Node 1.
- ResetCfg.Channel - Select the serial port location. Enter a 2 if the embedded serial port is used. Enter a 5 to use the serial port in the fist plug-in slot.
- ResetCfg.TriggerType - Enter a 1 to have the block execute every time that the ladder is scanned

- LocalCfg.Cmd - Enter a 5 to instruct the block to write to a coil (that is, turn on an input of the CR30 safety relay).
- ResetCfg.ElementCnt - Enter a 1 to write-only 1 bit.
- ResetAddr - The results are placed in LocalAddr. There is no need to change.

## Figure 140 - Reset Local Variables

<!-- image -->

## Recoverable Faults

## Status Indicators

## Troubleshooting

Faults fall into two categories:

- Recoverable
- Nonrecoverable

Recoverable faults are those faults that can be corrected without having to cycle the power to the CR30 safety relay. Nonrecoverable faults require the power to be cycled to recover after the fault is corrected.

Recoverable faults can be cleared if you eliminate the cause of the fault and cycle the inputs that are associated with the fault. The output that is connected to an input with that fault is switched off. The other non-affected outputs continue to work.

Examples of recoverable faults include:

- SMF faults
- Cross loop
- Simultaneity faults
- Reset button fault
- Muting: Synchronization time exceeded
- Muting time exceeded
- Sequence fault

The fault status indicator alerts you to faults. If the fault status indicator is flashing red, a recoverable fault has occurred. If the Fault status indicator is steady red, a nonrecoverable fault has occurred.

<!-- image -->

Figure 141 - Fault Status Indicator

<!-- image -->

## Nonrecoverable Faults

## Troubleshoot with the Connected Components Workbench Logic Editor

Nonrecoverable faults and failures are malfunctions of the device itself that occur during operation. Internal monitor measures verify the safety integrity of the device by detecting these faults. Nonrecoverable faults require a power cycle to allow the CR30 safety relay to perform all relevant internal system tests during initialization. If there are transient malfunctions, the CR30 safety relay recovers after a power cycle. If there is permanent damage or malfunction, the CR30 safety relay remains in safe state after a power cycle. Permanent nonrecoverable faults are typically related to random hardware faults that cause permanent damage of components.

Potential root cause for nonrecoverable faults:

- Transient EMC disturbance causing asynchrony of the two CPUs
- Environmental disturbances of high voltage or high current spikes that cause internal damage of components
- Internal voltage level monitor detects power supply interruptions
- Transient overload conditions of safety outputs that trigger short circuit and overload protection or the output (for example, high inrush currents)

When connected to the CR30 safety relay through the USB port, the Connected Components Workbench™ Logic Editor monitors and displays the status of each terminal and block.

- Green shows an on (HI) state.
- Red shows a fault state (output is LO).
- Gray blocks are off (LO) state.

## Figure 142 - Monitor Status with Logic Editor

<!-- image -->

Mouse over the red block, and the Connected Components Workbench software displays an error message for 5 seconds. Move the mouse away and then back over the block to show the message again. The fault tooltip automatically appears once a fault is detected during the Online Monitoring mode. You can acknowledge the fault to close the tooltip window by clicking the X in the upper-right hand corner of the tooltip. To show the fault information again, right-click on the function block and click Show Fault.

Figure 143 - Mouse Over to Show Error Message (in Yellow Box)

<!-- image -->

The type of fault is also shown in the top panel of the Project tab (see Figure 144).

- For a recoverable fault, the Device Details view only indicates Fault: Recoverable. For further details, navigate to the Logic Editor view and mouse over the red marked function block. You are allowed to change the operation mode to Program mode
- For a nonrecoverable fault, the Device Details view provides the fault type and status. The device automatically exits Run mode and switches to Program mode. You cannot change the operation mode. Mouse over the fault status area to get more information.

Figure 144 - Mouse Over Fault in Project Tab

<!-- image -->

To see a list of the recent nonrecoverable faults, click Faults in the Safety Tree.

The recent faults appear in the fault pane.

Click Export to export the faults to a comma-separated value (.csv) file. The default path for Win7 for saving the exported fault log file is the folder at C:\Users\&lt;user name&gt;\documents\CCW\Fault log.

## Troubleshooting with Modbus

Figure 145 - Recent Fault List

<!-- image -->

Many faults can be reported to an HMI or PLC using Modbus. Table 23 shows a list of the Modbus addresses for faults.

Table 23 - Modbus Addresses for Faults

| Modbus Address Parameter                                           |
|--------------------------------------------------------------------|
| 000265 Processor HW fault                                          |
| 000266 Safety input HW fault                                       |
| 000267 Safety output HW fault                                      |
| 000268 Power supply fault / main transistor fault                  |
| 000269 Communication fault                                         |
| 000270 Configuration fault (wrong revision, invalid configuration) |
| 000271 Time out (clock monitoring)                                 |
| 000272 Plug-in fault                                               |
| 000393...000416 Fault bit 0 of SMF 0...23                          |
| 000417...000440 Fault bit 1 of SMF 0...23                          |
| 000441...000464 Fault bit 2 of SMF 0...23                          |
| 000465...000488 Fault bit 3 of SMF 0...23                          |
| 000489...000504 Retrigger fault SOF 0...23                         |
| 000505...000512 Cross fault of terminals 12...17                   |
| 000849...000860 Fault log                                          |

Table 24 - Fault Messages for the SMF Type

|                                                                                                   | SMF Type Fault Bit 3 Fault Bit 2 Fault Bit 1 Fault Bit 0                                    |                                                                                                                                                               |                                                                                        |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
|                                                                                                   |                                                                                             |                                                                                                                                                               | 1 Channel Reserved Reserved Reserved Input circuit is shorted to 24V.                  |
| 2 Channel, two-hand control Reserved                                                              | The Left and Right buttons are in an inconsistent state for longer than 500 ms.             | Reserved                                                                                                                                                      | At least one circuit is shorted to 24V or another input circuit.                       |
| Safety Mat Reserved                                                                               | Discrepancy Fault: Input channels inconsistent greater than the configured discrepancy time | One channel went to the safe state and back to the active state while the other channel remained active, or One channel went to the safe state upon power-up. | At least one circuit is shorted to 24V or another input circuit.                       |
| 3 Channel Reserved Reserved                                                                       |                                                                                             | One channel went to the safe state upon power-up.                                                                                                             | At least one circuit is shorted to 24V.                                                |
|                                                                                                   | Reset Reserved Reserved Reserved                                                            |                                                                                                                                                               | A transition of the reset input from on (1) to off (0) did not occur within 3000 ms.   |
|                                                                                                   | Override Reserved Reserved Reserved                                                         |                                                                                                                                                               | At least one circuit is shorted to 24V or another input circuit.                       |
|                                                                                                   | Restart Reserved Reserved Reserved                                                          |                                                                                                                                                               | A transition of the restart input from on (1) to off (0) did not occur within 3000 ms. |
|                                                                                                   | Mute Reserved Muting sensor sequence fault.                                                 | The safety light curtain was muted for longer than the configured maximum mute time.                                                                          | Too much time has elapsed between sensors being blocked.                               |
| Lack of muting L-type Too much time has elapsed between Sensor2 and Light Curtain2 being blocked. | Muting sensor sequence fault.                                                               | The safety light curtain was muted for longer than the configured maximum mute time.                                                                          | Too much time has elapsed between Sensor1 and Sensor2 being blocked.                   |

## Example Fault Analysis – Cross Fault

Create a cross fault from input test pulse A to input pulse test B with the safety output on.

- The Modbus address 000505 goes HI immediately, this action indicates that the fault was detected.
- About 4 seconds later, the fault is acted upon.
- Modbus address 000393 (Bit 0 of SMF1) goes HI.
- The safety output goes off.
- On the Connected Components Workbench Logic tab, the E-stop and gate inputs go off, and both logic blocks show red color.
- The Connected Components Workbench Project tab shows Recoverable Fault.

Figure 146 - E-stop Block Fault Message

<!-- image -->

## Remove the fault.

- The Modbus address 000505 goes LO immediately, this action indicates that the fault was removed.
- Modbus address 000393 (Bit 0 of SMF1) remains HI.

Table 24 shows the fault bit message for the type of functions that are selected for the safety monitoring function block.

- On the Connected Components Workbench Logic tab, both the E-stop and gate logic blocks continue to show red color.
- The safety output remains off.

## Cycle the E-stop.

- Modbus address 000393 (Bit 0 of SMF1) goes LO.
- On the Connected Components Workbench Logic tab, the E-stop block turns green, and the gate block remains red,

## Cycle the gate.

- On the Connected Components Workbench Logic tab, the gate block turns green.

The safety system is back to an operating state and waits for the Reset button to be pressed.

## Security and Password

CR30 safety relay security has two components:

- Exclusive access that helps prevent simultaneous configuration of the safety relay by two users.
- Password protection that secures the intellectual property that is contained within the safety relay and helps prevent unauthorized access.
- CR30 safety relays with revision 7 or later firmware

| Exclusive Access    | Exclusive access is enforced on the CR30 safety relay whether the safety relay is password-protected or not. This access means that only one Connected Components Workbench™ session is authorized at a time and only an authorized client has exclusive access to the safety relay application. This access also verifies that only one software session has exclusive access to the Guardmaster® 440C application-specific configuration. Exclusive access is enforced on Guardmaster 440C firmware revision 7 and later. When you connect to a CR30 safety relay with the Connected Components Workbench software, the software is given exclusive access to that safety relay.                         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Password Protection | By setting a password on the safety relay, you effectively restrict access to the configuration software connections to the safety relay to software sessions that can supply the correct password. Essentially, Connected Components Workbench operations such as upload, download, and connect are prevented if the safety relay is secured with a password and the correct password is not provided. CR30 safety relays with firmware revision 7 and later are shipped with no password. A password can be set through the Connected Components Workbench software (version 7 or later). The CR30 safety relay password is also backed up to the memory backup module (catalog number 2080-MEMBAK-RTC). |
| Compatibility       | The Safety Relay Password feature is supported on: • Connected Components Workbench version 7 and later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

If you have earlier versions of the software and/or hardware, you are advised to upgrade the software and firmware. See DMK Extraction on page 171 for instruction on firmware updates.

<!-- image -->

## Work with a Locked Safety Relay

## Password Configuration

The following workflows are supported on compatible CR30 safety relays (firmware revision 7 or later) and Connected Components Workbench software version 7 or later.

## Upload from a Password-protected Safety Relay

1. Launch the Connected Components Workbench software project with your CR30 safety relay configuration.
2. To open the Safety Relay workspace, double-click Guardmaster 440C safety relay in the Project Organizer.
3. Select Upload from the pull-down menu in the safety relay header.
4. Select the target safety relay in the Connection Browser.
5. When requested, provide the safety relay password.

## Connect to a Password-protected Safety Relay

1. Launch the Connected Components Workbench project with your CR30 safety relay configuration.
2. To open the Safety Relay workspace, double-click Guardmaster 440C safety relay in the Project Organizer.
3. Select Connect from the pull-down menu in the safety relay header.
4. Select the target safety relay in the Connection Browser.
5. When requested, provide the safety relay password.

## Download to a Password-protected Safety Relay

1. Launch the Connected Components Workbench project with your CR30 safety relay configuration.
2. To open the Safety Relay workspace, double-click Guardmaster 440C safety relay in the Project Organizer.
3. Select Download from the pull-down menu in the safety relay header.
4. Select the target safety relay in the Connection Browser.
5. When requested, provide the safety relay password.

This section shows you how to set, change, and clear the password on a target safety relay through the Connected Components Workbench software.

IMPORTANT

The following instructions are supported on Connected Components Workbench software version 7 and CR30 safety relays with firmware revision 7.

## Set Safety Relay Password

In the following instructions:

- The Connected Components Workbench software is connected to the CR30 safety relay.
- The safety relay is loaded with a viable configuration.
- The configuration does not necessarily have to be verified.
- The CR30 safety relay can be in either Program or Run mode.

## Procedure:

1. On the Connected Components Workbench software, open the project for the target safety relay by double-clicking the safety relay in the Project Organizer.
2. On the Device Details toolbar, mouse over Secure. The tooltip message Set, Change, or Clear Safety Relay Password Protection is displayed.
3. Click Secure. Select Set Password.
4. Provide password. Confirm the password by providing it again in the Confirm field.

<!-- image -->

<!-- image -->

Passwords must have at least eight characters to be valid.

5. Click OK.

Once a password is created, any new session that tries to connect to the safety relay has to supply the password to gain exclusive access to the target safety relay.

<!-- image -->

## IMPORTANT

If you have to update the safety relay, the project in the safety relay is lost. A new project must be downloaded.

6. Click OK.

<!-- image -->

## Change Password

With an authorized session, you can change the password on a target safety relay through the Connected Components Workbench software. The target safety relay must be in Connected status.

1. On the Device Details toolbar, click Secure. Select Change Password.

<!-- image -->

The Change Safety Relay dialog appears.

2. Enter the Old Password, New Password, and Confirmation of the new password.
3. Click OK.

<!-- image -->

The safety relay requires the new password to grant access to any new session.

## IMPORTANT

Keep the password carefully. If lost, you have to update the safety relay to reset the password. The project in the safety relay is lost but a new project can be downloaded.

## Clear Password

With an authorized session, you can clear the password on a target safety relay through the Connected Components Workbench software.

1. On the Device Details toolbar, click Secure. Select Clear Password.

<!-- image -->

The Clear Password dialog appears.

<!-- image -->

2. Enter password.
3. To clear the password, click OK .

The safety relay requires no password on any new session.

## Lost Password

If the safety relay is secured with a password and the password has been lost, then it becomes impossible to access the safety relay with the Connected Components Workbench software.

To recover, use ControlFLASH™ software to refresh the safety relay firmware, which also clears the safety relay memory and clears the password

<!-- image -->

ATTENTION: The project in the safety relay is lost but a new project can be downloaded.

## Notes:

## Overview

## Project Back Up and Restore

## Use the Memory Module

## IMPORTANT

The CR30 safety relay fails to recognize 2080-MEMBAK-RTC memory modules that are manufactured on or after 2016/02/11 and cannot be used to back up and restore the program or update the firmware.

CR30 safety relays support the 2080-MEMBAK-RTC memory modules for the following purposes:

- Project backup and restore
- Firmware and project backup and restore

<!-- image -->

ATTENTION: Removal and Insertion Under Power (RIUP) is not supported on the 2080-MEMBAK-RTC memory module when used with a Guardmaster® 440C safety relay.

<!-- image -->

ATTENTION: The 2080-MEMBAK-RTC memory module can only be installed in Slot 1 (the leftmost plug-in slot) on the CR30 safety relay.

## IMPORTANT

Do not remove the 2080-MEMBAK-RTC memory module or power down while operations such as backup and restore are ongoing to help prevent data loss. A flashing status indicator on the memory module indicates that these operations are ongoing.

IMPORTANT

IMPORTANT

Backup can only occur when the safety relay is in the Safety Verified state. To learn about safety verification, see Verification on page 33 .

The use of the 2080-MEMBAK-RTC memory module with the CR30 safety relay is only supported with firmware revision 7 or later.

Project backup and restore on CR30 safety relays are supported through the 2080-MEMBAK-RTC memory module. Both backup and restore can be initiated through the Connected Components Workbench™ software and the use of buttons physically present on the CR30 safety relay and the 2080-MEMBAK-RTC memory module.

A backup of both the CR30 safety relay firmware and project can only occur through the Connected Components Workbench software.

Backup and restore can only occur when the 2080-MEMBAK-RTC memory module is present in plug-in Slot 1 (the leftmost slot) of the CR30 safety relay. On safety relay power-up, the safety relay enters a fault state where the application logic is not executing. Backup and restore commands can be issued in this fault state.

The 2080-MEMBAK-RTC memory module stores the safety relay password, if present, in encrypted format. When the password is mismatched, the contents of the 2080-MEMBAK-RTC memory module is not restored on the safety relay.

## Back Up Project

You can back up a CR30 safety relay project to a 2080-MEMBAK-RTC memory module with the button on the memory module.

1. Power down the CR30 safety relay.
2. Remove the dust cover or plug-in module in slot 1, the leftmost slot, of the safety relay module bay.
3. Snap the 2080-MEMBAK-RTC memory module into slot 1 of the module bay.
4. Power on the CR30 safety relay. The safety relay detects the presence of the 2080-MEMBAK-RTC memory module and enters a fault state

<!-- image -->

Status indicators:

PWR - steady green

RUN - off (not executing)

FAULT - steady red

LOCK - steady green

COM - off

The behavior of the IN and OUT status indicators depends on whether the configuration is verified:

- Verified - the IN and OUT status indicators continuously cycle through the verification number.
- Not Verified - the IN 0 and the OUT 1, 2, 3 and 4 are steady green. The backup cannot take place since the configuration is not verified.
5. Press the Backup button on the 2080-MEMBAK-RTC memory module with a small screwdriver. Hold the button until the status indicator on the 2080-MEMBAK-RTC memory module begins flashing, which indicates the backup process has begun. When the backup operation is complete, the status indicator on the 2080-MEMBAK-RTC memory module stops flashing.

<!-- image -->

If the status indicator does not flash and turns on after 15 seconds, the program is not verified and backup cannot take place.

6. Confirm the Verification ID displayed on the safety relay match the expected Verification ID of the application to be backed up.

7. Power down the CR30 safety relay.
8. Remove the 2080-MEMBAK-RTC memory module from slot 1 of the safety relay module bay.
9. Snap the dust cover or previous plug-in module into slot 1 of the module bay.
10. Power on the CR30 safety relay to resume normal operation.

## Restore Project

You can use the buttons on the memory module and safety relay to restore a CR30 safety relay project from a 2080-MEMBAK-RTC memory module.

1. Power down the CR30 safety relay.
2. Remove the dust cover or plug-in module in slot 1, the leftmost slot, of the safety relay module bay.
3. Snap the 2080-MEMBAK-RTC memory module into slot 1 of the module bay.
4. Power on the CR30 safety relay.
5. The safety relay detects the presence of the 2080-MEMBAK-RTC memory module and enters a fault state. The Fault status indicator is steady red and the application logic is not executed.

<!-- image -->

Status indicators: PWR - steady green RUN - off (not executing) FAULT - steady red LOCK - steady green COM - off

The behavior of the IN and OUT status indicators depends on whether the configuration is verified:

- Verified - the IN and OUT status indicators continuously cycle through the verification number of the configuration that is currently run by the CR30 safety relay.
- Not Verified - the IN 0 and the OUT 1, 2, 3 and 4 are steady green. The restore can take place since the configuration being downloaded is verified.
5. Press and hold the MEM/ID button that is on the CR30 safety relay just below the USB port.
6. While holding the MEM/ID button, use a small screwdriver to press the Backup button on the 2080-MEMBAK-RTC memory module. Hold both buttons until the status indicator on the memory module begins to flash (approximately 5 seconds) which indicates the restore process has begun.

<!-- image -->

You do not have to hold the Backup button down until the flashing stops.

When the restore operation is complete, the status indicator on the 2080-MEMBAK-RTC memory module stops flashing. The status indicators on the CR30 safety relay begin to cycle through each of the verification digits of the application that is restored to the safety relay from the memory module.

7. Confirm the Verification ID displayed on the safety relay match the expected Verification ID of the application to be restored from the memory module.
8. Power down the CR30 safety relay.
9. Remove the 2080-MEMBAK-RTC memory module from slot 1of the safety relay module bay.
10. Snap the dust cover or previous plug-in module into slot 1 of the module bay.
11. Power on the CR30 safety relay to resume normal operation.

## Overview

## Report Generator

## Reports

The Connected Components Workbench™ software allows you to generate a report using Microsoft® Word automatically. The report is editable, which allows you to add more information or combine the report with other documents for the safety technical file.

The Report Generator button is at the top of the logic editor. Click the icon that looks like a printer to generate a report.

Figure 147 - Report Icon at Top of Logic Editor

<!-- image -->

The report generator takes a snapshot of the logic editor as viewed by the operator. If the editor is actively monitoring the configuration, the report generator captures the colors reflected the block status. You can expand or collapse the blocks as desired to show or hide the advanced setting of each block.

<!-- image -->

Figure 148 - Report Output Settings

<!-- image -->

Media:

RS232 no handshake

Data Bits:

81

Vendor Name:

Allen-Bradley

Catalog ID:

2080-IQ40B4

1.004

Vendor Name:

Allen-Bradley

Catalog ID:

2080-OW41

Firmware Version:

1.004

2014-09-27

Select the desired output type, orientation, image options, header/footer options, and output file location and name. If a report with the same name exists, you are prompted to overwrite it.

An example of a report is shown in Figure 149 .

## Figure 149 - Example Report

| Type Filter                    | Value    |
|--------------------------------|----------|
| SafetyMonitoringFunctionStatus | SMF1     |
| SafetyMonitoringFunctionStatus | SMF2     |
| SafetyMonitoringFunctionStatus | SMF3     |
| SafetyMonitoringFunctionStatus | SMF4     |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Type Filter                    | Value    |
| Safety Output Function Status  | SOF1     |
| Safety Output Function Status  | SOF2     |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |
| Not Used                       | Not Used |

Page1

<!-- image -->

## SIL Rating

## Performance Level/ Category

## Specifications

The CR30 safety relay meets the requirements of SIL CL 3 in accordance with IEC/EN 61508.

Table 25 - SIL Rating

| Attribute Value                                                             |
|-----------------------------------------------------------------------------|
| Safety integrity level claim limit 3                                        |
| PFD  1.76 10-3 (whole safety function)                                      |
| PFH  1 10-8                                                                 |
| Mode of operation High-demand mode                                          |
| Safety-related subsystems Type B (use of programmable / complex components) |
| Hardware fault tolerance HFT = 1 (two-channel system)                       |
| Safe failure fraction 90…99%                                                |

The Performance Level of the safety function is dependent on the structure of all devices that comprise the safety function.

The CR30 safety relay can be used in safety systems that meet up to Category 4 and Performance Level PLe in accordance with ISO 13849-1.

| Attribute Value           |
|---------------------------|
| Category Up to 4          |
| Performance Level Up to e |

Table 26 - Performance Level/Category

<!-- image -->

## General

## Environmental

## Inputs

| Attribute Value                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of I/O 22                                                                                                                                 |
| Dimensions 90 mm x 100 mm x 80 mm (3.54 in. x 3.94 in. x 3.15 in.)                                                                               |
| Shipping weight, approx  0.423 kg (0.933 lb)                                                                                                     |
| Wire size 0.2…2.5 mm 2 (24…12 AWG) solid copper wire or 0.2…2.5 mm 2 (24…12 AWG) stranded copper wire ° rated at 90 °C (194 °F) insulation, max                                                                                                                                                  |
| Wiring category 2 on signal ports 2 on power ports Use this Conductor Category information to plan conductor routing. See publication 1770-4.1 . |
| Insulation-stripping length 7 mm (0.28 in.)                                                                                                      |
| Terminal screw torque, max  0.6 N•m (4.4 lb•in) Use a 2.5 mm (0.10 in.) screwdriver                                                              |
| Input circuit type 24V DC source                                                                                                                 |
| Output circuit type 24V DC source                                                                                                                |
| Power supply voltage range  24V DC +10% -15% (1)                                                                                                 |
| Reverse polarity protection Yes                                                                                                                  |
| Fuse specification 6 A                                                                                                                           |
| Power consumption 5.28 W                                                                                                                         |
| I/O rating  Input 24V DC, 4 mA Output 24V DC, Class 2, 0.5 A per point                                                                           |
| Enclosure type rating IP20                                                                                                                       |

| Attribute Value                              |
|----------------------------------------------|
| Temperature, operating -5…+55 °C (23…131 °F) |
| Relative humidity 90%                        |
| Vibration 10…55 Hz, 0.35 mm (0.001 in.)      |
| Shock 10 g, 16 ms                            |
| Pollution level 2                            |

| Attribute Value                                                                                |
|------------------------------------------------------------------------------------------------|
| Number of inputs 12 dedicated inputs                                                           |
| Operating voltage range 20.4…26.V DC                                                           |
| Off-state voltage, max 5V DC                                                                   |
| Off-state current, max 2.91 mA (independent of supply)                                         |
| On-state voltage, max 26.4V DC                                                                 |
| On-state voltage, min 11.0V DC                                                                 |
| On-state current, min 3.14 mA at 20.4V DC                                                      |
| On-state current, nom 3.2 mA at 24V DC                                                         |
| On-state current, max 3.25 mA at 26.4V DC                                                      |
| Off-pulse accepted for OSSD setting without declaring the input as off Min = 0 µs Max = 700 µs |
| Reverse voltage protection No                                                                  |
| Input capacitance 10 nF                                                                        |
| Galvanic isolation: I/O from Logic No                                                          |

## Outputs

## Reaction Times

## Recovery Times

## Response Times

## System Response Time Calculation

| Attribute Value                                |                                                            |
|------------------------------------------------|------------------------------------------------------------|
| Number of outputs Up to 10                     |                                                            |
|                                                | Output signals Standard, OSSD, and single wire safety      |
| Continuous output current                      | 0.5 A (Terminals 12…19) 0.3 A (Terminals 20…21)            |
| Aggregate current of outputs per device (max)  | 3 A                                                        |
| Surge output current 1 A                       |                                                            |
| Surge output current duration 5 ms             |                                                            |
| Residual voltage (drop from power supply), max | 0.2V DC                                                    |
| Load capacitance, max                          | 200 nF / 20 mA load 100 nF / 10 mA load 22 nF without load |
| Off-state leakage current, max < 0.1 mA        |                                                            |
| Short circuit detection Yes                    |                                                            |
| Short circuit protection Yes                   |                                                            |
| Galvanic isolation: I/O from Logic No          |                                                            |
| Pulse test duration                            | ≤ 700 µs                                                   |
| Pulse test period                              | ≤ 13,000 ms (less than 15 s)                               |

| Attribute Value          |                                                          |
|--------------------------|----------------------------------------------------------|
| Safety input             | Automatic reset < 100 ms Manual monitored reset < 500 ms |
| Single wire safety input | Automatic reset < 100 ms Manual monitored reset < 500 ms |
| Safety mats              | Automatic reset < 100 ms Manual monitored reset < 500 ms |

| Attribute Value                                                          |
|--------------------------------------------------------------------------|
| To trigger inputs again Response time as demand + reaction time + 100 ms |

| Attribute Value                        |
|----------------------------------------|
| Safety input 45 ms + input filter time |
| Single wire safety input < 45 ms       |
| Safety mats < 70 ms                    |
| Single wire safety output < 60 ms      |
| Output loop 25 ms                      |

The safety response time is the time that is required to establish the safe state of the safety output function with consideration to the demand of the safety monitor function and/or occurrence of faults and failures in the safety chain. The overall response time of the safety function considers the whole safety chain, including the safety input device, logic device, and actuator. The safety response time is used to calculate the safety distance, distance between a safeguarding device, and the hazardous area.

The following paths have to be considered:

<!-- image -->

## Response Time - Demand of the Safety Function

The safety response time of the CR30 safety relay is the screw-to-screw response time to turn off a safety output at demand of the safety function by the safety input device. The safety response has to be calculated for each safety monitor function. Table 27 shows the possible safety chain with all considerable response times.

Table 27 - Safety Chain Response Times

|                                                                                                                | Description Where to Find Value                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Safety sensors Safety response time of sensor device Sensor operating manual                                   |                                                 |
| SMF Specific Processing time of safety monitor function configured in Connected Components Workbench™ software | Table 28 (SMF process times)                    |
| Input filter Configured Input Filter time                                                                      | From SMF configuration (advanced settings)  (1) |
| Logic  Internal execution time to process input signal, routing, and output processing  (2)                    | From technical specification 45 ms              |
| SOF Configured Off-Delay time From SOF configuration                                                           |                                                 |
| Actuator Safety switching device controlling the load Actuator operating manual                                |                                                 |
|                                                                                                                | Total                                           |

## Table 28 shows the additional processing time of dedicated SMF

Table 28 - Process Time

|                                            | SMF Description SMF response time                                  |
|--------------------------------------------|--------------------------------------------------------------------|
| Emergency stop Enabling switch Gate switch | SMF inputs deactivated 0 ms                                        |
| Safety light curtain Alternative device    | Muting — 0 ms                                                      |
|                                            | Safety light curtain Light interrupted, not muted 0 ms             |
| Override                                   | Deactivate override when safety light curtain is interrupted  0 ms |

Table 28 - Process Time (Continued)

|                                                                | SMF Description SMF response time   |
|----------------------------------------------------------------|-------------------------------------|
| Safety mats  Step on Mat, cross loop between safety mat inputs | 25 ms                               |
| Single wire safety Deactivated SWS signal 15 ms                |                                     |
| Two-hand control Release of at least one hand actuator 0 ms    |                                     |

Figure 151 - Example

<!-- image -->

Table 29 - For SMF1 - E-stop

| Comment Value                                                                                           |              |
|---------------------------------------------------------------------------------------------------------|--------------|
| Safety sensors  Safety response time of sensor device - considered as 0 ms since mechanical device only | 0 ms         |
| SMF An E-stop SMF does not require extra process time 0 ms                                              |              |
| Input filter Advanced settings > Input filter - 10 x 25 ms = 250 ms 250 ms                              |              |
| Logic  Internal execution time to process input signal, routing, and output processing                  | 45 ms        |
| SOF Configured off-delay time - immediate off 0 ms                                                      |              |
| Actuator Assuming a contactor with a response time of 30 ms 30 ms                                       |              |
|                                                                                                         | Total 325 ms |

A demand of the E-stop forces a safe state after 325 ms.

Table 30 - For SMF2 - Safety Mat

|                | Comment Value                                                                           |              |
|----------------|-----------------------------------------------------------------------------------------|--------------|
| Safety sensors | Safety response time of sensor device - considered as 0 ms since mechanical device only | 0 ms         |
|                | SMF Safety mat process time 25 ms                                                       |              |
|                | Input filter Advanced settings > Input filter - 0 ms 0 ms                               |              |
| Logic          | Internal execution time to process input signal, routing, and output processing         | 45 ms        |
|                | SOF Configured off-delay time - immediate off 0 ms                                      |              |
| Actuator       | The safety mat SMF and the E-stop control the same contactor                            | 30 ms        |
|                |                                                                                         | Total 100 ms |

A demand of the Safety Mat forces a safe state after 100 ms.

## Monitor Time - Occurrence of Recoverable Faults and Failures

Recoverable faults as defined earlier (see Troubleshooting on page 133) are faults and failures within the connected periphery of the CR30 safety relay. The ability to detect faults depends on the wiring, the type of sensor, and the signal evaluation function that is applied to the circuit. The monitoring time is the amount of time to evaluate the fault or failure after detection and to initiate the appropriate system response. To recover recoverable faults, remove the fault and cycle the appropriate input circuit.

The detection of a recoverable fault does not lead to the loss of the safety function. When the safety function is demanded during the monitoring time, after the occurrence of a recoverable fault, the system responds within the safety response time according to the response time considerations of this safety function (see System Response Time Calculation on page 153).

<!-- image -->

Monitor measures that are provided by the CR30 safety relay to the periphery define the diagnostic coverage of the application and thus the safety rating. Internal monitoring measures related to a fail-safe design of the CR30 safety relay are only related to the safety integrity of the CR30 safety relay itself, see nonrecoverable faults.

Examples of recoverable faults include the following.

- Cross loop and shorts to 24V and COM faults
- Input discrepancy
- Muting: Synchronization times exceed
- Muting time exceeded
- Muting sequence fault
- Two-hand discrepancy fault
- Reset/Restart timing fault

The evaluation method of the input or output signal depends on the configuration of the SMF and SOF in Connected Components Workbench software and the wiring of the sensor. Table 31 shows typical evaluation functions and required settings to be enabled.

Table 31 - Evaluation Method

<!-- image -->

Table 31 - Evaluation Method (Continued)

<!-- image -->

## Test Pulse Evaluation

Integral test pulses are applied to the input circuit of the safety sensor with electromechanical outputs. The test pulse output signal becomes the input signal of a safety input through the contacts of the safety sensor. Sensors with electronic OSSDe (output safety switching device electronic) semiconductor outputs have their own test pulses and do not require the logic device to source a test pulse evaluation.

IMPORTANT

In case the same test pulse output sources multiple input circuits, a fault affects all inputs that are connected to this output.

## Multi-Channel Signal Evaluation and Discrepancy Monitoring

Independent of the test pulse evaluation or sensor type, components can be wired in a single-channel, dual-channel, or even three-channel structure. In a dual or three-channel structure, all channels must be active to enable the SMF. When at least one of the channels is disabled, the safety function is demanded. These channels can be monitored against discrepancy.

The discrepancy time is the amount of time that the input channels of an SMF are allowed to be in an inconsistent state before an instruction fault is generated. The discrepancy time cannot be set in Single Channel mode.

## Sequence and Timing Faults

Typically applied to specialty safety functions such as Muting or Two-hand control. It monitors the sequence of events to evaluate the validity of input signals to enable the SMF.

## Integral Test Pulses of Safety Outputs

Test pulses are applied to safety outputs to detect faults within the connected periphery such as short circuits to 24V of 0V or cross-loop faults between two output sources. Integral pulses on safety outputs are also used to confirm the safety integrity of the output itself, such as the ability to switch off. An output fault, internal or external, always requires a power cycle to test if the fault is recoverable or not.

## IMPORTANT

To verify the ability to switch off actuator devices if there are short circuits to 24V DC within the control line of one actuator, it is recommended to use a pair of safety outputs controlling two redundant switching actuators. Once the fault is detected, a second channel is able to switch off the load. Fault exclusions of potential short-circuits between two conductors are also possible when following the requirements for fault exclusions according to EN ISO 13849-2 Table D.3 and D.4, among others protection (for example, cable conduit) and separated wiring of safety signals.

The overall monitoring time to evaluate a fault and initiate a system response, after the occurrence of a recoverable fault must consider any specific-fault process times depending on the I/O evaluation method and configured input filter times. Table 32 shows the response time for specific recoverable faults, if the safety function is not demanded, and the required settings of SMF and SOF to enable the proper fault evaluation method.

Table 32 - Process Time of Recoverable Faults and Required Settings

|                                                       | Recoverable Fault Detection Enabled by Process Time                          |                                                |
|-------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------|
| Cross loop fault                                      | Inputs: 2 N.C. Pulse testing: 2 Sources                                      | 3 s                                            |
| Short circuit fault                                   | Inputs: 1 N.C., or 2 N.C. Pulse testing: 1 Source, 2 Sources                 | 3 s                                            |
| Input discrepancy fault                               | Inputs: 2 N.C., 2 OSSD Discrepancy time: >0…3 s                              | Discrepancy time + input filter time           |
| Reset/restart timing fault Default: 0.25…3 s          |                                                                              | 0 s (1)                                        |
| Non-retriggerable timer fault Retriggerable: Disabled |                                                                              | Configured time delay  (2)                     |
| Muting: Synchronization time exceeded                 | Synch time: 0.05…10 s Muting sensors input filter: 0…3 s                     | Maximum sync time  (3) + 2 x input filter time |
|                                                       | Muting time exceeded Maximum mute time: 1 s…10 days Configured max mute time |                                                |
| Muting sequence fault                                 | Muting type: 2 Sensor T-type, 2 Sensor L-type, 4 sensor                      | Input filter time                              |

(1) A reset/restart timing fault can only occur when safety outputs are off, so there is no impact on the safety response time

(2) The maximum of the configured delay must be considered. The remaining time at occurrence of fault will lapse.

(3) The synchronization time between the muting sensors, and between muting sensor can be set individually. The longest synchronization must be considered.

Table 33 - Response time of the Safety Chain at Occurrence of Recoverable Faults without a Demand of the Safety Function

|                                                                                             | Description Where to Find Value                               |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| SMF Fault processing                                                                        | Table 32, according to configured input evaluation of the SMF |
| Logic  Internal execution time to process input signal, routing, and output processing  (1) | From technical specification 45 ms (fix)                      |
| SOF Fault process time and configured time delay From SOF configuration                     |                                                               |
| Actuator Safety switching device controlling the load Actuator Operating manual             |                                                               |
|                                                                                             | Total                                                         |

(1) The internal execution time is static and independent of the number of function blocks that are configured for the safety function.

Figure 152 - Example

<!-- image -->

Table 34 - Consideration for Recoverable Faults of E-stop Safety Function

| Description Value                                                                           |
|---------------------------------------------------------------------------------------------|
| SMF Cross loop fault: 3 s according to above table 3 s                                      |
| Logic Internal execution time to process input signal, routing, and output processing 45 ms |
| SOF No off delay configured 0 s                                                             |
| Actuator Assuming a contactor with a response time of 30 ms 30 ms                           |
| Total 3.075 s                                                                               |

## Response Time - Occurrence of Nonrecoverable Faults and Failures

Internal monitoring measures applied to monitor the safety integrity of the system detect nonrecoverable faults. These faults are independent of the logic configuration. Once detected the CR30 safety relay forces the safe state within the internal process cycle time of 45 ms.

## Reaction Time

The reaction time is the time to enable the safety output function when you activate the safety input devices and perform a valid reset operation. The overall reaction time of the safety function considers the whole safety chain, including the safety input device, logic device, and actuator. The reaction time must be calculated for each safety function.

Table 35 shows the possible chain with all considerable reaction times for a safety function.

Table 35 - Safety Function Reaction Times

|               |                                                                                      | Description Where to Find Value                                |                        |
|---------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------|------------------------|
|               | Feedback Feedback input filter time                                                  | From SMF configuration (advanced settings)  (1)                |                        |
|               | Safety sensors Reaction time of sensor device Sensor operating manual                |                                                                |                        |
|               | SMF Configured input filter time                                                     | From SMF configuration (advanced settings)  (1)                |                        |
| Reset/restart | Reset/restart pulse time + 2 x filter time (2)                                       | Reset pulse: 3 s, max Input filter time from SMF configuration | 3 s + 2 x input filter |
| Logic         | Internal execution time to process input signal, routing, and output processing  (3) | From technical specification 100 ms                            |                        |
|               | SOF Configured on-delay time From SOF configuration                                  |                                                                |                        |
| Actuator      | Safety switching device controlling the load                                         | Actuator Operating manual                                      |                        |
|               |                                                                                      | Total                                                          |                        |

- (3) The internal execution time is static and independent of the number of function blocks that are configured for the safety function.

Figure 153 - Example 1

<!-- image -->

Table 36 - For SMF1 - E-stop

| Comment Value                                                                                        |
|------------------------------------------------------------------------------------------------------|
| Feedback Disabled for SOF 0 ms                                                                       |
| Safety sensors Reaction time of sensor device - considered as 0 ms since mechanical device only 0 ms |
| SMF Configured input filter time 10x 25 ms = 250 ms 250 ms                                           |
| Reset/restart SOF configured for Automatic 0 s                                                       |
| Logic Internal execution time to process input signal, routing, and output processing 2) 100 ms      |
| SOF No on-delay is configured for SOF 0 s                                                            |
| Actuator Assuming a contactor with a response time of 10 ms 10 ms                                    |
| Total 360 ms                                                                                         |

It takes 360 ms to enable the outputs when the E-stop is active (closed contacts).

Table 37 - For SMF2 – Safety Mat

| Comment Value                                                                                        |
|------------------------------------------------------------------------------------------------------|
| Feedback Disabled for SOF 0 ms                                                                       |
| Safety sensors Reaction time of sensor device - considered as 0 ms since mechanical device only 0 ms |
| SMF Input filter disabled 0 ms                                                                       |
| Reset/restart SOF configured for automatic 0 ms                                                      |
| Logic Internal execution time to process input signal, routing, and output processing 2) 100 ms      |
| SOF No on-delay is configured for SOF 0 s                                                            |
| Actuator Assuming a contactor with a response time of 10 ms 10 ms                                    |
| Total 110 ms                                                                                         |

It takes 110 ms to enable the outputs when the Safety Mat is released.

Figure 154 - Example 2 (1)

<!-- image -->

Table 38 - For SMF1 - E-stop

| Comment Value                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback Configured Input Filter time 10x 25 ms = 250 ms 250 ms                                                                                           |
| Safety sensors Reaction time of sensor device - considered as 0 ms since mechanical device only 0 ms                                                      |
| SMF Configured Input Filter time 10x 25 ms = 250 ms 250 ms                                                                                                |
| Reset/restart  Min: 2 x input filter time + 250 ms = 500 ms + 250 ms = 0.75 s Max: 2 x input filter time + 3 s = 0.5 + 3 s = 3.5 s Min: 0.75 s Max: 3.5 s |
| Logic Internal execution time to process input signal, routing, and output processing 2) 100 ms                                                           |
| SOF No on-delay is configured for SOF 0 s                                                                                                                 |
| Actuator Assuming a contactor with a response time of 10 ms 10 ms                                                                                         |
| Total  Min: 1.36 s Max: 4.11 s                                                                                                                            |

It takes a minimum of 1.36 s, after a valid Reset operation of at least 250 ms to enable the outputs when the E-stop is active (closed contacts).

Table 39 - For SMF2 - Safety Mat

| Comment Value                                                                                                                      |                         |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Feedback Configured input filter time 10x 25 ms = 250 ms 250 ms                                                                    |                         |
| Safety sensors  Reaction time of sensor device - considered as 0 ms since mechanical device only                                   | 0 ms                    |
| SMF Input filter disabled 0 ms                                                                                                     |                         |
| Reset/restart  Min: 2 x input filter time + 250 ms = 500 ms + 250 ms = 0.75 s Max: 2 x input filter time + 3 s = 0.5 + 3 s = 3.5 s | Min: 0.75 s Max: 3.5 s  |
| Logic Internal execution time to process input signal, routing, and output processing 2) 45 ms                                     |                         |
| SOF No on-delay is configured for SOF 0 s                                                                                          |                         |
| Actuator Assuming a contactor with a response time of 10 ms 10 ms                                                                  |                         |
| Total                                                                                                                              | Min: 1.055 s Max: 3.3 s |

It takes a minimum of 1055 s, after a valid reset operation of at least 250 ms to enable the outputs when the E-stop is active (closed contacts).

## 440C-ENET Plug-in module Specifications

The following are specifications for the Guardmaster® 440C-ENET Ethernet plug-in module.

Table 40 - Technical Specifications

| Specification Description                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module location Slot 1 module bay only.                                                                                                                                                 |
| Backplane current (mA) at 24V DC 42 mA                                                                                                                                                  |
| Isolation voltage  50V DC, reinforced insulation type, Ethernet to system Type tested at 1500V AC for 60 s                                                                              |
| Power consumption, max 1 W                                                                                                                                                              |
| Thermal dissipation 3.41 BTU/hr at 65 °C (149 °F)                                                                                                                                       |
| Wire size Ethernet connections: RJ45 connector according to IEC 60603-7, 2 or 4 pair Category 5e minimum cable according to TIA 568-B.1 or Category 5 cable according to ISO/IEC 24702. |
| Wiring category  1 - on communication port (1)                                                                                                                                          |
| Enclosure type rating None (open-style)                                                                                                                                                 |

Table 41 - Environmental Specifications

| Specification Description                                                                                                                                                                                       |                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating • IEC 60068-2-1 (Test Ad, operating cold) • IEC 60068-2-2 (Test Bd, operating dry heat) • IEC 60068-2-14 (Test Nb, operating thermal shock)                                              | -20…+65 °C (-4…+149 °F)                                                                                                                                 |
| Temperature, nonoperating • IEC 60068-2-1 (Test Ab, unpackaged nonoperating cold) • IEC 60068-2-2 (Test Bb, unpackaged nonoperating dry heat) • IEC 60068-2-14 (Test Na, unpackaged nonoperating thermal shock) | -40…+85 °C (-40…+185 °F)                                                                                                                                |
| Relative humidity, operating • IEC 60068-2-30 (Test Db, unpackaged damp heat)                                                                                                                                   | 5…85% noncondensing                                                                                                                                     |
| Relative humidity, nonoperating • IEC 60068-2-30 (Test Db, unpackaged damp heat)                                                                                                                                | 5…95% noncondensing                                                                                                                                     |
| Vibration • IEC 60068-2-6 (Test Ea, unpackaged shock)                                                                                                                                                           | 2 g at 10…500 Hz                                                                                                                                        |
| Shock, operating • IEC 60068-2-27 (Test Ea, unpackaged shock)                                                                                                                                                   | 25 g (DIN rail or panel mount)                                                                                                                          |
| Shock, nonoperating • IEC 60068-2-27 (Test Ea, unpackaged shock)                                                                                                                                                | • 25 g (DIN rail mount) • 35 g (panel mount)                                                                                                            |
| Emissions • CISPR 11                                                                                                                                                                                            | Group 1, Class A                                                                                                                                        |
| Immunity, ESD • IEC 6100-4-2                                                                                                                                                                                    | • 6 kV contact discharges • 8 kV air discharges                                                                                                         |
| Immunity, radiated RF • IEC 61000-4-3                                                                                                                                                                           | • 10V/m with 1-kHz sine wave 80% AM from 80…2700 MHz • 10V/m with 200 Hz 50% Pulse 100% AM at 900 MHz • 10V/m with 200 Hz 50% Pulse 100% AM at 1890 MHz |
| Immunity, EFT/B • IEC 61000-4-4                                                                                                                                                                                 | ±1 kV at 5 kHz on Ethernet port                                                                                                                         |
| Immunity, surge transient • IEC 61000-4-5                                                                                                                                                                       | ±1 kV line-earth(CM) on Ethernet port                                                                                                                   |
| Immunity, conducted RF • IEC 61000-4-6                                                                                                                                                                          | 10V rms with 1-kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                 |

Table 42 - Certifications

| Certification Description   |                                                                                                                                                                                                                                                                      |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cULus                       | UL Listed Industrial Control Equipment, which is certified for US and Canada. See UL File E361015.                                                                                                                                                                   |
| CE                          | 2014/30/EU EMC and 2006/42/EC MD Directive, compliant with: • EN 61326-1; Meas./Control/Lab., Industrial Requirements • EN 61000-6-2; Industrial Immunity • EN 61000-6-4; Industrial Emissions • EN 60947-1; Auxiliary Devices • EN ISO 13849-1; Safety of Machinery |
| UKCA                        | European Union 2004/108/EC EMC Directive, compliant with: • EN 61326-1; Meas./Control/Lab., Industrial Requirements • EN 61000-6-2; Industrial Immunity • EN 61000-6-4; Industrial Emissions • EN 60947-1; Auxiliary Devices • EN ISO 13849-1; Safety of Machinery   |
| C-Tick                      | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                                            |
|                             | EtherNet/IP ODVA conformance tested to EtherNet/IP™ specifications                                                                                                                                                                                                   |
|                             | TUV Rheinland Can be used in applications up to PL e and SIL 3                                                                                                                                                                                                       |

IMPORTANT

When product is marked, see rok.auto/certifications for Declarations of Conformity, Certificates, and other certification details

## Agency Certifications

## Declaration of Conformity

## Regulatory Approvals

- UL Listed Industrial Control Equipment (certified for US and Canada)
- CE Marked for all applicable EU directives
- UKCA marked for all applicable regulations
- C-Tick marked for all applicable acts
- S-Mark

## CE Conformity

Rockwell Automation declares that the products that are shown in this document conform with the 2014/30/EU Electromagnetic Compatibility Directive (EMC) and 2006/42/EC Machinery Directive (MD) and that the respective standards and/or technical specifications have been applied.

This product is intended for use in an industrial environment.

For a comprehensive CE certificate visit: rok.auto/certifications .

## UKCA Conformity

Rockwell Automation declares that the products that are shown in this document are in compliance with 2016 No. 1091 Electromagnetic Compatibility Regulations and 2008 No. 1597 Supply of Machinery (Safety) Regulations and that the respective standards and/or technical specifications have been applied.

This product is intended for use in an industrial environment.

For a comprehensive UKCA certificate visit: rok.auto/certifications .

<!-- image -->

## Notes:

## Overview

## Configuration Reference Document

The configuration reference document must be stored together with technical documentation of the machine. It includes information about the validity of a configuration that is created for the machine. This document must be updated anytime changes to the configuration have been made, validated, and verified.

Any new configuration or changes to an existing configuration require a validation and verification before putting it into service. An unverified application stops operating 24 hr after power-up.

With your signature you confirm that:

- You have validated and verified of the safety configuration, identified the previously mentioned details AND
- The configuration and installation meets all specified operational and environmental requirements of the machine to which CR30 safety relay is to be fitted AND
- You have read and understood the Important User Information on page 2

<!-- image -->

## Configuration Reference Document

## Device Information:

Device Name:

From Name Field, General View

Description:

From Description Field, General View

Vendor:

Allen-Bradley

Catalog ID:

440C-CR30-22BBB

Safety Relay Firmware Version:

Found in the Device Details Window of CCW

## Project Information:

Project Name:

As stored in the configuration tool

Project File Name: From file name

Software revision:

From Help -&gt; About CCW

Verification ID:

Generated in verification window

## Approval:

Project Developer Name:

Date:

Signature

## DMK Extraction

## ControlFLASH Firmware Update

## IMPORTANT

Before updating the firmware, verify that the CR30 safety relay is in Program mode.

Beginning with firmware revision 10.009, the CR30 safety relay firmware update is issued as a Device Management Kit, or a DMK (.dmk) file.

A DMK is a digitally signed file that contains the firmware. ControlFLASH™ authenticates the DMK file's origin and then validates the contents, which provides enhanced protection against malicious threats. Simply download the DMK file and then run the DMK extractor; there is no need to install or extract the file. For more information, see publication 1756-UM105J-EN-P .

1. Navigate to the Rockwell Automation Product Compatibility and Download Center (PCDC) at https:// compatibility.rockwellautomation.com/Pages/ MultiProductDownload.aspx?Keyword=Free&amp;crumb=112 .
2. Type 440C in the search field and click the search icon.
3. Select the firmware revision that you wish to download. Follow the download instructions.

## Figure 155 - Rockwell Automation Download Website

<!-- image -->

The downloaded file is named, for example, 440C-CR30-22BBB\_10.009.dmk, for easy identification and management.

4. Click the Windows® Start icon.

<!-- image -->

## ControlFLASH

5. As shown in Figure 156, expand the Flash Programming Tools and click the DMK Extraction Tool.

## Figure 156 - Access DMK Extraction Tool

<!-- image -->

6. Figure 157 shows an example of the DMK Extraction Tool and the files that are discovered in the default directory: C:\Program File (x86)\ControlFLASH. If necessary, use the Browse function to select another directory. Check the files that you wish to extract and click Extract.

## Figure 157 - DMK Extraction Tool

<!-- image -->

7. Figure 158 shows that the extraction succeeded. Now the firmware is ready to be downloaded into a CR30 safety relay. Click OK.

## Figure 158 - Extraction Status

<!-- image -->

ControlFLASH version 13.00 or later is required to download the DMK firmware to the CR30 safety relay.

1. Click the Windows Start icon.
2. Expand the FLASH Programming Tools and click ControlFLASH.

## Figure 159 - Access ControlFLASH.

<!-- image -->

3. Shown in Figure 160 on page 173, from the welcome screen you can view the log, check the inventory of firmware releases, and change from RSLinx® Classic to FactoryTalk® Linx, if necessary. Click Next.

## Figure 160 - ControlFlash Welcome Screen

<!-- image -->

4. Figure 161 shows the list of catalog numbers available for update. Highlight the CR30 safety relay catalog and click Next.

## Figure 161 - Target Catalog Numbers List

<!-- image -->

5. Figure 162 shows the devices using RSLinx. In this example, the highlighted CR30 safety relay is connected through an EtherNet/IP™ connection. A second CR30 safety relay is connected with a USB cable through the AB\_VBP-1 connection. Select the desired CR30 safety relay and click Next.

## Figure 162 - RSLinx

<!-- image -->

6. The example in Figure 163 shows the current revision of the selected CR30 safety relay (10.010) and a list of firmware revisions that reside in the inventory. Highlight the latest revision (10.011) and click Next.

## Figure 163 - Firmware Revision Screen

<!-- image -->

7. The example summery screen in Figure 164 on page 174 shows the summery of changes, the current and new revisions, and a DANGER message. If no danger exists, click Finish to initiate the update.

## Figure 164 - Summary

<!-- image -->

## IMPORTANT

If you see the following message, check the mode of the CR30 safety relay. ControlFLASH cannot be performed when the CR30 safety relay is in Run mode. Change the CR30 safety relay to Program mode and repeat the steps.

<!-- image -->

8. The example in Figure 165 shows a successful update. Click OK.

## Figure 165 - Update Status

<!-- image -->

## Input Assemblies

Table 43 - CR30 Safety Relay Input Assemblies

| Instance Decimal (hex)   | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                               |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|--------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------|--------------------------|----------------------|----------------------|
| 100 (64 h)               | 0 Reserved Minor Fault Major Fault                                                                 | Run mode                                                                                          | 0 Reserved Minor Fault Major Fault                                    | Connection Faulted                                                                                |                          |                          |                      |                      |
| 100 (64 h)               | 1 Reserved                                                                                         | 1 Reserved                                                                                        | 1 Reserved                                                            | 1 Reserved                                                                                        | 1 Reserved               | 1 Reserved               | 1 Reserved           | 1 Reserved           |
| 100 (64 h)               | High Byte Low Byte                                                                                 | High Byte Low Byte                                                                                | High Byte Low Byte                                                    | High Byte Low Byte                                                                                | High Byte Low Byte       | High Byte Low Byte       | High Byte Low Byte   | High Byte Low Byte   |
| 100 (64 h)               | 2, 3 Verification ID                                                                               | 2, 3 Verification ID                                                                              | 2, 3 Verification ID                                                  | 2, 3 Verification ID                                                                              | 2, 3 Verification ID     | 2, 3 Verification ID     | 2, 3 Verification ID | 2, 3 Verification ID |
| 100 (64 h)               | Major fault type  (1)                                                                              | Major fault type  (1)                                                                             | Major fault code  (1)                                                 | Major fault code  (1)                                                                             | Major fault code  (1)    | Major fault code  (1)    |                      |                      |
| 100 (64 h)               | Minor fault type (1)                                                                               | Minor fault type (1)                                                                              | Minor fault instance (1)                                              | Minor fault instance (1)                                                                          | Minor fault instance (1) | Minor fault instance (1) |                      |                      |
| 100 (64 h)               | Minor fault code (1)                                                                               | Minor fault code (1)                                                                              | Minor fault code (1)                                                  | Minor fault code (1)                                                                              | Minor fault code (1)     | Minor fault code (1)     | Minor fault code (1) | Minor fault code (1) |
| 100 (64 h)               |                                                                                                    |                                                                                                   | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                  |                                                                                                   |                          |                          |                      |                      |
| 100 (64 h)               |                                                                                                    | 10 Pt 07 Data Pt 06 Data Pt 05 Data Pt 04 Data Pt 03 Data Pt 02 Data Pt 01 Data Pt 00 Data        |                                                                       |                                                                                                   |                          |                          |                      |                      |
| 100 (64 h)               | 11 Pt 15 Data Pt 14 Data Pt 13 Data Pt 12 Data Pt 11 Data Pt 10 Data Pt 09 Data Pt 08 Data         |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
| 100 (64 h)               | 12 Reserved Pt 21 Data Pt 20 Data Pt 19 Data Pt 18 Data Pt 17 Data Pt 16 Data                      | 12 Reserved Pt 21 Data Pt 20 Data Pt 19 Data Pt 18 Data Pt 17 Data Pt 16 Data                     |                                                                       |                                                                                                   |                          |                          |                      |                      |
| 100 (64 h)               | Plug-in 2 Pt 07 Data                                                                               | Plug-in 2 Pt 05 Data Plug-in 2 Pt 02 Data Plug-in 2 Pt 00 Data                                    | 13  Plug-in 2 Pt 06 Data Plug-in 2 Pt 04 Data Plug-in 2 Pt 03 Data    | Plug-in 2 Pt 01 Data                                                                              |                          |                          |                      |                      |
|                          | 14 SMF 8 Data SMF 7 Data SMF 6 Data SMF 5 Data SMF 4 Data SMF 3 Data SMF 2 Data SMF 1 Data         |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | 15 SMF 16 Data SMF 15 Data SMF 14 Data SMF 13 Data SMF 12 Data SMF 11 Data SMF 10 Data SMF 9 Data  |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | 16 SMF 24 Data SMF 23 Data SMF 22 Data SMF 21 Data SMF 20 Data SMF 19 Data SMF 18 Data SMF 17 Data |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | 17 LLA 8 Data LLA 7 Data LLA 6 Data LLA 5 Data LLA 4 Data LLA 3 Data LLA 2 Data LLA 1 Data         |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | 18 LLA 16 Data LLA 15 Data LLA 14 Data LLA 13 Data LLA 12 Data LLA 11 Data LLA 10 Data LLA 9 Data  |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | 19 LLB 8 Data LLB 7 Data LLB 6 Data LLB 5 Data LLB 4 Data LLB 3 Data LLB 2 Data LLB 1 Data         |                                                                                                   |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          |                                                                                                    |                                                                                                   |                                                                       | 20 LLB 16 Data LLB 15 Data LLB 14 Data LLB 13 Data LLB 12 Data LLB 11 Data LLB 10 Data LLB 9 Data |                          |                          |                      |                      |
|                          | 21 SOF 8 Data SOF 7 Data SOF 6 Data SOF 5 Data                                                     |                                                                                                   |                                                                       | SOF 4 Data SOF 3 Data SOF 2 Data SOF 1 Data                                                       |                          |                          |                      |                      |
|                          |                                                                                                    | 22 SOF 16 Data SOF 15 Data SOF 14 Data SOF 13 Data SOF 12 Data SOF 11 Data SOF 10 Data SOF 9 Data |                                                                       |                                                                                                   |                          |                          |                      |                      |
|                          | SOF 8 Reset Required                                                                               | SOF 6 Reset Required SOF 3 Reset Required SOF 1 Reset Required                                    | 23  SOF 7 Reset Required SOF 5 Reset Required SOF 4 Reset Required    | SOF 2 Reset Required                                                                              |                          |                          |                      |                      |
|                          | SOF 16 Reset Required                                                                              | SOF 14 Reset Required SOF 11 Reset Required SOF 9 Reset Required                                  | 24  SOF 15 Reset Required SOF 13 Reset Required SOF 12 Reset Required | SOF 10 Reset Required                                                                             |                          |                          |                      |                      |
|                          | 25 Reserved                                                                                        | 25 Reserved                                                                                       | 25 Reserved                                                           | 25 Reserved                                                                                       | 25 Reserved              | 25 Reserved              | 25 Reserved          | 25 Reserved          |
|                          | 26 Reserved                                                                                        | 26 Reserved                                                                                       | 26 Reserved                                                           | 26 Reserved                                                                                       | 26 Reserved              | 26 Reserved              | 26 Reserved          | 26 Reserved          |
|                          | 27 Reserved                                                                                        | 27 Reserved                                                                                       | 27 Reserved                                                           | 27 Reserved                                                                                       | 27 Reserved              | 27 Reserved              | 27 Reserved          | 27 Reserved          |

## Where:

· Pt = Value of the I/O point

- SMF = Safety Monitoring Function (SMF) block status in the CR30 safety relay editor
- LLA = Logic Level A (LLA) Function block status in the CR30 safety relay editor
- LLB = Logic Level B (LLB) Function block status in the CR30 safety relay editor
- SOF = Safety Output Function (SOF) block status in the CR30 safety relay editor

(1) See Appendix F on page 177 for details on faults.

## EtherNet/IP I/O Assemblies

The following are input assemblies available over EtherNet/IP™ for the CR30 safety relay.

<!-- image -->

## Output Assemblies

Table 44 - CR30 Safety Relay Output Assemblies

| Instance Decimal (hex)   | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0      |                                                           |               |               |               |               |               |               |
|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|---------------|---------------|---------------|---------------|---------------|---------------|
|                          | 0 PNB 07 PNB 06 PNB 05 PNB 04 PNB 03 PNB 02 PNB 01 PNB 00 |                                                           |               |               |               |               |               |               |
| 150 (96 h)               |                                                           | 1 PNB 15 PNB 14 PNB 13 PNB 12 PNB 11 PNB 10 PNB 09 PNB 08 |               |               |               |               |               |               |
|                          | 2, 3 Reserved                                             | 2, 3 Reserved                                             | 2, 3 Reserved | 2, 3 Reserved | 2, 3 Reserved | 2, 3 Reserved | 2, 3 Reserved | 2, 3 Reserved |

## Where:

- PNB = Produced Network Bit, writes to the Communications Inputs selections in the CR30 safety relay editor.

<!-- image -->

The following are output assemblies available over EtherNet/IP for the CR30 safety relay.

## Input Tags

## Tag Definitions

|                               | Name Data Type Tag Definition                                                                                                                                                                                                                    |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RunMode BOOL                  | Run mode - Indicates the operating mode of the safety relay. 0 = Idle/Program mode 1 = Run mode                                                                                                                                                  |
| ConnectionFaulted BOOL        | Connection faulted - Indicates the state of the communication connection between the safety relay and the controller. 0 = Connection 1 = Connection faulted                                                                                      |
| MajorFault BOOL               | Major fault status - Indicates whether the safety relay is major (nonrecoverable) faulted. 0 = No fault 1 = Fault                                                                                                                                |
| MinorFault BOOL               | Minor fault status - Indicates whether the safety relay is minor (recoverable) faulted. 0 = No fault 1 = Fault                                                                                                                                   |
| VerificationID INT            | Verification ID - Indicates the unique verification ID of the safety relay when you have verified the configuration. Valid verification ID values - 0001…9999. 0000 = Configuration is not verified                                              |
| PtxxData BOOL                 | Data - Off/on status for input/output point that is echoed back from the safety relay. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On                                                  |
| Plugin2InPtxxData  (1)  BOOL  | Data - Off/on status for input/output point that is echoed back from the safety relay slot 2 plug-in module. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On                            |
| Plugin2OutPtxxData  (1)  BOOL | Data - Off/on status for input/output point that is echoed back from the safety relay slot 2 plug-in module. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On                            |
| MajorFaultType SINT           | Major fault type - Indicates the major fault type of the safety relay. 01H = Hardware fault 02H = Safety input fault 04H = Safety output fault 08H = Power fault 10H = Communication fault 20H = Configuration fault 40H = Time monitoring fault |
| MajorFaultCode SINT           | Major fault code - Indicates the specific major fault code for the corresponding major fault type. See Table 47 on page 179 for additional details                                                                                               |
| MinorFaultType SINT           | Minor fault type - Indicates the type of function block that is faulted. 10H = Safety monitoring function minor fault 40H = Safety output function minor fault                                                                                   |
| MinorFaultInstance SINT       | Minor fault instance - Indicates the instance of the function block that is faulted. Valid values: 01…24                                                                                                                                         |

Table 45 - CR30 Safety Relay Input Tags

<!-- image -->

## Output Tags

Table 45 - CR30 Safety Relay Input Tags (Continued)

|                         |      | Name Data Type Tag Definition                                                                                                                                                                   |
|-------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MinorFaultCode INT      |      | Minor fault code - Indicates the specific minor fault code for the corresponding minor fault type and instance. See Table 48 on page 181  for additional details.                               |
| SMFxx (1)               | BOOL | Data - Off/on status for Safety Monitoring Function echoed back from the safety relay. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On |
| LLAxx (1)               | BOOL | Data - Off/on status for Logic Level A Function echoed back from the safety relay. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On     |
| LLBxx (1)               | BOOL | Data - Off/on status for Logic Level A Function echoed back from the safety relay. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On     |
| SOFxx (1)               | BOOL | Data - Off/on status for Safety Output Function echoed back from the safety relay. This tag is used to verify proper communication only. No field side verification is done. 0 = Off 1 = On     |
| SOFxxResetRequired  (1) | BOOL | Safety output function reset required - Indicates whether a safety output function is awaiting a reset command before initiating its output. 0 = No reset required 1 = Reset required           |

Table 46 - CR30 Safety Relay Output Tags

|                         |      | Name Data Type Tag Definition                                                                          |
|-------------------------|------|--------------------------------------------------------------------------------------------------------|
| LogicDefinedDataxx  (1) | BOOL | Logic defined data - These 16 bits write to the communications inputs in the CR30 safety relay editor. |

## Major Faults

## Table 47 - Major Faults

|     |                                                                                                                                   | Type Code Cause Recovery Method                                                                                                                                                                                                                                                                                                             |
|-----|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | 01 RAM test failure                                                                                                               |                                                                                                                                                                                                                                                                                                                                             |
|     | 02 ROM test failure                                                                                                               | Do one of the following:                                                                                                                                                                                                                                                                                                                    |
|     | 03 Stack overflow or underflow                                                                                                    | • Power cycle the safety relay.                                                                                                                                                                                                                                                                                                             |
|     | 04 Watchdog expired                                                                                                               | • Reconfigure the safety relay.                                                                                                                                                                                                                                                                                                             |
|     | 05 Memory error                                                                                                                   | • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken.                                                                                                                                                                                                                              |
|     | 06 Register failure                                                                                                               | If the fault persists, contact your local Rockwell Automation technical support                                                                                                                                                                                                                                                             |
| 01H | 07 Flow control/switch default                                                                                                    | representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                               |
|     | 08 EEPROM fault                                                                                                                   |                                                                                                                                                                                                                                                                                                                                             |
|     | 11 Host detected incorrect safety firmware revision Do one of the following:                                                      |                                                                                                                                                                                                                                                                                                                                             |
|     |                                                                                                                                   | • Power cycle the safety relay.                                                                                                                                                                                                                                                                                                             |
|     | 12 Host detected incorrect safety firmware CRC A                                                                                  |                                                                                                                                                                                                                                                                                                                                             |
|     | 13 Host detected incorrect safety firmware CRC B                                                                                  | • Update the firmware in the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken.                                                                                                                                                                                   |
|     | 15 Host software error                                                                                                            | If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                               |
|     | 01…18  Safety input pulse test failure. Code corresponds to specific terminal that is faulted +1                                  | Do one of the following: • Check wiring for shorts to 24V or other channels. • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support |
| 02H | 19 Cross loop inputs of input shift register Do one of the following:                                                             | representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                               |
|     | 20…21 Input data transfer fault                                                                                                   | • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                |
|     | 01…10 Safety output plausibility failure (short of failure on power-up). Code 01…10 corresponds to terminals 12…21, respectively. | Do one of the following: • Check wiring for shorts to 24V or other channels. • Power cycle the safety relay.                                                                                                                                                                                                                                |
| 04H | 11…20  Safety output pulse test failure. Code 11…20 corresponds to terminals 12…21, respectively.                                 | • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                |
|     | 00 Other fault                                                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|     | 01 CRC Error                                                                                                                      |                                                                                                                                                                                                                                                                                                                                             |
|     | 02 EEPROM                                                                                                                         |                                                                                                                                                                                                                                                                                                                                             |
|     | 03  Processors A and B received different values from the host                                                                    | A configuration fault occurred. Do one of the following: • Reconfigure the safety relay. • Power cycle the safety relay.                                                                                                                                                                                                                    |
| 06H | 04 Configuration files not OK                                                                                                     | If the fault persists, contact your local Rockwell Automation technical support                                                                                                                                                                                                                                                             |
|     | 05 Plug-in slot 2 configuration not equal to actual                                                                               | representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                               |
|     | 20  Host detected safety processors did not respond to configuration step                                                         |                                                                                                                                                                                                                                                                                                                                             |
|     | 21 Plug-in slot 1 configuration not equal to actual                                                                               |                                                                                                                                                                                                                                                                                                                                             |

## Table 47 - Major Faults (Continued)

|     |                                                                                      | Type Code Cause Recovery Method                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 08H | 01  Over/under voltage is detected or pulse test failure of main internal transistor | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
| 08H | 02 Pulse test fault of voltage monitoring/main transistor                            | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
| 08H | 03 Under voltage reset                                                               | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
| 10H | 01 Compare UART data during operation                                                | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
| 10H | 02 Communication timeout between safety processors                                   | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
|     | 17  Host processor detected safety processors are unresponsive                       | Do one of the following:                                                                                                                                                                                                                                                                                                                                                                                                          |
|     | 18  Host processor detected safety processors lost communication                     | • Power cycle the safety relay. • Reattempt download of the safety relay configuration.                                                                                                                                                                                                                                                                                                                                           |
| 20H | 01 CRC Error in the configuration file                                               | • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken.                                                                                                                                                                                                                                                                                                                    |
| 20H | 02 CRC of configuration file different from EEPROM                                   | If the fault persists, contact your local Rockwell Automation technical support                                                                                                                                                                                                                                                                                                                                                   |
| 20H | 03  Mismatch between I/O µC A and I/O µC B in configuration files                    | representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                                                                                                                     |
| 20H | 04 Invalid ID numbers for configuration files                                        | Do one of the following: • Validate the electrical installation and the appropriate supply voltage is provided. • Power cycle the safety relay. • Reconfigure the safety relay. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                     |
|     | 05  Mismatch between configured plug-in and plug-in detected on slot 2               | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support                                                               |
|     | 21  Mismatch between configured plug-in and plug-in detected on slot 1               | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support                                                               |
|     | 40H 01…03 Timing fault                                                               | Do one of the following: • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                             |
| 80H | 20 Memory module restore failed Do one of the following:                             | • Verify that the memory module is properly seated in slot 1 • Power cycle the safety relay. • Initiate backup or restore If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                           |
| 80H | 21 Memory module backup failed                                                       | • Verify that the memory module is properly seated in slot 1 • Power cycle the safety relay. • Initiate backup or restore If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                           |
|     | 41 Plug-in slot 1: Parity failure                                                    | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 42 Plug-in slot 1: Communication error                                               | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 43 Plug-in slot 1: Plug-in type not supported                                        | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 81 Plug-in slot 2: Parity failure                                                    | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 82 Plug-in slot 2: Communication error                                               | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 83 Plug-in slot 2: Plug-in type is not supported.                                    | Do one of the following: • Verify that the plug-in physically present in the slot matches the configuration. • Reattempt download of the safety relay configuration. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |

## Minor Faults

## Table 48 - Minor Faults

|     |     |                                                                                                                               | Type Code Cause Recovery Method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----|-----|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | 01H | Pulse test failure: Channel is shorted to 24V or another channel.                                                             | Do one of the following: • Check wiring for shorts to 24V or other channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     | 02H | Reset held on: A transition of the reset input from on (1) to off (0) did not occur within 3 seconds.                         | • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                                    |
|     | 04H | Safety light curtain mute time exceeded: The safety light curtain was muted for longer than the maximum configured mute time. | Do one of the following: • Verify that there is no obstruction of the mute sensor or safety light curtain. • Verify that the application times are appropriate • Check wiring for shorts to 24V or other channels. • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | 05H | No input selection fault: A no input selection fault condition existed for more than 250 ms.                                  | Do one of the following: • Check the timing of the mode selection inputs to see if they are within 250 ms. • To clear the fault, cycle the Mode Selection switch through the valid modes. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                         |
|     | 06H | Input selection fault: A multiple input selection condition was detected. Check the mode selection inputs.                    | Do one of the following: • Check the timing of the mode selection inputs to see if they are within 250 ms. • To clear the fault, cycle the Mode Selection switch through the valid modes. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                         |
| 10H | 07H | Hazardous motion fault: Hazard Feedback transitioned to off (0) while the Unlock Command to the device was on (1).            | Do one of the following: • Adjust the application to verify that the hazard cannot be energized when the lockable guard is unlocked. • To clear the fault, press the Lock Request (LR) input. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                     |
|     | 08H | Contact bounce: One channel went to the safe state and back to the active state after a reset.                                | Do one of the following: • Check the wiring and mechanical integrity of the field device. • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                          |
|     | 10H | Mute time exceeded: Too much time has elapsed between mute sensors being blocked.                                             | Do one of the following: • Verify that there is no obstruction of the mute sensor. • Verify that the application times are appropriate • Check wiring for shorts to 24V or other channels. • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                         |
|     |     | 14H Combination of faults detected                                                                                            | See the following fault codes: • 04H • 10H                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     | 20H | Discrepancy fault: The configured amount of time that the inputs are allowed to be in an inconsistent state expired.          | Do one of the following: • Check wiring for shorts to 24V or other channels. • If appropriate, adjust the discrepancy time for the safety monitoring function. • Power cycle the safety relay. • Reconfigure the safety relay. • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                     |

## Table 48 - Minor Faults (Continued)

|     |                                                                                                                                                                 | Type Code Cause Recovery Method                                                                                                                                                                                                                                                                                                                                                                                           |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | 40H Muting sequence fault: An illegal input pattern, the pattern of sensors being blocked and cleared, for the mute sensors was detected.                       | Do one of the following: • Check the sensor • Check wiring • Power cycle the safety relay • Reconfigure the safety relay • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                     |
|     | 44H Combination of faults detected                                                                                                                              | See the following fault codes: • 04H • 40H                                                                                                                                                                                                                                                                                                                                                                                |
|     | 50H Combination of faults detected                                                                                                                              | See the following fault codes: • 10H • 40H                                                                                                                                                                                                                                                                                                                                                                                |
|     | 54H Combination of faults detected                                                                                                                              | See the following fault codes: • 4H • 10H • 40H                                                                                                                                                                                                                                                                                                                                                                           |
|     | 90H Combination of faults detected                                                                                                                              | See the following fault codes: • 10H • 80H                                                                                                                                                                                                                                                                                                                                                                                |
|     | 94H Combination of faults detected                                                                                                                              | See the following fault codes: • 4H • 10H • 80H                                                                                                                                                                                                                                                                                                                                                                           |
| 10H | 120H Combination of faults detected                                                                                                                             | See the following fault codes: • 40H • 80H                                                                                                                                                                                                                                                                                                                                                                                |
|     | 124H Combination of faults detected                                                                                                                             | See the following fault codes: • 4H • 40H • 80H                                                                                                                                                                                                                                                                                                                                                                           |
|     | 130H Combination of faults detected                                                                                                                             | See the following fault codes: • 10H • 40H • 80H                                                                                                                                                                                                                                                                                                                                                                          |
|     | 134H Combination of faults detected                                                                                                                             | See the following fault codes: • 4H • 10H • 40H • 80H                                                                                                                                                                                                                                                                                                                                                                     |
|     | 80H Safety light curtain sequence fault: An illegal input pattern, the pattern of sensors and the safety light curtain being blocked and cleared, was detected. | Do one of the following: • Check the sensor • Check wiring for shorts to 24V or other channels • Power cycle the safety relay • Reconfigure the safety relay • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support |
|     | FFFFH Unregistered fault                                                                                                                                        | Contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                                                    |
| 40H | 01H Retrigger fault: Enabled input has transitioned from off (0) to on (1) while the output delay time was in progress.                                         | Do one of the following: • Verify that application logic and wiring is appropriate • Power cycle the safety relay • Reconfigure the safety relay • Validate the electrical installation and appropriate measures to reduce noise and suppress surges are taken. If the fault persists, contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support             |
|     | FFFFH Unregistered fault                                                                                                                                        | Contact your local Rockwell Automation technical support representative. For contact information, see rok.auto/support                                                                                                                                                                                                                                                                                                    |

## Numerics

2080-IQ4 102

2080-IQ4OB4 102

2080-OB4 103

2080-OW4I 103

440C­ENET

about 105

connect to network 107

ground 106 install 104 , 106 set network address 107 specifications 165 status indicator 108 wire 106

## A

## about

Guardmaster 440C­ENET 105

## access

exclusive

139

module data with add-on profiles 119

add

CR30 safety relay 110

add-on profile

use 110

add-on profiles

access module data 119

advanced settings 64

after initial transition 51

agency certification 167

alternate device 81

dual channel 82

dual channel N.C./N.O. 84

dual channel OSSD 83

single channel 81

three channel 85

AND 88

with Restart 89

## approval

regulatory 167

architecture 128

assembly

EtherNet/IP I/O 175

input 175

output 176

automation controller communication 109

## B

## back up

project 145 , 146

## block

AND 88

AND with Restart 89

immediate OFF 96

jog 99

muting lamp 99

NAND 89

nest 92

NOR 89

NOT 89

OFF delay 98

ON delay 97

OR 88

OR with Restart 91

pass through 87

XOR 88

## build

configuration 30

## C

## cables 24

calculation

system response time 153

certification 167

change

password 141

channel

test 47

clear

password 142

## communication

automation controller 109

Modbus 127

communication connection 13

compatibility 139

## compliance

European Union directive 168

European Union directives 167

## configuration

build 30

download 30

download to CR30 safety relay online changes 117 password 140

115

reference document 169

## configure

safety relay logic 114

## connect

power supply 21 safety relay (password-protected) 140 to network 107

## Connected Components Workbench

obtain software 13

start 25

troubleshoot with Logic Editor 134

## connection

communication 13

Ethernet/IP 14

input 95 multiple block output 95 serial port 14

USB 13

## control

two-hand control 78

type IIIA two-hand 79

type IIIC two-hand 80

## ControlFLASH

firmware upgrade 171

## controller

insert module 101 status indicator 125

## CR30 safety relay

download configuration 115

## crossfault

fault analysis 137

## cycling

power 24

## D

## definition 8

tag 177

delay

OFF 98

ON 97

## detail

hardware 12

## device

alternate 81

## dimensions

mounting 15

## DIN Rail

mounting 15

## directive

EMC 168

## directives

compliance to European Union 167

## discrepancy

monitoring 159

test 47

## download

configuration

30

configuration to CR30 safety relay 115

safety relay (password-protected) ) 140

dual channel

82

N.C./N.O. 84

OSSD

83

## E

## embedded serial port

wire 23

EMC directive 168

emergency stop 55

enabling switch 56

enclosure consideration 16

environmental 152

E-stop See emergergency stop

38

## ethernet

message 109

## ethernet module

specifications 165

## EtherNet/IP

connection 14 175

I/O assembly

## EtherNet/IP plug­in module

about 105

connect to network 107

ground 106 install 104 , 106 set network address 107 status indicator 108 wire 106

## European Union directive

compliance 168

## European Union directives

compliance 167

## evaluation

multi-channel signal 159 test pulse 158

## excessive heat

prevention 17

## exclusive access 139

## explicit

message 120

## F

## fault analysis

crossfault 137

fault present 78

faults major 179

minor 181

nonrecoverable 134

recoverable 133

sequence 159

timing 159

## features

hardware 11

## feedback

parameter 95

feedback monitoring 57

## filter

input 45

## firmware

upgrade 171

## four-sensor muting 69

## function block

alternate device 81

emergency stop 55

enabling switch 56

feedback monitoring 57

gate switch muting 62 output loop

59

light curtain 60

86

reset 71

restart 72

safety mat 74

SensaGuard 75

single wire safety input 76

two-hand control 78

## functions

safety monitoring 55

## G

gate switch 59

## general

specifications 152

glossary 8

ground

Guardmaster 440C­ENET 106 safety relay 20

## Guardmaster 440C­ENET

about 105

connect to network 107

install 104 106

ground 106 , set network address 107

status indicator 108

wire 106

## H

## hardware

detail 12

features 11

## I

## I/O

EtherNet/IP assembly message 109

175

## I/O configuration

add CR30 safety relay 110

immediate OFF 96

indication naming error 54

## initial transition

after run mode 51

run mode 49

assembly 175

connection 95

device (mechanical contact) 22

device (OSSD output) 22

invert 93

maximum number 12

revert 93

single wire safety 76

specifications 152

status indicator 124

tag 177

## input filter 45

## insert

module into controller 101

## install

Guardmaster 440C­ENET 104 , 106

installation 15

## integral test pulse

safety output 159

intended use 11

invert 93

## input

jog 99

## L

## lamp

muting 71

LED See status indicator light curtain 60

lock control 61

locked safety relay 140

logic levels

A and B 87

nest 92

lost password 143

L-type muting two-sensor 67

## M

major faults 179

map

Modbus 127

## mechanical contact

input device 22

## memory module

use 145

## message

ethernet 109

explicit 120

I/O 109

minor faults 181

## Modbus

communication 127

map 127

troubleshoot 136

mode selection 62

## module

insert into controller 101

plug-in 101

## monitoring

discrepancy 159

time 156

## mounting

dimensions 15

DIN Rail 15

panel 16

## multi-channel signal

evaluation 159

## multiple block connections 38

muting 62

four-sensor 69

lamp 71 , 99

two-sensor L-type 67

two-sensor T-type 65

## N

## naming error

indication 54

NAND 89

## J

## nest

logic levels 92 network address set 107 new project 26 nonrecoverable faults 134 response time 161 NOR 89 normally closed input pulse testing 40 normally open input pulse testing 39 NOT 89

nonrecoverable faults and failures

## O

OFF delay 98

ON delay 97

online changes configuration 117

OR 88

with Restart 91

OSSD

dual channel 83

## OSSD output

input device 22

## output

assembly 176

connections 95

invert 93

loop 86

maximum number 12

pulse testing 41

revert 93

safety 95

specifcations 153

status indicator 124

tag 178

wire device 23

override settings 64

## P

## page

start 25

panel

mounting 16

parameter

feedback 95

reset 95

pass through 87

password 139

change 141

clear 142

configuration 140

lost 143

protection 139

set 140

## performance

category level 151

151

pinouts 24

plug-in module 101

```
power 19 power cycling 24 power supply connect 21 prevent excessive heat 17 project back up 145 , 146 new 26 restore 145 , 147 protection password 139 pulse testing 39
```

normally closed input 40

normally open input 39

output 41

## R

rating SIL 151 reaction time 153 , 162 read status 129 ready for reset 77 recoverable faults 133 recovery time 153 reference document configuration 169 regulatory approval 167 rename safety block 53 report example 150 reports 149 reset 71 parameter 95 send 131 reset set flip flop 93 response time 153 demand of safety function 154 nonrecoverable faults and failures 161 restart 72 restore project 145 , 147 revert 93 RS-FF See reset set flip flop RSLogix 5000 safety relay add-on profile 110 run mode 51 initial transition 49 S safety block rename 53 safety mat 74 safety monitoring functions 55 safety output 95 integral test pulse 159

## safety relay

## connect (password-protected) ) 140 download (password-protected) 140 ground 20 locked 140 upload (password-protected) 140 safety relay logic configure 114 security 139 send reset 131 SensaGuard 75 sequence faults 159 serial port connection 14 set network address 107 password 140 settings advanced 64 override 64 signal evaluation multi-channel 159 SIL rating 151 single channel 81 single wire safety input 76 software 13 Connected Components Workbench specifications 151 environmental 152 general 152 input 152 output 153 reaction time 153 recovery time 153 response time 153 start Connected Components Workbench start page 25 status read 129 status in 77 status indicator 123 , 133 controller 125 Guardmaster 440C­ENET 108 input 124 output 124 status out 100 surge suppressor 23 switch enabling 56 gate 59 system response time calculation 153 T tag definition 177 input 177 output 178 terminal assignment 20 test

channel 47

discrepancy 47

13

25

## test pulse

evaluation 158

integral 159

three channel 85

time

monitoring 156

reaction 153 , 162

recovery 153

response

153

## timing 95

faults 159

troubleshoot

133

with Connected Components Workbench

Logic Editor 134

with Modbus 136

## T-type muting

two-sensor 65

two-hand control

78

type IIIA 79

type IIIC 80

two-sensor L-type muting 67

## two-sensor muting

L-type 67

T-type 65

two-sensor T-type muting 65

type IIIA

two-hand control 79

## type IIIC

two-hand control 80

## U

## upgrade

firmware 171

## upload

safety relay (password-protected) 140

USB connection 13

use

memory module 145

RSLogix 5000 safety relay add-on profile 1 110

## V

## verification

view ID without Connected Components

Workbench software 35

## view ID

without Connected Components Workbench software 35

## W

## wire 19 , 22

embedded serial port 23

Guardmaster 440C­ENET 106

input devices 22

output device 23

recommendation 19

requirements 19

size 19

workspace 29

XOR 88

## X

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, and product notification updates.                   | rok.auto/support                                                                                         |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Knowledgebase                                    | rok.auto/knowledgebase                                                                                     | Access Knowledgebase articles.                                                                           |
| Locate the telephone number for your country.    | rok.auto/phonesupport                                                                                      | Local Technical Support Phone Numbers                                                                    |
|                                                  | rok.auto/literature                                                                                        | Literature Library  Find installation instructions, manuals, brochures, and technical data publications. |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and find associated firmware. | rok.auto/pcdc                                                                                            |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental information on its website at rok.auto/pec .

Allen-Bradley, Atlas, CompactLogix, Connected Components Workbench, ControlFLASH, ControlLogix, expanding human possibility, FactoryTalk, Guardmaster, GuardShield, Micro800, Micro830, PanelView, PowerFlex, Rockwell Automation, RSLinx, RSLogix 5000, SafeZone, SensaGuard, SoftLogix, Studio 5000, Studio 5000 Logix Designer, and Zero-Force Touch Buttons are trademarks of Rockwell Automation, Inc.

CIP, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Microsoft, Visual Studio, and Windows are trademarks of the Microsoft Corporation.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility?

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIA PACIFIC: RockwellAutomation, Level 14, Core F, Cyberport 3, 100 Cyberport Road, Hong Kong, Tel:(852)2887 4788,Fax:(852)2508 1846 UNITED KINGD0M:Rockwell Automation Ltd.Pitfield, Kiln Farm Milton Keynes, MK113DR, United Kingdom, Tel:(44)(1908)838-800,Fax:(44)(1908)261-917