<!-- image -->

<!-- image -->

## ControlLogix Redundancy System

Catalog Numbers 1756-CNB/D/E,

1756-CNBR/D/E, 1756-ENBT,

1756-EWEB, 1756-L55,

1756-L55M12, 1756-L55M13,

1756-L55M14, 1756-L55M16,

1756-L55M22, 1756-L55M23,

1756-L55M24, 1756-L61, 1756-L62,

1756-L63, 1757-SRM

User Manual

## Important User Information

Solid state equipment has operational characteristics differing from those of electromechanical equipment. Safety Guidelines for the Application, Installation and Maintenance of Solid State Controls (publication SGI-1.1 available from your local Rockwell Automation sales office or online at http://literature.rockwellautomation.com) describes some important differences between solid state equipment and hard-wired electromechanical devices. Because of this difference, and also because of the wide variety of uses for solid state equipment, all persons responsible for applying this equipment must satisfy themselves that each intended application of this equipment is acceptable.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

| WARNING      | Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal                                                                                  |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | injury or death, property damage, or economic loss.                                                                                                                                                                         |
| IMPORTANT    | Identifies information that is critical for successful application and understanding of the product.                                                                                                                        |
| ATTENTION    | Identifies information about practices or circumstances that can lead to: personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence |
| SHOCK HAZARD | Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.                                                                                             |
| BURN HAZARD  | Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.                                                                                    |

Allen-Bradley, RSLogix, RSLogix 5000, RSView, RSLinxRSNetworx, DH+, PanelView, PanelViewPlus, Rockwell Automation, TechConnect, and VersaView are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

## Introduction

## Updated Information

This release of this document contains new and updated information. To find new and updated information, look for change bars, as shown next to this paragraph.

The document contains these changes.

| Topic  Page                                                               |
|---------------------------------------------------------------------------|
| Series E information for 1756-CNB and -CNBR modules Throughout manual     |
| Redundant System Firmware Combinations 14                                 |
| Revised Procedure for Setting the Minimum Value for the Watchdog Time 100 |
| Restrictions and Known Anomalies Appendix E                               |
| Update an Online Redundant System 138                                     |
| Store a Project to Nonvolatile Memory While Process Is Running 128        |
| Change CNB Modules from Series D to Series E While Online 129             |

3

## Notes:

## Table of Contents

| Preface                        | Purpose of this Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11       |
|--------------------------------|-----------------------------------------------------------------------------------------|
|                                | Who Should Use this Manual. . . . . . . . . . . . . . . . . . . . . . . . 11            |
|                                | When to Use This Manual . . . . . . . . . . . . . . . . . . . . . . . . . . 11          |
|                                | How to Use this Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |
|                                | Related Documentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12        |
|                                | Chapter 1                                                                               |
| ControlLogix Redundancy System | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 |
| Overview                       | About the Main Parts of a Redundant System . . . . . . . . . . . . 14                   |
|                                | Firmware Combinations That Make Up a Redundant System. 14                               |
|                                | Important Terms in a Redundant System . . . . . . . . . . . . . . . 15                  |
|                                | Primary Chassis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15   |
|                                | Switching from One Controller to Another . . . . . . . . . . . . . . 15                 |
|                                | Network Access Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16      |
|                                | Bump in Outputs During a Switchover. . . . . . . . . . . . . . . . . 16                 |
|                                | Keep the Second Controller Up to Date . . . . . . . . . . . . . . . . 16                |
|                                | Making Online Edits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18      |
|                                | Increasing Scan Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18       |
|                                | Network Addresses During a Switchover . . . . . . . . . . . . . . . 18                  |
|                                | ControlNet Network. . . . . . . . . . . . . . . . . . . . . . . . . . . . 19            |
|                                | EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . . . . . . . . 20            |
|                                | Quick Start Checklists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21     |
|                                | Chapter 2                                                                               |
| Design the System              | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 |
|                                | Laying Out the System. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28       |
|                                | Placement of a Pair of Redundant Chassis . . . . . . . . . . . . . . 30                 |
|                                | If You Need More Than 100 Meters Between Chassis . . . 30                               |
|                                | Placement of the I/O. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31      |
|                                | Placement of Operator Interface Terminals. . . . . . . . . . . . . . 32                 |
|                                | Additional Redundant Components . . . . . . . . . . . . . . . . . . . 33                |
|                                | Redundant ControlNet Media . . . . . . . . . . . . . . . . . . . . . 33                 |
|                                | Redundant Power Supplies. . . . . . . . . . . . . . . . . . . . . . . 34                |
|                                | Checking Connection Requirements. . . . . . . . . . . . . . . . . . . 35                |
|                                | Planning a ControlNet Network . . . . . . . . . . . . . . . . . . . . . . 35            |
|                                | Planning an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . 38              |
|                                | Worksheet for IP Swapping . . . . . . . . . . . . . . . . . . . . . . 39                |
|                                | How an EtherNet/IP Module Handles a Cable Break . . . . 40                              |
|                                | Additional Design Considerations . . . . . . . . . . . . . . . . . . . . 41             |
|                                | Chapter 3                                                                               |
| Install the System             | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 |
|                                | Preliminary Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . 43       |
|                                | Install the Chassis for the Controllers . . . . . . . . . . . . . . . . . . 45          |
|                                | Install Modules in the First Redundant Chassis . . . . . . . . . . . 46                 |
|                                | Install Modules in the Second Redundant Chassis. . . . . . . . . 48                     |

5

|                                 | Install the Remote Chassis or Rails . . . . . . . . . . . . . . . . . . . . 49                                        |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|                                 | Configure EtherNet/IP Modules . . . . . . . . . . . . . . . . . . . . . . 50                                          |
|                                 | Flash the Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                                   |
|                                 | Check the Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                                   |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                                  |
|                                 | Chapter 4                                                                                                             |
| Configure the System Redundancy | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                               |
| Module                          | Open the SRM Configuration Tool . . . . . . . . . . . . . . . . . . . . 53                                            |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                                  |
|                                 | What to Do Next . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                        |
|                                 | Check the Revision of Your SRM Configuration Tool . . . . . . 55                                                      |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                                  |
|                                 | Set the SRM Clock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                                   |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                                  |
|                                 | Test a Switchover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                                  |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                                  |
|                                 | Change Auto-Synchronization . . . . . . . . . . . . . . . . . . . . . . . 61                                          |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                                  |
|                                 | Change Program Control . . . . . . . . . . . . . . . . . . . . . . . . . . . 62                                       |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                                  |
|                                 | Chapter 5                                                                                                             |
| Configure and Program the       | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                               |
| Controller                      | Plan for Online Edits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                                   |
|                                 | Decide if You Want to Keep Test Edits after a Switchover . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 |
|                                 | Original Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                                     |
|                                 | Decide How You Want to Set Aside Unused Memory . . . 67                                                               |
|                                 | Configure a Controller for Redundancy . . . . . . . . . . . . . . . . 68                                              |
|                                 | Configure Communications . . . . . . . . . . . . . . . . . . . . . . . . . 70                                         |
|                                 | Configure Produced Tags . . . . . . . . . . . . . . . . . . . . . . . 70                                              |
|                                 | Configure Message (MSG) Instructions . . . . . . . . . . . . . . 72                                                   |
|                                 | Configure Tags for an HMI. . . . . . . . . . . . . . . . . . . . . . . 73                                             |
|                                 | Estimate the Crossload Time of a Program . . . . . . . . . . . . . . 74                                               |
|                                 | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                                         |
|                                 | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                                  |
|                                 | Minimize Scan Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                     |

Maintain and Troubleshoot the

System

| Maintain Data Integrity During a Switchover . . . . . . . . . . . . 82                 |
|----------------------------------------------------------------------------------------|
| Look for Array Shift Instructions . . . . . . . . . . . . . . . . . . . 84             |
| Look for Scan-Dependent Logic . . . . . . . . . . . . . . . . . . . 84                 |
| Take Preventative Actions . . . . . . . . . . . . . . . . . . . . . . . 85             |
| Determine the Status of Your Redundant System . . . . . . . . . 87                     |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87   |
| Example 1: Ladder Diagram . . . . . . . . . . . . . . . . . . . . . . 87               |
| Example 2: Structured Text. . . . . . . . . . . . . . . . . . . . . . . 87             |
| Check Your Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88           |
| Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . 88          |
| Condition Logic to Run After a Switchover . . . . . . . . . . . . . . 89               |
| Example 1: Ladder Diagram . . . . . . . . . . . . . . . . . . . . . . 89               |
| Example 2: Structured Text. . . . . . . . . . . . . . . . . . . . . . . 90             |
| Send a Message to the SRM . . . . . . . . . . . . . . . . . . . . . . . . . 91         |
| Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92          |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93   |
| Download the Project to the Primary Controller . . . . . . . . . . 95                  |
| Schedule a ControlNet Network. . . . . . . . . . . . . . . . . . . . . . 97            |
| Schedule a New Network. . . . . . . . . . . . . . . . . . . . . . . . 97               |
| Update the Schedule of an Existing Network. . . . . . . . . . 98                       |
| Check the Keepers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99          |
| Save the Project for Each Controller . . . . . . . . . . . . . . . . 99                |
| Set Task Watchdog Times . . . . . . . . . . . . . . . . . . . . . . . . . 100          |
| Chapter 6                                                                              |
| Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 |
| Diagnose a Switchover or Disqualification . . . . . . . . . . . . . 104                |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104    |
| Troubleshoot a Failure to Synchronize . . . . . . . . . . . . . . . . 105              |
| Update a Keeper Signature . . . . . . . . . . . . . . . . . . . . . . . . 107          |
| Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107           |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107    |
| Edit Sessions in Progress . . . . . . . . . . . . . . . . . . . . . . . . . . 108      |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108    |
| Interpret the SRM Event Log . . . . . . . . . . . . . . . . . . . . . . . 109          |
| Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110           |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110    |
| Interpret SRM events . . . . . . . . . . . . . . . . . . . . . . . . . . 113           |
| Export the SRM Event Log . . . . . . . . . . . . . . . . . . . . . . . . . 115         |
| Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115           |
| Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116    |
| Manually Synchronize the Chassis . . . . . . . . . . . . . . . . . . . 118             |
| Optimize Communication . . . . . . . . . . . . . . . . . . . . . . . . . 119           |
| Enter a System Overhead Time Slice. . . . . . . . . . . . . . . 121                    |
| Make All Your Tasks Periodic. . . . . . . . . . . . . . . . . . . . 122                |

|                               | Check the Allocation of Unused Memory . . . . . . . . . . . . . . 123                            |
|-------------------------------|--------------------------------------------------------------------------------------------------|
|                               | Adjust CPU Usage for a CNB Module. . . . . . . . . . . . . . . . . 123                           |
|                               | Use RSLinx Software . . . . . . . . . . . . . . . . . . . . . . . . . . 124                      |
|                               | Four-Character Display. . . . . . . . . . . . . . . . . . . . . . . . . 124                      |
|                               | Send a Message to the CNB Module . . . . . . . . . . . . . . . 126                               |
|                               | Store or Load a Project Using Nonvolatile Memory . . . . . . . 126                               |
|                               | Store a Project to Nonvolatile Memory                                                            |
|                               | While a Process Is Running . . . . . . . . . . . . . . . . . . . . . . . . 128                   |
|                               | Chapter 7                                                                                        |
| Update Modules and Redundant  | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129           |
| Systems                       | Change CNB Modules from Series D to                                                              |
|                               | Series E While Online . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                |
|                               | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                     |
|                               | Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130              |
|                               | Update a Redundant Control System Offline. . . . . . . . . . . . 136                             |
|                               | Update an Online Redundant System . . . . . . . . . . . . . . . . 138                            |
|                               | Redundant System Relationships. . . . . . . . . . . . . . . . . . 139                            |
|                               | Appendix A                                                                                       |
| Set Up EtherNet/IP            | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147           |
| Communication Across Subnets  | Keep an HMI Communicating with the Primary Chassis . . . 148 Install the ControlLogix Redundancy |
|                               | Alias Topic Switcher Software. . . . . . . . . . . . . . . . . . . . 149                         |
|                               | Configure a Driver to Communicate with the Primary and                                           |
|                               | Secondary EtherNet/IP Modules . . . . . . . . . . . . . . . . . . 150                            |
|                               | Create a DDE/OPC Topic for Each Controller . . . . . . . . 151                                   |
|                               | Create an Alias Topic . . . . . . . . . . . . . . . . . . . . . . . . . . 152                    |
|                               | Set Up the Alias Topic Switcher . . . . . . . . . . . . . . . . . . 153                          |
|                               | Address the Alias Topic in the HMI Project . . . . . . . . . . 154                               |
|                               | Keep a Message Going to the Primary Chassis . . . . . . . . . . 154                              |
|                               | Create a Periodic Trigger for the Messages . . . . . . . . . . 155                               |
|                               | Get the Redundancy State of Chassis A . . . . . . . . . . . . 156                                |
|                               | Get the Redundancy State of Chassis B . . . . . . . . . . . . . 157                              |
|                               | Determine Which Chassis is Primary. . . . . . . . . . . . . . . 159                              |
|                               | Send the Message to the Appropriate Controller . . . . . . 160                                   |
|                               | Appendix B                                                                                       |
| Convert an Existing System to | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163           |
| Redundancy                    | Convert Local Modules to Remote Modules . . . . . . . . . . . . 163                              |
|                               | Reconfigure the Local I/O Modules. . . . . . . . . . . . . . . . 164                             |
|                               | Replace Local I/O Tags . . . . . . . . . . . . . . . . . . . . . . . . 164                       |
|                               | Replace Any Aliases to Local I/O Tags . . . . . . . . . . . . . 166                              |

Appendix C

| Attributes of the Redundancy   | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169   |
|--------------------------------|------------------------------------------------------------------------------------------|
| Object                         | Attributes of the Redundancy Object . . . . . . . . . . . . . . . . . 169                |
|                                | Appendix D                                                                               |
| Series B ControlNet Bridge     | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173   |
| Modules                        | Losing Communication while Bridging Via a                                                |
|                                | Series B ControlNet                                                                      |
|                                | Bridge Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173      |
|                                | Communication Stoppage While Using a Series B ControlNet                                 |
|                                | Bridge Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174      |
|                                | Appendix E                                                                               |
| Redundant System Restrictions  | Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177   |
|                                | Redundant System Restrictions. . . . . . . . . . . . . . . . . . . . . . 177             |
|                                | Index                                                                                    |
|                                | Rockwell Automation Support . . . . . . . . . . . . . . . . . . . . . . 186              |
|                                | Installation Assistance . . . . . . . . . . . . . . . . . . . . . . . . . 186            |
|                                | New Product Satisfaction Return. . . . . . . . . . . . . . . . . . 186                   |

## Purpose of this Manual

## Who Should Use this Manual

## When to Use This Manual

## How to Use this Manual

11

This manual guides the design, development, and implementation of a redundancy system for a ControlLogix controller.

This manual is intended for those in these professions who design and develop applications that use ControlLogix controllers:

- Software engineers
- Control engineers
- Application engineers
- Instrumentation technicians

Use this manual throughout the lifecycle of a redundancy system. The lifecycle consists of these stages:

- Design
- Installation
- Configuration
- Programming
- Testing
- Maintenance and troubleshooting

This manual is divided into the basic tasks performed during the design, development, and implementation of a ControlLogix redundancy system.

- Each chapter covers a task.
- Tasks are organized in the sequence you will typically perform them.

## Related Documentation

This table lists ControlLogix products and documentation that may be valuable as in programming an application.

| Catalog Number Title Publication Number   |                                                                                             |
|-------------------------------------------|---------------------------------------------------------------------------------------------|
| 1756-CNB/D and 1756-CNBR/D                | ControlLogix ControlNet Bridge Module Installation Instructions 1756-IN571                  |
| 1756-CNB/D and 1756-CNBR/D                | ControlLogix ControlNet Interface Module Release Notes 1756-RN587                           |
| 1756-CNB/E and 1756-CNBR/E                | ControlLogix ControlNet Bridge Module, Series E Installation Instructions 1756-IN604        |
| 1756-CNB/E and 1756-CNBR/E                | ControlLogix ControlNet Bridge Module, Series E Release Notes 1756-RN627                    |
|                                           | 1756-ENBT/A 1756 10/100Mbps EtherNet/IP Bridge, Twisted Pair Media Release Notes 1756-RN602 |
|                                           | 1756-ENBT 1756-ENBT ControlLogix EtherNet/IP Product Profile 1756-PP004                     |
|                                           | ControlLogix EtherNet/IP Bridge Module Installation Instructions 1756-IN019                 |
|                                           | ControlLogix EtherNet/IP Communication Release Notes 1756-RN591                             |
| 1756-RN604                                | 1756-EWEB 1756-EWEB EtherNet/IP Web Server Module Release Notes                             |
|                                           | EtherNet/IP Web Server Module Installation Instructions 1756-IN588                          |
|                                           | EtherNet/IP Web Server Module User Manual ENET-UM527                                        |
| 1756-L55                                  | ControlLogix Controller and Memory Board Installation Instructions 1756-IN101               |
| 1756-L61                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-L62                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-L63                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M12                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-IN101 1756-M13                       | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M14                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M16                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M22                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M23                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1756-M24                                  | ControlLogix Controller and Memory Board Installation Instructions                          |
| 1757-IN092                                | 1757-SRM/B ProcessLogix/ControlLogix System Redundancy Module Installation Instructions     |

To view or download these publications, go to:

http://literature.rockwellautomation.com

To obtain a hard copy, contact your Rockwell Automation distributor or sales representative.

## Introduction

13

## ControlLogix Redundancy System Overview

This chapter provides an overview of the ControlLogix redundancy system, including commonly used terms. It also answers some common questions about a ControlLogix redundancy system.

| Topic Page                                               |
|----------------------------------------------------------|
| About the Main Parts of a Redundant System 14            |
| Firmware Combinations That Make Up a Redundant System 14 |
| Primary Chassis 15                                       |
| Switching from One Controller to Another 15              |
| Network Access Port 16                                   |
| Bump in Outputs During a Switchover 16                   |
| Keep the Second Controller Up to Date 16                 |
| Making Online Edits 18                                   |
| Increasing Scan Time 18                                  |
| Network Addresses During a Switchover 18                 |
| Quick Start Checklists 21                                |

## About the Main Parts of a Redundant System

The ControlLogix redundancy system uses an identical pair of ControlLogix chassis to keep a machine or process running if a problem occurs with any hardware in one of the chassis.

This diagram illustrates the layout of a simple redundant setup.

## ControlLogix Redundant System

<!-- image -->

## Firmware Combinations That Make Up a Redundant System

43128

These firmware combinations make up revisions 15.56 and 15.57 of the ControlLogix redundancy system.

## ControlLogix Redundancy Firmware Combinations

|                                                                                | Module Catalog Number Series Firmware Revision   |
|--------------------------------------------------------------------------------|--------------------------------------------------|
| ControlLogix5555 controller 1756-L55Mxx                                        | Any 15.57                                        |
| ControlLogix5561 controller 1756-L61 Any 15.56                                 |                                                  |
| ControlLogix5562 controller 1756-L62 Any 15.56                                 |                                                  |
| ControlLogix5563 controller 1756-L63 Any 15.56                                 |                                                  |
| ControlNet bridge module 1756-CNB                                              | D 7.12                                           |
| ControlNet bridge module 1756-CNB                                              | 1756-CNBR E 11.002                               |
| 1756 10/100 Mbps EtherNet/IP Bridge, Twisted Pair Media 1756-ENBT Any 4.3      |                                                  |
| 1756 10/100 Mbps EtherNet/IP Bridge w/ Enhanced Web Services 1756-EWEB Any 4.3 |                                                  |
| Redundancy module 1757-SRM Any 4.3                                             |                                                  |

## Important Terms in a Redundant System

Redundancy requires no additional programming and is transparent to any devices connected over an EtherNet/IP or ControlNet network. Redundancy uses 1757-SRM modules to maintain communication between the pair of redundant chassis.

In a redundant system, these terms describe the relationship between the two redundant chassis.

## Redundancy Terms

| Term Description                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary Controller The controller that is currently controlling the machine or process.                                                                                                                                                                                                            |
| Primary Chassis The chassis that contains the primary controller or controllers.                                                                                                                                                                                                                   |
| Secondary Controller The controller that is standing by to take control of the machine or process. A secondary controller always resides in a different chassis than the primary controller.                                                                                                       |
| Secondary Chassis The chassis that contains the secondary controller or controllers.                                                                                                                                                                                                               |
| Switchover Transfer of control from the primary controller to the secondary controller. After a switchover, the controller that takes control becomes the primary controller. Its partner controller (the controller that was previously the primary controller) becomes the secondary controller. |

## Primary Chassis

## Switching from One Controller to Another

In a pair of redundant chassis, the first chassis turned on becomes the primary chassis. When the secondary chassis receives power, it synchronizes itself with the primary chassis.

When primary chassis components fail, control switches to the secondary controller. A switchover occurs for any of these reasons:

- any of these situations in the primary chassis:
- – loss of power
- – major fault of the controller
- – removal, insertion, or failure of any module in the primary chassis
- – break or disconnection of a ControlNet tap or ethernet cable
- command from the primary controller
- command from RSLinx software

## Network Access Port

## Bump in Outputs During a Switchover

## Keep the Second Controller Up to Date

To connect a device to the network access port (NAP) of a 1756-CNB/D/E or 1756-CNBR/D/E module, use an NAP that is outside of a redundant chassis.

## IMPORTANT

## Use of the Network Access Port (NAP)

Do not connect any device to the network access port (NAP) of a 1756-CNB/D/E or -CNBR/D/E module in a redundant chassis.

- If you connect a device to the NAP of a CNB module in a redundant chassis, a switchover will fail to occur if the CNB module is disconnected from the network. While the CNB module is disconnected from the network, the controller will be unable to control any I/O devices through that CNB module.
- If you connect a workstation to the NAP of a CNB module in a redundant chassis, the workstation will be unable to go online after a switchover.

To connect a device to a ControlNet network via a NAP, use a NAP that is outside of a redundant chassis.

Depending on how you organize your RSLogix 5000 project, outputs may or may not experience a change in state (bump) during a switchover.

- During the switchover, outputs controlled by the highest priority task experience a bump-free switchover. For example, outputs do not revert to a previous state.
- Outputs in lower priority tasks may experience a change of state.

The switchover time of a redundant system depends on the type of failure and the network update time (NUT) of the ControlNet network. For a NUT of 10 ms, the switchover time is approximately 80...220 ms.

To take over control, the secondary controller requires the same project as the primary controller. It also requires up-to-date tag values.

These terms describe the process of communication between the two controllers.

## Primary Chassis

<!-- image -->

## Controller Communication Terms

| Term Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Crossload The transfer of any or all of the contents of the primary controller to the secondary controller. This could be updated tag values, force values, online edits, or any other information about the project. A crossload happens initially when the chassis synchronize and then repeatedly as the primary controller executes its logic.                                                                                                                                                                                |
| Synchronize The process that readies a secondary chassis to take over control if a failure occurs in the primary chassis. During synchronization, the 1757-SRM modules check that the partner modules in the redundant chassis pair are compatible with each other. The SRM modules also provide the path for crossloading (transferring) the content of the primary controller to the secondary controller. Synchronization occurs when power is applied to the secondary chassis and after a switchover is diagnosed and fixed. |
| Synchronized The secondary chassis is ready to assume control if the primary chassis fails.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Disqualified The secondary chassis is not synchronized with the primary chassis. If a secondary chassis is disqualified, it cannot take over control of the machine or process. A secondary chassis can be manually disqualified.                                                                                                                                                                                                                                                                                                 |
| Qualify Same as synchronize.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Qualified Same as synchronized.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

The 1757-SRM modules keep communication between the primary and secondary chassis.

- Unless you are updating controller revisions, do not download the project to the secondary controller. While the secondary controller is synchronizing with the primary controller, the 1757-SRM modules automatically let the primary controller transfer the project to the secondary controller.
- Once the secondary controller is synchronized, the 1757-SRM modules keep the controller synchronized by providing the path for crossloading any changes that occur in the primary controller. These changes include:
- – online edits.
- – force values.
- – changes to properties.
- – changes to data.
- – results of logic execution.

## Making Online Edits

## Increasing Scan Time

Online edits automatically crossload to the secondary controller. They become inactive if a switchover happens before you assemble them into the project. This stops a mistake from faulting both the old and new primary controllers.

Suppose you test an online edit and it causes the controller to fault. In that case, a switchover happens. The new primary controller automatically untests the edits and goes back to the original code.

You have the option to keep the edits active after a switchover (at the risk of faulting both controllers).

At the end of each program, the primary controller pauses its execution to crossload the result of any output instruction that executed in the program. This results in an increased program scan time for a synchronized redundancy system.

<!-- image -->

## Network Addresses During a Switchover

Each CNB, ENBT, or EWEB module in a redundant chassis shares a pair of network addresses with its partner in the other chassis.

## ControlNet Network

<!-- image -->

## EtherNet/IP Network

<!-- image -->

## Quick Start Checklists

These checklists provide a summary of the criteria for a successful ControlLogix redundancy system. See the remaining chapters for more information on each parameter.

## System Layout

| Parameter Criteria Page         |                                                                                                                                                                                                                                                                                                                                         |        |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| ControlNet Networks             | • ControlNet networks are the primary networks for the system. •  OK to bridge to devices on other networks, such as DeviceNet, Universal Remote I/O, and DH+ networks. •  Networks follow the guidelines in Logix5000 Controllers Design Considerations, publication 1756-RM094.                                                       | 28, 31 |
| I/O Placement                   | • All I/O modules in remote chassis or DIN rails (no I/O in the local chassis) •  All I/O in only these locations: •  Same ControlNet network as the redundant controllers (no bridging) •  DeviceNet network (via a 1756-DNB module in a remote chassis) •  Universal remote I/O network (via a 1756-DHRIO module in a remote chassis) | 28, 31 |
| ControlNet Network Update Times | •  NUTs ≤ 90 ms •  NUTs ≤ specified relationship to each other                                                                                                                                                                                                                                                                          | 35     |
|                                 | Number of ControlNet Nodes At least 2 nodes on each network in addition to the CNBs in the redundant chassis. For example, each ControlNet network has at least 4 nodes.                                                                                                                                                                | 35     |
| ControlNet Node Assignments     | •  Nonredundant nodes use the lowest node numbers. •  CNB modules in the redundant chassis set close to the scheduled network maximum (SMAX). •  2 consecutive node addresses for each set of partner CNB modules (one in each chassis). •  Switches of each partner CNB module set to the same node address.                           | 18, 35 |
|                                 | Network Access Ports No devices connected to the network access ports of CNB modules in the redundant chassis.                                                                                                                                                                                                                          | 28     |
|                                 | EtherNet/IP Networks EtherNet/IP networks are only for HMIs, workstations, and messaging (no control of I/O). No EtherNet/IP network for: •  control of I/O. •  peer interlocking (produced and consumed tags).                                                                                                                         | 28, 38 |

## Redundant Chassis Configuration

| Parameter Criteria Page   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |              |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
|                           | Chassis Size Same size chassis for each pair of redundant chassis. 29                                                                                                                                                                                                                                                                                                                                                                                                        |              |
| Chassis Layout            | • Only these modules in each redundant chassis: •  Controllers •  ControlNet modules •  EtherNet/IP modules •  System redundancy module (needs 2 slots) •  Each chassis within a redundant pair looks the same. •  Identical modules (same catalog number, series, revision, and memory size) •  Same slot assignments                                                                                                                                                       | 29           |
| System Redundancy Modules | 1757-SRM module: •  1 in each redundant chassis •  Needs 2 slots •  Needs 1757-SRCx cable [1 m (3 ft), 3 m (9 ft), 10 m (30 ft), 50 m (150 ft), and 100 m (300 ft)]                                                                                                                                                                                                                                                                                                          | 29, 30       |
|                           | Controllers ControlLogix5555, ControlLogix5561, ControlLogix5562, or ControlLogix5563 controllers •  Which type of controller do you want to use? •  If ControlLogix5555, then 1 or 2 controllers in each redundant chassis. •  If ControlLogix5561, ControlLogix5562, or ControlLogix5563, then only 1 controller in each redundant chassis. •  Same type of controller throughout the chassis. •  Enough memory for 2 copies of all data. •  7 connections for redundancy. | 29           |
|                           | ControlNet Modules 1756-CNB/D/E or 1756-CNBR/D/E module or modules: •  CPU usage ≤ 75%. •  CNB modules have the same keeper information. • ≤ 5 CNB modules. See also parameter .                                                                                                                                                                                                                                                                                             | 29, 107, 123 |

## Redundant Chassis Configuration (Continued)

| Parameter Criteria Page                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| EtherNet/IP Modules 1756-ENBT or 1756-EWEB modules: •  Which modules do you want to use? •  If 1756-ENBT, catalog revision greater than or equal to E01 (E01, E02, …, F01). See the label on the side of the module or its box. •  If 1756-EWEB, any catalog revision. •  Up to 2 EtherNet/IP modules in each redundant chassis, within these limits. If you have Use up to 1 ControlNet module 2 EtherNet/IP modules 2 ControlNet modules 2 EtherNet/IP modules | 29, 38                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 3 ControlNet modules 2 EtherNet/IP modules  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 4 ControlNet modules 1 EtherNet/IP module   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 5 ControlNet modules No EtherNet/IP modules |
| Do not use more than 5 ControlNet modules.                                                                                                                                                                                                                                                                                                                                                                                                                       |                                             |

## RSLogix5000 Project

| Parameter Criteria         |                                                                                                                                                                                                                                                                                                                                                                  | Page        |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|                            | Number of Projects Only one RSLogix 5000 project for the pair of redundant controllers. The project automatically crossloads to the secondary controller when the secondary controller synchronizes with the primary controller.                                                                                                                                 | 65          |
| Controller Properties      | • ControlLogix5555, ControlLogix5561, ControlLogix5562, or ControlLogix5563 controller. •  Redundancy enabled.                                                                                                                                                                                                                                                   | 68          |
| Task Structure             | • Only one task at the highest priority. •  If more than one task, all tasks periodic.                                                                                                                                                                                                                                                                           | 70, 76, 119 |
| I/O                        | • Outputs that require a bumpless switchover are in the highest priority task. •  Requested packet interval (RPI) less than or equal to 375 milliseconds. (Larger RPIs may produce a bump at switchover.).                                                                                                                                                       | 70          |
|                            | Task Watchdog Time Watchdog time ≥ (2 * maximum_scan_time) + 150 ms where: Maximum_scan_time is the maximum scan time for the entire task when the secondary controller is synchronized.                                                                                                                                                                         | 100         |
| Minimizing Scan Time       | • A few large programs instead of a lot of small programs. •  No unused tags. •  Arrays and user-defined data types instead of individual tags. •  User-defined data types as compact as possible. •  Code as compact as possible. •  Code runs only when you need it. •  Data grouped by how often you need it. •  DINT tags instead of SINT or INT tags.       | 76          |
|                            | Data Integrity Special treatment for: •  Bit Shift Left (BSL) and Bit Shift Right (BSR) instructions. •  FIFO Unload (FFU) instructions. •  logic that is scan dependent.                                                                                                                                                                                        | 82          |
| Produced and Consumed Tags | If you want a controller in another chassis to consume a tag from the redundant controller, use a comm format of None. In the I/O configuration of the consuming controller, select a comm format of None for the remote CNB module (the CNB that is physically in the redundant chassis). This comm format of None is only available over a ControlNet network. | 70          |
| Message (MSG) Instructions | For any MSG instruction from a controller in another chassis to a redundant controller, cache the connection.                                                                                                                                                                                                                                                    | 70          |

## Operator Interface Terminals

|                                                                                                                                                      | Parameter Operator Interfaces Criteria Page                                                                                               | Parameter Operator Interfaces Criteria Page                                                                                               |            |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------|
|                                                                                                                                                      | EtherNet/IP Network PanelView Standard terminal Same as a nonredundant system 28, 32, 38                                                  | EtherNet/IP Network PanelView Standard terminal Same as a nonredundant system 28, 32, 38                                                  |            |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal:       | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal:       |            |
|                                                                                                                                                      |                                                                                                                                           | In this module Set aside                                                                                                                  |            |
|                                                                                                                                                      |                                                                                                                                           | controller 5 connections                                                                                                                  |            |
|                                                                                                                                                      |                                                                                                                                           | ENBT 5 connections                                                                                                                        |            |
|                                                                                                                                                      |                                                                                                                                           | EWEB 5 connections                                                                                                                        |            |
| RSView Supervisory Edition software with RSLinx Enterprise software                                                                                  | •  Use RSLinx Enterprise software revision 3.0 or later. •  Use IP swapping. •  Keep the HMI and both redundant chassis                   | •  Use RSLinx Enterprise software revision 3.0 or later. •  Use IP swapping. •  Keep the HMI and both redundant chassis                   |            |
| •  RSView Supervisory Edition software with RSLinx 2.x software •  RSView 32 software •  Any other HMI client software that uses RSLinx 2.x software | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                    | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                    |            |
| •  PanelView Standard terminal •  PanelView 1000e/1400e terminal                                                                                     | Do terminals use unscheduled communication? •  Yes — Use ≤ 4 terminals per controller. •  No — Use the number of terminals that you need. | Do terminals use unscheduled communication? •  Yes — Use ≤ 4 terminals per controller. •  No — Use the number of terminals that you need. | 28, 32, 35 |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal.       | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal.       |            |
|                                                                                                                                                      |                                                                                                                                           | In this module Set aside                                                                                                                  |            |
|                                                                                                                                                      |                                                                                                                                           | Controller 5 connections                                                                                                                  |            |
|                                                                                                                                                      |                                                                                                                                           | CNB 5 connections                                                                                                                         |            |
| •  RSView Supervisory Edition software with RSLinx 2.x software •  RSView 32 software •  Any other HMI client software that uses RSLinx 2.x software | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                    | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                    |            |

## Notes:

## Introduction

27

## Design the System

This chapter explains how to design a redundancy system for a ControlLogix controller.

| Topic Page                                   |
|----------------------------------------------|
| Laying Out the System 28                     |
| Placement of a Pair of Redundant Chassis 30  |
| Placement of the I/O 31                      |
| Placement of Operator Interface Terminals 32 |
| Additional Redundant Components 33           |
| Checking Connection Requirements 35          |
| Planning a ControlNet Network 35             |
| Planning an EtherNet/IP Network 38           |
| Additional Design Considerations 41          |

<!-- image -->

## Laying Out the System

## ControlLogix Redundancy Requirements and Recommendations

<!-- image -->

## ControlLogix Redundancy Requirements and Recommendations (Continued)

<!-- image -->

## Placement of a Pair of Redundant Chassis

With the standard redundancy module cables, a pair of redundant chassis (primary and secondary) can function up to 100 m (300 ft) apart.

## Redundant Chassis Placement

<!-- image -->

## If You Need More Than 100 Meters Between Chassis

To place the primary and secondary controller chassis more than 100 meters apart, use a custom fiber optic cable. For a custom cable, follow these rules:

- Keep total light loss through the cable less than or equal to 7dB.
- Keep total length less than or equal to 4 km.
- Use high quality 62.5/125 micron multi-mode fiber-optic cable.
- Use professionally installed SC-style connectors to connect to the 1757-SRM modules.

## Placement of the I/O

In a ControlLogix redundancy system, place all I/O in only these locations:

- Same ControlNet network as the redundant controllers (no bridging to I/O modules on another ControlNet network)
- DeviceNet network
- Universal remote I/O network

## IO Placement

<!-- image -->

## Placement of Operator Interface Terminals

For operator interface terminals, stay within these limitations.

## Operator Interface Terminal Limitations

| Network Operator Interfaces Guidelines                                                                                                               |                                                                                                                                                |                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                      | EtherNet/IP network PanelView Standard terminal Same as a nonredundant system                                                                  | EtherNet/IP network PanelView Standard terminal Same as a nonredundant system                                                                  |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal.            | •  Use RSLinx Enterprise software revision 3.0 or later. •  Set aside connections for each PanelView Plus or VersaView CE terminal.            |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | In this module Set aside                                                                                                                       |                                                                                                                                                |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    |                                                                                                                                                | Controller 5 connections                                                                                                                       |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    |                                                                                                                                                | CNB 5 connections                                                                                                                              |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    |                                                                                                                                                | ENBT 5 connections                                                                                                                             |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    |                                                                                                                                                | EWEB 5 connections                                                                                                                             |
| RSView Supervisory Edition software with RSLinx Enterprise software                                                                                  | •  Use RSLinx Enterprise software revision 3.0 or later. •  Use IP swapping. •  Keep the HMI and both redundant chassis on the same subnet.    | •  Use RSLinx Enterprise software revision 3.0 or later. •  Use IP swapping. •  Keep the HMI and both redundant chassis on the same subnet.    |
| •  RSView Supervisory Edition software with RSLinx 2.x software •  RSView 32 software •  Any other HMI client software that uses RSLinx 2.x software | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                         | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                         |
| ControlNet network  •  PanelView Standard terminal •  PanelView 1000e/1400e terminal                                                                 | Do your terminals use unscheduled communication? •  Yes — Use ≤ 4 terminals per controller. •  No — Use the number of terminals that you need. | Do your terminals use unscheduled communication? •  Yes — Use ≤ 4 terminals per controller. •  No — Use the number of terminals that you need. |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | Set aside connections for each PanelView Plus or VersaView CE terminal.                                                                        | Set aside connections for each PanelView Plus or VersaView CE terminal.                                                                        |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    | In this module Set aside                                                                                                                       |                                                                                                                                                |
| •  PanelView Plus terminal •  VersaView industrial computer running a Windows CE operating system                                                    |                                                                                                                                                | Controller 5 connections                                                                                                                       |
| •  RSView Supervisory Edition software •  RSView 32 software •  Any other HMI client software that uses RSLinx 2.x software                          | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                         | Limit the number of RSLinx servers that a controller uses to 1 (ideal) to 3 (maximum).                                                         |

## Additional Redundant Components

In addition to using redundant pairs of controllers, you may also add these redundant components to your system:

- Redundant ControlNet Media
- Redundant Power Supplies

## Redundant ControlNet Media

Redundant ControlNet media prevents a loss of communication if a trunkline or tap is severed or disconnected. It uses these components:

- 1756-CNBR ControlNet modules
- Two identical ControlNet links

## Redundant ControlNet Media Components

<!-- image -->

## Redundant Power Supplies

Redundant power supplies let you maintain power to a ControlLogix chassis if a power supply fails. Redundant power supplies use these supplies:

- Two redundant power supplies, any combination of 1756-PA75R and 1756-PB75R.
- 1756-PSCA chassis adapter module, in place of the standard power supply.
- Two 1756-CPR cables to connect the power supplies to the 1756-PSCA adapter.
- User-supplied annunciator wiring to connect the power supplies to the input modules if needed.

## Redundant Power Supplies

<!-- image -->

## Checking Connection Requirements

## Planning a ControlNet Network

Set aside seven connections in each redundant controller for redundancy communication.

- Two connections for the SRM
- Five connections for the partner controller

Follow these guidelines to plan a ControlNet network.

## ControlNet Network Guidelines

| Guideline Details                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Make sure the network has at least 2 nodes plus the redundant chassis pair.   | An additional node can be: •  a second CNB module in the same remote chassis or in a different remote chassis. •  any other ControlNet device. •  a workstation that is running RSLinx software. If your ControlNet network contains only one node other than the redundant chassis pair, that node will drop its connections during a switchover. This may cause the outputs of that node to change state during the switchover.                                                                                                                                                                                             |
| Give the lowest ControlNet addresses to I/O chassis and other remote chassis. | Do not give the lowest addresses to the redundant chassis pair. If you give the lowest address to a CNB module in the redundant chassis pair: •  on a switchover, you may temporarily lose communication with I/O modules, produced tags, and consumed tags. •  If you remove the CNB module from the primary chassis while chassis power is on, you may temporarily lose communication with I/O modules, produced tags, and consumed tags. •  If every ControlNet node powers down at the same time (for example, a plant-wide power loss), you may have to cycle the power to the primary chassis to restore communication. |

Guideline Details

Set aside 2 consecutive ControlNet addresses for each pair of redundant chassis (for example, nodes 3 and 4).

- If each redundant chassis has multiple CNB modules, set aside a pair of node numbers for each pair of CNB modules (one in each chassis).
- Do not configure any other device on the ControlNet network for either of these addresses. For example, if you allocated nodes 3 and 4 for the redundant chassis, then no other device should use those node numbers.

| Pair of CNB modules (one in each redundant chassis)   | Slot and node numbers   | Slot and node numbers                                       | Slot and node numbers   |
|-------------------------------------------------------|-------------------------|-------------------------------------------------------------|-------------------------|
| Pair of CNB modules (one in each redundant chassis)   |                         | Slot # Primary node # Secondary node # (primary node # + 1) |                         |
| 1st pair of CNB modules                               |                         |                                                             |                         |
| 2nd pair of CNB modules                               |                         |                                                             |                         |
| 3rd pair of CNB modules                               |                         |                                                             |                         |
| 4th pair of CNB modules                               |                         |                                                             |                         |
| 5th pair of CNB modules                               |                         |                                                             |                         |

Know that the switchover time depends on the NUT of the ControlNet network.

Use the network update time (NUT) of the ControlNet network to estimate how long it takes your system to switchover.

|                                                     | If And the NUT is Then the switchover time is   |
|-----------------------------------------------------|-------------------------------------------------|
| The chassis loses power or a module fails           | 6 ms or less 60 ms                              |
| The chassis loses power or a module fails           | 7 ms or more 5 (NUT  ) + MAX (2 (NUT  ), 30)    |
| A CNB module cannot communicate with any other node | ⇒  14 (NUT  ) + MAX (2 (NUT  ), 30) + 50        |

## Example 1

The chassis loses power and the NUT = 4 ms. In that case, the switchover time is approximately 60 ms.

## Example 2

The chassis loses power and the NUT = 10 ms. In that case, the switchover time is approximately 80 ms.

## Example 3

You unplug the CNB from the network and the NUT = 10 ms. In that case, the switchover time is approximately 220 ms.

Use a NUT that is less than or equal to 90 ms. If you use a larger network update time (NUT), the controller could lose its connection with a module during a switchover. This could cause outputs to change state.

Guideline Details

Do the redundant chassis use more than 1 ControlNet network?

- Yes — See page 29.
- No — Skip this guideline.

The NUT of each network must be within the values indicated on page 29. If you use a larger network update time (NUT), the controller could lose its connection with a module during a switchover. This could cause outputs to change state.

## Example

<!-- image -->

| If the smallest NUT on a network is (ms) Then the largest NUT on any other network must be less than or equal to (ms)   |
|-------------------------------------------------------------------------------------------------------------------------|
| 2 15                                                                                                                    |
| 3 17                                                                                                                    |
| 4 19                                                                                                                    |
| 5 21                                                                                                                    |
| 6 23                                                                                                                    |
| 7 25                                                                                                                    |
| 8 27                                                                                                                    |
| 9 29                                                                                                                    |
| 10 31                                                                                                                   |
| 11 33                                                                                                                   |
| 12 35                                                                                                                   |
| 13 37                                                                                                                   |
| 14 39                                                                                                                   |
| 15 41                                                                                                                   |
| 16 43                                                                                                                   |
| 17 46                                                                                                                   |
| 18 48                                                                                                                   |
| 19 50                                                                                                                   |
| 20 52                                                                                                                   |

| If the smallest NUT on a network is (ms) Then the largest NUT on any other network must be less than or equal to (ms)   |
|-------------------------------------------------------------------------------------------------------------------------|
| 21 55                                                                                                                   |
| 22 57                                                                                                                   |
| 23 59                                                                                                                   |
| 24 62                                                                                                                   |
| 25 64                                                                                                                   |
| 26 66                                                                                                                   |
| 27 68                                                                                                                   |
| 28 71                                                                                                                   |
| 29 73                                                                                                                   |
| 30 75                                                                                                                   |
| 31 78                                                                                                                   |
| 32 80                                                                                                                   |
| 33 82                                                                                                                   |
| 34 84                                                                                                                   |
| 35 87                                                                                                                   |
| 36 89                                                                                                                   |
| 37...90 90                                                                                                              |

## Planning an EtherNet/IP Network

Follow these guidelines as you plan your EtherNet/IP network.

## EtherNet/IP Network Guidelines

| Guideline Details                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use EtherNet/IP only for HMIs, workstations, and messaging.                                                          | In a redundant system, use an EtherNet/IP network only for HMI, workstation, and message communication. Do not use an EtherNet/IP network for: •  control of I/O modules. •  peer interlocking (produced and consumed tags). Important: RSLogix 5000 software lets you set up and download a project that tries to use an EtherNet/IP network for I/O, produced tags, or consumed tags. Those communications do not work however. |
| Are communication delays OK during a switchover? If Yes, then continue with EtherNet/IP. If No, then use ControlNet. | Communication stops over an EtherNet/IP network with your controllers and HMIs during a switchover. •  You will not be able to communicate with them for up to a minute. •  The actual delay depends on your network topology. If you need bumpless communication, use a ControlNet network.                                                                                                                                      |
|                                                                                                                      | If you need a redundant network, use ControlNet. 2 EtherNet/IP modules in same chassis does not give you redundant EtherNet/IP communication. A switchover still happens if one of the modules fails or a cable breaks. See How an EtherNet/IP Module Handles a Cable Break on page 40.                                                                                                                                           |
| Make sure that your ENBT modules are catalog revision E01 or later. ControlLog CATNO/SERIES 1756-ENBT CAT. NO./SERIES E01 CAT. REV. Ethernet/IP 10/100                                                                                                                      | To use a 1756-ENBT module in a redundant controller chassis, make sure the catalog revision of the module is greater than or equal to E01 (E01, E02, …, F01). •  To find the catalog revision, look at the label on the side of the module or box. •  If you use an older ENBT module, your secondary chassis will not synchronize.                                                                                               |

<!-- image -->

| Guideline Details                                                                             |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Decide how to handle IP addresses.                                                            | If both redundant chassis are on Then                                                                                                                                                                                                      |                                                                                                                                                                                                                                            |
|                                                                                               | Same subnet  Switch Primary Chassis Secondary Chassis                                                                                                                                                                                      | Use IP swapping. During a switchover the primary and secondary modules swap IP addresses. This lets you use the same IP address regardless of which chassis is primary. See the next guideline for details.                                |
|                                                                                               | Different subnets  Switch Router Switch                                                                                                                                                                                                    | Do not use IP swapping. You must change to the new primary address after a switchover. Use ControlLogix Redundancy Alias Topic Switcher software to do this. See Appendix A.                                                               |
| If you are using IP swapping, give the same IP address to the primary module and its partner. | A. Give the same IP address, subnet mask, and gateway address to both modules in the redundant pair. B. Leave the next highest IP address open for the secondary module. For example Set the primary and secondary modules to: 10.10.10.10 | A. Give the same IP address, subnet mask, and gateway address to both modules in the redundant pair. B. Leave the next highest IP address open for the secondary module. For example Set the primary and secondary modules to: 10.10.10.10 |

## Worksheet for IP Swapping

| Pair of ENBT or EWEB Modules (one in each redundant chassis)   | Slot # Configuration   | Slot # Configuration                       | Slot # Configuration        | Slot # Configuration   |
|----------------------------------------------------------------|------------------------|--------------------------------------------|-----------------------------|------------------------|
| Pair of ENBT or EWEB Modules (one in each redundant chassis)   | Primary IP Address     | Secondary IP Address (primary address + 1) | Subnet Mask Gateway Address |                        |
| 1st pair of ENBT or EWEB modules                               |                        |                                            |                             |                        |
| 2nd pair of ENBT or EWEB modules                               |                        |                                            |                             |                        |

## One switch

## One subnet

## How an EtherNet/IP Module Handles a Cable Break

An EtherNet/IP module looks for a carrier signal only from the closest switch. It does not know the health of the network beyond that point. Data does not have to be flowing.

If the EtherNet/IP module:

- gets the carrier signal, it considers the network as OK.
- does not get the carrier signal, it shows Link lost.

<!-- image -->

## Several switches

## Several subnets

<!-- image -->

## Additional Design Considerations

Switchover always triggers an event task in a remote, nonredundant controller.

Keep these things in mind as you design your system.

## Additional Design Considerations

A switchover triggers an event task under this combination of circumstances:

- The event task is in a nonredundant controller. An event task is not permitted in a redundant controller.
- A redundant controller triggers the event task via a produced tag.

This occurs regardless of how you configure the produced tag.

Both configurations always trigger an event task during a switchover.

<!-- image -->

<!-- image -->

## Notes:

## Introduction

## Preliminary Information

43

## Install the System

This chapter explains how to install the hardware of a ControlLogix redundancy system.

| Topic Page                                         |
|----------------------------------------------------|
| Preliminary Information 43                         |
| Install the Chassis for the Controllers 45         |
| Install Modules in the First Redundant Chassis 46  |
| Install Modules in the Second Redundant Chassis 48 |
| Install the Remote Chassis or Rails 49             |
| Configure EtherNet/IP Modules 50                   |
| Flash the Modules 51                               |
| Check the Installation 51                          |

## IMPORTANT

## Use of the Network Access Port (NAP)

Do not connect any device to the network access port (NAP) of a 1756-CNB/D/E or 1756-CNBR/D/E module in a redundant chassis.

- If you connect a device to the NAP of a CNB module in a redundant chassis, a switchover will fail to occur if the CNB module is disconnected from the network. While the CNB module is disconnected from the network, the controller will be unable to control any I/O devices through that CNB module.
- If you connect a workstation to the NAP of a CNB module in a redundant chassis, the workstation will be unable to go online after a switchover.

To connect a device to a ControlNet network via a NAP, use a NAP that is outside of a redundant chassis.

<!-- image -->

This chapter provides the sequence of tasks and the critical actions for the successful installation of a ControlLogix redundancy system. It does not replace the installation instructions for the components of the system. During installation, refer to these publications.

## Installation Publications

| Install this component According to this publication                                                                 |
|----------------------------------------------------------------------------------------------------------------------|
| 1756-A4, -A7, -A10, -A13, or -A17 chassis ControlLogix Chassis Installation Instructions, publication 1756-IN080     |
| 1756-PA72 or -PB72 power supply ControlLogix Power Supplies Installation Instructions, publication 1756-5.67         |
| 1756-PA75 or -PB75 power supply ControlLogix Power Supplies Installation Instructions, publication 1756-5.78         |
| ControlLogix controller ControlLogix Controller and Memory Board Installation Instructions, publication 1756-IN101   |
| 1756-CNB/D/E or -CNBR/D/E module ControlLogix ControlNet Bridge Installation Instructions, publication 1756-IN571    |
| 1756-ENBT module ControlLogix EtherNet/IP Bridge Module Installation Instructions, publication 1756-IN019            |
| 1756-EWEB module EtherNet/IP Web Server Module Installation Instructions, publication 1756-IN588                     |
| 1757-SRM module ProcessLogix/ControlLogix System Redundancy Module Installation Instructions, publication 1757-IN092 |

Installation instructions provide important information, such as detailed installation steps, safety considerations, enclosure requirements, and hazardous location information.

Before installing the system, review these guidelines for safe handling of ControlLogix components.

<!-- image -->

When you insert or remove a module while backplane power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## Install the Chassis for the Controllers

<!-- image -->

1. Install the two ControlLogix chassis (redundant) that will contain the controllers.
- Place the chassis within the length of a 1757-SRCx cable.
- Install each chassis according to the ControlLogix Chassis Installation Instructions, publication 1756-IN080.
- If you are converting an existing system that contains local I/O modules, you still need two additional chassis. In a redundant system, you must place all I/O modules outside the redundant chassis pair.

Repeated electrical arcing causes excessive wear to contacts on both a module and its mating connector. Worn contacts may create electrical resistance that can affect module operation.

<!-- image -->

## Preventing Electrostatic Discharge

This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- If available, use a static-safe workstation.
- When not in use, store the equipment in appropriate static-safe packaging.

## Install Modules in the First Redundant Chassis

<!-- image -->

2. For each chassis, install a ControlLogix power supply according to the corresponding installation instructions.

| Power Supply Publication   |                                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------------|
|                            | 1756-PA72 ControlLogix Power Supplies Installation Instructions, publication 1756-IN078B          |
| 1756-PB72                  | 1756-PA72 ControlLogix Power Supplies Installation Instructions, publication 1756-IN078B          |
|                            | 1756-PA75R ControlLogix Redundant Power Supply Installation Instructions, publication 1756-IN573C |
| 1756-PB75R                 | 1756-PA75R ControlLogix Redundant Power Supply Installation Instructions, publication 1756-IN573C |

## IMPORTANT

We recommend constant power supply to one of the redundant chassis to maintain uninterrupted operation of the redundant controller parts.

## IMPORTANT

Set the rotary switches of the 1756-CNB/D/E or 1756-CNBR/D/E modules for both redundant chassis to the same node address.

The primary node number is the node number of the primary chassis.

1. Set the rotary switches of each of the 1756-CNB/D/E or 1756-CNBR/D/E modules to the primary node number plus one.

For example, modules 3 and 4 have a primary node number of 2. If you allocate nodes 3 and 4 for the redundant chassis, set both CNB modules to node 3.

<!-- image -->

2. Install a 1756-CNB/D/E or 1756-CNBR/D/E module. See ControlLogix ControlNet Bridge Installation Instructions, publication 1756-IN571.

## WARNING

<!-- image -->

If you connect or disconnect the communications cable with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

3. Connect the CNB module to the ControlNet network.

<!-- image -->

42799

4. Install the controller or controllers. See ControlLogix Controller and Memory Board Installation Instructions, publication 1756-IN101.
5. Install the 1756-ENBT or 1756-EWEB module or modules (2 maximum), if required. Connect each module to an ethernet switch.
6. Install the 1757-SRM module. See ProcessLogix/ControlLogix System Redundancy Module Installation Instructions, publication 1757-IN092.

## Install Modules in the Second Redundant Chassis

<!-- image -->

## IMPORTANT

- The modules in each redundant chassis must match each other slot-by-slot.
- Set the rotary switches of the 1756-CNB/D/E or 1756-CNBR/D/E modules for both redundant chassis to the same node address.
1. For each module in the first redundant chassis, install an identical module into the same slot of the second redundant chassis.
2. Connect the CNB, ENBT, and EWEB modules to their respective networks.
3. Connect one of these fiber optic cables to the 1757-SRM modules:
- 1757-SRC1
- 1757-SRC3
- 1757-SRC10
- 1757-SRC50
- 1757-SRC100

## Install the Remote Chassis or Rails

You must install all I/O modules and additional types of communication modules in remote chassis or on DIN rails. This example shows a remote 1756 chassis. You can use any type of chassis or device that you can connect to the ControlNet network.

<!-- image -->

You must have at least 2 other nodes in addition to the redundant chassis pair. See Lay Out the System on page 2.

If you connect the workstation to the network via a network access port on a CNB module, use a CNB module in a remote chassis. This lets a switchover occur after the failure of a ControlNet tap of a primary chassis.

## IMPORTANT

As you install the chassis, follow these guidelines:

- Do not assign any device to the address of the CNB modules in the redundant chassis plus one.

For example, if you set the rotary switches of the CNB modules in the redundant chassis to node 11, no other device should use node 12.

- Use a remote chassis for communication modules such as:
- – 1756-ENET
- – 1756-DHRIO
- – 1756-MVI
- – 1756-DNB

## Configure EtherNet/IP Modules

To use an EtherNet/IP module, give it an IP address, subnet mask, and gateway address.

|                                                          | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                          | Before you begin. A. Perform these steps if you have not already: •  installed and connected both 1757-SRM modules. •  obtained the IP address, subnet mask, and gateway address for each EtherNet/IP module. See Plan the EtherNet/IP Networks on page 12. •  Do you know how to configure an EtherNet/IP module in a nonredundant system? •  If no, then continue with step B. •  If yes, then go to step B. B. Get this publication: EtherNet/IP Modules in Logix5000 Control Systems, publication ENET-UM001 You will use that publication when you configure each module. |
| Configure the EtherNet/IP modules in the first chassis.  | A. Turn on the power to only one of the redundant chassis. For example, if both chassis are on, turn off one of them. B. Configure the EtherNet/IP module in the chassis that is on. •  Do you see the IP address on the front of the module? •  If no, then return to step B. •  If yes, then continue with step C. C. Repeat step B for each EtherNet/IP module in this chassis.                                                                                                                                                                                             |
| Configure the EtherNet/IP modules in the second chassis. | A. Turn off the chassis that you just configured. B. Turn on the other chassis. C. Configure the EtherNet/IP module in the chassis that is on. •  Do you see the IP address on the front of the module? •  If no, then return to step C. •  If yes, then continue with step C. D. Repeat step C for each EtherNet/IP module in this chassis.                                                                                                                                                                                                                                   |

## Flash the Modules

<!-- image -->

## Check the Installation

To flash the modules, perform this procedure.

1. Turn on the power to one of the redundant chassis.

## IMPORTANT

Only power up one chassis at a time.

2. Wait for the 1757-SRM module to display PRIM.
3. Flash upgrade each module in the chassis with a compatible revision of firmware.
- See the ControlFLASH Firmware Upgrade Kit User Manual, publication 1756-6.5.6.
- To find the chassis in RSLinx software, locate the node number or IP address on the front of the communication module.
4. Turn off the power to the chassis.
5. Turn on the power to the second redundant chassis.
6. Wait for the 1757-SRM module to display PRIM.
7. Flash upgrade each module in the chassis with a compatible revision of firmware. Use the same revisions that you used for the first redundant chassis.

Check the installation to make sure that your redundant chassis are able to synchronize.

Complete this procedure after you:

- install the system.
- configure the communication modules.
- update firmware.

<!-- image -->

## Actions

1. Turn on the chassis power to the partner (secondary) chassis.
2. Wait for the 1757-SRM module to complete its power-up cycle.
- The SRM module takes 1...3 minutes to power up.
- It may also take several minutes to synchronize the secondary controller.
- Does 1 of the 1757-SRM modules show PRIM and the other module show SYNC?
- Yes — Stop. The system is synchronized.
- No — There is a problem. The system is not synchronized. Go to step 3.
3. Make sure that the Auto-Synchronization option of the SRMs is set to Always. For help, see Chapter 4.
- Does 1 of the 1757-SRM modules show PRIM and the other module show SYNC?
- Yes— Stop. The system is synchronized.
- No— Go to Troubleshoot a Failure to Synchronize on page 105.

## Introduction

<!-- image -->

## Configure the System Redundancy Module

This chapter explains how to set or change the configuration of a 1757-SRM module. The SRM module controls the synchronization and switchover of your redundancy system.

Use this chapter after you have installed your system to:

- change how the SRM supports your system.
- restart your system after redundant chassis regain power after a power loss.

|                                                         | If Refer to this section On page                                  |
|---------------------------------------------------------|-------------------------------------------------------------------|
|                                                         | You just installed your system Open the SRM Configuration Tool 53 |
|                                                         | Check the Revision of Your SRM Configuration Tool 55              |
|                                                         | Check the Revision of Your SRM Configuration Tool 56              |
|                                                         | Set the SRM Clock 56                                              |
|                                                         | Test a Switchover 59                                              |
| You want to change how the SRM supports your system     | Change Auto-Synchronization 61                                    |
| You want to change how the SRM supports your system     | Change Program Control 62                                         |
| Both redundancy chassis lost power Set the SRM Clock 56 |                                                                   |

## Open the SRM Configuration Tool

53

To configure the system redundancy module, open the 1757-SRM System Redundancy Module configuration tool.

Complete this procedure to:

- set the SRM clock.
- test a switchover.
- troubleshoot a system.
- store or load a project using nonvolatile memory.
- update firmware.

## Before You Begin

RSLinx software includes and automatically installs the 1757-SRM System Redundancy Module configuration tool.

<!-- image -->

Check your revision of the SRM configuration tool when you open it for the first time.

- The revision of tool that you get depends on your version of RSLinx software.
- Some revisions of the SRM configuration tool are not compatible with some revisions of a ControlLogix Redundancy system.

The next section shows you how to see if your revision of the SRM configuration tool is right for your redundancy system.

## Actions

1. Start RSLinx software.
2. From the Communications menu, choose RSWho.
3. Double-click the network to open it.
4. Double-click the communication module in the primary chassis to show the backplane.
5. Double-click the backplane to see its modules.
6. Right-click the 1757-SRM module and select Module Configuration.

<!-- image -->

<!-- image -->

## Check the Revision of Your SRM Configuration Tool

## What to Do Next

## IMPORTANT

Make sure that you check the revision of your SRM configuration tool before you use it. Later revisions of the SRM configuration tool are not compatible with earlier revisions of ControlLogix redundancy systems. See Check the Revision of Your SRM Configuration Tool on page 55.

Check the revision of your SRM configuration tool to make sure that you are using the right revision of the SRM configuration tool for your ControlLogix redundancy system.

## IMPORTANT

Make sure that you check the revision of your SRM configuration tool.

- Revision 2.6 is compatible only with revision 13.x or later ControlLogix redundancy systems.
- You will cause the 1757-SRM module to fault if you use revision 2.6 of the tool with an revision 11.x or earlier redundancy systems.

Perform this procedure to:

- use the SRM configuration tool for the first time.
- connect to a different ControlLogix redundancy system for the first time.
- update the firmware of a ControlLogix redundancy system.

## Before You Begin

RSLinx software automatically installs the SRM configuration tool. Use this table to see which revision of the tool that you get.

## RSLinx Software Versions

| Software Installed Tool                                           |
|-------------------------------------------------------------------|
| RSLinx software, version 2.42 SRM configuration tool revision 2.5 |
| RSLinx software, version 2.43 SRM configuration tool revision 2.6 |
| RSLinx software, version 2.52 SRM configuration tool revision 3.6 |

## Actions

<!-- image -->

| Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Choose which revision to use. Do you connect your computer to ControlLogix redundancy systems revision 11.x or earlier? •  Yes — Use revision 2.5 of the SRM Configuration Tool. Do not use revision 2.6. •  No — Use revision 2.6 of the SRM Configuration Tool. Revision 2.6 is compatible only with revision 13.x or later ControlLogix redundancy systems. You will cause the 1757-SRM module to fault if you use revision 2.6 of the tool with an revision 11.x or earlier redundancy systems. Keep in mind that some features are available only in revision 2.6 or later of the configuration tool. |
| 2. See which revision you have. A. Open the SRM configuration tool if you have not already done so. B. Right-click the title bar of the configuration tool and choose About… 1757-SRMREDUNDANCYMODULE Restore Module lnfo Configuration Synchronization Synchror Move                                                                                                                                                                                                                                                                                                                                         |
| 3. Change your revision If you need a different revision of the SRM configuration tool, see: Knowledgebase document G92234770. To access Rockwell Automation’s Knowledgebase, go to http://support.rockwellautomation.com Important: The SRM configuration tool lets you install only 1 revision on your computer at the same time. To change the revision, remove the revision that you installed earlier.                                                                                                                                                                                                   |

## Set the SRM Clock

To record significant events, set clock of the 1757-SRM module.

Perform this procedure:

- after system installation.
- after power loss to both chassis.

## Before You Begin

The SRM clock records when significant events occur. Please note these characteristics of the SRM clock:

- Only the primary SRM's clock requires setting. The secondary SRM's clock synchronizes itself to the primary SRM's clock.
- The SRM has no battery to keep its clock running. The clock stops without SRM power.
- With power, the primary SRM synchronizes its clock to the most recent event in its event log.
- The secondary SRM event log records when the secondary SRM powered up. Look for WCT time change (&gt; 1 second) event.
- An SRM with a firmware revision 3.37 or earlier does not log its power-down time. If only one of the chassis powers down, use the event log of the other chassis to see when it happened. Look for The Partner RM Screamed event. See Interpret the SRM Event Log on page 109.

## Actions

<!-- image -->

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the network branches until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. 品AB_ETH-2，Ethernet + 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane,1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 05,1757-5RM, Remove + 10.88.88.147, 1756-E AB_VBP-1,1789-A17AVir Driver Diagnostics Configure Driver Device Properties |

Action Details

2. Set the clock. A. Click Configuration.

<!-- image -->

## Test a Switchover

<!-- image -->

Use RSLinx software to manually initiate a switchover.

Perform this procedure after you have synchronized your system and want to test a switchover.

## Before You Begin

The CNB modules in the new primary chassis show the synchronization progress after a switchover. Typically, the modules show this sequence.

primary with no

PwNS ⇒ secondary

## Actions

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the network branches until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. AB_ETH-2，Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBTA 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane, 1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 05,1757-5RM Remove 10.88.88.147, 1756-E AB_VBP-1,1789-A17}A Vir Driver Diagnostics Configure Driver Device Properties |

