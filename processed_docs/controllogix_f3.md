<!-- image -->

## Logix 5000 Controllers Design Considerations

ControlLogix, GuardLogix, CompactLogix, Compact GuardLogix

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

|                           | Preface                                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                           | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9       |
|                           | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9         |
|                           | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10        |
|                           | Chapter 1                                                                                                                                  |
| 5590 Controllers          | ControlLogix 5590 Controllers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11              |
|                           | XT Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12  |
|                           | Process Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12       |
|                           | Controller Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12       |
|                           | Data Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 |
|                           | Extended Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13                 |
|                           | Date and Time Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13                    |
|                           | Programming Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15              |
|                           | Data Alignment Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                |
|                           | Produced and Consumed Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                  |
|                           | Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15  |
|                           | Chapter 2                                                                                                                                  |
| 5580 and 5380 Controllers | ControlLogix 5580 and GuardLogix 5580 Controllers. . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                                |
|                           | CompactLogix 5380 and Compact GuardLogix 5380 Controllers . . . . . . . . . . . . . . . . . . 18                                           |
|                           | Process Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19       |
|                           | Controller Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19       |
|                           | Data Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 |
|                           | Extended Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                 |
|                           | Date and Time Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                    |
|                           | Programming Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22              |
|                           | Data Alignment Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                |
|                           | Produced and Consumed Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                  |
|                           | Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22  |
|                           | Chapter 3                                                                                                                                  |
| 5480 Controllers          | CompactLogix 5480 Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                 |
|                           | Controller Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24       |
|                           | Data Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 |
|                           | Extended Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                 |
|                           | Date and Time Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                    |
|                           | Programming Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27              |
|                           | Data Alignment Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                |
|                           | Produced and Consumed Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                  |
|                           | Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27  |

Chapter 4

| 5570 Controllers and 5370   | ControlLogix 5570 and GuardLogix 5570 Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Controllers                 | CompactLogix 5370 and Compact GuardLogix 5370 Controllers . . . . . . . . . . . . . . . . . . 30                                            |
|                             | Controller Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31        |
|                             | CompactLogix 5370 and Compact GuardLogix 5370 Controllers . . . . . . . . . . . . . . 31                                                    |
|                             | Controller Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32          |
|                             | Determine Total Connection Requirements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                                   |
|                             | System Overhead Percentage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34                 |
|                             | Manage the System Overhead Timeslice Percentage. . . . . . . . . . . . . . . . . . . . . . . . 35                                           |
|                             | I/O Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36    |
|                             | Data Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37  |
|                             | Programming Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37               |
|                             | Produced and Consumed Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38                   |
|                             | Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 |
|                             | Chapter 5                                                                                                                                   |
| Logic Execution             | Decide When to Use Tasks, Programs, and Routines. . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                                  |
|                             | Specify Task Priorities. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40         |
|                             | Manage User Tasks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41         |
|                             | Pre-defined Tasks in ControlLogix and CompactLogix Process Controllers . . . . . 41                                                         |
|                             | Considerations that Affect Task Execution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42                         |
|                             | Configure a Periodic Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43            |
|                             | Configure an Event Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43            |
|                             | Guidelines to Configure an Event Task. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43                             |
|                             | Additional Considerations for Periodic and Event Tasks . . . . . . . . . . . . . . . . . . . . . 43                                         |
|                             | Configure a Continuous Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44                |
|                             | Access the Module Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44             |
|                             | Develop Application Code in Routines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45                     |
|                             | Comparison of Programming Languages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45                                    |
|                             | Programming Methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46             |
|                             | Inline Duplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46             |
|                             | Indexed Routine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46              |
|                             | Buffered Routine. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46              |
|                             | Controller Prescan of Logic. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47             |
|                             | Add-On Instruction Prescan Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                           |
|                             | Custom Tag Initialization During Prescan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                               |
|                             | Controller Postscan of SFC Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                 |
|                             | Add-On Instruction Postscan Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                            |
|                             | Edit an SFC Online. . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . . 51   |
|                             | SFC Step Timer Execution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                     |

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

|                              | Chapter 6                                                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Modular Programming          | Guidelines for Code Reuse. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53            |
| Techniques                   | Naming Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54          |
|                              | Parameter Name Prefixes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56             |
|                              | Guidelines for Program Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                    |
|                              | Comparison of Program Parameters and Add-On Instructions. . . . . . . . . . . . . . . . 59                                                 |
|                              | Guidelines for Subroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59            |
|                              | Guidelines for User-defined Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60                      |
|                              | Naming Conventions for User-Defined Data Types . . . . . . . . . . . . . . . . . . . . . . . . . 60                                        |
|                              | UDT Member Order Impact. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60                      |
|                              | Guidelines for Add-On Instructions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                 |
|                              | Add-On Instruction Design Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                            |
|                              | Naming Conventions for Add-On Instructions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                                   |
|                              | Comparison of Subroutines and Add-On Instructions . . . . . . . . . . . . . . . . . . . . . . . 64                                         |
|                              | Comparison of Partial Import/Export and Add-On Instructions . . . . . . . . . . . . . . . 65                                               |
|                              | Compare Controller Organizer and Logical Organizer . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                                |
|                              | Chapter 7                                                                                                                                  |
| Structure Logic According to | Physical Model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68   |
| Standards                    | Separate a Process Unit into Equipment Modules and Control Modules . . . . . . . . 70                                                      |
|                              | Physical Model Naming Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                             |
|                              | Procedural Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72      |
|                              | Identify Operations and Phases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                        |
|                              | Procedural Control Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74            |
|                              | Procedural Control States . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75           |
|                              | Procedural Control Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                 |
|                              | Procedural Model Naming Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                               |
|                              | State Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 |
|                              | Chapter 8                                                                                                                                  |
| Produced and Consumed Data   | Guidelines for Produced and Consumed Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                             |
|                              | Guidelines for Produced and Consumed Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                             |
|                              | Guidelines to Specify an RPI Rate for Produced and Consumed Tags . . . . . . . . . . . . . 80                                              |
|                              | Guidelines to Manage Connections for Produced and Consumed Tags. . . . . . . . . . . . . 81                                                |
|                              | Configure an Event Task Based on a Consumed Tag. . . . . . . . . . . . . . . . . . . . . . . . . . . . 81                                  |

## Chapter 9

| Data Structures      |                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Guidelines for Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                |
|                      | Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84 |
|                      | Guidelines for Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85            |
|                      | Indirect Addresses of Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                 |
|                      | Guidelines for Array Indexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87                 |
|                      | Guidelines for User-defined Data Types (UDT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87                               |
|                      | Select a Data Type for Bit Tags. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                   |
|                      | Serial Bit Addresses . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 89         |
|                      | Guidelines for String Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                     |
|                      | Configure Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90         |
|                      | Guidelines for Base Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91               |
|                      | Create Alias Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91          |
|                      | Guidelines for Data Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                |
|                      | Guidelines for Tag Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                 |
|                      | Guidelines for Extended Tag Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                           |
|                      | Tag Descriptions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93          |
|                      | Protect Data Access Control at Tag Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                           |
|                      | Chapter 10                                                                                                                                      |
| Communicate with I/O | Buffer I/O Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95        |
|                      | Guidelines to Specify an RPI Rate for I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                |
|                      | Communication Formats for I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                              |
|                      | Direct Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                  |
|                      | Rack-optimized Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                            |
|                      | Peer Control. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98              |
|                      | Electronic Keying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99          |
|                      | More Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                  |
|                      | Guidelines to Manage I/O Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100                           |
|                      | Create Tags for I/O Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101                |
|                      | Controller Ownership . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102              |
|                      | Runtime/Online Addition of Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                          |
|                      | Online Addition of Module and Connection Types . . . . . . . . . . . . . . . . . . . . . . . . . . 104                                          |
|                      | Design Considerations for Runtime/Online Addition of Modules. . . . . . . . . . . . . . 105                                                     |

Chapter 11

| Determine the Appropriate       | EtherNet/IP Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                 |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Network                         | Guidelines for EtherNet/IP Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                    |
|                                 | ControlNet Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                |
|                                 | Guidelines for ControlNet Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                   |
|                                 | Guidelines for Unscheduled ControlNet Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                             |
|                                 | Compare Scheduled and Unscheduled ControlNet Communication. . . . . . . . . . . . . . . 112                                                |
|                                 | DeviceNet Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113                 |
|                                 | Guidelines for DeviceNet Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113                    |
|                                 | Chapter 12                                                                                                                                 |
| Communicate with Other          | Cache Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115       |
| Devices                         | Message Buffers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116      |
|                                 | Outgoing Unconnected Buffers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117                         |
|                                 | Guidelines for Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117            |
|                                 | Guidelines to Manage Message Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117                            |
|                                 | Guidelines for Block Transfer Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                       |
|                                 | Map Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118 |
|                                 | Chapter 13                                                                                                                                 |
| Alarms                          | Guidelines for Tag-Based Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119                  |
|                                 | Access Tag-based Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120                      |
|                                 | Guidelines for Instruction-based Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                      |
|                                 | Configure Logix-based Alarm Instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122                         |
|                                 | Automatic Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123          |
|                                 | Chapter 14                                                                                                                                 |
| Optimize an Application for Use | Linx-based Software Use of Controller Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125                             |
| with HMI                        | HMI Implementation Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125               |
|                                 | Guidelines for FactoryTalk View Software. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                        |
|                                 | How a Data Server Communicates with the Controllers . . . . . . . . . . . . . . . . . . . . . . . . 126                                    |
|                                 | Compare RSLinx Classic and FactoryTalk Linx Software. . . . . . . . . . . . . . . . . . . . . . . . 127                                    |
|                                 | Guidelines for Linx-based Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128                   |
|                                 | Guidelines to Configure Controller Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128                      |
|                                 | Reference Controller Data from FactoryTalk View Software. . . . . . . . . . . . . . . . . 128                                              |

|                          | Chapter 15                                                                                                                          |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Develop Equipment Phases | Guidelines for Equipment Phases. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129            |
|                          | Equipment Phase Instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130          |
|                          | Chapter 16                                                                                                                          |
| Manage Firmware          | Guidelines to Manage Controller Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                  |
|                          | Compare Firmware Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132         |
|                          | Guidelines for the Firmware Supervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132                |
|                          | Access Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 |
|                          | Index                                                                                                                               |

## About This Publication

## Summary of Changes

This publication provides information to help design and plan Logix 5000™ systems.

Throughout this publication, programming software refers to the following:

- Studio 5000 Logix Designer® application, version 21 or later
- RSLogix 5000® software, version 16 or later

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes. Change bars indicate where information is new or has been updated.

| Topic                                                                                                                                                                                                       | Page   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Added resources to the Additional Resources                                                                                                                                                                 | 10     |
| Added a chapter for the ControlLogix 5590 controllers                                                                                                                                                       | 11     |
| Updated the data value that CompactLogix 5380, Compact GuardLogix 5380, ControlLogix 5580, and GuardLogix 5580 controllers’ CPU reads and manipulates from 32-bit to 64-bit                                 | 20     |
| Added to the list of instructions that support absolute and relative time data types with CompactLogix 5380, Compact GuardLogix 5380, ControlLogix 5580, and GuardLogix 5580 controllers                    | 21     |
| Updated the number of Add-On Instructions that you can nest with CompactLogix 5380, Compact GuardLogix 5380, ControlLogix 5580, and GuardLogix 5580 controllers based on Logix Designer application version | 22     |
| Updated the Logix Designer version support levels for CompactLogix 5480 controllers                                                                                                                         | 23     |
| Added to the list of instructions that support absolute and relative time data types with CompactLogix 5480 controllers                                                                                     | 26     |
| Updated the number of Add-On Instructions that you can nest with CompactLogix 5480 controllers based on Logix Designer application version                                                                  | 27     |
| Add to the list of considerations when you decide to use a routine in Logic Execution                                                                                                                       | 39     |
| Updated the timer execution description                                                                                                                                                                     | 50     |
| Added information about methods of comparing Produced/Consumed tags                                                                                                                                         | 81     |
| Updated the guidelines for data types                                                                                                                                                                       | 83     |
| Updated the guidelines for array indexes                                                                                                                                                                    | 87     |
| Changed Buffer Name Outgoing, connected to Outgoing, unconnected in the Message Buffers 116                                                                                                                 |        |
| Added ControlLogix 5590 controllers to the list of controllers Automatic Diagnostics                                                                                                                        | 123    |
| Updated information about using Linx-based software with Studio 5000 Logix Designer software                                                                                                                | 127    |
| Added recommendation that you use the ControlFLASH Plus tool whenever possible to manage firmware for devices in your application                                                                           | 131    |
| Added information about the ControlLogix 5590 controller memory card in the guidelines for the Firmware Supervisor feature                                                                                  | 133    |

<!-- image -->

<!-- image -->

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

| Resource                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| • EtherNet/IP Network Devices User Manual, publication ENET-UM006 • ControlNet Network Configuration User Manual publication CNET-UM001 • DeviceNet Network Configuration User Manual, publication DNET-UM004                                                                                                                                                                                              | EtheNet/IP™, ControlNet®, and DeviceNet® networks                                                                                                                                                                                                                               |
| • System Security Design Guidelines Reference Manual, SECURE-RM001 • Configure System Security Features User Manual, SECURE-UM001 • CIP Security with Rockwell Automation Products Application Technique, SECURE-AT001                                                                                                                                                                                     | System security and CIP Security™                                                                                                                                                                                                                                               |
| • High Availability System Reference Manual, publication HIGHAV-RM002                                                                                                                                                                                                                                                                                                                                      | High availability systems • ControlLogix 5590 High Availability Systems User Manual, publication                                                                                                                                                                                |
| • GuardLogix 5580 and Compact GuardLogix 5380 Controller Systems Reference Manual, publication 1756-RM012                                                                                                                                                                                                                                                                                                  | Safety systems                                                                                                                                                                                                                                                                  |
| • Replacement Guidelines: Logix 5000 Controllers Reference Manual, publication 1756-RM100 • Logix 5000 Common Procedures Programming Manual, publication 1756- PM001                                                                                                                                                                                                                                       | Logix 5000™ controllers                                                                                                                                                                                                                                                         |
| • ControlLogix 5590 Controllers User Manual, publication 1756-UM900 • ControlLogix 5580 and GuardLogix 5580 Controllers User Manual, publication 1756-UM543 • ControlLogix System User Manual, publication 1756-UM001 • SERCOS and Analog Motion Configuration and Startup User Manual, publication MOTION-UM001 • Motion Coordinate System User Manual, publication MOTION-UM002                          | ControlLogix® and GuardLogix® controllers                                                                                                                                                                                                                                       |
| • CompactLogix 5370 Controllers User Manual, publication 1769-UM021 • CompactLogix 5380 and Compact GuardLogix 5380 Controllers User Manual, publication 5069-UM001 • 1768 CompactLogix Controllers User Manual, publication 1768-UM001 • 1769 CompactLogix Controllers User Manual, publication 1769-UM011 • 1769 Packaged CompactLogix Controllers Quick Start and User Manual, publication IASIMP-QS010 | CompactLogix™ and Compact GuardLogix controllers                                                                                                                                                                                                                                |
| Technical Documentation Center, rok.auto/techdocs                                                                                                                                                                                                                                                                                                                                                          | Quickly access and download technical specifications, installation instructions, and user manuals.                                                                                                                                                                              |
| Safety Guidelines for the Application, installation, and Maintenance of Solid state Control, publication SGI-1.1                                                                                                                                                                                                                                                                                                                                                                                                            | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                                                                                                                                                                                                                                                                                                                | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Selection and Configuration tools, rok.auto/systemtools                                                                                                                                                                                                                                                                                                                                            | Helps configure complete, valid catalog numbers and build complete quotes based on detailed product information.                                                                                                                                                                |
| Product Certifications website, rok.auto/certifications                                                                                                                                                                                                                                                                                                                                                    | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

## ControlLogix 5590 Controllers

| Characteristic                   | ControlLogix 5590 Controllers                                                                                                                                     | ControlLogix 5590 Controllers                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Controller tasks                 | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                            | 32, including continuous, periodic, and event tasks 1000 programs/task                 |
| Event tasks                      | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                                                            | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events |
|                                  | 1756-L902TS, 1756-L902TSXT 2 MB standard + 2 MB safety                                                                                                            |                                                                                        |
|                                  | 1756-L905TS, 1756-L905TSXT, 1756-L905TPSXT 5 MB standard + 5 MB safety                                                                                            |                                                                                        |
|                                  | 1756-L908TS, 1756-L908TSXT 8 MB standard + 8 MB safety                                                                                                            |                                                                                        |
| User memory                      | 1756-L915TS, 1756-L915TSXT, 1756-L915TPSXT                                                                                                                        | 15 MB standard + 12 MB safety                                                          |
|                                  | 1756-L925TS, 1756-L925TSXT                                                                                                                                        | 25 MB standard + 12 MB safety                                                          |
|                                  | 1756-L950TS, 1756-L950TSXT, 1756-L950TPSXT                                                                                                                        | 50 MB standard + 12 MB safety                                                          |
|                                  | 1756-L980TS, 1756-L980TSXT, 1756-L980TPSXT                                                                                                                        | 80 MB standard + 12 MB safety                                                          |
| Built-in ports                   | 1 port USB (1) 2 Embedded Ethernet ports                                                                                                                          |                                                                                        |
| USB port communication           | USB 2.0 Type-C (does not support powering external devices) Full speed (12 Mbps) Programming, configuration, firmware update, and online edits only               |                                                                                        |
| Ethernet performance             | 10/100/1000 Mbps                                                                                                                                                  |                                                                                        |
| Communication options            | EtherNet/IP™ is the preferred network The controller also supports these networks: • ControlNet® • DeviceNet® • SERCOS • Third-party process and device networks. |                                                                                        |
|                                  | 1756-L902TS, 1756-L902TSXT                                                                                                                                        | 30                                                                                     |
|                                  | 1756-L905TS, 1756-L905TSXT, 1756-L905TPSXT                                                                                                                        | 100                                                                                    |
|                                  | 1756-L908TS, 1756-L908TSXT                                                                                                                                        | 200                                                                                    |
| EtherNet/IP nodes supported, max | 1756-L915TS, 1756-L915TSXT, 1756-L915TPSXT                                                                                                                        | 300                                                                                    |
|                                  | 1756-L925TS, 1756-L925TSXT                                                                                                                                        | 400                                                                                    |
|                                  | 1756-L950TS, 1756-L950TSXT, 1756-L950TPSXT                                                                                                                        | 500                                                                                    |
|                                  | 1756-L980TS, 1756-L980TSXT, 1756-L980TPSXT                                                                                                                        | 600(2)                                                                                 |
| Controller redundancy            | Fully supported                                                                                                                                                   |                                                                                        |
| Integrated motion                | Integrated Motion on the EtherNet/IP network SERCOS interface Analog options (encoder input, LDT input, SSI input)                                                |                                                                                        |

## 5590 Controllers

This chapter highlights these controllers.

| Controller Family Controller Names              |
|-------------------------------------------------|
| 5590 controllers ControlLogix® 5590 controllers |

<!-- image -->

## XT Controllers

## Process Controllers

## Controller Memory

## Data Types

The ControlLogix-XT™ 5590 controllers function in the same way and have the same features as standard ControlLogix 5590 controllers. You can enable these controllers for safety and redundancy. When you create a Logix Designer project for these controllers, you must choose a specific catalog number for XT controllers.

The ControlLogix-XT 5590 process controllers focus on plant-wide process control. The process controller comes configured with a default process tasking model and dedicated PlantPAx® process instructions optimized for process applications and to improve design and deployment efforts. You can enable these controllers for safety and redundancy.

For more information on the process library, see the Rockwell Automation Library of Process Objects Reference Manual, publication PROCES-RM200 .

For more information on process controller application guidelines, see the PlantPAx DCS Configuration and Implementation User Manual, publication PROCES-UM100 .

The Logix CPU on 5590 controllers works the same as in the 5580 controllers. For a description of how controller memory is used with a controller operating in a standard or safety application, see Controller Memory on page 19 .

The controllers support the following data types:

- Numerous IEC 61131-3 elementary data types
- Compound data types
- Arrays
- Predefined structures, such as counters and timers
- User-defined structures

The Logix CPU reads and manipulates 64-bit data values. The minimum memory allocation for data in a tag is 4 bytes. When you create a standalone tag that stores data that is less than 4 bytes, the controller allocates 4 bytes, but the data only fills the part that it needs.

For more information See Data Structures on page 83 .

| Data Type   | Bits                                          | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        |
|-------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Data Type   | 64…32 31 16 15 8 7 1 0                        |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| BOOL        | Not allocated                                 | Allocated but not used                                                                                      | Allocated but not used                                                                                      | 0 or 1                                                                                                      | Allocated but not used                                                                                      | Allocated but not used                                                                                      |                                                                                                             |
| SINT        | Not allocated                                 | Allocated but not used                                                                                      | -128…+127                                                                                                   | -128…+127                                                                                                   | Allocated but not used                                                                                      |                                                                                                             |                                                                                                             |
| INT         | Not allocated                                 | Allocated but not used -32,768…32,767                                                                       | Allocated but not used -32,768…32,767                                                                       |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| DINT        |                                               | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  |
| REAL        | Not allocated                                 | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) |
|             | LINT -922337203685477580…+9223372036854775807 | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               |

## Extended Data Types

The 5590 controllers support these extended data types:

| Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 64…32 31 16 15 8 7…1 0                                                                                                                  |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | USINT Not allocated Allocated but not used                                                                                              | USINT Not allocated Allocated but not used                                                                                              | Unsigned 0…255                                                                                                                          | Unsigned 0…255                                                                                                                          |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | UINT Not allocated Allocated but not used                                                                                               | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            |
| ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             |
| -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) |

The compute, compare, and math instructions support these extended data types for 64-bit operations.

## Date and Time Data Types

The 5590 controllers support date and time data types to standardize date and time values in instructions. Standardized values increase the accuracy and reliability of time-stamped inputs, scheduled outputs, and time-based registration for motion control. These data types are also helpful for sequence of events, time-stamped data logging and analytics, and time synchronization within and across systems.

|                                                               | Data Type Description                                                                       | Literal String Format                                     |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Absolute time data types—Use for specific points in time.     | Absolute time data types—Use for specific points in time.                                   | Absolute time data types—Use for specific points in time. |
|                                                               | DT Date and time. 64-bit storage; units are in microseconds. DT#2020-03-05-08:11:44.345_678 |                                                           |
| LDT                                                           | Long date and time. 64-bit storage; units are in nanoseconds.                               | LDT#2020-10-25-11:05:20.123_456_789                       |
| Relative time data types—Use for duration or lengths of time. | Relative time data types—Use for duration or lengths of time.                               | Literal String Display Format                             |
| TIME32                                                        | Duration of time. 32-bit storage; units are in microseconds.                                | T32#2d_3h_1m_22s_123ms_678us                              |
| TIME                                                          | Duration of time. 64-bit storage; units are in microseconds.                                | T#5d_8h_5m_33s_234ms_679us                                |
| LTIME                                                         | Long duration of time. 64-bit storage; units are in nanoseconds.                            | LT#3d_10h_18m_47s_123ms_456us_789ns                       |

The following instructions support absolute and relative time data types:

- Add (ADD)
- AOI parameters
- Equal To (EQ)
- Clear (CLR)
- Copy (COP) - In Logix Designer, version 38 and greater, only supports the DT data type.

· Greater Than or Equal To (GE)

- Greater Than (GT)
- Get System Value (GSV) and Set System Value (SSV)
- Jump to Subroutine (JSR)
- Less Than or Equal To (LE)
- Less Than (LT)
- Move (MOV)
- Not Equal To (NE)
- Return (RET)
- Subroutine (SBR)
- Subtract (SUB)

You can use the Date and Time Browser dialog box to set a value for any of the date and time data types. To access the Date and Time Browser dialog box from the Logix Designer application:

1. Create a tag and set the data type to TIME32, TIME, LTIME, DT, or LDT.
2. Select the Monitor Tags tab.
3. Set the Style to an appropriate format for that type.
4. Click the Value field and click the … button.

<!-- image -->

## Programming Techniques

## Produced and Consumed Data

## Connections

| Programming Technique Consideration   |                                                                                                                         |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Subroutines                           | • JSR calls are limited to 40 input parameters and 40 output parameters. • There is a maximum of 25 JSR nesting levels. |
| Add-On Instructions                   | You can nest Add-On Instructions up to 16 levels.                                                                       |

For more information, see Modular Programming Techniques on page 53 .

## Data Alignment Rules

The 5590 controllers have these data alignment rules on UDTs:

- 8-byte (64-bit) data types (LINT, ULINT, LREAL, TIME, LTIME, DT, and LDT) are placed on 8-byte address boundaries in RAM. The Studio 5000 Logix Designer® application manages this requirement automatically.
- UDTs that have no 8-byte elements retain the existing 4-byte memory allocation rules.
- UDTs that contain 8-byte data types are considered 8-byte data types with a size that is a multiple of 8 bytes.
- 8-byte data types within a UDT are aligned on an 8-byte boundary.

## The controller supports:

- Total number of produced tags ≤ 255
- Maximum number of multicast produce tags out of the Ethernet port ≤ 32
- Maximum number of consumed tags ≤ 255

For more information See Produced and Consumed Data on page 79 .

## The controller supports:

- Dedicated Class 1 (I/O, Produce and Consume) connection pool to support controller node count
- Dedicated Class 3 (HMI, message instructions) connection pool to support up to 768 connections
- This pool is split; 384 incoming and 384 outgoing connections
- 384 concurrent cached MSG connections
- 512 unconnected buffers to establish connections
- This value is fixed and cannot be increased with a CIP Generic message instruction.

## Notes:

## ControlLogix 5580 and GuardLogix 5580 Controllers

| Characteristic         | ControlLogix 5580 and GuardLogix 5580 Controllers                                                                                                                                              | ControlLogix 5580 and GuardLogix 5580 Controllers                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Controller tasks       | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                                                         | 32, including continuous, periodic, and event tasks 1000 programs/task                             |
| Event tasks            | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                                                                                         | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events             |
| User memory            | 1756-L81E, 1756-L81EK, 1756-L81E-NSE, 1756-L81EXT, 1756-L81EP 3 MB standard                                                                                                                    |                                                                                                    |
| User memory            | 1756-L82E, 1756-L82EK, 1756-L82E-NSE, 1756-L82EXT 5 MB standard                                                                                                                                |                                                                                                    |
| User memory            | 1756-L83E, 1756-L83EK, 1756-L83E-NSE, 1756-L83EXT, 1756-L83EP 10 MB standard                                                                                                                   |                                                                                                    |
| User memory            | 1756-L84E, 1756-L84EK, 1756-L84E-NSE, 1756-L84EXT 20 MB standard                                                                                                                               |                                                                                                    |
| User memory            | 1756-L85E, 1756-L85EK, 1756-L85E-NSE, 1756-L85EXT, 1756-L85EP 40 MB standard                                                                                                                   |                                                                                                    |
| User memory            | 1756-L81ES, 1756-L81ESK, 1756-L81EXTS                                                                                                                                                          | 3 MB standard + 1.5 MB safety                                                                      |
| User memory            | 1756-L82ES, 1756-L82ESK, 1756-L82EXTS                                                                                                                                                          | 5 MB standard + 2.5 MB safety                                                                      |
| User memory            | 1756-L83ES, 1756-L83ESK, 1756-L83EXTS                                                                                                                                                          | 10 MB standard + 5 MB safety                                                                       |
| User memory            | 1756-L84ES, 1756-L84ESK, 1756-L84EXTS                                                                                                                                                          | 20 MB standard + 6 MB safety                                                                       |
| User memory            | 1756-L85ES                                                                                                                                                                                     | 40 MB standard + 3 MB safety                                                                       |
| Built-in ports         | One USB port (1) One Embedded Ethernet port                                                                                                                                                    | One USB port (1) One Embedded Ethernet port                                                        |
| USB port communication | USB 2.0 Full speed (12 Mbps) Programming, configuration, firmware update, and online edits only                                                                                                | USB 2.0 Full speed (12 Mbps) Programming, configuration, firmware update, and online edits only    |
| Ethernet performance   | 10/100/1000 Mbps                                                                                                                                                                               | 10/100/1000 Mbps                                                                                   |
| Communication options  | • EtherNet/IP™ • ControlNet® • DeviceNet® • DH Plus™ • Remote I/O • SynchLink™ (ControlLogix only)                                                                                             | • EtherNet/IP™ • ControlNet® • DeviceNet® • DH Plus™ • Remote I/O • SynchLink™ (ControlLogix only) |
| Network nodes          | Studio 5000 Logix Designer® application, version 30 or later                                                                                                                                   |                                                                                                    |
| Network nodes          | 1756-L81E, 1756-L81EK, 1756-L81E-NSE, 1756-L81EXT, 1756-L81EP, 1756-L81ES, 1756-L81ESK, 1756-L81EXTS 100                                                                                       |                                                                                                    |
| Network nodes          | 1756-L82E, 1756-L82EK, 1756-L82E-NSE, 1756-L82EXT, 1756-L82ES, 1756-L82ESK, 1756-L82EXTS 175                                                                                                   |                                                                                                    |
| Network nodes          | 1756-L83E, 1756-L83EK, 1756-L83E-NSE, 1756-L83EXT, 1756-L83EP, 1756-L83ES, 1756-L83ESK, 1756-L83EXTS, 1756-L84E, 1756-L84EK, 1756-L84E-NSE, 1756-L84EXT, 1756-L84ES, 1756-L84ESK, 1756-L84EXTS | 250                                                                                                |
| Network nodes          | 1756-L85E, 1756-L85EK, 1756-L85E-NSE, 1756-L85EXT, 1756-L85EP, 1756-L85ES                                                                                                                      | 300(2)                                                                                             |

## 5580 and 5380 Controllers

This chapter highlights these controllers.

| Controller Family Controller Names                                          |
|-----------------------------------------------------------------------------|
| 5580 controllers ControlLogix® 5580 and GuardLogix® 5580 controllers        |
| 5380 controllers CompactLogix® 5380 and Compact GuardLogix 5380 controllers |

<!-- image -->

| Characteristic        | ControlLogix 5580 and GuardLogix 5580 Controllers                                                                                                                                                                                                                                             |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller redundancy | Fully supported with Studio 5000 Logix Designer application version 33 later for ControlLogix 5580 controllers. Uses the same firmware revision as standard ControlLogix 5580 controllers, but requires that redundancy is enabled on the Redundancy tab of the Controller Properties dialog. |
| Integrated motion     | EtherNet/IP                                                                                                                                                                                                                                                                                   |

- (1) The USB port is intended for temporary local programming purposes only and not intended for permanent connection. Do not use the USB port in hazardous locations.

(2) This is the recommended maximum. Additional EtherNet/IP nodes may be possible depending on remaining controller resources.

## CompactLogix 5380 and Compact GuardLogix 5380 Controllers

| Characteristic        | CompactLogix 5380 Controllers and Compact GuardLogix 5380 Controllers                                                 | CompactLogix 5380 Controllers and Compact GuardLogix 5380 Controllers                  |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Controller tasks      | 32, including continuous, periodic, and event tasks 1000 programs/task                                                | 32, including continuous, periodic, and event tasks 1000 programs/task                 |
| Event tasks           | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events |
|                       | 5069-L306ER, 5069-L306ERM 0.6 MB standard                                                                             |                                                                                        |
|                       | 5069-L310ER, 5069-L310ER-NSE, 5069-L310ERM 1 MB standard                                                              |                                                                                        |
|                       | 5069-L320ER, 5069-L320ERM, 5069-L320ERMK, 5069-L320ERP 2 MB standard                                                  |                                                                                        |
|                       | 5069-L330ER, 5069-L330ERM, 5069-L330ERMK 3 MB standard                                                                |                                                                                        |
|                       | 5069-L340ER, 5069-L340ERM, 5069-L340ERP 4 MB standard                                                                 |                                                                                        |
|                       | 5069-L350ERM, 5069-L320ERMK 5 MB standard                                                                             |                                                                                        |
|                       |                                                                                                                       | 5069-L380ERM 8 MB standard                                                             |
|                       | 5069-L3100ERM 10 MB standard                                                                                          |                                                                                        |
|                       | 5069-L306ERS2, 5069-L306ERMS2                                                                                         | 0.6 MB standard + 0.3 MB safety                                                        |
| User memory           | 5069-L310ERS2, 5069-L310ERMS2                                                                                         | 1 MB standard + 0.5 MB safety                                                          |
|                       | 5069-L320ERS2, 5069-L320ERMS2, 5069-L320ERS2K, 5069-L320ERMS2K                                                        | 2 MB standard + 1 MB safety                                                            |
|                       | 5069-L330ERS2, 5069-L330ERMS2, 5069-L330ERS2K, 5069-L330ERMS2K                                                        | 3 MB standard + 1.5 MB safety                                                          |
|                       | 5069-L340ERS2, 5069-L340ERMS2                                                                                         | 4 MB standard + 2 MB safety                                                            |
|                       | 5069-L350ERS2, 5069-L350ERMS2, 5069-L350ERS2K, 5069-L350ERMS2K                                                        | 5 MB standard + 2.5 MB safety                                                          |
|                       | 5069-L380ERS2, 5069-L380ERMS2                                                                                         | 8 MB standard + 4 MB safety                                                            |
|                       | 5069-L3100ERS2, 5069-L3100ERMS2                                                                                       | 10 MB standard + 5 MB safety                                                           |
| Built-in ports        | 1 - port USB 2 - Embedded Ethernet ports                                                                              | 1 - port USB 2 - Embedded Ethernet ports                                               |
| Ethernet performance  | 10/100/1000 Mpbs                                                                                                      | 10/100/1000 Mpbs                                                                       |
| Communication options | EtherNet/IP USB                                                                                                       | EtherNet/IP USB                                                                        |
|                       | Studio 5000 Logix Designer application, version 31or later                                                            | Studio 5000 Logix Designer application, version 31or later                             |
|                       | 5069-L306ER, 5069-L306ERM, 5069-L306ERS2, 5069-L306ERMS2                                                              | 16                                                                                     |
|                       | 5069-L310ER, 5069-L310ER-NSE, 5069-L310ERM, 5069-L310ERS2, 5069-L310ERMS2                                             | 24                                                                                     |
|                       | 5069-L320ER, 5069-L320ERM, 5069-L320ERMK, 5069-L320ERP, 5069-L320ERS2, 5069-L320ERMS2 5069-L320ERS2K, 5069-L320ERMS2K | 40                                                                                     |
| Network nodes         | 5069-L330ER, 5069-L330ERM, 5069-L330ERMK, 5069-L330ERS2, 5069-L330ERMS2 5069-L330ERS2K, 5069-L330ERMS2K               | 60                                                                                     |
|                       | 5069-L340ER, 5069-L340ERM, 5069-L340ERP, 5069-L340ERS2, 5069-L340ERMS2                                                | 90                                                                                     |
|                       | 5069-L350ERM, 5069-L350ERMK, 5069-L350ERS2, 5069-L350ERMS2 5069-L350ERS2K, 5069-L350ERMS2K                            | 120                                                                                    |
|                       | 5069-L380ERM, 5069-L380ERS2, 5069-L380ERMS2                                                                           | 150                                                                                    |
|                       | 5069-L3100ERM, 5069-L3100ERS2, 5069-L3100ERMS2                                                                        | 180                                                                                    |
| Controller redundancy | Logix Hot Backup - CompactLogix 5380 Controllers only                                                                 | Logix Hot Backup - CompactLogix 5380 Controllers only                                  |
| Integrated motion     | EtherNet/IP                                                                                                           | EtherNet/IP                                                                            |

## Process Controllers

## Controller Memory

ControlLogix 5580 and CompactLogix 5380 process controllers are extensions of the Logix 5000® controller family that focus on plant-wide process control.

The process controllers come configured with a default process tasking model and dedicated PlantPAx® process instructions that are optimized for process applications and that improve design and deployment efforts. The process controllers support release 5.0 of the Rockwell Automation Library of Process Objects.

For more information on the process library, see the Rockwell Automation Library of Process Objects Reference Manual, publication PROCES-RM200 .

For more information on process controller application guidelines, see the PlantPAx DCS Configuration and Implementation User Manual, publication PROCES-UM100 .

The Logix CPU runs control and motion, communications, and packet processing each on a separate core.

- The Logix Engine executes the user program, the control task, and the motion task.
- The Communications core manages all Class 3 and unconnected communications via the Ethernet, USB, and backplane communication ports. Communications do not interrupt the user task. The System Overhead Time Slice Percentage setting is no longer available and not necessary.
- The Packet Processing Engine moves all Ethernet Class 1 packets to and from the wire, and moves all packets to and from the backplane.

