<!-- image -->

## ControlLogix Configurable Flowmeter Module

Catalog Number 1756-CFM

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

|                              | Preface                                                                                              |                                                   |
|------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------|
|                              | Who Should Use This Manual . . . .  . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 7                   |
|                              | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . 7               |
|                              | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . 7               |                                                   |
|                              | Additional Resources . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . . 7                         |
|                              | Chapter 1                                                                                            |                                                   |
| What is the 1756-CFM Module? | What This Chapter Contains . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . 9               |
|                              | Use a 1756-CFM Module. . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 9               |
|                              | Module Features. . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 10                        |
|                              | Physical Features . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . 10                                |
|                              | Typical Applications . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . 11                                |
|                              | Understand Module Input Capabilities. . . . . . . . . . . . . . . . . . . . . . . . . . . . 12       |                                                   |
|                              | Understand Module Output Capabilities . . . .                                                        | . . . . . . . . . . . .  . . . . . . . . . . 12   |
|                              | Use Module Identification and Status Information. . . . . . . . . . . . . . . . . 13                 |                                                   |
|                              | Chapter 2                                                                                            |                                                   |
| Configurable Flowmeter       | What This Chapter Contains . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 15                |
| Operation in the             | Ownership . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 16                                |
| ControlLogix System          | Use Programming Software. . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 17                  |
|                              | 1756-CFM Modules in Local Chassis   . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . 17                      |
|                              | 1756-CFM Modules in Remote Chassis . . . . . . . . . . . . . . . . . . . . . . . . . 17              |                                                   |
|                              | Connections . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 18                                |
|                              | Direct Connections . . . . . . . .  . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 18                |
|                              | Listen-Only Connections . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 18                  |
|                              | 1756-CFM Modules in a Local Chassis . . . . . . .                                                    | . . . . . . . . . . . .  . . . . . . . . . . 19   |
|                              | Requested Packet Interval (RPI). . . . . . . . .                                                     | . . . . . . . . . . . .  . . . . . . . . . . 19   |
|                              | 1756-CFM Modules in a Remote Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . 20        |                                                   |
|                              | Chapter 3                                                                                            |                                                   |
| 1756-CFM Module Features     | What This Chapter Contains . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 21                |
| and Operational Modes        | Understand General Module Features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21       |                                                   |
|                              | Removal and Insertion Under Power (RIUP) . . . . . . . . . . . . . . . . . . . 21                    |                                                   |
|                              | Module Fault Reporting . . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 21                  |
|                              | Fully Software Configurable . . . . . . . . . . .                                                    | . . . . . . . . . . . . .  . . . . . . . . . . 21 |
|                              | Electronic Keying. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 22                        |
|                              | Producer/Consumer Model . . . . . . . . . . . . .                                                    | . . . . . . . . . . . .  . . . . . . . . . . 27   |
|                              | Module Status Information. . . . . . . . . . . .                                                     | . . . . . . . . . . . .  . . . . . . . . . . . 27 |
|                              | Configurable Flowmetering Channels . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . . 27     |
|                              | Flowmeter Inputs. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 27                |
|                              | Gate Inputs . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . . . . . . . . 27                                |
|                              | User-Defined Preset and Rollover Values. .                                                           | . . . . . . . . . . .  . . . . . . . . . . 28     |
|                              | Current-Sourcing Outputs . . . . . . . . . . . .                                                     | . . . . . . . . . . . .  . . . . . . . . . . . 28 |

|                             | Choose an Operational Mode. . . .  . . . . . . . . . . . . . . . . .                                                                                              | . . . . . . . . . . . . . . . . 28                  |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                             | Operate in High Resolution Frequency Mode . . . . . . . . . . . . . . . . . . . . . . 28                                                                          |                                                     |
|                             | Terminal Usage in High Resolution Frequency Mode . . . . . . . . . . . 29                                                                                         |                                                     |
|                             | Output Operation in High Resolution Frequency Mode . . . . . . . . . 29                                                                                           |                                                     |
|                             | Module Features Used in High Resolution Frequency Mode . . . . . 29                                                                                               |                                                     |
|                             | Alarms in High Resolution Frequency Mode. . . . . . . . . . . . . . . . . . . . 31                                                                                |                                                     |
|                             | Sample Configuration for High Resolution Frequency Mode. . . . . 31                                                                                               |                                                     |
|                             | Operate in Totalizer Mode  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                  | . . . . . . . . . . . . 32                          |
|                             | Nonresettable Totalizer . . . . .  . . . . . . . . . . . . . . . . .                                                                                              | . . . . . . . . . . . . . . . . 32                  |
|                             | Terminal Usage in Totalizer Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32                                                                      |                                                     |
|                             | Output Operation in Totalizer Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . 32                                                                        |                                                     |
|                             | Use the Totalizer Mode Prover Function. . . . . . . . . . . . . . . . . . . . . . . . . . . 33                                                                    |                                                     |
|                             | Use a Prover. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                  | . . . . . . . 34                                    |
|                             | Features Available with the Prover Function. . . . . . . . . . . . . . . . . . . . 35                                                                             |                                                     |
|                             | Alarms with the Prover Function . . . . . . .                                                                                                                     | . . . . . . . . . . . .  . . . . . . . . . . . 40   |
|                             | Sample Configuration for Totalizer Mode Prover Function . . . . . . 40                                                                                            |                                                     |
|                             | Use the Totalizer Mode Filler Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41                                                                 |                                                     |
|                             | Trickle Function for Totalizer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . 42                                                                      |                                                     |
|                             | Configurable Features Available with the Totalizer Mode Filler Function . . . . . . . . . .                                                                       | . . . . . . . . . . . .  . . . . . . . . . . 43     |
|                             | Alarms with the Filler Function . . . . . . .                                                                                                                     | . . . . . . . . . . . . .  . . . . . . . . . . . 48 |
|                             | Sample Configuration for Totalizer Mode Filler Function. . . . . . . . 48                                                                                         |                                                     |
|                             | Configurable Output Behaviors .  . . . . . . . . . . . . . . . . .                                                                                                | . . . . . . . . . . . . . . . . 49                  |
|                             | How To Enable Output Behavior Configuration . . . . . . . . . . . . . . . . 50                                                                                    |                                                     |
|                             | Chapter 4                                                                                                                                                         |                                                     |
| Install the 1756-CFM Module | What This Chapter Contains . . .  . . . . . . . . . . . . . . . . . .                                                                                             | . . . . . . . . . . . . . . . . 51                  |
|                             | Power Requirements . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . . . 52                |
|                             | Install the Module. . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                  | . . . . . . . . 52                                  |
|                             | Key the Removable Terminal Block/Interface Module. . . . . . . . . . . . . . . 54                                                                                 |                                                     |
|                             | Key the Module. . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                | . . . . . . . . . . . . 54                          |
|                             | Key the RTB/IFM . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                          | . . . . . . . . 54                                  |
|                             | Wire the Removable Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                                                  |                                                     |
|                             | Connect Grounded End of the Cable. . . . . .                                                                                                                      | . . . . . . . . . . . .  . . . . . . . . . 55       |
|                             | Connect Ungrounded End of the Cable . . . . . . . . . . . . . . . . . . . . . . . . 56                                                                            |                                                     |
|                             | Connect Wires to the RTBs  . . . . . . . . . . . . . . . . . .                                                                                                    | . . . . . . . . . . . . . . . . . 56                |
|                             | Wire the Module . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                          | . . . . . . . . . . . . 57                          |
|                             | Standard Flowmeter Wiring Example . . . . .                                                                                                                       | . . . . . . . . . . .  . . . . . . . . . 57         |
|                             | Standard Prover/Detector Wiring Example 1  . . . . . . . . . .                                                                                                    | . . . . . . . . . 58                                |
|                             | Standard Prover/Detector Wiring Example 2 .                                                                                                                       | . . . . . . . . .  . . . . . . . . . 59             |
|                             | Standard Output Wiring Example.   . . . . . . . . . . . . . .                                                                                                     | . . . . . . . . . . . . . . 60                      |
|                             | Assemble the Removable Terminal Block and Housing. . . . . . . . . . . . . . 61                                                                                   |                                                     |
|                             | Install the Removable Terminal Block on the Module . . . . . . . . . . . . . . . 61                                                                               |                                                     |
|                             | Remove the Removable Terminal Block from the Module . . . . . . . . . . . 62 Remove the Module . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . 63                          |

Chapter 5

| Configure the 1756-CFM Module   | What This Chapter Contains . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 65                  |
|---------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                                 | Use This Chapter. . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . . . . . . . . 65                                  |
|                                 | Overview of the Configuration Process. . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . . 65   |
|                                 | Create a New Module. . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 67                |
|                                 | Communication Format. . . . . . .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 69                    |
|                                 | Electronic Keying. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 70                          |
|                                 | Use the Default Configuration . . . . . . . . . . .                                                  | . . . . . . . . . . . . .  . . . . . . . . . . . 70 |
|                                 | Edit the Configuration . . . . . . .  . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 71                  |
|                                 | Access the Tags . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . . . 72                                  |
|                                 | Change Configuration Information at the Tags . .  . . . . . . . . . .                                | . . . . . . . . 73                                  |
|                                 | Configurable Features . . . . . .  . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 73                    |
|                                 | Download Configuration Data . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . .  . . . . . . . 74               |
|                                 | Change Configuration During Module Operation . . . . . . . . . . . . . . . . . . 75                  |                                                     |
|                                 | Use Ladder Logic . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . 75                            |
|                                 | Use Message Instructions. . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 76                  |
|                                 | Process Real-Time Control and Module Services . . . . . . . . . . . . . . . . 76                     |                                                     |
|                                 | One Service Performed Per Instruction . . . . . . . . . . . . . . . . . . . . . . . . 76             |                                                     |
|                                 | Create a New Tag . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . . 77                          |
|                                 | Enter Message Configuration. . . . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . . 79   |
|                                 | Configure 1756-CFM Modules in a Remote Chassis . . . . . . . . . . . . . . . . . 81                  |                                                     |
|                                 | Add and Configure Local Communication Module . . . . . . . . . . . . . . 81                          |                                                     |
|                                 | Add and Configure Remote Communication Module . . . . . . . . . . . 82                               |                                                     |
|                                 | Add and Configure Remote 1756-CFM Module . . . . . . . . . .                                         | . . . . . . . . 84                                  |
|                                 | Sample Configuration for High Resolution Frequency Mode . . . . . . . . 86                           |                                                     |
|                                 | Sample Configuration for Totalizer Mode Prover Function. . . . . . . . . . 88                        |                                                     |
|                                 | Sample Configuration for Totalizer Mode Filler Function . . . . . . . . . . . 93                     |                                                     |
|                                 | Digital Filter. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . . . . . . . . . . . . 97                          |
|                                 | Appendix A                                                                                           |                                                     |
| Troubleshoot the 1756-          | What This Appendix Contains. . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . 101                     |
| CFM Module                      | Use the Status Indicators . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 101                   |
|                                 | Use Programming Software to Troubleshoot Your Module . . . . . . . . . 102                           |                                                     |
|                                 | Determining Fault Type . . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . 103                     |
|                                 | Use Error Codes . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . 103                             |
|                                 | Appendix B                                                                                           |                                                     |
| Software Configuration Tags     | Configuration Structure . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . 105                                     |
|                                 | Input Tags . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . . . . . 110                           |
|                                 | Output Tags . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . 112                                   |

|                                | Appendix C                                                                                                                                  |                                            |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Module Schematics              | What This Appendix Contains. . . .  . . . . . . . . . . . . . . . . .                                                                       | . . . . . . . . . . . . . . 117            |
|                                | Input Circuits . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . 117                          |
|                                | Flowmeter Inputs. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                    | . . . . . . . . . . . . . . . 117          |
|                                | Gate Inputs . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . 118                            |
|                                | Output Circuits . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . 120                          |
|                                | Discrete Outputs . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . . 120                  |
|                                | Appendix D                                                                                                                                  |                                            |
| Frequency Accuracy             | Frequency Accuracy in High-Resolution Frequency Mode. . . . . . . . . . 123                                                                 |                                            |
|                                | Calculate Frequency Accuracy. . . . . . . . . . .  . . . . . . . . . . . .                                                                  | . . . . . . . . . 123                      |
|                                | Frequency Accuracy in Totalizer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . 124                                              |                                            |
|                                | Calculate Frequency Accuracy. . . . . . . . . . .  . . . . . . . . . . . .                                                                  | . . . . . . . . . 124                      |
|                                | Appendix E                                                                                                                                  |                                            |
| Configure Output Behavior with | Configure the 1756-CFM Module for Use in a New Application. . . . . . 128                                                                   |                                            |
| RSLogix 5000 Version 16 and    | Add the 1756-Generic Profile to the Program. . . . . . . . . . . . . . . . . . . 128                                                        |                                            |
| Earlier                        | Copy and Paste the Tags and Logic from the Example to Your Program . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . 129                    |
|                                | Specify the Configurable On/Off Behavior .                                                                                                  | . . . . . . . . . . .  . . . . . . . . 131 |
|                                | Configure a 1756-CFM Module for Use in an                                                                                                   |                                            |
|                                | Existing Application. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . 132                  |
|                                | Add the 1756-Generic Profile to the Program. . . . . . . . . . . . . . . . . . . 132                                                        |                                            |
|                                | Copy and Paste the Tags and Logic from the Example to Your Program. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . . . . . 133                  |
|                                | Specify the Configurable On/Off Behavior .                                                                                                  | . . . . . . . . . . .  . . . . . . . . 135 |
|                                | Glossary                                                                                                                                    |                                            |
|                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | 137                                        |
|                                | Index                                                                                                                                       |                                            |

This manual describes how to install, configure, and troubleshoot your ControlLogix® Configurable Flowmeter (CFM) module, catalog number 1756-CFM. Throughout the rest of this manual, the module is referred to as the 1756-CFM module.

Who Should Use This Manual You must be able to program and operate an Allen-Bradley ® ControlLogix controller to use your 1756-CFM module efficiently.

## Summary of Changes

## Download Firmware, AOP, EDS, and Other Files

## Additional Resources

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                                                                  | Page   |
|----------------------------------------------------------------------------------------|--------|
| Added information about how to use the module remotely over an EtherNet/IP™ network 17 |        |
| Updated configuration screens to more recent version of the programming software 65    |        |
| Updated Series B module Gate Input schematic to show bidirectional diode               | 119    |

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                           | Description                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756 ControlLogix I/O Technical Data, publication 1756-TD002                                                       | Provides specifications for the ControlLogix controllers, I/O modules, specialty modules, chassis, power supplies, and accessories.                                                                                                                                             |
| ControlLogix System User Manual, publication 1756-UM001                                                            | Detailed description of how to use your ControlLogix operating system.                                                                                                                                                                                                          |
| ControlLogix Digital I/O Modules User Manual, publication1756-UM058                                                | Detailed description of how to install and use ControlLogix digital I/O modules.                                                                                                                                                                                                |
| ControlLogix Analog I/O Modules User Manual, publication 1756-UM009                                                | Detailed description of how to install and use ControlLogix analog I/O modules.                                                                                                                                                                                                 |
| ControlLogix High-speed Counter Module Installation Instructions, publication 1756-IN018                           | Detailed description of how to install and use the ControlLogix high-speed counter module.                                                                                                                                                                                      |
| EtherNet/IP Network Devices User Manual, ENET-UM006                                                                | Describes how to configure and use EtherNet/IP devices to communicate on the EtherNet/IP network.                                                                                                                                                                               |
| Ethernet Reference Manual, ENET-RM002                                                                              | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                      |
| System Security Design Guidelines Reference Manual, SECURE-RM001                                                   | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                   |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                                     | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                                                                                                                 |
| American Standards, Configurations, and Ratings: Introduction to Motor Circuit Design, publication IC-AT001        | Provides an overview of American motor circuit design that is based on methods that are outlined in the NEC.                                                                                                                                                                    |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications .                                                          | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

You can view or download publications at rok.auto/literature .

## Notes:

## What This Chapter Contains

## Use a 1756-CFM Module

## What is the 1756-CFM Module?

This chapter describes the 1756-CFM module. It also describes what you must know and do before using the module.

The 1756-CFM module is an intelligent I/O module that performs high-speed flow metering for industrial applications. The module is a single-slot module that interfaces between a Logix controller and external I/O devices.

The module interfaces with these output types:

- Magnetic Pickup
- TTL
- Preamps

The 1756-CFM modules mount in a ControlLogix® chassis and use a removable terminal block (RTB) or a Bulletin 1492 interface module cable that connects to an IFM to connect all field-side wiring.

Before you install and use your module, make sure that you have completed the following tasks:

- Installed and grounded a 1756 chassis and power supply.

To install these products, refer to these publications:

- -ControlLogix Power Supply, publication 1756-IN619
- ControlLogix Redundant Power Supply, publication 1756-IN620
- -ControlLogix Chassis, publication 1756-IN621
- Ordered and received an RTB or IFM and its components for your application.

IMPORTANT

RTBs and IFMs are not included with your module.

<!-- image -->

## Module Features

These features available on the 1756-CFM module offer greater system applicability:

- Two configurable flow metering channels
- Flowmeter inputs
- Gate inputs
- Two current-sourcing outputs
- Removal and insertion under power
- CE marked
- UL Listed
- CSA certified for Class I Division 2 hazardous locations

For a complete listing and detailed explanation of all features available on the 1756-CFM module, see Configurable Flowmeter Module Features and Operational Modes on page 21 .

## Physical Features

<!-- image -->

- ControlLogix backplane connector - The backplane connector interface for the ControlLogix system connects the module to the ControlLogix backplane.
- Connectors pins - Input/output, power, and grounding connections are made to the module through these pins with the use of an RTB or IFM.
- Locking tab - The locking tab anchors the RTB or IFM cable on the module, maintaining wiring connections.

- Slots for keying - Mechanically keys the RTB to help prevent inadvertently making the wrong wire connections to your module.
- Status indicators - Indicators display the status of communication, module health, and input/output devices. Use these indicators to help in troubleshooting.
- Top and bottom guides - Guides help seat the RTB or IFM cable onto the module.

## Typical Applications

You can use the module in power management, automotive, food and beverage, and oil and gas industries for various flow and/or turbine metering applications.

This figure shows a module in a turbine shaft speed-monitoring application. In this example, the module is operating in High-Resolution Frequency mode. Other examples are shown in Chapter 3 to reflect the various operational modes available on the module.

<!-- image -->

For a detailed explanation of how the module works with other portions of a ControlLogix control system, see Chapter 2 , Configurable Flowmeter Operation in the ControlLogix System .

## Understand Module Input Capabilities

## Understand Module Output Capabilities

The module accepts input for up to two channels (mode dependent). Each of the input channels can connect to:

- Magnetic Pickup - 50 mV trigger
- TTL output - 1.3V trigger
- Preamp outputs - 4V trigger

You configure the module's two input channels for your specific application. Each input channel has two input selections:

- Flowmeter Input (F0 &amp; F1) - Connect input device to this input.
- Gate Input (Z0 &amp; Z1) - Accepts 4-40V DC input pulses from open collectors or external contact closures. These inputs are used in Totalizer mode to interface to a prover when a prover is enabled.

The module has two assignable outputs. These outputs are designed for applications that require fast response. The outputs:

- support an output current 1 A max per channel. Total output current is limited to 2 A.
- can be assigned to any input channel with user-defined trigger parameter (see Table 1).
- are current sourcing at 10-31.2V DC (1 amp maximum per output).
- must be connected to an external power supply.
- can be forced ON or OFF by the program.

## IMPORTANT

You can assign both outputs to a given channel; however, you cannot use the same output with two different channels.

## Table 1 - Assign the 1756-CFM Module Outputs

| In this operational mode   | You can assign outputs that are configured to trigger   |
|----------------------------|---------------------------------------------------------|
| Totalizer                  | Frequency (acceleration) Prover status Fill control     |
| High-Resolution Frequency  | Frequency Frequency rate of change (acceleration)       |

## Use Module Identification and Status Information

Each 1756-CFM module maintains specific identification information that separates it from all other modules. This information assists you in tracking the components of your system.

For example, you can track module identification information to be aware of exactly what modules are in any ControlLogix rack at any time. While you retrieve the module identity, you can also retrieve the module's status.

Each module maintains the information in Table 2:

Table 2 - Module Identification and Status Information

| Module Identification Description   |                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product Type                        | Module product type, such as Digital I/O or Analog I/O module                                                                                                                                                                                                                                                                                                                                              |
|                                     | Catalog Code Module catalog number                                                                                                                                                                                                                                                                                                                                                                         |
| Major Revision                      | Module major revision number                                                                                                                                                                                                                                                                                                                                                                               |
| Minor Revision                      | Module minor revision number                                                                                                                                                                                                                                                                                                                                                                               |
| Status                              | • Controller ownership (if any) • Whether module has been configured • Device-Specific Status, such as: • Self-test • Flash update in progress • Communications fault • Not owned (outputs in Program mode) • Internal fault (need flash update) • Run mode • Program mode (output mods only) • Minor recoverable fault • Minor unrecoverable fault • Major recoverable fault • Major nonrecoverable fault |
| Vendor ID                           | Module manufacturer vendor, for example, Allen-Bradley                                                                                                                                                                                                                                                                                                                                                     |
| Serial Number                       | Module serial number                                                                                                                                                                                                                                                                                                                                                                                       |
|                                     | Length of ASCII Text String Number of characters in module text string                                                                                                                                                                                                                                                                                                                                     |
| ASCII Text String                   | Number of characters in module text string                                                                                                                                                                                                                                                                                                                                                                 |

IMPORTANT

You must perform a WHO service to retrieve this information.

## Notes:

## What This Chapter Contains

<!-- image -->

## Configurable Flowmeter Operation in the ControlLogix System

This chapter describes how the module works within the ControlLogix® system.

In traditional industrial applications, controllers poll flowmeter modules to obtain their status. Controllers also send commands to the flowmeter modules. Retrieving flowmeter status and sending commands occur during the normal I/O program scan.

1756-CFM modules do not follow the traditional operational manner. Instead, they use the Producer/Consumer Model (see page 29 for more information) to produce data without having been polled by a controller first.

Configurable flowmeter modules follow these basic operational steps, as shown in Figure 1 .

1. The Logix controller establishes a connection to the module and downloads configuration via ladder logic and message instructions.
2. Flowmeters transmit input signals to the module.
3. The module calculates volume from accumulated pulse counts as engineering units.
4. Rather than being scanned by an owner-controller, the module periodically multicasts its status to the controller. (see Requested Packet Interval (RPI) on page 19.) The module also multicasts its status to controllers connected by a listen-only connection (page 18).
5. The Logix owner-controller processes the data that it received from the module and returns the appropriate data.

## Ownership

Figure 1 - 1756-CFM Basic Operational Steps

<!-- image -->

## IMPORTANT

The module communication or multicasting behavior varies depending upon whether it operates in the local chassis or in a remote chassis. The following sections detail the differences in data transfers between these setups.

Every 1756-CFM module in the ControlLogix system must be owned by a Logix5550 ® controller. The owner-controller:

- stores configuration data for every module that it owns.
- can be local or remote in regard to the I/O module's position.
- sends configuration data to the module to define the module's behavior within the control system.

Each module continuously maintains communication with its owner during normal operation. When connections are severed or compromised, the module performs as configured, either setting all outputs to reset (ON or OFF) or continuous operations.

Other controllers can also listen to the module (while another controller owns the module) through a listen-only connection. For more information on listenonly connections, see page 18 .

## Use Programming Software

The I/O configuration portion of the programming software generates configuration data structures and tags for that module, whether the module is in a local or remote chassis. A remote chassis, also known as networked, contains the module but not the module's owner-controller.

After creating the module, you can write specific configuration in the module's data structures; you must access the module tags to change information in the data structures. This process is explained in detail in Chapter 5, Configure the Configurable Flowmeter Module .

## IMPORTANT

Application-specific configuration data is transferred to the controller during the program download and sent to the module during the initial power-up. After module operation has begun, you must use ladder logic and message instructions to make configuration changes.

## 1756-CFM Modules in Local Chassis

Configurable flowmeter modules in the same chassis as the owner-controller are ready to run as soon as the configuration data has been downloaded.

## 1756-CFM Modules in Remote Chassis

You can communicate with remote 1756-CFM modules over the following networks:

- ControlNet - Via ControlLogix ControlNet® interface modules

## IMPORTANT

If you use ControlNet, you must run RSNetWorx™ for ControlNet software to enable modules in the networked chassis. Running RSNetWorx for ControlNet software transfers configuration data to networked modules and establishes a network update time (NUT) for ControlNet.

The NUT is compliant with the desired communications options that are specified for each module during configuration.

- EtherNet/IP - Via ControlLogix EtherNet/IP™ communication modules

Follow these general guidelines when you configure modules:

1. Use the programming software to configure all 1756-CFM modules for a given controller and download that information to the controller.
2. If the configuration data references a module in a remote chassis over a ControlNet network, run RSNetWorx for ControlNet software.