PwDS ⇒ primary with disqualified secondary

PwQg ⇒ primary with synchronizing (qualifying) secondary

PwQS primary with synchronized (qualified) secondary

<!-- image -->

<!-- image -->

<!-- image -->

2. Start a switchover. A. Click Synchronization.

- B. Choose Initiate Switchover and then choose Yes to continue.

3. Monitor the synchronization progress. A. Click Synchronization Status.

If the controller contains a large project, the system may spend some time synchronizing the secondary controller.

- B. If the Secondary Readiness remains Disqualified:

- Make sure the Auto-Synchronization option = Always.

- See Find the Cause of a Switchover or Disqualification on page 104.

Action Details

1757-SRMREDUNDANCYMODULE

Module Info

Configuration

Synchronization

Synchronization Status

Event Log

System Update

Commands

Sunchronize Secondary

Disqualify Secondary

InitiateSwitchover

Become

1757-SRM REDUNDANCY MODULE

Module Info

Configuration

Synchronization

Synchrorization Status

Event Log

System Update

1015

%Complete

Module

Secondary Readiness

State

Compatibility

口

0

1756-L63

Disqualified

Secondary

Full

1

0

1756-CNB

Disqualified

Secondary

Full

0

1756-ENBT

Disqualified

Secondary

Full