The controller allocates memory as needed to help prevent many runtime errors that are related to free memory. Runtime memory no longer consumes application memory space.

<!-- image -->

The GuardLogix 5580 and Compact GuardLogix 5380 CPU performs the same functions as the ControlLogix 5580 and CompactLogix 5380 controllers, with these differences:

- The Logix Engine executes the user program, the control task, the motion task, and the safety task.
- The Functional Safety Diagnostic Core runs the safety task with inverted data, and compares the results to the safety task that runs on the Logix Engine.

GuardLogix 5580 controllers and Compact GuardLogix 5380 controllers—Memory is in one, contiguous section.

<!-- image -->

## Data Types

The controllers support the following data types:

- Numerous IEC 61131-3 elementary data types
- Compound data types
- Arrays
- Predefined structures, such as counters and timers
- User-defined structures

The Logix CPU reads and manipulates 64-bit data values. The minimum memory allocation for data in a tag is 4 bytes. When you create a standalone tag that stores data that is less than 4 bytes, the controller allocates 4 bytes, but the data only fills the part that it needs.

For more information See Data Structures on page 83 .

| Data Type   | Bits                                          | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        |
|-------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Data Type   | 64…32 31                                      |                                                                                                             | 16                                                                                                          | 15 8 7 1 0                                                                                                  |                                                                                                             |                                                                                                             |                                                                                                             |
| BOOL        | Not allocated                                 | Allocated but not used                                                                                      | Allocated but not used                                                                                      | Allocated but not used                                                                                      | 0 or 1                                                                                                      | Allocated but not used                                                                                      |                                                                                                             |
| SINT        | Not allocated                                 | Allocated but not used                                                                                      | Allocated but not used                                                                                      | -128…+127                                                                                                   | -128…+127                                                                                                   |                                                                                                             |                                                                                                             |
| INT         | Not allocated                                 | Allocated but not used -32,768…32,767                                                                       | Allocated but not used -32,768…32,767                                                                       |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| DINT        |                                               | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  |
| REAL        | Not allocated                                 | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) |
|             | LINT -922337203685477580…+9223372036854775807 | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               | LINT -922337203685477580…+9223372036854775807                                                               |

## Extended Data Types

The 5380 and 5580 controllers support these extended data types:

| Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 64…32 31 16 15 8 7…1 0                                                                                                                  |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | USINT Not allocated Allocated but not used                                                                                              | USINT Not allocated Allocated but not used                                                                                              | Unsigned 0…255                                                                                                                          | Unsigned 0…255                                                                                                                          |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | UINT Not allocated Allocated but not used                                                                                               | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       |                                                                                                                                         |                                                                                                                                         |
|                                                                                                                                         | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            | UDINT Not allocated Unsigned 0…4,294,967,295                                                                                            |
| ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             |
| -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) |

The compute, compare, and math instructions support these extended data types for 64-bit operations.

## Date and Time Data Types

The 5380 and 5580 controllers support date and time data types to standardize date and time values in instructions. Standardized values increase the accuracy and reliability of timestamped inputs, scheduled outputs, and time-based registration for motion control. These data types are also helpful for sequence of events, time-stamped data logging and analytics, and time synchronization within and across systems.

|                                                               | Data Type Description                                                                       | Literal String Format                                     |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Absolute time data types—Use for specific points in time.     | Absolute time data types—Use for specific points in time.                                   | Absolute time data types—Use for specific points in time. |
|                                                               | DT Date and time. 64-bit storage; units are in microseconds. DT#2020-03-05-08:11:44.345_678 |                                                           |
| LDT                                                           | Long date and time. 64-bit storage; units are in nanoseconds.                               | LDT#2020-10-25-11:05:20.123_456_789                       |
| Relative time data types—Use for duration or lengths of time. | Relative time data types—Use for duration or lengths of time.                               | Literal String Display Format                             |
| TIME32                                                        | Duration of time. 32-bit storage; units are in microseconds.                                | T32#2d_3h_1m_22s_123ms_678us                              |
| TIME                                                          | Duration of time. 64-bit storage; units are in microseconds.                                | T#5d_8h_5m_33s_234ms_679us                                |
| LTIME                                                         | Long duration of time. 64-bit storage; units are in nanoseconds.                            | LT#3d_10h_18m_47s_123ms_456us_789ns                       |

The following instructions support absolute and relative time data types:

- Add (ADD)
- AOI parameters
- Equal To (EQ)
- Clear (CLR)
- Copy (COP) - In Logix Designer, version 38 and greater, only supports the DT data type.
- Greater Than or Equal To (GE)
- Greater Than (GT)
- Get System Value (GSV) and Set System Value (SSV)
- Jump to Subroutine (JSR)
- Less Than or Equal To (LE)
- Less Than (LT)
- Move (MOV)
- Not Equal To (NE)
- Return (RET)
- Subroutine (SBR)
- Subtract (SUB)

You can use the Date and Time Browser dialog box to set a value for any of the date and time data types. To access the Date and Time Browser dialog box from the Logix Designer application:

1. Create a tag and set the data type to TIME32, TIME, LTIME, DT, or LDT.
2. Select the Monitor Tags tab.
3. Set the Style to an appropriate format for that type.
4. Click the Value field and click the … button.

<!-- image -->

## Programming Techniques

## Produced and Consumed Data

## Connections

| Programming Technique Consideration   |                                                                                                                                                                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subroutines                           | For Logix Designer application Version 28 and later on 5580 and 5380 controllers: • JSR calls are limited to 40 input parameters and 40 output parameters. • There is a maximum of 25 JSR nesting levels.                       |
| Add-On Instructions                   | For 5580 controllers 5380 controllers, you can nest Add-On Instructions as follows: • Logix Designer application, version 28 and earlier - up to 25 levels • Logix Designer application, version 29 and later - up to 16 levels |
| PhaseManager™ equipment phases        | The PhaseManager option is supported on 5580 and 5380 controllers as of firmware revision 32.                                                                                                                                   |

For more information See Modular Programming Techniques on page 53 .

## Data Alignment Rules

The 5580, 5380, and all 64-bit controllers have these data alignment rules on UDTs:

- 8-byte (64-bit) data types (LINT, ULINT, LREAL, TIME, LTIME, DT, and LDT) are placed on 8-byte address boundaries in RAM. The Studio 5000 Logix Designer application manages this requirement automatically.
- UDTs that have no 8-byte elements retain the existing 4-byte memory allocation rules.
- UDTs that contain 8-byte data types are considered 8-byte data types with a size that is a multiple of 8 bytes.
- 8-byte data types within a UDT are aligned on an 8-byte boundary.

## The controller supports:

- Total number of produced tags ≤ 255
- Maximum number of multicast produce tags out of the Ethernet port ≤ 32
- Maximum number of consumed tags ≤ 255

For more information See Produced and Consumed Data on page 79 .

## The controller supports:

- Dedicated Class 1 (I/O, Produce and Consume) connection pool to support controller node count
- Dedicated Class 3 (HMI, message instructions) connection pool to support up to 512 connections
- This pool is split; 256 incoming and 256 outgoing connections
- 256 cached buffers
- 320 unconnected buffers to establish connections
- This value is fixed and cannot be increased with a CIP Generic message instruction.

## CompactLogix 5480 Controllers

## 5480 Controllers

| Characteristic        | CompactLogix® 5480 Controllers                                                                                                                                                                                                                                                                                                                                                                                   | CompactLogix® 5480 Controllers                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller tasks      | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                                                                                                                                                                                                                                                                           | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                                                                                                                                                                                                                                                                           |
| Event tasks           | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                                                                                                                                                                                                                                                                                                           | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                                                                                                                                                                                                                                                                                                           |
| User memory           | Windows® 10 (commercial operating system on controller)                                                                                                                                                                                                                                                                                                                                                          | • RAM: 6 GB • SSD: 64 GB                                                                                                                                                                                                                                                                                                                                                                                         |
| User memory           | Logix control engine                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                  |
| User memory           | 5069-L430ERMW                                                                                                                                                                                                                                                                                                                                                                                                    | 3 MB                                                                                                                                                                                                                                                                                                                                                                                                             |
| User memory           | 5069-L450ERMW                                                                                                                                                                                                                                                                                                                                                                                                    | 5 MB                                                                                                                                                                                                                                                                                                                                                                                                             |
| User memory           | 5069-L4100ERMW                                                                                                                                                                                                                                                                                                                                                                                                   | 10 MB                                                                                                                                                                                                                                                                                                                                                                                                            |
| User memory           | 5069-L4200ERMW                                                                                                                                                                                                                                                                                                                                                                                                   | 20 MB                                                                                                                                                                                                                                                                                                                                                                                                            |
| Built-in ports        | Logix control engine uses: • 3 - Ethernet ports, 10/100/1000 Mbps • 1 - USB port (1) IMPORTANT: Consider the following: • When the controller operates in Dual-IP mode, each Ethernet port requires a unique IP address. • When the controller operates in Linear/DLR mode, the controller uses only one IP address. Windows 10 uses: • 1 - Ethernet port 10/100/1000 Mbps • 2 - USB 3.0 ports • 1 - DisplayPort | Logix control engine uses: • 3 - Ethernet ports, 10/100/1000 Mbps • 1 - USB port (1) IMPORTANT: Consider the following: • When the controller operates in Dual-IP mode, each Ethernet port requires a unique IP address. • When the controller operates in Linear/DLR mode, the controller uses only one IP address. Windows 10 uses: • 1 - Ethernet port 10/100/1000 Mbps • 2 - USB 3.0 ports • 1 - DisplayPort |
| Communication options | • Dual-port EtherNet/IP™ • USB Client                                                                                                                                                                                                                                                                                                                                                                            | • Dual-port EtherNet/IP™ • USB Client                                                                                                                                                                                                                                                                                                                                                                            |
| Communication options | Studio 5000 Logix Designer® application, version 32.00.00 to 37.00.00                                                                                                                                                                                                                                                                                                                                            | Studio 5000 Logix Designer® application, version 32.00.00 to 37.00.00                                                                                                                                                                                                                                                                                                                                            |
| Communication options | 5069-L430ERMW                                                                                                                                                                                                                                                                                                                                                                                                    | 60                                                                                                                                                                                                                                                                                                                                                                                                               |
| Communication options | 5069-L450ERMW                                                                                                                                                                                                                                                                                                                                                                                                    | 120                                                                                                                                                                                                                                                                                                                                                                                                              |
| Communication options | 5069-L4100ERMW                                                                                                                                                                                                                                                                                                                                                                                                   | 180                                                                                                                                                                                                                                                                                                                                                                                                              |
| Communication options | 5069-L4200ERMW                                                                                                                                                                                                                                                                                                                                                                                                   | 250                                                                                                                                                                                                                                                                                                                                                                                                              |
| Communication options | 5069-L46ERMW                                                                                                                                                                                                                                                                                                                                                                                                     | 250                                                                                                                                                                                                                                                                                                                                                                                                              |
| Controller redundancy | None                                                                                                                                                                                                                                                                                                                                                                                                             | None                                                                                                                                                                                                                                                                                                                                                                                                             |
| Integrated motion     | EtherNet/IP                                                                                                                                                                                                                                                                                                                                                                                                      | EtherNet/IP                                                                                                                                                                                                                                                                                                                                                                                                      |

<!-- image -->

## Controller Memory

## Data Types

The Logix CPU runs control and motion, communications, and packet processing each on a separate core.

- The Logix Engine executes the user program, the control task, and the motion task.
- The Communications core manages all Class 3 and unconnected communications via the Ethernet, USB, and backplane communication ports. Communications do not interrupt the user task, and you do not need to adjust the System Overhead Time Slice Percentage.
- The Packet Processing Engine moves all Ethernet Class 1 packets to and from the wire, and moves all packets to and from the backplane.

The controller allocates memory as needed to help prevent many runtime errors that are related to free memory. Runtime memory no longer consumes application memory space.

1756 CompactLogix 5480 controllers- Memory is in one, contiguous section.

<!-- image -->

The controllers support the following data types:

- Numerous IEC 61131-3 elementary data types
- Compound data types
- Arrays
- Predefined structures, such as counters and timers
- User-defined structures

The Logix CPU reads and manipulates 32-bit data values. The minimum memory allocation for data in a tag is 4 bytes. When you create a standalone tag that stores data that is less than 4 bytes, the controller allocates 4 bytes, but the data only fills the part that it needs.

For more information See Data Structures on page 83 .

<!-- image -->

| Data Type   | Bits                                           | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        | Bits                                                                                                        |
|-------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Data Type   |                                                |                                                                                                             | 64…32 31 16 15 8 7 1 0                                                                                      |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| BOOL        | Not allocated                                  | Allocated but not used                                                                                      | Allocated but not used                                                                                      | 0 or 1                                                                                                      | Allocated but not used                                                                                      | Allocated but not used                                                                                      |                                                                                                             |
| SINT        | Not allocated                                  | Allocated but not used                                                                                      | -128…+127                                                                                                   | -128…+127                                                                                                   | Allocated but not used                                                                                      |                                                                                                             |                                                                                                             |
| INT         | Not allocated                                  | Allocated but not used -32,768…32,767                                                                       | Allocated but not used -32,768…32,767                                                                       |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| DINT        |                                                | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  | Not allocated -2,147,483,648…2,147,483,647                                                                  |
| REAL        | Not allocated                                  | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values) |
|             | LINT -9223372036854775808…+9223372036854775807 | LINT -9223372036854775808…+9223372036854775807                                                              | LINT -9223372036854775808…+9223372036854775807                                                              | LINT -9223372036854775808…+9223372036854775807                                                              | LINT -9223372036854775808…+9223372036854775807                                                              | LINT -9223372036854775808…+9223372036854775807                                                              | LINT -9223372036854775808…+9223372036854775807                                                              |

## Extended Data Types

The 5480 controller supports these extended data types:

| Data Type   | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    | Bits                                                                                                                                    |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Data Type   | 64…32 31 16 15 8 7…1 0                                                                                                                  |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |                                                                                                                                         |
| USINT       | Not allocated                                                                                                                           | Allocated but not used                                                                                                                  | Allocated but not used                                                                                                                  | Unsigned 0…255                                                                                                                          | Unsigned 0…255                                                                                                                          |                                                                                                                                         |                                                                                                                                         |
| UINT        | Not allocated                                                                                                                           | Allocated but not used                                                                                                                  | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       | Unsigned 0…65,535                                                                                                                       |                                                                                                                                         |                                                                                                                                         |
| UDINT       | Not allocated                                                                                                                           | Unsigned 0…4,294,967,295                                                                                                                | Unsigned 0…4,294,967,295                                                                                                                | Unsigned 0…4,294,967,295                                                                                                                | Unsigned 0…4,294,967,295                                                                                                                | Unsigned 0…4,294,967,295                                                                                                                | Unsigned 0…4,294,967,295                                                                                                                |
|             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             | ULINT Unsigned 0…18,446,744,073,709,551,615                                                                                             |
| LREAL       | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) | -1.7976931348623157E308…-2.2250738585072014E-308 (negative values) 0.0 2.2250738585072014E-308…1.7976931348623157E308 (positive values) |

The compute, compare, and math instructions support these extended data types for 64-bit operations.

## Date and Time Data Types

The 5480 controllers support date and time data types to standardize date and time values in instructions. Standardized values increase the accuracy and reliability of time-stamped inputs, scheduled outputs, and time-based registration for motion control. These data types are also helpful for sequence of events, time-stamped data logging and analytics, and time synchronization within and across systems.

|                                                               | Data Type Description                                                                       | Literal String Format                                     |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Absolute time data types—Use for specific points in time.     | Absolute time data types—Use for specific points in time.                                   | Absolute time data types—Use for specific points in time. |
|                                                               | DT Date and time. 64-bit storage; units are in microseconds. DT#2020-03-05-08:11:44.345_678 |                                                           |
| LDT                                                           | Long date and time. 64-bit storage; units are in nanoseconds.                               | LDT#2020-10-25-11:05:20.123_456_789                       |
| Relative time data types—Use for duration or lengths of time. | Relative time data types—Use for duration or lengths of time.                               | Literal String Display Format                             |
| TIME32                                                        | Duration of time. 32-bit storage; units are in microseconds.                                | T32#2d_3h_1m_22s_123ms_678us                              |
| TIME                                                          | Duration of time. 64-bit storage; units are in microseconds.                                | T#5d_8h_5m_33s_234ms_679us                                |
| LTIME                                                         | Long duration of time. 64-bit storage; units are in nanoseconds.                            | LT#3d_10h_18m_47s_123ms_456us_789ns                       |

The following instructions support absolute and relative time data types:

- Add (ADD)
- AOI parameters
- Equal To (EQ)
- Clear (CLR)
- Copy (COP) - In Logix Designer, version 38 and greater, only supports the DT data type.
- Greater Than or Equal To (GE)
- Greater Than (GT)
- Get System Value (GSV) and Set System Value (SSV)
- Jump to Subroutine (JSR)
- Less Than or Equal To (LE)
- Less Than (LT)
- Move (MOV)
- Not Equal To (NE)
- Return (RET)
- Subroutine (SBR)
- Subtract (SUB)

You can use the Date and Time Browser dialog box to set a value for any of the date and time data types. To access the Date and Time Browser dialog box from the Logix Designer application:

1. Create a tag and set the data type to TIME32, TIME, LTIME, DT, or LDT.
2. Select the Monitor Tags tab.
3. Set the Style to an appropriate format for that type.
4. Click the Value field and click the … button.

<!-- image -->

## Programming Techniques

## Produced and Consumed Data

## Connections

| Programming Technique Consideration   |                                                                                                                                                                                          |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subroutines                           | For Logix Designer application Version 32.00.00 and later: • JSR calls are limited to 40 input parameters and 40 output parameters. • There is a maximum of 25 JSR nesting levels.       |
| Add-On Instructions                   | You can nest Add-On Instructions as follows: • Logix Designer application, version 28 and earlier - up to 25 levels • Logix Designer application, version 29 and later - up to 16 levels |
| PhaseManager™ equipment phases        | The PhaseManager option is supported on 5480 controllers as of firmware revision 32.                                                                                                     |

For more information See Modular Programming Techniques on page 53 .

## Data Alignment Rules

The 5480 controllers have these data alignment rules on UDTs:

- 8-byte (64-bit) data types (LINT, ULINT, LREAL, TIME, LTIME, DT, and LDT) are placed on 8-byte address boundaries in RAM. The Studio 5000 Logix Designer application manages this requirement automatically.
- UDTs that have no 8-byte elements retain the existing 4-byte memory allocation rules.
- UDTs that contain 8-byte data types are considered 8-byte data types with a size that is a multiple of 8 bytes.
- 8-byte data types within a UDT are aligned on an 8-byte boundary.

## The controller supports:

- Total number of produced tags ≤ 255
- Maximum number of multicast produce tags out of the Ethernet port ≤ 32
- Maximum number of consumed tags ≤ 255

For more information See Produced and Consumed Data on page 79 .

## The controller supports the following:

- Dedicated Class 1 (I/O, Produce and Consume) connection pool to support controller node count
- Dedicated Class 3 (HMI, message instructions) connection pool to support up to 512 connections
- This pool is split; 256 incoming and 256 outgoing connections
- 256 cached buffers
- 320 unconnected buffers for establishing connections
- This value is fixed and cannot be increased with a CIP™ Generic message instruction.

## Notes:

## ControlLogix 5570 and GuardLogix 5570 Controllers

| Characteristic         | ControlLogix 5570 Controllers GuardLogix 5570 Controllers Armor™ ControlLogix 5570 Controllers Armor™ GuardLogix® 5570 Controllers            |                                                                                        |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Controller tasks       | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                        | 32, including continuous, periodic, and event tasks 1000 programs/task                 |
| Event tasks            | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events                                                        | Consumed tag, EVENT instruction triggers, Module Input Data changes, and motion events |
| User memory            | 1756-L71, 1756-L71EROM 2 MB standard                                                                                                          |                                                                                        |
| User memory            | 1756-L72, 1756-L72EROM 4 MB standard                                                                                                          |                                                                                        |
| User memory            | 1756-L73, 1756-L73XT, 1756-L73EROM 8 MB standard                                                                                              |                                                                                        |
| User memory            |                                                                                                                                               | 1756-L74 16 MB standard                                                                |
| User memory            |                                                                                                                                               | 1756-L75 32 MB standard                                                                |
| User memory            | 1756-L71S, 1756-L71EROMS                                                                                                                      | 2 MB standard +1 MB safety                                                             |
| User memory            | 1756-L72S, 1756-L72EROMS                                                                                                                      | 4 MB standard + 2 MB safety                                                            |
| User memory            | 1756-L73S, 1756-L73EROMS                                                                                                                      | 8 MB standard + 4 MB safety                                                            |
| Built-in ports         | 1756-L71, 1756-L72, 1756-L73, 1756-L73XT, 1756-L74, 1756-L75, 1756-L71S, 1756-L72S, 1756-L73S                                                 | 1-port USB                                                                             |
| Built-in ports         | 1756-L71EROM, 1756-L71EROMS, 1756-L72EROM, 1756-L72EROMS, 1756-L73EROM, 1756-L73EROMS                                                         | 1-port USB Dual-port EtherNet/IP™ port, 10/100 Mbps                                    |
| Communication options  | • EtherNet/IP • ControlNet® • DeviceNet® • Data Highway Plus™ • Remote I/O • SynchLink™ • USB Client                                          |                                                                                        |
| Controller connections | 500 connections                                                                                                                               |                                                                                        |
| Controller redundancy  | 1756-L71, 1756-L72, 1756-L73, 1756-L73XT, 1756-L74, and 1756-L75 controllers only. Full support with a separate redundancy firmware revision. |                                                                                        |
| Integrated motion      | EtherNet/IP                                                                                                                                   |                                                                                        |

## 5570 Controllers and 5370 Controllers

This chapter highlights these controllers.

| Controller Family Controller Names                                          |
|-----------------------------------------------------------------------------|
| 5570 controllers ControlLogix® 5570 and GuardLogix® 5570 controllers        |
| 5370 controllers CompactLogix® 5370 and Compact GuardLogix 5370 controllers |

<!-- image -->

## CompactLogix 5370 and Compact GuardLogix 5370 Controllers

| Characteristic         | CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers Armor CompactLogix 5370 Controllers and Armor Compact GuardLogix 5370 Controllers           | CompactLogix 5370 Controllers and Compact GuardLogix 5370 Controllers Armor CompactLogix 5370 Controllers and Armor Compact GuardLogix 5370 Controllers           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller tasks       | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                            | 32, including continuous, periodic, and event tasks 1000 programs/task                                                                                            |
| Event tasks            | Consumed tag, EVENT instruction triggers, and motion events                                                                                                       | Consumed tag, EVENT instruction triggers, and motion events                                                                                                       |
|                        |                                                                                                                                                                   | 1769-L16ER-BB1B 384 KB standard                                                                                                                                   |
|                        | 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK 512 KB standard                                                                                              |                                                                                                                                                                   |
|                        | 1769-L24ER-QB1B, 1769-L24ER-QBFC1B, 1769-L24ER-QBFC1BK 750 KB standard                                                                                            |                                                                                                                                                                   |
|                        | 1769-L19ER-BB1B, 1769-L19ER-BB1BK, 1769-L27ERM-QBFC1B, 1769-L30ER, 1769-L30ERK, 1769-L30ER-NSE, 1769-L30ERM, 1769-L30ERMK                                         | 1 MB standard                                                                                                                                                     |
|                        | 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMO                                                                                                  | 2 MB standard                                                                                                                                                     |
| User memory            | 1769-L36ERM, 1769-L36ERMO                                                                                                                                         | 3 MB standard                                                                                                                                                     |
|                        | 1769-L37ERM, 1769-L37ERMK, 1769-L37ERMO                                                                                                                           | 4 MB standard                                                                                                                                                     |
|                        | 1769-L38ERM, 1769-L38ERMK, 1769-L38ERMO                                                                                                                           | 5 MB standard                                                                                                                                                     |
|                        | 1769-L30ERMS                                                                                                                                                      | 1 MB + 0.5 MB safety                                                                                                                                              |
|                        | 1769-L33ERMS, 1769-L33ERMSK, 1769-L33ERMOS                                                                                                                        | 2 MB + 1 MB safety                                                                                                                                                |
|                        | 1769-L36ERMS, 1769-L36ERMOS                                                                                                                                       | 3 MB + 1.5 MB safety                                                                                                                                              |
|                        | 1769-L37ERMS, 1769-L37ERMSK, 1769-L37ERMOS                                                                                                                        | 4 MB + 1.5 MB safety                                                                                                                                              |
|                        | 1769-L38ERMS, 1769-L38ERMSK, 1769-L38ERMOS                                                                                                                        | 5 MB + 1.5 MB safety                                                                                                                                              |
| Built-in ports         | One - USB port Dual-port EtherNet/IP port                                                                                                                         | One - USB port Dual-port EtherNet/IP port                                                                                                                         |
| Communication options  | EtherNet/IP Embedded switch Single IP address DeviceNet ControlNet USB                                                                                            | EtherNet/IP Embedded switch Single IP address DeviceNet ControlNet USB                                                                                            |
| Controller connections | 256 connections                                                                                                                                                   | 256 connections                                                                                                                                                   |
|                        | 1769-L16ER-BB1B                                                                                                                                                   | 4                                                                                                                                                                 |
|                        | 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1BK, 1769-L19ER-BB1B, 1769-L19ER-BB1BK                                                                           | 8                                                                                                                                                                 |
|                        | 1769-L27ERM-QBFC1B, 1769-L30ER, 1769- L30ERK,1769-L30ER-NSE, 1769-L30ERM, 1769-L30ERMK, 1769-L30ERMS                                                              | 16                                                                                                                                                                |
| Network nodes          | 1769-L33ER, 1769-L33ERK, 1769-L33ERM, 1769-L33ERMK, 1769-L33ERMS, 1769-L33ERMSK, 1769-L33ERMO, 1769- L33ERMOS                                                     | 32                                                                                                                                                                |
|                        | 1769-L36ERM, 1769-L36ERMS, 1769-L36ERMO, 1769-L36ERMOS 48                                                                                                         |                                                                                                                                                                   |
|                        | 1769-L37ERM, 1769-L37ERMS, 1769-L37ERMO, 1769-L37ERMOS, 1769-L37ERMK, 1769-L37ERMSK                                                                               | 64                                                                                                                                                                |
|                        | 1769-L38ERM, 1769-L38ERMS, 1769-L38ERMO, 1769-L38ERMOS, 1769-L38ERMK, 1769-L38ERMSK                                                                               | 80                                                                                                                                                                |
| Controller redundancy  | Back up via DeviceNet - CompactLogix 5370 L3 Controllers and Compact GuardLogix 5370 L3 controllers only Logix Hot Backup - CompactLogix 5370 L3 Controllers only | Back up via DeviceNet - CompactLogix 5370 L3 Controllers and Compact GuardLogix 5370 L3 controllers only Logix Hot Backup - CompactLogix 5370 L3 Controllers only |
| Integrated motion      | EtherNet/IP                                                                                                                                                       | EtherNet/IP                                                                                                                                                       |
| Conformal coating      | 1769-L30ERK, 1769-L30ERMK, 1769-L33ERK, 1769-L33ERMK, 1769-L33ERMSK, 1769-L37ERMK, 1769-L37ERMSK, 1769-L38ERMK, 1769-L38ERMSK                                     | 1769-L30ERK, 1769-L30ERMK, 1769-L33ERK, 1769-L33ERMK, 1769-L33ERMSK, 1769-L37ERMK, 1769-L37ERMSK, 1769-L38ERMK, 1769-L38ERMSK                                     |

| Controller        |    |   I/O Task Priority Communication Task Priority |
|-------------------|----|-------------------------------------------------|
| CompactLogix 5370 |  6 |                                              12 |

<!-- image -->

## Controller Connections

The controller uses a connection to establish a communication link between two devices.

IMPORTANT The topics in this section apply only to ControlLogix 5570 and earlier controllers, and CompactLogix 5370 and earlier controllers operation.

Connections can be made to the following:

- Controller to local I/O modules or local communication modules
- Controller to remote I/O or remote communication modules
- Controller to remote I/O (rack-optimized) modules
- Produced and consumed tags
- Messages
- Access to programming software
- Linx-based software access for HMI or other software applications

The controllers have different communication limits.

| Communication Attribute 1756-L7x ControlLogix 1756-L6x ControlLogix 1769 CompactLogix CompactLogix 5370 1768 CompactLogix   |                                                                                                      |                                                                                                      |                                                                                                      |                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Connections  500                                                                                                            | 250                                                                                                  | 100                                                                                                  | 256                                                                                                  | 250                                                                                                  |
| Cached messages 32 for messages and block transfers combined                                                                |                                                                                                      |                                                                                                      |                                                                                                      |                                                                                                      |
| Unconnected receive buffers 3                                                                                               |                                                                                                      |                                                                                                      |                                                                                                      |                                                                                                      |
|                                                                                                                             | Unconnected transmit buffers Default 20 (can be increased to 40) Default 10 (can be increased to 40) | Unconnected transmit buffers Default 20 (can be increased to 40) Default 10 (can be increased to 40) | Unconnected transmit buffers Default 20 (can be increased to 40) Default 10 (can be increased to 40) | Unconnected transmit buffers Default 20 (can be increased to 40) Default 10 (can be increased to 40) |

The limit of connections can ultimately reside in the communication module you use for the connection. If a message path routes through a communication module, the connection that is related to the message also counts toward the connection limit of that communication module.

| Controller Communication Device                                                    | Supported Connections                                                                                                                                                                      |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-CN2R, 1756-CN2RXT                                                             | 100 CIP™ connections (any combination of scheduled and message connections)                                                                                                                |
| 1756-CN2/B                                                                         | 128 CIP connections                                                                                                                                                                        |
| 1756-CNB,1756 -CNBR                                                                | 64 CIP connections depending on RPI, recommend that you use only 48 connections (any combination of scheduled and message connections)                                                     |
| ControlLogix 1756-EN2F, 1756-EN2T, 1756-EN2TR, 1756-EN2TP, 1756-EN2TXT, 1756-EN3TR | 256 CIP connections 128 TCP/IP connections                                                                                                                                                 |
| 1756-EN4TR                                                                         | CIP connected messages: • 1000 I/O • 528 512 TCP/IP connections                                                                                                                            |
| 1756-ENBT 1756-EWEB                                                                | 128 CIP connections 64 TCP/IP connections                                                                                                                                                  |
| CompactLogix 5370 Built-in Ethernet ports                                          | See the CompactLogix 5370 Controllers User Manual, publication 1769-UM021, for information on how to count EtherNet/IP nodes on the I/O Configuration section of the programming software. |

## Determine Total Connection Requirements

The total connections for a controller include both local and remote connections. Counting local connections is not an issue for CompactLogix controllers. They support the maximum number of modules that are permitted in their systems.

When designing your CompactLogix 5370 controllers, you must consider these resources:

- EtherNet/IP network nodes
- Controller connections

For more information, see the CompactLogix 5370 Controllers User Manual, publication 1769-UM021 .

The ControlLogix controllers support more communication modules than the other controllers, so you must tally local connections to make sure that you stay within the connection limit.

Use this table to tally local connections.

| Connection Type                               | Device Quantity x Connections per Module =   |       | Total Connections   |       |
|-----------------------------------------------|----------------------------------------------|-------|---------------------|-------|
| Local I/O module (always a direct connection) | x 1                                          | =     |                     |       |
| SERCOS Motion module                          | x 3                                          | =     |                     |       |
| ControlNet communication module               | x 0                                          | =     |                     |       |
| EtherNet/IP communication module              | x 0                                          | =     |                     |       |
| DeviceNet communication module                | x 2                                          | =     |                     |       |
| DH+/Remote I/O communication module           | x 1                                          | =     |                     |       |
| DH-485 communication module                   | x 1                                          | =     |                     |       |
| Programming software access to controller     | x 1                                          | =     |                     |       |
| Total                                         | Total                                        | Total | Total               | Total |

IMPORTANT A redundant system uses eight connections in the controller.

The communication modules that you select determine how many remote connections are available. Use this table to tally remote connections.

| Connection Type                                                                                                            | Device Quantity x Connections per Module = Total Connections   |    |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|----|
| Remote ControlNet communication module Configured as a direct (none) connection Configured as a rack-optimized connection  | x 0 or 1                                                       | =  |
| Remote EtherNet/IP communication module Configured as a direct (none) connection Configured as a rack-optimized connection | x 0 or 1                                                       | =  |
| Remote device over a DeviceNet network (accounted for in rack-optimized connection for local DeviceNet module)             | x 0                                                            | =  |
| Safety device on a DeviceNet or EtherNet/IP network                                                                        | x 2                                                            | =  |
| Other remote communication adapter                                                                                         | x 1                                                            | =  |
| Distributed I/O module (individually configured for a direct connection)                                                   | x 1                                                            | =  |
| Produced tag and first consumer Each additional consumer                                                                   | x  2 1                                                         | =  |
| Consumed tag                                                                                                               | x 1                                                            | =  |
| Connected message (CIP Data Table read/write and DH+™)                                                                     | x 1                                                            | =  |
| Block transfer message                                                                                                     | x 1                                                            | =  |
| Linx-based software access for HMI or other software applications                                                          | x 4                                                            | =  |
| FactoryTalk® Linx software for HMI or other software applications                                                          | x 5                                                            | =  |
| Total                                                                                                                      |                                                                |    |

## System Overhead Percentage

The system overhead timeslice specifies the percentage of continuous task execution time that is devoted to communication and background redundancy functions.

- Message communication is any communication that you do not configure through the I/O configuration folder of the project, such as MSG instructions.
- Message communication occurs only when a periodic or event task is not running. If you use multiple tasks, make sure that their scan times and execution intervals leave enough time for message communication.
- System overhead interrupts only the continuous task.
- The controller performs message communication for up to 1 ms at a time and then resumes the continuous task.
- Adjust the update rates of the tasks as needed to get the best trade-off between executing your logic and servicing message communication.

## System overhead functions include the following:

- Communicating with HMI devices and programming software
- Sending and responding to messages
- Alarm management processing
- Redundancy qualification

The controller performs system overhead functions for up to 1 ms at a time. If the controller completes the overhead functions in less than 1 ms, it resumes the continuous task. The following chart compares a continuous and periodic task.

## Continuous Task Restarts

<!-- image -->

| Example                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous task 10% CPU overhead | In the top example, the system overhead timeslice is set to 10%. Given 40 ms of code to execute, the continuous task completes the execution in 44 ms. During a 60 ms period, the controller is able to spend 5 ms on communication processing.                                                                                                                                                                                                                                                                                                                                                                                                |
| Continuous task 25% CPU overhead | By increasing the system overhead timeslice to 25%, the controller completes the continuous task scan in 57 ms. The controller spends 15 ms of a 60 ms time span on communication processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Periodic task                    | Placing the same code in a periodic task yields even more time for communication processing. The bottom example assumes that the code is in a 60 ms periodic task. The code executes to completion and then goes dormant until the 60 ms, time-based trigger occurs. While the task is dormant, all CPU bandwidth can focus on communication. Because the code takes only 40 ms to execute, the controller can spend 20 ms on communication processing. Depending on the amount of communication to process during this 20 ms window, it can be delayed as it waits for other modules in the system to process the data that was communicated. |

The CPU timeslices between the continuous task and system overhead. Each task switch between user task and system overhead takes additional CPU time to load and restore task information. You can calculate the continuous task interval as:

ContinuousTime=(100/SystemOverheadTimeSlice%) - 1

The programming software forces at least 1 ms of execution time for the continuous task, regardless of the system overhead timeslice. This more efficiently uses system resources because letting shorter execution times of the continuous task exist means switching tasks more frequently.

|    |    |   System Overhead Timeslice % Communication Execution (ms) Continuous Task Execution (ms) |
|----|----|-------------------------------------------------------------------------------------------|
| 10 |  1 |                                                                                         9 |
| 20 |  1 |                                                                                         4 |
| 33 |  1 |                                                                                         2 |
| 50 |  1 |                                                                                         1 |
| 66 |  2 |                                                                                         1 |
| 80 |  4 |                                                                                         1 |
| 90 |  9 |                                                                                         1 |