## IMPORTANT

You must run RSNetWorx for ControlNet software whenever a new module is added to a remote chassis that is accessed via a ControlNet network.

When a module is permanently removed from a remote chassis that is accessed via a ControlNet network, we recommend that you run RSNetWorx for ControlNet software to optimize the allocation of network bandwidth.

## Connections

Logix controllers make connections to 1756-CFM modules to exchange data. The controller can make either of these connections to a module:

- Direct Connections - Only one controller can make this connection to a module.
- Listen-Only Connections - Multiple controllers can make this connection to a module simultaneously.

## Direct Connections

A direct connection is a real-time data transfer link between the controller and the device that occupies the slot that the configuration data references. When module configuration data is downloaded to an owner-controller, the controller attempts to establish a direct connection to each of the modules referenced by the data. One of these events occurs:

- If the data is appropriate to the module found in the slot, a connection is made and operation begins.
- If the configuration data is not appropriate, the data is rejected and an error message displays in the software. In this case, the configuration data can be inappropriate for any of a number of reasons. For example, a module's configuration data can be appropriate except for a mismatch in electronic keying that helps prevent normal operation.

The controller maintains and monitors its connection with a module. Any break in the connection, such as removal of the module from the chassis while under power, causes the controller to set fault status bits in the data area associated with the module. The programming software can monitor this data area to announce the modules' failures.

IMPORTANT

Each 1756-CFM module requires one connection.

## Listen-Only Connections

Any controller in the system can listen to the data from any 1756-CFM module even if the controller does not own the module. That is, the controller does not have to hold the module's configuration data to listen to the module.

During the module creation process in the programming software, you can specify the 'Listen-Only' Communication Format. For more information on Communication Format, see page 74 .

Choosing 'Listen-Only' mode allows the controller and module to establish communications without the controller sending any configuration data. In this instance, another controller owns the module.

## IMPORTANT

Controllers using the Listen-Only mode continue to receive data multicast from the module as long as a connection between an owner and module is maintained.

If the connection between all owners and the module is broken, the module stops multicasting data and connections to all 'Listening controllers' are also broken.

## 1756-CFM Modules in a Local Chassis

The 1756-CFM modules multicast their data periodically. Multicast frequency depends on the options that are chosen during configuration and where in the control system the module physically resides. The data consumer (an ownercontroller) is responsible for knowing that the format of the new data is integers.

## Requested Packet Interval (RPI)

This configurable parameter instructs the module to multicast its channel and status data to the local chassis backplane at specific time intervals.

The RPI instructs the module to multicast the current contents of its onboard memory when the RPI expires, that is, the module does not update its channels before the multicast, as shown in this figure.

<!-- image -->

## IMPORTANT

You set the RPI value during the initial module configuration and can adjust it when the controller is in Program mode.

The minimum RPI is determined by channel usage. For each channel using High-Resolution Frequency mode, add 5 ms to the minimum RPI. For each channel using Totalizer mode, add 50 ms to the minimum RPI.

For example, if one channel uses High-Resolution Frequency mode and the other goes unused, the minimum RPI = 5 ms. If one channel uses High-Resolution Frequency mode and the other uses Totalizer mode, the minimum RPI = 55 ms.

## 1756-CFM Modules in a Remote Chassis

If a module resides in a networked chassis, the role of the RPI changes slightly regarding getting data to the owner.

The RPI not only defines when the module multicasts data within its own chassis (as described in the previous section), but also determines how often the owner-controller receives it over the network.

When an RPI value is specified for a module in a remote chassis, in addition to instructing the module to multicast data within its own chassis, the RPI also "reserves" a spot in the stream of data flowing across the network.

The timing of this "reserved" spot may or may not coincide with the exact value of the RPI, but the control system guarantees that the owner controller receives data at least as often as the specified RPI.

See Figure 2 for a better understanding of the data flow with a module in a remote chassis.

Figure 2 - Module in Remote Chassis with RPI Reserving a Spot in Flow of Data

<!-- image -->

## What This Chapter Contains

## Understand General Module Features

<!-- image -->

## 1756-CFM Module Features and Operational Modes

This chapter describes the 1756-CFM module's features and operational modes.

This chapter provides only a general description of each feature, whether general or operational mode-specific. For examples of how to use these features in your module's configuration, see Configure the Configurable Flowmeter Module on page 69 .

These general module features are available with the 1756-CFM module.

## Removal and Insertion Under Power (RIUP)

All 1756-CFM modules can be inserted and removed from the chassis while power is applied. This feature allows greater availability of the overall control system because, while the module is being removed or inserted, there is no additional disruption to the rest of the controlled process.

## Module Fault Reporting

The modules provide both hardware and software indication when a module fault has occurred. Each module's LED fault indicator and the programming software will graphically display this fault and include a fault message describing the nature of the fault.

This feature lets you determine how your module has been affected and what action should be taken to resume normal operation.

## Fully Software Configurable

The programming software uses a custom, easily understood interface to write configuration. All module features are enabled or disabled through the I/O configuration portion of the software.

You can also use the software to interrogate any module in the system to retrieve:

- serial number
- revision information
- catalog number

- vendor identification
- error/fault information
- diagnostic counters.

By eliminating such tasks as setting hardware switches and jumpers, the software makes module configuration easier and more reliable.

## Electronic Keying

The electronic keying feature automatically compares the expected module, as shown in the programming software I/O Configuration tree, to the physical module before I/O communication begins. You can use electronic keying to help prevent communication to a module that does not match the type and revision expected.

For each module in the I/O Configuration tree, the user-selected keying option determines if, and how, an electronic keying check is performed. Typically, three keying options are available:

- Exact Match
- Compatible Keying
- Disable Keying

You must carefully consider the benefits and implications of each keying option when selecting between them. For some specific module types, fewer options are available.

Electronic keying is based on a set of attributes unique to each product revision. When a Logix 5000 ™ controller begins communicating with a module, this set of keying attributes is considered.

Table 3 - Keying Attributes

| Attribute      | Description                                                                                                                                                                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vendor         | The manufacturer of the module, for example, Rockwell Automation/Allen-Bradley.                                                                                                                                                                                                                                                   |
| Product Type   | The general type of the module, for example, communication adapter, AC drive, or digital I/O.                                                                                                                                                                                                                                     |
| Product Code   | The specific type of module, generally represented by its catalog number, for example, 1756-IB16I.                                                                                                                                                                                                                                |
| Major Revision | A number that represents the functional capabilities and data exchange formats of the module. Typically, although not always, a later, that is higher, Major Revision supports at least all of the data formats supported by an earlier, that is lower, Major Revision of the same catalog number and, possibly, additional ones. |
| Minor Revision | A number that indicates the module’s specific firmware revision. Minor Revisions typically do not impact data compatibility but can indicate performance or behavior improvement.                                                                                                                                                 |

You can find revision information on the General tab of a module Properties dialog box.

## Figure 3 - General Tab

<!-- image -->

## IMPORTANT

Changing electronic keying selections online can cause the I/O communication connection to the module to be disrupted and can result in a loss of data.

## Exact Match

Exact Match keying requires all keying attributes, that is, Vendor, Product Type, Product Code (catalog number), Major Revision, and Minor Revision, of the physical module and the module created in the software to match precisely to establish communication. If any attribute does not match precisely, I/O communication is not permitted with the module or with modules connected through it, as in the case of a communication module.

Use Exact Match keying when you need the system to verify that the module revisions in use are exactly as specified in the project, such as for use in highlyregulated industries. Exact Match keying is also necessary to enable Automatic Firmware Update for the module via the Firmware Supervisor feature from a Logix 5000 controller.

## EXAMPLE

In this scenario, Exact Match keying prevents I/O communication.

The module configuration is for a 1756-IB16D module with module revision 3.1. The physical module is a 1756-IB16D module with module revision 3.2. In this case, communication is prevented because the Minor Revision of the module does not match precisely.

Module Configuration

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IB16D

Major Revision = 3

Minor Revision = 1

Physical Module

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IB16D

Major Revision = 3

Minor Revision = 2

<!-- image -->

## IMPORTANT

Changing electronic keying selections online can cause the I/O Communication connection to the module to be disrupted and can result in a loss of data.

## Compatible Keying

Compatible Keying indicates that the module determines whether to accept or reject communication. Different module families, communication adapters, and module types implement the compatibility check differently based on the family capabilities and on prior knowledge of compatible products. Release notes for individual modules indicate the specific compatibility details.

Compatible Keying is the default setting. Compatible Keying allows the physical module to accept the key of the module configured in the software, provided that the configured module is one the physical module is capable of emulating. The exact level of emulation required is product and revision specific.

With Compatible Keying, you can replace a module of a certain Major Revision with one of the same catalog number and the same or later, that is higher, Major Revision. In some cases, the selection makes it possible to use a replacement that is a different catalog number than the original. For example, you can replace a 1756-CNBR module with a 1756-CN2R module.

When a module is created, the module developers consider the module's development history to implement capabilities that emulate those of the previous module. However, the developers cannot know future developments. Because of this, when a system is configured, we recommend that you configure your module using the earliest, that is, lowest, revision of the physical module that you believe will be used in the system. By doing this, you can avoid the case of a physical module rejecting the keying request because it is an earlier revision than the one configured in the software.

## EXAMPLE

In this scenario, Compatible Keying prevents I/O communication:

The module configuration is for a 1756-IB16D module with module revision 3.3. The physical module is a 1756-IB16D module with module revision 3.2. In this case, communication is prevented because the minor revision of the module is lower than expected and may not be compatible with 3.3.

Module Configuration

Vendor = Allen-Bradley Product Type = Digital Input Module Catalog Number = 1756-IB16D Major Revision = 3

Minor Revision = 3

Physical Module Vendor = Allen-Bradley Product Type = Digital Input Module Catalog Number = 1756-IB16D Major Revision = 3

Minor Revision = 2

<!-- image -->

## EXAMPLE

## IMPORTANT

## Disabled Keying

Disabled Keying indicates the keying attributes are not considered when attempting to communicate with a module. Other attributes, such as data size and format, are considered and must be acceptable before I/O communication is established. With Disabled Keying, I/O communication can occur with a module other than the type specified in the I/O Configuration tree with unpredictable results. We generally do not recommend using Disabled Keying.

<!-- image -->

ATTENTION: Be extremely cautious when using Disabled Keying; if used incorrectly, this option can lead to personal injury or death, property damage, or economic loss.

In this scenario, Compatible Keying allows I/O communication:

The module configuration is for a 1756-IB16D module with module revision 2.1. The physical module is a 1756-IB16D module with module revision 3.2. In this case, communication is allowed because the major revision of the physical module is higher than expected and the module determines that it is compatible with the prior major revision.

Module Configuration

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IB16D

Major Revision = 2

Minor Revision = 1

<!-- image -->

Communication is allowed.

Physical Module

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IB16D

Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

Changing electronic keying selections online can cause the I/O communication connection to the module to be disrupted and can result in a loss of data.

If you use Disabled Keying, you must take full responsibility for understanding whether the module being used can fulfill the functional requirements of the application.

## EXAMPLE

## EXAMPLE

In this scenario, Disable Keying prevents I/O communication:

The module configuration is for a 1756-IA16 digital input module. The physical module is a 1756-IF16 analog input module. In this case, communication is prevented because the analog module rejects the data formats that the digital module configuration requests.

Module Configuration

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IA16

Major Revision = 3

Minor Revision = 1

<!-- image -->

Communication is prevented.

Physical Module

Vendor = Allen-Bradley

Product Type = Analog Input Module

Catalog Number = 1756-IF16

Major Revision = 3

Minor Revision = 2

<!-- image -->

<!-- image -->

In this scenario, Disable Keying allows I/O communication:

The module configuration is for a 1756-IA16 digital input module. The physical module is a 1756-IB16 digital input module. In this case, communication is allowed because the two digital modules share common data formats.

Module Configuration

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IA16

Major Revision = 2

Minor Revision = 1

<!-- image -->

Communication is allowed.

<!-- image -->

Physical Module

Vendor = Allen-Bradley

Product Type = Digital Input Module

Catalog Number = 1756-IB16

Major Revision = 3

Minor Revision = 2

<!-- image -->

| IMPORTANT   | Changing electronic keying selections online can cause the I/O communication connection to the module to be disrupted and can result in a loss of data.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

## Producer/Consumer Model

By using the Producer/Consumer model, the modules can produce data without having been polled by a controller first. The modules produce the data and any other owner controller device can decide to consume it.

## Module Status Information

The 1756-CFM module has status indicators on the front of the module that allow you to check the module health and operational status.

These status can be checked with the status indicators:

- Input point status - display indicates a particular points status, including specific indicators for the input F and Z points for each channel
- Output point status - display indicates the status of two output points on the module

For an example of the status indicators, see page 103 .

## Configurable Flowmetering Channels

The module offers two configurable Flowmetering channels. Each channel uses two Flowmeter inputs (F0 &amp; F1) and two corresponding gate inputs (Z0 &amp; Z1).

## Flowmeter Inputs

Two flowmeter inputs (F0 &amp; F1) are available on your module. The inputs are capable of receiving these input signals:

- +/- 30V peak from passive Magnetic Pickups
- 5V DC logic (TTL compatible)
- 12-24V DC powered preamp outputs

## Gate Inputs

The module offers two gate inputs (Z0 &amp; Z1). You can wire the inputs for single-ended or differential applications and can accept signals at 5V DC or 1224V DC.

IMPORTANT

The Z0 and Z1 inputs can have different voltages connected to them simultaneously.

## Operate in High Resolution Frequency Mode

## User-Defined Preset and Rollover Values

The module has a maximum count of 2,147,483,647, but you can define the rollover values below this limit.

## Current-Sourcing Outputs

Two current-sourcing outputs are available on the module. Each output:

- can be tied to any Flowmeter input.
- operates in the 10-31.2V DC range (1A maximum per output).
- operates at 5V DC level (3-20mA maximum per output).

Choose an Operational Mode The module counts pulses from Flowmeters and operates in these modes:

- High Resolution Frequency mode
- Totalizer mode

You must choose an operational mode for your 1756-CFM module in the programming software.

In High Resolution Frequency mode, the module calculates frequency over a user-defined time period up to 2 seconds. Frequency sampling begins on the leading edge of the first pulse and ends on the next pulse to occur after the sampling period expires.

This figure shows a 1756-CFM module in a turbine shaft speed-monitoring application in High Resolution Frequency mode.

<!-- image -->

You must calculate a resolution for this mode. Use this equation to calculate resolution.

<!-- formula-not-decoded -->

Resolution =

Where:

- F in is the input frequency
- T sample is the sample time period

This table lists sample Fin and Tsample values and the corresponding resolution.

Table 4 - Sample Resolutions

| F in   | T sample                      | Resolution   |
|--------|-------------------------------|--------------|
|        | 60Hz 0.033 seconds 0.00045Hz  |              |
|        | 5000Hz 0.020 seconds 0.0625Hz |              |
|        | 50,000Hz 0.050 seconds 0.25Hz |              |

The values listed in Table 4 are listed for example purposes. Specific values will change according to your application.

## Terminal Usage in High Resolution Frequency Mode

In High Resolution Frequency mode, F0 and F1 are used as inputs.

## Output Operation in High Resolution Frequency Mode

In High Resolution Frequency mode, outputs can:

- operate normally
- be forced ON or OFF.
- be tied to the frequency flowmeter input (that is, F1).

## Module Features Used in High Resolution Frequency Mode

These module features are available in High Resolution Frequency mode.

| Module Feature            |   Page |
|---------------------------|--------|
| Low Frequency Clear       |     30 |
| Sample Time               |     30 |
| Acceleration Calculation  |     30 |
| Meter Factor              |     30 |
| Trigger On                |     30 |
| Tie to Counter            |     30 |
| Highest Allowed Frequency |     31 |
| Acceleration Alarm Value  |     31 |
| Frequency Average         |     31 |
| Acceleration              |     31 |

## Low Frequency Clear

Use Low Frequency Clear to set a minimum frequency level. Any frequencies detected below this level will be set 0.

## Sample Time

Use Sample Time to determine the length of time each sample uses. The maximum sample time is 2 seconds.

## Acceleration Calculation

Acceleration Calculation is derived by using the rate of change of frequency over a specified number of samples (1 to 255). This moving average produces quick responses when the number of samples = 1 and stable, but slower, responses when the number of samples =255.

The default number of samples used = 255, but a typical application uses 50 samples. There are significant differences between response times. For example, the quick response offer acceleration calculations more often but is more likely to set off the Acceleration Alarm for calculation spikes at low frequencies. The stable responses are slower but ignore acceleration spikes in favor of definitive operational trends.

| IMPORTANT   | Acceleration Calculation values can be entered on the bit level or byte level. If you are entering values at the byte level, you must use -1 to represent 255. If you are entering values on the bit level, you can use the actual number value.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Meter Factor

Meter Factor is used to calibrate the frequency (Hz) to a user-defined standard. For example, the module can read 59.9 Hz while the standard is set for 59.7 Hz. In this case, the meter factor (default = 1.0) should be changed to 0.99666 to correct the reading.

## Trigger On