&lt;empty&gt;

4

&lt;empty&gt;

0

1757-SRM

Disqualified

Secondary

Full

&lt;empty&gt;

[-

&lt;empty&gt;

00

&lt;empty&gt;

1757-SRMREDUNDANCYMODULE

Module Info

Configuration

Synchronization

Synchronization Status

Event Log

System Upd

Options

Auto-Synchronization:

Always

SRM Seria) Number:

Name'

## Change Auto-Synchronization

You can control when the 1757-SRM module tries to synchronize the controllers.

Perform this procedure to:

- help synchronize the system.
- prevent the system from crossloading changes.

## Actions

|                                                             | Action Details                                                                                                          |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| 1. Decide when you want the system to synchronize.          | Do you plan to manually disqualify a chassis so you can make changes? •  No — Choose Always •  Yes — Choose Conditional |
| 1. Decide when you want the system to synchronize.          | If you choose Then                                                                                                      |
| 1. Decide when you want the system to synchronize.          | Conditional The SRM keeps the synchronization command that you give it. If                                              |
| 1. Decide when you want the system to synchronize.          | Never The controllers will not try to synchronize, but you can still manually synchronize the controllers.              |
| 2. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the branches of your network until you find the 1757-SRM module in the primary  hi p chassis. D. Right-click the SRM and choose Module Configuration. 白品AB_ETH-2，Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEBA Backplane,1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 10.88.88.147, 1756-E Remove AB_VBP-1,1789-A17AVir Driver Diagnostics Configure Driver Device Properties Module Configuration...                                                                                                                         |

<!-- image -->

## Change Program Control

You can direct the controller to send a message to the 1757-SRM module or block the controller from doing so.

Perform this procedure when you:

- initially configure the SRM.
- decide to send the SRM a message from the controller.

## Before You Begin

See page 91 for a list of messages that a controller can send to an SRM module.

## Actions

<!-- image -->

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open all the network branches to find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. 品AB_ETH-2, Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane, 1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 05, 1757-5RM, 1757 c0M 050LIN04NW Me0 10.88.88.147, 1756-E Remove AB_VBP-1,1789-A17/A Vir Driver Diagnostics Configure Driver |
| 2. Set the program control option. A. Click Configuration.  | B. Do you want to let a controller send a message to the SRM? •  Yes — Check the Enable User Program Control check box. •  No — Uncheck the Enable User Program Control check box. C. Choose Apply and then Yes to continue. D. Choose OK. 1757-SRMREDUNDANCYM0DULE Module Info Configuration S ynchronization Synchronization Status Event Log System Update ptions Auto-Synchronization: Always SRM Serial Number: Name: Chassis ID: Chassis B Description: Enable User Program Control Location:                                                                               |

## Notes:

## Introduction

## Plan for Online Edits

65

<!-- image -->

## Configure and Program the Controller

This chapter explains how to configure and program the controller for redundancy.

## IMPORTANT

Create and maintain only one RSLogix 5000 project for the pair of redundant controllers. When you download the project to the primary controller, the project automatically crossloads to the secondary controller.

To configure and program a controller, complete these tasks.

| Topic Page                                        |
|---------------------------------------------------|
| Plan for Online Edits 65                          |
| Configure a Controller for Redundancy 68          |
| Configure Communications 70                       |
| Estimate the Crossload Time of a Program 74       |
| Minimize Scan Time 76                             |
| Maintain Data Integrity During a Switchover 82    |
| Determine the Status of Your Redundant System 87  |
| Condition Logic to Run After a Switchover 89      |
| Send a Message to the SRM 91                      |
| Download the Project to the Primary Controller 95 |
| Schedule a ControlNet Network 97                  |
| Set Task Watchdog Times 100                       |

Before editing online:

- decide if you want to keep test edits after a switchover.
- be aware that finalizing edits removes your original logic.
- decide how you want to set aside unused memory.

## Decide if You Want to Keep Test Edits after a Switchover

When you edit logic while online with the controller, the edits may fault the controller and cause a switchover.

<!-- image -->

If test edits fault the primary controller, they will likely also fault the secondary controller. To prevent faulting, any test edits are deactivated (untested) during a switchover. As an option, you can keep the edits active after a switchover.

## Retention of Test Edits

<!-- image -->

## Test Edit Options

| If you want to Then                                                                      |                                             |
|------------------------------------------------------------------------------------------|---------------------------------------------|
| Prevent an incorrect online edit from faulting both the primary and secondary controller | Do not retain test edits (default setting). |
| Keep test edits active during a switchover (at the risk of faulting both controllers)    | Retain test edits.                          |

## Be Aware That Finalizing Edits Removes Your Original Logic

Finalize all edits in program.

<!-- image -->

The controller removes the original logic when you finalize all edits in a program. If your changes cause a major fault and a switchover, the new primary controller also faults. That is because there is no original logic to go back to. For example, the new primary controller cannot untest the edits.