## Manage the System Overhead Timeslice Percentage

As the system overhead timeslice percentage increases, time that is allocated to executing the continuous task decreases. If there is no communication for the controller to manage, the controller uses the communication time to execute the continuous task.

IMPORTANT

System Overhead Time Slice does not apply to ControlLogix 5580 or CompactLogix 5380 controllers.

<!-- image -->

| Consideration                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous task always has at least 1 ms execution time | The programming software forces the continuous task to have at least 1 ms of execution time, regardless of the setting for the system overhead timeslice. This results in more efficient controller use because excessive swapping between tasks uses valuable CPU resources.                                                                                                                                                                                                                                |
| Impact on communication and scan time                   | Increasing the system overhead timeslice percentage decreases execution time for the continuous task while it increases communication performance. Increasing the system overhead timeslice percentage also increases the amount of time that it takes to execute a continuous task - increasing overall scan time. Program Scan Time Tags Per Second System Timeslice % Tags per Second Program Scan Time in Milliseconds 1600 14000 1400 12000 1200 10000 1000 8000 800 6000 600 4000 400 200 2000 0 0 90% |

| Consideration Description                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unused portion of system overhead timeslice | You can configure any unused portion of the system overhead timeslice to: • Run the continuous task, which results in faster execution of application code and increases the variability of the program scan. • Process communication, which results in more predictable and deterministic scan time for the continuous task. (This is for development and testing of an application to simulate communication.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| System overhead                             | System overhead is the time that the controller spends on message communication and background tasks. • Message communication is any communication that you do not configure through the I/O configuration folder of the project, such as MSG instructions. • Message communication occurs only when a periodic or event task is not running. If you use multiple tasks, make sure that their scan times and execution intervals leave enough time for message communication. • System overhead interrupts only the continuous task. • The system overhead timeslice specifies the percentage of time (excluding the time for periodic or event tasks) that the controller devotes to message communication. • System overhead timeslice does not apply to ControlLogix 5590, ControlLogix 5580, and CompactLogix 5380 controllers. • The controller performs message communication for up to 1 ms at a time and then resumes the continuous task. • Adjust the update rates of the tasks as needed to get the best trade-off between executing your logic and servicing message communication. |

Individual applications can differ, but the overall impact on communication and scan time remains the same. The data is based on a ControlLogix5555 controller running a continuous task with 5000 tags (no arrays or user-defined structures).

The 5370 controllers use a dedicated periodic task to process I/O data. This I/O task:

- Operates at priority 6.
- Higher-priority tasks take precedence over the I/O task and can affect processing.
- Executes at the fastest RPI that you have scheduled for the system.
- Executes for as long as it takes to scan the configured I/O modules.

## I/O Processing

## Data Types

## Programming Techniques

| Programming Technique   | Consideration                                                                                                                                                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subroutines             | For Studio 5000 Logix Designer® Version 28 and later on 5570 and 5370 controllers: • JSR calls are limited to 40 input parameters and 40 output parameters. • There is no limit on nesting JSR instructions. However, it is possible that too many nesting levels can cause the controller to run out of memory and fault. |
| Add-On Instructions     | For 5570 controllers or earlier, and 5370 controllers or earlier, there is no limit on nesting Add-On Instructions. However, it is possible that too many nesting levels can cause the controller to run out of memory and fault.                                                                                          |

For more information See Modular Programming Techniques on page 53 .

The controllers support the following data types:

- Numerous IEC 61131-3 elementary data types
- Compound data types
- Arrays
- Predefined structures, such as counters and timers
- User-defined structures

The Logix CPU reads and manipulates 32-bit data values. The minimum memory allocation for data in a tag is 4 bytes. When you create a standalone tag that stores data that is less than 4 bytes, the controller allocates 4 bytes, but the data only fills the part that it needs.

For more information See Data Structures on page 83 .

| Data Type   | Bits                                                                                                                   | Bits                                                                                                                   | Bits                                                                                                                   | Bits                                                                                                                   | Bits                                                                                                                   | Bits                                                                                                                   | Bits                                                                                                                   |
|-------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Data Type   | 64…32                                                                                                                  | 31                                                                                                                     | 16                                                                                                                     | 15                                                                                                                     | 8                                                                                                                      | 7 1 0                                                                                                                  |                                                                                                                        |
| BOOL        | Not allocated                                                                                                          | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | 0 or 1                                                                                                                 |
| SINT        | Not allocated                                                                                                          | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | -128…+127                                                                                                              | -128…+127                                                                                                              |
| INT         | Not allocated                                                                                                          | Allocated but not used                                                                                                 | Allocated but not used                                                                                                 | -32,768…32,767                                                                                                         | -32,768…32,767                                                                                                         | -32,768…32,767                                                                                                         | -32,768…32,767                                                                                                         |
| DINT        | Not allocated                                                                                                          | -2,147,483,648…2,147,483,647                                                                                           | -2,147,483,648…2,147,483,647                                                                                           | -2,147,483,648…2,147,483,647                                                                                           | -2,147,483,648…2,147,483,647                                                                                           | -2,147,483,648…2,147,483,647                                                                                           | -2,147,483,648…2,147,483,647                                                                                           |
| REAL        | Not allocated                                                                                                          | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            | -3.40282347E 38 …-1.17549435E -38   (negative values) 0 1.17549435E -38 …3.40282347E 38   (positive values)            |
|             | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC | LINT Valid Date/Time range is from 1/1/1970 12:00:00 AM coordinated universal time (UTC) to 12/31/2250 12:00:00 AM UTC |

To embed tag values within a string, you can use the DTOS, RTOS, and CONCAT instructions:

- Use the DTOS or RTOS instructions to convert a value to a string.
- Use the CONCAT instruction to merge characters with another string.

## Produced and Consumed Data

## Messages

## The controller supports:

- Total number of produced tags ≤ 127
- Maximum number of multicast produce tags out of the CompactLogix Ethernet port ≤ 32
- Maximum number of consumed tags ≤ 250 (or controller maximum)

For more information See Produced and Consumed Data on page 79

## The controller supports the following:

- As many outgoing, unconnected buffers as fit in controller memory. Each buffer uses approximately 1.2 KB of I/O memory.

You can use a CIP Generic message instruction to increase the number of unconnected buffers. See the Logix 5000 Controllers Messages Programming Manual, publication 1756-PM012 .

- Three incoming unconnected buffers
- 32 cached buffers, as of firmware revision 12 and later.

## Logic Execution

The controller operating system is a preemptive multitasking system that is IEC 61131-3 compliant.

| Tasks to configure controller execution                                             | A task provides scheduling and priority information for a set of one or more programs. You can configure tasks as either continuous, periodic, or event.                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Programs to group data and logic                                                    | A task contains programs, each with its own routines and program-scoped tags. Once a task is triggered (activated), the programs that are assigned to the task execute in the order in which they are listed in the Controller Organizer. Programs are useful for projects that multiple programmers develop. During development, the code in one program that uses program-scoped tags can be duplicated in a second program to minimize the possibility of tag names colliding. Tasks can contain programs and equipment phases. |
| Routines to encapsulate executable code that is written in one programming language | Routines contain the executable code. Each program has a main routine that is the first routine to execute within a program. Use logic, such as the Jump to Subroutine (JSR) instruction, to call other routines. You can also specify an optional program fault routine.                                                                                                                                                                                                                                                          |

## Decide When to Use Tasks, Programs, and Routines

Use these considerations to determine when to use a task, program, or routine.

| Comparison Task   |                                                                                                                                                                                                                                   | Program and Equipment Phase Routine                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Quantity available Varies by controller (4, 6, 8, or 32)                                                                                                                                                                          | 32 program and equipment phases (combined) per task 100 programs/task for ControlLogix® controllers with V23 and earlier 1000 programs/task for ControlLogix controllers with V24 and later                                                              | Unlimited number of routines per program                                                                                                                                                                                                                                                                                                                               |
|                   | Function Determines how and when code is executed                                                                                                                                                                                 | Organizes groups of routines that share a common data area and function.                                                                                                                                                                                 | Contains executable code (relay ladder, function block diagram, sequential function chart, or structured text)                                                                                                                                                                                                                                                         |
| Use               | • Use a periodic task for slower processes or when time-based operation is critical • Use an event task for operations that require synchronization to a specific event                                                           | • Put major equipment pieces or plant cells into isolated programs • Use programs to isolate different programmers or create reusable code • Configurable execution order within a task • Isolate individual batch phases or discrete machine operations | • Isolate machine or cell functions in a routine • Use the appropriate language for the process • Modularize code into subroutines that can be called multiple times                                                                                                                                                                                                   |
| Considerations    | • A high number of tasks can be difficult to debug • Can disable output processing on some tasks to improve performance • Tasks can be inhibited to help prevent execution • Do not configure multiple tasks at the same priority | • Data spanning multiple programs must be controller-scoped or a program parameter. • Listed in the Controller Organizer in the order of execution                                                                                                       | • Subroutines with multiple calls can be difficult to debug • Data can be referenced from program-scoped and controller-scoped areas • Calling many routines impacts scan time • Listed in the Controller Organizer as Main, Fault, and then alphabetically • Large routines can be hard to understand and can take longer to download than multiple smaller routines. |

<!-- image -->

## Specify Task Priorities

Each task in the controller has a priority level. A higher priority task (such as 1) interrupts any lower priority task (such as 15). The continuous task has the lowest priority; periodic or event tasks always interrupt continuous tasks.

The controller has these types of tasks.

| Priority   | User Task                  | Description                                                                                                 |
|------------|----------------------------|-------------------------------------------------------------------------------------------------------------|
|            | —                          | CPU overhead - general CPU operations                                                                       |
|            | —                          | Motion planner - executed at coarse update rate                                                             |
|            | —                          | Safety task - safety logic                                                                                  |
|            | —                          | Redundancy task - communication in redundant systems                                                        |
|            | —                          | Trend data collection - high-speed collection of trend data values                                          |
|            | Priority 1 Event/Periodic  | User defined                                                                                                |
|            | Priority 2 Event/Periodic  | User defined                                                                                                |
|            | Priority 3 Event/Periodic  | User defined                                                                                                |
| Highest    | Priority 4 Event/Periodic  | User defined                                                                                                |
|            | Priority 5 Event/Periodic  | User defined                                                                                                |
|            | Priority 6 Event/Periodic  | User defined 1769 CompactLogix® controllers process I/O as a periodic task based on the chassis RPI setting |
|            | Priority 7 Event/Periodic  | User defined                                                                                                |
|            | Priority 8 Event/Periodic  | User defined                                                                                                |
|            | Priority 9 Event/Periodic  | User defined                                                                                                |
|            | Priority 10 Event/Periodic | User defined                                                                                                |
|            | Priority 11 Event/Periodic | User defined                                                                                                |
|            | Priority 12 Event/Periodic | User defined CompactLogix communication and scheduled connection maintenance                                |
|            | Priority 13 Event/Periodic | User defined                                                                                                |
| Lowest     | Priority 14 Event/Periodic | User defined                                                                                                |
|            | Priority 15 Event/Periodic | User defined                                                                                                |
|            | Continuous                 | Lowest priority task. Interrupted by all other tasks including system overhead timeslice (if applicable.)   |

If a periodic or event task is executing when another is triggered, and both tasks are at the same priority level, the tasks execute in 1 ms increments until one of the tasks completes execution.

## Manage User Tasks

You can configure these user tasks.

| If you want logic to execute                                                                       | Use this task Description   |                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| • At a constant period (such as every 100 ms) • Multiple times within the scan of your other logic | Periodic task               | A periodic task performs a function at a specific time interval. Whenever the time for the periodic task expires, the periodic task: • Interrupts any lower priority tasks. • Executes one time. • Returns control to where the previous task left off.                                                                                                               |
| Immediately when an event occurs                                                                   | Event task                  | An event task performs a function only when a specific event (trigger) occurs. Whenever the trigger for the event task occurs, the event task: • Interrupts any lower priority tasks. • Executes one time. • Returns control to where the previous task left off.                                                                                                     |
| All the time                                                                                       | Continuous task             | The continuous task runs in the background. Any CPU time that is not allocated to other operations or tasks is used to execute the continuous task. • The continuous task runs all the time. When the continuous task completes a full scan, it restarts immediately. • A project does not require a continuous task. If used, there can be only one continuous task. |

The user tasks that you create appear in the Tasks folder of the controller. The predefined system tasks do not appear in the Tasks folder and they do not count toward the task limit of the controller.

## Pre-defined Tasks in ControlLogix and CompactLogix Process Controllers

PlantPAx® system release 5.0 adds process controllers to the Logix 5000 family of controllers. The process controllers offer additional capabilities that are targeted for DCS applications.

The Task folder contains a project structure that consists of four pre-defined periodic tasks:

- Fast (100 ms) – For control fast loops, such as liquid flow or pressure with related transmitters and pump drives
- Normal (250 ms) – For discrete control, such as motors, pumps, and valves
- Slow (500 ms) – For level, temperature, analysis loops, phases, and batch sequencing
- System (1000 ms) – For slow change temperature control and general controller operations, such as messaging or status

## Considerations that Affect Task Execution

| Consideration     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Motion planner    | The motion planner interrupts all other tasks, regardless of their priority. • The number of axes and coarse update period for the motion group affect how long and how often the motion planner executes. • If the motion planner is executing when a task is triggered, the task waits until the motion planner is done. • If the coarse update period occurs while a task is executing, the task pauses to let the motion planner execute. |
| Output processing | At the end of a task, the controller performs output processing for the output modules in your system. This processing depends on the number of output connections that are configured in the I/O tree.                                                                                                                                                                                                                                       |
| Too many tasks    | If you have too many tasks, then the following can occur: • Continuous task can take too long to complete. • Other tasks can experience overlaps. If a task is interrupted too frequently or too long, it must be triggered again to complete its execution. • Controller communication can be slower. • If your application is designed for data collection, try to avoid multiple tasks.                                                    |

This example depicts the execution of a project with these tasks.

## Table 1 - Example Task Execution

| Task                            | Priority Period   |                                | Execution Time Duration   |          |
|---------------------------------|-------------------|--------------------------------|---------------------------|----------|
| Motion planner                  | —                 | 8 ms (course update rate) 1 ms |                           | 1 ms     |
| Event task 1                    | 1                 | —                              | 1 ms                      | 1 … 2 ms |
| Periodic task 1 2 12 ms 2 ms    |                   |                                |                           | 2 … 4 ms |
| Continuous task — — 20 ms 48 ms |                   |                                |                           |          |

<!-- image -->

| Description   | Description                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
|               | 1 Initially, the controller executes the motion planner and the I/O task (if one exists).                                                |
|               | 2 The period for periodic task 1 expires (12 ms), so the task interrupts the continuous task.                                            |
| 3             | The triggers occur for event task 1. Event task 1 waits until the motion planner is done. Lower priority tasks experience longer delays. |
|               | 4 The continuous task automatically restarts.                                                                                            |

## Configure a Periodic Task

## Configure an Event Task

A periodic task executes automatically based on a preconfigured interval. You can configure whether the task updates output modules at the end of the periodic task. After the task executes, it does not execute again until the configured time interval has elapsed.

An event task executes automatically based on a trigger event occurring, or if a trigger event does not occur in a specific time interval. You configure whether the task updates output modules at the end of the task. After the task executes, it does not execute again until the event occurs again. Each event task requires a specific trigger.

| Trigger                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module Input Data State Change | A remote input module (digital or analog) triggers an event task that is based on the change of state (COS) configuration for the module. Enable COS for only one point on the module. If you enable COS for multiple points, a task overlap of the event task can occur. • The ControlLogix sequence of events modules (1756-IB16ISOE, 1756-IH16ISOE) use the Enable Coordinated System Time (CST) Capture feature instead of COS. • The embedded input points on the 1769-L16ER-BB1B, 1769-L18ER-BB1B, 1769-L18ERM-BB1B, 1769-L18ERM-BB1B, and 1769-L19ER-BB1BK modules can be configured to trigger an event task when a COS occurs. |
| Consumed Tag                   | Only one consumed tag can trigger a specific event task. Use an Immediate Output (IOT) instruction in the producing controller to signal the production of new data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                | Axis Registration 1 or 2 A registration input triggers the event task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Axis Watch                     | A watch position triggers the event task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Motion Group Execution         | The coarse update period for the motion group triggers the execution of both the motion planner and the event task. Because the motion planner interrupts all other tasks, it executes first.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| EVENT Instruction              | Multiple EVENT instructions can trigger the same task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## For more information on event tasks, see:

- Logix 5000 Controllers Common Procedures Programming Manual, publication 1756-PM001
- Using Event Tasks with Logix 5000 Controllers, publication LOGIX-WP003

## Guidelines to Configure an Event Task

| Guideline                                                                                  | Description                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Place the I/O module being used to trigger an event in the same chassis as the controller. | Placing the I/O module in a remote chassis adds more network communication and processing to the response time.                                                                                                   |
| Limit events on digital inputs to one input bit on a module.                               | All inputs on a module trigger one event, so if you use multiple bits you increase the chance of a task overlap. Configure the module to detect change of state on the trigger input and turn off the other bits. |
| Set the priority of the event task as the highest priority on the controller.              | If the priority of the event task is lower than a periodic task, the event task has to wait for the periodic task to complete execution.                                                                          |
| Limit the number of event tasks.                                                           | Increasing the number of event tasks reduces the available CPU bandwidth and increases the chances of task overlap.                                                                                               |

## Additional Considerations for Periodic and Event Tasks

| Consideration     | Description                                                                                                                                                                    |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Amount of code in the event task Each logic element (for example, rung, instruction, or structured text construct) adds to scan time.                                          |
| Task priority     | If the event task is not the highest priority task, a higher priority task can delay or interrupt the execution of the event task.                                             |
|                   | CPS and UID instructions If one of these instructions is active, the event task cannot interrupt the currently executing task. (The task with the CPS or UID.)                 |
| Motion planner    | The motion planner takes precedence over event or periodic tasks                                                                                                               |
| Trends            | Trend data collection takes precedence over event or periodic tasks.                                                                                                           |
| Output processing | You can disable output processing at the end of a task to reduce the amount of task processing time. The Controller Organizer displays whether outputs processing is disabled. |

## Configure a Continuous Task

## Access the Module Object

When you create a project in the programming software, the Main Task is configured as a continuous task.

- A controller supports one continuous task, but a continuous task is not required.
- You can configure the task to update output modules at the end of the continuous task.
- You can change the continuous task to either a periodic or event task.

The MODULE object provides status information about a module. To select a particular module object, set the Object Name operand of the GSV/SSV instruction to the module name. The specified module must be present in the I/O Configuration section of the controller organizer and must have a device name.

With the Studio 5000 Logix Designer® application, version 24.00.00 and later, you can access the MODULE object directly from an Add-On Instruction. Previously, you could access the MODULE object data, but not from within an Add-On Instruction.

You must create a Module Reference parameter when you define the Add-On Instruction to access the MODULE object data. A Module Reference parameter is an InOut parameter of the MODULE data type that points to the MODULE Object of a hardware module. You can use module reference parameters in both Add-On Instruction logic and program logic.

<!-- image -->

<!-- image -->

For more information on the Module Reference parameter, see the Logix 5000 Controllers AddOn Instructions Programming Manual, publication 1756-PM010, and the Logix Designer application online help.

The Path attribute is available with Logix Designer application, version 24.00.00 and later. This attribute provides a communication path to the module.

For more information on the attributes available in the MODULE object, see the Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .

## Develop Application Code in Routines

Each routine contains logic in one programming language. Choose a programming language that is based on the application.

| Section of Code Represents                                                                             | Language to Use                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------|
| Continuous or parallel execution of multiple operations (not sequenced)                                | Ladder Diagram(LD)              |
| Boolean or bit-based operations                                                                        | Ladder Diagram(LD)              |
| Complex logical operations                                                                             | Ladder Diagram(LD)              |
| Message and communication processing                                                                   | Ladder Diagram(LD)              |
| Machine interlocking                                                                                   | Ladder Diagram(LD)              |
| Operations that service or maintenance personnel can interpret to troubleshoot the machine or process. | Ladder Diagram(LD)              |
| Servo motion control                                                                                   | Ladder Diagram(LD)              |
| Continuous process and drive control                                                                   | Function block diagram (FBD)    |
| Loop control                                                                                           | Function block diagram (FBD)    |
| Calculations in circuit flow                                                                           | Function block diagram (FBD)    |
| High-level management of multiple operations                                                           | Sequential function chart (SFC) |
| Repetitive sequences of operations                                                                     | Sequential function chart (SFC) |
| Batch process                                                                                          | Sequential function chart (SFC) |
| Motion control sequencing (via sequential function chart with embedded structure text)                 | Sequential function chart (SFC) |
| State machine operations                                                                               | Sequential function chart (SFC) |
| Complex mathematical operations                                                                        | Structured text (ST)            |
| Specialized array or table loop processing                                                             | Structured text (ST)            |
| ASCII string handling or protocol processing                                                           | Structured text (ST)            |

## Comparison of Programming Languages

|                                                                                                                                                           |                                                                                                     |                                                                                                                                               | Comparison Relay Ladder Logic Function Block Diagram Sequential Function Chart Structured Text                                                                                                    |                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| • Boolean • General and trig math • Timers and counters • Array management • Diagnostic • Serial port and messaging • ASCII manipulation • Motion control | • General and trig math • Timers and counters • Bitwise logical • Advanced process • Advanced drive | • Step/action with embedded structured text • Transition with structure text comparisons • Simultaneous and selection branches • Stop element | • General and trig math • Timers and counters • Bitwise logical • Array management • Diagnostic • ASCII manipulation • Specialty CPU control • Motion control • Advanced process • Advanced drive | Instruction categories                         |
| • Graphical rungs • Unlimited rungs                                                                                                                       | • Graphical, free-form drawing • Unlimited sheets                                                   | • Graphical, free-form drawing • Unlimited grid space                                                                                         |                                                                                                                                                                                                   | Editor style  • Textual • Unlimited lines      |
| • Rung animation • Data value animation • Force status                                                                                                    | • Output and input pin data value animation                                                         |                                                                                                                                               | • Active steps animation • Auto display scroll • Branch/transition force status                                                                                                                   | Monitoring • Tag watch pane • Context coloring |
| • Tag • Rung                                                                                                                                              | • Tag • Text box                                                                                    | • Text box                                                                                                                                    | • Tag • Embedded structured text comments that are stored in CPU • Multi-line • End if line • Comments that are stored in CPU                                                                     | Comments                                       |

<!-- image -->

Function Block Diagram functions introduced in Logix Designer application, version 32.00.00 can execute faster, require less memory, and be easier to program and maintain than their FBD counterparts. Most operators in relay ladder logic are available in FBD as functions.

## Programming Methods

## Benefits

- One copy of code is faster to develop
- Slowest execution time because all tag references are calculated at runtime
- Can be difficult to maintain because the data monitor is not synchronized to execution
- Unsigned integer indexes are faster than signed integers

<!-- image -->

The capabilities of the controllers make different programming methods possible. There are trade-offs to consider when selecting a programming method.

## Inline Duplication

Write multiple copies of the code with different tag references.

## Advantages

- Fastest execution time because all tag references are defined before runtime
- Easiest to maintain because rung animation matches tag values

## Disadvantages

- Uses more memory
- Requires more time to create and modify

<!-- image -->

## Indexed Routine

Write one copy of code and use indexed references to data stored in arrays.

<!-- image -->

## Buffered Routine

Copy the values of an array into tags to directly reference these buffer tags.

<!-- image -->

## Benefits

- One copy operation can occur faster than multiple index offsets
- Minimizes the need to calculate array offsets at runtime
- The amount of code increases, but so do the benefits
- Can be difficult to maintain because the data monitor is not synchronized to execution

<!-- image -->

## Controller Prescan of Logic

On transition to Run mode, the controller prescans logic to initialize instructions. The controller resets all state-based instructions, such as outputs (OTE) and timers (TON). Some instructions also perform operations during prescan. For example, the ONSR instruction turns off the storage bit. For information on prescan, see the following resources:

- Logix 5000 Controllers General Instructions Reference Manual, publication 1756-RM003 .
- Logix 5000 Controllers Process Control and Drives Instructions Reference Manual, publication 1756-RM006 .

During prescan, input values are not current and outputs are not written.

| Prescan Affects              | Description                                                                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relay ladder logic           | The controller resets non-retentive I/O and internal values.                                                                                                                                                                                                |
| Function block diagram logic | Along with resetting non-retentive I/O and internal values, the controller also clears the EnableIn parameter for every function block diagram.                                                                                                             |
| Structured text logic        | The controller resets bit tags and forces numeric tags to zero. Use the bracketed assignment operator ([:=]) to force a value to be reset during prescan. If you want a tag that is left in its last state, use the non-bracketed assignment operator (:=). |
|                              | Sequential function chart logic Embedded structured text follows the same rules as listed previously.                                                                                                                                                       |

Prescan differs from first scan in that the controller does not execute logic during prescan. The controller executes logic during first scan. The controller sets S:FS for one scan:

- During the first scan that follows prescan.
- During the first scan of a program when it has been uninhibited.
- Each time a step is first scanned (when step.FS is set). You can view the S:FS bit being set only from the logic that is contained in actions that execute during the first scan of their parent step (N, L, P, and P1).

## Add-On Instruction Prescan Logic

An Add-On Instruction prescan logic routine executes after the main logic executes in Prescan mode. Use the prescan logic to initialize tag values before execution. For example, set a PID instruction to Manual mode with a 0% output before its first execution.

When an Add-On Instruction executes in Prescan mode, any required parameters have their data passed.

- Values are passed to Input parameters from their arguments in the instruction call.
- Values are passed out of Output parameters to their arguments defined in the instruction call.

## Custom Tag Initialization During Prescan

An Add-On Instruction prescan routine allows you to perform custom tag initialization after the system-defined initialization is complete. You can use this feature to customize the prescan initialization of any tag in the project.

When an Add-On Instruction is executed during prescan, the system-defined initialization is completed by executing the Add-On Instruction logic routine in prescan mode, and then the Add-On Instruction prescan routine is executed in normal mode to allow customized initialization.

## To accomplish:

- Create an Add-On Instruction with an empty logic routine (such as "PrescanInit"). Define an inout parameter for each tag you wish to initialize and add the custom initialization to the prescan routine.
- Add an always false invocation of your Add-On Instruction ("AFI( ) PrescanInit( )" ) to one of your routines, passing in the tags you wish to initialize.

## Benefits of Add-On Instruction Prescan Versus First Scan Routine To Initialize Tags

- Using S:FS requires your initialization to be done in the main routine of each program (or in a routine that will be executed during first scan).

Add-On Instruction-based initialization is done during prescan (before any logic executes) so the invocation can be placed anywhere, even in a fault handler. Fault handlers are prescanned before any other logic and, thereafter, only execute if a major fault is encountered (where scan time is not a concern).

## Additional notes:

- S:FS can be true in scenarios other than program-to-run. For example, in logic that is invoked from an SFC step or when a program is uninhibited.
- Since all parameters are inouts, the backing tag is small (on the order of 4 bytes).
- A false invocation of an Add-On Instruction that has no false routine that is defined is skipped so the impact on scan time is extremely small (if you invoke it from a fault handler, there is no impact to the scan time of the project).
- A first scan initialization routine must be defined and invoked for each program, and is required to initialize all desired tags.
- An Add-On Instruction is global and can be invoked from any program so it can be defined once and invoked from each program. This assumes that the tags need to be initialized in the same way (for example, each program represents one of a set of replicated cells).
- For program-scoped tags, the invocation would need to be within the parent program (or the program-scoped fault handler).
- For cases where a different type of initialization is required, another Add-On Instruction could be created. Controller-scoped tags could be initialized in a program or in the controller fault handler.
- If desired, you could expand this approach to make the initialization more flexible/ reusable: For example, you could define additional input parameters to pass the values you want the tags to be initialized to.
- If you configure your tags in an array or UDT, you could implement a generic initializer with only two inout parameters: the first parameter being the active tags that are initialized, and the second parameter being a duplicate array/structure containing the initial values (the prescan routine would use a COP instruction to copy the initial values to the active tags).

## Controller Postscan of SFC Logic

Limitations of Add-On Instruction Prescan Initialization

On ControlLogix 5590, GuardLogix® 5580, and Compact GuardLogix 5380 controllers, the maximum number of inouts that can be defined for an AOI is 64.

If this limit is a problem:

- You could create multiple prescan Add-On Instructions.
- You could organize tags in UDTs or arrays so they can all be passed into one inout parameter.

For information related to First Scan Safety Tag Initialization, see the GuardLogix 5580 and Compact GuardLogix 5380 Controller Systems Reference Manual, publication 1756-RM012 .

SFCs support an automatic reset option that performs a postscan of the actions that are associated with a step once a transition indicates that the step is completed. Also, every Jump to Subroutine (JSR) instruction causes the controller to postscan the called routine. During this postscan:

- Output energize (OTE) instructions are turned off and non-retentive timers are reset.
- In structured text code, use the bracketed assignment operator ([:=]) to have tags reset.
- In structured text code, use the non-bracketed assignment operator (:=) to have tags that are left in their last state.
- Selected array faults, that is, 4/20 and 4/83, can be suppressed. When the fault is suppressed, the controller uses an internal fault handler to clear it. Clearing the fault causes the postscan process to skip the instruction containing the fault and continue with the next instruction. This occurs only when SFC instructions are configured for automatic reset.

## Add-On Instruction Postscan Logic

When an Add-On Instruction is called by logic in an SFC Action and the Automatic Reset option is set, the Add-On Instruction executes in Postscan mode. An Add-On Instruction postscan routine executes after the main logic executes in Postscan mode. Use the postscan logic to reset internal states and status values or to disable instruction outputs when the SFC action completes.

## Timer Execution

There are two options when it comes to Timers in the controller.

- The traditional Timer uses the TIMER data type whose ACC member reflects elapsed time in milliseconds as a 32-Bit integer (DINT) value and is displayed as such (for example 2250).
- With 5590 controllers or later, a new kind of Timer based on the TIMER\_T data type is introduced. Its ACC member stores elapsed time as a 64-bit integer (TIME) value in microseconds but is displayed following the format that is described in feature 3a in Table 8 - Duration literals of IEC 61131-3 Edition 4 (e.g., T#2s\_250ms).

While TIMER\_T's ACC and PRE members have microsecond resolution, you only see millisecond changes due to the real-time clock implementation.

Timers internally store 22 bits of real-time clock value in milliseconds each time they are scanned. The next time through, they compare this stored value against the current clock and then adjust the ACC value by the difference. This results in a maximum elapsed time of 69 minutes until overlap occurs for TIMER datatype.

If program execution skips timers, it appears as if the timers pause. Actually, the timers are overrunning themselves. Depending on when the timer logic next executes, the lost time ranges from 0…69.905 minutes.

Program execution can skip executing timers due to the following:

- Subroutine not being called
- Jumping over code
- SFC action
- Inactive SFC step
- Event or periodic task not executing
- Equipment phase state routines

## SFC Step Timer Execution

An SFC step timer stores the clock time each time the step executes. On subsequent scans of the step, the controller compares the current clock time with the last scan and updates the step timer's ACC by the difference.

When you pause an SFC and then release the SFC, the step timer jumps forward by the duration of the pause. If you want a step timer to remain at its position during a pause:

- Latch a recovery bit when the chart pause is released.
- Add an action to the step to store the step timer's .ACC value and restore that value when the pause recovery bit is set.

<!-- image -->

## Edit an SFC Online

When you edit an SFC online, the software initially changes the offline project. When you accept the changes, they are downloaded to the controller. If you transition the controller to test or untest edits, the controller resets the SFC and starts execution at the initial step. If you edit an SFC online, do the following:

- Plan when you test or untest edits to coincide with the SFC executing the initial step.
- Place structured text logic in subroutines to minimize the impact of online edits.
- Use an SFR instruction to shift SFC execution to the desired step programmatically.

In some cases, this can result in the SFC being out of sync with the equipment. Program logic in the initial step to check the last state and use an SFR instruction to change to the appropriate step, if needed. One method is to set an index number in an action of each step. Then when the restart occurs, use the SFR instruction to jump to appropriate step based on the index value.

As of firmware revision 18, the following online edits to an SFC no longer reset the SFC to the initial step:

- Modified structured text in actions and transitions
- Physically moved steps, actions, and transitions on SFC sheets without changing the wiring
- Added, deleted, or modified text and description boxes
- Modified indicator tags

## Notes:

## Guidelines for Code Reuse

| Guideline                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use program parameters to share data between programs.                                                                     | Program parameters: • Are publicly accessible outside of the program. • Support external HMI external access on an individual basis for each parameter. Direct access lets the user reference program parameters in logic without configuring parameters in the local program. For example, if Program A has an output parameter that is called Tank_Level, Program B can reference the Tank_Level parameter in logic without creating a corresponding parameter to connect to Program A.                                                                                                                                                       |
| Use user-defined data types (UDTs) to group data.                                                                          | Within a UDT: • You can mix data types. • The tag names that you assign self-document the structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Use Add-On Instructions to create standardized modules of code for reuse across a project.                                 | Use an Add-On Instruction to: • Encapsulate specific or focused operations, such as a Motor or Valve action. A Conveyor or Tank action is better managed as a routine. • Create extensions to the base controller instructions. For example, create an Add-On Instruction to execute an SLC™ 500 or PLC controller instruction not available in the Logix 5000® controllers. • Encapsulate an instruction from one language for use in another language. For example, create a function block PIDE instruction for use in relay ladder.                                                                                                         |
| Use partial import/export programs, routines, Add-On Instructions, and code segments to create libraries of reusable code. | Partial import and export of routines and programs: • Provides more control over the scope of what is extracted from the project. • Provides reusable code for larger machine, cell, or unit control. • Promotes collaboration between multiple engineers, code standardization, and reuse. The export .L5X file includes all pertinent information, including program configuration, code, user-defined data types, tags, and descriptions, in an XML-formatted, ASCII text file. Use partial import/export to: • Distribute code separately from the project .ACD file. • Edit and create programs and routines by using other editing tools. |
| Use subroutines to reuse code within a program.                                                                            | Subroutines: • Can be created and used in standard and safety applications. • Pass User-Defined Structures (UDT). • Pass all input and output Parameters by value. • Subroutines require the most overhead to pass parameters when called. • Can only be called from within the program they reside.                                                                                                                                                                                                                                                                                                                                            |

## Modular Programming Techniques

Modular programming guidelines support the delivery of standardized programming structures, conventions, configurations, and strategies. The goal of modular programming is to provide consistency.

- Faster and easier development of application software
- Faster and easier testing of application software
- More reliable application software
- Improved maintenance and operation of application software
- Improved interoperability with other equipment and systems

This chapter applies to these controllers.

| Controller Family Controller Names                                          |
|-----------------------------------------------------------------------------|
| 5590 controllers ControlLogix® 5590 controllers                             |
| 5580 controllers ControlLogix 5580 and GuardLogix® 5580 controllers         |
| 5380 controllers CompactLogix® 5380 and Compact GuardLogix 5380 controllers |
| 5570 controllers ControlLogix 5570 and GuardLogix 5570 controllers          |
| 5370 controllers CompactLogix 5370 and Compact GuardLogix 5370 controllers  |
| 5480 controllers CompactLogix 5480 controllers                              |

<!-- image -->

## Naming Conventions

The following conventions are guidelines to help make an engineering library more reusable by other developers. These guidelines also help the resulting applications have a more consistent look and feel.

- Names that are meaningful (and readable) to people who use the application as a later date are most effective.
- Names use controller memory and have limited length, so keep them short by using abbreviations and acronyms. Use mixed case rather than underscore characters to indicate words.
- When you use acronyms, use those that are common or provided by industry standards.

Names for controller logic components must follow these guidelines.

- The name must start with a letter, either upper or lower case
- The name can contain as many as 40 characters; any mix of upper case letter, lower case letters, numbers, and underscore characters
- Case is not significant. The controller interprets Mix\_Tank the same and mix\_tank. However, the software displays the case as entered
- Underscores are significant. The controller interprets AB\_CD as unique from A\_BCD
- You cannot have two or more underscore characters in a row
- The name cannot end with an underscore.

| Component Name     | Recommendations                                                                                                                                                                                                                                                                                                                                                                                                  | Recommendations                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controller         | Area, unit, or units the controller controls, underscore, type of controller Example:                                                                                                                                                                                                                                                                                                                            | Area, unit, or units the controller controls, underscore, type of controller Example:                                                                                                                                                                                                                                                                                                                            |
| Controller         | Area/Unit + Type                                                                                                                                                                                                                                                                                                                                                                                                 | Controller Name: Mixing:ControlLogix®                                                                                                                                                                                                                                                                                                                                                                            |
| Controller project | Controller name, the letter C, 1-digit major revision number, underscore, 2-digit minor revision number Example: Increment the minor revision number for any documented engineering change according to the code in the controller (for example, the code for minor process or equipment changes). Project in controller Mixing_CLX, Major Revision 1, Minor Revision 02 Application Name: Mixing_CLX_C2_092.ACD | Controller name, the letter C, 1-digit major revision number, underscore, 2-digit minor revision number Example: Increment the minor revision number for any documented engineering change according to the code in the controller (for example, the code for minor process or equipment changes). Project in controller Mixing_CLX, Major Revision 1, Minor Revision 02 Application Name: Mixing_CLX_C2_092.ACD |
| Controller project | Prefix with the abbreviation of the type of tag Examples: Interprocessor communication tag IPC_                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Controller project | Input tag                                                                                                                                                                                                                                                                                                                                                                                                        | I_                                                                                                                                                                                                                                                                                                                                                                                                               |
| Controller project | Output tag                                                                                                                                                                                                                                                                                                                                                                                                       | O_                                                                                                                                                                                                                                                                                                                                                                                                               |
| Tag                | Remote I/O tag                                                                                                                                                                                                                                                                                                                                                                                                   | RIO_                                                                                                                                                                                                                                                                                                                                                                                                             |
| Controller project | Control module class tag                                                                                                                                                                                                                                                                                                                                                                                         | Device ID_                                                                                                                                                                                                                                                                                                                                                                                                       |
| Controller project | Equipment module class tag EM_                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Controller project | Equipment phase class tag                                                                                                                                                                                                                                                                                                                                                                                        | EP_                                                                                                                                                                                                                                                                                                                                                                                                              |
| Controller project |                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                  |

| Component Name              | Recommendations                                                                                                                                                                        | Recommendations                                                                                                                                                                        |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Controller name, underscore, abbreviation of rack location (L=local, R=remote), underscore, the letter S, 2-digit slot number, underscore, abbreviation of function Example Functions: | Controller name, underscore, abbreviation of rack location (L=local, R=remote), underscore, the letter S, 2-digit slot number, underscore, abbreviation of function Example Functions: |
|                             | Analog input                                                                                                                                                                           | AI                                                                                                                                                                                     |
|                             | Analog output                                                                                                                                                                          | AO                                                                                                                                                                                     |
|                             | Discrete input                                                                                                                                                                         | DI                                                                                                                                                                                     |
|                             | Discrete output                                                                                                                                                                        | DO                                                                                                                                                                                     |
|                             | Analog input/output combination AIO                                                                                                                                                    |                                                                                                                                                                                        |
|                             | Discrete input/output combination DIO                                                                                                                                                  |                                                                                                                                                                                        |
|                             | Analog/discrete input/output combination ADIO                                                                                                                                          |                                                                                                                                                                                        |
|                             | Serial data                                                                                                                                                                            | SIO                                                                                                                                                                                    |
|                             | Motion data                                                                                                                                                                            | MIO                                                                                                                                                                                    |
|                             | DeviceNet® data                                                                                                                                                                        | DNET                                                                                                                                                                                   |
|                             | EtherNet/IP™ data                                                                                                                                                                      | ENET                                                                                                                                                                                   |
|                             | ControlNet®                                                                                                                                                                            | CNET                                                                                                                                                                                   |
| I/O or communication module | Remote I/O data                                                                                                                                                                        | RIO                                                                                                                                                                                    |
|                             | Examples:                                                                                                                                                                              | Examples:                                                                                                                                                                              |
|                             | Mixer123 Controller, Local chassis, Slot 4, Analog Output                                                                                                                              | Module Name: M123_CLX_L00_S04_AO                                                                                                                                                       |
|                             | Mixer123 Controller, Local chassis, Slot 12, Discrete Output                                                                                                                           | Module Name: M123_CLX_L00_S12_DO                                                                                                                                                       |
|                             | Mixer123 Controller, Remote chassis #1, Slot 1, Analog Input                                                                                                                           | Module Name: M123_CLX_R01_S01_AI                                                                                                                                                       |
|                             | Mixer123 Controller, Remote chassis #1, Slot 2, Analog Output                                                                                                                          | Module Name: M123_CLX _R01_S02_AO                                                                                                                                                      |
|                             | Mixer123 Controller, Remote chassis #2, Slot 5, Discrete Input                                                                                                                         | Module Name: M123_CLX _R02_S05_DI                                                                                                                                                      |
|                             | Mixer123 Controller, Remote chassis #2, Slot 6, Discrete Output                                                                                                                        | Module Name: M123_CLX _R02_S06_DO                                                                                                                                                      |
|                             | Mixer123 Controller, Local chassis, Slot 5, Remote I/O                                                                                                                                 | Module Name: M123_CLX _R02_S06_RIO                                                                                                                                                     |

## Parameter Name Prefixes

Programming structures, such as Add-On Instructions and programs support parameters for passing values. The convention for prefixes is to abbreviate the function of the parameter to three letters and an underscore, followed by additional text to clarify the specific function.

| Parameter Function Prefix   |      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command                     | Cmd_ | Designates a command input, either from the operator via the HMI or from the program. Examples: • Cmd_Reset: Clear faults and reset the process • Cmd_JogServo: Jog a servo axis • Cmd_FillTank: Fill a tank with a liquid                                                                                                                                                                                                                                                                                                                                                                     |
| Configuration               | Cfg_ | Designates a configuration value for the structure. Enter from the HMI or as part of a recipe. Examples: • Cfg_JogDirection: Selects the direction a servo jogs: 0=Positive, 1=Negative • Cfg_BulkFill: Selects the fill rate to use: 0=Slow Rate, 1=Fast Rate • Cfg_UserUnits: Selects the measure of volume to use: 0=mm, 1=m, 2=gal • Cfg_EnableInterlocks: Enable interlock functionality • Cfg_EnablePermissive: Enable permissive functionality                                                                                                                                          |
| Status                      | Sts_ | Status of the process within the structure. Examples: • Sts_Alarm: An alarm condition (such as a HI/LOW alarm) exists within the process • Sts_ER: An error with an instruction execution within the process has been detected • Sts_IndexComplete: The servo index move within the process has completed • Sts_FillInProcess: The tank filling process is underway                                                                                                                                                                                                                            |
| Error                       | Err_ | If the Sts_ER bit is on, the Err_ parameter indicates the actual error. This can be either a bit level or value level indication. • Bit-level error recording supports multiple errors simultaneously, but can require many indicators to support all error states. • Value-based error annunciation supports a large quantity of errors within one indicator. However, this approach requires that errors are annunciated one at a time. Examples: • Err_Value: A nonzero value indicates an error condition • Err_PCamCalcFault: Indicates that an error has occurred in an MCCP             |
| Alarm                       | Alm_ | If the Sts_Alm bit is on, the Alm_ parameter indicates which alarm is occurring. This can be either a bit-level or value-level indication. • Bit-level alarming supports multiple alarms simultaneously, but can require many indicators to support all alarm states. • Value-based alarm annunciation supports a large quantity of alarms within one indicator. However, this approach requires alarms to be annunciated one at a time. Examples: • Alm_Value: A nonzero value indicates an alarm condition • Alm_TankHI: Indicates that a HI level condition has been detected within a tank |
| Input                       | Inp_ | Real-time data used to drive the process. Designates a connection either to a real input point, a control device, or to data received from other processes. Examples: • Inp_ServoPosition: Variable providing the input value for a position of a servo • Inp_ServoRegistrationPosition: Input of the registration position of the servo • Inp_InterlockOK: Input indicating external interlocks are met • Inp_TankLevel: Variable providing the analog input for a tank’ level • Inp_TankLevelFillRate                                                                                        |

| Parameter Function Prefix   |       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output                      | Out_  | Real-time data driven from the process. Designates a connection to a real output point, a control device, or to data sent to other processes. Examples: • Out_GlueGun1: Output signal to turn of Glue Gun 1 • Out_ServoCorrectionDistance: Output of a servo registration correction distance • Out_OverflowValve: Output signal to open the Overflow Valve • Out_TankLevelError: Output of a difference between target and actual fill level of a tank |
| Reference                   | Ref_  | Complex data structures that combine input and output data. These structures pass data into a structure, where some process is performed. The results are then loaded back into the structure to be passed out of Add-On Instruction for use elsewhere. Example: Ref_PositionCamRecovery: Provides the data set for calculating a Position Cam with all offsets factored in, and the resulting Position Cam Profile to run in an MAPC instruction       |
| Parameter                   | Par_  | Variables that are received from an external source that can be internal or external to the program. Examples: • Par_MachineSpeed: Provides a machine's running speed • Par_TargetFillLevel: Provides a tank's target fill level                                                                                                                                                                                                                        |
| Set point                   | Set_  | Variables that are received from an operator or HMI and are not part of an external source. Examples: • Set_MachineMaxSpeed: Provides the setting for a machine's maximum permissible speed • Set_TankHILevel: Provides the setting for a tank's HI alarm limit                                                                                                                                                                                         |
| Value                       | Val_  | Designates a value that might not be the primary output of the structure.                                                                                                                                                                                                                                                                                                                                                                               |
| Report                      | Rpt_  | Designates a value that is typically used for reporting.                                                                                                                                                                                                                                                                                                                                                                                                |
| Information                 | Inf_  | Non-functional data such as a revision level or name for displaying a faceplate.                                                                                                                                                                                                                                                                                                                                                                        |
| Ready                       | Rdy_  | Command-ready bits that are typically Booleans that are calculated inside the control routines to reflect whether the routine let states change commands. Used with HMI faceplates to enable or disable command buttons.                                                                                                                                                                                                                                |
| Program Command (optional)  | PCmd_ | Command input for commands typically issued by the application program. Examples: • PCmd_ProgReq - Request for Program Mode made by the application (as opposed to Cmd_ProgProgReq) • PCmd_AutoReq - Request for Auto Mode made by the application (as opposed to Cmd_ProgAutoReq)                                                                                                                                                                      |
| Operator Command (optional) | OCmd_ | Command input for commands typically issued by the operator via the HMI. Examples: • OCmd_ProgReq - Request for Program Mode made by the operator (as opposed to Cmd_OperProgReq) • OCmd_AutoReq - Request for Auto Mode made by the operator (as opposed to Cmd_OperAutoReq)                                                                                                                                                                           |

## Guidelines for Program Parameters

Program parameters define a data interface for programs to facilitate data sharing. Data sharing between programs can be achieved either through pre-defined connections between parameters or directly through a special notation. Unlike local tags, all program parameters are publicly accessible outside of the program. Additionally, HMI external access can be specified on individual basis for each parameter.

Standard (non-Safety) parameters can be created, edited, and deleted while online with the controller. The following exceptions apply:

- Parameters cannot be deleted while online if they are connected/bound to other parameters, or if the control logic references them.
- InOut parameters cannot be deleted while online
- InOut bindings can only be changed online through a Partial Import Online (PIO) operation

A safety parameter cannot be connected with or bound to a standard parameter or controllerscoped tag. A safety connection cannot be created, modified, or deleted in a safety-locked project. Input, Output, and Public parameters support the External Access attribute. InOut parameters do not.

| Program Parameter Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input                           | • Input parameters (including members) can only support ONE connection. Only one source can be delivering the value to the input parameter. • Input Parameter values are refreshed before each scan of a program. The values do not change during the logic execution so you do not need to write code to buffer inputs. • A program can write to its own input parameters. • Data values for Output parameters that are connected to controller scope tags or Public parameters are copied after the scan of a program. In a project with multiple tasks, the data copy for a parameter that is of type BOOL, SINT, INT, DINT, LINT, or REAL will not be interrupted. A task switch can interrupt the data copy from an Output parameter to a controller scope tag or Public parameter, or any other predefined or user-defined data type. |
| Output                          | • Output parameters (including members) can support multiple connections. For example, lets assume you have a BOOL input parameter in Program A and Program B named Input1a and Input1b. You can connect an output parameter in Program C to Input1a AND Input1b. As stated earlier, this is often referred to as fanning. • Output Parameter values are refreshed AFTER each scan of a program. Updated output parameter values are NOT available to the parameters connected to that output parameter until the program execution is complete. • Output parameters that are connected to Public parameters or controller scope tags are copied (pushed) at the end of the program execution. • An Output parameter can ONLY be connected to an InOut parameter if both the Output and InOut parameters are configured as Constants.       |
| InOut                           | • InOut parameters can only support ONE connection. You cannot configure connections to any member of an InOut parameter. • InOut parameters are passed by REFERENCE, which means they simply point to the base tag. In other words, when an InOut parameter is used in logic, the current value of the parameter that is connected to the InOut Parameter is used. • An InOut parameter can ONLY be connected to an Output parameter if both the Output and InOut parameters are configured as Constants. See the tool tip for Output Parameters for a more detailed explanation. • InOut parameters CANNOT be changed online, unless using the Partial Import Online (PIO).                                                                                                                                                               |
| Public                          | • Public parameters can support MULTIPLE connections. You can configure connections to the base Public parameter or any member of a Public parameter. This includes User-Defined Structures. • Public parameters are updated when the source is updated. In other words, when a Public parameter value updates, it is immediately available to any higher priority tasks that are connected to that parameter. • Public parameters can be aliased to Controller Scope Tags. If this functionality is desired, remember that the alias update is asynchronous to program execution. The public parameter contains the real-time value of the controller scope tag.                                                                                                                                                                           |

## Comparison of Program Parameters and Add-On Instructions

| Comparison                      | Program Parameters                                                                                                                                                                                                    | Add-On Instructions                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accessibility                   | Within program (multiple copies)                                                                                                                                                                                      | Anywhere in controller (single copy)                                                                                                                        |
| Parameters                      | Input / Output (pass by value), InOut (pass by reference), Public (pass by value)                                                                                                                                     | Input / Output (pass by value), InOut (pass by reference)                                                                                                   |
| Numeric parameters              | • Automatic data type conversion for Input and Output parameters • InOut parameters must match declared type exactly                                                                                                  | • Automatic data type conversion for Input and Output parameters • InOut parameters must match declared type exactly                                        |
| Parameters data types           | Atomic, strings, arrays, structures                                                                                                                                                                                   | • Atomic data types as In or Out parameters • LINT, user-defined, and structure data types as InOut parameters                                              |
| Parameter checking              | None, user must manage                                                                                                                                                                                                | Verification checks                                                                                                                                         |
| Data encapsulation              | All data at program or controller scope (accessible to anything). Programs can talk directly and exchange data between them. Local tags remain private to the Program. Cannot access Local Tags, only the parameters. | Local data is isolated (only accessible within instruction)                                                                                                 |
| Monitor/debug                   | Online editable.                                                                                                                                                                                                      | Logic that is animated with data from one calling instance                                                                                                  |
| Supported programming languages | FBD, LD, SFC, ST                                                                                                                                                                                                      | FBD, LD, ST                                                                                                                                                 |
| Callable from                   | FBD, LD, SFC, ST                                                                                                                                                                                                      | FBD, LD, SFC, ST                                                                                                                                            |
| Protection                      | —                                                                                                                                                                                                                     | Locked and View Only                                                                                                                                        |
| Documentation                   | —                                                                                                                                                                                                                     | Instruction description, revision information, vendor, rung, textbox, line, extended help                                                                   |
| Execution performance           | • Programs can talk directly and exchange data between them. • InOut passed by reference                                                                                                                              | • Call is more efficient • InOut passed by reference                                                                                                        |
| Memory use                      | Compact. One Public parameters can be connected or bound to multiple Input, Output, or InOut parameters to form a shared memory space.                                                                                | • Call requires more memory • All references need additional memory                                                                                         |
| Edit                            | Online editable, and supports sub-element connections. Copy / Paste Programs without disturbing parameter configuration.                                                                                              | Code modifications are limited to offline in the project file and require a new download Data values that are associated can be modified online and offline |

## Guidelines for Subroutines

Follow these parameter guidelines for subroutines.

| Guideline                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use FBD functions over FBD function blocks                                  | FBD functions are faster, use less memory, and are easier to program than FBD function blocks tasked to perform the same behavior.                                                                                                                                                                                                                                                                                                                                               |
| Input and Return parameters depend on the subroutine logic.                 | If the subroutine must know the previous state of any Return parameters (the values are used elsewhere in the project), these values should also be Input parameters: • If the subroutine contains latch/unlatch logic (holding circuits), intended outputs of the subroutine should be passed into and returned from the subroutine. • If the subroutine does not contain latch/unlatch logic, intended outputs of the subroutine only need to be returned from the subroutine. |
| Pass complete timers in and out of subroutines.                             | If a subroutine needs a timer, pass the complete timer tag to the subroutine as an input and return the complete timer tag as an output. Store the timer in a buffer tag outside of the subroutine.                                                                                                                                                                                                                                                                              |
| Create a user-defined tag to pass large numbers Input and Output parameters | Create and pass a UDT if you have several Input and Output parameters to save on execution time. The more parameters that you pass, the fewer nested JSRs you can perform.                                                                                                                                                                                                                                                                                                       |
| Data types must match                                                       | For each parameter in an SBR or RET instruction, use the same data type (including any array dimensions) as the corresponding parameter in the JSR instruction. Using different data types can produce unexpected results.                                                                                                                                                                                                                                                       |

## Guidelines for User-defined Data Types

A UDT lets you organize data logically, so that all the data associated with a device, such as a pressure transmitter or variable frequency drive, can be grouped.

- You can mix data types, such as real or floating point values, counters, timers, arrays, Booleans, and other UDTs, within one UDT.
- You can copy a UDT from one project to another, and even from one Logix controller type to another.
- A UDT is self-documenting based on the tag names that you assign and provides a logical representation of parts or subsystems.

## Naming Conventions for User-Defined Data Types

Element

Prefix\_

UDT name

## Examples

| Inventory tracking tag                                     | UDT_InventoryTracking   |
|------------------------------------------------------------|-------------------------|
| Clean-in-place system                                      | UDT_CIP                 |
| Two-state valve control module in control module UDT_CMV2S |                         |
| Water addition in equipment module                         | UDT_EM                  |

## UDT Member Order Impact

The order in which members are listed in the UDT can have a significant impact on memory use if a diverse set of data types are needed. The member data types also affect the alignment requirements for the UDT. If you are concerned about memory usage, then apply these guidelines:

- Group like data type members together.
- Group the ordering from largest to smallest.
- Review layout and adjust order to reduce padding.

These guidelines make the packing of members into the data table that is allocated for the UDT more efficient and as small as possible. However, if your larger concern is to group members based on functionality, then apply the guidelines only within the groups.

Description

UDT\_

Function or purpose of the UDT

Generally, a UDT size is in multiples of 4 bytes and aligned on 4-byte boundaries. However, if a UDT contains any 64-bit members, then the size of the UDT is a multiple of 8 bytes and aligned on 8-byte boundaries. Members who themselves are UDTs follow these same alignment rules. Padding bytes are added as needed to enforce alignment.

<!-- image -->

<!-- image -->

| Rule                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Each elementary data type of size n is n-byte aligned. Padding bytes are inserted to enforce the alignment.                                                                                                                               | DINT members start on 4-byte alignment. LINT members start on 8-byte alignment. struct t_UDT12 { SINT sintMem; char pad0; INT DintMem; SINT sintMem2; char pad1; char pad2; char pad3; DINT dintMem; char pad4; char pad5; char pad6; char pad7; LINT lintMem; };                                                                                                  |
| The UDT size is in multiples of 4 bytes. If the UDT contains a 64-bit member, then the UDT size is multiples of 8 bytes. Padding bytes are inserted at end of the UDT to enforce the size.                                                | struct t_UDT6 { SINT sintMem; SINT sintMem2; SINT sintMem3; SINT sintMem4; SINT sintMem5; char pad0; char pad1; char pad2; }; struct t_UDT7 { SINT sintMem; SINT sintMem2; SINT sintMem3; SINT sintMem4; char pad0; char pad1; char pad2; char pad3; LINT lintMem; SINT sintMem5; char pad4; char pad5; char pad6; char pad7; char pad8; char pad9; char pad10; }; |
| If the UDT member is array, then it is at least 4-byte aligned and padding is inserted at end of the member to make sure that it ends at an at least 4-byte aligned boundary. It is 8-byte aligned when the array element type is 64-bit. | struct t_UDT9 { SINT sintMem; char pad0; char pad1; char pad2; SINT sintArray[2]; char pad3; char pad4; INT intMem; char pad5; char pad6; };                                                                                                                                                                                                                       |

## Guidelines for Add-On Instructions

An Add-On Instruction encapsulates commonly used functions or device controls. It is not intended for use as a high-level hierarchical design tool. Once an Add-On Instruction is defined in a project, it behaves similarly to the built-in instructions that are already available in the programming software. The Add-On Instruction appears on the instruction toolbar and in the instruction browser.

| Guideline                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create Add-On Instructions in relay ladder, function block diagram, or structured text languages.                  | Supports all Add-On Instructions and most built-in instructions. Excludes JSR/SBR/RET, JXR, FOR/BRK (relay ladder), SFR, SFP, SAR, IOT, and EVENT instructions. GSV/SSV instructions in an Add-On Instruction cannot reference the Module, Message, Axis, Motion Group, or Coordinate System class names. Add-On Instructions support function block, relay ladder, and structured text programming languages. Each of the Add-On Instruction logic areas can be any language. For example, the main logic can be function block and the prescan logic can be relay ladder. You can create safety Add-On Instructions in a safety task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| An Add-On Instruction supports parameters: • Input (copied in) • Output (copied out) • InOut (passed by reference) | • For Version 24 and earlier, you are limited to 512 total parameters: Input parameter + Output parameter + local tags (no limit on the number of InOut parameters) • For Version 28 and later, you are limited to 40 InOut parameters, but no limit on the number of Input or Output parameters) • 2 MB maximum data instance (parameters and locals) • Alarm, axis, axis group, coordinate system, message, motion group, and produced/consumed tags must exist at the program or controller scope and passed as an InOut parameter • Can include references to controller-scoped tags, program-scoped tags, and immediate values. • Input and Output parameters are limited to atomic (BOOL, SINT, INT, DINT, REAL) data types. Use the InOut parameter for LINT, user-defined, and structure data types. • DINT data types provide optimal execution. • Default values of parameters and local tags are used to initialize the data structure when a tag is created of the instruction’s data type. When an existing parameter or local tag's default value is modified, the existing tag instances for that instruction are not updated. When a parameter or local tag is added to the instruction definition, the tag's default value is used in the existing tags. |
| Create and modify offline only.                                                                                    | Online operation supports monitoring. Modifications to Add-On Instructions are made offline. Make changes once to the Add-On Instruction definition to affect all instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| An Add-On Instruction executes like a routine.                                                                     | A task with a higher execution priority can interrupt an Add-On Instruction. Use a UID/UIE instruction pair to make sure an Add-On Instruction’s execution is not interrupted by a higher priority task. If you have many parameters or specialized options, consider multiple Add-On Instructions. Calling many Add-On Instructions impacts scan time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| The code within an Add-On Instruction can access data that is specified only via parameters or defined as local.   | Copy the local data to a parameter if you want to programmatically access it outside of an Add-On Instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Use optional Scan mode logic to design, initialize, or reset the Add-On Instruction code.                          | An Add-On Instruction can have logic along with the main logic for the instruction. • Prescan logic executes on controller startup. • Postscan logic executes on SFC Automatic reset. • EnableInFalse logic executes when rung condition is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Apply code signatures to Add-On Instructions for revision control.                                                 | Add-On Instructions can be sealed with a code signature. Use the code signature for revision control and to identify any Ü ggy y changes. For safety controllers, the signature can be used to get TÜV certification for a safety Add-On Instruction. For more information, see the Logix 5000 Controllers Add-On Instructions Programming Manual, publication 1756-PM010 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Add-On Instruction Design Concepts

To be sure that specific data is passed into or out of the Add-On Instruction, use a required parameter. A required parameter must be passed as an argument in order for a call to the instruction for verification. To pass a required parameter in ladder diagrams and in structured text, specify an argument tag for the parameter.

- In a function block diagram, required Input parameters and Output parameters must be wired.
- In a ladder diagram, InOut parameters must have an argument tag.
- If a required parameter lacks an associated argument, the routine that contains the call to the Add-On Instruction does not verify.

## Naming Conventions for Add-On Instructions

| Component Name     | Recommendations                                                                                                                    | Recommendations                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Add-On Instruction | Start with the application name. Add a variant name, is applicable. Capitalize the first letter in all words in the name. Example: | Start with the application name. Add a variant name, is applicable. Capitalize the first letter in all words in the name. Example: |
| Add-On Instruction | PCam profile display                                                                                                               | PCamProfileDisplay                                                                                                                 |
| Add-On Instruction | Suffix with underscore AOI, if space permits. Example:                                                                             | Suffix with underscore AOI, if space permits. Example:                                                                             |
| Add-On Instruction | PCam profile display                                                                                                               | PCamProfileDisplay_AOI                                                                                                             |

## Comparison of Subroutines and Add-On Instructions

| Comparison                      | Subroutine                                                                                                                                                                                                     | Add-On Instructions                                                                                                                                                                                                           |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accessibility                   | Within program (multiple copies)                                                                                                                                                                               | Anywhere in controller (single copy)                                                                                                                                                                                          |
| Parameters                      | Pass by value                                                                                                                                                                                                  | Pass by value or reference via InOut                                                                                                                                                                                          |
| Numeric parameters              | No conversion, you must manage                                                                                                                                                                                 | Automatic data type conversion for Input and Output parameters InOut parameters must match declared type exactly                                                                                                              |
| Parameters data types           | Atomic, arrays, structures                                                                                                                                                                                     | • Atomic data types as In or Out parameters • LINT, user-defined, and structure data types as InOut parameters                                                                                                                |
| Parameter checking              | None, you must manage                                                                                                                                                                                          | Verification checks                                                                                                                                                                                                           |
| Data encapsulation              | All data at program or controller scope (accessible to anything) Local data is isolated (only accessible within instruction)                                                                                   |                                                                                                                                                                                                                               |
| Monitor/debug                   | Logic that is animated with mixed data from multiple calls                                                                                                                                                     | Logic that is animated with data from one calling instance                                                                                                                                                                    |
| Supported programming languages | FBD, LD, SFC, ST                                                                                                                                                                                               | FBD, LD, ST                                                                                                                                                                                                                   |
| Callable from                   | FBD, LD, SFC, ST                                                                                                                                                                                               | FBD, LD, SFC, ST                                                                                                                                                                                                              |
| Protection                      | Locked and View Only                                                                                                                                                                                           | Locked and View Only                                                                                                                                                                                                          |
| Documentation                   | Routine, rung, textbox, line                                                                                                                                                                                   | Instruction description, revision information, vendor, rung, textbox, line, extended help                                                                                                                                     |
| Execution performance           | • JSR/SBR/RET add overhead • All data is copied                                                                                                                                                                | • Call is more efficient • InOut passed by reference                                                                                                                                                                          |
| Memory use                      | Compact                                                                                                                                                                                                        | • Call requires more memory • All references need additional memory                                                                                                                                                           |
| Edit                            | Both code and data can be modified offline and online in a running controller                                                                                                                                  | Code modifications are limited to offline in the project file and require a new download Data values that are associated can be modified online and offline                                                                   |
| Import/export                   | All routines are imported/exported in the full project .L5K file (protected routines can be excluded or encrypted) Individual LD rungs and references and tags/UDTs can be imported/exported via the .L5X file | All Add-On Instructions are imported/exported in the full project .L5K file (protected instructions can be excluded or encrypted) Individual Add-On Instruction definitions and code are imported/ exported via the .L5X file |

## Comparison of Partial Import/Export and Add-On Instructions

| Comparison               | Partial Import/Export                                                                                                                                                                                                                                                                                                                                                                            | Add-On Instructions                                                                                                |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Logic                    | Any program, equipment phase, routine, Add-On Instruction, or user defined data type in the project can be imported/exported via .L5X file.                                                                                                                                                                                                                                                                                                                                                                                                  | Create once (single copy) and use anywhere in the same controller project.                                         |
| Controller accessibility | Import online with a running controller: • Add programs, routines, and Add-On Instructions • Existing programs and routines can be replaced • Create tags and UDTs • Name collisions are detected automatically and you are prompted to rename or bind to existing components • The data values in the controller are maintained and new tags have their values initialized from the import file | Existing Add-On Instructions can only be edited offline. New Add-On Instructions can be created online or offline. |
| Logic checking           | You resolve conflicts on import.                                                                                                                                                                                                                                                                                                                                                                 | The software verifies the components that you add to Add On Instruction as you create it.                                                                                                                    |
| Data                     | Editing member definitions of an Add-On Instruction maintains the values that are assigned to the parameters when: • Inserting, adding, or deleting members • Rearranging (moving) members • Renaming members • Changing the data types of members Values for members that are both renamed and moved in the same operation are not to be maintained.                                            | Local data is isolated (only accessible within the instruction).                                                   |

## Compare Controller Organizer and Logical Organizer

The Controller Organizer presents program logic how the controller executes the logic. The Logical Organizer is configurable to present program logic how the user views the system.

<!-- image -->

## Notes:

<!-- image -->

## Structure Logic According to Standards

The ANSI/ISA-88.01-1995 (R2006) standard is the most recognized and broadly adopted standard for modular equipment control. Complementing ISA-88.01 is the ISA-TR88.00.02 technical report, which is also known as PackML. The ISA-TR88.00.02 technical report comes from the Organization for Machine Automation and Control (OMAC). The OMAC provides examples of how to apply ISA-88.01 in discrete manufacturing segments.

ISA refers to the International Society of Automation, an ANSI recognized Standards Development Organization (SDO).

- ISA-88 refers to a specific set of ISA standards, of which ISA88.01 is a subset.
- SP88 refers to the ISA working member group responsible for the creation and publication of the ISA-88 standards.

ISA-88 provides these models to define and understand the automation control requirements for manufacturing plants.

|            | Model Description                                                                                                                                                                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Physical   | The physical model (also known as the equipment model) describes a hierarchical organization of equipment and the basic control capabilities that are associated with that organization. The physical model is a representation of the equipment in the plant that makes the product.                         |
| Procedural | The procedural model describes a multi-tiered, hierarchical model that defines the process capability and automation control in relation to the Physical Model to perform a task. The procedural model is a representation of how to use the equipment (described in the physical model) to make the product. |

## Physical Model

The physical model (also known as the equipment model) describes a hierarchical organization of equipment and the basic control capabilities that are associated with that organization. The physical model is a representation of the equipment in the plant that is used to make the product.

<!-- image -->

The physical model defines the automation components within a given environment, and determines modular areas and component interactions.

The physical model shows that an enterprise can contain multiple sites, and a site can contain multiple areas, down to the equipment modules and control modules that implement the manufacturing process.

| Physical Model Component Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enterprise                             | The company that owns the facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Site                                   | The location of one facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Process cell                           | A collection of one or more units that are linked together to perform a task or multiple tasks of the process for one or more products in a defined sequence. A process cell contains the units, equipment modules, and control modules that are needed to make one or more batches.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Unit (or machine)                      | A collection of related equipment modules and control modules that execute one or more processing activities. The unit corresponds to the logical grouping of mechanical and electrical assemblies that historically has been called a machine. The term unit can apply to either a single-function machine or a multi-functional machine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Equipment module                       | A functional group of control modules, equipment modules, or both that execute a finite number of activities. The primary purpose of control in an equipment module is to coordinate the functions of other equipment modules and lower-level control modules. A process cell, unit, operator, or another equipment module can command an equipment module. An equipment module can be part of A unit, or a standalone equipment group can include an equipment module in a process cell. If engineered as a standalone equipment grouping, an equipment module can be an exclusive-use resource or a shared-use resource. The equipment module combines all necessary physical processing and control equipment that is required to perform the manufacturing process. The finite tasks that an equipment module is designed to implement defines the scope of the equipment module. The terms control module and equipment module apply to the physical equipment and to the equipment entity. The following are examples of equipment modules. • A valve matrix used for material transfer between units (shared resource of process cell) • A level control for a tank (equipment module within a specific unit) • A vertical form-fill-seal machine’s ‘sealing jaws control’ (equipment module within a discrete unit)                                                                                                                                                                                                               |
| Control module                         | Control module: A regulating device, state-oriented device, or combination thereof (typically, a collection of sensors, actuators, and other control modules) that is operated as one device. Control that is normally found at this level directly manipulates actuators and other control modules. A control module can direct commands to other control modules, or to actuators that have been configured as part of the control module. Control of the process is affected through the equipment-specific manipulation of control modules and actuators. The control module is the lowest level grouping of equipment in the physical model that can implement basic control. The following are examples of control modules. • An individual sensor or actuator • A state-oriented device that consists of an on/off automatic block valve with position feedback switches and that is operated via the setpoint of the device • A header that contains several on/off automatic block valves that coordinate the valves to direct flow to one or several destinations based on the setpoint directed to the header CM • A servo-controlled electronic gear or cam function (that is, a discrete unit), including its interlock and permissives. The following are typical control modules in a programming library: • Analog output • Analog input with scaling and alarms • Reversing motor • Variable speed drive • Solenoid-operated 2-state valve • Motor-operated 2-state valve • PID with standard modes and deviation alarms |

## Separate a Process Unit into Equipment Modules and Control Modules

To create a modular control program, start with one of these approaches.

- Identify the control modules in the process. Then group the control modules into equipment modules to be supervised and coordinated by procedural controls.
- Determine the units (typically vessels containing one batch at a time). Then determine the equipment modules (such as ingredient addition equipment, agitating equipment, thermal jacket temperature control equipment, and transfer out equipment) by reviewing the related equipment, piping, and instrumentation on a process and instrumentation diagram (P&amp;ID). Then determine the control modules that are related to the equipment states that must be controlled (such as motors, valves, or other process control loops).

One way to organize application logic in the Controller Organizer is to create a separate folder for each unit.

<!-- image -->

## Physical Model Naming Conventions

| Component Name Recommendations                                                                                                                                                                                                                                        | Component Name Recommendations                                                                                                                                                                                                                                        | Component Name Recommendations                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Short, preferably single character abbreviation, all upper case, of the formal name of the site Example:                                                                                                                                                              | Short, preferably single character abbreviation, all upper case, of the formal name of the site Example:                                                                                                                                                              | Short, preferably single character abbreviation, all upper case, of the formal name of the site Example:                                                                                                                                                              |
|                                                                                                                                                                                                                                                                       | Site: My Site Site Name: M                                                                                                                                                                                                                                            | Site: My Site Site Name: M                                                                                                                                                                                                                                            |
| Building number prefixed by a site name, but with no separating underscore Example:                                                                                                                                                                                   | Building number prefixed by a site name, but with no separating underscore Example:                                                                                                                                                                                   | Building number prefixed by a site name, but with no separating underscore Example:                                                                                                                                                                                   |
| Area: Manufacturing Building (102) Area Name: M102                                                                                                                                                                                                                    | Area: Manufacturing Building (102) Area Name: M102                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                       |
| Two- to three-character abbreviation of the formal name of the cell Prefix with an area name and one underscore (optional) Example:                                                                                                                                   | Two- to three-character abbreviation of the formal name of the cell Prefix with an area name and one underscore (optional) Example:                                                                                                                                   | Two- to three-character abbreviation of the formal name of the cell Prefix with an area name and one underscore (optional) Example:                                                                                                                                   |
|                                                                                                                                                                                                                                                                       | Cell: Mixing Cell Name: A102_MIX_123                                                                                                                                                                                                                                  | Cell: Mixing Cell Name: A102_MIX_123                                                                                                                                                                                                                                  |
| In a unit class, prefix the unit name with UN and an underscore Example:                                                                                                                                                                                              | In a unit class, prefix the unit name with UN and an underscore Example:                                                                                                                                                                                              | In a unit class, prefix the unit name with UN and an underscore Example:                                                                                                                                                                                              |
| Unit Class: Mix Tank                                                                                                                                                                                                                                                  | Unit Name: (Machine)                                                                                                                                                                                                                                                  | Unit Name: (Machine)                                                                                                                                                                                                                                                  |
| Unit Class: Packer  Unit Name: UN_Pckr                                                                                                                                                                                                                                | Unit Class: Packer  Unit Name: UN_Pckr                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                       |
| In a unit instance, use the unit identification from the piping and instrumentation diagram (P&ID) All uppercase letters; use underscores instead of dashes Prefix the unit name with the area name, which is separated from the unit name by one underscore Example: | In a unit instance, use the unit identification from the piping and instrumentation diagram (P&ID) All uppercase letters; use underscores instead of dashes Prefix the unit name with the area name, which is separated from the unit name by one underscore Example: | In a unit instance, use the unit identification from the piping and instrumentation diagram (P&ID) All uppercase letters; use underscores instead of dashes Prefix the unit name with the area name, which is separated from the unit name by one underscore Example: |
| Unit Instance: Mix Tank 1234                                                                                                                                                                                                                                          | Unit Instance: Mix Tank 1234                                                                                                                                                                                                                                          | Unit Name: A102_MT1234                                                                                                                                                                                                                                                |
| Machine Instance: Packaging Machine 1234 Unit Name: A102_PKR1234                                                                                                                                                                                                      | Machine Instance: Packaging Machine 1234 Unit Name: A102_PKR1234                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                       |
| In a unit program instance, add the unit identifier between the area name and the unit name Example: Unit Instance Program Name:  A102_UN02_MT1234                                                                                                                    | In a unit program instance, add the unit identifier between the area name and the unit name Example: Unit Instance Program Name:  A102_UN02_MT1234                                                                                                                    | In a unit program instance, add the unit identifier between the area name and the unit name Example: Unit Instance Program Name:  A102_UN02_MT1234                                                                                                                    |
| Machine Instance Program Name:                                                                                                                                                                                                                                        | Machine Instance Program Name:                                                                                                                                                                                                                                        | A102_UN02_PKR1234                                                                                                                                                                                                                                                     |
| In a unit tag instance, prefix the tag with the unit name Example:                                                                                                                                                                                                    | In a unit tag instance, prefix the tag with the unit name Example:                                                                                                                                                                                                    | In a unit tag instance, prefix the tag with the unit name Example:                                                                                                                                                                                                    |
| Unit Instance Tag Name:                                                                                                                                                                                                                                               | Unit Instance Tag Name:                                                                                                                                                                                                                                               | MT1234                                                                                                                                                                                                                                                                |
| Machine Instance Tag Name:                                                                                                                                                                                                                                            | Machine Instance Tag Name:                                                                                                                                                                                                                                            | PKR1234                                                                                                                                                                                                                                                               |
| Area name, underscore, letters EM, underscore, function abbreviation All uppercase letters Example:                                                                                                                                                                   | Area name, underscore, letters EM, underscore, function abbreviation All uppercase letters Example:                                                                                                                                                                   | Area name, underscore, letters EM, underscore, function abbreviation All uppercase letters Example:                                                                                                                                                                   |
| EM Instance: Mix Tank 1234 Vessel Agitator EM Name: MT1234_EM_Agitate                                                                                                                                                                                                 | EM Instance: Mix Tank 1234 Vessel Agitator EM Name: MT1234_EM_Agitate                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                       |
| EM Instance: Packager 1234 Bag Forming EM Name: PKR1234_EM_BagForming                                                                                                                                                                                                 | EM Instance: Packager 1234 Bag Forming EM Name: PKR1234_EM_BagForming                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                       |
| In a control module class, prefix the name with CM and an underscore                                                                                                                                                                                                  | In a control module class, prefix the name with CM and an underscore                                                                                                                                                                                                  | In a control module class, prefix the name with CM and an underscore                                                                                                                                                                                                  |
| Example: CM Class: PID Control Loop                                                                                                                                                                                                                                   | Example: CM Class: PID Control Loop                                                                                                                                                                                                                                   | CM Name: CM_PID                                                                                                                                                                                                                                                       |
| CM Class: Cylinder                                                                                                                                                                                                                                                    | CM Class: Cylinder                                                                                                                                                                                                                                                    | CM Name: CM_Cylndr                                                                                                                                                                                                                                                    |

## Procedural Model

The procedural model describes a multi-tiered, hierarchical model that defines the process capability and automation control in relation to the physical model to perform a task. The procedural model is a representation of how to use the equipment (described in the physical model) to make the product.

The procedural control that is laid out in the procedural model directs the equipment components, via the component interfaces, to perform the specific tasks out of the available capabilities needed to produce a given product.

| Procedural Model Component   | Description                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure                    | The general strategy for production within a process cell. A procedure is composed of unit procedures.                                                                                                                                                                                                                                                                                |
| Unit procedure               | A production sequence. Unit procedures are composed of operations.                                                                                                                                                                                                                                                                                                                    |
| Operation                    | The single sequence necessary for the initiation, organization, and control of phases. Operations are composed of phases.                                                                                                                                                                                                                                                             |
| Phase                        | The lowest level of a procedure that can accomplish an action. The intent of a phase is to cause or define a process-oriented action, while the set of steps in the phase is equipment-specific. • A phase can be subdivided into smaller parts. • A phase can issue one or more commands or cause one or more actions. • The execution of a phase can result in additional commands. |

Combine the procedural model with the physical model to reflect the hierarchy of control and equipment, and the vertical separation between process controls and procedural controls.

<!-- image -->

Not all manufacturing processes require the procedural control to reside in the physical equipment.

In a distributed or flexible process, procedural control can reside outside the equipment, in what is called the control recipe. Examples of this type of manufacturing are large batch systems, material handling systems, or automotive assembly systems. Use of the control recipe lets manufacturers with different automation requirements separate procedural control and process control.

The procedural control is where distributed and flexible control occurs, and where the need arises for a separation from process control.

<!-- image -->

## Procedural Control Modes

## Identify Operations and Phases

One way to organize application logic in the Controller Organizer is to add the procedural model as a separate folder of phases.

<!-- image -->

A control mode determines how equipment entities and procedural elements respond to commands and how they operate. The mode determines how the procedure progresses and who can affect that progression. For example, in a control module that contains basic control functions, such as an automatic block valve, the mode determines what drives the valve position and who can manipulate the position.

The ISA-88 standard defines the following modes.

| Control Mode                | Behavior                                                                                                 | Command                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Automatic (procedural)      | Transitions within a procedure are conducted without interruption as appropriate conditions are met.     | Operators can pause the progression, but can’t force transitions.                                                    |
| Automatic (basic control)   | Equipment entities are manipulated by their control algorithm.                                           | Equipment entities cannot be manipulated directly by the operator.                                                   |
| Semi-Automatic (procedural) | Transitions within a procedure are conducted on manual commands as appropriate conditions are fulfilled. | Operators can pause the progression or redirect the execution to an appropriate point. Transitions cannot be forced. |
| Manual (procedural)         | Procedural elements within a procedure are executed in the order that is specified by an operator.       | Operators can pause the progression or force transitions.                                                            |
| Manual (basic control)      | Equipment entities are not manipulated by their control algorithm.                                       | Equipment entities can be manipulated directly by the operator.                                                      |

## Procedural Control States

The ISA-88 standard defines the following states.

| Control State Description   |                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Idle                        | The procedural element is waiting for a Start command to cause a transition to the Running state.                                                                                                                                                                                                                                  |
|                             | Running The procedural element is operating normally.                                                                                                                                                                                                                                                                              |
| Complete                    | The procedural element has run to completion and is now waiting for a reset command that prompts a transition to Idle.                                                                                                                                                                                                             |
| Pausing                     | The procedural element or equipment entity received a Pause command. This causes the procedural element to stop at the next defined safe or stable stop location in its normal Running logic. Once the procedural element has stopped, the procedural element automatically transitions from Pausing to Paused.                    |
| Paused                      | Once the procedural element is paused at a defined stop location, it transitions from a Pausing to Paused. The Paused state is usually used for short-term pauses. A Resume command starts a transition to the Running state, and the procedural element resumes normal operation immediately following the defined stop location. |
| Holding                     | The procedural element received a Hold command and is executing its Holding logic to put the procedural element or equipment entity into a known state. If no sequencing is required, then the procedural element or equipment entity transitions immediately to the Held state.                                                   |
| Held                        | The procedural element completed its Holding logic and proceeded to the Held state. This state is usually used for a long-term stop. The procedural element or equipment entity waits for a further command to proceed.                                                                                                            |
| Restarting                  | The procedural element receives a Restart command while in the Held state and executes its restart logic to return to the Running state. If no sequencing is required, then the procedural element or equipment entity transitions immediately to the Running state.                                                               |
| Stopping                    | The procedural element received a Stop command and is executing its Stopping logic that facilitates a controlled normal stop. If no sequencing is required, then the procedural element or equipment entity transitions immediately to the Stopped state.                                                                          |
| Stopped                     | The procedural element or equipment entity completed its Stopping logic and waits for a Reset command to transition to an Idle state.                                                                                                                                                                                              |
| Aborting                    | The procedural element received an Abort command and is executing its Abort logic that is the logic that facilitates a quicker, but not necessarily controlled, abnormal stop. If no sequencing is required, then the procedural element transitions immediately to the Aborted state.                                             |
| Aborted                     | The procedural element completed its Aborting logic and waits for a Reset command to transition to the Idle state.                                                                                                                                                                                                                 |

## Procedural Control Commands

The ISA-88 standard defines the following commands.

| Command   | Description                                                                                                                                              | Valid States                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Start     | Orders the procedural element to begin executing the normal Running logic.                                                                               | Idle                                                            |
| Stop      | Orders the procedural element to execute the Stopping logic.                                                                                             | Running Pausing Paused Holding Held Restarting                  |
| Hold      | Orders the procedural element to execute the Holding logic.                                                                                              | Running Pausing Paused Restarting                               |
| Restart   | Orders the procedural element to execute the Restarting logic to safely return to the Running state.                                                     | Held                                                            |
| Abort     | Orders the procedural element to execute the Aborting logic.                                                                                             | Running Pausing Paused Holding Held Restarting Stopping Stopped |
| Reset     | Orders the procedural element to transition to an Idle state.                                                                                            | Complete Aborted Stopped                                        |
| Pause     | Orders the procedural element to pause at the next programmed pause transition within its sequencing logic and await a Resume command before proceeding. | Running                                                         |
| Resume    | Orders a procedural element that is in the Paused state, due to either a Pause command or a Single Step mode, to resume normal operation.                | Paused                                                          |

## Procedural Model Naming Conventions

| Component Name   | Recommendations                                                                                                                                                           |                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure        | Use all upper case letters Prefix with type of procedure (such as RP for recipe procedure), underscore, abbreviation of procedure Example:                                | Use all upper case letters Prefix with type of procedure (such as RP for recipe procedure), underscore, abbreviation of procedure Example:                                |
|                  | Mixing, Tank: Clean                                                                                                                                                       | Procedure Name: M102_MIX_RP_CLEAN                                                                                                                                         |
| Unit procedure   | Use all upper case letters Prefix with UP, underscore, abbreviation of unit procedure Example:                                                                            | For a unit procedure executed in a Logix controller, prefix with area name, underscore, unit name, underscore                                                             |
|                  |                                                                                                                                                                           | Unit Procedure Class: Clean Unit Procedure Name: UP_CLEAN                                                                                                                 |
| Operation        | Use all upper case letters Prefix with OP, underscore, abbreviation of operation Example:                                                                                 | Use all upper case letters Prefix with OP, underscore, abbreviation of operation Example:                                                                                 |
|                  | Unit Procedure Class: Mix Tank Clean                                                                                                                                      | M102_TK2333_UP_CLEAN                                                                                                                                                      |
|                  | For an operation executed in a Logix controller, prefix with area name, underscore, unit name, underscore Example: Operation Class: Steam-In-Place Operation Name: OP_SIP | For an operation executed in a Logix controller, prefix with area name, underscore, unit name, underscore Example: Operation Class: Steam-In-Place Operation Name: OP_SIP |
|                  | Mix Tank: Steam-In-Place Operation Operation Name: M102_TK2333_OP_SIP                                                                                                     |                                                                                                                                                                           |

## State Model

A state model helps program the equipment in a structured way, which results in the same behavior in all equipment throughout the plant

.

<!-- image -->

| Command            |                  |                         |                     |      |         | Start Stop Hold Restart Abort Reset Pause Resume   |
|--------------------|------------------|-------------------------|---------------------|------|---------|----------------------------------------------------|
| Initial State      | No Command State | State Transition Matrix |                     |      |         |                                                    |
| Idle               |                  | Running Stopping        | Aborting            |      |         |                                                    |
|                    | Running Complete | Stopping Holding        | Aborting            |      | Pausing |                                                    |
| Complete           |                  |                         |                     | Idle |         |                                                    |
|                    | Pausing Paused   | Stopping Holding        | Aborting            |      |         |                                                    |
| Paused             |                  | Stopping Holding        | Aborting            |      |         | Running                                            |
| Holding Held       |                  | Stopping                | Restarting Aborting |      |         |                                                    |
| Held               |                  | Stopping Holding        | Aborting            |      |         |                                                    |
| Restarting Running |                  | Stopping Holding        | Aborting            |      |         |                                                    |
|                    | Stopping Stopped |                         | Aborting            |      |         |                                                    |
| Stopped            |                  |                         | Aborting Idle       |      |         |                                                    |
| Aborting Aborted   |                  |                         |                     |      |         |                                                    |
| Aborted            |                  |                         |                     | Idle |         |                                                    |
| Resetting Idle     |                  | Stopping                | Aborting            |      |         |                                                    |

## Guidelines for Produced and Consumed Tags

| Guideline                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You cannot bridge produced and consumed tags over different networks.                                  | For two controllers to share produced or consumed tags, both controllers must be attached to the same network. You can produce and consume tags over ControlNet or EtherNet/IP networks.                                                                                                                                                                                                                          |
| Create the tag at controller scope.                                                                    | You can only produce and consume (share) controller-scoped tags.                                                                                                                                                                                                                                                                                                                                                  |
| Limit the size of the tag to ≤ 500 bytes.                                                              | If you produce or consume a tag over a network, the tag must be ≤ 480 bytes. Network transfers require 20 bytes of data overhead.                                                                                                                                                                                                                                                                                 |
| Combine data that goes to the same controller.                                                         | If you are producing several tags for the same controller: • Group the data into one or more user-defined structures. This uses fewer connections than producing each tag separately. • Group the data according to similar update intervals. To conserve network bandwidth, use a greater RPI for less critical data.                                                                                            |
| The following atomic data types can be directly produced or consumed: DINT UDINT LINT ULINT REAL LREAL | The listed atomic data types can be produced or consumed individually or in arrays. Other atomic data types (BOOL,SINT,USINT,INT,UINT) cannot be done individually or in arrays and are required to be part of a data structure to be produced or consumed.                                                                                                                                                       |
| Data structures can be produced or consumed                                                            | Data structures include user-defined data types (UDT), strings, add-on-defined, predefined, and module-defined data structures. Data structures meeting the size requirements can be produced or consumed.                                                                                                                                                                                                        |
| AXIS_CIP_DRIVE                                                                                         | Use AXIS_CIP_DRIVE to produce and consume axis data.                                                                                                                                                                                                                                                                                                                                                              |
| The data type in the producer and the consumer must match.                                             | The data type for a produced or consumed tag must be the same in both the producer and the consumer.                                                                                                                                                                                                                                                                                                              |
| Produce tags that are based on user-defined structures to non-Logix devices.                           | The controller produces tags in 32-bit words. For devices that communicate in other word boundaries, such as 16-bit words, the resulting data in the target device can be misaligned. To help avoid misalignment, structure the produced data in a user-defined structure.                                                                                                                                        |
| Use a programmatic handshake to help ensure that data is exchanged.                                    | Produced tags continually transmit based on the RPI, so it can be difficult to know when new data arrives. You can set a bit or increment a counter that is embedded in the produced tag to identify to the consumer that new data is present. You can also provide a return handshake via a reverse produced/consumed tag, so that the original producer knows that the consumer received and processed the tag. |
| Use a CPS instruction to buffer produced and consumed data.                                            | Use the CPS instruction to copy the data to the outgoing tag on the producer side. Then use another CPS instruction to copy the data into a buffer tag on the consumer side. The CPS instructions provide data integrity for data structures greater than 32 bits. Important: The controller inhibits all interrupts while it executes a CPS instruction.                                                         |

## Produced and Consumed Data

The controllers support the ability to produce (broadcast) and consume (receive) systemshared tags.

For two controllers to share produced or consumed tags, both controllers must be in the same backplane or attached to the same control network. You cannot bridge produced and consumed tags over two networks.

## IMPORTANTIMPORTANT

The actual number of produced and consumed tags that you can configure over ControlNet® or EtherNet/IP™ in a project depends on the connection limits of the communication module through which you produce or consume the tags.

For more information on produced and consumed tags, see the Logix 5000 Controllers Produced and Consumed Tags Programming Manual, publication 1756-PM011 .

<!-- image -->

|                                                                            | Guideline Description                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use unicast EtherNet/IP communication to reduce broadcast network traffic. | To reduce bandwidth use and preserve network integrity, some facilities block multicast Ethernet packets. You can configure a produced and consumed tag to use multicast or unicast connections. Unicast connections help with the following: • Reduce network bandwidth • Simplify Ethernet switch configuration |
| Monitoring produced and consumed data.                                     | Group produced and consumed tags as members in user-defined structures whose first member is a CONNECTION_STATUS type. This technique helps monitor connection status between controllers without increasing execution time, such as using a GSV instruction to detect status.                                    |
| Firmware revisions                                                         | When adding the Producer controller to the I/O configuration list of the Consumer controller, the firmware revision does not have to match. However, the rack size and slot number must be correct.                                                                                                               |

## Guidelines for Produced and Consumed Axis

| Guideline                                                                                                       | Description                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| You can configure a produced and consumed axis between controllers in a chassis or over an EtherNet/IP network. | Controllers that support motion support the AXIS_CIP_DRIVE data type for produced and consumed tags.                                        |
| Use a produced and consumed axis to synchronize motion functions across multiple controllers.                   | Synchronize functions such as: • PCAM • GEAR • MDSC moves • Scheduled outputs • Registration events • Position-based interlocks (handshake) |

## Guidelines to Specify an RPI Rate for Produced and Consumed Tags

When configuring produced and consumed tags, you specify a requested packet interval (RPI) rate. The RPI value is the rate at which the controller attempts to communicate with the module.

| Guideline                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Make sure that the RPI is equal to or greater than the NUT. | You use RSNetWorx™ for ControlNet software to select the network update time (NUT) and the software schedules the network connections. RSNetWorx software cannot schedule a ControlNet network if a module and/or produced/consumed tag on the network has an RPI that is faster than the network update time.                                                                                                                                                                                                                                                                              |
| RPI of multicast tags                                       | • For Studio 5000 Logix Designer® application version 24 and earlier: The smallest (fastest) consumer RPI determines the RPI for the produced tag. If multiple consumers request the same tag, the smallest (fastest) request determines the rate at which the tag is produced for all consumers. • For Studio 5000 Logix Designer application version 28 and later: the first consumer of a produce tag determines the RPI at which data is produced. All subsequent consumers must request the same RPI value as the first consumer. Otherwise, the subsequent consumers fail to connect. |

## Guidelines to Manage Connections for Produced and Consumed Tags

| Guideline                                          | Description                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimize the use of produced and consumed tags.    | To reduce network traffic, minimize the size of produced and consumed tags. Also, minimize the use of produced and consumed tags to high-speed, deterministic data, such as interlocks.                                                                                                           |
| Use arrays or user-defined structures.             | When sending multiple tags to the same controller, use an array or user-defined structure to consolidate the data. The byte limit of ≤ 500 bytes per produced and consumed tag still applies.                                                                                                     |
| Configure the number of consumers accurately.      | Make sure the number of consumers that are configured for a produced tag is the actual number of controllers that consumes the tag. If you set the number higher than the actual number of controllers, you unnecessarily use up connections. The default is two consumers per produced tag.      |
| Multiple produced/consumed connections are linked. | If there are multiple produced and consumed connections between two controllers and one connection fails, all produced and consumed connections fail. Consider combining all produced and consumed data into one structure or array so that you only need one connection between the controllers. |

## Configure an Event Task Based on a Consumed Tag

## Compare Messages and Produced/Consumed Tags

| Method                | Benefits                                                                                                                                                                                                                                                                                                                                                                                                                        | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read/Write Message    | • Programmatically initiated • Communication and network resources that are only used when needed • Support automatic fragmentation and reassembly of large data packets, up to as many as 32,767 elements • Some connections can be cached to improve retransmission time • Generic CIP™ message useful for third-party devices                                                                                                | • Delay can occur if resources are not available when needed • MSG instruction and processing can impact controller scan (system overhead timeslice) • Data arrives asynchronously to program scan (use a programmatic handshake or a UID/UIE instruction pair to reduce impact, no event task support) • Can add additional messages online in Run mode. • Utilizes class 3 connections which have lower priority than Produce/consume • Is intended for status information                                                                                                                                                                                                |
| Produced/Consumed Tag | • Configured once and sent automatically based on requested packet interval (RPI) • Multiple consumers can simultaneously receive the same data from a produced tag • Can trigger an event task when consumed data arrives • ControlNet resources are reserved up front • Does not affect the scan of the controller • Utilizes class 1 connections which have higher priority than Messages • Is intended for critical control | • Support limited to Logix 5000® and PLC-5® controllers, and the 1784-KTCS I/O Linx and select third-party devices • Limited to 500 bytes over the backplane and 480 bytes over a network • Must be scheduled when using ControlNet • Data arrives asynchronously to program scan (use a programmatic handshake or CPS instruction and event tasks to synchronize) • Connection status must be obtained separately • You can configure status information for a produced/consumed tag • On an EtherNet/IP network, you can configure produced/ consumed tags to use multicast or unicast connections. • Cannot create additional produced/consumed tags online in Run mode. |

An event task executes automatically based on a preconfigured event occurring. One such event can be the arrival of a consumed tag.

- Only one consumed tag can trigger a specific event task.
- Use an IOT instruction in the producing controller to signal the production of new data.
- When a consumed tag triggers an event task, the event task waits for all data to arrive before the event task executes.

## Notes:

## Guidelines for Data Types

## Data Structures

The controllers support the following data types:

- Numerous IEC 61131-3 elementary data types
- Compound data types
- Arrays
- Predefined structures, such as counters and timers
- User-defined structures

Follow these guidelines depending on the data type for your application.

| Guideline                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use 32-bit data types (for example, DINT) whenever possible | All controllers perform 32-bit (for example, DINT, REAL) math operations efficiently. 5590 controllers also do 64-bit (for example, LINT, LREAL) operations efficiently. For math operations in either of these two cases, use the right data type for the range of values and precision needed. To minimize type conversion costs, make sure the data types of all operands that are used in an operation are the same. Use unsigned integers for array indexes to reduce cost of bounds checking. |
| Co-locate BOOL values                                       | Though BOOL tags can be fast, they use extra memory. Grouping BOOL values into arrays makes better use of memory. In the case of a user-defined structure, locate BOOL members next to each other for the same effect.                                                                                                                                                                                                                                                                              |

| Memory                                                       | BOOL/SINT/ USINT       | INT/UINT                 | DINT/UDINT/ REAL/TIME32   | LREAL/LINT/ULINT/TIME/ LTIME/DT/LDT   |
|--------------------------------------------------------------|------------------------|--------------------------|---------------------------|---------------------------------------|
| Memory that is reserved for a standalone tag                 |                        |                          |                           | 4 bytes 4 bytes 4 bytes 8 bytes       |
| Memory that is reserved for data in a user-defined structure | 1 byte (8-bit aligned) | 2 bytes (16-bit aligned) | 4 bytes (32-bit aligned)  | 8 bytes (64-bit aligned)              |

A tag uses additional memory in the controller to store the tag name and symbol, and allocate memory for data.

When mixing data types among operand arguments, the system may need to perform type conversion before and after instruction execution. This requires additional memory and execution time when compared to using 32-bit operands all with the same data types for the same operation.

<!-- image -->

## Arrays

## BOOL[96] = 12 bytes

| BOOL arrays use 32-bit increments of memory          | 3               |       | ² ²   | 26   | 2   | 24 23   | 22   |    | 21     |    |       | 16 15    | 3      |         | 10 6口   |    | 6   |       | 3    |     |
|------------------------------------------------------|-----------------|-------|-------|------|-----|---------|------|----|--------|----|-------|----------|--------|---------|----------|----|-----|-------|------|-----|
| 63                                                   | 62              | 61 60 |       | 0o   |     |         | 5寸  |    |        |    | 4 寸8 | 寸～ 寸6 | 寸5    | 寸寸 43 | 41 寸口  |    | r-  | 36 36 | 34   |     |
| BOOL arrays use 32-bit increments of memory          |                 |       | 91    |      |     | 0o0o    |      | 06 | 00 8寸 | 00 |       |          | r-- oo |         | 42 寸 r- | r- |     |       | r 66 | 6寸 |
| BOOL arrays use 32-bit increments of memory          | 94              |       |       | 口6  |     |         | --o  |    |        | 00 |       |          | [-     |         |          |    | r=  | 00    |      |     |
| SINT[10] = 12 bytes of memory (2 bytes unused)       |                 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| SINT arrays are padded to use any left over bytes    | ² 1             |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| SINT arrays are padded to use any left over bytes    | Unused Unused 6 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| SINT arrays are padded to use any left over bytes    |                 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| INT arrays are padded to use any left over bytes     | 1 口            |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| INT arrays are padded to use any left over bytes     | 3               |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| INT arrays are padded to use any left over bytes     | Unused 4        |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| DINT[3] = 12 bytes and REAL[3] = 12 bytes            |                 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| DINT and REAL arrays use 4-byte increments of memory |                 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| DINT and REAL arrays use 4-byte increments of memory | 1 2             |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |
| DINT and REAL arrays use 4-byte increments of memory |                 |       |       |      |     |         |      |    |        |    |       |          |        |         |          |    |     |       |      |     |

An array allocates a contiguous block of memory to store a specific data type as a table of values.

- Tags support arrays in one, two, or three dimensions.
- User-defined structures can contain a single-dimension array as a member of the structure.

<!-- image -->

|                 | This array Stores Data like   | For Example                                                                                         | For Example                                   | For Example   | For Example   | For Example   |
|-----------------|-------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------|---------------|---------------|---------------|
| One dimension   |                               | Tag name one_d_array Total number of elements = 7                                                   | Type DINT[7]                                  | Dimension 0 7 | Dimension 1 — | Dimension 2 — |
| Two dimension   |                               | Tag name two_d_array                                                                                | Type DINT[4,5]                                | Dimension 0 4 | Dimension 1 5 | Dimension 2 — |
| Three dimension |                               | Tag name three_d_array Total number of elements = 2 ∗ 3 ∗ 4 = 24 Valid subscript range DINT[a , b , | Type DINT[2,3,4] c] where a=0…1; b=0…2, c=0…3 | Dimension 0 2 | Dimension 1 3 | Dimension 2 4 |

The data type you select for an array determines how the contiguous block of memory gets used.

## Guidelines for Arrays

| Guideline                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You can create arrays of most data types, except for ALARM_xxx, AXIS_xxx, COORDINATE_SYSTEM, ENERGY_xxx, HMIBC, MESSAGE, and MOTION_GROUP data types. | A subscript identifies an individual element within the array. A subscript starts at 0 and extends to the number of elements minus 1 (zero based). • Single-dimension arrays take less memory and execute faster than two-dimension or three-dimension arrays. • Direct references to array elements execute faster than indexed references. • An array can be as large as 2 MB. • If you create an array of structures, the memory for each element is allocated based on the structure definition. | A subscript identifies an individual element within the array. A subscript starts at 0 and extends to the number of elements minus 1 (zero based). • Single-dimension arrays take less memory and execute faster than two-dimension or three-dimension arrays. • Direct references to array elements execute faster than indexed references. • An array can be as large as 2 MB. • If you create an array of structures, the memory for each element is allocated based on the structure definition. |
| Type of Array                                                                                                                                         | Benefit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Single (1) dimension                                                                                                                                  | • Better support by native file instructions • Fully supported in user-defined structures and arrays • Smallest impact (execution time and memory) for indexed references • Can create arrays when programming online                                                                                                                                                                                                                                                                                | • Multiple arrays cannot be indirectly referenced like in PLC or SLC™ processors (such as, N[N7:0]:5) • BOOL arrays are not directly supported by file instructions • Can be changed only when programming offline                                                                                                                                                                                                                                                                                   |
| Double (2) dimension and Triple (3) dimension Nest arrays.                                                                                            | • Can provide a more accurate data representation for a physical system • Can emulate PLC file/word indirection with a two dimension array • Can create arrays when programming online instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | • Larger impact (execution time and memory) for indexed references • File manipulation requires extra code and file • Can only be changed when programming offline                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                       | The file instructions offer limited support for arrays. To work with array data, create a user-defined structure with one array as a member of the structure. Then create an array tag by using the user-defined structure as its data type.                                                                                                                                                                                                                                                         | The file instructions offer limited support for arrays. To work with array data, create a user-defined structure with one array as a member of the structure. Then create an array tag by using the user-defined structure as its data type.                                                                                                                                                                                                                                                         |
| Select the data type of the array based on the data and the instructions that manipulate that data.                                                   | While SINT and INT arrays can compact more values into a given memory area, they require additional memory and execution time for each instruction that references the array.                                                                                                                                                                                                                                                                                                                        | While SINT and INT arrays can compact more values into a given memory area, they require additional memory and execution time for each instruction that references the array.                                                                                                                                                                                                                                                                                                                        |
| Limit arrays to 2 MB of data.                                                                                                                         | The maximum array size is 2 MB. The software displays a warning if you try to create an array that is too large. The software also displays a warning if an array is 1.5…2 MB, even though these sizes are valid.                                                                                                                                                                                                                                                                                    | The maximum array size is 2 MB. The software displays a warning if you try to create an array that is too large. The software also displays a warning if an array is 1.5…2 MB, even though these sizes are valid.                                                                                                                                                                                                                                                                                    |
| Edit arrays online and offline.                                                                                                                       | You can create arrays when online or offline. However, you can modify only the size or data type of an existing array when offline.                                                                                                                                                                                                                                                                                                                                                                  | You can create arrays when online or offline. However, you can modify only the size or data type of an existing array when offline.                                                                                                                                                                                                                                                                                                                                                                  |

## Indirect Addresses of Arrays

If you want an instruction to access different elements in an array, use a tag in the subscript of the array (an indirect address). By changing the value of the tag, you change the element of the array that your logic references.

When index equals 1, array[index] points here.

<!-- image -->

When index equals 2, array[index] points here.

When you directly reference an element in an array (such as MyArray[20]), uses less memory and executes faster than an indirect reference (MyArray[MyIndex]). You can also indirectly address bits in a tag (MyDint.[Index]).

If you use indirect addresses, use DINT tags because other data types require conversion and execute slower. For each indexed access to data, the controller recalculates the array index. If you access a specific array element multiple times, copy the data out of the array into a fixed tag and use that tag in subsequent logic.

You can also use an expression to specify the index value. For example: MyArray[10 + MyIndex].

- An expression uses operators to calculate a value.
- The controller computes the result of the expression and uses it as the index.
- These are valid operators.

|     | Operator Description          | Optimal            |
|-----|-------------------------------|--------------------|
|     |                               | + Add DINT ,  REAL |
| -   | Subtract/negate DINT, REAL    |                    |
|     | * Multiply DINT               | ,  REAL            |
| /   | Divide                        | DINT, REAL         |
| **  | Exponent (x to y) DINT, REAL  |                    |
| ABS | Absolute value                | DINT, REAL         |
| ACS | Arc cosine                    | REAL               |
| AND | Bitwise AND                   | DINT               |
| ASN | Arc sine                      | REAL               |
| ATN | Arc tangent                   | REAL               |
| COS | Cosine                        | REAL               |
| DEG | Radians to degrees DINT, REAL |                    |
| FRD | BCD to integer                | DINT               |
| LN  | Natural log                   | REAL               |
| LOG | Log base 10                   | REAL               |
| MOD | Modulo divide                 | DINT, REAL         |

|     | Operator Description          | Optimal    |
|-----|-------------------------------|------------|
| NOT | Bitwise complement DINT       |            |
| OR  | Bitwise OR                    | DINT       |
| RAD | Degrees to radians DINT, REAL |            |
| SIN | Sine                          | REAL       |
| SQR | Square root                   | DINT, REAL |
| TAN | Tangent                       | REAL       |
| TOD | Integer to BCD                | DINT       |
| TRN | Truncate                      | DINT, REAL |
| XOR | Bitwise exclusive OR DINT     |            |

## Guidelines for Array Indexes

| Guideline                                                                 | Description                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use the SIZE instruction to determine the number of elements in an array. | By determining the number of elements in an array at runtime, you can write reusable code that adjusts itself to meet each instance where it is used. SIZE SizeinElements Source ? ？? Dim.ToVary ? Size ？ ??                                                                           |
|                                                                           | Use immediate values to reference array elements. Immediate value references to array elements are quicker to process and execute faster than indexed references.                                                                                                                        |
| Use UDINT tags for array indexes.                                         | UDINT is fastest data type to use for indexing because of its optimal bounds checking implementation. Of the remaining numeric data types, DINT is the fastest due to less data type conversion overhead.                                                                                |
| Avoid using array elements as indexes.                                    | The controller does not directly support the use of an array element as the index to look up a value in another array. To work around this, you can create an alias to the element and then use this as the index. Or copy the element to a base tag and use that base tag as the index. |

## Guidelines for User-defined Data Types (UDT)

| Guideline                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Group members of the same data type within a structure.                                 | You can create members of most data types, except for AXIS, COORDINATE_SYSTEM, MOTION_GROUP, and MESSAGE data types. Place members that use the same data type in sequence. The controller aligns every data type along an 8-bit boundary for SINTs, a 16-bit boundary for INTS, or a 32-bit boundary for DINTs and REALs. BOOLs also align on 8-bit boundaries, but if they are placed next to each other in 16bytes 12 bytes DATATYPESample1 DATATYPESample1 BOOL Bit1: BOOL Bit1: SINT Tiny_Value BOOLBit2: BOOLBit2: SINTTiny_Value INTSmall_Value INTSmall_Value DINT Big_Value DINT Big_Value REALFloat_Value REALFloat_Value END_TYPE END_TYPE |
| Arrays within a UDT can only be 1-dimension.                                            | If you include an array as a member, limit the array to one dimension. Multidimension arrays are not permitted in a user-defined structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| I/O data that is used in a UDT must be copied into the members.                         | If you include members that represent I/O devices, you must use logic to copy the data into the members of the structure from the corresponding I/O tags. Make sure that the data type of the structure member matches the I/O data type to avoid data type conversion.                                                                                                                                                                                                                                                                                                                                                                               |
| Limit user-defined data types to 500 members.                                           | The controllers limit user-defined structures to 500 members. If you need more, consider nesting structures within the main structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Limit user-defined data types to 2 MB of data.                                          | The maximum UDT size is 2 MB. The software displays a warning if you try to create an UDT that is too large. The software also displays a warning if the UDT is 1.5…2 MB, even though these sizes are valid.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Limit the size of user-defined structures if they are to be produced and consumed tags. | Produced and consumed tags are limited to 500 bytes over the backplane and 480 bytes if over a network. Linx-based software can optimize user-defined structures that are less than 480 bytes. UDT larger than the noted produced and consumed tag limits must use a MESSAGE instruction (MSG) if they are to be communicated.                                                                                                                                                                                                                                                                                                                        |

<!-- image -->

|                                                                      | Guideline Description                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use the appropriate instruction to load data into a structure.       | Load input values into the user-defined structure at the beginning of the program and copy output values from the user-defined structure at the end of the program. • Single bit - Examine On (XIC) and Output Energize (OTE) instructions • Contiguous bits - Bit Field Distribute (BTD) instruction • Single value - MOV instruction • Multiple contiguous values -COP/CPS instruction |
| Use structure descriptions to automatically create tag descriptions. | Enable the Use Pass-through Description workstation option (Tools > Options > Display) to display the descriptions you add to the members of structures for each tag that uses that structure data type.                                                                                                                                                                                 |
| Online and offline editing.                                          | You can create user-defined structures when online or offline. However, you can modify only an existing structure when offline.                                                                                                                                                                                                                                                          |

## Select a Data Type for Bit Tags

Bits in a controller can exist as: BOOL tags, bits in a BOOL array, bits in elements of a SINT, USINT, INT, UINT, DINT, UDINT, LINT, ULINT array, members of a user-defined structure, or as bits in a SINT, USINT, INT, UINT, DINT, UDINT, LINT, ULINT member of a user-defined structure.

| Tag Type                                                       | Description                                                                                                                                                                                 |                                                                                                                                |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| BOOL tag                                                       | Each tag accesses a specific bit. Each tag uses 4 bytes.                                                                                                                                    | Each tag accesses a specific bit. Each tag uses 4 bytes.                                                                       |
| MyBit:BOOL                                                     | Benefits                                                                                                                                                                                    | Considerations                                                                                                                 |
| MyBit T                                                        | • Each bit has a specific tag                                                                                                                                                               | • Requires extra bandwidth to communication • Uses more memory • Cannot use FBC/DDT bit file instructions                      |
| BOOL array                                                     | A BOOL array combines multiple bits into adjacent words (32-bit words).                                                                                                                     | A BOOL array combines multiple bits into adjacent words (32-bit words).                                                        |
| BOOL array                                                     | Benefits                                                                                                                                                                                    | Considerations                                                                                                                 |
| BitTable:BOOL[32] BitTable[10] 3E                              | • Consolidates multiple bits into one word • Better use of memory • Can address all bits in an array by using indirect addressing                                                           | • BOOL data type only supported by bit instructions • Cannot use file instructions, copy instructions, or DDT/FBC instructions |
| DINT array                                                     | A DINT combines multiple bits into adjacent words.                                                                                                                                          | A DINT combines multiple bits into adjacent words.                                                                             |
|                                                                | Benefits                                                                                                                                                                                    | Considerations                                                                                                                 |
| FaultTable:DINT[3] FaultTable[0].18 3E                         | • Consolidates multiple bits into one word • File instructions, copy instructions, and DDT/FBC instructions support DINT arrays • Lets you access the bits by element (word) and bit number | • Requires extra planning to indirectly address bits • Difficult to address bits in the array by using indirect addressing     |
| User-defined structure                                         | A user-defined structure combines multiple bits into adjacent, individually named words.                                                                                                    | A user-defined structure combines multiple bits into adjacent, individually named words.                                       |
| User-defined structure                                         | Benefits                                                                                                                                                                                    | Considerations                                                                                                                 |
| BitStructure Bit1:BOOL Bit2:BOOL Fault:BitStructure Fault.Bit1 | • Object based • Consolidates multiple bits into one word                                                                                                                                   | • Third-party MMI/EOI products do not directly support structures. • Cannot use FBC/DDT bit file instructions                  |

## Serial Bit Addresses

The Logix 5000 controller supports both of the following addressing modes, but you cannot use both to reference bits in the same array due to conformance with the IEC 61131-3 standard. Choose the method that best meets your application needs. You can copy data between arrays by using both methods.

| Address Mode Description   |                                                                                                                                                                                                                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serial bit                 | Serial bit addressing references all bits as a contiguous list (array) of bits. For example, if you want to reference the third bit in the second word of a B file, specify B3/18. This method is similar to a BOOL array in a Logix 5000 controller where you specify FaultBit[18]. |
| Word bit                   | Word bit addressing identifies a bit within a specific word. For example, B3:1/2 is the same as B3/18 from the serial bit example. This method is similar to accessing the bits of a SINT, INT, DINT array in a Logix 5000 controller where you specify FaultTable[1].2.             |

You can also use an expression to indirectly reference a bit in a DINT array by using a serialized bit number, as shown in the following example.

Tag

MyBits : DINT[10]

BitRef : DINT

EndTag

MOV(34, BitRef)

XIC(MyBits[BitRef / 32].[BitRef AND 31])

where:

| This expression                                                               | Calculates the                                                                |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [BitRef / 32]                                                                 | Element in the DINT array                                                     |
| If the tag MyBits is an INT or SINT, the divisor is 16 or 8, respectively.    | If the tag MyBits is an INT or SINT, the divisor is 16 or 8, respectively.    |
| [BitRef AND 31]                                                               | Bit within the element                                                        |
| If the tag MyBits is an INT or SINT, the mask value is 15 or 7, respectively. | If the tag MyBits is an INT or SINT, the mask value is 15 or 7, respectively. |

The Diagnostic Detect (DDT) and File Bit Compare (FBC) instructions provide a bit number as a result of their operation. These instructions are limited to DINT arrays so you can use them to locate the bit number that is returned from the example above.

## Guidelines for String Data Types

String data types are structures that hold ASCII characters. The first member of the structure defines the length of the string; the second member is an array that holds the actual ASCII characters.

<!-- image -->

| Guideline                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You can create a string data type that is longer or shorter than the default string data type. | The default string data type can contain as many as 82 characters. You can create custom-length string data types that range from 1 to 65535 characters.                                                                                                                                                                                                                                      |
| Only some instructions support string data types.                                              | These comparison instructions support string tags: EQU, NEQ, GRT, GEG, LES, LEQ, CMP. These string-handling instructions support string tags: STOD, DTOS, STOR, RTOS, CONCAT, MID, FIND, DELETE, INSERT, UPPER, LOWER, SIZE. These file instructions support string arrays: FAL, FFL, FFU, LFL, LFU, COP, CPS, FSC.                                                                           |
| Use the SIZE instruction to determine the number of characters in a string.                    | By determining the number of characters in a string at runtime, you can write reusable code that adjusts itself to meet each instance where it is used.                                                                                                                                                                                                                                       |
| Set the LEN field to indicate the number characters that are present.                          | The LEN field in the string structure indicates how many characters are in the string. The programming software and the controller instructions that manipulate strings use the LEN value to determine how many positions in the string DATA array contain valid characters. Both the programming software and the instructions stop processing the DATA array once they reach the LEN value. |

## Configure Tags

A tag is a text-based name for an area of controller memory where data is stored. Tags are the basic mechanism to allocate memory, reference data from logic, and monitor data.

| If you want the tag to                            | Then choose this type   |
|---------------------------------------------------|-------------------------|
| Store a value for use by logic within the project | Base                    |
| Use another name for an existing tag’s data (can help simplify long, pre-determined tag names, such as for I/O data or user defined structures)                                                   | Alias                   |
| Send (broadcast) data to another controller       | Produced                |
| Receive data from another controller              | Consumed                |

<!-- image -->

For more information on I/O tags, see Communicate with I/O on page 95 .

## Guidelines for Base Tags

Use the following guidelines for base tags.

| Guideline                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create standalone atomic tags.                            | The controller supports pre-defined, standalone tags. • Atomic tags are listed directly in the Tag Editor and Data Monitor and can easily be found by browsing the alphabetical list. • Atomic tags can be created online, but the data type can only be modified offline. Using only atomic tags can impact HMI communication performance as more information must be passed and acted on.                                                                                                                                                                      |
| Create user-defined structures                            | User-defined structures (data types) let you organize your data to match your machine or process. • One tag contains all data that is related to a specific aspect of your system. This keeps related data together and easy to locate, regardless of its data type. • Each piece of data (member) gets a descriptive name. • You can use the structure to create multiple tags with the same data layout. • User-defined structure can only be modified offline. Linx-based software optimizes user-defined structures more than standalone tags.               |
| Use arrays like files to create a group of similar tags.  | An array creates multiple instances of a data type under a common tag name. • Arrays let you organize a block of tags that use the same data type and perform a similar function. • You organize the data in one, two, or three dimensions to match what the data represents. • Arrays can only be modified offline. • Linx-based software optimizes array data types more than standalone tags. Minimize the use of BOOL arrays. Many array instructions do not operate on BOOL arrays, making it more difficult to initialize and clear an array of BOOL data. |
| Take advantage of program-scoped tags.                    | If you want multiple tags with the same name, define each tag at the program scope (program tags) for a different program. This lets you reuse both logic and tag names in multiple programs. Avoid using the same name for both a controller tag and a program tag. Within a program, you cannot reference a controller tag if a tag of the same name exists as a program tag for that program.                                                                                                                                                                 |
| Use mixed case and the underscore characters.             | Although tags are not case-sensitive (upper case A is the same as lower case a), mixed case is easier to read. For example, Tank_1 can be easier to read than tank1.                                                                                                                                                                                                                                                                                                                                                                                             |
| Consider alphabetical order.                              | The programming software displays tags of the same scope in alphabetical order. To make it easier to monitor related tags, use similar starting characters for tags that you want to keep together. For example, consider using Tank_North and Tank_South rather than North_Tank and South_Tank.                                                                                                                                                                                                                                                                 |
| Use leading zeroes (0) when numbers are part of tag names | The programming software uses a simple sort to alphabetize tag names in the Tag Editor and Data Monitor. This means if you have Tag1, Tag2, Tag11, and Tag12, the software displays them in order as Tag1, Tag11, Tag12, and then Tag2. If you want to keep them in numerical order, name them Tag01, Tag02, Tag11, and Tag12.                                                                                                                                                                                                                                   |

## Create Alias Tags

An alias tag lets you create one tag that represents another tag.

- Both tags share the same value as defined by the base tag.
- When the value of a base tag changes, all references (aliases) to the base tag reflect the change.

| Guideline                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upload behavior for alias tags.                | For 5370 and 5570 controllers, there are situations when uploading a project file that instruction operands that use alias references can change. To avoid these situations with ladder instruction operands, do not use: • Nested aliases (also known as an alias chain) • Multiple aliases to the same tag On an upload, the software uses a technique referred to as “best fit” to reconstruct instruction operands and operands that use an alias can change. This does not apply to 5380, 5480, 5580, or 5590 controllers, and on an upload, the aliases for these controllers are consistently reproduced. |
| Alias tags do not affect controller execution. | During download, the program is compiled into machine executable code and physical memory addresses. While the existence of an alias requires controller memory to store the name, the program performs the same operation for a reference with an alias or its associated base tag.                                                                                                                                                                                                                                                                                                                             |
| Access alias tags from Linx-based software.    | Because an alias tag appears as a standalone tag to Linx-based software, an alias tag that references a compound array or structure can require additional communication time. When you reference tags from Linx-based software or other HMI, it can be fastest to reference base tags directly.                                                                                                                                                                                                                                                                                                                 |

## Guidelines for Data Scope

<!-- image -->

## Guidelines for Tag Names

Data scope defines where you can access tags. Controller-scoped tags and parameters are accessible by all programs. Local tags are accessible only by the code within a specific program. Equipment Phases, like Programs, have parameters and local tags.

| If you want to                                                                                    | Then assign this scope                        |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Produce or consume data                                                                           | Controller scope (controller tags)            |
| Use a tag in multiple programs in the same project                                                | Controller scope (controller tags) Parameters |
| Use a tag in a message (MSG) instruction                                                          | Controller scope (controller tags) Parameters |
| Use motion tags                                                                                   | Controller scope (controller tags) Parameters |
| Reuse the same tag name multiple times for different parts or processes within a controller       | Parameters                                    |
| Have multiple programmers work on lo  Local Tags gic and you want to merge logic into one project | Parameters                                    |

Isolate portions of a machine or different stations into separate programs or equipment phases and use program-scoped or phase-scoped tags. This lets you do the following:

- Provide isolation between programs and equipment phases
- Help prevent tag name collisions
- Improve the ability to reuse code

See publication 1756-PM021, Logix 5000 Controllers Program Parameters Programming Manual, for more information on Parameters.

Use the following guidelines when you name tags.

| Guideline                                     | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create descriptive names but keep them short. | Tag names can be from 1 … 40 characters long. • Each character of the tag name uses 1 byte of controller memory, rounded to a 4-byte boundary. • For example, a tag name with 1…4 characters uses 4 bytes. A tag name with 5 characters uses 8 bytes. • Tag names are stored in the controller. • Use structures to reduce the number and size of tags needed. Program upload preserves tag names. |
| Create a naming convention.                   | Develop a tag-naming convention on electrical drawings or machine design. For example, Conv1_Full_PE101 combines the sensor function with the photoeye number.                                                                                                                                                                                                                                     |
| Use correct characters in tag names.          | Tag names follow the IEC 61131-3 standard. You can use: • Letters A through Z. • Numbers 0…9. • Underscore character (_). Tags must start with a letter to avoid confusion with logical expressions. The remaining characters can be any of the supported characters.                                                                                                                              |
| Pad names to improve sort order.              | The programming software displays tags in alphabetical order. If you use numbers in your tag names, pad the number with leading zeros so the names sort in the proper order. For example, tag names: TS1, TS2, TS3, TS10, TS15, TS20, TS30 display as: TS1, TS10, TS15, TS2, TS20, TS3, and TS30. Pad the numbers with zero so they display as: TS01, TS02, TS03, TS10, TS15, TS20, TS30.          |

## Guidelines for Extended Tag Properties

Use the following guidelines for extended tag properties.

| Guideline                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use extended tag properties to define additional information, such as limits, engineering units, or state identifiers, for various components within your controller project. | You can define extended tag properties for these components: • Tag • Parameter • User-defined data type • Add-On Instruction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Some extended tag properties support pass-through for data structures and arrays.                                                                                             | Pass-through behavior is available for descriptions, state identifiers, and engineering units and is configurable in data structures and arrays. Pass-through behavior is not available for limits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| You can read extended properties via logic, but you cannot write to extended properties values in logic.                                                                      | • Extended properties must be used as an input operand. • Alias tags with extended properties cannot be accessed in logic. • Limits can be configured for input and output parameters in Add-On Instructions. However, limit extended properties must not be defined on an InOut parameter of an Add-On Instruction. • Limits cannot be accessed inside Add-On Instruction logic. • If you read an extended property value in logic, it consumes memory equivalent to an equivalent program-scoped tag of that data type. If you do not use them in logic, extended tag properties use no user memory, only extended memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| If an array tag uses indirect addressing to access limit extended properties in logic, the following conditions apply.                                                                                                                                                                               | • If the array tag has limit extended properties that are configured, the extended properties are applied to any array element that does not explicitly have that particular extended property configured. For example, if the array tag MyArray has Max configured to 100, then any element of the array that does not have Max configured inherits the value of 100 when used in logic. However, it is not visible to you that the value inherited from MyArray is configured in the tag properties. • At least one array element must have specific limit extended property configured for indirectly referenced array logic to verify. For example, if MyArray[x].@Max is being used in logic, at least one array element of MyArray[] must have Max extended property configured if Max is not configured by MyArray. • Under the following circumstances a data type default value is used: – Array is accessed programmatically with an indirect reference. – Array tag does not have the extended property configured. – A member of an array does not have the extended property configured. |

## Tag Descriptions

The programming software searches a tag's origin to locate the first available description. This reduces the number of descriptions you need to enter. This also verifies that tag references display associated descriptions.

| Guideline                                                                           | Description                                   | Description                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tag descriptions display in the programming software according to the tag’s origin. | Type of Tag                                   | Description Display in the programming software                                                                                                                                                                                                                                                                                                                                  |
| Tag descriptions display in the programming software according to the tag’s origin. | Atomic                                        | For a BOOL, SINT, USINT, INT, UINT, DINT, UDINT, LINT, ULINT, REAL or LREAL tag, the description that is associated with the tag is the only description available for display.                                                                                                                                                                                                  |
| Tag descriptions display in the programming software according to the tag’s origin. | Alias                                         | First the alias tag description, then the base tag description.                                                                                                                                                                                                                                                                                                                  |
| Tag descriptions display in the programming software according to the tag’s origin. | User-defined structure and Add-On Instruction | All members use the description for tag, unless you define a specific description for a member. For example, MyTimer.DN uses the description for MyTimer if there is no description for MyTimer.DN.                                                                                                                                                                              |
| Tag descriptions display in the programming software according to the tag’s origin. | Atomic array                                  | • All references into an array use the description for the array, unless you define a description for an element of the array. • For example, MyTable[10] uses the description for MyTable if there is no description for MyTable[10]. • All indexed references into an array use the description for the array. • For example, MyTable[Index] uses the description for MyTable. |
| Tag descriptions display in the programming software according to the tag’s origin. | Structure array                               | All references to a member of a structure in an array default to the array definition, unless you define a description for the structure member of the array. For example, Table[0].Field1 uses the description for Table if there is no description for the specific field.                                                                                                     |

For more information, see the Create Tag Descriptions Automatically with User-Defined Data Types White Paper, publication LOGIX-WP004 .

## Protect Data Access Control at Tag Level

New tag attributes define access to tag data at runtime.

| Tag Attribute Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| External access Defines how an external application, such as an HMI, historian, or OPC data server, can access a tag. For arrays, this feature applies to the top level only; for user-defined structure, this feature applies to individual members. Possible values are: • Read/Write: External applications can both read and modify the tag’s value • Read Only: External applications can read the tag’s value, but not modify it • None: External applications can neither read or write the tag’s value |
| Constant Defines whether a tag value remains constant. Tags with this attribute set cannot be changed programmatically.                                                                                                                                                                                                                                                                                                                                                                                        |

You can Use RSLinx® Classic software, version 2.56 or later, RSLinx® Enterprise software, versions 5.21 to 5.90, or FactoryTalk® Linx software version 6.00 or later, for best results with these tag attributes. Using earlier versions of RSLinx software can result in anomalous behavior from the data servers with the external access options of Read Only and None.

## Buffer I/O Data

## Communicate with I/O

I/O values update at a period, requested packet interval (RPI), which you configure via Module Property dialog in the I/O configuration folder of the project. The values update asynchronously to the execution of logic.

The module sends input values to the controller at the specified RPI. Because this transfer is asynchronous to the execution of logic, an I/O value in the controller can change in the middle of a scan.

If you reference an I/O tag multiple times, and the application could be impacted if the value changes during a program scan, you must buffer the I/O value. You can buffer an I/O tag by using input parameters or coping into a buffer tag. In your code, reference the buffer tag rather than the I/O tag.

## IMPORTANT

Use the synchronous copy (CPS) instruction to buffer I/O data. While the CPS instruction copies data, no I/O updates or other tasks can change the data. Tasks that attempt to interrupt a CPS instruction are delayed until the instruction is done. Overuse of the CPS instruction can impact controller performance by keeping all other tasks from executing.

## Buffer I/O data to do the following:

- Help prevent an input or output value from changing during the execution of a program (I/O updates asynchronous to the execution of logic).
- Copy an input or output tag to a member of a structure or element of an array.
- Help prevent produced or consumed data from changing during the execution of a program.
- Make sure all produced and consumed data arrives or is sent as a group (not mixed from multiple transfers).
- Only use the CPS instruction if the I/O data that you want to buffer is greater than 32 bits (or 4 bytes) in size.

Overuse of the CPS instruction can greatly impact controller performance.

If you have a user-defined structure with members that represent I/O devices, you must use logic to copy the data into the members of the structure from the corresponding I/O tags.

<!-- image -->

## Guidelines to Specify an RPI Rate for I/O Modules

Configure an RPI rate per module (ControlLogix®) or an RPI rate per controller (CompactLogix®). The RPI value is the rate at which the controller attempts to communicate with the module.

<!-- image -->

| Guideline                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Specify an RPI at 50% of the rate that you need new data.                            | If you set the RPI faster (specify a smaller number) than what your application needs, it can waste network resources, such as ControlNet® schedule bandwidth, network processing time, and CPU processing time. For example, if you need information every 80 ms, set the RPI at 40 ms. The data is asynchronous to the controller scan, so you sample data twice as often (but no faster), you ensure that you have the most current data. |
| Group devices with similar performance needs onto the same module.                   | By grouping devices with similar performance needs on the same module, you consolidate data transmission to one module rather than multiple modules. This conserves network bandwidth.                                                                                                                                                                                                                                                       |
| Set the ControlNet™ network update time (NUT) equal to or less than the fastest RPI. | When configuring a ControlNet network, set the network update time (NUT) equal to or less than the fastest RPI of the I/O modules and produced/consumed tags in the system. For example, if your fastest RPI is 10 ms, set the NUT to 5 ms for more flexibility in scheduling the network.                                                                                                                                                   |
| In a ControlNet system, use even multiples of the NUT for the RPI value.             | Set the RPI to a binary multiple of the NUT. For example, if the NUT is 10 ms, select an RPI such as 10, 20, 40, 80, or 160 ms.                                                                                                                                                                                                                                                                                                              |
| In a ControlNet system, isolate I/O communication.                                   | If you use unscheduled ControlNet communication or want to be able to add ControlNet I/O at runtime (see page 103), dedicate one ControlNet network to I/O communication only. On the dedicated I/O network, make sure that there is the following: • No HMI traffic • No MSG traffic • No programming workstations • No peer-to-peer interlocking in multi-processor system architectures                                                   |
| In an EtherNet/IP™ system, module change of state is limited to 1/4 of the RPI.      | If you configure change of state communication for a module in a remote chassis that is connected via an EtherNet/IP network, the module can send data only as fast as the module RPI. Initially, the module sends its data immediately. However, when an input changes, the module data is held at the adapter until 1/4 of the RPI is reached to avoid overloading the EtherNet/IP network with the module communication.                  |
| Data transmission depends on the controller.                                         | The type of controller determines the data transmission rate. • ControlLogix controllers transmit data at the RPI that you configure for the module. • CompactLogix controllers transmit data at powers of 2 ms (such as 2, 4, 8, 16, 64, or 128). For example, if you specify an RPI of 100 ms, the data actually transfers at 64 ms.                                                                                                       |

## Communication Formats for I/O Modules

The communication format determines whether the controller connects to the I/O module via a direct or a rack-optimized connection. The communication format also determines the type and quantity of information that the module provides or uses.

## Direct Connection

Each module passes its data to/from the controller individually. Communication modules bridge data across networks.

| Benefits                                                                                                                                                  | Considerations                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| • Each module can determine its own rate (RPI) • More data can be sent per module, such as diagnostic and analog data • Supports event task communication | • Requires additional connections and network resources • This is the only method that is supported in the local chassis • I/O data is presented as individual tags |

<!-- image -->

## Rack-optimized Connection

The communication module in a remote chassis consolidates data from multiple modules into one packet and transmits that packet as one connection to the controller.

<!-- image -->

| Benefits                                                                                               | Considerations                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| • One connection can service a full chassis of digital modules • Reduces network resources and loading | • All Modules are sent at the same rate • Unused slots are still communicated • Still need a direct connection for analog and diagnostic data • Limited to remote chassis • I/O data is presented as arrays with alias tags for each module |

The rack-optimized format limits data to one 32-bit input word per module in a chassis. If you place a diagnostic module in a chassis, the rack-optimized format eliminates the value that the diagnostic module offers. In this case, it's better to use a direct connection so that the diagnostic information from the module is passed to the controller.

.

## Peer Control

Output modules let peer ownership of input modules to consume input data to directly control outputs without requiring controller processing.

The 1756-IB16IF and 1756-IB16IFC modules can be listened to presuming the output module knows the input data layout and connection information. The configuration from the controller defines how the peer input data is mapped to the output modules. The controller can use the other digital points on the module that are not peer-owned as conventional outputs.

The controller can also use the output data that it normally sends to the module with consumed inputs, letting 'gate-type' features enabled by controller logic selectively letting application of the consumed peer input data.

<!-- image -->

## Benefits

- Faster response time because the controller scan time is removed from the equation. Data is sent directly to the output module from the input module.
- Increases controller performance by reducing the need for event tasks to close loops quickly.
- Each input module has an AND and OR bit mask that defines the logic that is applied to each input module.

## Considerations

- You must program the controller for proper relationship with the output modules.
- The peer output module must be in the same chassis as the input module to maximize response time.

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

| Keying Option Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compatible Module           | Lets the installed device accept the key of the device that is defined in the project when the installed device can emulate the defined device. With Compatible Module, you can typically replace a device with another device that has the following characteristics: • Same catalog number • Same or higher Major Revision • Minor Revision as follows: – If the Major Revision is the same, the Minor Revision must be the same or higher. – If the Major Revision is higher, the Minor Revision can be any number. This is the default selection in the Logix Designer application.                       |
| Disable Keying              | Indicates that the keying attributes are not considered when attempting to communicate with a device. With Disable Keying, communication can occur with a device other than the type specified in the project. ATTENTION: Be cautious when using Disable Keying; if used incorrectly, this option can lead to personal injury or death, property damage, or economic loss. We strongly recommend that you do not use Disable Keying. If you use Disable Keying, you must take full responsibility for understanding whether the device being used can fulfill the functional requirements of the application. |
| Exact Match                 | Indicates that all keying attributes must match to establish communication. If any attribute does not match precisely, communication with the device does not occur.                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Carefully consider the implications of each keying option when selecting one.

## IMPORTANT

When you change Electronic Keying parameters online, it interrupts connections to the device and any devices that are connected through the device. Connections from other controllers can also be broken. If an I/O connection to a device is interrupted, the result can be a loss of data.

## More Information

For more detailed information on Electronic Keying, see Electronic Keying in Logix 5000™ Control Systems Application Technique, publication LOGIX-AT001 .

## Guidelines to Manage I/O Connections

Use the following guidelines to administer your I/O modules.

## IMPORTANT Compact 5000® I/O does not support rack-optimization.

1. The type of I/O module can determine the type of connection.
- Analog modules always use direct connections, except for 1771 analog modules that use messaging and 1734 analog modules that use Enhanced Rack Optimization.
- Digital modules can use direct or rack-optimized connections. Communication formats that include optimization in the title are rack-optimized connections; all other connection options are direct connections.
2. Select the communication format for a remote adapter based on the remote I/O modules.
3. Use rack-optimized connections to conserve connections.

| Select                     | If                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None                       | The remote chassis contains only analog modules, diagnostic digital modules, fused output modules, or communication modules. On a ControlNet network, use None to add a chassis to the network while the controller is running.                                                                                                                                                                                                                                                  |
| Rack-optimized             | The remote chassis only contains standard, digital input, and output modules (no diagnostic modules or fused output modules). For a ControlNet network at runtime (controller is online), you can add new digital modules to an existing rack-optimized connection, but new rack-optimized connections can only be added when offline. An EtherNet/IP network supports new rack-optimized connections both offline and at runtime (online). For more information, see page 103 . |
| Listen Only Rack-optimized | You want to receive I/O module and chassis slot information from a rack-optimized remote chassis that is owned by another controller. The runtime capability for listen only rack-optimized connections is the same as for rack-optimized connections.                                                                                                                                                                                                                           |

If you are trying to limit the number of controller and network connections, rackoptimized connections can help.

4. In some cases, all direct connections work best.

For a remote adapter that is configured for rack-optimized connections, there is always data that is sent for each slot in the chassis, even if a slot is empty or contains a direct connection module. There are 12 bytes of data that is transferred for rack-optimized overhead between the controller and the remote adapter. In addition, the remote adapter sends 8 bytes per slot to the controller; the controller sends 4 bytes per slot to the remote adapter.

For a few digital modules in a large chassis, it can be better to use direct connections because transferring the full chassis information can require more system bandwidth than direct connections to a few modules.

| Example                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Remote 17-slot chassis Slot 0: 1756-CNBR/D Slots 1…15: analog modules Slot 16: standard digital module | Option 1: Select Rack Optimization as the communication format for the remote adapter. This example uses 16 controller connections (15 for analog modules and 1 for the rack-optimized connection). This example also transfers: • 12 bytes for rack-optimized overhead. • 12 bytes for the digital module. • 12 bytes for each of the 15 analog modules, for a total of 180 bytes. Option 2: Select None as the communication format for the remote adapter. This example also uses 16 controller connections (1 direct connection to each I/O module). There is no rack-optimized overhead data to transfer. Recommendation: Option 2 is recommended because it avoids unnecessary network traffic, and thus improves network performance.                                                                                                                                                                                                                                                                                                                                                            |
| Remote 17-slot chassis Slot 0: 1756-CNBR/D Slots 1…8: analog modules Slots 9…16: digital modules       | Option 1: Select Rack Optimization as the communication format for the remote adapter. This example uses nine controller connections (eight for analog modules and one for the rack-optimized connection). This example also transfers: • 12 bytes for rack-optimized overhead. • 12 bytes for each of the 8 digital modules, for a total of bytes 96 bytes. • 12 bytes for each of the 8 analog modules, for a total of 96 bytes. Option 2: Select Rack Optimization for the communication format of the remote adapter. This example uses 16 controller connections (1 direct connection to each I/O module). There is no rack-optimized overhead data to transfer. Recommendation: The best option for this example depends on the type of digital I/O modules in the system and other controller connections. If the total system has many analog modules, diagnostic modules, fused output modules, or produced/consumed tags, select Option 1 to conserve controller connections. If there are plenty of controller connections available, select Option 2 to reduce unnecessary network traffic. |

## Create Tags for I/O Data

Each I/O tag is automatically created when you configure the I/O module through the programming software. Each tag name follows this format:

Location:SlotNumber:Type.MemberName.SubMemberName.Bit

| This address variable Is   |                                                                                                                  |
|----------------------------|------------------------------------------------------------------------------------------------------------------|
| Location                   | Identifies network location LOCAL = local chassis or DIN rail ADAPTER_NAME = identifies remote adapter or bridge |
|                            | SlotNumber Slot number of I/O module in its chassis                                                              |
| Type                       | Type of data: I = inputC = configuration O = outputS = status                                                    |
|                            | MemberName Specific data from the I/O module, such as Data and Fault; depends on the module                      |
|                            | SubMemberName Specific data that is related to a MemberName                                                      |
| Bit (optional)             | Specific point on the I/O module; depends on the size of the I/O module (0…31 for a 32- point module)            |

If you configure a rack-optimized connection, the software creates a rack-object tag for the remote communication module. You can reference the rack-optimized I/O module individually, or by its element within the rack-object tag.

<!-- image -->

## Controller Ownership

When you choose a communication format, you have to choose whether to establish an owner or listen-only relationship with the module.

| Mode Description                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Owner The owner controller writes configuration data and can establish a connection to the module.                                                                                                                                                |
| Listen-only A controller that uses a listen-only connection only monitors the module. It does not write configuration data and can only maintain a connection to the I/O module when the owner controller is actively controlling the I/O module. |

There is a noted difference in the ownership of input modules versus the ownership of output modules.

|                | Controlling This Ownership Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input modules  | Owner                                    | An input module is configured by a controller that establishes a connection as an owner. This configuring controller is the first controller to establish an owner connection. Once an input module has been configured (and owned by a controller), other controllers can establish owner connections to that module. This lets additional owners continue to receive multicast data if the original owner controller breaks its connection to the module. All other additional owners must have the identical configuration data and identical communication format that the original owner controller has, otherwise the connection attempt is rejected. |
| Input modules  | Listen-only                              | Once an input module has been configured (and owned by a controller), other controllers can establish a listen-only connection to that module. These controllers can receive multicast data while another controller owns the module. If all owner controllers break their connections to the input module, all controllers with listen-only connections no longer receive multicast data.                                                                                                                                                                                                                                                                  |
| Output modules | Owner                                    | An output module is configured by a controller that establishes a connection as an owner. Only one owner connection can be connected to an output module. If another controller attempts to establish an owner connection, the connection attempt is rejected.                                                                                                                                                                                                                                                                                                                                                                                              |
| Output modules | Listen-only                              | Once an output module has been configured (and owned by one controller), other controllers can establish listen-only connections to that module. These controllers can receive multicast data while another controller owns the module. If the owner controller breaks its connection to the output module, all controllers with listen-only connections no longer receive multicast data.                                                                                                                                                                                                                                                                  |

## Runtime/Online Addition of Modules

You can add modules when the controller is in Run mode.

| Network             | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ControlNet network  | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. | You can use: • 1756-CN2, 1756-CN2R, 1756-CN2RTXT any series modules. • 1756-CNB, 1756-CNBR series D or later communication modules. Digital I/O modules can be added as rack-optimized connections if the parent module is already configured with rack-optimized connections. While you can add a new digital I/O module to an existing rack-optimized connection, you cannot add rack-optimized connections while online. Digital I/O modules can also be added as direct connections. Analog I/O modules can be added only as direct connections. Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent more quickly than the RPI. If you plan to add large amounts of I/O to the ControlNet network, dedicate one ControlNet network for I/O. For the dedicated ControlNet network, verify that there is little or no: • HMI traffic. • MSG traffic. • Programming workstations. |
|                     | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       | You can add I/O modules until you reach these limits: • 80% of CPU utilization of the 1756-CN2, 1756-CN2R, or 1756-CN2RXT communication module. • Less than 400,000 unscheduled bytes per second are displayed in RSNetWorx™ for ControlNet software after the network has been scheduled. Considerations for 1756-CNB, 1756-CNBR Modules Requested Packet Intervals (RPIs) faster than 25 ms for unscheduled modules can overload the 1756-CNB or 1756-CNBR communication module. To avoid the overload, make these considerations: • Use a NUT of 10 ms or more.                                                                                                                                                                                                                                                                                                                                                                       |
| EtherNet/IP network | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The EtherNet/IP I/O modules that you add at runtime can be: • Added to existing rack-optimized connections • Added to new rack-optimized connections • Added as direct connections (you can create rack-optimized connections when adding EtherNet/IP I/O modules at runtime) You can add I/O modules until you reach the limits of the communication module:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                     | 1756-EN4TR, 1756-EN4TRXT Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1756-EN2TR, 1756-EN3TR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1756-EN2T, 1756-EN2TP, 1756-EN2TXT, 1756-EN2F Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1756-ENBT Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 5069-AENTR, 5094-AENTxx COMPACT 5000 I/O Ethernet Adapter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 5069-AEN2TR COMPACT 5000 I/O Ethernet Adapter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                     | • 50,000 pps without CIP Security™ • 25,000 pps with integrity • 15,000 pps with integrity and confidentiality                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 20,000 pps 10,000 pps 5000 pps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 100,000 pps (total number of packets from both Ethernet Ports)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 100,000 pps (total number of packets from both Ethernet Ports)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 512 TCP connections 128 TCP connections 128 TCP connections 64 TCP connections 32 TCP Connections 32 TCP Connections                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                     | CIP™ connected messages: 1000 I/O 528 CIP™ connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 256 CIP connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 256 CIP connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 128 CIP connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 80 CIP connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 320 CIP connected messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Online Addition of Module and Connection Types

| Module Type and Connection Method                            | In Local Chassis   | Remote Via an EtherNet/IP Network   | Remote Via a ControlNet® Network   | Remote Via a ControlNet® Network            | Configure Hold Last Output State      | Remote Via a ControlNet® Network   |
|--------------------------------------------------------------|--------------------|-------------------------------------|------------------------------------|---------------------------------------------|---------------------------------------|------------------------------------|
| Module Type and Connection Method                            |                    | Offline Runtime Offline Runtime     | Offline                            | Runtime                                     | Offline only                          |                                    |
| Module Type and Connection Method                            |                    | Offline Runtime Offline Runtime     |                                    | Scheduled Unscheduled Scheduled Unscheduled | Offline only                          |                                    |
| Digital - direct                                             |                    | Yes Yes Yes Yes Yes Yes — Yes       |                                    |                                             | Yes - 1756 I/O digital output modules |                                    |
| Digital - rack-optimized — — Yes Yes Yes —                   |                    |                                     |                                    | Yes —                                       | Yes - 1756 I/O digital output modules |                                    |
| Analog - direct                                              |                    | Yes Yes Yes Yes Yes Yes — Yes Yes   |                                    |                                             |                                       |                                    |
| Generic third-party - direct Yes Yes Yes Yes Yes Yes — Yes — |                    |                                     |                                    |                                             |                                       |                                    |
| 1715 Redundant I/O — — Yes Yes — —                           |                    |                                     |                                    | — —                                         | —                                     |                                    |
| 1718/1719 I/O                                                |                    | — — Yes Yes — —                     |                                    | — —                                         | Yes – both analog and digital modules |                                    |
| 1756-ENx - no connection Yes Yes Yes Yes — —                 |                    |                                     |                                    | — —                                         | —                                     |                                    |
| 1756-ENx - rack-optimized — — Yes Yes — —                    |                    |                                     |                                    | — —                                         | —                                     |                                    |
| Generic EtherNet/IP third party - direct                                                              |                    | — — Yes Yes — — — — —               |                                    |                                             |                                       |                                    |
| 1788-EN2FFR or 1788-EN2PAR                                   |                    |                                     |                                    | — — — — — — Yes Yes —                       |                                       |                                    |
| 1788-CN2FFR or 1788-CN2PAR                                   |                    | — — Yes Yes No Yes — — —            |                                    |                                             |                                       |                                    |
| 1794 FLEX™ I/O                                               |                    | — — Yes — Yes Yes — —               |                                    |                                             | Yes - Analog output modules only      |                                    |
| 1734 POINT I/O™                                              |                    | — — Yes — Yes Yes — —               |                                    |                                             | Yes                                   |                                    |
| 1734 POINT Guard I/O™ Yes — Yes — — —                        |                    |                                     |                                    | — —                                         | —                                     |                                    |
| 5069 Compact 5000 I/O Yes — Yes  Yes(1)                      |                    |                                     |                                    |                                             | — — — — Yes                           |                                    |
| 5069 Compact 5000 I/O Safety Modules                         |                    | Yes — Yes — — —                     |                                    | — —                                         | —                                     |                                    |
| 5094 FLEX 5000                                               |                    | — — Yes Yes — —                     |                                    | — —                                         | Yes                                   |                                    |
| 5094 FLEX 5000® I/O Safety Modules                           |                    | — — Yes — — —                       |                                    | — —                                         | Yes                                   |                                    |

(1) Only supported if adding an entire rack of Compact 5000 I/O modules.

## Design Considerations for Runtime/Online Addition of Modules

When you design your network, address these considerations to add modules at runtime.

|                         | Design Issue Considerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I/O modules             | If you plan to add 1756 I/O modules at runtime, leave space in the local chassis, remote chassis on a ControlNet network, or remote chassis on an EtherNet/IP network for the I/O modules you want to add.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Other modules           | You can add 1757-FFLDC devices remotely via the unscheduled portion of a ControlNet network at runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Input transmission rate | Make sure the RPIs work for the data you want to send and receive. Make sure the added I/O does not depend on change of state data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Network topology        | On a ControlNet network, install spare taps so you can add modules at runtime without disrupting the network. Each tap must be terminated not to ground out the system. Check ControlNet system requirements to determine how many spare taps your network can support. • In a ControlNet network with redundant cabling, you can break the trunk and add a tap, but redundant cabling is lost during the module installation. • In a ControlNet ring, add a drop off the ring or add new nodes off the coax and disrupt only part of the network. • You could remove an existing node and add a repeater off that drop. Then reconnect the existing node and add any new nodes off the new segment. On an EtherNet/IP network, reserve some connection points on the switch so that you can connect additional nodes or switches in the future. |
| Network configuration   | On a ControlNet network, plan which communication can be scheduled or unscheduled. On an EtherNet/IP network, all communication is immediate and occurs based on the module RPI (also referred to as unscheduled). If you know that you need a new chassis with digital modules in the future, configure the network and add it to the I/O configuration tree as rack-optimized. Then inhibit the communication adapter until you need the chassis.                                                                                                                                                                                                                                                                                                                                                                                              |
| Network performance     | You can add modules at runtime until you impact the capacity of the communication module. Make sure that you have sufficient communication modules for the connections you plan to add.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Notes:

<!-- image -->

## Determine the Appropriate Network

EtherNet/IP™, ControlNet®, and DeviceNet® networks share a universal set of communication services. These are the recommended networks for Logix control systems.

| Comparison                | EtherNet/IP Network                                                                                                     | ControlNet Network                                                                 | DeviceNet Network                                                                                           |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Function                  | Plant management system tie-in (material handling); configuration, data collection, and control on a high-speed network | Supports transmission of time critical data between PLC processors and I/O devices | Connects low-level devices directly to plant-floor controllers—without interfacing them through I/O modules |
| Typical devices networked | Mainframe computers Programmable controllers Robots HMI I/O Drives Process instruments                                  | Programmable controllers I/O chassis HMIs PCs Drives Robots                        | Sensors Motor starters Drives PCs Push buttons Low-end HMIs Barcode readers PLC processors Valve manifolds  |
| Data repetition           | Large packets, data sent regularly                                                                                      | Medium-size packets; data transmissions are deterministic and repeatable           | Small packets; data is sent as needed                                                                       |
| Number of nodes, max      | Network overall: no limit                                                                                               | 99 nodes                                                                           | 64 total nodes                                                                                              |
| Data transfer rate        | 10 Mbps, 100 Mbps, or 1000 Mbps 5 Mbps                                                                                  |                                                                                    | 500 Kbps, 250 Kbps, or 125 Kbps                                                                             |
| Typical use               | Plant-wide architecture High-speed applications Redundant Applications Safety Applications                              | Redundant applications Scheduled communication                                     | Supply power and connectivity to low-level devices.                                                         |

Follow these guidelines when planning a network.

| Design Issue            | Considerations                                                                                                                                                                                          |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Network topology        | Plan for future connections. Plan for additional controllers and/or communication modules to handle future I/O modules. Consider distances between devices. Determine resiliency requirements.          |
| Network configuration   | On a ControlNet network, plan which communication can be scheduled or can be unscheduled. On an EtherNet/IP network, all I/O communication is based on the RPI of the module.                           |
| Network performance     | Make sure that you have sufficient communication modules for the connections you plan to use. Use available network performance tools.                                                                  |
| Chassis                 | Consolidate communication connections for multiple modules to one network node. Group digital I/O modules into a rack-optimized connection to reduce the amount of communication and network bandwidth. |
| Input transmission rate | Make sure the RPIs work for the data you want to send and receive. Make sure that I/O added at runtime does not depend on change of state data.                                                         |

## EtherNet/IP Network Topology

## EtherNet/IP Network

- An EtherNet/IP network supports messaging, produced and consumed tags, and distributed I/O.
- An EtherNet/IP network with 5570 or earlier, and 5370 or earlier controllers supports half-duplex/full-duplex, 10 Mbps or 100 Mbps operation.
- An EtherNet/IP network with 5590, 5580 or 5380 controllers supports full-duplex, 10/ 100/1000 Mbps operation.
- An EtherNet/IP network requires no network scheduling.
- There are several methods available to configure EtherNet/IP network parameters for devices. Not all methods are always available. These methods are device and configuration dependent:
- – DHCP
- – Rockwell Automation® BOOTP/DHCP utility
- – Programming software
- – Studio 5000 Logix Designer® application
- – RSNetWorx™ for EtherNet/IP software
- – Web browser
- – SNMP tools
- 5590 and 5380 controllers can connect directly to a DLR topology via dual built-in Ethernet ports

## Application Ideas

- Connectivity to commercial devices (such as cameras and phones)
- Business systems with remote access or sharing data
- Applications with motion or safety on the same network.
- Plant management (material handling)
- Configuration, data collection, and control on a high-speed network
- Time-critical applications with no established schedule
- Inclusion of commercial technologies (such as video over IP)
- Internet/Intranet connection

This section features these controllers, and where applicable, the controllers are known as:

| Controller Family Includes these controllers                                |
|-----------------------------------------------------------------------------|
| 5590 controllers ControlLogix® 5590 controllers                             |
| 5580 controllers ControlLogix 5580 and GuardLogix® 5580 controllers         |
| 5380 controllers CompactLogix® 5380 and Compact GuardLogix 5380 controllers |
| 5570 controllers ControlLogix 5570 and GuardLogix 5570 controllers          |
| 5370 controllers CompactLogix 5370 and Compact GuardLogix 5370 controllers  |

## Example Topologies

<!-- image -->

## Guidelines for EtherNet/IP Networks

| Guideline                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use these publications.                                     | • EtherNet/IP Network Devices User Manual ENET-UM006A-EN-P, publication ENET-UM006 • EtherNet/IP Device Level Ring Application Technique, publication ENET-AT007 • EtherNet/IP Design Considerations Reference Manual, publication ENET-RM002                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Data transmission depends on the controller.                | The type of controller determines the data transmission rate. • ControlLogix controllers transmit data at the RPI that you configure for the module. • CompactLogix controllers transmit data at powers of 2 ms (such as 2, 4, 8, 16, 64, or 128). For example, if you specify an RPI of 100 ms, the data actually transfers at 64 ms.                                                                                                                                                                                                                                                                                                                                                     |
| You can add I/O modules at runtime.                         | You can add I/O modules to remote chassis connected via an EtherNet/IP network to a running controller. You can configure direct or rack-optimized connections. For more information, see Runtime/Online Addition of Modules on page 103 .                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Data transmission rate depends on the RPI.                  | An EtherNet/IP network broadcasts I/O information to the controller based on the RPI setting. With change of state (COS) enabled and: • No data changes, the EtherNet/IP module produces data every RPI. • Data changes, the EtherNet/IP module produces data at a maximum rate of RPI/4.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Select unicast EtherNet/IP communication whenever possible. | To reduce bandwidth use and preserve network integrity, some facilities block multicast Ethernet packets. Multicast is a more efficient method for transmitting data with multiple consumers and redundancy applications. You can configure multicast or unicast connections for: • Produced and consumed tags by using the Logix Designer application • I/O modules by using the Logix Designer application. Unicast connections help with the following: • Let produced and consumed tag communication span multiple subnets • Reduce network bandwidth. • Simplify configuration for EtherNet/IP network devices because of unicast default setting for the Logix Designer application. |

## ControlNet Network Topology

## ControlNet Network

- A ControlNet network lets both I/O and messaging on the same wire.
- Multiple controllers and their respective I/O can also be placed on the same ControlNet wire.
- When new I/O is added, or when the communication structure on an existing I/O module changes, you must use RSNetWorx for ControlNet software to reschedule the network.
- If the network timing changes, every device with scheduled traffic on the network is affected.
- To reduce the impact of changes, place each CPU and its respective I/O on isolated ControlNet networks.
- Place shared I/O and produced/consumed tags on a common network available to each CPU that needs the information.
- Built-in redundant cabling supports I/O network and provides HMI switchover in redundant ControlLogix system.

## Application Ideas

- Default Logix network
- Best replacement for universal remote I/O
- Backbone to multiple distributed DeviceNet networks
- Peer interlocking network
- Common devices include: Logix 5000® controllers, PanelView™ terminals, I/O modules, and drives

## Guidelines for ControlNet Networks

| Guideline                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use these publications.                                                                                                    | • ControlNet Coax Media Planning and Installation Guide, publication CNET-IN002 • ControlNet Fiber Media Planning and Installation Guide, publication CNET-IN001 • ControlNet Network Configuration User Manual, publication CNET-UM001                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Adjust the default RSNetWorx for ControlNet settings.                                                                      | Change these settings in the RSNetWorx for ControlNet software: • UMAX (highest unscheduled node on the network) – Default is 99 – The network takes the time to process the total number of nodes that are specified in this setting, even if there are not that many devices on the network – Change to a reasonable level to accommodate the active network devices and additional devices that can be connected • SMAX (highest scheduled node on the network) – Default is 1 – This must be changed for all systems – Set SMAX < UMAX                                                                                                                                                                                  |
| Design for at least 400 KB of available, unscheduled network bandwidth, as displayed by RSNetWorx for ControlNet software. | Leaving too little bandwidth for unscheduled network communication results in poor message throughput and slower workstation response. Unscheduled data transfers on ControlNet occur asynchronously to the program scan and support a maximum of 510 bytes/node per ControlNet NUT.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Place DeviceNet (1756-DNB) communication modules in the local chassis.                                                     | DeviceNet (1756-DNB) communication modules have multiple, 500-byte data packets that impact scheduled bandwidth. Place these modules in the same chassis as the controller to avoid this data being scheduled over the DeviceNet network. If you must place these communication devices in remote chassis, configure the input and output sizes to match the data that is configured in RSNetWorx for DeviceNet software. This reduces the amount of data that must be transmitted.                                                                                                                                                                                                                                         |
| Limit 1756-CNB, 1756-CNBR connections.                                                                                     | For best performance, limit the 1756-CNB, 1756-CNBR to 40…48 connections. Add additional 1756-CNB, 1756-CNBR modules in the same chassis if you need more connections. To improve system performance, you can add more modules and split connections among the modules. If the chassis that contains the CNB module also contains multiple digital I/O modules, configure the CNB communication format for Rack Optimization. Otherwise, use None. As a cost savings measure, use 1756-CNB, 1756-CNBR modules in chassis that contain only I/O modules for traditional adapter functionality. Use the 1756-CN2, 1756-CN2R, 1756-CN2RXT modules in the same chassis as the controller for traditional scanner functionality. |
| For additional connections, consider the 1756-CN2, 1756-CN2R, 1756-CN2RXT modules.                                         | The 1756-CN2/B, 1756-CN2R/B, 1756-CN2RTXT communication modules each support 131 connections, and have higher performance than previous modules. The 1756-CN2/A, 1756-CN2R/A communication modules each support 100 connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Topology

<!-- image -->

|                                                                 | Guideline Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If you change network settings, resave each controller project. | Anytime that you edit the network with RSNetWorx for ControlNet software and you save or merge your edits, connect to each controller in the system with their respective project file and perform a save and upload. This copies the ControlNet settings into the offline, database file and makes sure that future downloads of the controller permit it to go online without having to run RSNetWorx for ControlNet software. |
| You can add I/O modules at runtime.                             | You can add 1756 I/O modules and some drives to remote chassis connected via ControlNet to a running controller. It is recommended to use a 1756-CN2/B, 1756-CNB2R/B, or 1756-CN2RXT module as the traditional scanner in these applications.                                                                                                                                                                                    |
| Data transmission depends on the controller.                    | The type of controller determines the data transmission rate. • ControlLogix controllers transmit data at the RPI that you configure for the module. • CompactLogix controllers transmit data at powers of 2 ms (such as 2, 4, 8, 16, 64, and 128). For example, if you specify an RPI of 100 ms, the data actually transfers at 64 ms.                                                                                          |

## Guidelines for Unscheduled ControlNet Networks

| Guideline                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You can run an entire ControlNet network as unscheduled.                  | An unscheduled ControlNet network: • provides for easier network configuration. • is useful if your I/O updates needs are slower. • supports the addition of 1756 I/O modules and some drives without placing the controller in Program mode. • provides an HMI network with fast switchover times in a redundant controller system. You must still run RSNetWorx for ControlNet software at least once to configure NUT, SMAX, UMAX, and media configuration settings.                                                                                                                                                                                                                                                                                       |
| Plan appropriately if you place I/O on an unscheduled ControlNet network. | Follows these recommendations for I/O on an unscheduled ControlNet network: • A 1756-CN2, 1756-CN2R Series B or later, or a 1756-CN2RXT is recommended. • Disable the Change of State (COS) feature on digital input modules because it can cause inputs to be sent faster than the RPI. • Set the real-time sample (RTS) on analog cards slower than the RPI • Dedicate a ControlNet network to I/O only. • Do not exceed 80% utilization of a 1756-CN2, 1756-CN2R, 1756-CN2RXT communication module. • Do not exceed 75% utilization of a 1756-CNB, 1756-CNBR communication module. • Have no more than 48 connections on the 1756-CNB, 1756-CNBR communication module. • Use a NUT of 10 ms or more. • Keep the SMAX and UMAX values as small as possible. |
| 1756-CNB, 1756-CNBR only Set the RPI at 25 ms or slower.                  | Use RPI of 25 ms or slower for unscheduled modules to avoid overload on the 1756-CNB, 1756-CNBR communication module. Depending on the RPI, the communication module loading increases 1…4% for each I/O module added. Additional 1756-CNB, 1756-CNBR Loading RPI (ms) Additional CNB Loading % 45% 4.0% 3.5% 3.0% 2.5% 2.0 % 1.5% 1.0 % 0.5% 0.0% 25 45 65 85 105 125 145 165 185 205 225 245                                                                                                                                                                                                                                                                                                                                                                |

<!-- image -->

<!-- image -->

| Guideline                                                                   | Description                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-CNB, 1756-CNBR only The RPI affects how many I/O modules you can have. | This chart shows the number of modules and associated RPIs so that you do not exceed 75% utilization of the 1756-CNB, 1756-CNBR communication module. Maximum Number of I/O Modules in an Unscheduled Network Number of Unscheduled Modules 60 50 40 30 20 10 0 25 30 35 40 45 50 55 60 65 70 75 80 |

## Compare Scheduled and Unscheduled ControlNet Communication

| Scheduled ControlNet Communication                                                                                                                                                                                                                                                                                                                | Unscheduled ControlNet Communication                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Deterministic                                                                                                                                                                                                                                                                                                                                     | Less deterministic than scheduled communication Provides simpler ControlNet installations when scheduled networks are not required                                          |
| To add scheduled I/O on the ControlNet network, you must: • Add the I/O to an offline controller project. • Download the project to the controller. • Run RSNetWorx to schedule the network requires network to be scheduled (must stop the network and put the controller in Program mode to schedule a network). • Save the controller project. | Can be changed online without impacting the schedule New modules can affect other modules communicating via unscheduled bandwidth Supports 1756 I/O modules and some drives |
| RPI and NUT determine module communication rates                                                                                                                                                                                                                                                                                                  | RPI determines module communication rates                                                                                                                                   |
| MSG and HMI traffic can occur on the same network because they are isolated in unscheduled traffic MSG and HMI traffic do not affect I/O communication                                                                                                                                                                                            | Recommend 1756-CN2, 1756-CN2R, 1756-CN2RXT Recommend a dedicated ControlNet network for only I/O modules MSG and HMI traffic can affect I/O communication                   |
| Direct and rack-optimized connections to I/O                                                                                                                                                                                                                                                                                                      | Only direct connections to I/O (results in being able to use fewer total I/O modules because of the connection limits of controllers and communication modules)             |
| Supports any firmware revision of a ControlNet communication module                                                                                                                                                                                                                                                                               | You can use any 1756-CN2, 1756-CN2R, 1756-CN2RXT communication module If you use a 1756-CNB, 1756-CNBR communication module, it must be series D or later                   |
| Supports any I/O platform that can communicate via a ControlNet network Supports only 1756 I/O modules                                                                                                                                                                                                                                            |                                                                                                                                                                             |

## DeviceNet Network Topology

<!-- image -->

## Guidelines for DeviceNet Networks

| Guideline                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use these publications.                                                             | • DeviceNet Cable System Manual, publication DNET-UM072 • DeviceNet Network Configuration User Manual, publication DNET-UM004                                                                                                                                                                                                                                                                             |
| Use the DeviceNet Tag Generator tool.                                               | The Logix Designer application includes a DeviceNet tag generator tool that creates device-specific structured tags and logic based on the network configuration in RSNetWorx for DeviceNet software. The logic copies data to and from the DNB data array tags to the device tags so that data is presented synchronously to program scan.                                                               |
| Place DeviceNet (DNB) communication modules in the local chassis.                   | Place DNB modules in the local chassis to help maximize performance, especially in ControlLogix systems. Size the input and output image for the DNB modules to the actual devices that are connected plus 20% for future growth. If you have to place DNB modules in remote chassis, sizing the input and output images is critical for best performance.                                                |
| Verify that the total network data does not exceed the maximum DNB data table size. | A DNB supports: • 124, 32-bit input words. • 123, 32-bit output words. • 32, 32-bit status words. You can use RSNetWorx for DeviceNet software offline to estimate network data. Use a second DNB if there is more network data than one module can support.                                                                                                                                              |
| Configure clients first.                                                            | Configure device parameters before adding that device to the scanlist. You cannot change the configuration of many devices once they are already in the scanlist. If you configure the scanner first, there is a chance that the scanner configuration cannot match the current configuration for a device. If the configuration does not match, the device does not show up when you browse the network. |
| Leave node address 63 open to add nodes.                                            | Devices default to node 63 out-of-the-box. Leave node address 63 unused so you can add a new device to the network. Then change the address of the new device.                                                                                                                                                                                                                                            |
| Leave node address 62 open to connect a computer.                                   | Always leave at least one open node number to let a computer be attached to the network if needed for troubleshooting or configuration.                                                                                                                                                                                                                                                                   |
| Don’t forget to set the scanner run bit.                                            | For the scanner to be in Run mode, the controller must be in Run mode and the logic in the controller must set the scanner run bit.                                                                                                                                                                                                                                                                       |

Make sure that you have the most current EDS files for your devices.

RSNetWorx for DeviceNet software uses EDS file to recognize devices. If the software is not properly recognizing a device, you are missing the correct EDS files. For some devices, you can create an EDS file by uploading information from the device. Or you can get EDS files from: http://www.ab.com/networks/eds .

## Notes:

## Cache Messages

<!-- image -->

## Communicate with Other Devices

The MSG instruction asynchronously reads or writes a block of data to another device.

| If the target device is a                                                      | Select one of these message types   |
|--------------------------------------------------------------------------------|-------------------------------------|
| Logix 5000® controller                                                         | CIP™ Data Table Read                |
| Logix 5000® controller                                                         | CIP Data Table Write                |
| I/O module that you configure with the Studio 5000 Logix Designer® application | Module Reconfigure                  |
| I/O module that you configure with the Studio 5000 Logix Designer® application | CIP Generic                         |
| SERCOS drive                                                                   | SERCOS IDN Read                     |
| SERCOS drive                                                                   | SERCOS IDN Write                    |
| PLC-5® controller                                                              | PLC5 Typed Read                     |
| PLC-5® controller                                                              | PLC5 Typed Write                    |
| PLC-5® controller                                                              | PLC5 Word Range Read                |
| PLC-5® controller                                                              | PLC5 Word Range Write               |
| SLC™ controller MicroLogix™ controller                                         | SLC Typed Read                      |
| SLC™ controller MicroLogix™ controller                                         | SLC Typed Write                     |
| Block transfer module                                                          | Block Transfer Read                 |
| Block transfer module                                                          | Block Transfer Write                |
| PLC-3® processor                                                               | PLC3 typed read                     |
| PLC-3® processor                                                               | PLC3 typed write                    |
| PLC-3® processor                                                               | PLC3 word range read                |
| PLC-3® processor                                                               | PLC3 word range write               |
| PLC-2® processor                                                               | PLC2 unprotected read               |
| PLC-2® processor                                                               | PLC2 unprotected write              |

Some types of messages use a connection to send or receive data. Some also give you the option to either leave the connection open (cache) or close the connection when the message is done transmitting. This table shows messages that use a connection and whether you can cache the connection.

| Message Type                         | Communication Method Uses Connection Can Cache Connection   |                |                 |
|--------------------------------------|-------------------------------------------------------------|----------------|-----------------|
| CIP data table read or write CIP     |                                                             | Yes            | Yes             |
|                                      | CIP                                                         |                |                 |
| PLC2, PLC3, PLC5, or SLC (all types) | CIP with Source ID                                          |                |                 |
|                                      | DH+™                                                        | Yes            | Yes             |
| CIP generic                          | N/A                                                         | Your option(1) | Your option (1) |
| Block transfer read or write N/A     |                                                             | Yes            | Yes             |

A cached connection remains open until one of the following occurs:

- The controller goes to Program mode.
- You rerun the message as uncached.
- Another message is initiated and a cached buffer is needed.
- An intermediate node in the connection goes down.

## Message Buffers

The controller has buffers for unconnected messages and for cached messages. Buffers store incoming and outgoing message data until the controller can process the data.

<!-- image -->

| Buffer                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outgoing, unconnected | The outgoing unconnected buffers are for: • Establishing I/O connections to local I/O modules and remote devices on ControlNet®, EtherNet/IP™, and remote I/O networks. • Executing unconnected PLC2, PLC3, PLC5, or SLC (all types) messages over Ethernet/IP or ControlNet (CIP and CIP with Source ID) networks. • Initiation of messaging over a DH+™ network (uses 2 buffers, one to open the connection and one to transfer data). • Initiation of uncached block transfers. • Initiation of uncached CIP read/write message instructions. • Initiation of cached block transfers. • Initiation of cached CIP read/write messages instructions. • CIP Generic message instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Incoming, unconnected | The incoming unconnected buffers: • Initially receive a cached CIP message instruction. • Receive an uncached CIP message instruction. • Receive a message over a DH+ network. • Receive a CIP Generic message instruction. • Receive a read or write request from a ControlNet PanelView™ terminal (unconnected messaging). • Initially receive of a read request from an EtherNet/IP PanelView terminal (connected messaging). • Receive a write request from an EtherNet/IP PanelView terminal (unconnected messaging). • Receive an initial request from the Logix Designer application to go online. • Initially receive Linx-based connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cached buffers        | The cached buffers are outgoing buffers for messages and block transfers. A cached connection helps message performance because the connection is left open and does not need to be re-established the next time that it is executed. A cached connection counts towards the total limit of connections for a controller. A cached connection is refreshed at the connection RPI. All cached entries are closed when the controller transitions to Program mode. The first time a cached message is executed, it uses one of the outgoing unconnected buffers. When the connection is established, it moves into the cached buffer area. For optimum performance, do not cache more messages or block transfers than there are cached buffers. If you cache more than the available cached buffers, the controller looks for a connection that has been inactive for the longest time, closes that connection, and lets a new connection take its place. The controller closes a cached message or block transfer, depending on which has been inactive the longest. If all cached connections are in use, the message is executed as connected and, once it is completed, the connection is closed. You can multiplex cached connections. If a connection is inactive and a message instruction executes that has the same target and path, it uses that inactive connection. For example, if you have a block transfer read and write to the same module, interlock the read and write so that only one is active at a time. Then when they are cached, they use the same cached connection. |

## Outgoing Unconnected Buffers

|         | IMPORTANT  This section does not apply to 5380, 5480, 5580, or 5590 controllers.                                                                                                                                                                                                            |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Buffers | Use                                                                                                                                                                                                                                                                                         |
| 1…10    | The first 10 buffers (default) are shared for unconnected messaging, initiating connected messaging, establishing I/O connections, and establishing produced/consumed connections.                                                                                                          |
| 11      | The 11th buffer is dedicated to establishing I/O and produced/consumed connections.                                                                                                                                                                                                         |
| 12…40   | The 12th to the 40th buffers are used only for initiating connected messages and executing unconnected messages. To increase the outgoing buffers to a value higher than 11, execute a CIP generic message to configure that change each time you transition from Program mode to Run mode. |

## Guidelines for Messages

| Guideline                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message tags can be created at controller scope (all controller) or program scope (5380, 5480, 5580, and 5590 controllers only) | The operating system accesses the information in a message tag asynchronously to the program scan. Along with the visible fields within the message tag, there are hidden attributes that are only referenced by the background operating system.                                                                                                                                                                                                                                                                                                                                                      |
| You can use a message to send a large amount of data.                                                                           | Even though there are network packet limitations (such as 500 bytes on ControlNet and 244 bytes on DH+), the controller can send a large amount of data from one MSG instruction. When configuring the message, select an array as the source/destination tags and select the number of elements (as many as 32,767 elements) you want to send. The controller automatically breaks the array into small fragments and sends the fragments to the destination. On the receiving side, the data appears in fragments, so some application code can be required to detect the arrival of the last piece. |
| Do not manipulate the message status bit                                                                                        | Do not change the following status bits of a MSG instruction: • DN • EN • ER • EW • ST Do not change those bits either by themselves or as part of the FLAGS word. If you do, the controller can have a nonrecoverable fault. The controller clears the project from its memory when it has a nonrecoverable fault.                                                                                                                                                                                                                                                                                    |

## Guidelines to Manage Message Connections

| Guideline                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create user-defined structures or arrays. | User-defined structures let you organize your data to match your machine or process. • One tag contains all data that is related to a specific aspect of your system. This keeps related data together and easy to locate, regardless of its data type. • Each individual piece of data (member) gets a descriptive name. This automatically creates an initial level of documentation for your logic. • You can use the structure to create multiple tags with the same data layout. • Linx-based software can optimize user-defined structures more than standalone tags. |
| Cache connections when appropriate.       | If a message executes frequently, cache the connection. This keeps the connection open and optimizes execution time. You can increase execution time if you open a connection each time the message executes. If a message executes infrequently, do not cache the connection. This closes the connection upon completion of the message, which frees up that connection for other uses.                                                                                                                                                                                    |

## Guidelines for Block Transfer Messages

| Guideline                                                                                                                         | Description                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Distribute 1771 analog modules across multiple chassis.                                                                           | To reduce the number of block transfers that one 1771-ACN or 1771-ASB module manages, distribute 1771 analog modules across multiple chassis.                                                                                                                                                                          |
| Isolate different 1771 chassis on different networks.                                                                             | When you isolate different chassis onto different networks, it diversifies the communication so that no single network or communication module has to deal with all communication.                                                                                                                                     |
| Increase ControlNet unscheduled bandwidth.                                                                                        | If you communicate over a ControlNet network, increase the amount of ControlNet unscheduled bandwidth to permit additional time on the network for data exchange. See Compare Scheduled and Unscheduled ControlNet Communication on page 112 for more information about unscheduled bandwidth on a ControlNet network. |
| Increase the system overhead timeslice percentage on ControlLogix® 5570 or earlier and CompactLogix® 5370 or earlier controllers. | Increase the system overhead timeslice to allocate more CPU time to communication processing from the continuous task.                                                                                                                                                                                                 |
| Interlock block transfer read and write messages to the same module.                                                              | Programmatically interlock block transfer read and write messages to the same module so that both operations cannot be active simultaneously.                                                                                                                                                                          |
| Use the 1756-RIO module for systems with a high number of block transfer modules.                                                 | The 1756-RIO module provides connectivity from a ControlLogix chassis to 1771 I/O and other modules that are connected via remote I/O. The 1756-RIO module offloads the burden of performing block transfers from the controller and increases the number of block transfer operations that can be performed.          |

## Map Tags

<!-- image -->

A Logix 5000 controller stores tag names on the controller so that other devices can read or write data without having to know physical memory locations. Many products only understand PLC/SLC data tables, so the Logix 5000 controller offers a PLC/SLC mapping function that lets you map Logix tag names to memory locations.

- You only have to map the file numbers that are used in messages; the other file numbers do not need to be mapped.
- The mapping table is loaded into the controller and is used whenever a logical address accesses data.
- You can only access controller-scoped tags (global data).

Follow these guidelines when you map tags.

- Do not use file numbers 0, 1, and 2. These files are reserved for Output, Input, and Status files in a PLC-5 processor.
- Use PLC-5 mapping only for tag arrays of data type INT, DINT, or REAL. Attempting to map elements of system structures can produce undesirable effects.
- Use these file types and identifiers.

| For this Logix 5000 array type   | Use this PLC file identifier   |
|----------------------------------|--------------------------------|
| INT array                        | N or B                         |
| DINT array                       | L                              |
| REAL array                       | F                              |

## Alarms

The following options are available for alarms.

| Alarm Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FactoryTalk® Alarms and Events      | The FactoryTalk® Alarms and Events system integrates alarming between FactoryTalk View SE applications and the controllers by embedding an alarming engine in the controllers. • Uniform, micro-second accurate, time stamps determined at the alarm source • Server-client model so all clients get the updates simultaneously • Single connection to controller • Combines all alarms in the system into one uniform view • Supports ControlLogix®, CompactLogix®, SLC™, PLC-5®, and non-Rockwell Automation controller For more information, see FactoryTalk Alarms and Events Configuration Guide, FTAE-RM001 . |
| Controller tag-based alarms         | Tag-based alarms monitor a tag value to determine the alarm condition. Tag-based alarms are not part of the logic program and do not increase the scan time for a project. • Alarms defined on tags with periodic evaluation • Standards-based design • Leverages existing FactoryTalk Alarms and Events infrastructure Only 5380, 5580, and 5590 controllers support tag-based alarms.                                                                                                                                                                                                                             |
| Controller instruction-based alarms | Instruction-based alarms are generated and maintained by using an instruction in a Logix controller. Two Logix based alarm instructions that are available in relay ladder, structured text, and function block diagram. • The Digital Alarm (ALMD) instruction detects alarms that are based on Boolean (true/false) conditions. • The Analog Alarm (ALMA) instruction detects alarms that are based on the level or rate of change of analog values. Alarm instructions and their specific data types consume a larger portion of controller memory and scan time than tag-based alarms. • Alarms are detected at the same time logic is executed • Alarms events are buffered in controller memory • Alarms events are pushed to the HMI only on state changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Guidelines for Tag-Based Alarms

Tag-based alarms are useful when you want to maximize controller scan time and when you want to integrate alarms with legacy or third-party devices.

| Guideline                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| An alarm definition is associated with an Add-On Instruction (AOI) or a defined data type. | When a tag is created using a data type or an AOI that has alarm definitions, alarms are created automatically based on the alarm definitions. You can create an alarm definition for the following components: • Tag or parameter of an AOI. • Member of a user-defined data type (UDT) • Member of a system-defined data type • Member of a module-defined data type When a tag uses a data type that has alarm definitions that are associated with it, alarm conditions are automatically added for the tag based on its alarm definitions. When an AOI is based on an AOI definition, alarm conditions are automatically added for the AOI instance based on the alarm definitions that are associated with the AOI definition. |
| Use the keyword THIS to create modular logic to access alarm attributes                    | When the logic executes, the controller replaces THIS with the name of a program, controller, or Add-On Instruction. The keyword THIS lets you create a logic module that can be inserted in any project on any controller and still execute correctly. Use:THIS to represent a controller name, \THIS to represent a program name, and THIS to represent the name of an Add-On Instruction.                                                                                                                                                                                                                                                                                                                                         |
| Access individual alarm attributes                                                         | Use tag-based alarm attributes as operands in instructions to access tag-based alarm attributes or attributes from a set of alarms. For example, the alarm set for a controller, program, or for instances of an Add-On Instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Access alarm set attributes                                                                | Use alarm set attributes as operands in instructions to access the attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Access individual alarm attributes in Add-On Instruction definitions                       | Use individual alarm attributes as operands in Add-On Instruction (AOI) definitions to access the attributes of alarms that are associated with local tags, input parameters, or output parameters within the same AOI instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Access attributes from Add-On Instruction alarm sets                                       | The alarms contained in an Add-On Instruction (AOI) definition, a structured tag of an AOI definition, or an array tag of an AOI definition can be referenced as an alarm set. Use these alarm set attributes as operands in logic. When you reference an attribute from an individual alarm, you insert the owner of the alarm in the operand syntax. Similarly, when you reference an attribute from an AOI alarm set, you insert the alarm set container (the AOI definition, AOI structured tag, or AOI array tag) in the operand syntax.                                                                                                                                                                                        |

<!-- image -->

## Access Tag-based Alarms

Instructions can access the members of the following tag-based alarms:

- Alarm conditions that are associated with controller tags.
- Alarm conditions that are associated with local scalar tags, input parameters, output parameters, or public parameters within the same program.
- Alarm conditions that are associated with input, output, or public parameters of other programs.
- Alarm definitions that are associated with local tags, input parameters, or output parameters of an Add-On Instruction.
- Alarm definitions that are associated with local tags, input parameters, or output parameters of nested Add-On Instructions.

Instructions can access the following alarm sets or members of alarm sets:

- Alarm sets that are associated with the controller or with a program.
- Alarm sets that are associated with controller tags.
- Alarm sets that are associated with local tags, input parameters, output parameters, or public parameters within the same program.
- Alarm sets that are associated with local tags, input parameters, output parameters, or public parameters of other programs.
- Alarm sets that are associated with input, output, or public parameters in other programs.
- Alarm sets that are associated with local tags, input parameters, or output parameters of an Add-On Instruction.
- An alarm condition or an alarm set of an input, output, or public parameter in another program.
- Alarm sets that are associated with local tags, input parameters, or output parameters of nested Add-On Instructions.

Instruction cannot access the members of the following tag-based alarms:

- Alarm conditions that are associated with local tags in other programs.
- Alarm definitions that are associated with the parent Add-On Instruction.
- Alarm definitions that are associated with tags or parameters of the parent Add-On Instruction.

Instruction cannot access the members of the following alarm sets:

- Alarm sets that are associated with local tags in other programs.
- Alarm sets that are associated with the parent Add-On Instruction.
- Alarm sets that are associated with tags or parameters of the parent Add-On Instruction.

Instructions cannot access the following alarm attributes:

- Evaluation period, alarm condition types, and expressions.
- Time-related attributes that have LINT data types.
- Attributes that have STRING data types.
- Reference type attributes, such as associate tags, target tags, and input tags.

## Guidelines for Instruction-based Alarms

Instruction-based alarms are useful when you want timestamps on alarm or you want to integrate alarms without modifying the HMI displays.

| Guideline                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estimate increased controller memory use for each alarm.                                                                                                         | The alarm instructions use new alarm data types that contain state information and time stamps for each alarm. Estimate this memory used in the controller: • 2 KB per FactoryTalk Alarms and Events subscriber that receives alarms from the controller • There is a maximum of 16 subscribers per controller. Most applications only require one subscriber to a controller to provide data to many FactoryTalk View SE clients. • 2.2 KB per alarm (typical), depends on use of associated tags                                                                                                                                                                                                                                                                                                                                                                             |
| Alarm instructions increase total controller scan time.                                                                                                          | The ALMD instructions and ALMA instructions affect total scan time. See Logix 5000 Controllers Instruction Execution Time and Memory Use Reference Manual, publication 1756-RM087 for execution times for your controller firmware. An alarm state change is any event that changes the condition of the alarm, such as acknowledgment or suppression of the alarm. Creating dependencies on related alarms to minimize the potential for many alarms to change state simultaneously (alarm bursts). Large alarm bursts can have a significant impact on application code scan time. IMPORTANT: In redundancy systems, consider scan time impact due to crossloading alarm tag data. For more information, see: • ControlLogix 5580 Redundant Controller User Manual, publication 1756-UM015 • ControlLogix 5590 High Availability Systems User Manual, publication 1756-UM901 |
| You can edit or add an alarm instruction online.                                                                                                                 | Online edits of new and existing alarms are automatically sent to the subscribers. You do not have to re subscribe to receive the updated information. Online changes automatically propagate from the controller alarm structure to the rest of the architecture.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| In relay ladder, how you define the alarm values on the instruction determines whether you can access those values programmatically through the alarm structure. | When you create an alarm instruction, you also create an alarm data type for that alarm. For example, MyDigitalAlarm of data type DigitalAlarm. In relay ladder, the following values are shown on the instruction: • ProgAck • ProgReset • ProgDisable • ProgEnable If you enter a value or assign a tag to these faceplate parameters (such as AckSection1All), the value or tag value is automatically written to the alarm structure each time the instruction is scanned. If you want to programmatically access the alarm structure, you must assign the structure tag to the faceplate. For example, to use MyAnalogAlarm.ProgAck in logic, assign the tag MyAnalogAlarm.ProgAck on the faceplate to the ProgAck parameter.                                                                                                                                             |
| Test alarm behavior from within the Logix Designer application.                                                                                                  | On the Status tab of the alarm dialog, monitor the alarm condition, acknowledge an alarm, disable an alarm, suppress an alarm, or reset an alarm. Use the dialog selections to see how an alarm behaves, without needing an operational HMI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Reduce mistakes by making sure that alarms are noticed.                                                                                                          | Shelving an alarm removes the alarm from the operator view for a period of time. It is like suppressing an alarm, except that shelving is time-limited. If an alarm is acknowledged while it is shelved, it remains acknowledged even if it becomes active again. It becomes unacknowledged when the shelved duration ends provided the alarm is still active at that moment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Increase productivity by eliminating nuisance alarms.                                                                                                            | Set a duration (ms) on the ALMA instruction to specify how long an alarm condition must exist before being reported. Apply the duration to individual, analog alarm levels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| High availability of alarm data helps reduce material losses.                                                                                                    | Previous to revision 31, the alarm log in the controller stores the last 10,000 alarm state transitions in a circular log. This replaces the alarm buffer in controllers with firmware earlier than revision 21.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Configure Logix-based Alarm Instructions

| Option          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message string  | The message string (maximum of 255 characters, including embedded text) contains the information to display to the operator regarding the alarm. Besides entering text, you can also embed variable information. In the alarm message editor, select the variable that you want and add it anywhere in the message string. You cannot programmatically access the alarm message string from the alarm tag. To change the alarm message based on specific events, configure one of the associated tags as a string data type and embed that associated tag in the message. You can maintain alarm messages in multiple languages. Either enter the different languages in the associated language versions of the Logix Designer application or in an import/export (.CSV or .TXT) file. |
| Associated tags | You can select as many as four additional tags from the controller project to associate with the alarm. These tags are sent with an alarm message to the alarm server. Associated tags can be BOOL, INT, SINT, DINT, REAL, or string data types. For example, a digital alarm for a pressure relief valve can also include information such as pump speed and system pressure, and tank temperature. Optionally, embed the associated tags into the message text string.                                                                                                                                                                                                                                                                                                                |
| Severity        | Use the configurable severity range from 1…1000 to rank the importance of an alarm. A severity of 1 is for low-priority alarms; a severity of 1000 is for an emergency condition. You can configure how the FactoryTalk ranges are presented to the operator. The operator can also filter on alarm levels. For example, a maintenance engineer can filter to see only those alarms at severity 128.                                                                                                                                                                                                                                                                                                                                                                                    |
| Alarm class     | Use the alarm class to group related alarms. Specify the alarm class the same for each alarm you want in the same class. The alarm class is case-sensitive. For example, specify class Control Loop to group all alarms for PID loops. You can then display and filter alarms at the HMI based on the class. For example, an operator can display all tank alarms or all PID loop alarms. The alarm class does not replace subscription to specific alarms. The FactoryTalk View SE Alarm object graphics have configuration options to determine which controller alarms an operator sees.                                                                                                                                                                                             |
| View command    | Execute a command on the operator station when requested by an operator for a specific alarm. This lets an operator execute any standard FactoryTalk View command, such as call specific faceplates and displays, execute macros, access help files, and launch external applications. When the alarm condition occurs and is displayed to the operator, a button on the summary and banner displays lets the operator run an associated view command.                                                                                                                                                                                                                                                                                                                                  |
| Defaults        | The Parameters tab of the alarm instruction properties lets you define values for instruction parameters. You can return the parameters to factory defaults and you can define your own set of instruction defaults. The instruction defaults you assign are defaults for only that instance of the instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Automatic Diagnostics

Automatic Diagnostics provide device diagnostics to HMIs and other clients, with zero programming. You need:

- ControlLogix 5590 with firmware revision 38 or later
- ControlLogix 5580, GuardLogix® 5580, CompactLogix® 5380, Compact GuardLogix 5380, or CompactLogix 5480 controller with firmware revision 33 or later.
- FactoryTalk View SE version 12 or later to add the Automatic Diagnostic object to FactoryTalk View displays. See the FactoryTalk View Site Edition User's Guide, publication VIEWSE-UM006 .
- FactoryTalk Alarms and Events version 6.20 or later to subscribe to the diagnostic messages created in the controller. See the FactoryTalk Alarms and Events System Configuration Guide, publication FTAE-RM001 .

The diagnostics include device description conditions and state events. Diagnostics based on the device definition (such as fault or open wire) are sent to a compatible Rockwell Automation HMI device or software, and displayed on the Automatic Diagnostic Event Summary object.

<!-- image -->

Automatic Diagnostics is enabled by default with firmware revision 33.00 or later. You can disable and enable the whole feature while online or offline from the Controller Properties dialog box. You can also disable Automatic Diagnostics for a specific device in the device's configuration.

When Automatic Diagnostics is enabled, there is little impact to device and network performance.

## Notes:

## Linx-based Software Use of Controller Memory

## HMI Implementation Options

| Method                    | Benefits                                                                                                                                                                                                                                                                                                  | Considerations                                                                                                                                                                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single HMI                | • All HMI/EOI support this method • Limited number of controller connections • No server to configure and manage • Local control and monitoring                                                                                                                                                           | • Single point of failure for visualization • Only one person can monitor one display at a time                                                                                                                                                  |
| Multiple, Independent HMI | • All HMI/EOI support this method • The same HMI displays can be viewed at multiple stations • Multiple people can monitor different parts of system simultaneously • Each HMI gets its own data • No central server to configure and manage • Local control and monitoring                               | • More controller connections are required • Additional burden on controller to service all communication (controller resource impact) • No sharing of data except through the controller • Adding additional HMIs has larger increase on system |
| Client/Server HMI         | • The same HMI displays can be viewed at multiple stations • Server provides data to multiple clients • Fewer controller connections required • Impact on system is smaller than with multiple HMIs • Administer application at the server, not individually at the clients or multiple, independent HMIs | • Server is a point of failure for all HMIs, unless you implement redundancy • Little communication overhead savings if each client wants different data • Networking knowledge that is required                                                 |

Most third-party HMIs are limited to direct communication similar to the multiple HMI method.

<!-- image -->

## Optimize an Application for Use with HMI

Rockwell Automation offers these HMI (human machine interface) platforms.

| Platform                   | Description                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                            | PanelView™ 5000 terminal Dedicated, machine-level HMI running Studio 5000 View Designer® software                                                                                                                                                                                                                                                                      |
| PanelView Plus terminal    | Dedicated, machine-level HMI running FactoryTalk® View Machine Edition software                                                                                                                                                                                                                                                                                        |
| FactoryTalk® View software | Product family that consists of: • FactoryTalk View ME (Machine Edition) software for an open, machine-level HMI; also runs on PanelView Plus terminals • FactoryTalk View Site Edition Station software for a single-workstation, supervisory-level HMI • FactoryTalk View Site Edition distributed software for a multi-server, multi-client, supervisory-level HMI" |

Software products that provide plant-floor device connectivity for HMI applications include:

- RSLinx® Classic software
- FactoryTalk Linx software (formerly RSLinx Enterprise)

The amount of memory that Linx-based software needs depends on the type of data Linxbased software reads. These equations provide a memory estimate.

| IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   | IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   | IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   | IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   | IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   | IMPORTANT  This topic does not apply to 5380, 5480, 5580, or 5590 controllers.   |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Linx-based software overhead (per connection)                                    | _____ * 1345 = ___ bytes (four connections by default)                           |                                                                                  |                                                                                  |                                                                                  |                                                                                  |
| Individual tags _____ * 45 = ___ bytes                                           |                                                                                  |                                                                                  |                                                                                  |                                                                                  |                                                                                  |
| Arrays / structures _____ * 7 = ___ bytes                                        |                                                                                  |                                                                                  |                                                                                  |                                                                                  |                                                                                  |
|                                                                                  | Total = ___ bytes                                                                |                                                                                  |                                                                                  |                                                                                  |                                                                                  |

You can consolidate tags into an array or a structure to reduce the communication overhead and the number of connections that are used to obtain the data.

## Guidelines for FactoryTalk View Software

## How a Data Server Communicates with the Controllers

For the latest information on guidelines for FactoryTalk View Site Edition Software, see the Knowledgebase Technote FactoryTalk View SE Distributed System Design Considerations .

Linx-based software acts as a data server to optimize communication to HMI applications. Linx-based software groups data items into one network packet to reduce:

- The number of messages that are sent over the network.
- The number of messages a controller processes.
1. When Linx-based software first connects to a controller, it queries the tag database and uploads definitions for all controller-scoped tags. If there are multi-layer, user-defined structures that are controller-scoped, Linx-based software just queries the upper layer.
2. When the HMI client requests data, Linx-based software queries the definitions for program-scoped tags and the lower layers of multi-layer user-defined structures.
3. Linx-based software receives requests for data items from local or remote HMI/EOI clients and combines multiple requests in optimized packets. Each data item is a simple Logix tag, array, or user-defined structure. Each optimized packet can be as large as 480 bytes of data and can contain one or more data items.
4. The controller allocates unused system memory to create an optimization buffer to contain the requested data items.
- One optimization buffer can contain as much data as can fit into one 480-byte packet (optimization is limited to 480 bytes).
- If you use the Logix Designer application to monitor controller RAM, you can see used memory increase. (Note that this does not apply to 5380, 5480, 5580, or 5590 controllers.)
- The controller creates an optimization buffer for each Linx-based optimization packet in the scan.

<!-- image -->

## Compare RSLinx Classic and FactoryTalk Linx Software

The Logix Designer application use of RSLinx Classic and FactoryTalk Linx software is as follows:

- Versions 31 and 32 - RSLinx Classic software is the default but FactoryTalk Linx software is installed too during the Logix Designer software installation. You can configure the Logix Designer software to use FactoryTalk Linx software instead.
- Versions 33…35 - FactoryTalk Linx software is the default but RSLinx Classic software is installed too during the Logix Designer software installation. You can configure the Logix Designer software to use RSLinx Classic software instead.
- Versions 36 and 37 - FactoryTalk Linx software is the default. RSLinx Classic is no longer installed during the Logix Designer software installation.

You can install RSLinx Classic software separately and configure your Logix Designer software to use it.

- Version 38 or later - FactoryTalk Linx software is the only option.

| Comparison                        | RSLinx Classic Software                                                                                                                                                                                                              | FactoryTalk Linx Software(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Supported platforms               | Microsoft Windows® operating systems. For the latest information regarding software platform support, see the Product Compatibility and Download Center: https://www.rockwellautomation.com/global/support/pcdc.page                 | Microsoft Windows® operating systems. For the latest information regarding software platform support, see the Product Compatibility and Download Center: https://www.rockwellautomation.com/global/support/pcdc.page                                                                                                                                                                                                                                                                                                               |
| Data server                       | OPC data server Preferred data server for PLC/SLC platforms and applications that require complex network routings Maximum 10 clients per data server                                                                                | Factory Talk Live data server Preferred data server for Logix 5000® platforms Maximum 20 clients per data server                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                                      | PLC/SLC systems Maximum 20 controllers per data server via an Ethernet network Maximum 20 controllers per data server via an Ethernet network                                                                                                                                                                                                                                                                                                                                                                                      |
| Logix 5000 systems                | Maximum: • 10 controllers per data server via an Ethernet network • 10,000 active (on-scan) tags per data server • Three RSLinx data servers per controller                                                                          | Maximum: • 20 controllers per data server via an Ethernet network • 20,000 active (on-scan) tags per data server • Three FactoryTalk Linx data servers per controller                                                                                                                                                                                                                                                                                                                                                              |
| User interface and event logs Yes |                                                                                                                                                                                                                                      | • Available user interfaces are FactoryTalk Studio software and FactoryTalk Administration Console software • Event logs are available with FactoryTalk Diagnostics software                                                                                                                                                                                                                                                                                                                                                       |
| Benefits                          | • Supports topic switching with redundant ControlLogix® system • Supports user-defined tag optimization • RSLinx Gateway software consolidates multiple HMI requests to reduce network traffic • Works with an integrated OPC server | • Automatically handles Logix tag changes • FactoryTalk Live Data software consolidates multiple HMI requests to reduce network traffic                                                                                                                                                                                                                                                                                                                                                                                            |
| Considerations                    | • Requires HMI to be restarted if a Logix 5000 controller is reloaded with changes to tags on scan • Default is four connections for a read and one connection for a write                                                           | • Supports redundant shortcut paths to primary and secondary ControlLogix redundancy pairs. For more information, see: – ControlLogix 5580 Redundant Controller User Manual, publication 1756-UM015 . – ControlLogix 5590 High Availability Systems User Manual, publication 1756-UM901 – High Availability Systems Reference Manual, publication HIGHAV-RM002 • Optimization is limited to array tags • FactoryTalk Gateway software provides OPC support • Default is four connections for a read and one connection for a write |

(1) With version 6.00, RSLinx Enterprise is known as FactoryTalk Linx.

## Guidelines for Linx-based Software

| Guideline                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use Linx-based software as the data server for multiple HMIs. | For multiple HMI stations: • Leverage remote OPC (RSLinx Classic software) or FactoryTalk software (FactoryTalk Linx software) for data collection. • Only the RSLinx data server is expected to have an active topic. • Do not configure or use topics on the HMI stations. • Linx-based software does not need to be on the HMI stations.                                                                                                                                                                                                                                                                                                                                                                              |
| Do not use too many RSLinx stations.                          | The performance of tag collection decreases as the more RSLinx stations collect data from the same controller. Use an RSLinx Gateway station and have the other data collection stations use remote OPC for data collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Account for delay time when adding/removing scanned tags.     | When switching from one HMI display to another, it takes time to put items in the controller on scan and take items off scan. Part of this time delay is because the controller allocates system memory for the optimization buffer. To minimize this delay, when switching between HMI displays, put the items in the HMI displays on scan and leave them on scan. For example, you can create a data log to keep the items on scan. Then when switching between HMI displays, data collection continues without interruption. FactoryTalk Linx and FactoryTalk View Site Edition software account for this time delay. When HMI displays change, these applications deactivate tags rather than remove them from scan. |

## Guidelines to Configure Controller Tags

| Guideline                                     | Description                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use INT data types with third-party products. | Most third-party operator interface products do not support DINT (32-bit) data types. However, there are additional performance and memory-use considerations when you use INT data types. FactoryTalk View software supports native Logix 5000 data types (including BOOL, SINT, INT, DINT, and REAL), structures, and arrays.                       |
| Group-related data in arrays.                 | Most third-party operator interface products do not support user-defined structures. Arrays also make sure that data is in contiguous memory, which optimizes data transfer between the controller and Linx-based software or other operator interfaces. Arrays of tags transfer more quickly and take up less memory than groups of individual tags. |
| Use Linx-based OPC services.                  | Use Linx-based OPC services to bundle multiple tag requests into one message to reduce communication overhead. OPC provides better optimization than DDE.                                                                                                                                                                                             |

## Reference Controller Data from FactoryTalk View Software

This table shows how to reference data in a FactoryTalk View tag address.

| Logix 5000 Array Data Type Description   |                                                                      | PLC File Identifier   | FactoryTalk View Tag Data Type   |
|------------------------------------------|----------------------------------------------------------------------|-----------------------|----------------------------------|
| BOOL                                     | Value of 0, 1, or -1                                                 | B                     | Digital                          |
| SINT                                     | 8-bit integer                                                        | A                     | Byte                             |
| INT                                      | 16-bit integer                                                       | N                     | Integer                          |
| DINT                                     | 32-bit integer                                                       | L                     | Long Integer                     |
| LINT                                     | 64-bit integer value to store date and time values No PLC identifier |                       | Not supported                    |
| REAL                                     | Floating point                                                       | F                     | Floating Point                   |

When addressing a Logix 5000 string tag, use the address syntax [OPC\_Topic]StringTag.Data[0],SC82 to address a SINT array. The string data is stored in the SINT array .Data of the string tag, and you address the first element of this array (.Data[0]). The maximum number of characters in a STRING tag is 82. If you need more characters, then create your own user-defined structure to hold the characters.

To write data into a Logix 5000 string tag from an HMI or external source, set the L.EN field to indicate the number of characters that are in the string. The Logix Designer application and the controller use the .LEN value to determine how many characters are present.

## Guidelines for Equipment Phases

| Guideline                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use a separate phase for each activity of the equipment. | Each phase is a specific activity that the equipment performs. • Use one phase for standalone machines. • Make sure that each phase does an independent activity. • Keep the total number of phases and programs in a project within the limit of programs for the controller. • List the equipment that goes with each phase.                                                                                                                                                                                                                                                                                                                                               |
| Complete one state model for each phase.                 | Each phase runs its own set of states. A state model divides the operating cycle of the equipment into a series of states. • Decide which state to use for the initial state after power-up. • Start with the initial state and work through the model. • Use only the states that you need; skip those states that do not apply. • Use subroutines for producing and standby states. The state model of an equipment phase is similar to the S88 state model. U.S. standard ISA S88.01-1995 and its IEC equivalent IEC 61512-1-1998 is commonly referred to as S88. It is a set of models, terms, and good practices for the design and operation of manufacturing systems. |
| Separate phase code from equipment code.                 | One advantage of a phase is that it lets you separate the procedures (recipes) for how to make the product from the control of the equipment that makes the product. This makes it easier to execute different procedures for different products by using the same equipment.                                                                                                                                                                                                                                                                                                                                                                                                |
| Separate normal execution from exceptions.               | A state model makes it much easier to separate the normal execution of your equipment from any exceptions (faults, failures, off-normal conditions). • Use a prestate routine to watch for faults. • A prestate routine is not a phase state routine. Create a routine like you do for any program and assign it as the prestate routine for the equipment phase program. • Use a state bit to limit code to a specific state. • The Logix Designer application automatically makes a tag for each phase. The phase tag has bits that identify the state of the phase. For example, My_Phase.Running.                                                                        |
| Use Equipment Phases in redundant systems.               | PhaseManager has been tested for compatibility with ControlLogix® redundancy systems. See the ControlLogix Enhanced Redundancy System, firmware revision 16.81, Release Notes, publication 1756-RN650, for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Develop Equipment Phases

The PhaseManager™ option of the Studio 5000 Logix Designer® software gives you a state model for your equipment. It includes the following components:

- Phase to run the state model
- Equipment phase instructions for programming the phase
- PHASE data type

<!-- image -->

## Equipment Phase Instructions

The equipment phase instructions are available in relay ladder and structured text programming languages. You can use them in relay ladder routines, structured text routines, and SFC actions.

| If you want to:                                                                                                                                                                                               | Use this instruction:                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Signal a phase that the state routine is complete so go to the next state.                                                                                                                                    | Phase State Complete (PSC)              |
| Change the state or substate of a phase.                                                                                                                                                                      | Equipment Phase Command (PCMD)          |
| Signal a failure for a phase.                                                                                                                                                                                 | Equipment Phase Failure (PFL)           |
| Clear the failure code of a phase.                                                                                                                                                                            | Equipment Phase Clear Failure (PCLF)    |
| Initiate communication with FactoryTalk® Batch software.                                                                                                                                                      | Equipment Phase External Request (PXRQ) |
| Clear the NewInputParameters bit of a phase.                                                                                                                                                                  | Equipment Phase New Parameters (PRNP)   |
| Create breakpoints within the logic of a phase.                                                                                                                                                               | Equipment Phase Paused (PPD)            |
| Take ownership of a phase to either: • Prevent another program or FactoryTalk Batch software from commanding a phase. • Make sure another program or FactoryTalk Batch software does not already own a phase. | Attach to Equipment Phase (PATT)        |
| Relinquish ownership of a phase.                                                                                                                                                                              | Detach from Equipment Phase (PDET)      |
| Override a command.                                                                                                                                                                                           | Equipment Phase Override (POVR)         |

For more information, see the PhaseManager User Manual, publication LOGIX-UM001 .

## Guidelines to Manage Controller Firmware

| Guideline                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maintain software versions and firmware revisions at the same major revision levels. | At release, a specific version of software supports the features and functions in a specific revision of firmware. To use a specific revision of firmware, you must have the corresponding software version. This combination of software and firmware is considered to be compatible. A revision number consists of a major and minor revision number in this format xx.yyy.                                                       |
| Maintain software versions and firmware revisions at the same major revision levels. | xx  Major revision Updated every release there is a functional change.                                                                                                                                                                                                                                                                                                                                                              |
| Maintain software versions and firmware revisions at the same major revision levels. | yyy  Minor revision Updated anytime there is a change that does not affect function or interface.                                                                                                                                                                                                                                                                                                                                   |
| Use digitally signed firmware to maintain firmware integrity.                        | Controllers support digitally signed, and encrypted for 5380, 5580 and 5590 controllers, firmware for additional security.                                                                                                                                                                                                                                                                                                          |
| Document firmware revisions.                                                         | Include software version and firmware revision information in electrical drawings and other project documentation.                                                                                                                                                                                                                                                                                                                  |
| Read the associated release notes.                                                   | Always read the release notes that accompany new software versions and firmware revisions before you install them. The release notes help you to understand what has improved and changed, and also help you determine whether you must modify your application because of the changes. In most cases, your application runs normally following an update.                                                                          |
| Configure modules so that the controller automatically updates I/O firmware.         | Controller firmware, revision 16, includes a Firmware Supervisor feature that lets controllers automatically update devices. To use the Firmware Supervisor: • You can update Local and remote modules while in Program or Run modes, as long as their electronic keying configurations are set to Exact Match and the ControlFLASH Software supports the modules. • Firmware kits reside on the removable media in the controller. |
| Control that users have access to change firmware revisions.                         | ControlFLASH software, version 8.0 and later, is integrated with FactoryTalk® Security software so you can establish update or no update privileges for users.                                                                                                                                                                                                                                                                      |
| Use the ControlFLASH kit manager to update only the firmware you need or have.       | With ControlFLASH software, version 8.0 and later, you can: • View available firmware kits before updating a device. • Import and export kits to create custom kits. • Delete kits as single devices or as groups by catalog number and device type. • Support third-party applications to push/pull kits as needed.                                                                                                                |

## Manage Firmware

The controllers, I/O modules, and other devices use firmware that you can update on your own. You choose the firmware revision level and decide when to update the firmware.

<!-- image -->

There are multiple tools that you can use to update firmware. We recommend that, if your application is compatible with ControlFLASH™ Plus, you use that tool. Among other things, ControlFLASH PLUS let you selectively flash multiple devices at once instead of updating firmware one device at a time.

<!-- image -->

## Compare Firmware Options

Controllers ship with basic firmware that supports only updating the controller firmware to the required revision. You must update the firmware to a revision that is compatible with your version of the Studio 5000 Logix Designer® application.

| ControlFLASH and ControlFLASH Plus Software AutoFlash Function                                                                                                                                |                                                                                                                                                                                                                                                                        | Controller-based Firmware Supervisor                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Standalone tool. Manually launch from desktop icon or program list. ControlFLASH Plus™ integrates with the Product Compatibility and Download Center and with FactoryTalk® Security software. | Integrated with the Logix Designer application. The software automatically checks the controller, motion module, and SERCOS drive firmware during a project download. If the firmware is out of date or incompatible, the software prompts you to update the firmware. | Integrated on the controller removable media and run by the controller without user intervention. Controllers automatically update modules on keying mismatch situations.                                                                        |
| Supports controllers, communication modules, I/O modules, motion modules, and newer SERCOS drives, and many other devices. ControlFLASH Plus also supports component products.                | Supports the same devices as the ControlFLASH™ Software.                                                                                                                                                                                                               | Supports local and remote devices that: • Are in the I/O tree and configured as Exact Match. • Support firmware updates via the ControlFLASH Software. • The hardware revision supports the firmware that is stored for that Exact Match device. |
| Supports valid CIP™ path to the device to update, such as serial, DeviceNet®, ControlNet®, and EtherNet/IP™ connections.                                                                      | Supports valid CIP path to the device to update, such as serial, DeviceNet, ControlNet, and EtherNet/IP connections.                                                                                                                                                   | Supports all communication paths to devices that reside in the controller I/O tree and that also support the ControlFLASH Software. The firmware must already be on removable media in the controller.                                           |

For more information, see these publications:

- ControlFLASH Plus Quick Start Guide, publication CFP-QS001 .
- ControlFLASH Firmware Upgrade Software User Manual, publication 1756-UM105 .

The Firmware Supervisor feature can automatically load firmware when you replace a device in the system.

- OEMs who build multiple machines a month can have the controller update all modules and devices in the system without user intervention.
- Machines with strict regulation can require specific firmware revisions for the devices to maintain certification. The Firmware Supervisor helps make sure that devices are at the correct firmware revision.
- Maintenance personnel replacing failed hardware can install the replacement device and the controller automatically updates the device with the correct firmware revision.

## Description

The Firmware Supervisor works on local I/O modules and distributed modules via EtherNet/IP, SERCOS, and ControlNet networks. On DeviceNet networks, the Firmware Supervisor supports local devices only, such as scanners and linking devices that reside in the I/O tree of the controller project. Because you cannot directly place a remote DeviceNet device in the I/O tree, the Firmware Supervisor does not manage remote DeviceNet devices.

The Firmware Supervisor supports:

- Controllers that support removable media (except for redundant controllers).
- The Firmware Supervisor does not manage the firmware of other standard controllers in the I/O Configuration tree.
- Safety products, including GuardLogix® Safety controllers and 1791ES CompactBlock™ Guard I/O™ EtherNet/IP modules.

The Firmware Supervisor does not manage the firmware of POINT Guard I/O™ modules or 1791DS CompactBlock Guard I/O™ DeviceNet modules.

SERCOS drives that support updates over a SERCOS network:

- 1394 drives, firmware revision 1.85 and later.
- Kinetix® 6000 drives, firmware revision 1.85 and later.
- Ultra™ 3000 drives, firmware revision 1.50 and later.
- 8720MC drives, firmware revision 3.85 and later.

Non-modular, distributed I/O products that sit directly on the network without an adapter. Distributed I/O products that require an adapter, such as POINT I/O™ or FLEX™ I/O modules, are not supported. Instead, the Firmware Supervisor manages the firmware for the adapters.

The Firmware Supervisor does not support PanelView™ Plus terminals, since the terminals do not support the ControlFLASH software.

## Guidelines for the Firmware Supervisor

## Guideline

The Firmware Supervisor can update any Rockwell Automation® device that:

- Can be placed in the I/O Configuration tree
- Has electronic keying that is configured as Exact Match
- Normally can be updated with ControlFLASH software

| Guideline                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| For the Firmware Supervisor to manage firmware for a device, the device must have its electronic keying that is configured for Exact Match. | Other modules can exist in the I/O Configuration that are not configured as Exact Match, but the Firmware Supervisor does not maintain the firmware for those modules. To disable the Firmware Supervisor for a specific device: Change the electronic keying for that device to something besides Exact Match. Disable Firmware Supervisor from either an SSV instruction or the Nonvolatile Memory tab of the controller properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Removable media must be formatted properly. IMPORTANT: This does not apply to microSD™ cards that are used with 5590 controllers.           | If you have a Secure Digital card with 4 GB memory or more, format the card FAT32. If you have a Secure Digital card with less than 4 GB memory, format the card FAT16.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                             | Make sure that the removable media is not locked. The Secure Digital card has a lock feature. The card must be unlocked to write to the card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| For modules that are managed by the Firmware Supervisor, each controller must store the firmware files on removable media.                  | Enable the Firmware Supervisor, from the Nonvolatile Memory tab of the controller properties. Click Load/Store. From the Automatic Firmware Updates dropdown menu, choose Store to copy it to removable media. The computer that runs the Logix Designer application must have: • ControlFLASH Software installed. • The required firmware kits in the ControlFLASH default directory for the modules the Firmware Supervisor is to maintain. The Logix Designer application moves firmware kits from your computer to the removable media in the controller for the Firmware Supervisor to use. • Controller firmware and application logic are managed outside of Firmware Supervisor on the Nonvolatile Memory tab. Firmware Supervisor adds to the ability to store controller firmware and logic on the removable media. If you disable the Firmware Supervisor, you disable the Firmware Supervisor updates and not the controller firmware updates that still occur when the controller image is reloaded. |

Enable or disable the automatic firmware updates by using GSV and SSV instructions.

You can monitor the status of automatic firmware updates.

<!-- image -->

Monitor the status of automatic firmware updates on the Nonvolatile Memory tab on the controller properties. To monitor the status of automatic firmware updates for a specific module, use GSV instructions. This example shows that the Firmware Supervisor encountered the wrong hardware revision for 1756-OB16D module.

GSV

GetSystemValue

Class Name

Instance Narme

Attribute Narme

MODULE

MyOutputCard

FaultCode

Dest

FirmwareSupMocule[0]

278

MOV-

FirmwareSupModule[0]

278

Dest

Storage

2#0000\_0000\_0000\_0000\_...

Not Equel

Source A

Source B

NEQ

FirmwareSupMocule[0]

278

65040

Move

Source

## Access Firmware

The Logix Designer application ships with firmware update kits. Firmware revisions are also available on the Rockwell Automation website.

5. Go to https://www.rockwellautomation.com/global/support/download-center/ overview.page?
6. Under Drivers and Firmware, click Find Drivers and Firmware.

## A

## access

firmware 134 module object 44

access the module object 44

## add-on instruction

first scan initialization 47

guidelines 63

postscan logic 49

prescan 47

## alias tags

creating 91

## applications

HMI 125

## array

guidelines

85

index

guidelines 84

87

indirect addresses 86

tag storage

automatic diagnostics

123

## B

## base tag

guidelines 91

bit tags

88

## block-transfer messages

guidelines 118

## buffer

message storage 116 routine 46

## C

## cache

messages 115

## code reuse

guidelines 53

## communication

Linx-based software data packets 126 module connections 32 MSG instruction 115

## comparison

import/export, add-on instructions 65 program parameters, add-on instructions 59 programming languages 45 scheduled and unscheduled ControlNet 112 subroutines, add-on instructions 64

## configuration

Logix-based alarms 122 tags 90

## connection

communication module 32

## considerations

periodic, event tasks 43 task 42

## consumed tag

event task 81

## continuous

task 41

lowest priority 40

## controller

dual-core 31

Linx-based software

software memory 125

resources 31

-scoped tags 126

tag guidelines 128

## ControlNet network

guidelines 110

scheduled and unscheduled comparison 112

topology 110

## creating

alias tags 91

## D

## data

scope guidelines type guidelines

92

83

date and time data types 13 , 21 , 25

## DeviceNet network

guidelines topology

113

113

diagnostics 123

## dual-core

controller 31

## E

## equipment phases 129

guidelines 129 instructions 130

## EtherNet/IP network

guidelines 109 topology 108

## event

task 41

configuration 43

considerations 43

consumed tag 81

guidelines 43

## execution

project 42

## HMI

## F

## FactoryTalk

software guidelines 126

FactoryTalk Linx software 127

## firmware

access 134

management 131

options 132

supervisor guidelines 132

first scan initialization 47

## G

## guidelines

block-transfer messages 118 controller firmware 131 controller tags 128 ControlNet network 110 DeviceNet network 113 equipment phases 129 EtherNet/IP network 109 FactoryTalk View software 126 firmware supervisor 132

Linx-based software 128

messages 117

## H

optimization 125

## I

indexed routine 46

inline duplication 46

instructions equipment phases 130

## L

## Linx-based software

controller memory estimate 125 guidelines 128 126

network data packet

## logic

routine application code 45

## Logix-based

alarm configuration 122

## manage

firmware updates 131 system overhead 35

map tags 118

## memory

Linx-based software estimation 125

## message

block-transfer guidelines 118

cache 115

guidelines 117 storage buffer

116

## module object 44

path attribute 44

## MSG

communication 115

## N

## network

ControlNet guidelines 110

ControlNet topology 110 DeviceNet guidelines 113 DeviceNet topology 113 EtherNet/IP guidelines 109 EtherNet/IP topology 108 guidelines 107

services 107

unscheduled and scheduled ControlNet 112

unscheduled ControlNet guidelines 111

## O

online addition of module 104

## P

## packet

Linx-based software data 126

path attribute 44

## periodic

task 41

configuration

43

considerations 43

## phases

equipment 129

PhaseManager option 129

## postscan

add-on instruction 49 SFC logic 49

## M

## pre-defined tasks

process controllers 41

## prescan

add-on instruction 47

## priority level

task 40

process controllers 41

## produced and consumed

RPI 80 tag guidelines tags 79

79

## program

considerations 39 languages comparison 45 methods 46 -scoped tags 126

## project

execution 42

## R

## routine

considerations 39 programming logic 45

## RPI

produced and consumed tags 80

RSLinx Classic software 127

RSLinx. See also Linx-based Software

## S

## services

network 107

SFC

logic postscan 49 online editing 51

## storage

message buffer 116

## string data types

guidelines 90

## system overhead

manage timeslice 35 timeslice 34

## table

## tag

## task

considerations 39 , 42 continuous, periodic, event 41 priority level 40 types 40

time and date data types 13 , 21 , 25

## timeslice

manage system overhead 35 system overhead 34

## topology

ControlNet network 110

DeviceNet network 113

EtherNet/IP network 108

## U

## UDT

guidelines 87

unscheduled ControlNet network guidelines 111

## updating

firmware 131

## T

mapping 118

configuration 90 controller-scoped 126 descriptions 93 maps 118 name guidelines 92 produced and consumed 79 program-scoped 126

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

Allen-Bradley, Armor, Compact 5000, CompactBlock, CompactLogix, ControlFLASH, ControlFLASH Plus, ControlLogix, ControlLogix-XT, Data Highway Plus, DH+, expanding human possibility, FactoryTalk, FLEX, GuardLogix, Guard I/O, Logix 5000, MicroLogix, PanelBuilder, PanelView, PhaseManager, PlantPAX, POINT Guard I/O, POINT I/O, PLC-2, PLC-3, PLC-5, Rockwell Automation, RSLinx, RSLogix 5000, RSNetWorx, RSView, SLC, Studio 5000 Logix Designer, and SynchLink are trademarks of Rockwell Automation, Inc

CIP, CIP Sync, ControlNet, DeviceNet, EtherNet/IP are trademarks of ODVA, Inc.

Microsoft and Windows are trademarks of Microsoft Corporation. Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 UNITEDKINGD0M:RockwellAutomationLtd.Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:（44)（1908)838-800