Use Trigger On to determine what state triggers an output to energize in High Resolution Frequency mode (that is, an output can be configured to turn ON if the Frequency Average reaches a particular frequency.

- Frequency - Input exceeds MaxAllowedFreq.
- Acceleration - Input speed accelerates beyond AccelAlarmValue.

## IMPORTANT

For the Trigger On feature, Frequency and Acceleration are tied to the Overspeed Alarm and Acceleration Alarm respectively. The alarms remain latched ON once set and can only be reset if you toggle the Alarm Enable bits.

## Tie to Counter

Choose which output is connected to which flowmeter input.

## Highest Allowed Frequency

Use Highest Allowed Frequency to set the trigger point for Frequency. In other words, set this value so that when the input reaches it, the outputs are energized. This value is also used for the Overspeed Alarm.

## Acceleration Alarm Value

Use Acceleration Alarm to set the trigger point for Acceleration. In other words, set this value so that when the input reaches it, the outputs are energized. This value is also used for the Acceleration Alarm.

## Frequency Average

With Frequency Average, the module divides meter counts by a user-defined sample interval (up to 2 seconds) to determine the Frequency Average.

## Acceleration

Use Acceleration to determine an acceleration value over a user-defined number of samples.

## Alarms in High Resolution Frequency Mode

High Resolution Frequency mode offers these alarms:

- Overrange Alarm
- Overspeed Alarm
- Acceleration Alarm

You must enable each alarm. When any of the alarms occur, it is latched and remains on until the user resets the alarm.

## Sample Configuration for High Resolution Frequency Mode

To see a sample configuration for a 1756-CFM module using High Resolution Frequency mode, including the use of all the features mentioned in the previous section, see page 88 .

## Operate in Totalizer Mode

In Totalizer mode, the 1756-CFM module counts pulses and scales them to engineering units. Every effort is made to store the least significant count even when the least significant unit of the total is larger. The module calculates three forms of calculated frequency:

- Frequency over a fixed period
- Frequency over a requested number of samples
- Moving average of the frequency

All of the forms mentioned above are available in Totalizer mode. In this mode, the module also offers these functions:

- Prover function
- Filler function

These functions are described later in this chapter.

## Nonresettable Totalizer

Configure the module for Nonresettable Totalizer mode to make sure the total counts value is not reset during normal module operation. The module stores total count values up to 2 31 -1 (2,147,483,647) counts.

IMPORTANT

The total count value can be reset in Nonresettable Totalizer mode if power is cycled to the module for any reason (for example, module is removed from and reinserted to the chassis).

## Terminal Usage in Totalizer Mode

In Totalizer mode, F0 and F1 are used as inputs. Z0 and Z1 are used as prover signals.

## Output Operation in Totalizer Mode

In Totalizer mode, outputs:

- can operate normally or be forced ON or OFF.
- can be tied to either flowmeter input. If one channel is configured for trickle operation, both outputs are tied to that flowmeter input.

## Use the Totalizer Mode Prover Function

Logix controller:

- performs AGA/API calculations
- controls prover
- calculates/compensates based on actual temperature

In the Totalizer mode prover function, the 1756-CFM module interfaces to a prover and counts pulses using a flowmeter or positive displacement meter. The module then scales pulse count to engineering units. The module can also use this mode to calculate frequency over a user-defined time period, where frequency is calculated as counts per unit time.

Either module output can be tied to either flowmeter input with the prover function, and output operation can occur independently from new data from the Logix owner-controller.

With the prover function, the Totalizer is active all the time, but the prover function must first be enabled and started to activate the Prover Total. Once the prover function is started, only the gate signal or a user-override (that is, clearing the Prover Enable bit) can eliminate the function. However, the Gross Volume, Net Volume, and Fill Total will continue to accumulate as long as the flow input frequency is enabled and is greater than Low Frequency Clear.

This figure shows a 1756-CFM module in a petrochemical flow and custody transfer application while operating in the Totalizer mode prover function.

<!-- image -->

## Use a Prover

A prover is used for the calibration of liquid meters in custody transfer applications. This calibration is done by comparing a metered throughput to a known volume in the prover. When enabled, the prover total updates while the spheroid moves between two detectors and is then compared to the predetermined volume of the prover section to ascertain the meter factor.

If you are using the Totalizer or Nonresettable Totalizer mode for capturing meter counts during a prover calibration, you have the option of selecting either of these types of provers:

- Unidirectional - With a unidirectional prover, the module:
- begins updating Prover Total when the spheroid passes the first detector
- stops updating Prover Total when the spheroid passes the second detector
- Bidirectional - With a bidirectional prover, the module:
- begins updating Prover Total when the spheroid passes the first detector
- stops counting when the spheroid passes the second detector (Prover Total is updated at this time - intermediate value returned)
- continues updating when the spheroid returns past the second detector
- stops updating when the spheroid returns past the first detector (Prover Total Count Value is updated at this time)

This figure shows an example of a spheroid and detectors.

<!-- image -->

## Features Available with the Prover Function

These module features are available with the Totalizer mode prover function.

| Module Feature      |   Page |
|---------------------|--------|
| Prover Direction    |     35 |
| Low Frequency Clear |     35 |
| Trigger On          |     36 |
| Tie to Counter      |     36 |
| Total Overflow      |     36 |
| Total Overrange     |     36 |
| Total Overspeed     |     37 |
| Total Acceleration  |     37 |
| Prover Total        |     37 |
| Total Counts        |     37 |
| Frequency Average   |     37 |
| Frequency Period    |     37 |
| Speed               |     38 |
| Acceleration        |     38 |
| Gross Volume        |     38 |
| Net Volume          |     38 |
| Gross Rate          |     39 |
| Net Rate            |     40 |

## Prover Direction

You can operate the module as a unidirectional or bidirectional prover. Use Prover Direction to configure the module for the prover type used in your application.

## Low Frequency Clear

Use Low Frequency Clear to set a minimum frequency level. Any counts detected below this level will not be used in count calculations.

## Trigger On

Use Trigger On to determine what flowmeter state triggers the output to energize. For example, you can configure the module to trigger an output when the flowmeter reaches a particular frequency (count).

These events can trigger output 0 when using the flowmeter function:

- Frequency - flowmeter exceeds a certain frequency (count)
- Acceleration - flowmeter accelerates beyond a particular rate
- Prover Run State - flowmeter is operating in the run state
- Prover Range State - flowmeter is enabled and not complete
- Full Flow - flowmeter is in Full Flow mode
- Trickle Flow - flowmeter is in Trickle Flow mode

## Tie to Counter

Choose which output is connected to which flowmeter input.

## Total Overflow

Use Total Overflow to monitor when the total counts has exceeded the rollover value. The rollover value is a user-defined value set during configuration. Three events must occur for you to use this feature:

- Overflow is enabled
- You set a rollover value
- The count total exceeds the rollover value

When the rollover value is exceeded, the Total Overflow bit is toggled to indicate the event and the Overflow Alarm is set.

## Total Overrange

Use Total Overrange to monitor when a flowmeter exceeds the maximum frequency (100 kHz). The maximum frequency period is calculated by the number of pulses being counted by the flowmeter per second. When the frequency period exceeds 100 kHz, and the Overrange Alarm is enabled, the Overrange Alarm is set.

## Total Overspeed

Use Total Overspeed to monitor when a flowmeter exceeds the Highest Allowed Frequency. With this feature, the module calculates speed by the number of pulses counted in a user-defined sampling period. When the speed exceeds Highest Allowed Frequency, and the Overspeed Alarm is enabled, the Overspeed Alarm is set.

## Total Acceleration

Use Total Acceleration to monitor when a flowmeter exceeds the maximum acceleration rate. The acceleration rate is calculated by using a three-point difference formula with unevenly spaced points. The acceleration calculation indicates the number of samples used in the calculation.

## Prover Total

Use Prover Total to monitor the raw counts received during the Prover portion of the cycle. The Prover Total represents a net total count value obtained by applying a K-factor and CCF or AGA 7 compensation to the raw count.

## Total Counts

Use Total Counts to monitor the total number of counts the module has received since it was last reset to zero.

## Frequency Average

Use Frequency Average when Frequency Period must be averaged over multiple samples (meter samples). You must configure the module with a userdefined number of Meter Samples to use this feature. This uses the total counts over the total time per a user-defined number of meter samples. (A meter sample is approximately 20.0 ms.)

## Frequency Period

Use Frequency Period to determine the frequency over a user-defined sample time.

## Speed

To use the Speed feature, you must set a resolution. The module uses the resolution to determine the number of counts used in the Speed calculation.

For example, if you set the resolution at 0.00001, the module requires 100,000 counts. In this case, the module examines the previous samples stored in its buffers until 100,000 counts are found. The counts are divided by the time it took to accumulate them and the resulting value is the module speed.

## Acceleration

Use Acceleration to determine an acceleration value over a user-defined number of samples.

## Gross Volume

Use Gross Volume to convert total counts to volumetric units. The module employs a user-defined K-factor in the conversion. For example, you can configure the module so that 4 counts = 1 pint. The module can then convert the total number of counts received to a total number of pints.

## Net Volume

The Net Volume value represents the Gross Volume value with a AGA 7 or Logix compensation applied. This value is calculated at an application's base (that is, standard) operating conditions.

## Gross Rate

Use Gross Rate to convert total counts to rate units. The module employs a user-defined K-factor in the conversion. The K-factor is a divisor, and the time interval is divided by this number, as shown below.

<!-- image -->

- If the input frequency is below 100Hz, the K-factor used is always 10.0 for frequencies interpolated between 0-100Hz.
- If the input frequency is between 100Hz and 200Hz, the K-factor is interpolated as follows:

<!-- formula-not-decoded -->

- If the input frequency is between 200Hz and 300Hz, the K-factor is interpolated as follows:

<!-- formula-not-decoded -->

- If the input frequency is greater than 300Hz, the K-factor used is always 100.0. There is no K-factor calculation over 300Hz.

To use Gross Rate, you must set the K-factor values in Module Tags, as shown.

| Name                                                                                          | Style   |      |           | Data type Value Change during operation   |
|-----------------------------------------------------------------------------------------------|---------|------|-----------|-------------------------------------------|
| C.Operations[0].kFactStruct.kFactorForChan[0]                                                 | Float   | REAL | 25.0(1)   | Yes                                       |
| C.Operations[0].kFactStruct.kFactorForChan[1] Float REAL                                      |         |      | 25.0(1)   | Yes                                       |
| C.Operations[0].kFactStruct.kFactorForChan[2]                                                 | Float   | REAL | 71.0      | Yes                                       |
| C.Operations[0].kFactStruct.kFactorForChan[3]                                                 | Float   | REAL | 111.0     | Yes                                       |
| C.Operations[0].kFactStruct.kFactorForChan[4]- C.Operations[0].kFactStruct.kFactorForChan[12] | Float   | REAL | 0         | Yes                                       |
| C.Operations[0].kFactStruct.FreqAtKFactor[0]                                                  | Float   | REAL | 0.0       | Yes                                       |
| C.Operations[0].kFactStruct.FreqAtKFactor[1]                                                  | Float   | REAL | 100.0     | Yes                                       |
| C.Operations[0].kFactStruct.FreqAtKFactor[2]                                                  | Float   | REAL | 200.0 Yes |                                           |
| C.Operations[0].kFactStruct.FreqAtKFactor[3]                                                  | Float   | REAL | 300.0 Yes |                                           |
| C.Operations[0].kFactStruct.FreqAtKFactor[4]- C.Operations[0].kFactStruct.FreqAtKFactor[12]   | Float   | REAL | 0         | Yes                                       |

IMPORTANT

For more information on setting values in the Module Tags, see Configure the Configurable Flowmeter Module on page 69 .

## Net Rate

Use Net Rate in a fashion similar to Gross Rate. The key difference between Gross Rate and Net Rate is that Net Volume also uses a user-defined compensation factor (that is, AGA 7 or Logix compensation) to convert net counts to net rate units.

## Prover Status

Prover Status notifies you of these prover states:

- Prover not active
- Prover waiting for 1st start
- Prover waiting for 1st stop
- Prover waiting for 2nd start
- Prover waiting for 2nd stop
- Prover complete

## Alarms with the Prover Function

The module offers these alarms when operating with the prover function:

- Overflow Alarm
- Overrange Alarm
- Overspeed Alarm
- Acceleration Alarm

You must enable each alarm. When any of the alarms occur, it is latched and remains on until you reset the alarm. (Toggle the alarm enable bit to reset the alarm.)

## Sample Configuration for Totalizer Mode Prover Function

To see a sample configuration for a 1756-CFM module using Totalizer mode prover function, including the use of all the features mentioned in the previous section, see page 91 .

## Use the Totalizer Mode Filler Function

The Totalizer mode filler function performs the basic operations of a fill application, including these basic steps:

- Set a target fill volume
- Start filling
- Stop filling when the target volume is reached

Within the basic operations mentioned above, the filler function provides multiple features that can be configured to adjust the fill application for specific circumstances. Those features are described later in this chapter.

The filler function requires a ladder program transition to start the fill cycle. Similar to the prover function, the Totalizer is active all the time, but the Filler function must be first enabled, and started to activate the Fill Total.

This figure shows a 1756-CFM module in a brewery flow monitoring application while operating in the Totalizer mode filler function. The application shown requires additional ladder logic.

<!-- image -->

## Trickle Function for Totalizer Mode

The trickle function is used with the filler function to improve volume repeatability in a filling application. The trickle function requires two filling lines and an optional discrete module to activate the trickle valve. Activation of the valve should be sized for worst case volume at least 100 ms based on typical program scan = 5 ms and an output module RPI = 25 ms.

For most of the filling process, the full flow state is assigned to one of the module's outputs. For more repeatable fills or to prevent overfills, the pretrigger feature helps make sure that the full flow valve turns off before it reaches the Fill Transition or Fill Total Target volume.

When the filling application reaches the user-defined Fill Transition point, the trickle Totalizer mode changes the application from the full flow line to the trickle flow line. This slower line allows the application to finish the filling process without any waste.

For more information on the Fill Transition feature, see page 48 .

The filler function can be used in any of these conditions:

- Starting with the trickle flow
- Filling with the full flow only
- Restarting the timed trickle flow
- Starting the trickle flow prior to the fill transition
- Restarting full flow while in trickle flow

Using the Trickle feature in previously mentioned conditions requires specific configuration changes.

## Configurable Features Available with the Totalizer Mode Filler Function

These configurable features are available with the Totalizer mode filler function:

| Module Features       |   Page |
|-----------------------|--------|
| Low Frequency Clear   |     43 |
| PreTrigger            |     43 |
| Fill Mode             |     44 |
| Trigger On            |     44 |
| Tie to Counter        |     44 |
| Fill Enable           |     44 |
| Fill Start            |     44 |
| Fill Hold             |     45 |
| Fill State            |     45 |
| Fill Total            |     45 |
| Total Counts          |     46 |
| Gross Volume          |     46 |
| Net Volume            |     46 |
| Net Rate              |     48 |
| Fill Total Target     |     48 |
| Fill Transition       |     48 |
| Fill Transition Timer |     48 |

## Low Frequency Clear

Use Low Frequency Clear to set a minimum frequency level. Any frequencies detected below this level will not be used in count calculations.

Low Frequency Clear uses two tags to configure channel 0.

- Local:X.C.Ch0LowFreqClear
- Local:X.C.Operations[0].MinDetectableFreq

## PreTrigger

PreTrigger works only on the Full Flow state. PreTrigger turns OFF the Full Flow state when it determines that the Fill Transition or Fill Total Target will be met before the next update. You must assign a channel to the local module output for this feature to provide repeatable operation.

## Fill Mode

Use Fill mode to choose volume or time for Trickle mode operation.

## Trigger On

Use Trigger On to determine what state triggers output 0 to energize. For example, you can configure the module to trigger an output when the prover reaches a particular frequency.

These events can trigger an output in Filler mode:

- Frequency - Input exceeds a certain frequency (latched).
- Acceleration - Input accelerates at a particular rate (latched).
- Full Flow State - Module is operating in the full flow state.
- Trickle Flow State - Module is operating in trickle state.

## Tie to Counter

Choose which output is connected to which channel's Totalizer. There are two outputs on each module.

## Fill Enable

Use Fill Enable to reset the Fill Total value. This feature does not reset the Gross Volume or Net Volume. You must use the reset for the Totalizer to reset those values.

## Fill Start

Fill Start starts the Fill upon transition from 0 to 1. Reset the Fill Enable to reset this feature. If any outputs are connected to the channel, they will transition back to reset and close the valve.

## Fill Hold

## Use the Fill Hold feature to shutdown the:

- full flow valve

or

- trickle flow valve.

Setting the Fill Hold feature changes the Fill State to 0 and causes the fill function to continue even when the Fill Start has been reset.

## Fill State

Use Fill State to monitor the current state of the module. These fill states are possible:

- Filler not active or In Hold
- Filler Enabled only, waiting for start
- Timed Trickle Flow complete, not filled
- Full Flow Active (or Running)
- Timed Trickle Flow Active
- Full Flow Active
- Trickle Flow Active
- Fill complete (7 in module tags)

<!-- image -->

Use the Fill States to operate a trickle flow valve connected to an optional digital output module.

## Fill Total

Use Fill Total to determine the current total in an ongoing fill application. During the fill cycle, use Net Volume to check the Fill Total.

## Total Counts

Use Total Counts for the accumulated raw counts the module has received since its last reset. The total counts can be used for applications that employ a different methodology to calculate Gross and Net Volumes.

## Gross Volume

Use Gross Volume to convert total counts to volumetric units. The module employs a user-defined K-factor in the conversion. For example, you can configure the module so that 4 counts = 1 pint. A meter factor is also available for calibration.

## Net Volume

Use Net Volume to apply a user-defined compensation factor (that is, AGA 7 or Logix compensation) to the Gross Volume. This feature uses this equation:

<!-- image -->

## Gross Rate

Use Gross Rate to convert total counts to rate units. The module employs a user-defined K-factor in the conversion. The K-factor is a divisor, and the time interval is divided by this number, as shown.

<!-- image -->

| Gross Rate =   | Total Counts in Meter Sample   | Meter Factor   |
|----------------|--------------------------------|----------------|

- If the input frequency is below 100 Hz, the K-factor used is always 10.0 for frequencies interpolated between 0-100 Hz.

- If the input frequency is greater than 100Hz-200Hz, the K-factor is interpolated as follows:

<!-- formula-not-decoded -->

- If the input frequency is greater than 200Hz-300Hz, the K-factor is interpolated as follows:

<!-- formula-not-decoded -->

- If the input frequency is greater than 300Hz, the K-factor used is always 100.0. There is no K-factor calculation over 100Hz.

To use Gross Rate, you must set the K-factor values in Module Tags, as shown.

| Name                                                                                          | Style Data type Value   | Change during operation   |
|-----------------------------------------------------------------------------------------------|-------------------------|---------------------------|
| C.Operations[0].kFactStruct.kFactorForChan[0] Float REAL                                      | 25.01                   | Yes                       |
| C.Operations[0].kFactStruct.kFactorForChan[1] Float REAL                                      | 25.01                   | Yes                       |
| C.Operations[0].kFactStruct.kFactorForChan[2] Float REAL 71.0 Yes                             |                         |                           |
| C.Operations[0].kFactStruct.kFactorForChan[3] Float REAL 111.0 Yes                            |                         |                           |
| C.Operations[0].kFactStruct.kFactorForChan[4]- C.Operations[0].kFactStruct.kFactorForChan[12] |                         | Float REAL 0 Yes          |
| C.Operations[0].kFactStruct.FreqAtKFactor[0] Float REAL 0.0 Yes                               |                         |                           |
| C.Operations[0].kFactStruct.FreqAtKFactor[1] Float REAL 100.0 Yes                             |                         |                           |
| C.Operations[0].kFactStruct.FreqAtKFactor[2] Float REAL 200.0 Yes                             |                         |                           |
| C.Operations[0].kFactStruct.FreqAtKFactor[3]                                                  | Float REAL 300.0        | Yes                       |
| C.Operations[0].kFactStruct.FreqAtKFactor[4]- C.Operations[0].kFactStruct.FreqAtKFactor[12]   | Float REAL 0            | Yes                       |

IMPORTANT

For more information on setting values in the Module Tags, see Configure the Configurable Flowmeter Module on page 69 .

## Net Rate

Use Net Rate to convert Net Volume to a rate by using this equation:

<!-- image -->

## Fill Total Target

Fill Total Target is the user-defined final volume (in engineering units) for a total fill.

## Fill Transition

Fill Transition is the user-defined Net Volume value to switch from full flow to trickle flow.

## Fill Transition Timer

After the transition from full flow to trickle flow, the Fill Transition Timer value determines how long the trickle will last (that is, this feature sets the time that the trickle valve is open or ON).

## Alarms with the Filler Function

The module offers these alarms when operating the filler function:

- Overflow Alarm - TotalCounts &gt; RollOver Value
- Overrange Alarm - FreqPeriod &gt; 100kHz
- Overspeed Alarm - Speed &gt; Highest Allowed Frequency
- Acceleration Alarm - Acceleration &gt; Acceleration Alarm Value

You must enable each alarm. When any of the alarms occur, it is latched and remains on until you reset the alarm. (Toggle the alarm enable bit to reset the alarm.)

## Sample Configuration for Totalizer Mode Filler Function

To see a sample configuration for a 1756-CFM module using Totalizer mode filler function, including the use of all the features mentioned in the previous section, see page 96 .

## Configurable Output Behaviors

Firmware revision 2.4 enables you to configure the 1756-CFM module outputs to turn on or off at specified frequency counts.

Three types of behaviors, listed in the Frequency Values and Resulting Behaviors table, can be configured with the use of firmware revision 2.4. Use this table as a reference when determining on/off frequency values later in the configuration procedure.

Table 5 - On/Off Frequency Behaviors

<!-- image -->

## How To Enable Output Behavior Configuration

To enable output behavior configuration for a 1756-CFM module with firmware revision 2.4, select one of these options.

- If you are using RSLogix 5000® software version 16 or earlier, see page 129 .
- If you are using programming software version 17 or later, add a new module to your I/O Configuration folder and complete these steps.
1. On the Select Module screen, select the 1756-CFM module and click OK.

The Select Major Revision dialog box opens.

<!-- image -->

2. Verify that Major Revision 2 is chosen and click OK.

The New Module dialog box opens with Major Revision 2 chosen.

<!-- image -->

Output Behavior configuration is enabled.

## What This Chapter Contains

## Environment and Enclosure

<!-- image -->

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR 11. Without appropriate precautions, there may be difficulties with electromagnetic compatibility in residential and other environments due to conducted and radiated disturbances.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA, V2, V1, V0 (or equivalent) if nonmetallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional installation requirements
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosures

## North American Hazardous Location Approval

<!-- image -->

| This information applies when operating this equipment in hazardous locations. Informations sur l’utilisation de cet equipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                              | This information applies when operating this equipment in hazardous locations. Informations sur l’utilisation de cet equipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marques "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'a une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livre avec des marquages sur sa plaque d'identification qui indiquent le code de temperature pour les environnements dangereux. Lorsque plusieurs produits sont combines dans un systeme, le code de temperature le plus defavorable (code de temperature le plus faible) peut etre utilise pour determiner le code de temperature global du systeme. Les combinaisons d'equipements dans le systeme sont sujettes a inspection par les autorites locales qualifiees au moment de l'installation. | Les produits marques "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'a une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livre avec des marquages sur sa plaque d'identification qui indiquent le code de temperature pour les environnements dangereux. Lorsque plusieurs produits sont combines dans un systeme, le code de temperature le plus defavorable (code de temperature le plus faible) peut etre utilise pour determiner le code de temperature global du systeme. Les combinaisons d'equipements dans le systeme sont sujettes a inspection par les autorites locales qualifiees au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | EXPLOSION HAZARD - • Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. • Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. • Substitution of components may impair suitability for Class I, Division 2. • If this product contains batteries, they must only be changed in an area known to be nonhazardous.          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | RISQUE D’EXPLOSION – • Couper le courant ou s'assurer que l'environnement est classe non dangereux avant de debrancher l'equipement. • Couper le courant ou s'assurer que l'environnement est classe non dangereux avant de debrancher les connecteurs. Fixer tous les connecteurs externes relies a cet equipement a l'aide de vis, loquets coulissants, connecteurs filetes ou autres moyens fournis avec ce produit. •  La substitution de composants peut rendre cet equipement inadapte a une utilisation en environnement de Classe I, Division 2. • S'assurer que l'environnement est classe non dangereux avant de changer les piles.                                                      |

## Install the 1756-CFM Module

This chapter describes how to install the 1756-CFM module.

<!-- image -->

<!-- image -->

## Prevent Electrostatic Discharge

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

<!-- image -->

ATTENTION: The ControlLogix system has been agency certified using only the ControlLogix RTBs (catalog numbers 1756TBNH and 1756-TBSH). Any application that requires agency certification of the ControlLogix system using other wiring termination methods may require application specific approval by the certifying agency.

## Power Requirements

## Install the Module

This module receives power from the 1756 chassis power supply and requires two sources of power from the backplane:

- 300 mA at 5.1V DC
- 16 mA at 24V DC

Add this current/power value (1.7 W) to the requirements of all other modules in the chassis to help prevent overloading the power supply.

You can install or remove the module while chassis power is applied.

<!-- image -->

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance that can affect module operation.

WARNING: When you connect or disconnect the removable terminal block (RTB) with field side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

1. Align the circuit board with the top and bottoms chassis guides.
2. Slide the module into the chassis until the module locking tabs click.

<!-- image -->

<!-- image -->

## Key the Removable Terminal Block/Interface Module

Wedge-shaped keying tabs and U-shaped keying bands came with your RTB to help prevent connecting the wrong wires to your module.

Key positions on the module that correspond to unkeyed positions on the RTB. For example, if you key the first position on the module, leave the first position on the RTB unkeyed.

## Key the Module

1. Insert the U-shaped band as shown in this figure.
2. Push the band until it snaps in place.

<!-- image -->

## Key the RTB/IFM

1. Insert the wedge-shaped tab with the rounded edge first, as shown in this figure.
2. Push the tab until it stops.

<!-- image -->

Reposition the tabs to re-key future module applications.

## Wire the Removable Terminal Block

Wire the RTB with a 8 mm (5/16 in.) maximum flat-bladed screwdriver before installing it onto the module.

Shielded cable is required with this module. We recommend using Belden 8761 cable to wire the module. The RTB terminations can accommodate 10.33…2.1 mm2 (22…14 AWG) shielded wire.

<!-- image -->

WARNING: If you connect or disconnect wiring while the field-side power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## Connect Grounded End of the Cable

1. Ground the drain wire, as shown in this figure.

## IMPORTANT

We recommend grounding the drain wire at the field-side. If you cannot ground at the field-side, ground at an earth ground on the chassis as shown.

<!-- image -->

2. Connect the insulated wires to the field-side.

## Connect Ungrounded End of the Cable

1. Cut the foil shield and drain wire back to the cable casing and apply shrink wrap.
2. Connect the insulated wires to the RTB as shown in the next section.

## Connect Wires to the RTBs

There are two types of RTBs available for use with the 1756-CFM module:

- 1756-TBSH Spring Clamp RTB
- 1756-TBNH NEMA Screw RTB

## 1756-TBSH Spring Clamp RTB

1. Strip 11 mm (7/16 in.) maximum length of wire.
2. Insert the screwdriver into the inner hole of the RTB, as shown in this figure.
3. Insert the wire into the open terminal and remove the screwdriver.

<!-- image -->

## 1756-TBNH NEMA Screw RTB

1. Strip 8 mm (5/16 in.) maximum length of wire.
2. Turn the terminal screw counterclockwise.
3. Wrap wire around the terminal.
4. Turn the terminal screw clockwise until it tightens on the wire.

<!-- image -->

## Wire the Module

You can only connect wiring to your module through an RTB or IFM. In this chapter, we show how to wire the 1756-CFM for three applications.

- Standard Flowmeter Wiring Example
- Standard Prover/Detector Wiring Example 1
- Standard Prover/Detector Wiring Example 2
- Standard Output Wiring Example

## Standard Flowmeter Wiring Example

<!-- image -->

- This wiring diagram can be used in applications with 50mV (magnetic pickup), 1.3V (TTL) or 4V (preamp level) thresholds. You must use the programming software to choose the appropriate threshold level for your specific application.
- If separate power sources are used, do not exceed the specified isolation voltage.

## Standard Prover/Detector Wiring Example 1

<!-- image -->

- Detectors #1 and #2 must be wired in parallel.
- Customer VCC can be used to power detectors. In this case, though, the maximum current on the wiring arm must be less than 4A.
- The wiring example above shows a 12-24V DC standard prover connected to the module.

If you use a 5V DC standard prover, make sure the positive wire is connected to the 5V terminal (e.g. Z0 5V DC).

- If separate power sources are used, do not exceed the specified isolation voltage.

## Standard Prover/Detector Wiring Example 2

<!-- image -->

- Customer VCC can be used to power detectors. In this case, though, the maximum current on the wiring arm must be less than 4A.
- The wiring example above shows a 12-24V DC standard prover connected to the module. If you use a 5V DC standard prover, make sure the positive wire is connected to the 5V terminal (e.g. Z0 5V DC).
- If separate power sources are used, do not exceed the specified isolation voltage.

## Standard Output Wiring Example

<!-- image -->

If separate power sources are used, do not exceed the specified isolation voltage.

After completing field-side wiring, secure the wires in the strain relief area with a cable-tie.

## Assemble the Removable Terminal Block and Housing

## Install the Removable Terminal Block on the Module

1. Align the grooves at the bottom of the housing with the side edges of the RTB.
2. Slide the RTB into the housing until it snaps into place.

<!-- image -->

<!-- image -->

WARNING: When you connect or disconnect the removable terminal block (RTB) with field side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Before installing the RTB, verify the following:

- Field-side wiring of the RTB has been completed.
- The RTB housing is snapped into place on the RTB.
- The RTB housing door is closed.
- The locking tab at the top of the module is unlocked.
1. Align the side, top and bottom RTB guides with the side, top and bottom module guides.
2. Press quickly and evenly to seat the RTB on the module until the latches snap into place.

<!-- image -->

## Remove the Removable Terminal Block from the Module

3. Slide the locking tab down to lock the RTB onto the module.

<!-- image -->

<!-- image -->

WARNING: When you connect or disconnect the removable terminal block (RTB) with field side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Before removing the module, you must remove the RTB.

1. Unlock the locking tab at the top of the module.
2. Open the RTB door and pull the RTB off the module, as shown.

<!-- image -->

<!-- image -->

## Remove the Module

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance that can affect module operation.

1. Push in the locking tabs.
2. Pull the module out of the chassis.

<!-- image -->

<!-- image -->

## Notes:

## What This Chapter Contains

## Use This Chapter

## Overview of the Configuration Process

## Configure the 1756-CFM Module

This chapter describes how to use programming software to configure the 1756-CFM module.

You must configure your module upon installation. It does not work with the ladder program until it has been configured.

## IMPORTANT

You can use different versions of the programming software to configure the 1756-CFM module. This chapter shows how to configure the module with Studio 5000 Logix Designer®, version 33.

Other versions of the programming software, for example, RSLogix 5000® software versions, can have different screens. But the tasks and how to complete them are typically the same.

## This chapter is broken into two sections:

- Overview of the Configuration Process - Includes a detailed explanation of how to perform each task mentioned in the overview
- Examples of how to configure your 1756-CFM module for any of these operational modes:
- High-Resolution Frequency mode
- – Totalizer mode using the prover function
- – Totalizer mode using the filler function

This chapter is intended to teach you how to configure the module for basic operation in each of the operational modes.

## IMPORTANT

The examples that are offered in this chapter only list the tags that must be changed for specific operational modes. For a complete listing of configuration, input, and output tags, see Appendix B on page 105 .

When you create a module, module-defined data structures and tags are created in the programming software. The information that is contained in these structures determines your module's behavior.

The owner-controller sends configuration information to the module in one of these ways:

- Controller project goes online - Typically, this is the method in which initial configuration is sent. When the project goes online, a program is downloaded to the controller, and connections are made to all devices that controller owns, including any modules. When a connection is established, the configuration for that particular module is transferred.

<!-- image -->

Change configuration before module

operation begins

- Message instructions - Typically, this method is used after module operation has begun and additional configuration changes are necessary.

IMPORTANT This chapter assumes that you have created a Logix controller in your project.

Figure 4 - Overview of the Configuration Process

<!-- image -->

## Create a New Module

After you have started the programming software and created a controller, you must create a 1756-CFM module.

1. Go offline.
2. Right-click on the ControlLogix® chassis and choose New Module.
3. When the Select Module Type dialog appears, select the 1756-CFM module and click Create.

<!-- image -->

<!-- image -->

4. Choose a Major Revision, and click OK.

<!-- image -->

This step is not required with all versions of the programming software.

<!-- image -->

The New Module dialog box appears.

<!-- image -->

You can take one of the following options:

- Use the default module configuration - For more information, see page 70 .
- Edit module configuration - For more information, see page 71 . The fields are defined as follows:
- -Name - Uniquely identifies the module in the project. This field is required.
- -Slot - Must match the module location in the chassis. By default, the software lists the field based on what other modules are in the chassis at the time of module creation, described on page 67 .
- -Description - Describes the module.
- -Comm Format - Determines the type of communication between the module and the owner-controller. For more information about how to choose a Communication Format, see page 69 .
- Revision - The major firmware revision is fixed based on your choice during initial module creation. The minor revision can be modified.
- Electronic keying - Helps prevent incorrect communication to a module that does not match the type and revision expected. For more information about how to choose an Electronic Keying method, see page 70 .

## Communication Format

The communication format determines what type of data is transferred between the module and its owner-controller. This feature also defines the connection between the controller writing the configuration and the module itself.

describes the communication formats that are available with the 1756-CFM module.

Table 6 - Communication Format Definitions

| Communication Format Description   |                                                                                                                                                                                                                                                                                                                                                            | Notes                                                                                                                                                             |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data                               | Use this format for a controller that you want to own the module and control its configuration data. Only one controller can use the Data communications format when connecting to a module.                                                                                                                                                               | —                                                                                                                                                                 |
| Data - Output Window               | Use this format for a controller that you want to own the module and control its configuration data. With this option, as opposed to the Data option, you can configure specific output On/Off frequencies rather than use fixed frequency limits.                                                                                                         | This option is not available with all versions of the programming software.                                                                                       |
| Listen-only Data                   | Use this format for any controller that you want to listen to the module but not own it. Multiple controllers can use the Listen-only Data communication format when connecting to the module. These controllers do not own the module’s configuration and lose their connection to the module if the owner-controller loses its connection to the module. | When you select a Listen-only Communications Format, only the General and Connection tabs appear when you view a module’s properties in the programming software. |

This screen shows the choices available.

<!-- image -->

IMPORTANT

Once the module is created, the communication format cannot be changed. You must delete and recreate the module in the project.

## Use the Default Configuration

## Electronic Keying

When you create a create a module, you can choose how specific the keying must be when a module is inserted into the module's slot in the chassis.

This screen shows the choices available.

<!-- image -->

For more information, see Electronic Keying on page 22 .

If you want to use the default configuration, name the module and click OK.

For more information on how to download the default configuration information and begin module operation, see page 74 .

<!-- image -->

## Edit the Configuration

Adjust the Requested Packet Interval here.

Inhibit the connection to the module here

If you want a Major Fault on the Controller to occur if there is connection failure with the I/O module, click here

## IMPORTANT: Minimum RPI values:

- 50 ms for one channel in Totalizer mode
- 100 ms for two channels in Totalizer mode
- 5 ms for one channel in High Resolution Frequency mode
- 10 ms for two channels in High Resolution Frequency mode
- 55 ms for one channel in each mode

If you want to edit the default configuration, complete the following steps.

1. Make the desired changes on the New Module dialog box.
2. Check Open Module Properties and click OK.
3. On the next wizard screen, you can change the module's configuration as shown.

<!-- image -->

<!-- image -->

Click here to finish this portion of configuration and move to the Tag Editor, see page 72 .

## IMPORTANT

Two additional wizard screens appear during initial module configuration. The screens are used during online application monitoring but are shown below to give you an accurate description of the screens that appear during initial configuration.

<!-- image -->

<!-- image -->

After you finish the Module Properties screen, you must access the module tags, via the Tag Editor, to make additional configuration changes, see page 72 .

## Access the Tags

When you access tags to change configuration or monitor the I/O data exchange, you have two options:

- Monitor tags - You view tags and change their values.
- Edit tags - You add or delete tags but not change their values.
1. Right-click Controller Tags.
2. Choose Monitor Tags.
3. View tags here.

<!-- image -->

<!-- image -->

## Change Configuration Information at the Tags

Some configurable features are changed on a module-wide basis and some on a point-by-point basis.

## Configurable Features

There are two ways to change the configuration:

- Use a pull-down menu.
- Highlight the value of a particular feature for a particular point and type a value.

## Pull-down Menu

<!-- image -->

2. Highlight the point that must be changed and type a valid new value.

## Highlight Value

<!-- image -->

## Download Configuration Data

After you have changed the configuration data for a module, the change does not actually take effect until you download the new program that contains that information. This downloads the entire program to the controller and overwrites any existing programs.

1. To access the Download option, click the pull-down menu.
2. Click Download.
3. When the Download dialog box appears, read the text and click Download.

<!-- image -->

<!-- image -->

This completes the download process.

## Change Configuration During Module Operation

After the module has begun operation, you can only change configuration by using ladder logic and message instructions.

Follow these steps to change module configuration during operation:

1. Access the data structures through the tag monitor to make specific configuration changes, see page 72 .
2. Use ladder logic and a configuration message instruction to send the configuration changes to the module, see below through page 80 .

## Use Ladder Logic

You must use ladder logic to perform these operations on your module:

- change configuration
- perform run time services

Ladder logic uses message instructions to exchange data between the controller and module. You can access the ladder logic by double-clicking the Main Routine portion of the MainProgram.

<!-- image -->

## Use Message Instructions

Ladder logic uses message instructions to change the module configuration during module operation.

Message instructions maintain the following characteristics:

- Messages use unscheduled portions of system communication bandwidth
- One service is performed per instruction
- Performing module services does not impede module functionality, such as counting incoming pulses

## Process Real-Time Control and Module Services

Because message instructions use unscheduled portions of systems communication bandwidth, the services that are requested of a module are not guaranteed to occur within a specific time period. Although the module response typically occurs in less than a second, there is no specific time interval that reflects this response.

## One Service Performed Per Instruction

Message instructions only cause a module service to be performed once per execution. For example, if a message instruction sends new configuration data to the module, the message instruction must be reexecuted to update send the configuration data in the future.

## Create a New Tag

.

Ladder logic is written in the Main Routine section of the programming software.

1. Access the Main Routine.
2. Right-click Rung 0 and click Add Ladder Element
3. Choose a Message element from the Choose Ladder Element screen and click OK.

<!-- image -->

<!-- image -->

<!-- image -->

4. Create a tag for the message instruction.
- a. Right-click on the question mark.
- b. Click New Tag.
5. Configure the fields on the New Tag dialog box as necesary.

<!-- image -->

## IMPORTANT

We suggest that you name the tag to indicate what module service that the message instruction sends. For example, the message instruction that is shown is used to write configuration.

<!-- image -->

## Enter Message Configuration

After you create a new tag, you must configure the message. Click the ellipsis to access the configuration.

<!-- image -->

Enter message configuration on these screens:

- Configuration Pop-up Screen
- Communications Pop-up Screen
- Tag Pop-up Screen

A description of the purpose and setup of each screen follows.

## Configuration Pop-up Screen

This screen provides information on what module service to perform and where to perform it.

For example, the screen shows the information that is needed to send a configuration message (module service) to a 1756-CFM module (where to perform service).

<!-- image -->

This table contains information that must be entered on the configuration screen to perform the example flowmeter module service:

| Field              | Select                                   |
|--------------------|------------------------------------------|
| Service Code       | 4c                                       |
| Class Name         | 4                                        |
| Instance Name      | 16                                       |
| Source             | Local:1:C (dependent on module location) |
| Number of Elements | 300                                      |
| Destination        | N/A                                      |

## Communications Pop-up Screen

This pop-up screen provides information on the path of the message instruction. For example, the slot number of a 1756-CFM module distinguishes exactly for which module a message is designated. .

<!-- image -->

## Tag Pop-up Screen

This screen provides an opportunity to change some characteristics of the newly created tag. Access this screen to change the attributes of a tag:

- Name
- Description
- Style - Not available on all versions of the programming software.
- Number of consumers - Not available on all versions of the programming software.

<!-- image -->

## IMPORTANT

In some versions of the programming software, the following apply:

- You can change the style and number of consumers on this tab.
- You must add a second Apply rung to the ladder logic to send configuration to the module.

## Configure 1756-CFM Modules in a Remote Chassis

You can communicate with remote 1756-CFM modules over the following networks:

- ControlNet - Via ControlLogix ControlNet® interface modules
- EtherNet/IP - Via ControlLogix EtherNet/IP™ communication modules

## IMPORTANT

For example purposes only, this section shows a ControLogix EtherNet/IP communication module. The same concepts apply if you communicate with a remote 1756-CFM module over a ControlNet network.

You must configure the communications module in the local chassis and the remote chassis before adding new I/O modules to the project.

## Add and Configure Local Communication Module

1. Right-click on the ControlLogix chassis and choose New Module.
2. When the Select Module Type dialog appears, select the EtherNet/IP communication module and click Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

<!-- image -->

3. Configure the ControlLogix EtherNet/IP communication module. For more information on how to configure the ControlLogix EtherNet/IP communication module, see the EtherNet/IP Network Devices User Manual, publication ENET-UM006.

## Add and Configure Remote Communication Module

1. Right-click on Ethernet and choose New Module.

<!-- image -->

2. When the Select Module Type dialog appears, select the new EtherNet/IP communication module and click Create.

<!-- image -->

The New Module dialog box appears.

<!-- image -->

3. Configure the ControlLogix EtherNet/IP communication module. For more information on how to configure the ControlLogix EtherNet/IP communication module, see the EtherNet/IP Network Devices User Manual, publication ENET-UM006.

## Add and Configure Remote 1756-CFM Module

1. Right-click on the remote backplane, that is, 1756 Backplane, and choose New Module.
2. When the Select Module Type dialog appears, select the 1756-CFM module and click Create.

<!-- image -->

<!-- image -->

3. Choose a Major Revision, and click OK.

<!-- image -->

This step is not required with all versions of the programming software.

<!-- image -->

The New Module dialog box appears.

<!-- image -->

4. Configure the 1756-CFM module as described beginning on page 70 .

## IMPORTANT

If you use a ControlNet network to access a remote 1756-CFM module, you must run RSNetWorx™ for ControlNet software for the ownercontroller to establish connections with and send configuration information to the remote flowmeter module.

## Sample Configuration for High Resolution Frequency Mode

High Resolution Frequency mode provides speed control of machinery such as turbines where shutdown on acceleration or speed is required independent of the owner-controller. Speed is calculated without the K-factor but includes the meter factor and CCF for special calculations.

When using this mode, you can calculate resolution by using this equation to calculate resolution.

F

in

(250 x 10

-9

)

T

sample

Resolution =

## Where:

- F in is the input frequency

- T sample is the sample time period

<!-- image -->

Table 7 - Sample Resolutions

| F in      | T sample                       | Resolution   |
|-----------|--------------------------------|--------------|
|           | 60 Hz 0.033 seconds 0.00045 Hz |              |
| 5000 Hz   | 0.020 seconds                  | 0.0625 Hz    |
| 50,000 Hz | 0.050 seconds                  | 0.25 Hz      |

The values that are listed in Table 7 are listed for example purposes. Specific values change according to your application.

This section offers a sample configuration to configure your module for High Resolution Frequency mode. In this configuration, channel 0 is configured and channel 1 is left unused.For a detailed explanation of the features available in this mode, see page 31 .

To configure your module for High Resolution Frequency mode, complete the following.

1. Create a module, see page 67 .
2. Set all communications options, including:
- name
- communication format
- slot number
- minor revision
- electronic keying
- RPI - For this application, the minimum RPI = 5 ms See pages 68 to 71 .
3. Access the module tags via the Tag Editor, see page 72 .

4. Change only the tags listed in Table 8. You can ignore all other tags; they do not affect High Resolution Frequency mode

Table 8 - Tag Changes Required for High Resolution Frequency Mode

| Name                                           |              | Style Data Type Definition                                                                                                                                                                                                                   |   Enter This Value |
|------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.Ch0LowFreqClear                              | Decimal BOOL | Enables the minimum detectable frequency level for Channel 0. Set the bit to 1 to enable it                                                                                                                                                  |              1     |
| C.Operations[0].OperationalMode                | Decimal SINT | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High Resolution Frequency Mode                                                                                                          |              3     |
| C.Operations[1].OperationalMode                | Decimal SINT | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High Resolution Frequency Mode                                                                                                          |              0     |
| C.Operations[0].AccelCalculation               | Decimal SINT | Number of past samples to use to calculate an acceleration value. Sample range is 0...255.                                                                                                                                                   |             50     |
| C.Operations[0].MeterFactor                    | Float REAL   | Calibration Adjust for metering reading that is applied after K-factor correction. Typically, this factor is between 0.8 and 1.2 but the module restricts the value>0.                                                                       |              0     |
| C.Operations[0].FilterResolution Float REAL    |              | Sets resolution of the Speed calculation based on the raw counts 0 = default of 0.00001 0.00001 = resolution of + 1 count of 100,000 raw counts.                                                                                             |              1e-05 |
| C.Operations[0].SampleTime                     | Float REAL   | Sets time for a sample to be taken. (2.0 second maximum sample time for High Resolution Frequency mode and 5.0 second maximum sample time for Totalizer mode)                                                                                |              0.033 |
| C.Operations[0].HighestAllowedFreq             | Float REAL   | User-defined value between MinDetectableFreq and 120,000 When the frequency reaches this level, it sets the Overspeed alarm limit                                                                                                            |           3700     |
| C.Operations[0].AccelAlarmValue                | Float REAL   | Sets Acceleration alarm limit -Maximum acceleration (cycles per second 2 ) <AccelAlarmValue< +Maximum acceleration (cycles per second 2 )                                                                                                    |            100     |
| C.OutputSetup[0].TriggerOn                     | Decimal SINT | Sets when output 0 energizes 0 = No Action 1 = Frequency 2 = Acceleration 3 = Full Flow State (N/A in this mode) 4 = Trickle Flow State (N/A in this mode) 5 = Prover Run State (N/A in this mode) 6 = Prover Range State (N/A in this mode) |              0     |
| C.OutputSetup[0].TieToCounter                  |              | Ties a channel to output 0 0 = No connection 1 = Connect Channel0 to Output0 2 = Connect Channel1 to Ouput0                                                                                                                                  |              0     |
| O.Total[0].CombinedCorrectionFactor Float REAL |              | 0 = Default value of 1.0 Use this value to convert from Hz to RPMs. Results are displayed in Frequency Average only                                                                                                                          |             60     |
| O.Total[0].Overrange                           | Decimal BOOL | Enables the Overrange alarm on output that is connected to channel 1. When the Frequency Average exceeds 100 KHz, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                          |              0     |
| O.Total[0].Overspeed                           | Decimal BOOL | Enables the Overspeed alarm on output that is connected to channel 0. When the Speed exceeds the Highest Allowed Frequency value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                          |              1     |

Table 8 - Tag Changes Required for High Resolution Frequency Mode

| Name                                 |              | Style Data Type Definition                                                                                                                                                                      | Enter This Value   |
|--------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| O.Total[0].Acceleration Decimal BOOL |              | Enables the Acceleration alarm on output that is connected to channel 0. When the absolute acceleration exceeds the Acceleration Alarm value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled | 1                  |
|                                      |              | I.Status[0].FreqAverage Float REAL Displays frequency averaged over the Meter samples on channel 0                                                                                              |                    |
| I.Status[0].Acceleration Float REAL  |              | Displays acceleration on channel 0 as calculated by using AccelCalculation samples                                                                                                              |                    |
| I.Ch0OverrangeAlarm                  | Decimal BOOL | Displays whether overrange alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                   |                    |
| I.Ch1AccelerationAlarm               | Decimal BOOL | Displays whether acceleration alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                |                    |
| I.Ch1OverspeedAlarm                  | Decimal BOOL | Displays whether overspeed alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                   |                    |

5. Use ladder logic and a message instructions to send the new configuration to your module, see page 76 .

In the Totalizer mode prover function, the 1756-CFM module interfaces to a prover and counts pulses using a Flowmeter or positive displacement meter. The module then scales pulse count to engineering units. The module also calculates frequency over a user-defined time period.

When using Totalizer mode (with prover or fill function), you can apply a Kfactor as a function of frequency, as shown.

<!-- image -->

This section offers a sample configuration to configure your module for Totalizer mode prover function. In this configuration, channel 0 is configured and channel 1 is left unused. For a detailed explanation of the features available in this mode, see page 36 .

## Sample Configuration for Totalizer Mode Prover Function

Follow these steps to configure your module for Totalizer mode prover function.

1. Create a module, see page 67 .
2. Set all communications options, including the following:
- Name
- Communication format
- Slot number
- Minor revision
- Electronic keying
- RPI - For this application, the minimum RPI = 50 ms See pages 68 to 71 .
3. Access the module tags via the Tag Editor, see page 72 .
4. Change only the tags listed in Table 9. Ignore all other tags; they do not affect Totalizer mode prover function.

Table 9 - Tag Changes Required for Totalizer Mode Using Prover Function

| Name                                        |              | Style Data Type Definition                                                                                                                                                                                                                                                 |   Enter This Value |
|---------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.ProgToFaultEn                             | Decimal BOOL | Sets outputs to selected Fault state when the owner controller is in Program mode. 0 = outputs use Program mode setting 1 = outputs use fault mode settings                                                                                                                                                                                                                                                                            |              0     |
| C.Operations[0].FilterControl (1)           | Decimal SINT | bit 0 = 1 - apply filter to F0 bit 1 = 1 - apply filter to G0 bit 2 = 1 - apply 1second debounce to G0                                                                                                                                                                     |              0     |
| C.Operations[0].MeterSamples                | Decimal SINT |                                                                                                                                                                                                                                                                            |             50     |
| C.Operations[0].ThresholdControl            | Decimal SINT | Sets flowmeter input threshold control 0 = 50 mV threshold (magnetic pickup) 1 = 1.3V threshold (TTL) 2 = 4.0V threshold (PreAmp)                                                                                                                                          |              0     |
| C.Operations[0].CalculationType             | Decimal SINT | Sets calculation type 0 = Counts/K-factor x MeterFactor correction x CCF 1 = Counts/K-factor x MeterFactor correction x AGA 7 compensation or CCF if CCF is not equal to 0.0                                                                                               |              0     |
| C.Operations[0].AccelCalculation            | Decimal SINT | Number of past samples to use to calculate an acceleration value. Sample range is 0...255.                                                                                                                                                                                 |             50     |
| C.Operations[0].MinDetectableFreq           | Float REAL   | User-defined value from 0 - 120,000. Sets FreqAverage, FreqPeriod, Speed, GrossRate, and NetRate reading to 0 when calculated value is less than value entered. GrossVolume, and NetVolume do not increment below this value even though TotalCounts increments over time. |              5     |
| C.Operations[0].HighestAllowedFreq          | Float REAL   | User-defined value between MinDetectableFreq and 120,000 When the frequency reaches this level, it sets the overspeed alarm limit                                                                                                                                          |           3700     |
| C.Operations[0].AccelAlarmValue             | Float REAL   | Sets Acceleration alarm limit -Maximum acceleration (cycles per second 2 ) <AccelAlarmValue< +Maximum acceleration (cycles per second 2 )                                                                                                                                  |            100     |
| C.Operations[0].MeterFactor                 | Float REAL   | Calibration Adjust for metering reading that is applied after K-factor correction. Typically, this factor is between 0.8 and 1.2 but the module restricts the value>0.                                                                                                     |              1     |
| C.Operations[0].FilterResolution Float REAL |              | Sets resolution of the Speed calculation based on the raw counts 0 = default of 0.00001 0.00001 = resolution of + 1 count of 100,000 raw counts.                                                                                                                           |              0.166 |

Table 9 - Tag Changes Required for Totalizer Mode Using Prover Function

| Name                                           | Style Data Type Definition   |                                                                                                                                                                                                               |   Enter This Value |
|------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.Operations[0].SampleTime                     | Float REAL                   | Sets time for a sample to be taken. (2.0 second maximum sample time for High Resolution Frequency mode and 5.0 seconds for Totalizer mode)                                                                    |                0.5 |
| C.Operations[0].kFactStruct.kFactorForChan[0]  | Float REAL                   | K-factor 0 for Channel 0 when frequency is < FreqAtKFactor[1]                                                                                                                                                 |              600   |
| C.Operations[0].kFactStruct.kFactorForChan[1]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [1]                                                                                                                            |              600   |
| C.Operations[0].kFactStruct.kFactorForChan[2]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [2]                                                                                                                            |              550   |
| C.Operations[0].kFactStruct.kFactorForChan[3]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [3]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[4]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [4]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[5]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [5]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[6]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [6]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[7]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [7]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[8]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [8]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[9]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [9]                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[10] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [10]                                                                                                                           |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[11] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [11]                                                                                                                           |                0   |
| C.Operations[0].kFactStruct.kFactorForChan[12] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [12]                                                                                                                           |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[0]   | Float REAL                   |                                                                                                                                                                                                               |              100   |
| C.Operations[0].kFactStruct.FreqAtKFactor[1]   |                              | Float REAL Freq[1] for KFactor [1]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[2]   |                              | Float REAL Freq[2] for KFactor [2]                                                                                                                                                                            |              500   |
| C.Operations[0].kFactStruct.FreqAtKFactor[3]   |                              | Float REAL Freq[3] for KFactor [3]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[4]   |                              | Float REAL Freq[4] for KFactor [4]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[5]   |                              | Float REAL Freq[5] for KFactor [5]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[6]   |                              | Float REAL Freq[6] for KFactor [6]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[7]   |                              | Float REAL Freq[7] for KFactor [7]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[8]   |                              | Float REAL Freq[8] for KFactor [8]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[9]   |                              | Float REAL Freq[9] for KFactor [9]                                                                                                                                                                            |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[10]  |                              | Float REAL Freq[10] for KFactor [10]                                                                                                                                                                          |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[11]  |                              | Float REAL Freq[11] for KFactor [11]                                                                                                                                                                          |                0   |
| C.Operations[0].kFactStruct.FreqAtKFactor[12]  |                              | Float REAL Freq[12] for KFactor [12]                                                                                                                                                                          |                0   |
| C.OutputSetup[0].FaultMode                     | Decimal SINT                 | Sets the state of output 0 when communications are lost with the owner-controller in Fault Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Fault Mode 2 = Set Output 0 to ON when in Fault Mode |                1   |

Table 9 - Tag Changes Required for Totalizer Mode Using Prover Function

| Name                              |              | Style Data Type Definition                                                                                                                                                                                                                       |   Enter This Value |
|-----------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.OutputSetup[0].ProgMode         | Decimal SINT | Sets the state of output 0 when communications are lost with the owner-controller in Program Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Program Mode 2 = Set Output 0 to ON when in Program Mode                              |                  0 |
| C.OutputSetup[0].DynamicError     | Decimal SINT | Sets the state of output 0 when a dynamic error occurs 0 = Continue operation 1 = Reset Output 0 to OFF on Error 2 = Set Output 0 to ON on Error                                                                                                 |                  0 |
| C.OutputSetup[0].TriggerOn        | Decimal SINT | Sets when output 0 energizes 0 = No Action 1 = Frequency 2 = Acceleration 3 = Full Flow State (N/A in this mode) 4 = Trickle Flow State (N/A in this mode) 5 = Prover Run State 6 = Prover Range State                                           |                  0 |
| C.OutputSetup[0].TieToCounter     |              | Ties a channel to output 0 0 = No connection 1 = Connect Channel0 to Output0 2 = Connect Channel1 to Ouput0                                                                                                                                      |                  0 |
| C.Ch0ProverDirection              | Decimal BOOL | Defines the direction of a prover that is connected to Channel 0. 0 = unidirectional prover 1 = bidirectional prover                                                                                                                             |                  0 |
| C.Ch0LowFreqClear                 | Decimal BOOL | Enables the minimum detectable frequency level for Channel 0. Set the bit to 1 to enable it                                                                                                                                                      |                  1 |
| C.Operations[0].OperationalMode   | Decimal SINT | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High Resolution Frequency Mode                                                                                                              |                  2 |
| O.OutputControl[0].0              | Decimal BOOL | Manually sets the operation of outputs that are connected to channel 0. 0 = Module operation of outputs 1 = Override Output0 to 0 2 = Override Output0 to 1                                                                                      |                  0 |
| O.Total[0].ProverEnable           | Decimal BOOL | Enables the prover operation on output that is connected to channel 0. Once this bit is enabled, the module waits for output Z0 to energize before beginning prover operations. 0 = Prover operation is disabled 1 = Prover operation is enabled |                  0 |
| O.Total[0].Overrange Decimal BOOL |              | Enables the Overrange alarm on output that is connected to channel 0. When the Frequency Period exceeds 100 KHz, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                               |                  0 |
| O.Total[0].Overflow Decimal BOOL  |              | Enables the Overflow alarm on output that is connected to channel 0. When the Total Counts exceeds the Roll Over value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                        |                  0 |
| O.Total[0].Overspeed Decimal BOOL |              | Enables the Overspeed alarm on output that is connected to channel 0. When the Speed exceeds the Highest Allowed Frequency value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                              |                  1 |

Table 9 - Tag Changes Required for Totalizer Mode Using Prover Function

| Name                     |              | Style Data Type Definition                                                                                                                                                                                                                                                                         | Enter This Value   |
|--------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| O.Total[0].Acceleration  | Decimal BOOL | Enables the Acceleration alarm on output that is connected to channel 0. When the absolute acceleration exceeds the Acceleration Alarm value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                    | 1                  |
| I.Status[0].ProverState  | Decimal SINT | Displays status of the prover operation on channel 0 0 = Prover Not Active 1 = Prover waiting for first start 2 = Prover waiting for first stop 3 = Prover waiting for second start 4 = Prover waiting for second stop 5 = Prover Complete                                                         |                    |
| I.Status[0].TotalCounts  | Decimal DINT | Displays actual pulses that are counted by the counter that is connected to the channel 0                                                                                                                                                                                                          |                    |
| I.Status[0].FreqAverage  | Float REAL   | Displays frequency averaged over the Meter samples on channel 0                                                                                                                                                                                                                                    |                    |
| I.Status[0].FreqPeriod   |              | Float REAL Displays frequency using sample time on channel 0                                                                                                                                                                                                                                       |                    |
| I.Status[0].Speed        |              | Float REAL Displays frequency using filter resolution on channel 0                                                                                                                                                                                                                                 |                    |
| I.Status[0].Acceleration | Float REAL   | Displays acceleration on channel 0 as calculated by using AccelCalculation samples                                                                                                                                                                                                                 |                    |
| I.Status[0].GrossVolume  | Float REAL   | Total Counts during each Sample/K-factor x Meter Factor as occurs on channel 0                                                                                                                                                                                                                 |                    |
| I.Status[0].NetVolume    | Float REAL   | Total Counts during each Sample/K-factor x MeterFactor x CCF) as occurs on channel 0                                                                                                                                                                                                           |                    |
| I.Status[0].GrossRate    | Float REAL   | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor as occurs on channel 0                                                                                                                                                                                                  |                    |
| I.Status[0].NetRate      | Float REAL   | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor x CCF as occurs on channel 0                                                                                                                                                                                            |                    |
| I.Status[0].ProverTotal  | Float REAL   | Corrected/compensated volume received on Channel 0 during prover cycle. Prover total resets when the ProverEnable transitions from 0 to 1. Prover total concurrently accumulates with net volume, and must be saved if subtracted from the NetVolume for single and multiple prover verifications. |                    |
| I.Ch0AccelerationAlarm   | Decimal BOOL | Displays whether acceleration alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                                                                                                                   |                    |
| I.Ch0OverspeedAlarm      | Decimal BOOL | Displays whether overspeed alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                                                                                                                      |                    |
| I.Ch0OverrangeAlarm      | Decimal BOOL | Displays whether overrange alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                                                                                                                      |                    |
| I.Ch0OverflowAlarm       | Decimal BOOL | Displays whether overflow alarm was set on channel 0 0 = alarm was not set 1 = alarm was set                                                                                                                                                                                                       |                    |