This happens even if you set the controller to untest edits on a switchover.

<!-- image -->

## Decide How You Want to Set Aside Unused Memory

<!-- image -->

When the secondary controller receives crossload data, it first buffers tag data in a quarantine section of memory. When it has all of the data and knows it is valid, it moves the data into the main memory area. That is why a redundant controller requires twice as much memory for tags as a nonredundant controller.

The controller sets up the quarantine area at the time of download:

- The controller divides its memory into two sections:
- – tags, including a quarantine area
- – logic
- The controller also divides its unused memory. It reserves a specific amount for tags that you create while online. The rest for logic.

You configure how to reserve unused memory between tags and logic. You do this online in program mode.

## Reservation of Unused Memory

| If you plan to Then Notes                                                                         |                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| While online, create roughly the same amount of new tags and new logic Leave the default setting. |                                                                                                                                                                   |
| While online, create a relatively large amount of new tags but a much smaller amount of new logic | Drag to slider toward Tags. Avoid setting the slider all the way to Tags: •  You will be unable to perform online edits. •  OPC communications may error or fail. |
| While online, create a relatively large amount of new logic but a much smaller amount of new tags | Drag to slider toward Logic. Avoid setting the slider all the way to Logic; you will be unable to create tags while online.                                       |

## Configure a Controller for Redundancy

1. Open or create the RSLogix 5000 project.
2. On the Online toolbar, click the controller button.

<!-- image -->

Does General display the controller type?

- If no, go to step 3.
- If yes, go to step 6.
3. Click the Change Type button.
4. Select your controller.
5. Click OK.
6. Select Redundancy.

<!-- image -->

7. Select Redundancy Enabled.

<!-- image -->

## 8. Click Advanced.

<!-- image -->

- We recommend that you not check this box. Leaving it unchecked prevents an incorrect online edit from faulting both the primary and secondary controller.
- If you want any test edits to remain active during a switchover, then check this box. However, by doing so, you run the risk of faulting both controllers.
- We recommend that you leave the Memory Usage slider in the middle, the default position.
10. To close the Controller Properties dialog box, click .

<!-- image -->

## Configure Communications

A redundant system requires some specific configuration choices for successful communications. Use this section to perform these redundancy tasks:

- Configure I/O
- Configure produced tags
- Configure message (MSG) instructions
- Configure tags for an HMIConfigure I/O

## IMPORTANT

For each module in your system, make sure that the requested packet interval (RPI) is less than or equal to 375 milliseconds. If you use a larger RPI, the controller could lose its connection with the module during a switchover. This could cause outputs to change state.

For any outputs that require a bumpless switchover:

- put those outputs in the highest priority task.
- configure only that task at the highest priority.

## Configure Produced Tags

## IMPORTANT

During a switchover, the connection for tags that are consumed from a redundant controller may time out.

- The data does not update.
- The logic acts on the last data that it received.

After the switchover, the connection reestablishes and the data begins to update again.

If you want a controller in another chassis to consume a tag from the redundant controller, use a comm format of None. In the I/O configuration of the consuming controller, select a comm format of None for the remote CNB module (the CNB that is physically in the redundant chassis).

## IMPORTANT

If you set the remote CNB module to a comm format other than None, you will receive module fault 16#000C in RSLogix5000. This fault signifies a service request error due to an invalid mode or status during a service request.

If

## Produced Tag Configuration

<!-- image -->

## Configure Message (MSG) Instructions

<!-- image -->

## Configured Message Instructions

| If the MSG instruction originates from a redundant controller   | Then                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                 | During a switchover The message instructions status bits are updated asynchronously to the program scan. Consequently, you cannot crossload your message instructions status bits to a secondary controller. During a switchover, any active message instructions become inactive. When this occurs, you will need to reinitialize the execution of your message instructions in the new primary controller. |
|                                                                 | During qualification The scrolling display changes from CMPT for compatible to Qfng for qualifying. •  If a configured message is cached, the primary controller automatically establishes a connection with no errors. •  If a configured message is uncached or unconnected, the primary controller receives Error 1 Extended Error 301, No Buffer Memory .                                                |

## Configured Message Instructions, Continued

| If the message instruction is targeted to a redundant controller   | Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| During the erroring out of a message                               | All backplane communications cease. This stoppage allows the redundant controller to receive the message instruction required to perform a switchover or any diagnostics. Important: If any of your messages are active during a switchover, you can expect one of these things to happen: •  Cached and connected messages cause the message instruction to pause for 7.5 seconds because the initiating controller has not received a response from the targeted controller. For cached messages, the message instruction tries to execute three more times, each attempt followed by a pause of 7.5 seconds. If, after 30 seconds pass, the targeted controller does not respond to the initiating controller, then the switchover errors out with connected time out Error 1 Extended Error 203 . An example of a connected message would be CIP data table read-and-write messages after a connection has been established. •  Uncached messages error out after 30 seconds if you have just initiated them because the intiating controller never received a reply to the forward-open request. The error is Error 1F Extended Error 204 , an unconnected time out. Examples of uncached messages would include CIP generic messages and messages captured during the connection process. |
|                                                                    | During qualification Cached messages run with no errors. A connection has been established. Connected, but uncached, messages or unconnected messages error out with Error 1 Extended Error 301, No Buffer Memory .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Configure Tags for an HMI

To monitor tags directly in the secondary controller (not typical), monitor from no more than 3 devices through a CNB module.

Monitor tags in a secondary controller only via:

- RSLogix 5000 programming software.
- Any method that does not try to create OPC optimized packets. Only a primary controller can create an OPC optimized packet.

## Estimate the Crossload Time of a Program

You can estimate the crossload time of a program in a redundant controller.

<!-- image -->

By lowering the amount of time you spend crossloading data, you can reduce your scan time.

Perform this procedure to gauge the time a project spends crossloading data.

## Before You Begin

## Crossload Time Estimations

| Consideration Details                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The controller crossloads data at the end of every program.                                                                 | The primary controller stops at the end of every program to crossload fresh data to the secondary controller. This keeps the secondary controller up to date and ready to take over. It also increases the scan time when compared to a nonredundant system. Execute Program in Primary Controller Crossload Results to Secondary Controller Scan Time of Program                                                    |
| The crossload time depends on how much data changed.                                                                        | The length of time for the crossload depends on the how much data the primary controller has to crossload. •  The primary controller crossloads any tag to which an instruction wrote a value (even the same value) since the last crossload. •  Crossloading also requires a small amount of overhead time to tell the secondary controller which program the primary controller is executing.                      |
| In a redundant system, a ControlLogix5561, 5562, or 5563 controller is up to 30% faster than a ControlLogix5555 controller. | The scan time improvement of ControlLogix5561, 5562, and 5563 controllers is less in a redundant system is than in a nonredundant system. •  Even though the ControlLogix5561, 5562, and 5563 controllers execute logic faster, they must still crossload data. •  Given the same project and redundant system, a ControlLogix5561, 5562, or 5563 controller is up to 30% faster than a ControlLogix5555 controller. |

## Actions

Action Details

1. Get the size of your crossload data. Use a Get System Value (GSV) instruction to read the REDUNDANCY object.

| For this information Get this attribute Data                                                     |                       | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------|-----------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| •  Size of the last crossload •  Size of the last crossload if you had a secondary chassis       | LastDataTransfer Size |        | DINT This attribute gives the size of data that was or would have been crossloaded in the last scan. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. Is there a synchronized secondary chassis? •  Yes — This gives number of DINTs that was crossloaded in the last scan. •  No — This gives number of DINTs that would have been crossloaded in the last scan.                                      |
| •  Size of the biggest crossload •  Size of the biggest crossload if you had a secondary chassis | MaxDataTransfer Size  |        | DINT This attribute gives the biggest size of the LastDataTransfer Size attribute. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. •  To reset this value, use an SSV instruction with a Source value of 0. Is there a synchronized secondary chassis? •  Yes — This gives biggest number of DINTs that was crossloaded. •  No — This gives biggest number of DINTs that would have been crossloaded. |

See Logix5000 Controllers General Instructions Reference Manual, publication 1756-RM003, for more information on the GSV and SSV instructions.

2. Estimate the crossload time. Which controller do you have?

·

·

·

·

If ControlLogix5555, then crossload time = (0.0015 ms * DINTs) + 1 ms overhead

If ControlLogix5561, then crossload time = (0.0013 ms * DINTs) + 1 ms overhead

If ControlLogix5562, then crossload time = (0.0013 ms * DINTs) + 1 ms overhead

If ControlLogix5563, then crossload time = (0.0013 ms * DINTs) + 1 ms overhead where DINTs is the size of tag data to be crossloaded, measured in 4-byte words.

## Minimize Scan Time

To minimize a project's scan time, perform this procedure.

<!-- image -->

Do not try to get the scan time of a ControlLogix redundancy project down below about 20 milliseconds. At very low scan times, crossload data becomes a bigger performance burden. This burden limits the minimum scan time.

<!-- image -->

<!-- image -->

|                                                                 | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Use a few large programs instead of a lot of small programs. | The controller stops at the end of every program to crossload data. So the more programs that you have, the more the controller stops to crossload. And it often ends up crossloading the same data many times. To cut down the number of crossloads: •  Use only one or a few programs. •  Divide each program into whatever number of routines makes the most sense. A routine does not cause a crossload. •  Use the main routine of each program to call the other routines of the program. •  If you want to use several tasks for different scan periods, put only one program in each task. Remember that each program adds a crossload. So use only one or a few tasks. This is better Than this 白Tasks MainTask  MainProgram Program Tags MainRoutine added_startup ATR1_S1_Get_Data ATR1_S1_Send_Data ATR1_53_Process_Data ATR2_S1_Get_Data ATR2_S1_Send_Data ATR2_53_Process_Data ATRControl Beacons CalMerge Control Count_Reset CtrlZone_02 CtrlZone_11 Tasks 白皂 MainTask MainProgram Program Tags 鑫自自自自目 MainRoutine Count_Reset MDS_Alarms MDS_PLC_Clock MD5_Status SCANTIME_MONITOR ATR_Comms HLCComms ME_Comms |

<!-- image -->