5. Use ladder logic and a message instructions to send the new configuration to your module, see page 76 .

## Sample Configuration for Totalizer Mode Filler Function

In the Totalizer mode filler function, the 1756-CFM module interfaces to a prover and counts pulses using a Flowmeter or positive displacement meter. The module then scales pulse count to engineering units. The module also interpolates the K-Factors between frequencies 1…12.

When using Totalizer mode (with prover or fill function), you can apply a Kfactor as a function of frequency.

<!-- image -->

This section offers a sample configuration to configure your module for Totalizer mode prover function. In this configuration, channel 0 is configured and channel 1 is left unused. For a detailed explanation of the features available in this mode, see page 44 .

Follow these steps to configure your module for Totalizer mode filler function.

1. Create a module, see page 67 .
2. Set all communications options, including:
- Name
- Communication format
- Slot number
- Minor revision
- Electronic keying
- RPI - For this application, the minimum RPI = 5 ms .

See pages 68 to 71

3. Access the module tags via the Tag Editor, see page 72 .
4. Change only the tags listed in Table 10. Ignore all other tags; they do not affect Totalizer mode using the prover function.

Table 10 - Tag Changes Required for Totalizer Mode Using Filler Function

| Name                                          |              | Style Data Type Definition                                                                                                                                                   | Enter This Value   |
|-----------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.ProgToFaultEn                               | Decimal BOOL | Sets outputs to selected Fault state when the owner controller is in Program mode. 0 = outputs use Program mode setting 1 = outputs use fault mode settings                                                                                                                                                                              | 0                  |
| C.Operations[0].FilterControl (1)             | Decimal SINT | bit 0 = 1 - apply filter to F0 bit 1 = 1 - apply filter to G0 bit 2 = 1 - apply 1second debounce to G0                                                                       | 0                  |
|                                               |              | C.Operations[0].MeterSamples Decimal SINT 50                                                                                                                                 |                    |
| C.Operations[0].ThresholdControl Decimal SINT |              | Sets flowmeter input threshold control 0 = 50 mV threshold (magnetic pickup) 1 = 1.3V threshold (TTL) 2 = 4.0V threshold (PreAmp)                                            | 0                  |
| C.Operations[0].CalculationType Decimal SINT  |              | Sets calculation type 0 = Counts/K-factor x MeterFactor correction x CCF 1 = Counts/K-factor x MeterFactor correction x AGA 7 compensation or CCF if CCF is not equal to 0.0 | 0                  |
| C.Operations[0].AccelCalculation Decimal SINT |              | Number of past samples to use to calculate an acceleration value. Sample range is 0...255.                                                                                   | 50                 |