|                                                                       | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                       | 2. Delete unused tags. This reduces the size of the tag database. A smaller database takes less time to crossload. To delete unused tags: A. Open one of the tags folders. D. From the Edit menu, choose Select All. B. Click Edit Tags. C. From the Show list, select Unused. Controller Tags -My_Project(controller) Scope: My_Project(controlle Show: Unused Sort: Tag N. ag Name 色 Type Description 米 Monitor Tags EditTags                                                  |
| 3. Use arrays and user-defined data types instead of individual tags. | When you create a tag, the controller always sets aside at least 4 bytes (32 bits) of memory. The controller does this even if the tag needs only 1 bit. When you create an array or a user-defined data type, the controller packs smaller data types into 4-byte (32-bit) words. This means the controller has less data to crossload. This array of 32 BOOLs takes only 4-bytes. The controller crossloads only 4 bytes. Tag Name Alias For Base Tag Type ±-Bool_Array BOOL[32] |

Action Details

4. If you have already created individual tags, change them to aliases.

If you have already created individual tags, change them to aliases for elements of an array. Your logic points to the aliases. The controller crossloads the base array.

- A. Create an array.
- B. Change each individual tag to an alias for an element in the array.
- C. Keep pointing your logic to the individual tag names.
5. Keep user-defined data types as compact as possible.

| Tag Name     | 色 Alias For   | Base Tag      | Type     |
|--------------|----------------|---------------|----------|
| ±-Bool_Array |                |               | BO0L[32] |
| Bool_Tag_1   | Bool_Array[0]  | Bool_Array[0] | B00L     |
| Bool_Tag_2   | Bool_Array[1]  | Bool_Array[1] | BOOL     |
| Bool_Tag_3   | Bool_Array[2]  | Bool_Array[2] | BOOL     |

<!-- image -->

Put like data types together when you lay out a user-defined data type.

- Put all the BOOLs together.
- Put all the SINTs together.
- Put all the INTs together.

This data type takes 12 bytes. The BOOLs are together.

| Members:   | Data Type Size: 12 byte[s]   | Data Type Size: 12 byte[s]   | Data Type Size: 12 byte[s]   |
|------------|------------------------------|------------------------------|------------------------------|
| Name       | Data Type                    | Style                        | Description                  |
| Bool_1     | BOOL                         | Decimal                      |                              |
| Bool_2     | BOOL                         | Decimal                      |                              |
| Bool_3     | BOOL                         | Decimal                      |                              |
| Dint_1     | DINT                         | Decimal                      |                              |
| Dint_2     | DINT                         | Decimal                      |                              |
| 米         |                              |                              |                              |

This data type takes 20 bytes. The BOOLs are spread out.

| Members:   | Members:   | Data Type Size: 20 byte[s)   | Data Type Size: 20 byte[s)   | Data Type Size: 20 byte[s)   |
|------------|------------|------------------------------|------------------------------|------------------------------|
|            | Name       | Data Type                    | Style                        | Description                  |
|            | Boo_1      | BOOL                         | Decimal                      |                              |
|            | Dint_1     | DINT                         | Decimal                      |                              |
|            | Bool_2     | BOOL                         | Decimal                      |                              |
|            | Dint_2     | DINT                         | Decimal                      |                              |
|            | Bool_3     | BOOL                         | Decimal                      |                              |
| 米         |            |                              |                              |                              |

This is better

Than this

Action Details

6. Keep code as compact as possible. Avoid checking the same conditions many times. Each instruction adds scan time to your controller.

## This is better

This rung checks Bool\_B and Bool\_C only once each scan.

<!-- image -->

## Than this

This rung checks Bool\_B and Bool\_C twice each scan. One or two instructions do not add much scan time. But if you do this often, the extra instructions add up to a much longer scan time.

<!-- image -->

| Action Details                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7. Execute code only when you need it. The controller crossloads a tag anytime an instruction writes a value to the tag. This happens even if the value stays the same. |

- Many instructions write a value whenever they run. For example, instructions such as OTL, OTU, and many instructions with Destination operands write a value each time the rung-condition-in is true.
- Whenever an instruction writes a value, the controller marks the value for the next crossload. This occurs even if the instruction wrote the same value that was previously in the tag.

If you execute an instruction only when you need to, you reduce the amount of crossload data. This reduces scan time. To limit the execution of an instruction:

- make a rung false when you do not need to execute its instructions.
- divide your logic into subroutines and call each subroutine only when needed.
- run noncritical code every few scans instead of every scan.

## This is better

The ADD instruction runs only when the controller gets new data (New\_Data = on). And Dest\_Tag crossloads only when the ADD instruction produces a new value.

<!-- image -->

## Than this

The ADD instruction writes the sum of Tag\_1 + Tag\_2 to Dest\_Tag each time the rung executes. The controller crossloads Dest\_Tag every scan, even if Tag\_1 and Tag\_2 stay the same.

<!-- image -->

Action Details

8. Group your data by how often you need it. To update the secondary controller, the primary controller divides its memory into blocks of 256 bytes. Anytime an instruction writes a value, the primary controller crossloads the entire block that contained the value. For example, if your logic writes only 1 BOOL value to a block, the controller crossloads the entire block (256 bytes).

To minimize crossload time, group your data by how often you need it.

Suppose that you have some DINTs that you use only as constants to initialize your logic. You have some BOOLs that you update every scan. And you have some REALs that you update every second.

## This is better

One user-defined data type for the BOOLs. The controller crossloads these 4 bytes every scan.

One user-defined data type for the DINTs. The controller crossloads these 12 bytes only once.

One user-defined data type for the REALs. The controller crossloads these 12 bytes every second.

## Than this

One user-defined data type for all the data. The controller crossloads these 28 bytes every scan.

<!-- image -->

<!-- image -->

| Tag Name 色         | Type        |
|---------------------|-------------|
| -My_Data            | My_Data_UDT |
| -My_Data.Constant_1 | DINT        |
| -My_Data.Constant_2 | DINT        |
| -My_Data.Cosntant_3 | DINT        |
| My_Data.Bool_1      | BOOL        |
| My_Data.Bool_2      | BOOL        |
| My_Data.Bool_3      | BOOL        |
| My_Data.Real_1      | REAL        |
| My_Data.Real_2      | REAL        |
| My_Data.Real_3      | REAL        |

To keep your logic as efficient as possible, use the DINT data type instead of the SINT or INT data types.

A ControlLogix controller usually works with 32-bit values (DINTs or REALs). If you use a SINT or INT value:

- the controller usually changes a SINT or INT value to a DINT or REAL value before it uses the value.
- if the destination is a SINT or INT tag, the controller usually changes the value back to a SINT or INT value.
- you do not have to program the controller to change values to or from SINTs or INTs. The controller does it automatically. But it takes extra execution time and memory.
9. Use DINT tags instead of SINT or INT tags

## Maintain Data Integrity During a Switchover

The redundancy system guarantees a bumpless switchover for any logic in the highest priority task. In some cases, a switchover may make lower priority tasks repeat part of their scan. This has to do with how data crossloads from the primary controller to the secondary controller.

As the primary controller executes its logic, it updates the secondary controller at the end of every program.

## Switchover Overview

<!-- image -->

- A. This data is sent to the secondary controller:
- Data from the program in the higher priority task.
- Data from the first part of the program in the lower priority task.
- B. Execution returns to the program in the lower priority task.
- C. Data from the second part of the program in the lower priority task is sent to the secondary controller.

When a switchover interrupts the execution of the primary controller, the secondary controller reexecutes an interrupted program from the beginning of the program.

## Interrupted Switchover

<!-- image -->

- This portion of the task is not executed during this scan.
- Instructions executing at the time of the switchover do not complete in this scan.
- A. This data is sent to the secondary controller:
- Data from the program in the higher priority task.
- Data from the first part of the program in the lower priority task.
- B. Execution returns to the program in the lower priority task.
- C. The secondary controller:
- starts the scan at the beginning of the program that was in progress in the primary controller during the switchover.
- uses the data from the last update.

In this example, the secondary controller starts the scan with an image of the data as it was during the primary controller's last scan.

To prevent a scan from repeating after a switchover:

- look for array shift instructions.
- look for scan-dependent logic.
- take preventative actions

## Look for Array Shift Instructions

These instructions might corrupt data during a switchover:

- BSL
- BSR
- FFU

Because these instructions shift data within an array, an interruption by a higher priority task and a subsequent switchover leaves the data with an incomplete shift.

- If a higher priority task interrupts one of these instructions, the partially shifted array values are sent to the secondary controller.
- If a switchover occurs before the instruction completes its execution, data remains only partially shifted.
- The secondary controller starts its execution at the beginning of the program. When it reaches the instruction, it shifts the data again.

## Look for Scan-Dependent Logic

A rung that must read the output of another rung during the same scan might miss a scan during a switchover.

<!-- image -->

- A. The CTU instruction counts each scan.
- B. The EQU instruction uses the count of each scan (scan\_count.ACC).

- C. If a higher priority task interrupts the logic, the value of scan\_count.ACC is sent to the secondary controller at the end of the program in the higher priority task.
- D. If a switchover occurs before the EQU instruction, the secondary controller starts its execution at the beginning of the program. The EQU instruction misses the last value of scan\_count.ACC.

## Take Preventative Actions

If logic seems susceptible to an upset during a switchover, either place susceptible logic in the highest priority task, or, if the logic must remain in a lower priority task, take one of these actions:

- Use UID and UIE Instruction Pairs.
- Buffer critical data.

Place Susceptible Logic in the Highest Priority Task

This prevents the controller from sending any data to the secondary controller until the program finishes.

If a switchover occurs during the program, the secondary controller repeats the scan using the same starting data.

## Use UID and UIE Instruction Pairs

Bound critical rungs with UID and UIE instruction pairs. This prevents the higher priority task form interrupting the scan-dependent logic.

<!-- image -->

## Buffer Critical Data

This example shows the use of a buffer together with a BSL instruction.

<!-- image -->

1. The COP instruction moves the data into a buffer array.
2. The BSL instruction uses the data in the buffer. If a switchover occurs, the source data (array tag) remains unaffected.
3. The CPS instruction updates array tag. Since higher priority tasks cannot interrupt a CPS instruction, the instruction keeps the integrity of the data.

## Determine the Status of Your Redundant System

You can write code that determines the status of your redundant system.

Perform this procedure to:

- show system status on an HMI screen.
- condition code to execute based on system status.
- get diagnostic information to troubleshoot a system.

## Actions

Use a Get System Value (GSV) instruction to read the attributes of the REDUNDANCY object. See Appendix C for a list of attributes.

## Example 1: Ladder Diagram

Get the ID of the primary chassis. The primary chassis always runs the code.

Store the ID in the Chassis\_ID\_Now tag. Chassis\_ID\_Now is a DINT.

<!-- image -->

## Example 2: Structured Text

<!-- image -->

## Check Your Work

Use the Redundancy tab of the Controller Properties window to check the code attributes. It does not show all the attributes, but it shows the more common attributes.

1. Download and run your project.

<!-- image -->

## Additional Resources

For more information, consult these sources.

- Appendix C
- Logix5000 Controllers General Instructions Reference Manual, publication 1756-RM003

## Condition Logic to Run After a Switchover

You can condition a section of your logic to run after a switchover.

Follow these examples to create logic in preparation for a possible switchover.

## Example 1: Ladder Diagram

Get the ID of the primary chassis. That is always the chassis that runs the code.

Store the ID in the Chassis\_ID\_Now tag.

Chassis\_ID\_Now — DINT.

<!-- image -->

If this is the first scan then

Set the last value of the chassis ID = the ID of this chassis.

<!-- image -->

If the chassis ID changes, a switchover happened.

If a switchover occurs, then

1. Turn on the Switchover\_Happened bit.
2. Set the last value of the chassis ID = the ID of this chassis.

Switchover\_Happened — BOOL.

<!-- image -->

Continued on next page

If Switchover\_Happened = on, then

1. Execute the instructions that you want to execute after a switchover.
2. Turn off the Switchover\_Happened bit.

<!-- image -->

## Example 2: Structured Text

```
//Get the ID of the primary chassis. //That is always the chassis that runs the code. //Store the ID in Chassis_ID_Now. //Chassis_ID_Now -- DINT. GSV(REDUNDANCY,,PhysicalChassisID,Chassis_ID_Now); //If this is the first scan //Then set the last value of the chassis ID = the ID of this chassis //Chassis_ID_Last -- DINT. If S:FS then Chassis_ID_Last := Chassis_ID_Now; End_If; //If the chassis ID changes, a switchover happened. //If a switchover happens then //Turn on the Switchover_Happened bit. //Set the last value of the chassis ID = the ID of this chassis //Switchover_Happened -- BOOL comment comment comment comment code
```

## Send a Message to the SRM

```
If Chassis_ID_Now <> Chassis_ID_Last then Switchover_Happened := 1; Chassis_ID_Last := Chassis_ID_Now; End_If; //If Switchover_Happened = on //Then //Execute the instructions that you want to execute after a switchover. //Turn off the Switchover_Happened bit. If Switchover_Happened then Put your statements here. Switchover_Happened := 0; End_If;
```

You can let your logic initiate actions in the SRM.

Perform this procedure to:

- Initiate a switchover.
- disqualify the secondary controller.
- synchronize the secondary controller.
- set the clock of the SRM module.

## Before You Begin

Before sending a message to an SRM, make sure that:

- the SRM is configured for program control.
- the message is unconnected.

<!-- image -->

<!-- image -->

## Actions

Use this table to configure a message to an SRM module.

## Configuring a Message to an SRM

|                                                              | If you want to On this tab For this item Type or select                                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Initiate a switchover Configuration Message Type CIP Generic |                                                                                                                                    |
| Initiate a switchover Configuration Message Type CIP Generic | Service Code 4e                                                                                                                    |
| Initiate a switchover Configuration Message Type CIP Generic | Class name bf                                                                                                                      |
| Initiate a switchover Configuration Message Type CIP Generic | Instance name 1                                                                                                                    |
| Initiate a switchover Configuration Message Type CIP Generic | Attribute name Leave blank                                                                                                         |
| Initiate a switchover Configuration Message Type CIP Generic | Source INT tag with a value of 1                                                                                                   |
| Initiate a switchover Configuration Message Type CIP Generic | Num. Of Elements 2                                                                                                                 |
| Initiate a switchover Configuration Message Type CIP Generic | Destination Leave blank                                                                                                            |
| Initiate a switchover Configuration Message Type CIP Generic | Communication Path 1, slot_number where: slot_number is the left-hand slot number of the 1757-SRM module.                          |
| Initiate a switchover Configuration Message Type CIP Generic | Connected check box. Leave the Connected check box clear (unchecked). You can send only unconnected messages to a 1757-SRM module. |
| Disqualify the secondary controller                          | Configuration Message Type CIP Generic                                                                                             |
| Disqualify the secondary controller                          | Service Code 4d                                                                                                                    |
| Disqualify the secondary controller                          | Class name bf                                                                                                                      |
| Disqualify the secondary controller                          | Instance name 1                                                                                                                    |
| Disqualify the secondary controller                          | Attribute name Leave blank                                                                                                         |
| Disqualify the secondary controller                          | Source INT tag with a value of 1                                                                                                   |
| Disqualify the secondary controller                          | Num. Of Elements 2                                                                                                                 |
| Disqualify the secondary controller                          | Destination Leave blank                                                                                                            |
| Disqualify the secondary controller                          | Communication Path 1, slot_number where: slot_number is the left-hand slot number of the 1757-SRM module.                          |
| Disqualify the secondary controller                          | Connected check box. Leave the Connected check box clear (unchecked). You can send only unconnected messages to a 1757-SRM module. |

## Configuring a Message to an SRM (Continued)

|                                      | If you want to On this tab For this item Type or select                                                                            |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Synchronize the secondary controller | Configuration Message Type CIP Generic                                                                                             |
| Synchronize the secondary controller | Service Code 4c                                                                                                                    |
| Synchronize the secondary controller | Class name bf                                                                                                                      |
| Synchronize the secondary controller | Instance name 1                                                                                                                    |
| Synchronize the secondary controller | Attribute name Leave blank                                                                                                         |
| Synchronize the secondary controller | Source INT tag with a value of 1                                                                                                   |
| Synchronize the secondary controller | Num. Of Elements 2                                                                                                                 |
| Synchronize the secondary controller | Destination Leave blank                                                                                                            |
| Synchronize the secondary controller | Communication Path 1, slot_number where: slot_number is the left-hand slot number of the 1757-SRM module.                          |
| Synchronize the secondary controller | Connected check box. Leave the Connected check box clear (unchecked). You can send only unconnected messages to a 1757-SRM module. |
| Set the clock of the SRM module      | Configuration Message Type CIP Generic                                                                                             |
| Set the clock of the SRM module      | Service Code 10                                                                                                                    |
| Set the clock of the SRM module      | Class name 8b                                                                                                                      |
| Set the clock of the SRM module      | Instance name 1                                                                                                                    |
| Set the clock of the SRM module      | Attribute name 1                                                                                                                   |
| Set the clock of the SRM module      | Source  WallClockTime[0] where: WallClockTime is a DINT[2] array that stores the CurrentValue of the WALLCLOCKTIME object.         |
| Set the clock of the SRM module      | Num. Of Elements 8                                                                                                                 |
| Set the clock of the SRM module      | Destination Leave blank                                                                                                            |
| Set the clock of the SRM module      | Communication Path 1, slot_number where: slot_number is the left-hand slot number of the 1757-SRM module.                          |
| Set the clock of the SRM module      | Connected check box Leave the Connected check box clear (unchecked). You can send only unconnected messages to a 1757-SRM module.  |

## Download the Project to the Primary Controller

You only have to download the project to the primary controller. When the secondary controller is synchronized, the system automatically crossloads the project to the secondary controller.

## IMPORTANT

If the secondary chassis becomes disqualified after you download the project, make sure that you:

- configured the project for the right type of controller.
- enabled redundancy.

See Plan for Online Edits on page 65.

1. Open or create the RSLogix 5000 project for the controller.
2. From the File menu, choose Save.
3. From the Communications menu, choose Who Active.

<!-- image -->

Before proceeding to download your project, do not try to match your project to your controller.

- a. Right-click on your controller and select Properties.

<!-- image -->

## b. Choose Advanced.

<!-- image -->

IMPORTANT

If you match your downloaded project to your controller, you tie your project to your controller's serial number. If you then switch over to a controller in a different chassis, your project will not match the new controller's serial number, disabling the controller functions originally specified under the Advanced tab of Controller Properties

4. Browse to the controller in the primary chassis.
- A. Open a branch in one of these ways:
- Double-click it.
- Click its + sign.
- Select it and press the → key.
- B. Find the primary chassis. Its communication module uses the address that you gave it.
- C. Find the controller.
5. Select the controller and choose Download.

<!-- image -->

The Download diaglog opens.

6. Choose Download.

## Schedule a ControlNet Network

<!-- image -->

Before you schedule a ControlNet network, turn on the power to both redundant chassis. If you schedule a ControlNet network while the secondary chassis is off, the keeper signature of a CNB module may not match its partner, and the secondary chassis will fail to synchronize.

To schedule a ControlNet network:

- schedule a new network.
- update the schedule of an existing network.
- check the keepers.
- save the project for each controller.

## Schedule a New Network

To schedule a new network, perform this procedure.

1. Turn on the power to each chassis.
2. Start RSNetworx for ControlNet software.
3. From the File menu, choose New.
4. From the Network menu, choose Online.
5. Select your ControlNet network and choose OK.
6. Select the Edits Enabled check box.
7. From the Network menu, choose Properties.
8. From Network Parameters, type or select these parameters.
9. Choose OK.

| In this box Specify                                                                            |
|------------------------------------------------------------------------------------------------|
| Network Update Time Repetitive time interval in which data is sent over the ControlNet network |
| Max Scheduled Address Greatest node number to use scheduled communications on the network      |
| Max Unscheduled Address Greatest node number that you will use on the network                  |
| Media Redundancy Channels in use                                                               |
| Network Name Name for the network                                                              |

10. From the Network menu, choose Single Pass Browse.
11. From the File menu, choose Save.
12. Type a name for the file that stores the network configuration, then choose Save.
13. Select the Optimize and rewrite Schedule for all Connections button (default) and choose OK.

## Update the Schedule of an Existing Network

To update the schedule of an existing network, perform this procedure.

1. Turn on the power to each chassis.
2. Start RSNetworx for ControlNet software.
3. From the File menu, choose Open.
4. Select the file for the network and choose Open.
5. From the Network menu, choose Online.
6. Select the Edits Enabled check box.
7. From the Network menu, choose Properties.
8. From Network Parameters, update these parameters.
9. Choose OK.
10. From the Network menu, choose Single Pass Browse.
11. From the File menu, choose Save.
12. Select the Optimize and rewrite Schedule for all Connections button and choose OK.

| In this box Specify                                                                       |
|-------------------------------------------------------------------------------------------|
| Max Scheduled Address Greatest node number to use scheduled communications on the network |
| Max Unscheduled Address Greatest node number to use on the network                        |

## Check the Keepers

To check the keepers, perform this procedure.

On a ControlNet network, each keeper must:

- take over the keeper duties if the current keeper drops off the network.
- use the same configuration regardless of which keeper first comes online after a major network disturbance, such as a cable short or system power cycle.

After you schedule your ControlNet networks:

<!-- image -->

| 1. 2.                                          | 1. 2.      | 1. 2.   |
|------------------------------------------------|------------|---------|
| Keeper Capable Node Active Keeper Valid Keeper |            |         |
| Offline file                                   |            |         |
|                                                | 01 No Yes  |         |
|                                                | 02 Yes Yes |         |

1. Make sure the network shows all keeper capable nodes.
2. Make sure that each node is a valid keeper.

For more information, see Update a Keeper Signature on page 107.

## Save the Project for Each Controller

To save the project for each controller, perform this procedure.

After your schedule your ControlNet networks, save the online project of each controller. This lets you download a project in the future without having to reschedule the networks.

For each controller (redundant and nonredundant) on a ControlNet network:

1. Go online to the controller.
2. Save the project.

## Set Task Watchdog Times

To give a redundant controller longer watchdog times than a nonredundant controller, perform this procedure.

- After a switchover, the secondary controller starts the scan at the beginning of the program that was running in the primary controller at the time of the switchover.
- The watchdog timer for the task that has the program, however, is not reset.
- A major fault happens (type 6, code 1) if the watchdog timer has too little time to completely rescan the program.

|                                              | Action Details                                                                                                                                                                                                                              |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Set the minimum watchdog time for a task. | Use this formula to set the minimum watchdog time for a task: Minimum watchdog time = (2 * maximum_scan_time) + 150 ms where: Maximum_scan_time is the maximum scan time for the entire task when the secondary controller is synchronized. |

<!-- image -->

<!-- image -->

## Notes:

## Introduction

<!-- image -->

## Maintain and Troubleshoot the System

This chapter explains how to commission, maintain, and troubleshoot your redundancy system.

| Simultaneous power of redundant chassis pair may bump another redundant chassis pair off the EtherNet/IP network   | Under this combination of conditions (all must apply), duplicate IP addresses on your EtherNet/IP network will cause you to lose communication with a redundant chassis pair over that EtherNet/IP network. •  You have multiple pairs of redundant chassis on the same EtherNet/IP network. For example, pair 1 and pair 2. •  The IP addresses of one pair of redundant chassis is the same as another pair of redundant chassis. For example, pair 1 = 10.10.10.10 and pair 2 = 10.10.10.10. •  A redundant chassis pair with the conflict (both chassis that make up the pair) simultaneously powers up. For example, both chassis of pair 2 power up at the same time. When this occurs the newly powered up chassis use the IP address. The redundant chassis pair that was previously communicating at that IP address stops communicating on the network. For example, when pair 2 powers up at 10.10.10.10, pair 1 stops communicating on the network.   |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|                                                                                                                                               | If you want to Then see this section Page     |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| •  Find the cause of an unplanned switchover •  Find why secondary chassis became disqualified                                                | Diagnose a Switchover or Disqualification 104 |
| Find why the secondary controller fails to synchronize Troubleshoot a Failure to Synchronize 105                                              |                                               |
| See if the keeper signature of a CNB module is stopping the secondary chassis from synchronizing                                              | Update a Keeper Signature 107                 |
| See if a computer is stopping the secondary chassis from synchronizing                                                                        | Edit Sessions in Progress 108                 |
| Look through a log of events to see why system switched over or failed to synchronize                                                         | Interpret the SRM Event Log 109               |
| Export specific events from the SRM event log and view them in software such as Microsoft Excel                                               | Export the SRM Event Log 115                  |
| Initiate the synchronization process Manually Synchronize the Chassis 118                                                                     |                                               |
| •  Determine why it takes a very long time to synchronize the secondary controller •  Determine why communication with your HMIs is very slow | Optimize Communication 119                    |
| •  Determine why OPC communication has errored or failed •  Determine why you are unable to create tags or edit logic while online            | Check the Allocation of Unused Memory 123     |

103

|                                                                                                                                                                        | If you want to Then see this section Page                        |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-----|
| •  Determine the CPU usage of a CNB module •  Reduce the CPU usage of a CNB module                                                                                     | Adjust CPU Usage for a CNB Module 123                            |     |
| •  Store a project to the nonvolatile memory of a controller in a redundant system •  Load a project into the controller from the nonvolatile memory of the controller | Store or Load a Project Using Nonvolatile Memory                 | 126 |
| Store an updated project and firmware to the nonvolatile memory of the controller while the process is running                                                         | Store a Project to Nonvolatile Memory While a Process Is Running | 128 |

## Diagnose a Switchover or Disqualification

<!-- image -->

To find and fix the cause of an unplanned switchover or loss of synchronization, perform this procedure when:

- an unplanned switchover happens.
- a chassis that was synchronized becomes disqualified.

## Actions

- Do the 1756-CNB/D/E or 1756-CNBR/D/E modules in the primary chassis show PwQS?
- Yes — Go to Interpret the SRM Event Log on page 109.
- No — Go to step 2.
- Does any module in the primary chassis show PwNS?
- Yes — Go to step 2.
- No — Go to step 3.
1. Use this table to troubleshoot the secondary chassis.

| If the secondary chassis And each communication module in the primary chassis   | And a secondary communication module has a   | Then                                                                                               |
|---------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------|
| Has power Has a matching partner in the secondary chassis                       |                                              | Red OK light A. Power cycle the module. B. Replace the module if the Red OK light keeps coming on. |
| Has power Has a matching partner in the secondary chassis                       |                                              | Green OK light Check the 1757-SRC cable for a proper connection.                                   |
| Does not have a matching partner in the secondary chassis                       | ⇒                                            | Install a matching module.                                                                         |
| Does not have power  ⇒                                                          | Does not have power  ⇒                       | Restore the power.                                                                                 |

## Troubleshoot a Failure to Synchronize

2. Wait several minutes for the system to try to synchronize. What do the CNB modules in the primary chassis show?
- PwQS — Stop. Your system is synchronized.
- PwDS — Go to step 3.
3. Use this table to troubleshoot the secondary chassis.
4. Wait several minutes for the system to try to synchronize. Do the CNB modules in the primary chassis show PwQS?
- Yes — Stop. Your system is synchronized.
- No — Go to Troubleshoot a Failure to Synchronize on page 105.

| If the SRM module has a   | And a secondary CNB module   | And a secondary controller has a   | Then                                                                                                                                                                                   |
|---------------------------|------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Green OK LED Indicator    |                              |                                    | Does not show NET ERR Flashing Red OK light Clear the major fault of the controller. It is possible that you have to clear the fault on both the primary and secondary controllers.    |
|                           |                              |                                    | Solid Red OK light A. Cycle the power to the chassis. B. If the OK light remains solid red, replace the controller and flash the controller with the appropriate revision of firmware. |
|                           |                              | Solid Green OK light Go to step 4. |                                                                                                                                                                                        |
|                           | Shows NET ERR                | ⇒                                  | Check all ControlNet taps, connectors, and terminators for proper connections.                                                                                                         |
| Red OK LED Indicator      | ⇒                            | ⇒                                  | A. Cycle the power to the chassis. B. If the OK light of the SRM module remains solid red, contact your local distributor or Rockwell Automation representative.                       |

To troubleshoot a failure to synchronize, perform this procedure.

## IMPORTANT

- If the steps in this section do not correct the situation, check the usage of the CNB modules. See Adjust CPU Usage for a CNB Module on page 123.
- If the chassis still doesn't synchronize, try to manually synchronize it. See Manually Synchronize the Chassis on page 118.

<!-- image -->

1. Observe the 1756-CNB/D/E or 1756-CNBR/D/E modules in the primary chassis.
2. Observe the CNB modules in the secondary chassis.

| Primary CNB Front panel If It means So do this   |                                                                              |                                               |
|--------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------|
| Look here.                                       | PwQS Primary with Synchronized (Qualified) Secondary                         | Stop. The redundant chassis are synchronized. |
| Look here.                                       | PwDS Primary with Disqualified Secondary Go to step 2. A problem exists. The | redundant chassis are not synchronized.       |
| Look here.                                       | PwNS Primary with No Secondary                                               | redundant chassis are not synchronized.       |

| Front panel If the display   |                                                                                                       | Then So check                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Secondary CNB                | !Cpt The CNB modules in the primary and secondary chassis do not match in some way.                   | •  The CNB modules in the primary and secondary chassis are the same revision, or the CNB modules in the primary chassis are series D and those in the secondary chassis are series E. •  Each CNB module has a partner in the same slot in the other redundant chassis. •  Each pair of CNB modules (one in each chassis) is set to the same node address. •  Each module has compatible firmware. •  All CNB modules in each redundant chassis are valid keepers. See Update a Keeper Signature on page 107.                                            |
|                              | CMPT Some module other than this CNB module does not match between the primary and secondary chassis. | •  Each module has a partner in the same slot in the other redundant chassis. •  Each pair of controllers (one in each chassis) has the same memory board (for example, 1756-L55M14). •  Each module has compatible firmware. •  The RSLogix 5000 project is configured for the right type of controller and redundancy is enabled. See Configure a Controller for Redundancy on page 68. •  The Module Configuration window for the 1757-SRM module does not list any reasons for the failure to synchronize. See Edit Sessions in Progress on page 108. |
|                              | DUPL NODE More than one device on your ControlNet network is using the same node number.              | •  No other device on the ControlNet network is set to the address of the CNB modules plus one. •  For example, if the CNB modules are set to 3, no other device should be set to 4. •  The 1757-SRCx cable is connected to both SRM modules.                                                                                                                                                                                                                                                                                                             |
|                              | NET ERR The ControlNet media is not completely connected.                                             | •  All ControlNet taps, connectors, and terminators are connected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Update a Keeper Signature

<!-- image -->

To see if the keeper signature of a CNB module is stopping the secondary chassis from synchronizing, you need to update the keeper signature.

To update the keeper signature, perform this procedure when a secondary chassis will not synchronize and its CNB modules show !CPT.

## Before You Begin

The secondary chassis will not synchronize if the keeper signature of a CNB module does not match its partner. This happens if you schedule the ControlNet network while the secondary chassis is off or if the CNB module was previously configured in a different network.

## Actions

1. Start RSNetWorx for ControlNet software. Has this network been scheduled before?
2. From the Network menu, choose Keeper Status.
3. Make sure the list contains all your keeper capable nodes. This includes the CNB modules in the secondary chassis.

| If Then                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------|
| No A. From the File menu, select New. B. From the Network menu, select Online. C. Select your ControlNet network and choose OK.      |
| Yes A. From the File menu, select Open. B. Select the file for the network and choose Open. C. From the Network menu, select Online. |

<!-- image -->

## Edit Sessions in Progress

<!-- image -->

4. Make sure that each node has a valid keeper signature.
5. Choose Close.

| If the Valid Keeper column shows Then        |
|----------------------------------------------|
| Yes The node has a valid keeper signature.   |
| No Select the node and choose Update Keeper. |

To see if a computer is stopping the secondary chassis from synchronizing, you must see if an edit session is in progress.

To edit sessions in progress, perform this procedure when a secondary chassis will not synchronize and the CNB modules in the secondary chassis show CMPT.

## Actions

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the branches of your network until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. AB_ETH-2,Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane,1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 10.88.88.147, 1756-E Remove ①AB_VBP-1,1789-A17AVir Driver Diagnostics Configure Driver Device Properties |

| 3. Look for the reason.   |                                                                                    | If Then                                         |
|---------------------------|------------------------------------------------------------------------------------|-------------------------------------------------|
|                           | Another computer is editing the project in the controller.                         | Stop the edit session.                          |
|                           | The project contains test edits. Untest the edits.                                 |                                                 |
|                           | The Nonvolatile Memory Load/Store dialog of the controller is open.                | Close the Nonvolatile Memory Load/Store dialog. |
|                           | You tried to synchronize the chassis while downloading a project at the same time. | Wait for the download to finish.                |

<!-- image -->

Interpret the SRM Event Log To determine why a system switched over or failed to synchronize,
ihSRM l you must interpret the SRM event log.

To interpret the SRM event log, perform this procedure when:

- a switchover happens but your system synchronizes again.
- you have already tried to use the hardware lights to find why your system will not synchronize.

## Before You Begin

The SRM clock is accurate only if you:

- initially set it after you installed your system.
- reset it after any power loss to both chassis.

## Actions

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the network branches until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. 品AB_ETH-2,Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane,1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 口 02, 1756-EWEB/A 05,1757-5RM 10.88.88.147, 1756-E Remove  AB_VBP-1, 1789-A17/A Vir Driver Diagnostics Configure Driver Device Properties |

2. Go to the event log. Click Event Log.

<!-- image -->

Action Details

3. Look through the events of the secondary chassis for a substantial change in log times.
- A. Start with the secondary chassis.
- The lower list is the secondary chassis.
- The cause of the switchover probably happened to secondary chassis while it was the primary chassis.
- B. Look for a change of months, days, or hours between the log times of events.
- Sometimes the difference is only minutes.
- The SRM logs only significant events. It does not log events while your system is running normally.
- C. Use the slot and module columns to find the module that caused the event.
- D. Go to Interpret SRM events on page 113 to interpret the description.

## Example

<!-- image -->

Here is a substantial change in the log time.

The slot, module, and description columns show that the 1756-EWEB module in slot 2 went lonely. That usually means it lost its network connection.

Action Details

4. Double-click and event for more information.

A. Double-click an event to see if it gives more information.

The Extended Information Definition dialog opens.

- B. Click OK when you are done to close the Extended Information Definition dialog.

## Example

<!-- image -->

5. If the secondary log does not show the cause, look at the primary log.

Sometimes you have to use both logs to find out what happened.

## Example

<!-- image -->

## Interpret SRM events

Use this table to interpret events recorded in the SRM's event log.

## SRM Event Descriptions

| Event Description Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autoqualification Trigger Something happened that caused the system to try and synchronize again. Double-click the event to see what happened.                                                                                                                                                                                                                                                                                                                                                                  |
| Blank Memories Rule A check to choose a primary chassis if both chassis power up at the same time. Suppose that the controllers in one chassis don't have projects while the controllers in the other chassis do have projects. In that case, the other chassis becomes primary.                                                                                                                                                                                                                                |
| Chassis Modules Rule A check to choose a primary chassis if both chassis power up at the same time. Suppose that one chassis has more modules than the other chassis. In that case, the chassis with the most modules gets the first chance to become primary. It becomes primary as long as the other chassis isn't more able to control the system.                                                                                                                                                           |
| Chassis Redundancy State changed to… The chassis changed to a different redundancy state. •  PwQS — Primary with qualified (synchronized) secondary partner •  QSwP — Qualified (synchronized) secondary with primary partner •  DSwP — Disqualified secondary with primary partner •  DSwNP — Disqualified secondary with no partner •  PwDS — Primary with disqualified secondary partner •  PwNS — Primary with no secondary partner •  PLU — Primary locked for update •  SLU — Secondary locked for update |
| Crossloading Error A module isn't able to get some information to its partner.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Disqualified Secondaries Rule A check to choose a primary chassis if both chassis power up at the same time. Suppose that the modules in one of the chassis powered down in a disqualified secondary state. In that case, the other chassis becomes primary.                                                                                                                                                                                                                                                    |
| Failed Modules Rule A check to choose a primary chassis if both chassis power up at the same time. Suppose that a module in one of the chassis is faulted but its partner module in the other chassis is not faulted. In that case, the other chassis becomes primary.                                                                                                                                                                                                                                          |
| Firmware Error The SRM has a problem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Improper Mode or Keyswitch Position A lock for update cannot be performed if the primary controller is faulted. A lock for update or locked switchover cannot be performed if the keyswitch on either controller is not in the REM position.                                                                                                                                                                                                                                                                    |
| Incompatible Application A lock for update cannot be performed if the project names or applications are not identical in the primary and secondary chassis.                                                                                                                                                                                                                                                                                                                                                     |
| Invalid Application A lock for update cannot be performed if test edits or SFC forces exist in the application.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Module Insertion The SRM now sees the module on the backplane. This means the module has either just powered up, just been put into the chassis, or just finished resetting. Double click the event to see the slot number of the module.                                                                                                                                                                                                                                                                       |
| Module Rejected Lock for Update Command from SRM A module (with a slot number specified in byte 0 of the extended status) rejected the lock-for-update command. See events from that module to determine the cause.                                                                                                                                                                                                                                                                                             |

| Event Description Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module Removal The SRM no longer sees a module on the backplane. This means that the module either experienced a nonrecoverable fault, was removed from the chassis, or was reset. Double-click the event to see the slot number of the module.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Modules Chassis State Rule A check to choose a primary chassis if both chassis power up at the same time. Suppose that the modules in one chassis are already in a primary state. In that case, that chassis becomes primary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| NRC Modules Rule A check to choose a primary chassis if both chassis power up at the same time. NRC stands for nonredundancy compliant. Suppose that a module in one of the chassis doesn't support redundancy and all the modules in the other chassis do support redundancy. In that case, the other chassis becomes primary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Partner not on same CNet link A primary CNB isn't able to communicate with the secondary CNB over the ControlNet network. This means there is either: •  a network problem such as noise, a poor connection, or a problem with the termination. •  a secondary CNB that isn't connected to the network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Powerdown Time Rule A check to choose a primary chassis if both chassis power up at the same time. If the two chassis powered down more than one second apart, the last chassis to power down gets the first chance at being primary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Program Fault A controller has a major fault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SRM OS Error The SRM has a problem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SRM Serial Number Rule A check to choose a primary chassis if both chassis power up at the same time. This is the final tie-breaker. The SRM with the lower serial number gets the first chance to become primary. It becomes primary as long as the other chassis isn't more able to control the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Standby Secondaries Rule A check to choose a primary chassis if both chassis power up at the same time. Since standby isn't available yet, this check always ends in a tie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SYS_FAIL_L Active A module has a nonrecoverable fault or lost its connection to the network. When that happens, the SYS_FAIL signal becomes true. The backplane of the chassis has a SYS_FAIL signal. Each module in the chassis uses this signal to indicate a problem. •  The signal is normally false (inactive), which means that all modules in the chassis are OK. •  A module turns the SYS_FAIL signal true (active) when the module has a nonrecoverable fault or it losses its connection to the network. Look for later events to find out what happened. •  If you see a Module Removal event shortly afterward, then a module has a nonrecoverable fault. Double-click the Module Removal event to see the slot number of the module. The SYS_FAIL signal may stay true until you cycle power or remove the faulted module. •  If you see a SYS_FAIL_L Inactive event within a few hundred milliseconds, then a cable is probably disconnected or broken. A communication module pulses the SYS_FAIL signal when the module loses its connection to the network. Look for a Transition to Lonely event to see which module lost its connection. |
| The partner RM has been connected The partner SRM powered up or become connected by the fiber-optic cable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Event Description Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The partner RM screamed The partner SRM lost power, has an unrecoverable fault, or was removed. An SRM has circuits that hold power long enough for it to send a message to its partner over the fiber-optic interconnect cable. The SRM sends the message even after you remove it from the chassis. This message is called a scream. The scream lets the partner SRM tell the difference between a broken fiber-optic interconnect cable and the power loss or removal of the primary SRM. •  If the fiber optic cable breaks, then there isn't a switchover. •  If the SRM loses power or is removed, then there is a switchover. |
| Transition to Lonely A communication module doesn't see any other devices on its network. This usually means that the network cable of the module is disconnected or broken. The event log shows Transition to Not Lonely when you reconnect the cable.                                                                                                                                                                                                                                                                                                                                                                              |
| Unknown Event The SRM configuration tool doesn't have a description for the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| WCT time change (> 1 second) The clock of the SRM changed. This happens when you: •  use the SRM configuration tool to set the clock. •  connect the SRM to another SRM that is already primary. The SRM synchronizes its clock to that of the primary SRM.                                                                                                                                                                                                                                                                                                                                                                          |

## Export the SRM Event Log

Once you have reviewed your SRM event log, you can export specific logged events from the SRM event log to a CSV or TXT file.

To export the SRM event log, perform this procedure, which specifically allows you to:

- look at the event log in spreadsheet software such as Microsoft Excel.
- send the event log to someone else.

## Before You Begin

The SRM configuration tool lets you export events from both the primary and the secondary chassis at the same time.

| Chassis ID   | Event   | Log  Time                   | 1015 Module   | Description                         |
|--------------|---------|-----------------------------|---------------|-------------------------------------|
| Chassis      |         | 12/2/2004 16:02:27:055      | 2 1756-EVVEB  | (69) Equally Able To Control        |
| Chassis      |         | 12/2/2004 16:02:27:050      | L 1757-SRM    | [1A]（ Chassis Redundancy State ch: |
| Chassis      | 743582  | 12/2/2004 16:02:26:967      | 2 1756-EVVEB  | [4A] Entered Qualification Phase 4  |
| Chassis B    | 743581  | 12/2/2004 16:02:26:917      | L 1757-SRM    | [2E] Qualification Complete         |
| Chassis A    | 5720    | 12/3/2004 14:18:43:894      | 5 1757-SRM    | (C)Port2 Communication error        |
| Chassis A    |         | 5719 12/2/2004 16:02:27:052 | 5 1757-SRM    | (1E) Chassis Redundancy State ch:   |

## IMPORTANT

## Actions

<!-- image -->

|                                                             | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Open the SRM configuration tool for the primary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the branches of your network until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. 白AB_ETH-2, Ethernet + 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A  Backplane, 1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A [05, 1757-5RM, 1757 50M050LN0a412W Me0 10.88.88.147, 1756-E Remove AB_VBP-1, 1789-A17/A Vir Driver Diagnostics Configure Driver Device Properties |

<!-- image -->

When you send event logs to Rockwell Automation:

- send events from both the primary and secondary chassis.
- include all events from the latest event to the last event when you knew that the chassis were in a good state.
- export them in the CSV format, which makes it easier to read and manipulate your data.

<!-- image -->

## Manually Synchronize the Chassis

After a switchover, you may have to manually synchronize the chassis because either:

- the Auto-Synchronization option is not set to Always or
- the chassis failed to synchronize.

To manually synchronize the chassis, perform this procedure.

1. Display RSLinx software.
2. From the Communications menu, choose RSWho.
3. Expand the network until you see the 1757-SRM module in the primary chassis.
4. Right-click the 1757-SRM module and select Module Configuration.
5. Click Synchronization.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Optimize Communication

6. Click Synchronize Secondary and then choose Yes to confirm.
7. Click OK.
8. In the primary chassis, what do the CNB modules display?
9. Cycle power to the secondary chassis.
10. If the CNB module in the primary chassis fails to display PwQS, see Troubleshoot a Failure to Synchronize on page 105.

|            | Front Panel If you see Which means Then                |                                                                                                                           |
|------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Look here. | PwQg Primary with Synchronizing (Qualifying) Secondary | •  Synchronization is in progress. •  Continue waiting. It may take several minutes to synchronize the secondary chassis. |
| Look here. | PwQS Primary with Synchronized (Qualified) Secondary   | •  The secondary chassis is synchronized. •  Skip the remaining steps in this section.                                    |
| Look here. | PwDS Primary with Disqualified Secondary               | •  The secondary chassis is not synchronized. •  Go to step 9.                                                            |

If it takes too long to synchronize the secondary chassis or update your HMI, there may not be enough controller time for unscheduled communication. In general, unscheduled communication is any type of communication that you do not configure through the I/O configuration folder of the controller.

## Communication Types

| This type of communication Is                                                                                                                                                     |                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Update I/O data (not including block-transfers). Scheduled communication                                                                                                          |                           |
| Produce or consume tags.                                                                                                                                                          |                           |
| Communicate with programming devices (for example, RSLogix 5000 software).                                                                                                        | Unscheduled communication |
| Communicate with HMI devices.                                                                                                                                                     |                           |
| Execute Message (MSG) instructions, including block-transfers.                                                                                                                    |                           |
| Respond to messages from other controllers.                                                                                                                                       |                           |
| Synchronize the secondary controller of a redundant system.                                                                                                                       |                           |
| Reestablish and monitor I/O connections, such as Removal and Insertion Under Power conditions; this does not include normal I/O updates that occur during the execution of logic. |                           |
| Bridge communications from the serial port of the controller to other ControlLogix devices via the ControlLogix backplane.                                                        |                           |

## Acceleration of Unscheduled Communication

| If an RSLogix 5000 project contains Then See Page                                   |                                             |     |
|-------------------------------------------------------------------------------------|---------------------------------------------|-----|
| Only a continuous task and no other tasks (This is the default task configuration.) | Choose a Greater System Overhead Time Slice | 120 |
| More than one task (for example, at least 1 periodic task)                          | Make All Your Tasks Periodic 122            |     |

## Choose a Greater System Overhead Time Slice

The system overhead time slice specifies the percentage of time (excluding the time for periodic tasks) that the controller devotes to unscheduled communication. The controller performs unscheduled communication for up to 1 ms at a time and then resumes the continuous task.

This table shows the ratio between the continuous task and unscheduled communication at various system overhead time slices.

## Continuous Task and Unscheduled Communication Ratios

| At this time slice The continuous task runs for And unscheduled communication occurs for up to   |
|--------------------------------------------------------------------------------------------------|
| 10% 9 ms 1 ms                                                                                    |
| 20% 4 ms 1 ms                                                                                    |
| 33% 2 ms 1 ms                                                                                    |
| 50% 1 ms 1 ms                                                                                    |

At a system overhead time slice of 20 % (default), unscheduled communication occurs every 4 ms of continuous task time for 1 ms.

<!-- image -->

If you increase the system overhead time slice to 33 %, unscheduled communication occurs every 2 ms of continuous task time for 1 ms.

<!-- image -->

## Enter a System Overhead Time Slice

To change the system overhead time slice, perform this procedure.

1. Right-click on your controller and select Properties.
2. Select Advanced.
3. Type or select a value for the system overhead time slice.

<!-- image -->

<!-- image -->

<!-- image -->

## Make All Your Tasks Periodic

Action Details

1. If you have more than one task, make them all periodic tasks.

If the controller contains only a periodic task or tasks, the system overhead time slice value has no effect. Unscheduled communication happens whenever a periodic task is not

running.

Example

Suppose your task takes 50 ms to execute and you configure its period to 80 ms. In that case, the controller has 30 ms out of every 80 ms for unscheduled communication.

<!-- image -->

2. Follow these guidelines to set the periods of the tasks.

If you have multiple tasks, make sure that:

- The execution time of a highest priority task is significantly less than its period.
- The total execution time of all your tasks is significantly less than the period of the lowest priority tasks.

This generally leaves enough time for unscheduled communication.

For example, in this configuration of tasks:

| Task Priority Execution Time Rate   |
|-------------------------------------|
| 1 Higher 20 ms 80 ms                |
| 2 Lower 30 ms 100 ms                |
| Total execution time: 50 ms         |

- The execution time of the highest priority task (Task 1) is significantly less than its period (20 ms is less than 80 ms).
- The total execution time of all tasks is significantly less than the period of the lowest priority task (50 ms is less than 100 ms).

3. Tune the periods of the tasks. Adjust the periods of the tasks as needed to get the best trade-off between executing your logic and servicing unscheduled communication.

4. Look for overlaps. Look at the Monitor tab of the properties of the task to see if overlaps are happening. An overlap happens if the period of a task is less than its scan time. If you see overlaps,

increase the period of the task.

## Check the Allocation of Unused Memory

To display this dialog:

1. Choose Edit ⇒ Controller Properties.
2. On the Redundancy tab, choose the Advanced button.

The controller reserves a specific amount of unused memory for tags and the rest for logic. Depending on how you configure the memory usage, you might not have memory for the required operation.

<!-- image -->

|                                                                                              | If Then Important                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You are unable to perform online edits                                                       |                                                                                                                                                                          |
|                                                                                              | OPC communications error or fail Make sure the slider is not all the way to Tags. You are able to change this setting only while: •  offline. •  online in program mode. |
| You are unable to create tags while online Make sure the slider is not all the way to Logic. | OPC communications error or fail Make sure the slider is not all the way to Tags. You are able to change this setting only while: •  offline. •  online in program mode. |

## Adjust CPU Usage for a CNB Module

For each CNB module in a redundant chassis, keep CPU usage to less than 75 percent.

- Each redundant CNB module needs enough additional processing time for redundancy operations.
- At peak operations such as synchronization, redundancy uses an additional 8 percent (approximately) of the CPU of the CNB module.
- A total CPU usage that is higher than 75 percent may prevent a secondary chassis from synchronizing after a switchover.

To reduce the CPU usage of a module, take any of these actions:

- Change the network update time (NUT) of the ControlNet network (Typically, increase the NUT to reduce the CPU usage of a CNB module.)
- Increase the requested packet interval (RPI) of your connections.
- Reduce the number of connections to (through) the CNB.
- Reduce the number of MSG instructions.
- Add another CNB module to each redundant chassis.

To obtain status information about a CNB module:

- use RSLinx software.
- look at the four-character display.
- send a message to the CNB module.

## Use RSLinx Software

1. Start RSLinx software.
2. Expand a network until the CNB module appears.
3. Right-click the module and choose Module Statistics.
4. Click Connection Manager.

<!-- image -->

<!-- image -->

## Four-Character Display

The four-character display on the front of the 1756-CNB/D/E or 1756-CNBR/D/E module, shows this information.

## Four-Character Display Readings

| For this information about a CNB module                       | Display Where                                                                                                                                                                                                                 | Display Where                                                                                                                                                                                                                 |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Address of the module A#xx xx                                 |                                                                                                                                                                                                                               | is the node address of the module.                                                                                                                                                                                            |
|                                                               |                                                                                                                                                                                                                               | Percent of CPU usage %Cxx xx is the percent of CPU usage. The range for the display is 00 - 99%.                                                                                                                              |
| Number of open connections nCxx                               |                                                                                                                                                                                                                               | xx is the number of open connections that the module is using.                                                                                                                                                                |
| Number of unconnected client buffers                          | Ucxx xx  is the number of unconnected client buffers that the module is using. You see this number only if the module is using 80% of its buffers or more. The module stops showing the number if the number drops below 50%. | Ucxx xx  is the number of unconnected client buffers that the module is using. You see this number only if the module is using 80% of its buffers or more. The module stops showing the number if the number drops below 50%. |
| Number of unconnected server buffers                          | Usxx xx  is the number of unconnected server buffers that the module is using. You see this number only if the module is using 80% of its buffers or more. The module stops showing the number if the number drops below 50%. | Usxx xx  is the number of unconnected server buffers that the module is using. You see this number only if the module is using 80% of its buffers or more. The module stops showing the number if the number drops below 50%. |
| State of the module’s keeper function                         | Kpxx xx is the state of the module’s keeper function.                                                                                                                                                                         | Kpxx xx is the state of the module’s keeper function.                                                                                                                                                                         |
| State of the module’s keeper function                         | If xx                                                                                                                                                                                                                         | is Then the module is                                                                                                                                                                                                         |
| State of the module’s keeper function                         |                                                                                                                                                                                                                               | Ai Active network keeper with either: •  invalid keeper information or •  keeper signature that does not match the keeper signature of the network.                                                                           |
| State of the module’s keeper function                         |                                                                                                                                                                                                                               | Av Active network keeper with: •  valid keeper information. •  keeper signature that defines the keeper signature of the network.                                                                                             |
| State of the module’s keeper function                         |                                                                                                                                                                                                                               | Ii Inactive network keeper with either: •  invalid keeper information or •  keeper signature that does not match the keeper signature of the network.                                                                         |
| State of the module’s keeper function                         |                                                                                                                                                                                                                               | Iv Inactive network keeper with valid keeper information that matches the keeper signature of the network.                                                                                                                    |
| State of the module’s keeper function                         | Oi                                                                                                                                                                                                                            | • Powering up with invalid keeper information or •  offline with invalid keeper information.                                                                                                                                  |
| State of the module’s keeper function                         | Ov                                                                                                                                                                                                                            | • Powering up with valid keeper information that may or may not match the keeper signature of the network or •  offline with valid keeper information that may or may not match the keeper signature of the network.          |
| Number of times that the bandwidth of the module was exceeded | Bxnn nn  is the number of times that the bandwidth of the module was exceeded (bandwidth exceeded error) since the module was turned off or reset. You see this number only if the number is more than zero.                  | Bxnn nn  is the number of times that the bandwidth of the module was exceeded (bandwidth exceeded error) since the module was turned off or reset. You see this number only if the number is more than zero.                  |

## Send a Message to the CNB Module

To use a Message (MSG) instruction to learn the CPU usage of a CNB module, configure the MSG instruction.

## CNB Module Configuration

| On this tab For this Type or select                                                        | On this tab For this Type or select                                                        | On this tab For this Type or select                                                        |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Configuration Message Type CIP Generic                                                     | Configuration Message Type CIP Generic                                                     | Configuration Message Type CIP Generic                                                     |
| Service Type Custom                                                                        | Service Type Custom                                                                        | Service Type Custom                                                                        |
| Service Code 4f                                                                            | Service Code 4f                                                                            | Service Code 4f                                                                            |
| Class a1                                                                                   | Class a1                                                                                   | Class a1                                                                                   |
| Instance 8                                                                                 | Instance 8                                                                                 | Instance 8                                                                                 |
| Attribute 0                                                                                | Attribute 0                                                                                | Attribute 0                                                                                |
| Source Element Tag that uses a user-defined data type:                                     | Source Element Tag that uses a user-defined data type:                                     | Source Element Tag that uses a user-defined data type:                                     |
| Members of the Data Type Tag Value                                                         | Members of the Data Type Tag Value                                                         |                                                                                            |
|                                                                                            | Name Data Type                                                                             |                                                                                            |
|                                                                                            | offset DINT 0                                                                              |                                                                                            |
| size_returned INT 2                                                                        |                                                                                            |                                                                                            |
| Source Length 6                                                                            | Source Length 6                                                                            | Source Length 6                                                                            |
| Destination INT tag in which to store the CPU usage of the CNB module (0 - 99%.)           | Destination INT tag in which to store the CPU usage of the CNB module (0 - 99%.)           | Destination INT tag in which to store the CPU usage of the CNB module (0 - 99%.)           |
| Communication Path 1, slot_number where: slot_number is the slot number of the CNB module. | Communication Path 1, slot_number where: slot_number is the slot number of the CNB module. | Communication Path 1, slot_number where: slot_number is the slot number of the CNB module. |

## Store or Load a Project Using Nonvolatile Memory

Nonvolatile memory lets you keep a copy of your project on the controller.

## Nonvolatile Memory Definitions

| Term Description                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nonvolatile memory Memory of the controller that retains its contents while the controller is without power or a battery.                                   |
| Store To copy a project to the nonvolatile memory of the controller. This overwrites any project that is currently in the nonvolatile memory.               |
| Load To copy a project from nonvolatile memory to the user memory (RAM) of the controller. This overwrites any project that is currently in the controller. |

In a redundant system, store or load a project only while the secondary chassis is disqualified. To store or load a project, perform these procedures.

## Storing or Loading Projects

| Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Store a Project  Important: If your computer is online with the controller over a ControlNet network, check the CPU usage of the CNB module. The CPU usage module must be less than about 75% for the store to work. 1. Put the primary controller in program mode (program or remote program). 2. Open the Module Configuration properties for one of the 1757-SRM modules. 3. Set the Auto-Synchronization option to Conditional. 4. Disqualify the secondary chassis. 5. Store the project that is in the primary controller. For step-by-step procedures on how to store a project, see Logix5000 Controllers Common Procedures, publication 1756-PM001. Important: Do not go back online to the primary controller until you complete the rest of the steps in this procedure. 6. Go online to the secondary controller and store the project. 7. Return to the Module Configuration properties for one of the 1757-SRM modules. 8. Synchronize the controllers. |
| Load a Project—User Initiated 1. Disqualify the secondary chassis. 2. Go online to the primary controller. 3. In the primary controller, load the project. For step-by-step procedures on how to store a project, see Logix5000 Controllers Common Procedures, publication 1756-PM001. 4. Synchronize the controllers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Load a Project—On Power Up This Load Image option works the same as in a nonredundant system. •  The controller loads the project on power up. •  The controller loads the project before it activates the redundancy feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Load a Project—On Corrupt Memory This Load Image option works the same as in a nonredundant system. •  The controller loads the project when the memory is empty or corrupt. •  The controller loads the project before it activates the redundancy feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Store a Project to Nonvolatile Memory While a Process Is Running

To store an updated project and firmware to the nonvolatile memory of a 1756-L61, 1756-L62 or 1756-L63 controller while the process is running, perform this procedure.

## IMPORTANT

Use this procedure only with a 1756-L61, 1756-L62 or 1756-L63 controller. Do not use the nonvolatile memory of a 1756-L55M2x controller if you have updated it to revision 15.56. If nonvolatile memory is used to store a project with a 1756-L55M2x controller, use revision 15.57 or later. Otherwise the controller will have an unrecoverable fault (solid red OK light) and clear the project from its memory.

| Action Details                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Make sure the chassis are synchronized. Synchronize the chassis if they are not already synchronized.                                                                                                                                                                                                                                                                                                                |
| 2. Disqualify the secondary chassis. A. Open the SRM configuration tool for the primary chassis. B. Set the Auto-Synchronization option to Never. C. Disqualify the secondary chassis.                                                                                                                                                                                                                                  |
| 3. Store the secondary controller’s project.  A. Go online to the secondary controller B. Store the project to the nonvolatile memory of the secondary controller. For step-by-step procedures on how to store a project, see Logix5000 Controllers Common Procedures, publication 1756-PM001. Important: Do not go back online to the secondary controller until you complete the rest of the steps in this procedure. |
| 4. Initiate a switchover. A. Go to the SRM configuration tool. B. Synchronize the chassis. C. Initiate a switchover.                                                                                                                                                                                                                                                                                                    |
| 5. Store the new secondary controller’s project. A. Go online to the new secondary controller B. Store the project to the nonvolatile memory of the secondary controller. For step-by-step procedures on how to store a project, see Logix5000 Controllers Common Procedures, publication 1756-PM001. Important: Do not go back online to the secondary controller until you complete this procedure.                   |
| 6. Synchronize the chassis. A. Go to the SRM configuration tool. B. Set the Auto-Synchronization option to the desired option. C. Synchronize the chassis.                                                                                                                                                                                                                                                              |

## Introduction

## Update Modules and Redundant Systems

This chapter explains how to update your module and redundant system.

|                                                                              | If you want to Then see this section Page                 |     |
|------------------------------------------------------------------------------|-----------------------------------------------------------|-----|
| Replace 1756-CNB/D or 1756-CNBR/D module(s) with series E modules            | Change CNB Modules from Series D to Series E While Online | 129 |
| Change the revision of a module while minimizing the time your system is off | Update a Redundant Control System Offline                 | 136 |
| Update the firmware of a redundant chassis without shutting down the process | Update an Online Redundant System 138                     |     |

## Change CNB Modules from Series D to Series E While Online

129

To replace 1756-CNB/D or 1756-CNBR/D module(s) with series E modules while you are online, perform this procedure.

## IMPORTANT

- Use this procedure only if your redundancy system is already at revision 15.
- Replace CNB modules with CNB modules and CNBR modules with CNBR modules. Otherwise your chassis will not synchronize.
- Finish this procedure once you start it.

## Before You Begin

This procedure is easier to complete if you first update the firmware of your 1756-CNB/D or 1756-CNBR/D module(s).

## Firmware Update

| If the CNB modules are And you Then                                      |                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                          | Revision 11.1 or later Go to Actions and start the procedure. You do not need to update the firmware of the modules.                                                                                                                                                                                                                                                  |
| Not revision 11.1 or later Have a nonredundant chassis with an open slot | 1. Add the revision 11 EDS files for the CNB modules, if you have not already done so. 2. Put one of the CNB modules into the open slot of the nonredundant chassis. 3. Use ControlFlash software and update the firmware of the CNB module. 4. Remove the CNB module. 5. Repeat steps 1-4 for the rest of the CNB modules. 6. Go to Actions and start the procedure. |
| Do not have a nonredundant chassis with an open slot                     | Go to Actions and start the procedure. You will have to use the secondary chassis to update the modules.                                                                                                                                                                                                                                                              |

## Actions

<!-- image -->

<!-- image -->

|                                                              | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Did you already update the firmware of the series E modules? | Did you already update the firmware of the series E modules? •  Yes — Go to step 6. •  No — Continue with step 5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 5. Update the firmware of the series E modules.              | A. Remove the 1757-SRM module from the secondary chassis. B. Set the address of each series E module to the address of its corresponding series D module plus one. C. Replace each series D module with the corresponding series E module. Important: Make sure you connect the correct ControlNet tap to each module. D. Use ControlFlash software and update the firmware of each series E module. E. Remove the series E modules from the secondary chassis and set their addresses to match the original series D modules. F. Repeat steps B-E for the second set of series E modules. G. Put the secondary SRM back into the secondary chassis. H. Put one set of series E modules into the secondary chassis. Important: Make sure that you use the correct address, slot, and ControlNet tap for each module. I. Go to step 7. |
| 6. Replace the CNB modules in the secondary chassis.         | Replace the CNB/D modules in the secondary chassis with series E modules. As you replace the modules: •  make sure that you set each module to the same address as the module that it is replacing. •  make sure that you connect the correct ControlNet tap. To avoid connecting the wrong tap, replace the modules one at a time and reconnect the ControlNet tap.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Action Details

7. Update the keeper signatures of the CNB modules.
- A. Start RSNetWorx for ControlNet and open the network configuration file.
- B. Go online with the network. You do not have to browse the entire network.
- C. Select Network &gt; Keeper Status.
- D. Select the node number of the secondary CNB and click Update Keeper.
- E. Verify that the keeper signature has been updated.
- F. Repeat steps D and E for the other CNB modules in the secondary chassis.
- G. Click Close.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Update a Redundant Control System Offline

Complete this procedure to upgrade the revision of your redundant modules. This procedure minimizes the time your process is down during an upgrade.

## IMPORTANT

Do not connect your computer to the network access port on a CNB module in the primary chassis. You will lose access to the network when you turn off power to the chassis.

|                                                               | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                               | 1. Upload and save the project. Do you have an up-to-date copy of the project for the controller stored offline? •  Yes — Go to step 2. •  No — Continue with step A. A. Upload the project in the primary controller. B. Save the project.                                                                                                                                                                                                                                                                                                                                     |
| 2. Open the SRM configuration tool for the secondary chassis. | A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the branches of your network until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. AB_ETH-2,Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBT/A 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane, 1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 05,1757-5RM 10.88.88.147, 1756-E Remove AB_VBP-1,1789-A17AVir Driver Diagnostics Configure Driver Device Properties |

<!-- image -->

<!-- image -->

<!-- image -->

3. Disqualify the secondary chassis, A. Click Configuration.

- B. Set Auto-Synchronization to Never.

- C. Choose Apply and then Yes to confirm.

- D. Click Synchronization.

- E. Choose Disqualify Secondary and then Yes to confirm.

4. Upgrade the required firmware of the secondary chassis.

See the ControlLogix Controller and Memory Board Installation Instructions, publication 1756-IN101.

5. Make the secondary controller the new primary controller.

- A. Start RSLogix 5000 software.

- B. Download the project to the secondary controller.

- C. When it is safe to stop the system, change the primary controller to Program Mode.

- D. Turn off power to the primary chassis.

- E. Go to the 1757-SRM properties of the secondary chassis.

- F. Choose Become Primary.

6. Clear the fault of the new primary controller.

- A. In RSLogix 5000 software, go online to the new primary controller.

- B. The controller is faulted. When a disqualified secondary controller becomes a primary controller, the controller experiences a major fault.

- C. From the Communications menu, choose Clear Faults.

- D. To start control of the process, from the Communications menu, choose Run Mode.

7. Upgrade the other redundant chassis. A. Turn on power to the other redundant chassis.

- B. Upgrade the required firmware of the chassis.

8. Change the Auto-Synchronization Option to Always.

- A. Open the SRM configuration tool for the primary chassis.

- B. On the Configuration tab, change the Auto-Synchronization option to Always.

- C. Choose OK.

Action Details

## 1757-SRMREDIJNDANCYMODULE

Module lnfo

Configuration

Synchronization

SynchronizationStatus

Event Log

System Update

Options

Auto-Synchronization:

Never

SRMSerial Number:

## 1757-SRMREDUNDANCYMODULE

Module Info

Configuration

Synchronization

Synchronization Status

E vent Log

System Update

Commands

Sunchronize Secondary

Disqualify Secondary

Initiate Switchover

Become

## 1757-SRMREDUNDANCYM0DULEProperties

Module Info

Configuration

Synchronization

Synchronization Status

Event Log

System Update

Commands

Synchronize Secondary

Disqualify Secondary

Initiate Switehover

Become Primary

## Update an Online Redundant System

The redundancy system update feature of ControlLogix lets you update the firmware in a secondary chassis while the primary chassis is controlling outputs.

However, during a redundancy system update, remember that:

- the secondary chassis' redundancy feature is disabled.
- the secondary chassis cannot act on a primary chassis failure.

## IMPORTANT

Once you have updated the firmware of the modules in the secondary chassis and downloaded the recompiled application programs to your updated secondary chassis, you can then lock your redundant system and switch control to the secondary chassis without any changes to your outputs or data.

A locked switchover differs from a normal switchover in that only you can initiate the former. A primary chassis failure cannot initiate a locked switchover.

Attempting to update a system with busy 1756-L55Mxx controllers will result in a loss of system control. A system that is locked for update requires additional processor resources. A CPU utilization of a synchronized pair of 1756-L55Mxx controllers that exceeds 80% suggests that adequate processor resources are not available to your application.

## Redundant System Definitions

| Term Description                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controlling Outputs When outputs are being controlled, they are active and reacting to input state changes being monitored by your application. When not being controlled, outputs can still be active but cannot react to input state changes.                                            |
| Locked for Update No application changes are allowed on either the primary or secondary controllers. Your system must enter this state in order to initiate a locked switchover from the primary to secondary chassis.                                                                     |
| Locked Switchover This is the process of transferring control from a locked primary chassis to a locked secondary chassis.                                                                                                                                                                 |
| Locking for Update This is the process of locking a redundant system in preparation for entering the locked state.                                                                                                                                                                         |
| Supports Locking This attribute in a redundancy object indicates whether a module supports the locking feature. Only secondary chassis modules need this attribute to enable your redundancy system to enter a locked state.                                                               |
| Partner A partner is a module in a chassis that is in the same slot position as a module in the corresponding chassis. A module in the primary chassis can have a partner in the secondary chassis. Likewise, a module in the secondary chassis can have a partner in the primary chassis. |
| Disqualified Secondary The secondary chassis or modules are in either the DSwP or DSwNP states, depending on whether or not the primary chassis or modules exist.                                                                                                                          |

## IMPORTANT

When a secondary communications module is locking for updating, it displays SLU. When a primary communications module is locked for updating and has firmware revision 15.56 or later, it displays PLU. If the primary communications module's firmware is an earlier revision, PwQS will be displayed when the system is locked.

## Redundant System Relationships

Different terms are unique to normal redundancy and redundancy during an update.

| This term in normal redundancy Equates to this term during the updating of a redundant system   |
|-------------------------------------------------------------------------------------------------|
| Synchronize Lock for Update                                                                     |
| Synchronizing Locking for Update                                                                |
| Synchronized Locked for Update                                                                  |
| Switchover Locked Switchover                                                                    |

Complete this procedure to update the firmware of a redundant chassis without shutting down the process.

## IMPORTANT

Use this procedure only if your system is already at revision 13.

Do not use this procedure if:

- your system is at revision 11 or earlier.
- your system is not operating yet.

During this procedure, you will not be able to use RSLogix 5000 software to change the mode of the controller. Use the keyswitch on the front of the controller to change its mode.

Leave RSNetWorx for ControlNet software closed or offline throughout this procedure. Otherwise, you will see errors in the RSNetWorx software during the update process.

During this procedure:

- do not make any changes to the RSLogix 5000 project other than the ones called out in this procedure.
- make sure no one else makes changes to the project.

<!-- image -->

| Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Update the software. A. Go to the tool tray of your computer and shutdown RSLinx software. B. Update this software: •  1757-SRM System Redundancy Module Configuration tool •  RSLogix 5000 software •  RSLinx software •  RSNetWorx software •  ControlFLASH firmware update kit. If you are planning to uninstall version 13 of your RSLogix 5000 software, wait until you have completed and validated your update. Restore Shutdown RSLinxClassic RSLUgIX SUuu 11:02AM                                                                                                                                                                                                               |
| 2. Add the latest EDS files. Start ⇒ Programs ⇒ Rockwell Software  ⇒ RSLinx Tools  ⇒ EDS Hardware Installation Tool                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3. Put the keyswitches in the REM position. Put the keyswitch of each redundant controller to the REM position. Otherwise you will not be able to update the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 4. Open the SRM configuration tool for the primary chassis. A. Start RSLinx software. B. From the Communications menu, choose RSWho. C. Open the branches of your network until you find the 1757-SRM module in the primary chassis. D. Right-click the SRM and choose Module Configuration. 品AB_ETH-2,Ethernet 10.88.88.130, 1756-ENBT/A, 1756-ENBTA 10.88.88.146, 1756-EWEB/A, 1756-EWEB/A Backplane,1756-A7/A 00, 1756-L63 LOGIX5563, 1756-L63/A 13.53.2 01, 1756-CNB/D, 1756-CNB/D 5.044 Build 030 02, 1756-EWEB/A 05, 1757-5RM,1757 s0MD50LMDAMCV MO0 10.88.88.147, 1756-E Remove AB_VBP-1,1789-A17AVir Driver Diagnostics Configure Driver Device Properties Module Configuration... |

<!-- image -->

<!-- image -->

|                                                      | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8. Initiate a switchover.                            | A. Click Initiate Switchover and Yes. B. Wait for the system to switchover. The other chassis is now the primary chassis. 1757-SRMREDUNDANCYMODULE Module lnfo Configuration Synchronization Synchronization Status Event Log System Update Redundancy Commands Disqualify Secondary InitiateSwitchover Become Chassis B: Primary with Disqualified Secondary OK Auto-Synchronization State:Never                                                                                                                                                                                                                                                                                                                                 |
| 9. Update the modules in the new secondary chassis.  | Use the ControlFLASH firmware update tool to update the modules in the new secondary chassis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 10. Prepare the RSLogix 5000 project for the update. | A. Start RSLogix 5000 software and go online to the primary controller. B. Set the watchdog time for each task to this value or more: Minimum watchdog time = (2 *maximum_scan_time) + 150 ms where: Maximum_scan_time is the maximum scan time for the entire task when the secondary controller is synchronized. C. Cancel or assemble any test edits. D. Remove all SFC forces from the project. E. Make sure that you do not need to make any changes to: You can make those changes again when the update is done and both chassis synchronize. F. Save the project. •  I/O Forces — Once you start this procedure, you will not be able to disable or enable I/O forces until you update both chassis. •  I/O configuration |

<!-- image -->

|                                                       | Action Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 12. Download the project to the secondary controller. | Important: If I/O forces are enabled in the offline project, the software asks if you want to enable the forces in the controller. Even if you choose No, I/O forces stay enabled in the primary controller and become enabled in this controller after you switchover. A. Use RSLogix 5000 software to download the project to the controller in the secondary chassis. The secondary chassis has the higher network address of the redundant pair. B. Go offline. Important: Stay offline until you finish this procedure. |

<!-- image -->

<!-- image -->

## Notes:

## Introduction

147

<!-- image -->

## Set Up EtherNet/IP Communication Across Subnets

This appendix explains how to keep HMIs and messages pointing to the primary chassis when IP swapping is not in use.

This appendix provides this information.

| Topic Page                                             |
|--------------------------------------------------------|
| Keep an HMI Communicating with the Primary Chassis 148 |
| Keep a Message Going to the Primary Chassis 154        |

Use this appendix when:

- you want to use alias topics instead of IP swapping.
- your primary and secondary chassis are on different EtherNet/IP subnets

## Redundant Chassis Subnets

<!-- image -->

| If both redundant chassis are on Then                                     |                                                                                                                             |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Different subnets  Switch Router Switch Primary Chassis Secondary Chassis | You must point your HMIs and messages to the new primary chassis after a switchover. Use this appendix to show you how.     |
| Same subnet  Switch Primary Chassis Secondary Chassis                     | Stop. Use IP swapping instead. This lets you use the same IP address regardless of which chassis is primary. See Chapter 2. |

When primary and secondary chassis are on different EtherNet/IP subnets, they keep their IP addresses during a switchover. This means that your and other controllers must be able to switch between the IP address of each redundant chassis.

## Keep an HMI Communicating with the Primary Chassis

If you are not using IP swapping, your HMIs must direct their communication to the new primary chassis after a switchover. ControlLogix Redundancy Alias Topic Switcher software can most easily do this. Look for this software on the CD along with your firmware.

## IMPORTANT

To use the ControlLogix Redundancy Alias Topic Switcher software, your computer needs an activation file for RSLinx software. The activation file lets you perform DDE/OPC communication.

The ControlLogix Redundancy Alias Topic Switcher software works with RSLinx alias topics. Together they keep your HMI communicating with the primary controller after a switchover.

## HMI Communication

<!-- image -->

To keep an HMI communicating with the primary chassis:

- install the ControlLogix Redundancy Alias Topic Switcher Software.
- configure a Driver to Communicate with the Primary and Secondary EtherNet/IP Modules.
- create a DDE/OPC topic for each controller.
- create an alias topic.
- set up the alias topic switcher.
- address the alias topic in the HMI project.

## Install the ControlLogix Redundancy Alias Topic Switcher Software

The ControlLogix Redundancy Alias Topic Switcher software maintains communication between your HMI project and the primary controller after a switchover.

To install the Alias Topic Switcher software, use the ControlLogix Redundancy Alias Topic Switcher.Exe file. The file is located on the same CD as the firmware for your redundancy system.

The Alias Topic Switcher software runs as a service. It starts automatically when you start your computer and shows up in the tool tray of your desktop.

Alias Topic Switcher Software Tool Tray

ControlLogix Redundancy Alias Topic Switcher

<!-- image -->

## Configure a Driver to Communicate with the Primary and Secondary EtherNet/IP Modules

<!-- image -->

## Create a DDE/OPC Topic for Each Controller

<!-- image -->

1. In RSLinx software, choose DDE/OPC ⇒ Alias Topic Configuration.

## Create an Alias Topic

<!-- image -->

2. Type a name for the alias topic that will communicate with this pair of redundant controllers.
3. Add the topic for each redundant controller to the Aliased Topics list.

To add a topic, select the topic and choose . &lt;-PP

4. Check the Switch on command check box. Uncheck the remaining check boxes.

This lets the ControlLogix Redundancy Alias Topic Switcher software control which topic the alias topic uses for communication.

<!-- image -->

5. Click and then .

<!-- image -->

## Set Up the Alias Topic Switcher

## IMPORTANT

If you start the Alias Topic Switcher software without access to an RSLinx activation file (for example, without a version of RSLinx which supports OPC), this error occurs:

0x80040112

(The text for the message depends on your operating system.)

<!-- image -->

1. In the tool tray, right-click the Redundancy Switch icon and choose Open Alias Topic Switching Tool.

<!-- image -->

4. Click .

<!-- image -->

using

## Address the Alias Topic in the HMI Project

<!-- image -->

When you create tags for your HMI project, use the alias topic in the address of the tag.

## Keep a Message Going to the Primary Chassis

If you are not using IP swapping, any controller that sends a message to a redundant chassis has to point to the new primary chassis after a switchover.

## Sending Message to Primary Chassis

<!-- image -->

In this procedure, use CIP Generic messages to determine which chassis is primary. Then send a Message (MSG) instruction to the primary controller.

<!-- image -->

To keep a Message (MSG) instruction going to the new primary chassis after a switchover:

- create a periodic trigger for the messages.
- obtain the redundancy state of chassis A.
- obtain the redundancy state of chassis B.
- determine which chassis is primary.
- send the message to the appropriate controller.

## Create a Periodic Trigger for the Messages

Free-running timer that triggers the execution of MSG instructions. The timer runs for 2 seconds (2000 ms) and then resets and starts timing again. Every 2 seconds, Timer\_RedundancyMSGs.DN = 1 for a single scan. The MSG instructions use this bit as one of their conditions for execution.

<!-- image -->

| Tag Name Description Alias For Data Type                                                              |       |
|-------------------------------------------------------------------------------------------------------|-------|
| Timer_RedundancyMSGs Periodic trigger for the execution of MSG instructions. Triggers MSGs every 2 s. | TIMER |

## Get the Redundancy State of Chassis A

If Timer\_RedundancyMSGs.DN = 1 (2 seconds are up so execute the MSG instruction again)

And ChasA\_GetRedundState\_FromENBT.EN = 0 (The MSG instruction is not currently enabled.)

## Then

Execute a MSG instruction that gets the redundancy state of Chassis A from the ENBT module in Chassis A. Store the value in ChasA\_RedundancyState (data type = DINT).

<!-- image -->

| Tag Name Description Alias For Data Type                                                             |         |
|------------------------------------------------------------------------------------------------------|---------|
| Timer_RedundancyMSGs Periodic trigger for the execution of MSG instructions. Triggers MSGs every 2s. | TIMER   |
| ChasA_GetRedundState_FromENBT Message instruction that gets the redundancy state of Chassis A.       | MESSAGE |
| ChasA_RedundancyState Redundancy state of the Chassis A: 2 = PwQS 3 = PwDS 4 = PwNS                  | DINT    |

| MSG Parameter Value               |
|-----------------------------------|
| Message Type CIP Generic          |
| Service Type Get Attribute Single |
| Service Code e                    |
| Class c0                          |
| Instance 1                        |
| Attribute 4                       |
| Source Element                    |

| MSG Parameter Value      |                                                                                                                                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source Length            |                                                                                                                                                                                                                                                                      |
|                          | Destination ChasA_RedundancyState                                                                                                                                                                                                                                    |
| Path (communication tab) | Specify the 1756-ENBT module in Chassis A. Use either of these methods: •  Add the module to the I/O configuration of the controller. Then use the Browse button on the Communication tab to identify the module. •  Type the path using port numbers and addresses. |

## Get the Redundancy State of Chassis B

If Timer\_RedundancyMSGs.DN = 1 (2 seconds are up so execute the MSG instruction again)

And ChasB\_GetRedundState\_FromENBT.EN = 0 (The MSG instruction is not currently enabled.)

## Then

Execute a MSG instruction that gets the redundancy state of Chassis B from the ENBT module in Chassis B. Store the value in ChasB\_RedundancyState (data type = DINT).

<!-- image -->

| Tag Name Description Alias For Data Type                                                             |         |
|------------------------------------------------------------------------------------------------------|---------|
| Timer_RedundancyMSGs Periodic trigger for the execution of MSG instructions. Triggers MSGs every 2s. | TIMER   |
| ChasB_GetRedundState_FromENBT Message instruction that gets the redundancy state of Chassis B.       | MESSAGE |
| ChasB_RedundancyState Redundancy state of the Chassis B: 2 = PwQS 3 = PwDS 4 = PwNS                  | DINT    |

| MSG Parameter Value                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message Type CIP Generic                                                                                                                                                                                                                                                                      |
| Service Type Get Attribute Single                                                                                                                                                                                                                                                             |
| Service Code e                                                                                                                                                                                                                                                                                |
| Class c0                                                                                                                                                                                                                                                                                      |
| Instance 1                                                                                                                                                                                                                                                                                    |
| Attribute 4                                                                                                                                                                                                                                                                                   |
| Destination ChasB_RedundancyState                                                                                                                                                                                                                                                             |
| Path (communication tab) Specify the 1756-ENBT module in Chassis B. Use either of these methods: •  Add the module to the I/O configuration of the controller. Then use the Browse button on the Communication tab to identify the module. •  Type the path using port numbers and addresses. |

## Determine Which Chassis is Primary

If ChasA\_RedundancyState = 2, 3, or 4 then

ChasA\_IsPrimary = 1. (Chassis A is the primary chassis.)

<!-- image -->

If ChasB\_RedundancyState = 2, 3, or 4 then

ChasB\_IsPrimary = 1. (Chassis B is the primary chassis.)

<!-- image -->

| Tag Name Description Alias For Data Type                                            |      |
|-------------------------------------------------------------------------------------|------|
| ChasA_RedundancyState Redundancy state of the Chassis A: 2 = PwQS 3 = PwDS 4 = PwNS | DINT |
| ChasB_RedundancyState Redundancy state of the Chassis B 2 = PwQS 3 = PwDS 4 = PwNS  | DINT |

| Tag Name Description Alias For Data Type                                                                                                                                                                                             |      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| ChasA_IsPrimary If set (1), then Chassis A is the primary chassis. IsPrimary.0 BOOL                                                                                                                                                  |      |
| ChasB_IsPrimary If set (1), then Chassis B is the primary chassis. IsPrimary.1 BOOL                                                                                                                                                  |      |
| IsPrimary Each bit represents the primary status for an individual chassis within a redundant chassis pair. 1 = primary. 0 = not primary. A single DINT tag for all the chassis uses less memory than a unique tag for each chassis. | DINT |

## Send the Message to the Appropriate Controller

If Timer\_RedundancyMSGs.DN = 1 (2 seconds are up.)

And ChasA\_IsPrimary = 1. (Chassis A is the primary chassis.)

And ChasA\_MSG.EN = 0 (The message is not currently enabled.)

Then

Execute the MSG instruction for the controller in Chassis A.

<!-- image -->

If Timer\_RedundancyMSGs.DN = 1 (2 seconds are up.)

And ChasB\_IsPrimary = 1. (Chassis B is the primary chassis.)

And ChasB\_MSG.EN = 0 (The message is not currently enabled.)

Then

Execute the MSG instruction for the controller in Chassis B.

<!-- image -->

| Tag Name Description Alias For Data Type                                                                             |         |
|----------------------------------------------------------------------------------------------------------------------|---------|
| ChasA_IsPrimary If set (1), then Chassis A is the primary chassis. IsPrimary.0 BOOL                                  |         |
| ChasA_MSG Message instruction that transfers data between this controller and the controller in redundant Chassis A. | MESSAGE |
| ChasB_IsPrimary If set (1), then Chassis B is the primary chassis. IsPrimary.1 BOOL                                  |         |
| ChasB_MSG Message instruction that transfers data between this controller and the controller in redundant Chassis B. | MESSAGE |

## Notes:

## Introduction

## Convert Local Modules to Remote Modules

163

## Convert an Existing System to Redundancy

This appendix explains how to convert an existing system to redundancy.

If you are adding redundancy to an existing system, follow these guidelines:

- Changing the node number of a CNB module may affect messages, tags, or listen-only connections in other devices. Choose node numbers that have the least impact on existing communications.
- An existing system that contains local I/O modules still requires two additional chassis.
- – A redundant system can use only I/O that is in a remote chassis (for example, not in the same chassis as the controller).
- – We recommend that you move the existing 1756-L55Mxx controller from the original chassis and place it in a redundant chassis.
- Change any event tasks to periodic tasks. You cannot use event tasks in a ControlLogix redundancy system.

You can convert an existing system to a redundant system.

## Local Module Conversions

| If the existing system Then                                                  |                                                                                                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Contains only I/O modules that are not in the same chassis as the controller | Do not change the I/O configuration of the controller.                                                                         |
|                                                                              | Contains local I/O modules Use the procedures in this section to convert the configuration of local modules to remote modules. |

To convert a local module to a remote module:

- reconfigure the local I/O modules.
- replace local I/O tags.
- replace any aliases to local I/O tags.

## Reconfigure the Local I/O Modules

1. If you have not already done so, add the CNB module of the remote chassis to the I/O configuration of the controller. See the ControlLogix System User Manual, publication 1756-UM001.
2. In the controller organizer, cut these modules from the local I/O configuration and paste them into the remote CNB module:
- I/O
- 1756-DHRIO
- 1756-DNB
- 1756-ENET or -ENB
- 1756-MVI

<!-- image -->

## Replace Local I/O Tags

1. Open a routine. If a routine is already open, click within the routine to activate the window.
2. Press the Ctrl + H keys.

This dialog appears.

<!-- image -->

3. Type Local.
4. Type the name of the CNB module that is in the remote chassis.
5. Select All Routines.
6. Click Find Within &gt;&gt;.
7. Select Ladder Diagrams.
8. Check Instruction Operands.
9. Choose Replace All.

<!-- image -->

The Search Results tab displays the changes to the logic.

10. Choose Close.

This example shows the results of replacing Local with chassis\_c.

## EXAMPLE

| Replacing Local with chassis_c...                                     |
|-----------------------------------------------------------------------|
| Searching through MainProgram - MainRoutine...                        |
| Replaced: Rung 0, XIC, Operand 0: XIC(Local:16:I.Data.0)              |
| Replaced: Rung 0, OTE, Operand 0: OTE(Local:2:O.Data.0)               |
| Replaced: Rung 1, XIC, Operand 0: XIC(Local:16:I.Data.1)              |
| Replaced: Rung 1, OTE, Operand 0: OTE(Local:2:O.Data.1)               |
| Replaced: Rung 2, XIC, Operand 0: XIC(Local:16:I.Data.2)              |
| Replaced: Rung 2, OTE, Operand 0: OTE(Local:2:O.Data.2)               |
| Replaced: Rung 8, OTE, Operand 0: OTE(Local:15:O.CommandRegister.Run) |
| Complete - 7 occurrence(s) found, 7 occurrence(s) replaced.           |

## Replace Any Aliases to Local I/O Tags

Are any tags aliases for I/O devices that were previously in a local chassis?

| If Then                 |
|-------------------------|
| Yes Go to step 1.       |
| No Skip this procedure. |

1. From the Logic menu, choose Edit Tags.
2. Press the Ctrl + H keys (replace).

<!-- image -->

3. Type Local.
4. Type the name of the CNB module that is in the remote chassis.
5. Select All Tags.
6. Click Find Within &gt;&gt;.
7. Check Alias.
8. Choose Replace All.
9. Choose Close.

<!-- image -->

## Notes:

## Introduction

## Attributes of the Redundancy Object

<!-- image -->

## Attributes of the Redundancy Object

This appendix explains how to use the redundancy object to learn about the status of your redundant system.

These are the attributes of the redundancy object.

## Redundant System Status and Corresponding Attributes

| For this information Get this attribute Data   |                                | Type    | GSV/SSV Description   |                                           |
|------------------------------------------------|--------------------------------|---------|-----------------------|-------------------------------------------|
| Redundancy status of the entire chassis.       | ChassisRedundancy State        |         | INT GSV               | If Then                                   |
| Redundancy status of the entire chassis.       | ChassisRedundancy State        |         | INT GSV               | 16#2 Primary with synchronized secondary  |
| Redundancy status of the entire chassis.       | ChassisRedundancy State        |         | INT GSV               | 16#3 Primary with disqualified secondary  |
| Redundancy status of the entire chassis.       | ChassisRedundancy State        |         | INT GSV               | 16#4 Primary with no secondary            |
| Redundancy status of the entire chassis.       | ChassisRedundancy State        |         | INT GSV               | 16#10 Primary locked for update           |
| Redundancy state of the partner chassis.       | PartnerChassis RedundancyState | INT GSV |                       | If Then                                   |
| Redundancy state of the partner chassis.       | PartnerChassis RedundancyState | INT GSV |                       | 16#8 Synchronized secondary               |
| Redundancy state of the partner chassis.       | PartnerChassis RedundancyState | INT GSV |                       | 16#9 Disqualified secondary with primary  |
| Redundancy state of the partner chassis.       | PartnerChassis RedundancyState | INT GSV |                       | 16#E No partner                           |
| Redundancy state of the partner chassis.       | PartnerChassis RedundancyState | INT GSV |                       | 16#12 Secondary locked for update         |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | If Then                                   |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#2 Primary with synchronized secondary  |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#3 Primary with disqualified secondary  |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#4 Primary with no secondary            |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#6 Primary with synchronizing secondary |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#F Primary locking for update.          |
| Redundancy status of the controller.           | ModuleRedundancy State         | INT GSV |                       | 16#10 Primary locked for update           |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | If Then                                   |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#7 Synchronizing secondary              |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#8 Synchronized secondary               |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#9 Disqualified secondary with primary  |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#E No partner                           |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#11 Secondary locking for update        |
| Redundancy state of the partner.               | PartnerModule RedundancyState  | INT GSV |                       | 16#12 Secondary locked for update         |

169

| For this information Get this attribute Data                                                                  |                              | GSV/SSV Description   |                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Results of the compatibility checks with the partner controller.                                              | CompatibilityResults INT GSV |                       | If Then                                                                                                                           |
| Results of the compatibility checks with the partner controller.                                              | CompatibilityResults INT GSV |                       | 0 Undetermined                                                                                                                    |
| Results of the compatibility checks with the partner controller.                                              | CompatibilityResults INT GSV |                       | 1 No compatible partner                                                                                                           |
| Results of the compatibility checks with the partner controller.                                              | CompatibilityResults INT GSV |                       | 2 Fully compatible partner                                                                                                        |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | If Then                                                                                                                           |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | -1 Synchronization (qualification) is not in progress.                                                                            |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | 0 Unsupported                                                                                                                     |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | 1 - 99 For modules that can measure their completion percentage, the percent of synchronization (qualification) that is complete. |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | 50 For modules that cannot measure their completion percentage, synchronization (qualification) is in progress.                   |
| Status of the synchronization (qualification) process.                                                        | Qualification InProgress     | INT GSV               | 100 Synchronization (qualification) is complete.                                                                                  |
| Keyswitch settings of the controller and its partner match or do not match.                                   | KeyswitchAlarm DINT GSV      |                       | If Then                                                                                                                           |
| Keyswitch settings of the controller and its partner match or do not match.                                   | KeyswitchAlarm DINT GSV      | 0                     | • The keyswitches match or •  No partner is present.                                                                              |
| Keyswitch settings of the controller and its partner match or do not match.                                   | KeyswitchAlarm DINT GSV      |                       | 1 Keyswitches do not match                                                                                                        |
| Position of the keyswitch of the partner.                                                                     | PartnerKeyswitch DINT GSV    |                       | If Then the keyswitch is in                                                                                                       |
| Position of the keyswitch of the partner.                                                                     | PartnerKeyswitch DINT GSV    |                       | 0 Unknown                                                                                                                         |
| Position of the keyswitch of the partner.                                                                     | PartnerKeyswitch DINT GSV    |                       | 1 RUN                                                                                                                             |
| Position of the keyswitch of the partner.                                                                     | PartnerKeyswitch DINT GSV    |                       | 2 PROG                                                                                                                            |
| Position of the keyswitch of the partner.                                                                     | PartnerKeyswitch DINT GSV    |                       | 3 REM                                                                                                                             |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  | This                  | Means this minor fault                                                                                                            |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 1 Powerup fault                                                                                                                   |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 3 IO fault                                                                                                                        |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 4 Problem with an instruction (program)                                                                                           |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 6 Periodic task overlap (watchdog)                                                                                                |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 9 Problem with the serial port                                                                                                    |
| Status of the minor faults of the partner (if the ModuleRedundancyState indicates that a partner is present). | PartnerMinorFaults DINT GSV  |                       | 10 Low battery                                                                                                                    |

| For this information Get this attribute Data                                                                     | Type                      | GSV/SSV Description   |                         |
|------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------------|-------------------------|
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | If Then                 |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#0 Power up           |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#1 Program            |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#2 Run                |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#3 Test               |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#4 Faulted            |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#5 Run-to-program     |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#6 Test-to-program    |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#7 Program-to-run     |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#8 Test-to-run        |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#9 Run-to-test        |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#A Program-to-test    |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#B Into faulted       |
| Mode of the partner. PartnerMode DINT GSV                                                                        |                           |                       | 16#C Faulted-to-program |
| In a pair of redundant chassis, identification of a specific chassis without regard to the state of the chassis. | PhysicalChassisID INT GSV |                       | If Then                 |
| In a pair of redundant chassis, identification of a specific chassis without regard to the state of the chassis. | PhysicalChassisID INT GSV |                       | 0 Unknown               |
| In a pair of redundant chassis, identification of a specific chassis without regard to the state of the chassis. | PhysicalChassisID INT GSV |                       | 1 Chassis A             |
| In a pair of redundant chassis, identification of a specific chassis without regard to the state of the chassis. | PhysicalChassisID INT GSV |                       | 2 Chassis B             |

| For this information Get this attribute Data                                                 |                       | GSV/SSV Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                | GSV/SSV Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Slot number of the 1757-SRM module in this chassis.                                          | SRMSlotNumber INT GSV |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| •  Size of the last crossload. •  Size of the last crossload if you had a secondary chassis. | LastDataTransfer Size | DINT GSV This attribute gives the size of data that was or would have been crossloaded in the last scan. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. Is there a synchronized secondary chassis? •  Yes — This gives number of DINTs that was crossloaded in the last scan. •  No — This gives number of DINTs that would have been                                                           | DINT GSV This attribute gives the size of data that was or would have been crossloaded in the last scan. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. Is there a synchronized secondary chassis? •  Yes — This gives number of DINTs that was crossloaded in the last scan. •  No — This gives number of DINTs that would have been                                                           |
| •  Size of the biggest crossload.                                                            | MaxDataTransfer Size  | This attribute gives the biggest size of the LastDataTransfer Size attribute. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. •  To reset this value, use an SSV instruction with a Source value of 0. Is there a synchronized secondary chassis? •  Yes — This gives biggest number of DINTs that was crossloaded. •  No — This gives biggest number of DINTs that would have been crossloaded. | This attribute gives the biggest size of the LastDataTransfer Size attribute. •  The size in DINTs (4-byte words). •  You must configure the controller for redundancy. •  You do not need a secondary chassis. •  To reset this value, use an SSV instruction with a Source value of 0. Is there a synchronized secondary chassis? •  Yes — This gives biggest number of DINTs that was crossloaded. •  No — This gives biggest number of DINTs that would have been crossloaded. |
| •  Size of the biggest crossload if you had a secondary chassis.                             |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                              |                       | crossloaded in the last scan.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | crossloaded in the last scan.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                              |                       | DINT GSV SSV                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | DINT GSV SSV                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Introduction

## Losing Communication while Bridging Via a Series B ControlNet Bridge Module

173

<!-- image -->

## Series B ControlNet Bridge Modules

This appendix explains the possible consequences of using a series B ControlNet Bridge module.

| Topic Page                                                                      |
|---------------------------------------------------------------------------------|
| Losing Communication while Bridging Via a Series B ControlNet Bridge Module 173 |
| Communication Stoppage While Using a Series B ControlNet Bridge Module 174      |

You can temporarily lose communication with a remote chassis if you use both these modules in the remote chassis:

- 1756-CNB/B or 1756-CNBR/B module

and

- 1756-DHRIO module that is connected to a remote I/O network.

## Communication Loss While Bridging

<!-- image -->

IMPORTANT

On the first switchover after you download a project to the controller, you may temporarily lose communications with these devices

## Communication Stoppage While Using a Series B ControlNet Bridge Module

The loss of communication happens on the first switchover after you download the project to the redundant controller.

- You lose communication with the remote chassis and any devices to which you were bridging via the chassis, such as the remote I/O modules.
- During the communication loss, the I/O modules go to their configured state for a communication fault.
- The communication loss is temporary. Communications restore themselves.

To prevent this situation, use series D or series E ControlNet Bridge modules.

All communication on a ControlNet network could stop if the lowest node is a 1756-CNB/B or 1756-CNBR/B module. This happens if you unplug or break the tap of the module while it is turned on.

## Module Corrective Action

|                                                                          | If Then                                                                                      |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Tap of a series B ControlNet Bridge module becomes unplugged or broken   | 1. Turn off the power to the module. 2. Replace the tap. 3. Turn on the power to the module. |
| Communication on the network stops because of an unplugged or broken tap | Cycle power to each primary controller on the network.                                       |

To prevent this situation, use series D or series E ControlNet Bridge modules.

## Loss of Communication

|                                                                               | Restriction Description                                                                                                                                                                                           |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Communication Loss When Bridging Through a Series B ControlNet Bridge Module. | You could temporarily lose communication with a remote chassis if you use both these modules in the chassis: •  1756-CNB/B or 1756-CNBR/B module. •  1756-DHRIO module that is connected to a remote I/O network. |

## Redundant Chassis Pair

<!-- image -->

## IMPORTANT

On the first switchover after you download a project to the controller, you may temporarily lose communications with these devices

The loss of communication occurs on the first switchover after you download the project to the redundant controller.

- You lose communication with the remote chassis and any devices to which you were bridging via the chassis, such as the remote I/O modules.
- During the communication loss, the I/O modules go to their configured state for a communication fault.
- The communication loss is temporary. Communications restore themselves.

To prevent this situation, use 1756-CNB/D/E or 1756-CNBR/D/E modules.

|                                                                                                                                          | Restriction Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If the lowest node is a 1756-CNB/B or -CNBR/B module, removing a tap or breaking a cable could stop all communications over the network. | If the lowest node on a ControlNet network is a 1756-CNB/B or 1756-CNBR/B module, all communications over the network could stop if a tap to the 1756-CNB or -CNBR/D module is disconnected or breaks and then is replaced while power is still applied to the the 1756-CNB/B or -CNBR/D module. If a tap to a 1756-CNB/B or -CNBR/B module becomes disconnected or broken, take these actions. 1. Turn off the power to the 1756-CNB/B or -CNBR/B module. 2. Replace the tap. If a communication failure occurs because of a disconnected or broken tap, cycle power to each primary controller on the network. To prevent this situation, use a 1756-CNB/D/E or -CNBR/D/E module as your lowest node on the network. |

## Introduction

## Redundant System Restrictions

177

## Redundant System Restrictions

This appendix explains the known restrictions affecting a redundant system.

## IMPORTANT

In a redundant system, use an EtherNet/IP network only for HMI/workstation communication and messaging.

Do not use an EtherNet/IP network for:

- communication with I/O modules.
- communication between devices via produced/consumed tags.

There are several restricted features and functions in a redundant system.

Do not use any of these features in a ControlLogix redundancy system.

- Local chassis I/O, 1756-DHRIO, or 1756-DNB modules.
- Event task.
- Inhibit a task.
- Motion control, such as these modules:
- – 1756-HYD02
- – 1756-L60M03SE
- – 1756-M02AE
- – 1756-M02AS
- – 1756-M03SE
- – 1756-M08SE
- – 1756-M16SE

## Notes:

## Numerics

## 1756-ENBT module

See ENBT module

1756-EWEB module

EWEB module

## 1757-SRM module

See SRM module

## A

## add

redundant components 33

additional redundant components 33

adjust

CPU usage 123

## attributes

redundancy object 169

auto-synchronization 61

## B

BSL instruction 82

BSR instruction 82

## C

## change

CNB module from series D to series E 129

## chassis

install 45

## check

connection requirements 35

## choose

time slice 120

## CNB module

addresses during a switchover 19 change from series D to series E 129 four-character display 124 install 46 requirements 22 , 29 usage 123

## communication

optimize 119

## configure

consumed tag 70

controller 68 EtherNet/IP module 50 message instruction 72 produced tag 70 SRM module 53

## connect

device via NAP 16

## connection requirements 35

## consumed tag

configure 70

## controller

configure 68

download project 95

install

46

nonvolatile memory 126

periodic task 122

program scan time 74

requirements 22 , 29

synchronize 51 , 118

system overhead time slice 120

## ControlLogix redundancy system

overview 13

## ControlNet network

keeper signature 99 , 107 lay out system 28 plan 35 redundant media 33 schedule 97

## conversion

to redundant system 163

## convert

local to remote modules 163

## CPU usage

adjust 123

## crossload 16 , 18

estimate time for 74

## D

## data

crossload 18 integrity 82

## DeviceNet network

design 21

## diagnose

disqualification 104 switchover 104

## disqualified

overview 16 troubleshoot 104

download 95

## E

## edit

edit online 18 , 65

## edit session in progress

troubleshoot 108

## ENBT module

addresses during a switchover 20

configure 50

requirements 23

## estimate program scan time 74 EtherNet/IP network

configure modules 50 design 21 IP swapping 20 module requirements 23 plan 38

proper use 177

## event log

export 115 interpret 109

## EWEB module

addresses during a switchover 20 configure 50 requirements 23

## export

event log 115

## F

## FFU instruction 82

## finalize

online edits 67

## firmware

update 51

## firmware combinations

redundant system 14

## G

Get System Value instruction 87

GSV instruction 87

## H

## HMI

configure tags 73 optimize communication 119

## I

## I/O

placement 21 , 31 , 49

## import

event log 115

## install

rails 49 remote chassis 49 system 43

## interpret

SRM event log 109

## IP address

assign 50

what happens during a switchover 20

## IP swapping

overview 20

## K

## keeper signature

check 99 update 107

## L

## load

project from nonvolatile memory 126 locked for update 138 locked switchover 138

## M

## message

configure 72 instruction 72 send to SRM module 91

## Microsoft Excel

import event log 115

## minimize

scan time 76

## modules

update 129

## MSG instruction 72

## N

## NAP 16

network access port 16

## nonvolatile memory

load a project 126 store a project 126

## O

## online edits

during a switchover 18 finalize 67 plan for 65

## open

SRM configuration tool 53

## operator interface terminals

placement 32

## overview

ControlLogix redundancy system 13

## P

## periodic task 122 place

I/O 31

operator interface terminals 32 pair of redundant chassis 30

## plan

ControlNet network 35

EtherNet/IP network 38

## power supplies

redundant 34

## primary chassis 15 produced tag

configure 70

## program

finalize online edits 67

## program scan time

estimate crossload time 74 minimize 76 overview 18

## project

download 95 edit online 18 load 126 store 126 storing while process is running 128

## proper use

EtherNet/IP network 177

## Q

## qualify. See synchronize

## R

## rails

install 49

## redundancy

convert existing system 163 object attributes 169

## redundant system

firmware combinations 14 power supplies 34 restrictions 177 update 129 update while offline 136

## remote chassis

install 49

## remote I/O network

design 21

## restrictions

redundant system 177

## revision 13

updating system 138

## RIO network

design 21

## S

## scan time

See program scan time, task scan time

## schedule

ControlNet network 97

## secondary chassis

troubleshoot 104

## set

SRM clock 56

task watchdog time 100

## set up

EtherNet/IP communication 147

## SRM clock

set 56

## SRM configuration tool

check the revision 55 open 53

## SRM module

auto-synchronization 61 configure 53 enable program control 62 export event log 115 install 46 interpret event log 109 program control 62 send message to 91

synchronize controllers 118

## status

of my redundancy system 87

## store

project to nonvolatile memory 126 project to nonvolatile memory while

process is running 128

## switchover

causes 15 data integrity 82 diagnose cause 104 run code after 89 test 59 troubleshoot 104 what happens to network addresses 19 , 20 what happens to online edits 18

## synchronize

controllers 51 , 118 diagnose failure 104 overview 16

## system

getting information 87 install 43 overhead time slice 120

## T

## task

number of 122 set watchdog time 100

## test

switchover 59

## test edits

finalize 67 what happens during a switchover 18

## troubleshoot

switchover 104

## U

## update

firmware 51 keeper signature 107 modules 129 offline redundant system 136 online redundant system 138 redundant systems 129 system that is already at revision 13 138

<!-- image -->

## How Are We Doing?

Your comments on our technical publications will help us serve you better in the future. Thank you for taking the time to provide us feedback.

You can complete this form and mail it back to us, visit us online at www.ab.com/manuals, or email us at RADocumentComments@ra.rockwell.com

Please complete the sections below. Where applicable, rank the feature (1=needs improvement, 2=satisfactory, and 3=outstanding) .

Pub. Title/

Type

ControlLogix Redundancy System

Cat. No. 1756-CNB/D/E, 1756-CNBR/D/E, 1756-ENBT,

1756-EWEB, 1756-L55, 1756-L55M12, 1756-L55M13,

1756-L55M14, 1756-L55M16, 1756-L55M22,

1756-L55M23, 1756-L55M24, 1756-L61, 1756-L62,

1756-L63, 1757-SRM

Pub. No. 1756-UM523F-EN-P Pub. Date

December 2006 Part No. 953030-15

Overall Usefulness

How can we make this publication more useful for you?

Completeness

(all necessary information is provided)

1 2 3 Can we add more information to help you?

- [ ] procedure/step

- [ ] illustration

- [ ] feature

- [ ] example

- [ ] guideline

- [ ] other

- [ ] explanation

- [ ] definition

Technical Accuracy

(all provided information is correct)

1 2 3 Can we be more accurate?

- [ ] text

- [ ] illustration

Clarity

(all provided information is easy to understand)

1 2 3 How can we make things clearer?

Other Comments

You can add additional comments on the back of this form.

Your Name

Location/Phone

Your Title/Function

Would you like us to contact you regarding your comments?

- [ ] \_\_\_No, there is no need to contact me

- [ ] \_\_\_Yes, please call me

- [ ] \_\_\_Yes, please email me at \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] \_\_\_Yes, please contact me via \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Return this form to: Allen-Bradley Marketing Communications, 1 Allen-Bradley Dr., Mayfield Hts., OH 44124-9705

Phone: 440-646-3176 Fax: 440-646-3525 Email: RADocumentComments@ra.rockwell.com

Publication ICCG-5.21- January 2001

Other Comments

PLEASE FOLD HERE

## BUSINESS REPLY MAIL

FIRST-CLASS MAIL PERMIT NO. 18235 CLEVELAND OH

POSTAGE WILL BE PAID BY THE ADDRESSEE

<!-- image -->

1 ALLEN-BRADLEY DR MAYFIELD HEIGHTS OH 44124-9705

<!-- image -->

<!-- image -->

## Rockwell Automation Support

Rockwell Automation provides technical information on the web to assist you in using our products. At http://support.rockwellautomation.com, you can find technical manuals, a knowledge base of FAQs, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools.

For an additional level of technical phone support for installation, configuration and troubleshooting, we offer TechConnect Support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://support.rockwellautomation.com.

## Installation Assistance

If you experience a problem with a hardware module within the first 24 hours of installation, please review the information that's contained in this manual. You can also contact a special Customer Support number for initial help in getting your module up and running:

|                       | United States 1.440.646.3223 Monday – Friday, 8am – 5pm EST                                    |
|-----------------------|------------------------------------------------------------------------------------------------|
| Outside United States | Please contact your local Rockwell Automation representative for any technical support issues. |

## New Product Satisfaction Return

Rockwell tests all of our products to ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned:

|                       | United States Contact your distributor. You must provide a Customer Support case number (see phone number above to obtain one) to your distributor in order to complete the return process.   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States | Please contact your local Rockwell Automation representative for return procedure.                                                                                                            |

Back Cover