Table 10 - Tag Changes Required for Totalizer Mode Using Filler Function

| Name                                                     | Style Data Type Definition   |                                                                                                                                                                                                                                                                            | Enter This Value   |
|----------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.Operations[0].MinDetectableFreq                        | Float REAL                   | User-defined value from 0 - 120,000. Sets FreqAverage, FreqPeriod, Speed, GrossRate, and NetRate reading to 0 when calculated value is less than value entered. GrossVolume, and NetVolume do not increment below this value even though TotalCounts increments over time. | 5                  |
| C.Operations[0].HighestAllowedFreq                       | Float REAL                   | User-defined value between MinDetectableFreq and 120,000 When the frequency reaches this level, it sets the Overspeed alarm limit                                                                                                                                          | 3700               |
| C.Operations[0].AccelAlarmValue                          | Float REAL                   | Sets Acceleration alarm limit -Maximum acceleration (cycles per second 2 ) <AccelAlarmValue< +Maximum acceleration (cycles per second 2 )                                                                                                                                  | 100                |
| C.Operations[0].MeterFactor                              | Float REAL                   | Calibration Adjust for metering reading that is applied after K-factor correction. Typically, this factor is between 0.8 and 1.2 but the module restricts the value>0.                                                                                                     |                    |
| C.Operations[0].FilterResolution                         | Float REAL                   | Sets resolution of the Speed calculation based on the raw counts 0 = default of 0.00001 0.00001 = resolution of + 1 count of 100,000 raw counts.                                                                                                                           | 0.166              |
| C.Operations[0].SampleTime Float REAL                    |                              | Sets time for a sample to be taken. (2.0 second maximum sample time for High Resolution Frequency mode and 5.0 seconds for Totalizer mode)                                                                                                                                 | 0.5                |
| C.Operations[0].kFactStruct.kFactorForChan[0] Float REAL |                              | K-factor 0 for Channel 0 when frequency is < FreqAtKFactor[1]                                                                                                                                                                                                              | 600.0              |
| C.Operations[0].kFactStruct.kFactorForChan[1]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [1]                                                                                                                                                                                         | 600.0              |
| C.Operations[0].kFactStruct.kFactorForChan[2]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [2]                                                                                                                                                                                         | 550.0              |
| C.Operations[0].kFactStruct.kFactorForChan[3]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [3]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[4]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [4]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[5]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [5]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[6]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [6]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[7]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [7]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[8]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [8]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[9]            | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [9]                                                                                                                                                                                         | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[10]           | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [10]                                                                                                                                                                                        | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[11]           | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [11]                                                                                                                                                                                        | 0.0                |
| C.Operations[0].kFactStruct.kFactorForChan[12]           | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [12]                                                                                                                                                                                        | 0.0                |
| C.Operations[0].kFactStruct.FreqAtKFactor[0]             | Float REAL                   |                                                                                                                                                                                                                                                                            | 0.0                |
| C.Operations[0].kFactStruct.FreqAtKFactor[1]             |                              | Float REAL Freq[1] for KFactor [1]                                                                                                                                                                                                                                         | 100.0              |
| C.Operations[0].kFactStruct.FreqAtKFactor[2]             |                              | Float REAL Freq[2] for KFactor [2]                                                                                                                                                                                                                                         | 500.0              |
| C.Operations[0].kFactStruct.FreqAtKFactor[3]             |                              | Float REAL Freq[3] for KFactor [3]                                                                                                                                                                                                                                         | 0.0                |

Table 10 - Tag Changes Required for Totalizer Mode Using Filler Function

| Name                                          |              | Style Data Type Definition                                                                                                                                                                                          |   Enter This Value |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| C.Operations[0].kFactStruct.FreqAtKFactor[4]  |              | Float REAL Freq[4] for KFactor [4]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[5]  |              | Float REAL Freq[5] for KFactor [5]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[6]  |              | Float REAL Freq[6] for KFactor [6]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[7]  |              | Float REAL Freq[7] for KFactor [7]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[8]  |              | Float REAL Freq[8] for KFactor [8]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[9]  |              | Float REAL Freq[9] for KFactor [9]                                                                                                                                                                                  |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[10] |              | Float REAL Freq[10] for KFactor [10]                                                                                                                                                                                |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[11] |              | Float REAL Freq[11] for KFactor [11]                                                                                                                                                                                |                  0 |
| C.Operations[0].kFactStruct.FreqAtKFactor[12] |              | Float REAL Freq[12] for KFactor [12]                                                                                                                                                                                |                  0 |
| C.OutputSetup[0].FaultMode                    | Decimal SINT | Sets the state of output 0 when communications are lost with the owner-controller in Fault Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Fault Mode 2 = Set Output 0 to ON when in Fault Mode       |                  1 |
| C.OutputSetup[0].ProgMode                     | Decimal SINT | Sets the state of output 0 when communications are lost with the owner-controller in Program Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Program Mode 2 = Set Output 0 to ON when in Program Mode |                  0 |
| C.OutputSetup[0].DynamicError                 | Decimal SINT | Sets the state of output 0 when a dynamic error occurs 0 = Continue operation 1 = Reset Output 0 to OFF on Error 2 = Set Output 0 to ON on Error                                                                    |                  0 |
| C.OutputSetup[0].TriggerOn                    | Decimal SINT | Sets when output 0 energizes 0 = No Action 1 = Frequency 2 = Acceleration 3 = Full Flow State 4 = Trickle Flow State 5 = Prover Run State (N/A in this mode) 6 = Prover Range State (N/A in this mode)              |                  0 |
| C.OutputSetup[0].TieToCounter                 |              | Ties a channel to output 0 0 = No connection 1 = Connect Channel0 to Output0 2 = Connect Channel1 to Ouput0                                                                                                         |                  0 |
| C.Operations[0].OperationalMode               | Decimal SINT | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High Resolution Frequency Mode                                                                                 |                  1 |
| C.Ch0LowFreqClear                             | Decimal BOOL | Enables the minimum detectable frequency level for Channel 0. Set the bit to 1 to enable it                                                                                                                         |                  1 |
| C.Ch0PreTrigger                               | Decimal BOOL | Enables the PreTrigger on Channel 0 for full flow. Set the bit to 1 to enable it                                                                                                                                    |                  1 |
| C.Operations[0].FillMode                      | Decimal SINT | Sets the Trickle mode to complete on fill total target or time. 0 = Fill total target (Engineering units) 1 = Time (seconds)                                                                                        |                  0 |
| O.OutputControl[0].0                          | Decimal BOOL | Manually sets the operation of outputs that are connected to channel 0. 0 = Module operation of outputs 1 = Override Output0 to 0 2 = Override Output0 to 1                                                         |                  0 |

Table 10 - Tag Changes Required for Totalizer Mode Using Filler Function

| Name                           |              | Style Data Type Definition                                                                                                                                                                                                                                                                                                                                   | Enter This Value   |
|--------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| O.Total[0].FillEnable          | Decimal BOOL | Enables the filling operation on output that is connected to channel 0. 0 = Fill operation is disabled 1 = Fill operation is enabled.                                                                                                                                                                                                                        | 0                  |
| O.Total[0].FillStart           | Decimal BOOL | Begins filling operation when Fill Enable is enabled on output that is connected to channel 0. 0 = Do not begin filling 1 = Begin filling                                                                                                                                                                                                                    | 0                  |
| O.Total[0].FillHold            | Decimal BOOL | Holds/pauses filling operation on output that is connected to channel 0 0 = Continue filling operation 1 = Hold/pause filling operation                                                                                                                                                                                                                      | 0                  |
| O.Total[0].FillTotalTarget     | Float REAL   | Target for Fill Complete, except when Fill Transition is greater than this value.                                                                                                                                                                                                                                                                            | 100                |
| O.Total[0].FillTransition      | Float REAL   | When fill cycle is started, trickle flow is initiated when the Fill Total is equal to or greater than this value. Full flow is initiated when the Fill Total is less than this value.                                                                                                                                                                        | 75                 |
| O.Total[0].FillTransitionTimer | Float REAL   | When timed trickle flow is selected, the status remains ON for this time during this state. The value must be changed before entering the trickle flow state.                                                                                                                                                                                                | 1.0                |
| O.Total[0].Overrange           | Decimal BOOL | Enables the Overrange alarm on output that is connected to channel 0. When the Frequency Period exceeds 100 KHz, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                                                           | 0                  |
| O.Total[0].Overflow            | Decimal BOOL | Enables the Overflow alarm on output that is connected to channel 0. When the Total Counts exceeds the Roll Over value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                                                    | 0                  |
| O.Total[0].Overspeed           | Decimal BOOL | Enables the Overspeed alarm on output that is connected to channel 0. When the Speed exceeds the Highest Allowed Frequency value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                                          | 1                  |
| O.Total[0].Acceleration        | Decimal BOOL | Enables the Acceleration alarm on output that is connected to channel 0. When the absolute acceleration exceeds the Acceleration Alarm value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                              | 1                  |
| I.Status[0].FillState          | Decimal SINT | Displays current state of module for channel 0. These states are possible: 0 = Filler not active 1 = Filler Enabled only, waiting for start 2 = Timed Trickle Flow complete, not filled 3 = Full Flow (Fill mode =1) 4 = Timed Trickle Flow (Fill mode =1) 5 = Full Flow (Fill mode =0) 6 = Fill Total Target Trickle Flow (Fill mode = 0) 7 = Fill complete |                    |
| I.Status[0].TotalCounts        | Decimal DINT | Displays actual pulses that are counted by the counter that is connected to the channel 0                                                                                                                                                                                                                                                                    |                    |
| I.Status[0].FillTotal          | Float REAL   | Same calculation as Net Volume during fill cycle.                                                                                                                                                                                                                                                                                                            |                    |
| I.Status[0].GrossVolume        | Float REAL   | Total Counts during each Sample/K-factor x Meter Factor as occurs on channel 0                                                                                                                                                                                                                                                                           |                    |
| I.Status[0].NetVolume          | Float REAL   | Total Counts during each Sample/K-factor x MeterFactor x CCF) as occurs on channel 0                                                                                                                                                                                                                                                                     |                    |
| I.Status[0].GrossRate          | Float REAL   | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor as occurs on channel 0                                                                                                                                                                                                                                                            |                    |

Table 10 - Tag Changes Required for Totalizer Mode Using Filler Function

| Name                   |              | Style Data Type Definition                                                                              | Enter This Value   |
|------------------------|--------------|---------------------------------------------------------------------------------------------------------|--------------------|
| I.Status[0].NetRate    | Float REAL   | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor x CCF as occurs on channel 0 |                    |
| I.Ch0AccelerationAlarm | Decimal BOOL | Displays whether acceleration alarm was set on channel 0 0 = alarm was not set 1 = alarm was set        |                    |
| I.Ch0OverspeedAlarm    | Decimal BOOL | Displays whether overspeed alarm was set on channel 0 0 = alarm was not set 1 = alarm was set           |                    |
| I.Ch0OverrangeAlarm    | Decimal BOOL | Displays whether overrange alarm was set on channel 0 0 = alarm was not set 1 = alarm was set           |                    |
| I.Ch0OverflowAlarm     | Decimal BOOL | Displays whether overflow alarm was set on channel 0 0 = alarm was not set 1 = alarm was set            |                    |

5. Use ladder logic and a message instructions to send the new configuration to your module, see page 76 .

You can use the C.Operations[0].FilterControl and C.Operations[1].FilterControl tags to configure the filters digitally. The filter applies to only F0/Z0 or F1/Z1 depending on which config byte they are referencing.

Table 11 - Digital Filter Configuration

| C.Operations[0].FilterControl affects F0/Z0 C.Operations[1].FilterControl affects F1/Z1   | Byte   |
|-------------------------------------------------------------------------------------------|--------|
| 50 Hz filter for F                                                                        | 0x01   |
| 50 Hz filter for Z                                                                        | 0x02   |
| 50 Hz filter for F and Z                                                                  | 0x03   |
| 1 s debounce filter for Z                                                                 | 0x04   |
| 50 Hz filter for Z, 1 s debounce filter for Z                                             | 0x06   |
| 50 Hz filter for F, Z, and 1 s debounce filter for Z                                      | 0x07   |
| 500 Hz filter for F                                                                       | 0x08   |
| 5 kHz filter for F                                                                        | 0x09   |
| 50 kHz filter for F                                                                       | 0x0A   |
| 500 Hz filter for Z                                                                       | 0x0B   |
| 5 kHz filter for Z                                                                        | 0x0C   |
| 50 kHz filter for Z                                                                       | 0x0D   |
| 500 Hz filter for F and Z                                                                 | 0x0E   |
| 5 kHz filter for F and Z                                                                  | 0x0F   |
| 50 kHz filter for F and Z                                                                 | 0x10   |
| 50 Hz filter for F and 500 Hz filter for Z                                                | 0x11   |
| 50 Hz filter for F and 5 kHz filter for Z                                                 | 0x12   |
| 50 Hz filter for F and 50 kHz filter for Z                                                | 0x13   |
| 500 Hz filter for F and 50 Hz filter for Z                                                | 0x14   |
| 500 Hz filter for F and 5 kHz filter for Z                                                | 0x15   |

## Digital Filter

Table 11 - Digital Filter Configuration

| C.Operations[0].FilterControl affects F0/Z0 C.Operations[1].FilterControl affects F1/Z1   | Byte   |
|-------------------------------------------------------------------------------------------|--------|
| 500 Hz filter for F and 50 kHz filter for Z                                               | 0x16   |
| 5 kHz filter for F and 50 Hz filter for Z                                                 | 0x17   |
| 5 kHz filter for F and 500 Hz filter for Z                                                | 0x18   |
| 5 kHz filter for F and 50 kHz filter for Z                                                | 0x19   |
| 50 kHz filter for F and 50 Hz filter for Z                                                | 0x1A   |
| 50 kHz filter for F and 500 Hz filter for Z                                               | 0x1B   |
| 50 kHz filter for F and 5 kHz filter for Z                                                | 0x1C   |
| 500 Hz filter for F, Z, and 1 s debounce filter for Z                                     | 0x1D   |
| 5 kHz filter for F, Z, and 1 s debounce filter for Z                                      | 0x1E   |
| 50 kHz filter for F, Z, and 1 s debounce filter for Z                                     | 0x1F   |
| 500 Hz filter for Z and 1 s debounce filter for Z                                         | 0x20   |
| 5 kHz filter for Z and 1 s debounce filter for Z                                          | 0x21   |
| 50 kHz filter for Z and 1 s debounce filter for Z                                         | 0x22   |
| 50 Hz filter for F, 500 Hz filter for Z and 1 s debounce filter for Z                     | 0x23   |
| 50 Hz filter for F, 5 kHz filter for Z and 1 s debounce filter for Z                      | 0x24   |
| 50 Hz filter for F, 50 kHz filter for Z and 1 s debounce filter for Z                     | 0x25   |
| 500 Hz filter for F, 50 Hz filter for Z and 1 s debounce filter for Z                     | 0x26   |
| 500 Hz filter for F, 5 kHz filter for Z and 1 s debounce filter for Z                     | 0x27   |
| 500 Hz filter for F, 50 kHz filter for Z and 1 s debounce filter for Z                    | 0x28   |
| 5 kHz filter for F, 50 Hz filter for Z and 1 s debounce filter for Z                      | 0x29   |
| 5 kHz filter for F, 500 Hz filter for Z and 1 s debounce filter for Z                     | 0x2A   |
| 5 kHz filter for F, 50 kHz filter for Z and 1 s debounce filter for Z                     | 0x2B   |
| 50 kHz filter for F, 50 Hz filter for Z and 1 s debounce filter for Z                     | 0x2C   |
| 50 kHz filter for F, 500 Hz filter for Z and 1 s debounce filter for Z                    | 0x2D   |
| 50 kHz filter for F, 5 kHz filter for Z and 1 s debounce filter for Z                     | 0x2E   |

## IMPORTANTIMPORTANT

To avoid disabling filtering, set the filter byte to only those selections that are listed in Table 11 .

Before creating a module, make sure you complete these procedures in the programming software:

- Create a controller project.
- If you plan to add the I/O module to a remote chassis, add ControlNet or EtherNet/IP communication modules to both the local and remote chassis in the I/O Configuration tree.
- For more information on ControlLogix ControlNet modules, see ControlNet Network Configuration User Manual, publication CNET-UM001 .
- For more information on ControlLogix EtherNet/IP modules, see EtherNet/IP Network Devices User Manual, publication ENET-UM006 .

Complete the following steps to a local or remote 1756-CFM module.

1. Go offline.
2. To add an I/O module to a local chassis, right-click the ControlLogix chassis and choose New Module.

or

To add an I/O module to a remote chassis, right-click the remote communication module, and choose New Module.

<!-- image -->

## Notes:

## What This Appendix Contains

## Use the Status Indicators

Table 12 - 1756-CFM Module Status Indicators

| Status Indicator This Display   |                      | Means                                                                                                             | Take This Action                                                                        |
|---------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| OK                              | Steady green light   | The inputs are being multicast and in normal operating state.                                                     | None                                                                                    |
| OK                              | Flashing green light | The module has passed internal diagnostics but is not actively controlled.                                        | Configure the module.                                                                   |
| OK                              |                      | Flashing red light Previously established communication has timed out. Check controller and chassis communication |                                                                                         |
| OK                              |                      | Steady red light The module must be replaced.                                                                     | Replace the module.                                                                     |
| Input (F, Z)                    | Off                  | The input is turned off. The input is not in use. A wire is disconnected.                                         | If you must use the input, check wiring connections                                     |
| Input (F, Z)                    | Steady yellow        | The input is in normal operating state.                                                                           | None                                                                                    |
| Output (0, 1)                   | Off                  | The output is turned off. The output is not in use.                                                               | If you must use the output, check wiring connections and your ladder logic application. |
| Output (0, 1)                   | Steady yellow        | The output is in normal operating state.                                                                          | None                                                                                    |

## Troubleshoot the 1756-CFM Module

This appendix describes how to troubleshoot the module.

The module offers status indicators to show the health of your module. The indicators show individual I/O status (green) for each point and a bi-colored indicator for module "OK" (red/green).

## Series A Module

<!-- image -->

## Series B and Later Modules

<!-- image -->

During power-up, an indicator test is performed and the following occurs:

- The "OK" indicator turns red for 1 second.
- If the module passes the self-test, the "OK" indicator turns to flashing green.

<!-- image -->

## Use Programming Software to Troubleshoot Your Module

The programming software alerts you to fault conditions. You are alerted in one of the following ways:

- Warning signal on the main screen next to the module - This occurs when the connection to the module is broken
- Fault message in a screen's status line
- Notification in the Tag Editor - General module faults are also reported in the Tag Editor. Diagnostic faults are only reported in the Tag Editor
- Status on the Module Info Page

The screens below display fault notification in the programming software.

## Warning signal on main screen

<!-- image -->

## Determining Fault Type

When you are monitoring a module's configuration properties in the programming software and receive a Communications fault message, the Connection page lists the type of fault.

<!-- image -->

## Use Error Codes

## Errors are displayed

- on the Connection tab of the Module Properties section in the programming software

and

- in the .EXERR field of the message variable when your reconfigure the module.

Table 13 - Configurable Flowmeter Configuration Error Codes

| Error Code Definition   |                              |
|-------------------------|------------------------------|
| 1                       | BAD_OPERATIONAL_MODE         |
|                         | 2 BAD _ FILTER _ VALUE       |
| 3                       | BAD_THRESHOLD_VALUE          |
|                         | 4 BAD _ CALCULATION _ TYPE   |
| 5                       | BAD_FILL_MODE_VALUE          |
| 6                       | BAD_MINIMUM_FREQ_VALUE       |
| 7                       | BAD_HIGHEST_ALLOWED_FREQ     |
| 8                       | BAD_ACCELERATION_ALARM_VALUE |
| 9                       | BAD_METER_FACTOR_VALUE       |
| a                       | BAD_FILTER_RESOLUTION_VALUE  |
| b                       | BAD_SAMPLE_TIME_VALUE        |
|                         | c BAD _ KFACTOR _ VALUE      |
| d                       | BAD_KFACTOR_FREQ_VALUE       |
| e                       | BAD_FAULT_MODE_VALUE         |
|                         | f BAD _ PROGMODE _ VALUE     |

Table 14 - Configurable Flowmeter Consumer Error Codes

|   Error Code Definition |                                 |
|-------------------------|---------------------------------|
|                      10 | BAD_DYNAMIC_ERROR_VALUE         |
|                      11 | BAD_TRIGGER_ON_VALUE            |
|                      12 | BAD_COUNTER_TIE_VALUE           |
|                      19 | BAD_CCF_VALUE                   |
|                      20 | BAD_BASE_TEMPERATURE_VALUE      |
|                      21 | BAD_FLOWINGTEMP_VALUE           |
|                      22 | BAD_ATMOSPHERICPRESSURE_VALUE   |
|                      23 | BAD_STATICGAUGEPRESSURE_VALUE   |
|                      24 | BAD_BASE_PRESSURE_VALUE         |
|                      25 | BAD_BASECOMPRESSIBILITY_VALUE   |
|                      26 | BAD_FLOWINGCOMPRESS_VALUE       |
|                      27 | BAD_FILL_TOTAL_TARGET_VALUE     |
|                      28 | BAD_FILL_TRANSITION_VALUE       |
|                      29 | BAD_FILL_TRANSITION_TIMER_VALUE |
|                      30 | OUTPUT_CONTROL_ERROR            |

## Software Configuration Tags

This appendix lists the following categories of 1756-CFM data structures:

- Configuration - This structure is used to write configuration upon insertion and to make changes during module operation.
- Input - This structure displays the current operational status of the module.
- Output - This structure is used to modify module operation and override the outputs.

## Configuration Structure

You must use the Configuration tags to alter module configuration. Table 15 lists and defines Configuration tags.

| Name                            |              | Style Data Type Definition                                                                                                                                  |
|---------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.ProgToFaultEn                 | Decimal BOOL | Sets outputs to selected Fault state when the owner-controller is in Program mode. 0 = outputs use Program mode setting 1 = outputs use fault mode settings |
| C.ChannelCfgBits for Channel 0  | Binary SINT  |                                                                                                                                                             |
| C.Ch0ProverDirection            | Decimal BOOL | Defines the direction of a prover that is connected to Channel 0. 0 = unidirectional prover 1 = bidirectional prover                                        |
| C.Ch1ProverDirection            | Decimal BOOL | Defines the direction of a prover that is connected to Channel 1. 0 = unidirectional prover 1 = bidirectional prover                                        |
| C.Ch0LowFreqClear               | Decimal BOOL | Enables the minimum detectable frequency level for Channel 0. Set the bit to 1 to enable it                                                                 |
| C.Ch1LowFreqClear               | Decimal BOOL | Enables the minimum detectable frequency level for Channel 1. Set the bit to 1 to enable it                                                                 |
| C.Ch0PreTrigger                 | Decimal BOOL | Enables the PreTrigger on Channel 0 for full flow. Set the bit to 1 to enable it                                                                            |
| C.Ch1PreTrigger                 | Decimal BOOL | Enables the PreTrigger on Channel 1 for full flow. Set the bit to 1 to enable it                                                                            |
| C.Operations[0].OperationalMode | Decimal SINT | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High-Resolution Frequency Mode                         |

Table 15 - 1756-CFM Module Configuration Tags

<!-- image -->

Table 15 - 1756-CFM Module Configuration Tags

| Name                                                     |              | Style Data Type Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.Operations[0].FilterControl (1)                        | Decimal SINT | The following values placed in the appropriate word invoke these filters. 0x01 = Hardware (sub 100 Hz RC) filter for F0 0x02 = Hardware (sub 100 Hz RC) filter for G0 0x03 = 2 Hardware filters (sub 100 Hz RC) for F0 and G0 0x04 = Firmware filter, 1 second debounce filter that is used for prover applications for G0 (ignore/disable the gate for 1 second after an initial pulse) 0x06 = both the Hardware and Firmware filters for G0 0x07 = all filters above: Hardware (sub 100 Hz RC) for F0 and G0 and the Firmware, 1 second debounce on prover for G0 Further combinations are applied to digital filter tags for only Series B. See Table 10 ,  Digital Filter Configuration . |
| C.Operations[0].MeterSamples                             | Decimal SINT |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| C.Operations[0].ThresholdControl                         | Decimal SINT | Sets module threshold control 0 = 50 mV threshold 1 = 1.3V (TTL) threshold 2 = 4.0V threshold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].CalculationType                          | Decimal SINT | Sets calculation type 0 = Counts/K-factor x MeterFactor correction x CCF 1 = Counts/K-factor x MeterFactor correction x AGA 7 compensation of CCF if CCF is not equal to 0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| C.Operations[0].AccelCalculation                         | Decimal SINT | Number of past samples to use to calculate an acceleration value. Sample range is 0...255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| C.Operations[0].FillMode                                 | Decimal SINT | Sets the Trickle mode for engineering units or time. 0 = Engineering units 1 = Time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| C.Operations[0].MinDetectableFreq                        | Float REAL   | User-defined value from 0 - 100,000. Sets FreqAverage, FreqPeriod, Speed, GrossRate, and NetRate reading to 0 when calculated value is less than value entered. GrossVolume, and NetVolume do not increment below this value even though TotalCounts increments over time.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| C.Operations[0].HighestAllowedFreq                       | Float REAL   | User-defined value between MinDetectableFreq and 120,000 When the frequency reaches this level, it sets the Overflow alarm limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| C.Operations[0].AccelAlarmValue                          | Float REAL   | Sets Acceleration alarm limit -Maximum acceleration (cycles per second 2 ) <AccelAlarmValue< +Maximum acceleration (cycles per second 2 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| C.Operations[0].MeterFactor                              | Float REAL   | Calibration Adjust for metering reading that is applied after K-factor correction. Typically, this factor is between 0.8 and 1.2 but the module restricts the value>0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| C.Operations[0].FilterResolution Float REAL              |              | Sets resolution of the Speed calculation based on the raw counts 0 = default of 0.00001 0.00001 = resolution of + 1 count of 100,000 raw counts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| C.Operations[0].SampleTime                               | Float REAL   | Sets time for a sample to be taken. 0...5.0 seconds (2.0 second maximum sample time for High-Resolution mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.kFactorForChan[0]            |              | Float REAL K-factor 0 for Channel 0 when frequency is < FreqAtKFactor[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| C.Operations[0].kFactStruct.kFactorForChan[1] Float REAL |              | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| C.Operations[0].kFactStruct.kFactorForChan[2] Float REAL |              | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| C.Operations[0].kFactStruct.kFactorForChan[3]            | Float REAL   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| C.Operations[0].kFactStruct.kFactorForChan[4]            | Float REAL   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| C.Operations[0].kFactStruct.kFactorForChan[5]            | Float REAL   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [5]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| C.Operations[0].kFactStruct.kFactorForChan[6]            | Float REAL   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [6]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Table 15 - 1756-CFM Module Configuration Tags

| Name                                           | Style Data Type Definition   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.Operations[0].kFactStruct.kFactorForChan[7]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [7]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.kFactorForChan[8]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [8]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.kFactorForChan[9]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [9]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.kFactorForChan[10] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [10]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| C.Operations[0].kFactStruct.kFactorForChan[11] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [11]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| C.Operations[0].kFactStruct.kFactorForChan[12] | Float REAL                   | This tag is an ordered pair with tag C.Operations[0].kFactStruct.FreqAtKFactor [12]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| C.Operations[0].kFactStruct.FreqAtKFactor[0]   | Float REAL                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| C.Operations[0].kFactStruct.FreqAtKFactor[1]   |                              | Float REAL Freq[1] for KFactor [1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[2]   |                              | Float REAL Freq[2] for KFactor [2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[3]   |                              | Float REAL Freq[3] for KFactor [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[4]   |                              | Float REAL Freq[4] for KFactor [4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[5]   |                              | Float REAL Freq[5] for KFactor [5]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[6]   |                              | Float REAL Freq[6] for KFactor [6]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[7]   |                              | Float REAL Freq[7] for KFactor [7]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[8]   |                              | Float REAL Freq[8] for KFactor [8]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[9]   |                              | Float REAL Freq[9] for KFactor [9]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C.Operations[0].kFactStruct.FreqAtKFactor[10]  |                              | Float REAL Freq[10] for KFactor [10]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| C.Operations[0].kFactStruct.FreqAtKFactor[11]  |                              | Float REAL Freq[11] for KFactor [11]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| C.Operations[0].kFactStruct.FreqAtKFactor[12]  |                              | Float REAL Freq[12] for KFactor [12]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| C.Operations[1].OperationalMode                | Decimal SINT                 | Sets the module’s operational mode. 0 = OFF 1 = Totalizer Mode 2 = Non-Resettable Totalizer Mode 3 = High-Resolution Frequency Mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| C.Operations[1].FilterControl (1)              | Decimal SINT                 | The following values placed in the appropriate word invoke these filters. 0x01 = Hardware (sub 100 Hz RC) filter for F1 0x02 = Hardware (sub 100 Hz RC) filter for G1 0x03 = 2 Hardware filters (sub 100 Hz RC) for F1 and G1 0x04 = Firmware filter, 1 second debounce filter that is used for prover applications for G1 (ignore/disable the gate for 1 second after an initial pulse) 0x06 = both the Hardware and Firmware filters for G1 0x07 = all filters above: Hardware (sub 100 Hz RC) for F1 and G1 and the Firmware, 1 second debounce on prover for G1 Further combinations are applied to digital filter tags for only Series B. See |
| C.Operations[1].MeterSamples Decimal SINT      |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| C.Operations[1].ThresholdControl Decimal SINT  |                              | Sets module threshold control 0 = 50 mV threshold 1 = 1.3V (TTL) threshold 2 = 4.0V threshold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| C.Operations[1].CalculationType Decimal SINT   |                              | Sets calculation type 0 = Counts/K-factor x MeterFactor correction x CCF 1 = Counts/K-factor x MeterFactor correction x AGA 7 compensation of CCF if CCF is not equal to 0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                |                              | C.Operations[1].AccelCalculation Decimal SINT Number of past samples to use to calculate an acceleration value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Table 15 - 1756-CFM Module Configuration Tags

| Name                                           | Style Data Type Definition   |                                                                                                                                                                                                                                                                            |
|------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.Operations[1].FillMode                       | Decimal SINT                 | Sets the Trickle mode for engineering units or time. 0 = Engineering units 1 = Time                                                                                                                                                                                        |
| C.Operations[1].MinDetectableFreq              | Float REAL                   | User-defined value from 0 - 100,000. Sets FreqAverage, FreqPeriod, Speed, GrossRate, and NetRate reading to 0 when calculated value is less than value entered. GrossVolume, and NetVolume do not increment below this value even though TotalCounts increments over time. |
| C.Operations[1].HighestAllowedFreq             | Float REAL                   | User-defined value between MinDetectableFreq and 120,000 When the frequency reaches this level, it sets the Overflow alarm limit                                                                                                                                           |
| C.Operations[1].AccelAlarmValue                | Float REAL                   | Sets Acceleration alarm limit -Maximum acceleration (cycles per second 2 ) <AccelAlarmValue< +Maximum acceleration (cycles per second 2 )                                                                                                                                  |
| C.Operations[1].MeterFactor Float REAL         |                              | Calibration Adjust for metering reading that is applied after K-factor correction. Typically, this factor is between 0.8 and 1.2 but the module restricts the value>0.                                                                                                     |
| C.Operations[1].FilterResolution               | Float REAL                   | Sets resolution of the Speed calculation based on the raw counts 0 = default of 0.00001 0.00001 = resolution of + 1 count of 100,000 raw counts.                                                                                                                           |
| C.Operations[1].SampleTime                     | Float REAL                   | Sets time for a sample to be taken. 0...5.0 seconds (2.0 second maximum sample time for High-Resolution mode)                                                                                                                                                              |
| C.Operations[1].kFactStruct.kFactorForChan[0]  |                              | Float REAL K-factor 0 for Channel 1 when frequency is < FreqAtKFactor[1]                                                                                                                                                                                                   |
| C.Operations[1].kFactStruct.kFactorForChan[1]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [1]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[2]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [2]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[3]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [3]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[4]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [4]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[5]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [5]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[6]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [6]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[7]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [7]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[8]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [8]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[9]  | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [9]                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.kFactorForChan[10] | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [10]                                                                                                                                                                                        |
| C.Operations[1].kFactStruct.kFactorForChan[11] | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [11]                                                                                                                                                                                        |
| C.Operations[1].kFactStruct.kFactorForChan[12] | Float REAL                   | This tag is an ordered pair with tag C.Operations[1].kFactStruct.FreqAtKFactor [12]                                                                                                                                                                                        |
| C.Operations[1].kFactStruct.FreqAtKFactor[0]   | Float REAL                   |                                                                                                                                                                                                                                                                            |
| C.Operations[1].kFactStruct.FreqAtKFactor[1]   |                              | Float REAL Freq[1] for KFactor [1]                                                                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.FreqAtKFactor[2]   |                              | Float REAL Freq[2] for KFactor [2]                                                                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.FreqAtKFactor[3]   |                              | Float REAL Freq[3] for KFactor [3]                                                                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.FreqAtKFactor[4]   |                              | Float REAL Freq[4] for KFactor [4]                                                                                                                                                                                                                                         |
| C.Operations[1].kFactStruct.FreqAtKFactor[5]   |                              | Float REAL Freq[5] for KFactor [5]                                                                                                                                                                                                                                         |

Table 15 - 1756-CFM Module Configuration Tags

| Name                                          |              | Style Data Type Definition                                                                                                                                       |
|-----------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.Operations[1].kFactStruct.FreqAtKFactor[6]  |              | Float REAL Freq[6] for KFactor [6]                                                                                                                               |
| C.Operations[1].kFactStruct.FreqAtKFactor[7]  |              | Float REAL Freq[7] for KFactor [7]                                                                                                                               |
| C.Operations[1].kFactStruct.FreqAtKFactor[8]  |              | Float REAL Freq[8] for KFactor [8]                                                                                                                               |
| C.Operations[1].kFactStruct.FreqAtKFactor[9]  |              | Float REAL Freq[9] for KFactor [9]                                                                                                                               |
| C.Operations[1].kFactStruct.FreqAtKFactor[10] |              | Float REAL Freq[10] for KFactor [10]                                                                                                                             |
| C.Operations[1].kFactStruct.FreqAtKFactor[11] |              | Float REAL Freq[11] for KFactor [11]                                                                                                                             |
| C.Operations[1].kFactStruct.FreqAtKFactor[12] |              | Float REAL Freq[12] for KFactor [12]                                                                                                                             |
| C.OutputSetup[0].FaultMode                    | Decimal SINT | Sets the state of output 0 when communications are lost with the owner controller in Fault Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Fault Mode 2 = Set Output 0 to ON when in Fault Mode                                                                                                                                                                  |
| C.OutputSetup[0].ProgMode                     | Decimal SINT | Sets the state of output 0 when communications are lost with the owner controller in Program Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Program Mode 2 = Set Output 0 to ON when in Program Mode                                                                                                                                                                  |
| C.OutputSetup[0].DynamicError                 | Decimal SINT | Sets the state of output 0 when a dynamic error occurs 0 = Continue operation 1 = Reset Output 0 to OFF on Error 2 = Set Output 0 to ON on Error                 |
| C.OutputSetup[0].TriggerOn                    | Decimal SINT | Sets when output 0 energizes 0 = No Action 1 = Frequency 2 = Acceleration 3 = Full Flow State 4 = Trickle Flow State 5 = Prover Run State 6 = Prover Range State |
| C.OutputSetup[0].TieToCounter                 |              | Ties a channel to output 0 0 = No connection 1 = Connect Channel0 to Output0 2 = Connect Channel1 to Ouput0                                                      |
| C.OutputSetup[1].FaultMode                    | Decimal SINT | Sets the state of output 1 when communications are lost with the owner controller in Fault Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Fault Mode 2 = Set Output 0 to ON when in Fault Mode                                                                                                                                                                  |
| C.OutputSetup[1].ProgMode                     | Decimal SINT | Sets the state of output 1 when communications are lost with the owner controller in Program Mode 0 = Continue operation 1 = Reset Output 0 to OFF when in Program Mode 2 = Set Output 0 to ON when in Program Mode                                                                                                                                                                  |
| C.OutputSetup[1].DynamicError                 | Decimal SINT | Sets the state of output 1 when a dynamic error occurs 0 = Continue operation 1 = Reset Output 0 to OFF on Error 2 = Set Output 0 to ON on Error                 |
| C.OutputSetup[1].TriggerOn                    | Decimal SINT | Sets when output 1 energizes 0 = No Action 1 = Frequency 2 = Acceleration 3 = Full Flow State 4 = Trickle Flow State 5 = Prover Run State 6 = Prover Range State |
| C.OutputSetup[1].TieToCounter                 |              | Ties a channel to output 1 0 = No connection 1 = Connect Channel0 to Output 1 2 = Connect Channel1 to Output 1                                                   |

## Input Tags

Table 16 - 1756-CFM Module Input Tags

| Name                    |              | Style Data Type Definition                                                                                |
|-------------------------|--------------|-----------------------------------------------------------------------------------------------------------|
| I.Fault                 | Hex  DINT    | Display if a fault has occurred on the module. 0 = no fault has occurred 1 = a fault has occurred         |
| I.ChannelStatus         | Hex  DINT    |                                                                                                           |
| I.Output0State          | Decimal BOOL | Displays the state of output 0 0 = OFF 1 = ON                                                             |
| I.Output1State          | Decimal BOOL | Displays the state of output 1 0 = OFF 1 = ON                                                             |
| I.Output0IsOverridden   | Decimal BOOL | Displays whether output 0 was manually overridden 0 = output was not overridden 1 = output was overridden |
| I.Output1IsOverridden   | Decimal BOOL | Displays whether output 1 was manually overridden 0 = output was not overridden 1 = output was overridden |
| I.Ch0WasReset           | Decimal BOOL | Displays whether channel 0 was reset 0 = output was not reset 1 = output was reset                        |
| I.Ch1WasReset           | Decimal BOOL | Displays whether channel 1 was reset 0 = output is not overridden 1 = output is overridden                |
| I.Ch0AccelerationAlarm  | Decimal BOOL | Displays whether acceleration alarm was set on channel 0 0 = alarm was not set 1 = alarm was set          |
| I.Ch0OverspeedAlarm     | Decimal BOOL | Displays whether overspeed alarm was set on channel 0 0 = alarm was not set 1 = alarm was set             |
| I.Ch0OverrangeAlarm     | Decimal BOOL | Displays whether overrange alarm was set on channel 0 0 = alarm was not set 1 = alarm was set             |
| I.Ch0OverflowAlarm      | Decimal BOOL | Displays whether overflow alarm was set on channel 0 0 = alarm was not set 1 = alarm was set              |
| I.Ch1AccelerationAlarm  | Decimal BOOL | Displays whether acceleration alarm was set on channel 1 0 = alarm was not set 1 = alarm was set          |
| I.Ch1OverspeedAlarm     | Decimal BOOL | Displays whether overspeed alarm was set on channel 1 0 = alarm was not set 1 = alarm was set             |
| I.Ch1OverrangeAlarm     | Decimal BOOL | Displays whether overrange alarm was set on channel 1 0 = alarm was not set 1 = alarm was set             |
| I.Ch1OverflowAlarm      | Decimal BOOL | Displays whether overflow alarm was set on channel 1 0 = alarm was not set 1 = alarm was set              |
| I.Ch0ConsumerErrorAlarm | Decimal BOOL | Displays whether the consumer error alarm was set on channel 0 0 = alarm was not set 1 = alarm was set    |
| I.Ch1ConsumerErrorAlarm | Decimal BOOL | Displays whether the consumer error alarm was set on channel 1 0 = alarm was not set 1 = alarm was set    |

You must use the Input tags to monitor module status. Table 16 lists and defines Input tags.

Table 16 - 1756-CFM Module Input Tags

| Name                                 | Style Data Type Definition                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I.Status[0].ProverState              | Decimal SINT Displays status of the prover operation on channel 0 0 = Prover Not Active 1 = Prover waiting for first start 2 = Prover waiting for first stop 3 = Prover waiting for second start 4 = Prover waiting for second stop 5 = Prover Complete                                                                                                                    |
| I.Status[0].FillState                | Decimal SINT Displays current state of module for channel 0. These states are possible: 0 = Filler not active 1 = Filler Enabled only, waiting for start 2 = Timed Trickle Flow complete, not filled 3 = Full Flow for Fill function 4 = Timed Trickle Flow for Fill function 5 = Engineering units for Full Flow 6 = Engineering units for Trickle Flow 7 = Fill complete |
| I.Status[0].ConsumerErrorCode        | Decimal INT  See Using Error Codes on page 105                                                                                                                                                                                                                                                                                                                             |
| I.Status[0].TotalCounts Decimal DINT | Displays actual pulses that are counted by the counter that is connected to the channel 0                                                                                                                                                                                                                                                                                  |
|                                      | I.Status[0].FreqAverage Float REAL Displays frequency averaged over the Meter samples on channel 0                                                                                                                                                                                                                                                                         |
|                                      | I.Status[0].FreqPeriod Float REAL Displays frequency using sample time on channel 0                                                                                                                                                                                                                                                                                        |
|                                      | I.Status[0].Speed Float REAL Displays frequency using filter resolution on channel 0                                                                                                                                                                                                                                                                                       |
| I.Status[0].Acceleration Float REAL  | Displays acceleration on channel 0 as calculated by using AccelCalculation samples                                                                                                                                                                                                                                                                                         |
|                                      | I.Status[0].FillTotal Float REAL Fill total in engineering units                                                                                                                                                                                                                                                                                                           |
| I.Status[0].GrossVolume Float REAL   | Total Counts during each Sample/K-factor x Meter Factor as occurs on channel 0                                                                                                                                                                                                                                                                                         |
| I.Status[0].NetVolume Float REAL     | Total Counts during each Sample/K-factor x MeterFactor x CCF) as occurs on channel 0                                                                                                                                                                                                                                                                                   |
| I.Status[0].GrossRate Float REAL     | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor as occurs on channel 0                                                                                                                                                                                                                                                                          |
| I.Status[0].NetRate Float REAL       | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor x CCF as occurs on channel 0                                                                                                                                                                                                                                                                    |
| I.Status[0].ProverTotal Float REAL   | Displays total counts (in engineering units) received on channel 0 in prover operation. Total resets when the ProverEnable feature is enabled. This value operates concurrently with NetVolume, and must be saved if subtracted from the NetVolume for single and multiple prover verifications.                                                                           |
| I.Status[1].ProverState Decimal SINT | Displays status of the prover operation on channel 1 0 = Prover Not Active 1 = Prover waiting for first start 2 = Prover waiting for first stop 3 = Prover waiting for second start 4 = Prover waiting for second stop 5 = Prover Complete                                                                                                                                 |
| I.Status[1].FillState Decimal SINT   | Displays current state of module for channel 1. These states are possible: 0 = Filler not active 1 = Filler Enabled only, waiting for start 2 = Timed Trickle Flow complete, not filled 3 = Full Flow for Fill function 4 = Timed Trickle Flow for Fill function 5 = Engineering units for Full Flow 6 = Engineering units for Trickle Flow 7 = Fill complete              |
|                                      | I.Status[1].ConsumerErrorCode Decimal INT See Using Error Codes on page 105                                                                                                                                                                                                                                                                                                |
| I.Status[1].TotalCounts Decimal DINT | Displays actual pulses that are counted by the counter that is connected to the channel 1                                                                                                                                                                                                                                                                                  |

Table 16 - 1756-CFM Module Input Tags

| Name                     |              | Style Data Type Definition   |                                                                                                                                                                                                                                                                                    |
|--------------------------|--------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I.Status[1].FreqAverage  | Float        | REAL                         | Displays frequency averaged over the Meter samples on channel 1                                                                                                                                                                                                                    |
| I.Status[1].FreqPeriod   | Float        | REAL                         | Displays frequency using sample time on channel 1                                                                                                                                                                                                                                  |
| I.Status[1].Speed        | Float        | REAL                         | Displays frequency using filter resolution on channel 1                                                                                                                                                                                                                            |
| I.Status[1].Acceleration | Float        | REAL                         | Displays acceleration on channel 1 as calculated by using AccelCalculation samples                                                                                                                                                                                                 |
| I.Status[1].FillTotal    | Float        |                              | REAL Fill total in engineering units                                                                                                                                                                                                                                               |
| I.Status[1].GrossVolume  | Float        | REAL                         | Total Counts during each Sample/K-factor x Meter Factor as occurs on channel 1                                                                                                                                                                                                 |
| I.Status[1].NetVolume    | Float        | REAL                         | Total Counts during each Sample/K-factor x MeterFactor x CCF) as occurs on channel 1                                                                                                                                                                                           |
| I.Status[1].GrossRate    | Float        | REAL                         | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor as occurs on channel 1                                                                                                                                                                                  |
| I.Status[1].NetRate      | Float        | REAL                         | Total Counts in Meter Sample/ (K-factor x Sample Interval) x Meter Factor x CCF as occurs on channel 1                                                                                                                                                                            |
| I.Status[1].ProverTotal  | Float        | REAL                         | Displays total counts that are received on channel 1 in prover operation. Total resets when the ProverEnable feature is enabled. This value operates concurrently with NetVolume, and must be saved if subtracted from the NetVolume for single and multiple prover verifications. |
| I.CSTTimestamp[0]        | Decimal DINT |                              |                                                                                                                                                                                                                                                                                    |
| I.CSTTimestamp[1]        | Decimal DINT |                              |                                                                                                                                                                                                                                                                                    |

## Output Tags

Table 17 - 1756-CFM Module Output Tags

| Name                    | Style        | Data Type Definition                                                                                                                                                                            |
|-------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O.Total[0].AlarmEnables | Binary SINT  |                                                                                                                                                                                                 |
| O.Total[0].Overrange    | Decimal BOOL | Enables the Overrange alarm on output that is connected to channel 0. When the Frequency Period exceeds 100 KHz, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                              |
| O.Total[0].Overflow     | Decimal BOOL | Enables the Overflow alarm on output that is connected to channel 0. When the Total Counts exceeds the Roll Over value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                       |
| O.Total[0].Overspeed    | Decimal BOOL | Enables the Overspeed alarm on output that is connected to channel 0. When the Speed exceeds the Highest Allowed Frequency value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled             |
| O.Total[0].Acceleration | Decimal BOOL | Enables the Acceleration alarm on output that is connected to channel 0. When the absolute acceleration exceeds the Acceleration Alarm value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled |
| O.Total[0].Control      | Binary SINT  |                                                                                                                                                                                                 |

You must use the Output tags to change module configuration during operation. Table 17 lists and defines Output tags.

Table 17 - 1756-CFM Module Output Tags

| Name  Style                                              | Data Type Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O.Total[0].Reset                                         | Decimal BOOL Rising edge resets the count We recommend that you latch the <tagname>O.ResetCounter.(0-1) bit and unlatch that with the <tagname>I.WasReset.(0-1) bit. • When the <tagname>I.WasReset.(0-1) bit will remain on until the next time, the <tagname>O.ResetCounter.(0-1) bit is turned on. • When the <tagname>O.ResetCounter.(0-1) bit goes high, the <tagname>I.WasReset.(0-1) goes low until the <tagname>I.StoredValue.(0-1) equals 0. Then, <tagname>I.WasReset.(0-1) will go high again. The toggle from On to Off is done quickly and you may not see it in the controller. |
| O.Total[0].Load                                          | Decimal BOOL  Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| O.Total[0].ProverEnable                                  | Decimal BOOL Enables the prover operation on output that is connected to channel 0. Once this bit is enabled, the module waits for output Z0 to energize before beginning prover operations. 0 = Prover operation is disabled 1 = Prover operation is enabled                                                                                                                                                                                                                                                                                                                                 |
| O.Total[0].FillEnable Decimal BOOL                       | Enables the filling operation on output that is connected to channel 0. 0 = Fill operation is disabled 1 = Fill operation is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| O.Total[0].FillStart Decimal BOOL                        | Begins filling operation when Fill Enable is enabled on output that is connected to channel 0. 0 = Do not begin filling 1 = Begin filling                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| O.Total[0].FillHold Decimal BOOL                         | Holds/pauses filling operation on output that is connected to channel 0 0 = Continue filling operation 1 = Hold/pause filling operation                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| O.Total[0].RollOverValue Decimal DINT                    | Sets the user-defined rollover value on output that is connected to channel 0. Range of 0 - 2,147,483,647                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| O.Total[0].CombinedCorrectionFactor Float REAL           | Unitless factor that is multiplied by Gross Rate with results shown as NetRate of channel 0. This value must be set to 1.0 when not used or gross rate will be 0. Calculation Type must be set to 0 to use this factor.                                                                                                                                                                                                                                                                                                                                                                       |
|                                                          | O.Total[0].BaseTemperature Float REAL Temperature in °F of output connected to channel 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                          | O.Total[0].FlowingTemperature Float REAL Temperature in °F of output connected to channel 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                          | O.Total[0].AtmosphericPressure Float REAL Pressure in psia of output connected to channel 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                          | O.Total[0].StaticGaugePressure Float REAL Pressure in psig of output connected to channel 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                          | O.Total[0].BasePressure Float REAL Pressure in psig of output connected to channel 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| O.Total[0].BaseCompressibility Float REAL Default = 1    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| O.Total[0].FlowingCompressibility Float REAL Default = 1 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| O.Total[0].FillTotalTarget Float REAL                    | Target for Fill Complete, except when Fill Transition is greater than this value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| O.Total[0].FillTransition Float REAL                     | When fill cycle is started, trickle flow is initiated when the Fill Total is equal to or greater than this value. Full flow is initiated when the Fill Total is less than this value.                                                                                                                                                                                                                                                                                                                                                                                                         |
| O.Total[0].FillTransitionTimer Float REAL                | When timed trickle flow is selected, the status remains ON for this time during this state. The value must be changed prior to entering the trickle flow state.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| O.Total[1].AlarmEnables Binary SINT                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| O.Total[1].Overrange Decimal BOOL                        | Enables the Overrange alarm on output that is connected to channel 1. When the Frequency Period exceeds 100 KHz, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                                                                                                                                                                                                                                                                                            |
| O.Total[1].Overflow Decimal BOOL                         | Enables the Overflow alarm on output that is connected to channel 1. When the Total Counts exceeds the Roll Over value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                                                                                                                                                                                                                                                                                                                                                                                     |

Table 17 - 1756-CFM Module Output Tags

| Name                                | Style        | Data Type Definition   |                                                                                                                                                                                                                                                  |
|-------------------------------------|--------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O.Total[1].Overspeed                | Decimal BOOL |                        | Enables the Overspeed alarm on output that is connected to channel 1. When the Speed exceeds the Highest Allowed Frequency value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                              |
| O.Total[1].Acceleration             | Decimal BOOL |                        | Enables the Acceleration alarm on output that is connected to channel 1. When the absolute acceleration exceeds the Acceleration Alarm value, this alarm is set. 0 = No Alarm 1 = Alarm Enabled                                                  |
| O.Total[1].Control                  | Binary SINT  |                        |                                                                                                                                                                                                                                                  |
| O.Total[1].Reset                    | Decimal BOOL |                        |                                                                                                                                                                                                                                                  |
| O.Total[1].Load                     | Decimal BOOL |                        |                                                                                                                                                                                                                                                  |
| O.Total[1].ProverEnable             | Decimal BOOL |                        | Enables the prover operation on output that is connected to channel 1. Once this bit is enabled, the module waits for output Z0 to energize before beginning prover operations. 0 = Prover operation is disabled 1 = Prover operation is enabled |
| O.Total[1].FillEnable               | Decimal BOOL |                        | Enables the filling operation on output that is connected to channel 1. 0 = Fill operation is disabled 1 = Fill operation is enabled.                                                                                                            |
| O.Total[1].FillStart                | Decimal BOOL |                        | Begins filling operation when Fill Enable is enabled on output that is connected to channel 1. 0 = Do not begin filling 1 = Begin filling                                                                                                        |
| O.Total[1].FillHold                 | Decimal BOOL |                        | Holds/pauses filling operation on output that is connected to channel 1. 0 = Continue filling operation 1 = Hold/pause filling operation                                                                                                         |
| O.Total[1].RollOverValue            | Decimal DINT |                        | Sets the user-defined rollover value on output that is connected to channel 1. Range of 0 - 2,147,483,647                                                                                                                                        |
| O.Total[1].CombinedCorrectionFactor | Float        | REAL                   | Unitless factor that is multiplied by Gross Rate with results shown as NetRate of channel 1. This value must be set to 1.0 when not used or gross rate will be 0. Calculation Type must be set to 0 to use this factor.                          |
| O.Total[1].BaseTemperature          | Float        | REAL                   | Temperature in °F of output connected to channel 1.                                                                                                                                                                                              |
| O.Total[1].FlowingTemperature       | Float        | REAL                   | Temperature in °F of output connected to channel 1.                                                                                                                                                                                              |
| O.Total[1].AtmosphericPressure      | Float        | REAL                   | Pressure in psia of output connected to channel 1.                                                                                                                                                                                               |
| O.Total[1].StaticGaugePressure      | Float        | REAL                   | Pressure in psig of output connected to channel 1.                                                                                                                                                                                               |
| O.Total[1].BasePressure             | Float        | REAL                   | Pressure in psig of output connected to channel 1.                                                                                                                                                                                               |
| O.Total[1].BaseCompressibility      | Float        | REAL                   | Default = 1                                                                                                                                                                                                                                      |
| O.Total[1].FlowingCompressibility   | Float        | REAL                   | Default = 1                                                                                                                                                                                                                                      |
| O.Total[1].FillTotalTarget          | Float        | REAL                   | Target for Fill Complete, except when Fill Transition is greater than this value.                                                                                                                                                                |
| O.Total[1].FillTransition           | Float        | REAL                   | When fill cycle is started, trickle flow is initiated when the Fill Total is equal to or greater than this value. Full flow is initiated when the Fill Total is less than this value.                                                            |

Table 17 - 1756-CFM Module Output Tags

| Name                                                                                                                                                                                                                                                                                                                 | Style        |      | Data Type Definition                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O.Total[1].FillTransitionTimer                                                                                                                                                                                                                                                                                       | Float        | REAL |                                                                                                                                                             |
| O.OutputControl[0].0 (A series of tags similar to this one are used repeatedly for outputs 0...31 connected to channel 0. The name changes in each occurrence for the specific output. For example, output 1 is named: O.OutputControl[0].1 Only output 0 is listed here but all exist in the programming software.) | Decimal BOOL |      | Manually sets the operation of outputs that are connected to channel 0. 0 = Module operation of outputs 1 = Override Output0 to 0 2 = Override Output0 to 1 |
| O.OutputControl[1].0 (A series of tags similar to this one are used repeatedly for outputs 0...31 connected to channel 1. The name changes in each occurrence for the specific output. For example, output 1 is named: O.OutputControl[1].1 Only output 0 is listed here but all exist in the programming software.) | Decimal BOOL |      | Manually sets the operation of outputs that are connected to channel 1. 0 = Module operation of outputs 1 = Override Output0 to 0 2 = Override Output0 to 1 |

## Notes:

## What This Appendix Contains

## Input Circuits

## Module Schematics

Use this appendix to understand the internal logic of the 1756-CFM module.

Follow the wiring practices that are described in Chapter 4, Install the 1756CFM Module, when wiring your I/O devices. This includes:

- Routing conductors
- Grounding practices
- use of shielded cables

The module input logic consists of:

- Flowmeter input circuits
- gate input circuits

## Flowmeter Inputs

The flowmeter input circuit combines operational amplifier principles with solid-state devices to provide constant logic pulses internal to the module. The circuit is designed to interface with both active or passive sensor inputs by accepting any pulse output device (such as turbine flowmeter, magnetic pickup or digital pickup).

<!-- image -->

<!-- image -->

CASE A – for 5V DC operation

gate input current = (gate input voltage - 2V

150 

## Examples

If gate input voltage = 5V DC

gate input current = (5V- 2V)

150 

gate input current = 20 mA

## Gate Inputs

Gate inputs are used for running prover and store count values. There is one gate that is associated with each flowmeter input circuit (Z0 corresponds to F0).

## Series A Module

<!-- image -->

To turn on a gate circuit, you must source current through the input resistors sufficient to turn on the opto-isolator in the circuit. If no connection is made to the pair of gate terminals, no current flows through the photodiode of the opto-isolator and that gate is OFF (the corresponding input status indicator is OFF).

The input current magnitude can be determined by:

<!-- image -->

1. There is approximately a 2V drop across (Q1 + the photodiode).
2. The operating range of the input is 5-10mA and Q1 functions as an overcurrent protection circuit. If an open collector device with pull-up is used, the value of the pull-up must be added to the  value shown in the denominator.

2

1

)

CASE A – for 5V DC operation

<!-- image -->

1. There is approximately a 0.4V drop across R65 that is maintained by Q15 constant current source. A minimum of 4.5V is required to turn on the Input circuit.

## Series B Module

<!-- image -->

To turn on a gate circuit, you must source current through the input resistors sufficient to turn on the Q3 and opto-isolator in the circuit. Operating current range for this new input circuit is 5…8mA. If no connection is made to the pair of gate terminals, no current flows through the photodiode of the opto-isolator and that gate IS OFF (the corresponding input status indicator is OFF).

The photodiode, combined with Q3, requires approximately 1.8V DC total to switch ON. Q15 works as constant current source and maintains constant current flow of approximately 4 mA across photo diode. R65 is around 93 Ω and Q3 maintains approximately 0.4V drop across it.

The input current magnitude can be determined by:

CASE B – for 10V DC to 31.2V DC operation

<!-- image -->

1. There is approximately a 2.5...4.5 V drop across Resistors in series with Q15 that is maintained by Q15 constant current source. A minimum of approximately 7.5V is required to turn on the Input circuit.

## Output Circuits

The module provides two output circuits.

## Discrete Outputs

The module's outputs are composed of isolated power MOSFETs. These devices operate in current sourcing mode, and can deliver up to 1 A (@ 10-31.2V DC) and 20 mA (@ 5V DC).

Series A Module

## IMPORTANT This schematic represents the Series A module

<!-- image -->

The 1756-CFM/A module contains two output circuits. Customer supplied power, ranging from +5V…+31.2V DC, is connected internally (through terminals #18 and 20) to the power output transistors.

When an output is turned on, current flows into the source, out of the drain, through the load connected to the ground of the customer supply (customer return). Diode D26 protects the power output transistor Q11 from damage due to inductive loads.

Output transistor Q11 is thermally protected power MOSFET and turns off at approximately 4 A. After an output goes into thermal shutdown, you must fix the cause of the shutdown and toggle the output OFF and ON to reenergize the output.

## Series B Module

## IMPORTANT This schematic represents the Series B module

<!-- image -->

The 1756-CFM/B module contains two output circuits. Customer supplied power, ranging from +5V DC…+31.2V DC, is connected internally through terminals #18 and 20 to the power output transistors, for example, Q28 as depicted above.

When an output is turned on, current flows into the source, out of the drain, through the load connected to the ground of the customer supply (customer return). Diode D34 protects the power output transistor Q11 from damage due to inductive loads.

Output transistor Q28 is thermally protected by MOS Driver and turns off at approximately 1.2 A. After an output goes into thermal shutdown, you must fix the cause of the shutdown and toggle the output OFF and ON to re-energize the output.

## Notes:

## Frequency Accuracy in High-Resolution Frequency Mode

## Frequency Accuracy

Use this appendix to calculate the frequency accuracy for High-Resolution Frequency mode and Totalizer mode.

There are two steps to calculating frequency accuracy in High-Resolution Frequency mode.

1. Calculate frequency accuracy.
2. Determine the application's operating conditions and add the error for those conditions to the value obtained in step 1.

These values must be added to your frequency accuracy results in Totalizer mode:

- Crystal error - 0.005% @ 25 °C
- Drift and crystal error - 0.01% from 0…60 °C

## Calculate Frequency Accuracy

When calculating frequency accuracy in High-Resolution Frequency mode, you must know:

- sample time period
- input frequency

Use one of two equations to calculate the firmware error, in High-Resolution Frequency mode.

Choose the equation according to the frequency of your application.

- If your application has a frequency in this range:
- 1 Hz to 1/T s

use the following equation:

<!-- formula-not-decoded -->

- If your application has a frequency in this range:
- greater than 1/T s to 120 kHz

<!-- image -->

## Frequency Accuracy in Totalizer Mode

use the following equation:

<!-- formula-not-decoded -->

## EXAMPLE

Based on the equations listed above, if your application uses a T s = 0.1 seconds, the "cut off" frequency for choosing an equation is 10 Hz because 1/T s (or 1/0.1) = 10.

In other words, if your application uses a T s = 0.1 seconds, for frequencies 1...10 Hz, use this equation:

<!-- formula-not-decoded -->

For frequencies greater than 10 Hz to 1 kHz, use this equation.

<!-- formula-not-decoded -->

There are two steps to calculating frequency accuracy in Totalizer mode.

1. Calculate frequency accuracy.
2. Determine the application's operating conditions and add the error for those conditions to the value obtained in step 1. These values must be added to your frequency accuracy results in Totalizer mode:
- Crystal error - 0.005% @ 25 °C
- Drift and crystal error - 0.01% 0...60 °C

## Calculate Frequency Accuracy

You can calculate frequency accuracy in Totalizer mode for:

- Frequency Period
- Speed
- Frequency average

## Frequency Period

For frequency period, you must know:

- User-defined sample time period (T s )
- Application frequency (Fin)
- Number of accumulated counts in sample time (Counts)

Use this equation to calculate frequency accuracy in Totalizer mode for frequency period:

<!-- formula-not-decoded -->

EXAMPLE For example, in an application with these conditions:

- 0.5 seconds time period
- 123 Hz frequency
- y
· 25 °C operating temperature

accuracy is determined with this equation:

<!-- image -->

## Speed

For speed, you must know the filter resolution. Use this equation to calculate frequency accuracy in Totalizer mode for speed:

Accuracy = Resolution x 100

EXAMPLE For example, in an application with these conditions:

- 0.001 filter resolution
- 25 °C operating temperature accuracy is determined with this equation:

<!-- image -->

## Frequency Average

For frequency average, you must know:

- Application frequency (Fin)
- Number of accumulated in sample time (Counts)

Use this equation to calculate frequency accuracy in Totalizer mode for frequency period:

<!-- formula-not-decoded -->

EXAMPLE For example, in an application with these conditions:

- 25 meter samples
- 123 Hz frequency
- y
· 60 °C operating temperature

accuracy is determined with this equation:

<!-- image -->

## Configure Output Behavior with RSLogix 5000 Version 16 and Earlier

If you have a 1756-CFM module with firmware revision 2.4 and are using RSLogix 5000® software, version 16 or earlier, use this procedure to enable and configure the output behavior.

If you do not want to use the output behavior features available in firmware revision 2.4, you do not need to complete this procedure. For an explanation of the output behavior features, see Configurable Output Behaviors on page 52 .

## IMPORTANT

Use these configuration procedures only if you are configuring your 1756-CFM module by using RSLogix 5000 software version 16 or earlier.

To complete the configuration, you must download and open the CFM\_GenericProfileExample.ACD file from one of these locations:

- As packaged with the1756-CFM firmware revision 2.4 firmware kit provided at http://www.rockwellautomation/support.
- In the RSLogix 5000 software version 16 quick start page:
- To open the file, click the Controller Projects tab. Then choose Open Sample Project &gt; V16 &gt; Rockwell Automation &gt; CFM\_GenericProfileExample.ACD.

Once you have downloaded and opened the CFM\_GenericProfileExmple.ACD file, complete the configuration procedure that matches your application.

| If you are using the module in Go to   |                                                                              |
|----------------------------------------|------------------------------------------------------------------------------|
| A new application                      | Configure the 1756-CFM Module for Use in a New Application on page 128 .     |
| An existing application                | Configure a 1756-CFM Module for Use in an Existing Application on page 132 . |

<!-- image -->

## Configure the 1756-CFM Module for Use in a New Application

Complete this procedure if you are using the 1756-CFM module and the configurable on/off feature in a new application.

## Add the 1756-Generic Profile to the Program

1. In RSLogix 5000 software, create a project named CFM\_DEMO.
2. Specify the controller type, revision number, chassis type, and slot number according to your ControlLogix® controller chassis.
3. In the I/O Configuration folder, add a new module.
4. Use the Generic 1756 Module profile listed in Other module types.
5. In the New Module dialog box, enter the Connection Parameter information exactly as displayed below.

Enter the slot number that matches the location of the 1756-CFM module in your ControlLogix® chassis.

<!-- image -->

6. Click OK.
2. The Module Properties dialog box opens.
7. Set the module RPI to 100.
8. Click OK.

The 1756-Generic module is now in the I/O configuration.

## Copy and Paste the Tags and Logic from the Example to Your Program

1. Minimize the CFM\_DEMO project and open a new instance of RSLogix 5000 software.
2. Open CFM\_GenericProfileExample.ACD.
3. In the controller organizer of the CFM\_GenericProfileExample project, expand the User-Defined data types.
4. Copy one of the User-Defined data types. You must select and copy each of the User-Defined data types individually.
5. In the CFM\_DEMO project, paste the copied User-Defined data type into the User-Defined data type folder.

<!-- image -->

<!-- image -->

<!-- image -->

6. Repeat steps four and five until all User-Defined data types contained in the CFM\_GenericProfileExample project have been pasted in the CFM\_DEMO project.
7. In the CFM\_GenericProfileExample project, copy these data tags in the Controller Tag folder.
8. In the CFM\_DEMO project, paste the copied data tags into the Controller Tags folder by using the Edit Tags tab.
9. In the CFM\_GenericProfileExample project, copy ladder logic rung 1 in the Main Routine folder.
10. In the CFM\_DEMO project, paste the copied rung into the Main Routine folder.
11. Change the Local:5 tag references to correspond to the location of your 1756-CFM module in your chassis.
12. Accept the pasted rung.
13. Delete the empty rung.

<!-- image -->

|            | Value   | Force Mas   | Style   | Data Type   |
|------------|---------|-------------|---------|-------------|
| CFMB_C     | {...}   |             |         | CFM_Rev_B   |
| CFM_Config | 0       |             | Decimal | DINT        |
| CFM_IN     | {...}   |             |         | CFM_        |
| CFMOUT     | (...}   | {...}       |         | CFM_0       |

<!-- image -->

## Specify the Configurable On/Off Behavior

1. In the CFM\_DEMO program, select the Controller Tag folder and view the Monitor Tags tab.
2. Expand the CFM\_B\_C tag until you reach the CFM\_B\_C.OutputWindow data tags.
3. In the Value column of CFM\_B\_C.OutputWindow FreqOn and FreqOff data tags, enter the desired On and Off frequency limits.

<!-- image -->

| Name                            | Value ←     | Force Mas   | Style   | Data Type       |
|---------------------------------|-------------|-------------|---------|-----------------|
| -CFM_B_C                        | (...}       | {...}       |         | CFM_Rev_B       |
| CFM_B_C.ProgToFaultEn           | 0           |             | Decimal | BOOL            |
| -CFM_B_C.ChannelCfgBits         | 2#0000_0000 |             | Binary  | SINT            |
| CFM_B_C.ChOProverDirection      | 0           |             | Decimal | BOOL            |
| CFM_B_C.Ch1ProverDirection      | 0           |             | Decimal | BOOL            |
| CFM_B_C.ChOLowFreqClear         | 0           |             | Decimal | BOOL            |
| CFM_B_C.Ch1LowFreqClear         | 0           |             | Decimal | BOOL            |
| CFM_B_C.ChOPreTrigger           | 0           |             | Decimal | BOOL            |
| CFM_B_C.Ch1PreTrigger           | 0           |             | Decimal | BOOL            |
| -CFM_B_C.Operations             | (...}       | {...}       |         | CFM_Setup_C[2]  |
| -CFM_B_C.OutputSetup            | {...}       | (...}       |         | CFM_OutCfg_C[2] |
| -CFM_B_C.OutputSetup[0]         | (...}       | (...}       |         | CFM_OutCfg_C    |
| -CFM_B_C.OutputSetup[1]         | {...}       | (...}       |         | CFM_OutCfg_C    |
| -CFM_B_C.Outputwindow           | (...}       | (...}       |         | OUT_WIN[2]      |
| -CFM_B_C.Outputwindow[0]        | (...}       | (...}       |         | OUT_WIN         |
| CFM_B_C.Outputwindow[0].FreqOn  | 6000.0      |             | Float   | REAL            |
| CFM_B_C.Outputwindow[0].FreqOff | 4000.0      |             | Float   | REAL            |
| -CFM_B_C.Outputwindow[1]        | {...}       | {...}       |         | OUT_WIN         |
| CFM_B_C.Outputw/indow[1].FreqOn | 6000.0      |             | Float   | REAL            |
| CFM_B_C.Outputwindow[1].FreqOff | 4000.0      |             | Float   | REAL            |

See Table 5 on page 52 for more information about determining your On/ Off frequency limits.

## IMPORTANT

Test the configuration before implementing the changes into your production process.

## Configure a 1756-CFM Module for Use in an Existing Application

Complete this configuration process if you are using the 1756-CFM module with an existing application.

## Add the 1756-Generic Profile to the Program

1. In RSLogix 5000 software, open a project that contains programming for an existing 1756-CFM module.
2. In the I/O configuration, delete the existing 1756-CFM module.
3. In the I/O configuration, add a new module. Use the generic 1756 module profile listed in Other module types.
4. Name the new module according to your preference.
5. In the New Module dialog box, enter the Connection Parameters and Comm Format exactly as displayed below.

Enter the slot number that matches the location of the 1756-CFM module in your ControlLogix chassis.

<!-- image -->

6. Click OK. The Module Properties dialog box displays.
7. Set the module RPI to 100.
8. Click OK.

The 1756-Generic module is now in the I/O configuration.

## Copy and Paste the Tags and Logic from the Example to Your Program

1. Minimize the previously existing project and open a new instance of RSLogix 5000 software.
2. Open the CFM\_GenericProfileExample.ACD.
3. In the controller organizer of the CFM\_GenericProfileExample project, expand the User-Defined data types.
4. Copy one of the User-Defined data types.

<!-- image -->

You must select and copy each of the User-Defined data types individually.

<!-- image -->

5. In the previously existing project, paste the copied User-Defined data type into the User-Defined data type folder.

<!-- image -->

6. Repeat steps four and five until all User-Defined data types types that are contained in the CFM\_GenericProfileExample project have been pasted into the previously existing project.
7. In the CFM\_GenericProfile project, copy these Controller Tag data tags.
8. In the other RSLogix 5000 project, paste the copied data tags into the Controller Tags folder.
9. In the CFM\_GenericProfileExample project, copy ladder logic rung 1 in the Main Routine folder.
10. In the other open RSLogix project, paste the copied rung into the Main Routine folder.
11. Accept the pasted rung.
12. Delete the empty rung.

| Name       | Value        | Force Mas   | Style   | Data Type   |
|------------|--------------|-------------|---------|-------------|
| CFM_B_C    | （...} {...} |             |         | CFM_Rev_B   |
| CFM_Config | 0            |             | Decimal | DINT        |
| CFM_IN     | {...}        | {...}       |         | CFM_I       |
| CFM_OUT    | {...}        | {...}       |         | CFM_0       |

<!-- image -->

## Specify the Configurable On/Off Behavior

1. In the previously existing program, select the Controller Tag folder and view the Monitor Tags tab.
2. Expand the CFM\_B\_C tag until you reach the CFM\_B\_C.OutputWindow data tags.
3. In the Value column of the CFM\_B\_C.OutputWindow data tags, enter the desired the On and Off frequency limits.

<!-- image -->

| Name                            | Value       | Style   | Data Type       |
|---------------------------------|-------------|---------|-----------------|
| -CFM_B_C                        | {...}       | {...}   | CFM_Rev_B       |
| CFM_B_C.ProgToFaultEn           | 0           | Decimal | BOOL            |
| -CFM_B_C.ChannelCfgBits         | 2#0000_0000 | Binary  | SINT            |
| CFM_B_C.ChOProverDirection      | 0           | Decimal | BOOL            |
| CFM_B_C.Ch1ProverDirection      | 0           | Decimal | BOOL            |
| CFM_B_C.ChOLowFreqClear         | 0           | Decimal | BOOL            |
| CFM_B_C.Ch1LowFreqClear         | 0           | Decimal | BOOL            |
| CFM_B_C.ChOPreTrigger           | 0           | Decimal | BOOL            |
| CFM_B_C.Ch1PreTrigger           | 0           | Decimal | BOOL            |
| -CFM_B_C.Operations             | {...}       | {...}   | CFM_Setup_C[2]  |
| -CFM_B_C.OutputSetup            | {...}       | (...}   | CFM_OutCfg_C[2] |
| -CFM_B_C.OutputSetup[0]         | (...}       | (...}   | CFM_OutCfg_C    |
| -CFM_B_C.OutputSetup[1]         | (...}       | {...}   | CFM_OutCfg_C    |
| -CFM_B_C.Outputwindow           | (...}       | (...}   | OUT_WIN[2]      |
| -CFM_B_C.Outputwindow[0]        | {...}       | {...}   | OUT_WIN         |
| CFM_B_C.Outputwindow[0].FreqOr  | 6000.0      | Float   | REAL            |
| CFM_B_C.Outputwindow[0].FreqOff | 4000.0      | Float   | REAL            |
| -CFM_B_C.Outputwindow[1]        | {...}       | {...}   | OUT_WIN         |
| CFM_B_C.Outputwindow[1].FreqOn  | 6000.0      | Float   | REAL            |
| CFM_B_C.Outputwindow[1].FreqOff | 4000.0      | Float   | REAL            |

See Table 5 on page 52 for more information about determining your On/ Off frequency limits.

4. Edit existing tag references throughout the project so they link to the appropriate, newly added, user-defined tags.

For example, if the tag reference is Local:5:I.Status.FreqAverage, change it to the corresponding user-defined tag, CFM\_IN.Status.FreqAverage.

IMPORTANT

Test the configuration before implementing the changes into your production process.

|                       | These terms and abbreviations are used throughout this manual. For definitions of terms not listed here, refer to the Allen-Bradley Industrial Automation Glossary, publication AG-7.1 .                                                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Broadcast             | Data transmissions to all addresses                                                                                                                                                                                                                                                                            |
| Communications format | Format that defines the type of information transferred between an I/O module and its owner controller. This format also defines the tags created for each I/O module                                                                                                                                          |
|                       | Compatible match An electronic keying protection mode that requires the physical module and the module configured in the software to match according to vendor, catalog number and major revision. In this case, the minor revision of the module must be greater than or equal to that of the configured slot |
| Connection            | The communication mechanism from the controller to another module in the control system                                                                                                                                                                                                                        |
|                       | Coordinated System Time (CST) Timer value which is kept synchronized for all modules within a single ControlLogix® backplane chassis. The CST is a 64 bit number with s resolution                                                                                                                            |
| Direct connection     | An I/O connection where the controller establishes an individual connection with I/O modules                                                                                                                                                                                                                   |
|                       | Disable keying Option that turns off all electronic keying to the module. Requires no attributes of the physical module and the module configured in the software to match                                                                                                                                     |
| Download              | The process of transferring the contents of a project on the workstation into the controller                                                                                                                                                                                                                   |
|                       | Electronic keying A system feature which makes sure that the physical module attributes are consistent with what was configured in the software                                                                                                                                                                |
| Exact match           | An electronic keying protection mode that requires the physical module and the module configured in the software to match identically, according to vendor, catalog number, major revision and minor revision                                                                                                  |
| Field side            | Interface between user field wiring and I/O module                                                                                                                                                                                                                                                             |
|                       | High Resolution Frequency Mode Operational mode in which CFM module measures incoming pulses over a user-defined time period up to 2 seconds                                                                                                                                                                   |
|                       | Inhibit A ControlLogix process that allows you to configure an I/O module but prevent it from communicating with the owner controller. In this case, the controller does not establish a connection                                                                                                            |
|                       | Listen-only connection An I/O connection that allows a controller to monitor I/O module data without owning the module                                                                                                                                                                                         |
|                       | Major revision A module revision that is updated any time there is a functional change to the module resulting in an interface change with software                                                                                                                                                            |
| Minor revision        | A module revision that is updated any time there is a change to the module that does not affect its function or software user interface (e.g. bug fix)                                                                                                                                                         |
| Multicast             | Data transmissions which reach a specific group of one or more destinations                                                                                                                                                                                                                                    |

Network update time (NUT) The smallest repetitive time interval in which the data can be sent on a ControlNet® network. The NUT can be configured over the range from 2 ms to 100 ms using RSNetWorx software

Nonresettable Totalizer Mode

Operational mode in which 1756-CFM module counts pulses from a Flowmeter and scales them into volume (engineering units). In this mode, though, the count total cannot be reset during normal module operation.

Owner controller

The controller that creates and stores the primary configuration and communication connection to a module

Producer/consumer

Intelligent data exchange system devices in which the CFM module produces data without having been polled first

Program mode

In this mode, the controller program is not executing. Inputs are actively producing data. Outputs go to their configured program mode state

Prover

Device used for the calibration of liquid meters in custody transfer applications. Calibration compares a metered throughput to a known volume in the prover.

Remote connection

An I/O connection where the controller establishes an individual connection with I/O modules in a remote chassis

Removable terminal block (RTB)

Field wiring connector for I/O modules

Removal and insertion under power (RIUP)

ControlLogix feature that allows a user to install or remove a module or RTB while power is applied

Requested packet interval (RPI) A configurable parameter which defines when the module will multicast data

Run mode In this mode, the controller program is executing Inputs are actively producing data. Outputs are actively controlled

Service A system feature that is performed on user demand

System side Backplane side of the interface to the I/O module

Tag A named area of the controller’s memory where data is stored like a variable

Totalizer Mode

Operational mode in which CFM module counts pulses from a Flowmeter and scales them into volume (engineering units).

Trickle Operational mode in which the CFM module controls two lines in a filling application, a full flow and a trickle flow. The trickle flow line provides users greater accuracy by slowly finishing thefill process.

## A

## Acceleration Alarm Value Feature

in high resolution frequency mode 31

## Acceleration Calculation Feature

in high resolution frequency mode 30

## Acceleration Feature

in high resolution frequency mode

31

with prover function in totalizer mode 38

## Accessing the Tags 72

## Alarms

in high resolution frequency mode 31

with the filler function in totalizer mode 48

with the prover function in totalizer mode 40

## Applications

Typical applications for the 1756-CFM module 11

## Assembling the RTB and housing 61

## C

## Changing Configuration During Module

Operation 75

## Communications

Producer/consumer model 27

Communications Format 66 , 69 , 137

Communications Pop-Up Screen 80

## Compatible Match

Electronic keying 137

## Configuration 65

Altering the default configuration 66 , 71

Changing at the tags 73

Changing during module operation 75

Communications pop-up screen for use with message instructions 80

Configuration pop-up screen for use with message instructions 79

Configuring CFM modules in remote chassis 81

Downloading data 74

Message instructions 76

Overview 65

Overview of the configuration process 65

Tag pop-up screen for use with message instructions 80

Using ladder logic 75

Using the default configuration 66 , 70

## Configuration Data Structure 105

Configuration Pop-Up Screen 79

## Connections 18 , 137

Connector pins on the module 10

ControlLogix backplane connector 10

Direct 137

Direct connection 18

Listen-only 18 , 137

Remote connection 138

Using the IFM 9

Using the RTB 9

Wiring the RTB 55

Wiring the standard flowmeter 57

Wiring the standard output 60

Wiring the standard prover 59

## ControlLogix Backplane Connector

## r 10

## ControlNet

Setting the Network Update Time (NUT) 17

## Coordinated System Time (CST) 137

Creating a New Tag 77

Current-Sourcing Outputs 28

## D

## Data Structures

Configuration structure Input tags 110

Output tags 112

## Data Transmissions

Choosing a communications format 69

Default Configuration 66 , 70

Digital Filter r 97

Direct Connections 137

## Disable Keying

Electronic keying 137

## Discrete Outputs

Schematics 120

## Downloading Configuration Data 74

## E

## Electronic Keying 70 , 137

Choosing in RSLogix 5000 70 Compatible match 137 Disable keying 137 Exact match 137

Error Codes

103

## Exact Match

Electronic keying 137

105

## F

## Fault Reporting 21 , 71 , 103

Error codes 103

## Features

Internal 10 , 21 Physical 10

## Fill Enable Feature

with filler function in totalizer mode 44

## Fill Hold Feature

with filler function in totalizer mode 45

## Fill Mode Feature

with filler function in totalizer mode 44

## Fill Start Feature

with filler function in totalizer mode 44

## Fill State Feature

with filler function in totalizer mode 45

## Fill Total Feature

with filler function in totalizer mode 45

## Fill Total Target Feature

with filler function in totalizer mode 48

## Fill Transition Feature

with filler function in totalizer mode 48

## Fill Transition Timer Feature

with filler function in totalizer mode 48

## Filler Function

Alarms 48

Features available 43

Fill enable feature 44

Fill hold feature 45

Fill mode feature 44

Fill start feature 44

Fill state feature 45

Fill tansition timer feature 48

Fill total feature 45

Fill total target feature 48

Fill transition feature 48

Gross volume feature 46

in totalizer mode 41

Low frequency clear feature 43

Net rate feature 48

Net volume feature 46

PreTrigger feature 43

Tie to counter feature 44

Total counts feature 46

Trigger on feature 44

## Flowmeter Inputs 27

Schematics 117

## Flowmetering Channels 27

## Frequency Average Feature

in high resolution frequency mode

31

with prover function in totalizer mode 37

## Frequency Period Feature

with prover function in totalizer mode 37

## Functions

Filler function in totalizer mode 41

Prover function in totalizer mode 33

## G

## Gate Inputs 27

Schematics 118

## Gross Rate Feature

with prover function in totalizer mode 39 , 46

## Gross Volume Feature

with filler function in totalizer mode 46

with prover function in totalizer mode 38

## Grounding the Module 55

## H

## High Resolution Frequency Mode 28 , 137

Acceleration alarm value feature 31

Acceleration calculation feature 30

Acceleration feature 31

Alarms 31

Features available 29

Frequency average feature 31

Highest allowed frequency 31

Low frequency clear feature 30

Meter factor feature 30

Output operation 29

Sample time feature 30

Terminal usage 29

Tie to counter feature 30

Trigger on feature 30

## Highest Allowed Frequency

in high resolution frequency mode 31

## I

## Indicators 27

Using to troubleshoot the module 101

## Inhibit

the module 137

## Input Tags Data Structure 110

## Inputs

Flowmeter inputs 27

Gate inputs 27 , 118

Input schematics 117

Installing the Module 52

Installing the RTB on the module 61

Interface Module (IFM) 9

## K

## Keying

Compatible match 137

Disable 137

Electronic 70 , 137

Exact match 137

Keying the module 54

Keying the RTB 54

Mechanical keying 11

## L

Ladder Logic 75

Listen-only Connection 137

Locking Tab 10

Logix5550 Controller 11 , 28 , 33

## Low Frequency Clear Feature

in high resolution frequency mode 30 with filler function in totalizer mode 43 with prover function in totalizer mode 35

## M

## Magnetic Pickup

Using 9 , 12

Major Revision 66 , 137

Mechanical Keying 11

Keying the module Keying the RTB 54

54

Message Instructions 76

## Meter Factor Feature

in high resolution frequency mode 30

Minor Revision 66 , 137

Module Features 10

## Module Identification Information 13

ASCII text string 13

Catalog code 13

Major revision 13

Minor revision 13

Product type 13

Retrieving 21

Serial number 13

Status 13

Vendor ID 13

WHO service 13

Module Input Capabilities 12

Module Operation in Remote Chassis 20

Module Output Capabilities 12

Module Status

Retrieving 13

Module Status Information 27

## N

## Net Rate Feature

with filler function in totalizer mode 48 40

with prover function in totalizer mode

## Net Volume Feature

with filler function in totalizer mode 46 38

with prover function in totalizer mode

Network Update Time (NUT) 17 , 138

Nonresettable Totalizer Mode 32 , 138

NUT 17 , 138

## O

## Operational Modes

High resolution frequency mode 12 , 28 , 137

Nonresettable totalizer

32

Nonresettable totalizer mode 138

Totalizer 32

Totalizer mode 12 , 138

## Output Tags Data Structure 112 Outputs

Current-sourcing 28

Operation in high resolution frequency mode 29

Operation in totalizer mode

32

Output schematics 120

Owner Controller 138

Ownership 16

Owner controller 138

## P

Physical Features 10

Power Requirements 52

Preamp Outputs

Using 9 , 12

Preset Values 28

PreTrigger Feature with filler function in totalizer mode 43

Producer/Consumer Communications Model 27

Program Mode 138

Programming Software

Using RSLogix 5000 to troubleshoot the module 102

## Prover Direction Feature

with prover function in totalizer mode 35

## Prover Function

Acceleration feature 38

Alarms 40

Features available 35

Frequency average feature 37

Frequency period feature 37

Gross rate feature 39 , 46

Gross volume feature 38

in totalizer mode 33

Low frequency clear feature 35

Net rate feature 40

Net volume feature 38

Prover direction feature

Prover total feature 37

Speed feature 38

Tie to counter feature 36

Total acceleration feature 37

Total counts feature 37

Total overflow feature 36

Total overrange feature 36

Total overspeed feature 37

Trigger on feature 36

## Prover Total Feature

with prover function in totalizer mode 37

35

## R

| Remote Chassis                                                                                       | Remote Chassis                                                                                       |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| CFM module operation  17 ,  20 Configuring CFM modules  81                                           | CFM module operation  17 ,  20 Configuring CFM modules  81                                           |
| Remote Connection  138                                                                               | Remote Connection  138                                                                               |
| Removable Terminal Block (RTB)  9 10 138                                                             | Removable Terminal Block (RTB)  9 10 138                                                             |
| Assembling with the housing  61                                                                      | Assembling with the housing  61                                                                      |
| Installing on the module  61                                                                         | Installing on the module  61                                                                         |
| Keying  54                                                                                           | Keying  54                                                                                           |
| Removing from the module  62                                                                         | Removing from the module  62                                                                         |
| Wiring  55 Removal and Insertion Under Power (RIUP)  21 ,  138                                       | Wiring  55 Removal and Insertion Under Power (RIUP)  21 ,  138                                       |
| Removing the Module  63 Removing the RTB from the module  62                                         | Removing the Module  63 Removing the RTB from the module  62                                         |
| Requested Packet Interval (RPI)  19 ,  138                                                           | Requested Packet Interval (RPI)  19 ,  138                                                           |
| Adjusting in RSLogix 5000  71                                                                        | Adjusting in RSLogix 5000  71                                                                        |
| Retrieving Module Identification Information  13                                                     | Retrieving Module Identification Information  13                                                     |
| Retrieving Module Status  13 Revision                                                                | Retrieving Module Status  13 Revision                                                                |
| Major                                                                                                | 137                                                                                                  |
| Minor  137 RIUP                                                                                      | Minor  137 RIUP                                                                                      |
| Removal and insertion under power  21 ,  138                                                         | Removal and insertion under power  21 ,  138                                                         |
| RPI  19 ,  138                                                                                       | RPI  19 ,  138                                                                                       |
| Adjusting in RSLogix 5000  71 RSLogix 5000                                                           | Adjusting in RSLogix 5000  71 RSLogix 5000                                                           |
| Configuring I/O modules  21 Electronic keying  70 Error codes  103                                   | Configuring I/O modules  21 Electronic keying  70 Error codes  103                                   |
| Using to troubleshoot the module  102 Using with RSNetWorx  17 RSNetworx Using with RSLogix 5000  17 | Using to troubleshoot the module  102 Using with RSNetWorx  17 RSNetworx Using with RSLogix 5000  17 |
| RTB Assembling with the housing  61 Installing on the module  61                                     | RTB Assembling with the housing  61 Installing on the module  61                                     |
| Keying  54                                                                                           | Keying  54                                                                                           |
| NEMA screw type  56                                                                                  | NEMA screw type  56                                                                                  |
| Removing from the module  62 Spring clamp type  56                                                   | Removing from the module  62 Spring clamp type  56                                                   |
| Wiring  55                                                                                           | Wiring  55                                                                                           |
| 138                                                                                                  | 138                                                                                                  |
| Run Mode                                                                                             | Run Mode                                                                                             |
| S                                                                                                    | S                                                                                                    |
| Sample Time Feature                                                                                  | Sample Time Feature                                                                                  |
| in high resolution frequency mode  30                                                                | in high resolution frequency mode  30                                                                |
| Schematics  117                                                                                      | Schematics  117                                                                                      |
| Discrete outputs  120                                                                                | Discrete outputs  120                                                                                |
| Flowmeter inputs  117                                                                                | Flowmeter inputs  117                                                                                |
| Gate inputs  118 117                                                                                 | Gate inputs  118 117                                                                                 |
| Input circuits  Output circuits  120                                                                 | Input circuits  Output circuits  120                                                                 |
| Speed Feature                                                                                        | Speed Feature                                                                                        |
| with prover function in totalizer mode  38                                                           | with prover function in totalizer mode  38                                                           |
| Standard Flowmeter                                                                                   | Standard Flowmeter                                                                                   |
| 57                                                                                                   | 57                                                                                                   |
| Wiring to the CFM module                                                                             | Wiring to the CFM module                                                                             |
| Standard Output                                                                                      | Standard Output                                                                                      |
| 60                                                                                                   | 60                                                                                                   |
| Wiring to the CFM module  59                                                                         | Wiring to the CFM module  59                                                                         |
| Standard Prover                                                                                      | Standard Prover                                                                                      |
| Wiring to the CFM module                                                                             | Wiring to the CFM module                                                                             |

## Status Indicators 11 , 27

| Using to troubleshoot the module  101                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Tag Pop-Up Screen  80 Tags Accessing  72 Changing configuration at the tags  73 Creating a new tag  77 Tie to Counter Feature                                                                                                                                                                                                                                                                                                     |
| in high resolution frequency mode  30 with filler function in totalizer mode  44 with prover function in totalizer mode  Total Acceleration Feature with prover function in totalizer mode  Total Counts Feature with filler function in totalizer mode  46 with prover function in totalizer mode  Total Overflow Feature with prover function in totalizer mode  Total Overrange Feature with prover function in totalizer mode |
| 37                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 36 37                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 36                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 36 Total Overspeed Feature                                                                                                                                                                                                                                                                                                                                                                                                        |
| with prover function in totalizer mode  37                                                                                                                                                                                                                                                                                                                                                                                        |
| Totalizer Mode  12 ,  32 ,  138 Filler function  41                                                                                                                                                                                                                                                                                                                                                                               |
| Output operation  32 Prover function  33 Terminal usage  32                                                                                                                                                                                                                                                                                                                                                                       |
| Trickle feature  42                                                                                                                                                                                                                                                                                                                                                                                                               |
| Trickle Feature  138                                                                                                                                                                                                                                                                                                                                                                                                              |
| for filler function in totalizer mode  Trigger On Feature                                                                                                                                                                                                                                                                                                                                                                         |
| 42 in high resolution frequency mode  30                                                                                                                                                                                                                                                                                                                                                                                          |
| with filler function in totalizer mode  44                                                                                                                                                                                                                                                                                                                                                                                        |
| with prover function in totalizer mode  36                                                                                                                                                                                                                                                                                                                                                                                        |
| Troubleshooting                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Module status indicators  11 Using RSLogix 5000  102 101                                                                                                                                                                                                                                                                                                                                                                          |
| Using status indicators  101                                                                                                                                                                                                                                                                                                                                                                                                      |
| Troubleshooting the Module                                                                                                                                                                                                                                                                                                                                                                                                        |
| TTL Outputs                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 9 12                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Using  ,                                                                                                                                                                                                                                                                                                                                                                                                                          |
| W                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| the NEMA screw RTB  56                                                                                                                                                                                                                                                                                                                                                                                                            |
| the spring clamp RTB  56 Wiring the RTB  55                                                                                                                                                                                                                                                                                                                                                                                       |
| Wiring the Standard Flowmeter  57                                                                                                                                                                                                                                                                                                                                                                                                 |
| 60                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Wiring                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Wiring the Standard Output                                                                                                                                                                                                                                                                                                                                                                                                        |
| Typical 1756-CFM Applications  11                                                                                                                                                                                                                                                                                                                                                                                                 |

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, and product notification updates.           | rok.auto/support       |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------|
| Knowledgebase                                    | Access Knowledgebase articles.                                                                     | rok.auto/knowledgebase |
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.                                                      | rok.auto/phonesupport  |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.               | rok.auto/literature    |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes. | rok.auto/pcdc          |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Allen-Bradley, ControlLogix, expanding human possibility, FactoryTalk, Logix5550, Rockwell Automation, RSLogix 5000, RSNetWorx, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

ControlNet and EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000,Fax:（1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASlAPACIFIC:RockwellAutomation,Level14,CoreF,Cyberport3,100CyberportRoad,HongKong,Tel:(852)28874788,Fax:(852)25081846