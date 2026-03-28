<!-- image -->

## ControlLogix Analog I/O Modules

Catalog Numbers 1756-IF16, 1756-IF16K, 1756-IF6CIS, 1756-IF6I, 1756-IF8, 1756-IF8K, 1756-IR6I, 1756-IT6I, 1756-IT6I2, 1756-OF4, 1756-OF4K, 1756-OF6CI, 1756-OF6VI, 1756-OF8, 1756-OF8K

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

## IMPORTANT

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

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

Preface

## Table of Contents

|                                 | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9       |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                                 | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                           |
|                                 | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9         |
|                                 | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9       |
|                                 | Chapter 1                                                                                                                                  |
| ControlLogix Analog I/O Modules | I/O Modules in the ControlLogix System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                      |
| Overview                        | Module Identification and Status Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14                          |
|                                 | Preventing Electrostatic Discharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                  |
|                                 | Chapter 2                                                                                                                                  |
| Analog I/O Operation in the     | Ownership . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 |
| ControlLogix System             | Direct Connections . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . 17   |
|                                 | Input Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18          |
|                                 | Input Modules in a Local Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                |
|                                 | Real Time Sample (RTS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                  |
|                                 | Requested Packet Interval (RPI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                       |
|                                 | Triggering Event Tasks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                 |
|                                 | Input Modules in a Remote Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                   |
|                                 | Output Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21           |
|                                 | Output Modules in a Local Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                 |
|                                 | Output Modules in a Remote Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                    |
|                                 | Listen-only Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22     |
|                                 | Multiple Owners of Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                |
|                                 | Configuration Changes in an Input Module with Multiple Owners. . . . . . . . . . . . . . . . . . 23                                        |
|                                 | Chapter 3                                                                                                                                  |
| ControlLogix Analog I/O Module  | Common Analog I/O Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                |
| Features                        | Removal and Insertion Under Power (RIUP). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                                 |
|                                 | Module Fault Reporting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                 |
|                                 | Electronic Keying . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25             |
|                                 | Access to System Clock for Time Stamp Functions . . . . . . . . . . . . . . . . . . . . . . . . . 26                                       |
|                                 | Rolling Time Stamp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26               |
|                                 | Producer/Consumer Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                       |
|                                 | Status Indicator Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                    |
|                                 | Full Class I Division 2 Compliance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                       |
|                                 | Agency Certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27              |
|                                 | Field Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27           |
|                                 | Sensor Offset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27          |
|                                 | Latching of Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27              |
|                                 | Data Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28          |
|                                 | Module Inhibiting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28            |
|                                 | Relationship Between Module Resolution, Scaling, and Data Format. . . . . . . . . . . . . . . 29                                           |

|                                  | Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30   |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | Data Format as Related to Resolution and Scaling. . . . . . . . . . . . . . . . . . . . . . . . . . 30                                   |
|                                  | Chapter 4                                                                                                                                |
| Non-isolated Analog Voltage/     | Choose a Wiring Method. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33         |
| Current Input Modules (1756-IF16 | Single-ended Wiring Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                    |
| and 1756-IF8)                    | Differential Wiring Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                |
|                                  | High-speed Mode Differential Wiring Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                                |
|                                  | Choose a Data Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34        |
|                                  | Features Specific to Non-Isolated Analog Input Modules . . . . . . . . . . . . . . . . . . . . . . . . 34                                |
|                                  | Multiple Input Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34             |
|                                  | Module Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34       |
|                                  | Real-time Sampling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35             |
|                                  | Underrange/Overrange Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                         |
|                                  | Digital Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35    |
|                                  | Process Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36          |
|                                  | Rate Alarm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37      |
|                                  | Wire Off Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37           |
|                                  | Use Module Block and Input Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                         |
|                                  | Field-side Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41                 |
|                                  | Wire the 1756-IF16 Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43         |
|                                  | Wire the 1756-IF8 Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47        |
|                                  | 1756-IF16 Module Fault and Status Reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                       |
|                                  | Fault Reporting in Floating Point Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                          |
|                                  | Fault Reporting in Integer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                     |
|                                  | 1756-IF8 Module Fault and Status Reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                      |
|                                  | Fault Reporting in Floating Point Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                          |
|                                  | Fault Reporting in Integer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                     |
|                                  | Chapter 5                                                                                                                                |
| Non-isolated Analog Output       | Choose a Data Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61        |
| Modules (1756-OF4 and            | Non-isolated Output Module Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                   |
| 1756-OF8)                        | Ramping/Rate Limiting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                 |
|                                  | Hold for Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62           |
|                                  | Open Wire Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62             |
|                                  | Clamping/Limiting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62             |
|                                  | Clamp/Limit Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63              |
|                                  | Data Echo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63      |
|                                  | User Count Conversion to Output Signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                            |
|                                  | Use Module Block and Output Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                          |
|                                  | Field-side Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                 |
|                                  | Wire the 1756-OF4 Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67          |
|                                  | Wire the 1756-OF8 Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68          |
|                                  | 1756-OF4 and 1756-OF8 Module Fault and Status Reporting . . . . . . . . . . . . . . . . . . . . . . 69                                   |
|                                  | Fault Reporting in Floating Point Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69                          |
|                                  | Fault Reporting in Integer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                     |

|                               | Chapter 6                                                                                                                             |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Configure ControlLogix Analog | Create a New Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76    |
| I/O Modules                   | Module Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77        |
|                               | Modify the Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81     |
|                               | General Category. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81        |
|                               | Connection Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82            |
|                               | Module Info Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83           |
|                               | Channels Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84          |
|                               | Alarms Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87        |
|                               | Limits Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88      |
|                               | Calibration Category. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89          |
|                               | Download Configuration Data to the Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                    |
|                               | Reconfigure Parameters in Run Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                 |
|                               | Reconfigure Parameters in Program Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                     |
|                               | Configure I/O Modules in a Remote Chassis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                    |
|                               | View the Module Tags. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93    |
|                               | Chapter 7                                                                                                                             |
| Use Ladder Logic To Define    | Perform Runtime Services. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95        |
| Module Operation              | Add a Message Instruction to a Routine. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                        |
|                               | Configure the Message Instruction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                     |
|                               | Add Bit Instructions, Rungs, and Branches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                          |
|                               | Reconfigure a Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101     |
|                               | Chapter 8                                                                                                                             |
| Calibrate the ControlLogix    | Difference Between Calibrating Input and Output Modules. . . . . . . . . . . . . . . . . . . . . . 104                                |
| Analog I/O Modules            | Calibrating in Program Mode or Without a Connection . . . . . . . . . . . . . . . . . . . . . 104                                     |
|                               | Calibrate 1756-IF16 and 1756-IF8 Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                  |
|                               | Calibrate 1756-OF4 and 1756-OF8 Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                  |
|                               | Current Meter Calibrations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111             |
|                               | Analog to Digital (A/D) Converter Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117                  |
|                               | Calibrated Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118   |
|                               | Error Calculated Over Hardware Range . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                  |
|                               | How Operating Temperature Changes Affect Module Accuracy . . . . . . . . . . . . . . . . . . 119                                      |
|                               | Gain Drift With Temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119                 |
|                               | Module Error Over Full Temperature Range. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119                             |
|                               | Chapter 9                                                                                                                             |
| Troubleshoot Your Module      | Status Indicators for Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121             |
|                               | Status Indicators for Output Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122               |
|                               | Use Logix Designer Application for Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . 123                          |
|                               | Fault Type Determination. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125               |
|                               | Appendix A                                                                                                                            |
| Analog I/O Tag Definitions    | Access the Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127 |
|                               | Integer Mode Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128   |

Integer Input Tags. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128

|                               | Integer Output Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128          |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|                               | Integer Configuration Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129               |
|                               | Floating Point Mode Tags. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130      |
|                               | Floating Point Input Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130            |
|                               | Floating Point Output Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131               |
|                               | Floating Point Configuration Tags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                    |
|                               | Appendix B                                                                                                                           |
| 1492 AIFMs for Analog I/O     | Module Wiring Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135    |
| Modules                       | Pre-wired and AIFM Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136        |
|                               | Module-ready Pre-wired Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137            |
|                               | Appendix C                                                                                                                           |
| 6-channel Isolated Analog I/O | 1756-IF6CIS and 1756-IF6I Module Features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139                   |
| Modules                       | 1756-IF6CIS Module Isolated Power Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139                           |
|                               | Data Format Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140           |
|                               | Multiple Input Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140          |
|                               | Notch Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140   |
|                               | Real-time Sampling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141          |
|                               | Underrange/Overrange Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141                      |
|                               | Digital Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142 |
|                               | Process Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143       |
|                               | Rate Alarm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144   |
|                               | Wire Off Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145        |
|                               | Module Block and Input Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                          |
|                               | 1756-IF6CIS Module Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148              |
|                               | 1756-IF6I Module Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151            |
|                               | 1756-IF6CIS or 1756-IF6I Module Fault and Status Reporting . . . . . . . . . . . . . . . . . 154                                     |
|                               | 1756-OF6CI and 1756-OF6VI Module Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158                      |
|                               | Data Format Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158           |
|                               | Ramping/Rate Limiting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158              |
|                               | Hold for Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158        |
|                               | Clamping/Limiting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159          |
|                               | Clamp/Limit Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159           |
|                               | Data Echo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159   |
|                               | User Count Conversion to Output Signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159                         |
|                               | Module Block and Output Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160                           |
|                               | 1756-OF6CI Module Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163               |
|                               | 1756-OF6VI Module Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165               |
|                               | 1756-OF6CI and 1756-OF6VI Module Fault and Status Reporting . . . . . . . . . . . . . . 166                                          |
|                               | Calibrate 1756-IF6CIS and 1756-IF6I Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170                   |
|                               | Calibrating the 1756-IF6I for Voltage Applications . . . . . . . . . . . . . . . . . . . . . . . . . 170                             |
|                               | Calibrating the 1756-IF6CIS or 1756-IF6I for Current Applications . . . . . . . . . . . . 171                                        |
|                               | Calibrate 1756-OF6VI and 1756-OF6CI Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176                      |
|                               | Current Meter Calibrations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176              |

Voltage Meter Calibrations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180

## Appendix D

| 6-channel Temperature                               | 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Features. . . . . . . . . . . . . . . . . . . . . . . . . . . 187                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| measuring Isolated Analog I/O | Data Format Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187                      |
|                               | Multiple Input Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187                     |
| Modules                       | Notch Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188              |
|                               | Real-time Sampling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188                     |
|                               | Underrange/Overrange Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188                                 |
|                               | Digital Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189            |
|                               | Process Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190                  |
|                               | Rate Alarm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191              |
|                               | 10 Ohm Offset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191                 |
|                               | Wire Off Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192                   |
|                               | Sensor Type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193               |
|                               | Temperature Units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194                     |
|                               | Input Signal to User Count Conversion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194                                  |
|                               | Wire Length Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194                        |
|                               | Differences Between the 1756-IT6I and 1756-IT6I2 Modules . . . . . . . . . . . . . . . . . 195                                                  |
|                               | Module Block and Input Circuit Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199                                     |
|                               | 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Wiring . . . . . . . . . . . . . . . . . . . . . . . . . 201                                        |
|                               | 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Fault and Status Reporting . . . . . . . 205                                                        |
|                               | Configuring RTD and Thermocouple Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209                                  |
|                               | Configure the RTD Module (1756-IR6I). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209                                 |
|                               | Configure the Thermocouple Modules (1756-IT6I and 1756-IT6I2). . . . . . . . . . . . . 210                                                      |
|                               | Calibrate 1756-IR61 Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211                  |
|                               | Calibrate 1756-IT6I and 1756-IT612 Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215                             |
|                               | RTD and Thermocouple Error Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                               |
|                               | RTD Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220             |
|                               | Thermocouple Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                      |
|                               | Module Error at 25 °C (77 °F) (-12…+30 mV Range) . . . . . . . . . . . . . . . . . . . . . . . . . 221                                          |
|                               | Module Error at 25 °C (77 °F) (-12…+78 mV Range) . . . . . . . . . . . . . . . . . . . . . . . . . 224                                          |
|                               | Thermocouple Resolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227                   |
|                               | Module Resolution (-12…+30 mV Range) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227                                      |
|                               | Module Resolution (-12…+78 mV Range). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231                                     |
|                               | Dealing with Incorrect Thermocouple Temperature Readings . . . . . . . . . . . . . . . 233                                                      |
|                               | Appendix E                                                                                                                                      |
| Remote Connections Via a      | Using RSNetWorx and RSLogix 5000 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235                                   |
| ControlNet Network            | Remote Input Modules Connected Via a ControlNet Network . . . . . . . . . . . . . . . . . . . . 236                                             |
|                               | Remote Output Modules Connected Via a ControlNet Network. . . . . . . . . . . . . . . . . . . 237                                               |
|                               | Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239          |
|                               | Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . .241 |

## About This Publication

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

This manual describes how to install, configure, and troubleshoot your ControlLogix® analog I/O module.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication aren't in alignment with the movement toward inclusive language in technology. We're proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic  Page                                                                                           |
|-------------------------------------------------------------------------------------------------------|
| Added series and firmware revision information to non-isolated output module ramp rate information 61 |
| Added Important statement regarding the use of Pre-wired and AIFM Cables in harsh environments 136    |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

| Resource                                                                                          | Description                                                                                                                                  |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 1756 ControlLogix I/O Specifications, publication 1756-TD002                                      | Provides specifications for ControlLogix analog and digital I/O modules as well as the accessories that can be used with each.               |
| ControlLogix Power Supply Installation Instructions, publication 1756-IN619                       | Provides information about how to install a wide range of ControlLogix power supplies.                                                       |
| ControlLogix Chassis Installation Instructions, publication 1756-IN621                            | Provides information about how to install a wide range of ControlLogix chassis.                                                              |
| 1756 ControlLogix Analog I/O Modules Installation Instructions, publication 1756-IN063            | Provides information about how to install and wire 1756 ControlLogix analog I/O modules.                                                     |
| ControlLogix High Resolution Analog I/O Modules Installation Instructions, publication 1756-IN056 | Provides information about how to install and wire ControlLogix high resolution analog I/O modules.                                          |
| Migrating 6-channel to 8-channel 1756 Analog Modules, publication 1756-RM011                      | Provides information about how to migrate the 1756 Isolated Analog I/O 6-channel modules to the 8-channel modules.                           |
| ControlLogix Digital I/O Modules User Manual, publication 1756-UM058                              | Provides information about how to install, configure, and troubleshoot ControlLogix digital I/O modules.                                     |
| ControlNet to EtherNet/IP Migration Reference Manual, publication NET-RM001                       | Provides information to migrate from an existing ControlNet® network to an EtherNet/IP™ network.                                             |
| ControlLogix System User Manual, publication 1756-UM001                                           | Describes how to install, configure, program, and operate a ControlLogix system.                                                             |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                       | Provides general guidelines for installing a Rockwell Automation industrial system.                                                          |
|                                                                                                   | Product Certifications website, rok.auto/certifications. Provides declarations of conformity, certificates, and other certification details. |

## Notes:

<!-- image -->

## ControlLogix Analog I/O Modules Overview

This chapter provides an overview of the ControlLogix® analog I/O modules to explain to you how they operate.

ControlLogix analog I/O modules are interface modules that convert analog signals to digital values for inputs and convert digital values to analog signals for outputs. Controllers can then use these signals for control purposes.

By using the Producer/Consumer network model, ControlLogix analog I/O modules produce information when needed while providing additional system functions.

## ControlLogix Analog I/O Module Features

| Feature                                          | Description                                                                                                                                                                                                                                                                |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Removal and insertion under power (RIUP)         | You can remove and insert modules and removable terminal blocks (RTB) while power is applied.                                                                                                                                                                              |
| Producer/Consumer communication                  | This communication is an intelligent data exchange between modules and other system devices in which each module produces data without first being polled.                                                                                                                 |
| Rolling time stamp of data                       | A 15-bit module-specific rolling time stamp with millisecond resolution that indicates when data was sampled and/or applied. This time stamp can be used to calculate the interval between channel or field-side updates.                                                  |
| Multiple data formats                            | Analog I/O modules offer the option of IEEE 32-bit floating point or 16-bit integer data formats.                                                                                                                                                                          |
| Module resolution                                | Analog input modules use 16-bit resolution, and analog output modules offer 13…16- bit output resolution (depending on the module type), to detect data changes.                                                                                                           |
| Onboard features                                 | Scaling to engineering units, alarming, and under/overrange detection, are some examples of the I/O module features.                                                                                                                                                       |
| Calibration                                      | ControlLogix analog I/O module ships from the factory with factory calibration. You can recalibrate the module calibration on a channel-by-channel or module-wide basis to increase accuracy in customer-specific applications, if necessary.                              |
| Coordinated system time (CST) time stamp of data | A 64-bit system clock places a time stamp on the transfer of data between the module and its owner-controller within the local chassis.                                                                                                                                    |
| Agency Certification                             | Full agency certification for in any application that requires approval. Agency certification varies depending on the catalog number. For the latest I/O module specifications, see the 1756 ControlLogix I/O Modules Technical Specifications ,  publication 1756-TD002 . |

## I/O Modules in the ControlLogix System

ControlLogix modules mount in a ControlLogix chassis and use a removable terminal block (RTB) or a Bulletin 1492 interface module (IFM)(1) cable to connect to all field-side wiring.

This section assumes that you've selected and sized the components of your ControlLogix system. In addition to standard ControlLogix power supplies, ControlLogix Redundant Power Supplies are also available.

## IMPORTANT

The power requirements of series B and C 1756-OF4, 1756-OF4K, 1756OF8, or 1756-OF8K modules are higher than series A modules. Prior to module replacement, consider the following:

- The total power supply consumption of a system that includes one or more series B and C 1756-OF4, 1756-OF4K, 1756-OF8, or 1756-OF8K modules within a series C chassis, cannot exceed 75 W @ 60 °C (140 °F).
- The total power supply consumption of a system that includes one or more series B and C 1756-OF4, 1756-OF4K, 1756-OF8, or 1756-OF8K modules within a series B chassis, cannot exceed 75 W @ 55 °C (131 °F).

For more information on choosing the correct power supply for your ControlLogix system, see these resources:

- The ControlLogix Selection Guide, publication 1756-SG001, provides a high-level selection process for ControlLogix system components.
- The 1756 ControlLogix I/O Modules Technical Specifications, publication 1756-TD002 , provides detailed specifications for ControlLogix I/O modules that are needed to size a system.
- The Integrated Architecture® Builder (IAB) software from Rockwell Automation https:// www.rockwellautomation.com/en-us/support/product/product-selectionconfiguration/integrated-architecture-builder.html provides advanced selection assistance and a graphical interface for designing systems.
- The interactive spreadsheet available in Knowledgebase Technote, Sizing the ControlLogix Power Supply that lets you enter a chassis configuration and automatically calculates the total power supply consumption.

## IMPORTANT

You must have a support agreement with Rockwell Automation to access the Knowledgebase.

For more information, contact your local Allen-Bradley distributor or sales representative.

(1) The ControlLogix system has been agency certified using only the ControlLogix RTBs (1756-TBCH, 1756-TBNH, 1756-TBSH, and 1756-TBS6H). Any application that requires agency certification of the ControlLogix system using other wiring termination methods can require application-specific approval by the certifying agency. To see what analog interface modules are used with each ControlLogix analog I/O module, see Appendix B .

Before you install and use your module, do the following:

- Install and ground a 1756 chassis and power supply.

For information about how to install a wide range of ControlLogix power supplies, see publication 1756-IN619 .

For information about how to install a wide range of ControlLogix chassis, see publication 1756-IN621 .

- Order and receive the RTB or IFM and its components compatible for use with your application.

IMPORTANT

RTBs and IFMs aren't included with your module purchase.

## Parts of the ControlLogix Analog I/O Module

<!-- image -->

|    | Item Description                                                                                                                                           |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Backplane connector - Interface for the ControlLogix system that connects the module to the backplane.                                                     |
|  2 | Top and bottom guides - Guides provide assistance in seating the RTB or IFM cable onto the module.                                                         |
|  3 | Status indicators - Indicators display the status of communication, module health, and input/output devices. Indicators help in troubleshooting anomalies. |
|  4 | Connectors pins - Input/output, power, and grounding connections are made to the module through these pins with the use of an RTB or IFM.                  |
|  5 | Locking tab - The locking tab anchors the RTB or IFM cable on the module, maintaining wiring connections.                                                  |
|  6 | Slots for keying - Mechanically keys the RTB to help prevent inadvertently making the wrong wire connections to your module.                               |

## Module Identification and Status Information

Each ControlLogix I/O module maintains specific identification information that separates it from all other modules. This information assists you in tracking all system components.

For example, you can track module identification information to be aware of exactly what modules are in any ControlLogix rack at any time. While retrieving module identity, you can also retrieve the module's status.

## Module Identification and Status Information

| Item         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product Type | Module’s product type, such as Analog I/O                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Catalog Code | Module’s catalog number (1)                                                                                                                                                                                                                                                                                                                                                                                                                               |
|              | Major Revision Module’s major revision number                                                                                                                                                                                                                                                                                                                                                                                                             |
|              | Minor Revision Module’s minor revision number                                                                                                                                                                                                                                                                                                                                                                                                             |
| Status       | Module’s status that shows the following information: • Controller ownership (if any) • Whether the module has been configured Device Specific Status, such as: • Self-test • Update in progress • Communications fault • Not owned (outputs in program mode) • Internal fault (need update) • Run mode • Program mode (output modules only) • Minor recoverable fault • Minor unrecoverable fault • Major recoverable fault • Major nonrecoverable fault |
|              | Vendor ID Module manufacturer vendor, for example Allen-Bradley                                                                                                                                                                                                                                                                                                                                                                                           |
|              | Serial Number Module serial number                                                                                                                                                                                                                                                                                                                                                                                                                        |
|              | Length of ASCII Text String Number of characters in module’s text string                                                                                                                                                                                                                                                                                                                                                                                  |
|              | ASCII Text String Number of characters in module’s text string                                                                                                                                                                                                                                                                                                                                                                                            |

## IMPORTANT

You must perform a WHO service via RSLinx® Classic or FactoryTalk® Linx to retrieve this information.

## Preventing Electrostatic Discharge

This module is sensitive to electrostatic discharge.

<!-- image -->

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- If available, use a static-safe workstation.
- When not in use, store the equipment in appropriate static-safe packaging.

## Notes:

## Ownership

## Direct Connections

## Analog I/O Operation in the ControlLogix System

I/O modules are interfaces between the controller and the field devices that comprise the ControlLogix® system. Analog signals, which are continuous, are converted by the module and used by the controller to mandate field-device results.

This chapter describes how analog I/O modules operate within the ControlLogix system.

Every I/O module in the ControlLogix system must be owned by a ControlLogix controller. This owner-controller:

- stores configuration data for every module that it owns.
- can be local or remote in regard to the I/O module's position.
- sends the I/O module configuration data to define the module's behavior and begin operation within the control system.

Each ControlLogix I/O module must continuously maintain communication with its owner to operate normally.

Typically, each module in the system has one owner only. Input modules can have multiple owners. Output modules, however, are limited to a single owner.

For more information on the increased flexibility that is provided by multiple owners and the ramifications of using multiple owners, see page 23 .

ControlLogix analog I/O modules use direct connections only.

A direct connection is a real-time data transfer link between the controller and the device that occupies the slot that the configuration data references. When module configuration data is downloaded to an owner-controller, the controller attempts to establish a direct connection to each of the modules referenced by the data.

If a controller has configuration data referencing a slot in the control system, the controller periodically checks for the presence of a device there. When a device's presence is detected there, the controller automatically sends the configuration data, and one of the following events occurs:

- If the data is appropriate to the module found in the slot, a connection is made and operation begins.
- If the configuration data isn't appropriate, the data is rejected and an error message displays in the software. In this case, the configuration data can be inappropriate for any of a number of reasons.

For example, a module's configuration data can be appropriate except for a mismatch in electronic keying that helps prevent normal operation.

The controller maintains and monitors its connection with a module. Any break in the connection, such as removal of the module from the chassis while under power, causes the controller to set fault status bits in the data area associated with the module.

<!-- image -->

## Input Module Operation

## Input Modules in a Local Chassis

In traditional I/O systems, controllers poll input modules to obtain their input status. In the ControlLogix system, a controller does not poll analog input modules after a connection is established. Instead, the modules multicast their data periodically. The frequency depends on the options that are chosen during configuration and where in the control system that input module physically resides.

An input module's behavior varies depending upon whether it operates in the local chassis or in a remote chassis. The following sections detail the differences in data transfers between these set-ups.

When a module resides in the same chassis as the owner-controller, these two configuration parameters affect how and when an input module produces data.

## Real Time Sample (RTS)

This configurable parameter, which is set during the initial configuration by using the Studio 5000 Logix Designer® application, instructs the module to perform two basic operations:

1. Scan all of its input channels and store the data into onboard memory.
2. Multicast the updated channel data (and other status data) to the backplane of the local chassis.

Data Operations Under RTS Configuration

<!-- image -->

## Requested Packet Interval (RPI)

This configurable parameter also instructs the module to multicast its channel and status data to the local chassis backplane.

The RPI, however, instructs the module to produce the current contents of its onboard memory when the RPI expires (that is, the module does not update its channels before the multicast).

<!-- image -->

## IMPORTANT

The RPI value is set during the initial module configuration using the programming software. To avoid interrupting control and a temporary loss of connection, make adjustments to this value when the controller is in Program mode.

The module resets the RPI timer each time an RTS is performed. This operation dictates how and when the owner-controller in the local chassis receives updated channel data, depending on the values given to these parameters.

If the RTS value is less than or equal to the RPI, each multicast of data from the module contains updated channel information. The module is only multicasting at the RTS rate.

If the RTS value is greater than the RPI, the module produces at both the RTS rate and the RPI rate. Their respective values dictate how often the owner-controller receives data and how many multicasts from the module contain updated channel data.

## Input Modules in a Remote Chassis

In this example, the RTS value is 100 ms and the RPI value is 25 ms. Only every fourth multicast from the module contains updated channel data.

<!-- image -->

## Triggering Event Tasks

When configured, ControlLogix analog input modules can trigger an event task. The event task lets you execute a section of logic immediately when an event (that is, receipt of new data) occurs.

Your ControlLogix analog I/O module can trigger event tasks every RTS, after the module has sampled and multicast its data. Events tasks are useful for synchronizing process variable (PV) samples and proportional integral derivative (PID) calculations.

## IMPORTANT

ControlLogix analog I/O modules can trigger event tasks at every RTS but not at the RPI. For example, if the RTS value is 100 ms and the RPI value is 25 ms, an event task can be only triggered every 100 ms.

When remote analog input modules are connected to the owner-controller via an EtherNet/IP™ network, data is transferred to the owner-controller in the following way:

- At the RTS or RPI (whichever is faster), the module broadcasts data within its own chassis.
- The 1756 Ethernet bridge in the remote chassis immediately sends the module's data over the network to the owner-controller as long as it hasn't sent data within a time frame that is one-quarter the value of the analog input module's RPI.

For example, if an analog input module uses an RPI = 100 ms, the Ethernet module sends module data immediately on receiving it if another data packet wasn't sent within the last 25 ms.

The Ethernet module either multicasts the module's data to all devices on the network or unicasts to a specific owner-controller depending on the setting of the Unicast box, as shown on page 82 .

<!-- image -->

For more information, see the Guidelines to Specify an RPI Rate for I/O Modules section in the Logix5000 Controllers Design Considerations Reference Manual, publication 1756-RM094 .

If connecting via a ControlNet® network, refer to Appendix E .

## Output Module Operation

## Output Modules in a Local Chassis

## Output Modules in a Remote Chassis

The RPI parameter governs exactly when an analog output module receives data from the owner-controller and when the output module echoes data. An owner-controller sends data to an analog output module only at the period specified in the RPI. Data isn't sent to the module at the end of the controller's program scan.

When an analog output module receives new data from an owner-controller (that is, every RPI), the module automatically multicasts or 'echoes' a data value that corresponds to the analog signal present at the output terminals to the rest of the control system. This feature, called Output Data Echo, occurs whether the output module is local or remote.

Depending on the value of the RPI, the output module can receive and 'echo' data multiple times during one program scan regarding the length of the controller program scan.

When the RPI is less than the program scan length, the controller effectively allows the module's output channels to change values multiple times during a one program scan because the output module isn't dependent on reaching the end of the program to send data.

Specifying an RPI value for an analog output module instructs the controller when to broadcast the output data to the module. If the module resides in the same chassis as the ownercontroller, the module receives the data almost immediately after the controller sends it.

<!-- image -->

When remote analog output modules are connected to the owner-controller via an EtherNet/IP network, the controller multicasts data in the following ways:

- At the RPI, the owner-controller multicasts data within its own chassis.
- When the RPI timer expires or a programmed Immediate Output (IOT) instruction is executed. An IOT sends data immediately and resets the RPI timer.

If connecting via a ControlNet network, refer to Appendix E .

## Listen-only Mode

## Multiple Owners of Input Modules

Any controller in the system can listen to the data from any I/O module (that is, input data or 'echoed' output data) even if the controller does not own the module. In other words, the controller does not have to own a module's configuration data to listen to it.

During the I/O configuration process, you can specify one of several 'Listen-Only' modes on the Module Definition dialog box.

Choosing a 'Listen-Only' mode option allows the controller and module to establish communications without the controller sending any configuration data. In this instance, another controller owns the module being listened to.

## IMPORTANT

If a 'Listen-Only' connection is used by any controller to the module, any connections over the Ethernet network can't use the Unicast option. For more information regarding the Unicast box, see page 82 .

The 'Listen-Only' controller continues to receive multicast data from the I/O module as long as a connection between an owner-controller and an I/O module is maintained.

If the connection between all owner-controllers and the module is broken, the module stops multicasting data and connections to all 'Listening controllers' are also broken.

Because 'Listening controllers' lose their connections to modules when communication with the owner stops, the ControlLogix system lets you define multiple owners for input modules.

## IMPORTANT

Only input modules can have multiple owners. If multiple owners are connected to the same input module, they must maintain an identical configuration for that module.

In this example, Controller A and Controller B are configured as the owner of the input module.

<!-- image -->

When multiple controllers are configured to own the same input module, these events occur:

- When the controllers begin downloading configuration data, both try to establish a connection with the input module.
- Whichever controller's data arrives first establishes a connection.
- When the second controller's data arrives, the module compares it to its current configuration data (the data that is received and accepted from the first controller).
- If the configuration data that is sent by the second controller matches the configuration data that is sent by the first controller the connection is also accepted.
- If any parameter of the second configuration data differs from the first, the module rejects the connection and the programming software generates an error message.

The advantage of multiple owners over a 'Listen-only' connection is that, if either of the controllers lose the connection to the module, the module continues to operate and multicast data to the system because of the connection maintained by the other owner-controller.

## Configuration Changes in an Input Module with Multiple Owners

You must be careful when changing an input module's configuration data in a multiple owner scenario. When the configuration data is changed in one of the owners, for example, Controller A, and sent to the module, that configuration data is accepted as the new configuration for the module. Controller B continues to listen, unaware that any changes have been made in the module's behavior.

<!-- image -->

Controller B is unaware that the changes were made by Controller A.

## IMPORTANT

A popup screen in the programming software alerts you to the possibility of a multiple owner situation and lets you inhibit the connection before changing the module's configuration. When changing configuration for a module with multiple owners, we recommend that the connection is inhibited.

To help prevent other owners from receiving potentially erroneous data, do the following steps when changing a module's configuration in a multiple owner-controller scenario while online.

1. For each owner-controller, inhibit the controller's connection to the module, either in the software on the Connection category or the popup window warning of the multiple owner-controller condition.
2. Make the appropriate configuration data changes in the software.
3. Repeat steps 1 and 2 for all owner-controllers, making the exact same changes in all controllers.
4. Disable the Inhibit box in each owner's configuration.

## Notes:

## Common Analog I/O Features

<!-- image -->

## ControlLogix Analog I/O Module Features

This chapter describes features that are common to all ControlLogix® analog I/O modules.

ControlLogix analog input modules convert an analog signal, which is measured in either volts, millivolts, milliamps, or ohms, that's connected to the module's screw terminals into a digital value.

The digital value that represents the magnitude of the analog signal is then transmitted on the backplane to either a controller or other control entities.

ControlLogix output modules convert a digital value that is delivered to the module via the backplane into an analog signal of -10.5…10.5 volts or 0…21 milliamps.

The digital value represents the magnitude of the desired analog signal. The module converts the digital value into an analog signal and provides this signal on the module's screw terminals.

## Removal and Insertion Under Power (RIUP)

All ControlLogix I/O modules can be inserted and removed from the chassis while power is applied. This feature allows greater availability of the overall control system because, while the module is being removed or inserted, there's no additional disruption to the rest of the controlled process.

## Module Fault Reporting

ControlLogix analog I/O modules provide both hardware and software indications when a module fault has occurred. Each module has a status fault indicator. The Studio 5000 Logix Designer® application graphically displays this fault and includes a fault message that describes the nature of the fault. This feature lets you determine how your module has been affected and what action is to be taken to resume normal operation.

For more information on module fault reporting as it relates to specific modules, see Chapter 4 for information about the IF16 and IF8 modules, Chapter 5 for information about the OF4 and OF8 modules, and Appendix C and Appendix D for support with legacy modules.

## Electronic Keying

Electronic Keying reduces the possibility that you use the wrong device in a control system. It compares the device that is defined in your project to the installed device. If keying identifies an attribute that doesn't match, a fault occurs.

## Electronic Keying Device Attributes

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

For more detailed information on Electronic Keying, see Electronic Keying in Logix 5000™ Control Systems Application Technique, publication LOGIX-AT001 .

## Access to System Clock for Time Stamp Functions

Controllers within the ControlLogix chassis maintain a system clock. This clock is also known as the coordinated system time (CST). You can configure your analog I/O modules to access this clock and time stamp input data or output echo data when the module multicasts to the system. You decide how to time stamp data when you choose a Communication Format on the Module Definition dialog box. For more information, see page 77 .

This feature provides accurate calculations between events to help you identify the sequence of events in either fault conditions or in the course of normal I/O operations. The system clock can be used between multiple modules in the same chassis.

In systems using an EtherNet/IP™ network and 1588 Grandmaster time, the value of this time stamp is still the CST time. You must convert this CST value to Grandmaster time in the controller.

## Rolling Time Stamp

Each module maintains a rolling time stamp that is unrelated to the CST. The rolling time stamp is a continuously running 15-bit timer that counts in milliseconds.

For input modules, whenever a module scans its channels, it also records the value of the rolling time stamp. The user program can then use the last two rolling time stamp values and calculate the interval between receipt of data or the time when new data has been received.

For output modules, the rolling time stamp value is only updated when new values are applied to the Digital to Analog Converter (DAC).

## Producer/Consumer Model

By using the Producer/Consumer model, ControlLogix I/O modules can produce data without being polled by a controller first. The modules produce the data and any owner or listen-only controller device can consume it.

For example, an input module produces data and any number of processors can consume the data simultaneously. This eliminates the need for one processor to send the data to another processor.

## Status Indicator Information

ControlLogix analog I/O modules use status indicators to show the health and operational status a module.

## ControlLogix Analog I/O Module Status Indicators

| Status   | Description                                                                |
|----------|----------------------------------------------------------------------------|
|          | Calibration Display indicates when your module is in the calibration mode. |
| Module   | Display indicates the module’s communication status.                       |

For a list of status indicators and descriptions, see Chapter 9 .

## Full Class I Division 2 Compliance

ControlLogix analog I/O modules maintain CSA Class I Division 2 system certification. This allows a ControlLogix system to be in an environment other than one that's 100% hazard-free.

IMPORTANT

Do not pull modules under power or remove a powered RTB bed when a hazardous environment is present.

## Agency Certification

Any ControlLogix analog I/O modules that have obtained various agency certifications are marked as such. Ultimately, all analog modules are to obtain these agency approvals and display the according markings.

## Field Calibration

ControlLogix analog I/O modules can be calibrated on a channel-by-channel or module-wide basis. The Studio 5000 Logix Designer® application provides an interface to perform calibration.

For calibration procedures, see Chapter 8 .

## Sensor Offset

You can add this offset directly to the input or output during calibration calculation. The purpose of this feature is to let you compensate for any sensor offset errors that exist. Such offset errors are common in thermocouple sensors.

To set a sensor offset, see page 84 .

## Latching of Alarms

The latching feature allows analog I/O modules to latch an alarm in the set position once it has been triggered, even if the condition causing the alarm to occur disappears.

## Data Format

During initial configuration of any ControlLogix analog I/O module, you must choose a Communication Format. The format determines the data format of data that is exchanged between the owner-controller and the I/O module.

Some features may not be available for use with all data format options. For example, if you use an integer data format with the 1756-OF6CI module, the clamping feature isn't available for use. The data format limitations of various modules are described throughout this document.

## ControlLogix Analog I/O Module Communication Formats

| Format type Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integer This mode uses a 16-bit signed format and allows faster sampling rates while using less memory in the controller but also limits the availability of features on your module. The faster sampling rates and lower memory usage vary according to module and application type. For more information on the specific sampling rates, see the Module Filter section in the module-specific chapters. Memory usage can be up to 50% less than in floating point. |
| Floating point This mode uses a 32-bit IEEE floating point format and offers all module features.                                                                                                                                                                                                                                                                                                                                                                    |

<!-- image -->

We recommend that you use the floating point data format in most applications. Floating point is simpler to use. All ControlLogix analog I/O modules default to floating point when initially configured.

Use only the integer data format if your application requires faster sampling rates than offered in floating point or if your application memory is extremely limited.

## Module Inhibiting

Module inhibiting lets you indefinitely suspend a connection between an owner-controller and an analog I/O module. This process can occur in either of the following ways:

- You configure an I/O module but inhibit the module to prevent it from communicating with the owner-controller. In this case, the owner does not establish a connection and configuration isn't sent to the module until the connection is uninhibited.
- In your application, a controller already owns a module, has downloaded the configuration to the module, and is exchanging data over the connection between the devices. In this case, you can inhibit the module and the owner-controller behaves as if the connection to the module does not exist.

## IMPORTANT

Whenever you inhibit an output module, it enters the Program mode and all outputs change to the state configured for the Program mode. For example, if an output module is configured so that the state of the outputs change to zero during Program mode, whenever that module is inhibited, the outputs change to zero.

The following examples are instances that can require the use of module inhibiting:

- Multiple controllers own the same analog input module. A change is required in the module's configuration; however, the change must be made to the program in all controllers. In this case, you can:
- a. Inhibit the module.
- b. Change configuration in all controllers.
- c. Uninhibit the module.
- You want to update the firmware of an analog I/O module. We recommend you:
- a. Inhibit the module.
- b. Perform the upgrade.
- c. Uninhibit the module.
- You're using a program that includes a module that you do not physically possess yet, but you don't want the controller to look continuously for a module that doesn't exist yet. You can inhibit the module in the program until you can place it in the proper slot.

## Relationship Between Module Resolution, Scaling, and Data Format

This section describes the close relationship between module resolution, scaling, and data format.

## Module Resolution

Resolution is the smallest amount of change that the module can detect. Analog input modules are capable of 16-bit resolution. Output modules are capable of 13…16 bit resolution, depending on the module type.

The 16 bits represent 65,536 counts. This total is fixed but the operational range that you choose for your module determines the value of each count.

For example, the 1756-IF6I module has an available current range of 21 mA. If the range is divided by the number of counts to figure out the value of each count, one count is approximately 0.34 µA.

<!-- image -->

## IMPORTANT

Module resolution is fixed. It does not change regardless of what data format you choose or how you scale your module in floating point mode. Resolution is based on the module hardware and the range selected. If you use a limited range sensor, you don't change the module resolution.

This table lists the range and resolution of the analog I/O modules.

## Current Values Represented in Engineering Units

| Module                                         | Range                                  | Number of Significant Bits Resolution   |                                                     |
|------------------------------------------------|----------------------------------------|-----------------------------------------|-----------------------------------------------------|
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | +/- 10.25V 0…10.25V 0…5.125V 0…20.5 mA | 16 bits                                 | 320 µV/count 160 µV/count 80 µV/count 0.32 µA/count |
| 1756-IF6CIS                                    | 0 mA…21 mA 16 bits                     |                                         | 0.34 µA/count                                       |
| 1756-IF6I                                      | +/- 10.5V 0…10.5V 0…5.25V 0…21 mA      | 16 bits                                 | 343 µV/count 171 µV/count 86 µV/count 0.34 µA/count |
| 1756-IR6I                                      | 1…487  2…1000  4…2000  8…4020      | 16 bits                                 | 7.7 M/count 15 M/count 30 M/count 60 M/count    |
| 1756-IT6I and 1756-IT6I2                       | -12…+30 mV -12…+78 mV                  | 16 bits                                 | 0.7 µV/count 1.4 µV/count                           |
| 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K   | +/- 10.4V 0…21 mA                      | 16 bits                                 | 320 µV/count 325 nA/count                           |
| 1756-OF6VI                                     | +/- 10.5V                              | 14 bits                                 | 1.3 mV                                              |
| 1756-OF6CI                                     | 0…21 mA                                | 13 bits                                 | 2.7 µA                                              |

For information regarding the module resolution of the ControlLogix High Resolution Analog I/O Modules, see publication 1756-UM540 .

## IMPORTANT

Because these modules must allow for possible calibration inaccuracies, resolution values represent the available Analog to Digital or Digital to Analog counts over the specified range.

## Scaling

With scaling, you change a quantity from one notation to another. For ControlLogix analog I/O modules, scaling is only available with the floating point data format. When you scale a channel, you must choose two points along the module's operating range and apply low and high values to those points.

For example, if you're using the 1756-IF6I module in current mode, the module maintains a 0…21 mA range capability. But if your application uses a 4…20 mA transmitter, you can scale the module to represent 4 mA as the low signal and 20 mA as the high signal.

Scaling lets you configure the module to return data to the controller so that 4 mA returns a value of 0% in engineering units and 20 mA returns a value of 100% in engineering units.

## Module Resolution Compared to Module Scaling

<!-- image -->

## IMPORTANT

In choosing two points for the low and high value of your application, you do not limit the range of the module. The module's range and its resolution remain constant regardless of how you scale it for your application.

The module can operate with values beyond the 4…20 mA range.

If an input signal beyond the low and high signals is present at the module (that is, 3 mA), the data is represented in terms of the engineering units set during scaling. This table shows an example of the values that could appear.

## Current Values Represented in Engineering Units

| Current   | Engineering Units Value   |
|-----------|---------------------------|
| 3 mA      | -6.25%                    |
| 4 mA      | 0%                        |
| 12 mA     | 50%                       |
| 20 mA     | 100%                      |
| 21 mA     | 106.25%                   |

## Data Format as Related to Resolution and Scaling

This section describes the details of and differences between the integer mode and floating point mode data formats.

## Integer mode

This mode provides the most basic representation of analog data. When a module multicasts data in the integer mode, the low and high signals of the input range are fixed.

## IMPORTANT

Scaling isn't available in integer mode. The low signal of your application range equals -32,768 counts while the high signal equals 32,767 counts.

In integer mode, input modules generate digital signal values that correspond to a range from -32,768…+32,767 counts.

## Input Signal to User Count Conversion

|                                                |          |                             | Input Module Available Range Low Signal and User Counts High Signal and User Counts   |
|------------------------------------------------|----------|-----------------------------|---------------------------------------------------------------------------------------|
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | +/- 10V  | -10.25V -32768 counts       | 10.25V 32,767 counts                                                                  |
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | 0…10V    | 0V -32768 counts            | 10.25V 32,767 counts                                                                  |
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | 0…5V     | 0V -32768 counts            | 5.125V 32,767 counts                                                                  |
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | 0…20 mA  | 0 mA -32768 counts          | 20.58 mA 32,767 counts                                                                |
| 1756-IF6CIS 0…20 mA                            |          | 0 mA -32768 counts          | 21.09376 mA 32,767 counts                                                             |
| 1756-IF6I                                      | +/- 10V  | -10.54688V -32768 counts    | 10.54688V 32,767 counts                                                               |
| 1756-IF6I                                      | 0…10V    | 0V -32768 counts            | 10.54688V 32,767 counts                                                               |
| 1756-IF6I                                      | 0…5V     | 0V -32768 counts            | 5.27344V 32,767 counts                                                                |
| 1756-IF6I                                      | 0…20 mA  | 0 mA -32768 counts          | 21.09376 mA 32,767 counts                                                             |
| 1756-IR6I                                      | 1…487   | 0.859068653  -32768 counts | 507.862  32,767 counts                                                               |
| 1756-IR6I                                      | 2…1000  | 2  -32768 counts           | 1016.502  32,767 counts                                                              |
| 1756-IR6I                                      | 4…2000  | 4  -32768 counts           | 2033.780  32,767 counts                                                              |
| 1756-IR6I                                      | 8…4020  | 8  -32768 counts           | 4068.392  32,767 counts                                                              |
| 1756-IT6I and 1756-IT6I2                       | -12…30mV | -15.80323 mV -32768 counts  | 31.396 mV 32,767 counts                                                               |
| 1756-IT6I and 1756-IT6I2                       | -12…78mV | -15.15836 mV -32768 counts  | 79.241 mV 32,767 counts                                                               |

You can generate an analog signal at the screw terminals of an output module that corresponds to a range from -32,768…+32,767 counts.

This table lists the conversions a generated digital signal to the number of counts.

## Output Signal to User Count Conversion

|                                |         | Output Module Available Range Low Signal and User Counts High Signal and User Counts   |                          |
|--------------------------------|---------|----------------------------------------------------------------------------------------|--------------------------|
| 1756-OF4, 1756-OF4K, 1756-OF8, | 0…20 mA | 0 mA -32,768 counts                                                                    | 21.2916 mA 32,767 counts |
| 1756-OF8K                      | +/- 10V | -10.4336V -32,768 counts                                                               | 10.4336V 32,767 counts   |
| 1756-OF6CI 0…20 mA             |         | 0 mA -32,768 counts                                                                    | 21.074 mA 32,767 counts  |
| 1756-OF6VI +/- 10V             |         | -10.517V -32,768 counts                                                                | 10.517V 32,767 counts    |

## Floating point mode

This mode lets you change the data representation of the selected module. Although the full range of the module does not change, you can scale your module to represent I/O data in terms specific for your application.

For example, if you're using the 1756-IF6I module in floating point mode and choose an input range of 0 mA…20 mA, the module can use signals within the range of 0 mA…21 mA but you can scale the module to represent data between 4 mA…20 mA as the low and high signals in engineering units.

For an example of how to define data representation in engineering units through the programming software, see page 84 .

## Difference Between Integer and Floating Point

The key difference between choosing integer mode or floating point mode is that the integer is fixed between -32,768…+32,767 counts and floating point mode provides scaling to represent I/O data in specific engineering units for your application. Module resolution remains constant between the formats at 0.34 µA/count.

This table shows the difference in the data that is returned from the 1756-IF6I module to the controller between data formats. In this case, the module uses the 0 mA…20 mA input range with 4 mA scaled to 0% and 20 mA scaled to 100%.

## 1756-IF6I Module Using Different Data Types

| Signal Value   | Fixed Number of Counts in Integer Mode   | Data Representation in Floating Point Mode (Engineering Units)   |
|----------------|------------------------------------------|------------------------------------------------------------------|
| 0 mA           | -32,768 counts                           | -25%                                                             |
| 4 mA           | -20,341 counts                           | 0%                                                               |
| 12 mA          | 4514 counts                              | 50%                                                              |
| 20 mA          | 29,369 counts                            | 100%                                                             |
|                | 21.09376 mA 32,767 counts                | 106.25%                                                          |

## Choose a Wiring Method

<!-- image -->

## Non-isolated Analog Voltage/Current Input Modules (1756-IF16 and 1756-IF8)

This chapter describes features specific to ControlLogix® non-isolated, analog voltage/current input modules.

The non-isolated analog voltage/current input modules support all the features that are described in this chapter and Chapter 3 .

The 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules support single-ended, differential, and high-speed mode differential wiring methods.

Examples of each of these wiring methods on the 1756-IF16 and 1756-IF16K modules begin on page 43. Examples of each of these wiring methods on the 1756-IF8 and 1756-IF8K modules begin on page 47 .

## Single-ended Wiring Method

Single-ended wiring compares one side of the signal input to the signal ground. This difference is used by the module to generate digital data for the controller.

When using the single-ended wiring method, all input devices are tied to a common ground. The use of single-ended wiring and the common ground maximizes the number of usable channels on the module (eight channels for the 1756-IF8 and 1756-IF8K modules and 16 channels for the 1756-IF16 and 1756-IF16K modules).

## Differential Wiring Method

The differential wiring method is recommended for applications that can have separate signal pairs or a common ground isn't available. Differential wiring is recommended for environments where improved noise immunity is needed.

## IMPORTANT

This wiring method lets you use only half of the channels on a module. You can use only eight channels on the 1756-IF16 and 1756-IF16K modules and four channels on the 1756-IF8 and 1756-IF8K modules.

In differential mode, the channels aren't totally isolated from each other. If multiple differential input signals have different voltage common references, one channel could affect the reading of another channel. If this condition can't be avoided, then wire these inputs on different modules or replace the non-isolated module with an isolated input module.

## High-speed Mode Differential Wiring Method

You can configure the 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules for a high-speed mode that gives you the fastest data updates possible. When using the high-speed mode, remember these conditions:

- This mode uses the differential wiring method.
- This mode only allows use of one out of every four channels on the module.

Update times for applications that use the high-speed mode can be found on page 35 .

## Choose a Data Format

## Features Specific to Non-Isolated Analog Input Modules

Data format determines the format of the data that is returned from the module to the ownercontroller and the features that are available to your application. There are many possible Input Module Communication Formats to choose from when you configure your module.

When you choose a Communication Format, you can select one of two data formats:

- Integer mode
- Floating point mode

## Features Available in Each Data Format

| Data Format         | Features Available                                     | Features Not Available                               |
|---------------------|--------------------------------------------------------|------------------------------------------------------|
| Integer mode        | Multiple input ranges Module filter Real-time sampling | Process alarms Digital filtering Rate alarms Scaling |
| Floating point mode | All features                                           | See the following                                    |

## IMPORTANT

When using the 1756-IF16 or 1756-IF16K module in single-ended mode (that is, 16-channel mode) with a floating point data format, process and rate alarms aren't available.

This condition only exists when the 1756-IF16 or 1756-IF16K module is wired for single-ended mode. The 1756-IF8 or 1756-IF8K isn't affected.

The following features are specific to the 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules.

## Multiple Input Ranges

You can select from a series of operational ranges for each channel on your module. The range designates the minimum and maximum signals that are detectable by the module.

## 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K Module Input Ranges

| Module                                         | Possible Ranges             |
|------------------------------------------------|-----------------------------|
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | -10…+10V 0…5V 0…10V 0…20 mA |

For an example of how to choose an input range for your module, see page 84 .

## Module Filter

The module filter is a built-in feature of the analog-to-digital converter that attenuates the input signal, which begins at the specified frequency. This feature is applied on a module-wide basis.

The module attenuates the selected frequency by approximately -3 dB or 0.707 of the applied amplitude. This selected frequency is also called the bandwidth of the module.

An input signal with frequencies above the selected frequency is attenuated more, while frequencies below the selection receive no attenuation.

A by-product of the filter selection, in addition to frequency rejection, is the minimum sample rate (RTS) that is available. For example, in floating point mode, the 1000 Hz selection does not attenuate any frequencies less than

1000 Hz, but allows sampling of all 16 channels within 18 ms. But the

10 Hz selection attenuates all frequencies above 10 Hz and allows only sampling of all 16 channels within 488 ms.

## IMPORTANT

The default setting for the module filter is 60 Hz. This setting provides approximately 3 dB of filtering of a 60 Hz input.

See this table to choose a module filter setting.

## Filter Selections with Associated Performance Data

| Module Filter Setting (-3 dB) (1)(2)          | Wiring Mode                                       | 10 Hz                | 50…60 Hz (Default)   |                   |                                         | 100 Hz 250 Hz 1000 Hz   |
|-----------------------------------------------|---------------------------------------------------|----------------------|----------------------|-------------------|-----------------------------------------|-------------------------|
| Minimum sample time (RTS) Integer mode        | Single-ended Differential High-speed differential | 488 ms 244 ms 122 ms | 88 ms 44 ms 22 ms    | 56 ms 28 ms 14 ms | 28 ms 14 ms 7 ms                        | 16 ms 8 ms 5 ms         |
| Minimum sample time (RTS) Floating point mode | Single-ended Differential High-speed differential | 488 ms 244 ms 122 ms | 88 ms 44 ms 22 ms    | 56 ms 28 ms 14 ms | 28 ms 14 ms 7 ms                        | 18 ms 11 ms 6 ms        |
| Effective resolution                          |                                                   |                      |                      |                   | 16 bits 16 bits 16 bits 14 bits 12 bits |                         |

(1) For optimal 50…60 Hz noise rejection (&gt;80 dB), choose the 10 Hz filter.

(2) Worst case setting time to 100% of a step change is double the RTS sample times.

## Real-time Sampling

This parameter instructs the module how often to scan its input channels and obtain all available data. After the channels are scanned, the module multicasts that data. This feature is applied on a module-wide basis.

During module configuration, you specify a real-time sampling (RTS) period and a requested packet interval (RPI) period. Both of these features instruct the module to multicast data, but only the RTS feature instructs the module to scan its channels before multicasting.

## Underrange/Overrange Detection

This alarm feature detects when the non-isolated input module is operating beyond limits set by the input range. For example, if you're using the

1756-IF16 or 1756-IF16K module in the 0V…10V input range and the module voltage increases to 11V, the overrange detects this condition.

Table 13 shows the input ranges of non-isolated input modules and the lowest/highest signal available in each range before the module detects an underrange/overrange condition.

## Module Input Ranges and Lowest/Highest Signal

|                                                |                                 |                    | Input Module Available Range Lowest Signal in Range Highest Signal in Range   |
|------------------------------------------------|---------------------------------|--------------------|-------------------------------------------------------------------------------|
| 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K | +/- 10V 0V…10V 0V…5V 0 mA…20 mA | -10.25V 0V 0V 0 mA | 10.25V 10.25V 5.125V 20.5 mA                                                  |

## IMPORTANT

## Digital Filter

The digital filter smooths input data noise transients for all channels on the module. This feature is applied on a per channel basis.

Be careful when 'disabling all alarms' on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not 'disable all alarms'.

We recommend that you disable only unused channels so extraneous alarm bits aren't set.

Amplitude

The digital filter value specifies the time constant for a digital first order lag filter on the input. It's specified in units of milliseconds. A value of 0 disables the filter.

The digital filter equation is a classic first order lag equation.

<!-- formula-not-decoded -->

Yn = Present output, filtered peak voltage (PV)

Yn-1 =Previous output, filtered PV

t = Module channel update time (seconds)

TA = Digital filter time constant (seconds)

Xn = Present input, unfiltered PV

This illustration uses a step input change to illustrate the filter response. You can see that when the digital filter time constant elapses, 63.2% of the total response is reached. Each additional time constant achieves 63.2% of the remaining response.

<!-- image -->

To see how to set the Digital Filter, see page 84 .

## Process Alarms

Process alarms alert you when the module has exceeded configured high or low limits for each channel. You can latch process alarms. These are set at four user configurable alarm trigger points.

- High high
- High
- Low
- Low low

## IMPORTANT

## Alarm Deadband

You can configure an alarm deadband to work with the process alarms. The deadband allows the process alarm status bit to remain set, despite the disappearance of the alarm condition, as long as the input data remains within the deadband of the process alarm.

Process alarms aren't available in integer mode or in applications using a 1756-IF16 or 1756-IF16K module in the single-ended, floating point mode. The values for each limit are entered in scaled engineering units.

This illustration shows input data that sets each of the four alarms at some point during module operation. In this example, latching is disabled; therefore, each alarm turns Off when the condition that caused it to set ceases to exist.

<!-- image -->

To see how to set Process Alarms, see page 87 .

## Rate Alarm

The rate alarm triggers if the rate of change between input samples for each channel exceeds the specified trigger point for that channel.

## IMPORTANT

Rate alarms aren't available in integer mode or in applications that use a 1756-IF16 or 1756-IF16K module in the single-ended, floating point mode. The values for each limit are entered in scaled engineering units.

For example, if you set the 1756-IF16 or 1756-IF16K module (with normal scaling in volts) to a rate alarm of 1.0 V/s, the rate alarm only triggers if the difference between measured input samples changes at a rate &gt; 1.0 V/s.

If the module's RTS is 100 ms (that is, sampling new input data every 100 ms) and at time 0, the module measures 5.0 volts and at time 100 ms measures

5.08V, the rate of change is (5.08V - 5.0V) / (100 ms) = 0.8 V/s. The rate alarm does not set as the change is less than the trigger point of 1.0 V/s.

If the next sample taken is 4.9V, the rate of change is (4.9V…5.08V)/ (100 ms)=-1.8V/s. The absolute value of this result is &gt; 1.0V/s, so the rate alarm sets. Absolute value is applied because the rate alarm checks for the magnitude of the rate of change being beyond the trigger point, whether a positive or negative excursion.

## Wire Off Detection

The 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules alert you when a signal wire only has been disconnected from one of its channels or the RTB has been removed from the module. When a wire-off condition occurs for this module, two events occur:

- Input data for that channel changes to a specific scaled value.
- A fault bit is set in the owner-controller that can indicate the presence of a wire-off condition.

Because the 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules can be applied in voltage or current applications, differences exist as to how a wire-off condition is detected in each application.

## IMPORTANT

Be careful when 'disabling all alarms' on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not 'disable all alarms'.

We recommend that you disable only unused channels so extraneous alarm bits aren't set.

This table details the events that occur when a wire-off condition occurs in various applications.

## Wire-Off Conditions

| Condition                         | Events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Single-ended Voltage Applications • Input data for odd-numbered channels changes to the scaled value associated with the underrange signal value of the selected operational range in floating point mode (minimum possible scaled value) or -32,767 counts in integer mode The ChxUnderrange (x = channel number) tag is set to 1 • Input data for even-numbered channels changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,767 counts in integer mode |
| Single-Ended Current              | The ChxOverrange (x= channel number) tag (1) is set to 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Differential Voltage              | • Input data for that channel changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,768 counts in integer mode The ChxOverrange (x= channel number) tag is set to 1                                                                                                                                                                                                                                                                                         |
| Differential Current Applications | • Input data for that channel changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,768 counts in integer mode The ChxOverrange (x= channel number) tag is set to 1                                                                                                                                                                                                                                                                                         |

In current applications, wire-off detection occurs for one of the following reasons:

Because the RTB has been disconnected from the module

Both the signal wire and/or the jumper wire have been disconnected

## Use Module Block and Input Circuit Diagrams

This section shows the block diagrams for 1756-IF16 and 1756-IF16K series A and B modules.

## 1756-IF16/A, 1756-IF16K/A Module Block Diagram

<!-- image -->

## 1756-IF16/B, 1756-IF16K/B Module Block Diagram

<!-- image -->

This section shows the block diagrams for 1756-IF8 and 1756-IF8K series A and B modules.

## 1756-IF8/A, 1756-IF8K/A Module Block Diagram

<!-- image -->

## 1756-IF8/B, 1756-IF8K/B Module Block Diagram

<!-- image -->

## Field-side Circuit Diagrams

The field-side circuit diagrams are the same for 1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K modules.

1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K Module Voltage Input Circuit Diagram

1756-IF16, 1756-IF16K, 1756-IF8, and 1756-IF8K Module Current Input Circuit Diagram

<!-- image -->

<!-- image -->

## Wire the 1756-IF16 Module

This section shows current and voltage wiring examples for the 1756-IF16 module.

## 1756-IF16, 1756-IF16K Module Differential Current Wiring Example

<!-- image -->

Reference this table when wiring your 1756-IF16 or 1756-IF16K module in differential mode.

## 1756-IF16, 1756-IF16K Module Differential Current Wiring Reference

| Channel Terminals                     | Channel Terminals                                                              |
|---------------------------------------|--------------------------------------------------------------------------------|
| Channel 0 IN-0 (+), IN-1 (-) & iRTN-0 | Channel 4 IN-8 (+), IN-9 (-) & iRTN-8                                          |
|                                       | Channel 1 IN-2 (+), IN-3 (-) & iRTN-2 Channel 5 IN-10 (+), IN-11 (-) & iRTN-10 |
|                                       | Channel 2 IN-4 (+), IN-5 (-) & iRTN-4 Channel 6 IN-12 (+), IN-13 (-) & iRTN-12 |
| Channel 3 IN-6 (+), IN-7 (-) & iRTN-6 | Channel 7 IN-14 (+), IN-15 (-) & iRTN-14                                       |

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- A 249  current loop resistor is between IN-x and iRTN-x terminals.
- If multiple (+) or multiple (-) terminals are tied together, connect that tie point to an RTN terminal to maintain the accuracy of the module.
- Place additional loop devices (strip chart recorders, so forth) at the A location in the current loop.
- Do not connect more than two wires to any single terminal.

## IMPORTANT

When operating in four-channel, high-speed mode, only use channels 0, 2, 4 and 6.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF16, 1756-IF16K Module Differential Voltage Wiring Example

<!-- image -->

Reference this table when wiring your 1756-IF16 or 1756-IF16K module in differential mode.

## 1756-IF16, 1756-IF16K Module Differential Voltage Wiring

| Channel Terminals             | Channel Terminals               |
|-------------------------------|---------------------------------|
| Channel 0 IN-0 (+) & IN-1 (-) | Channel 4 IN-8 (+) & IN-9 (-)   |
| Channel 1 IN-2 (+) & IN-3 (-) | Channel 5 IN-10 (+) & IN-11 (-) |
| Channel 2 IN-4 (+) & IN-5 (-) | Channel 6 IN-12 (+) & IN-13 (-) |
| Channel 3 IN-6 (+) & IN-7 (-) | Channel 7 IN-14 (+) & IN-15 (-) |

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- Terminals marked iRTN aren't used for differential voltage wiring.
- In general, RTN is not used in differential circuits. However, if multiple (+) or multiple (-) terminals are tied together, connect that tie point to an RTN terminal to maintain the module's accuracy.
- Do not connect more than two wires to any single terminal.

## IMPORTANT

When operating in four-channel, high-speed mode, only use channels 0, 2, 4 and 6.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF16, 1756-IF16K Module Single-ended Current Wiring Example

<!-- image -->

Reference this table when wiring your 1756-IF16 or 1756-IF16K module in single-ended current mode.

## 1756-IF16, 1756-IF16K Module Single-ended Current Wiring

| Channel Terminals                                                         | Channel Terminals                                                            |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Channel 0 IN-0 (+), iRTN-0 (-) & RTN Channel 8 IN-8 (+), iRTN-8 (-) & RTN |                                                                              |
|                                                                           | Channel 1 IN-1 (+), iRTN-1 (-) & RTN Channel 9 IN-9 (+), iRTN-9 (-) & RTN    |
|                                                                           | Channel 2 IN-2 (+), iRTN-2 (-) & RTN Channel 10 IN-10 (+), iRTN-10 (-) & RTN |
|                                                                           | Channel 3 IN-3 (+), iRTN-3 (-) & RTN Channel 11 IN-11 (+), iRTN-11 (-) & RTN |
|                                                                           | Channel 4 IN-4 (+), iRTN-4 (-) & RTN Channel 12 IN-12 (+), iRTN-12 (-) & RTN |
|                                                                           | Channel 5 IN-5 (+), iRTN-5 (-) & RTN Channel 13 IN-13 (+), iRTN-13 (-) & RTN |
|                                                                           | Channel 6 IN-6 (+), iRTN-6 (-) & RTN Channel 14 IN-14 (+), iRTN-14 (-) & RTN |
| Channel 7 IN-7 (+), iRTN-7 (-) & RTN                                      | Channel 15 IN-15 (+), iRTN-15 (-) & RTN                                      |

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- For current applications, all terminals marked iRTN must be wired to terminals marked RTN.
- A 249  current loop resistor is between IN-x and iRTN-x terminals.
- Place additional loop devices (strip chart recorders, so forth) at the A location in the current loop.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF16, 1756-IF16K Module Single-ended Voltage Wiring Example

<!-- image -->

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- Terminals marked iRTN aren't used for single-ended voltage wiring.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## Wire the 1756-IF8 Module

This section details current and voltage wiring examples for the 1756-IF8 or 1756-IF8K module.

## 1756-IF8, 1756-IF8K Module Differential Current Wiring Example - Four Channels

<!-- image -->

Reference this table when wiring your 1756-IF8 or 1756-IF8K module in differential mode.

1756-IF8, 1756-IF8K Module Differential Current Wiring

| Channel   | Terminals                   |
|-----------|-----------------------------|
| Channel 0 | IN-0 (+), IN-1 (-) & iRTN-0 |
| Channel 1 | IN-2 (+), IN-3 (-) & iRTN-2 |
| Channel 2 | IN-4 (+), IN-5 (-) & iRTN-4 |
| Channel 3 | IN-6 (+), IN-7 (-) & iRTN-6 |

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- A 249  current loop resistor is between IN-x and iRTN-x terminals.
- If multiple (+) or multiple (-) terminals are tied together, connect that tie point to an RTN terminal to maintain the module's accuracy.
- Place additional loop devices (strip chart recorders, so forth) at the A location in the current loop.
- Do not connect more than two wires to any single terminal.

## IMPORTANT

When operating in two-channel, high-speed mode, only use channels 0 and 2.

## 1756-IF8, 1756-IF8K Module Differential Voltage Wiring Example - Four Channels

<!-- image -->

Reference this table when wiring your 1756-IF8 or 1756-IF8K module in differential mode.

1756-IF8, 1756-IF8K Module Differential Voltage Wiring

| Channel   | Terminals           |
|-----------|---------------------|
| Channel 0 | IN-0 (+) & IN-1 (-) |
| Channel 1 | IN-2 (+) & IN-3 (-) |
| Channel 2 | IN-4 (+) & IN-5 (-) |
| Channel 3 | IN-6 (+) & IN-7 (-) |

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- Terminals marked iRTN aren't used for differential voltage wiring.
- In general, RTN is not used in differential circuits. However, if multiple (+) or multiple (-) terminals are tied together, connect that tie point to an RTN terminal to maintain the module's accuracy.
- Do not connect more than two wires to any single terminal.

## IMPORTANT

When operating in two-channel, high-speed mode, only use channels 0 and 2.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF8, 1756-IF8K Module Single-ended Current Wiring Example

<!-- image -->

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- For current applications, all terminals marked iRTN must be wired to terminals marked RTN.
- A 249  current loop resistor is between IN-x and iRTN-x terminals.
- Place additional loop devices (strip chart recorders, so forth) at the A location in the current loop.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF8, 1756-IF8K Module Single-ended Voltage Wiring Example

<!-- image -->

## Keep in mind the following:

- All terminals marked RTN are connected internally.
- Terminals marked iRTN aren't used for single-ended voltage wiring.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF16 Module Fault and Status Reporting

The 1756-IF16 and 1756-IF16K modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a manner as to let you choose the level of granularity you desire when examining fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                                                                                                                                                                                                                                                                      |
| Channel Fault Word   | This word provides underrange, overrange, and communication fault reporting. Its tag name is ChannelFaults. When examining the Channel Fault Word for faults, remember the following: • 16 channels are used in single-ended wiring. • Eight channels are used in differential wiring. • Four channels are used in high-speed differential wiring. • All bytes start with bit 0. |
| Channel Status Words | These words provide individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults.                                                                                                                                                                                                                                         |
| IMPORTANT            | Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.                                                                                                                                                                                                              |

## Module Fault Word

(described on page 52)

15 = AnalogGroupFault

10 = Calibrating

9 = CalFault

14, 13, 12, &amp; 11 aren't used

## Channel Fault Word

## (described on page 53)

15 = Ch15Fault

14 = Ch14Fault

13 = Ch13Fault

12 = Ch12Fault

11 = Ch11Fault

10 = Ch10Fault

9 = Ch9Fault

7 = Ch7Fault

6 = Ch6Fault

5 = Ch5Fault

4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

8 = Ch8Fault

0 = Ch0Fault

16 channels are used in S.E. wiring Eight channels are used in Diff. wiring Four channels are used in H.S. Diff. wiring All start at bit 0

Channel Status Words (one for each channel, described on page 53)

7 = ChxCalFault

6 = ChxUnderrange

5 = ChxOverrange

4 = ChxRateAlarm

3 = ChxLAlarm

2 = ChxHAlarm

1 = ChxLLAlarm

0 = ChxHHAlarm

.

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. ts tag name is CalFault.                                          |

## Fault Reporting in Floating Point Mode

This illustration provides an overview of the fault reporting process for the 1756-IF16 or 1756-IF16K module in floating point mode.

<!-- image -->

1756-IF16, 1756-IF16K Module Fault Word Bits – Floating Point Mode

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-IF16, 1756-IF16K Channel Fault Word Bits – Floating Point Mode

During normal module operation, bits in the Channel Fault word are set if any of the respective channels has an Under or Overrange condition. A quick way to check for Under or Overrange conditions on the module is to check this word for a nonzero value.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

| Condition                                                                  | Display                                                                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                              | • ‘FFFF’ for single-ended operating mode • ‘00FF’ for differential operating mode • ‘000F’ for high-speed differential operating mode |
| A communication fault occurred between the module and its owner-controller | ‘FFFF’ for all bits, regardless of the application                                                                                    |

Your logic can monitor the Channel Fault word bit for a particular input to determine the state of that point.

## 1756-IF16, 1756-IF16K Channel Status Word Bits – Floating Point Mode

Any of the Channel Status words, one for each channel, display a nonzero condition if that particular channel has faulted under certain conditions. Some of these bits set bits in other Fault words. When the Underrange or Overrange bits (bits 6 and 5) in any of the words are set, the appropriate bit is set in the Channel Fault word.

This table lists the conditions that set each of the word bits.

|               |      | Tag (Status Word) Bit Event That Sets This Tag                                                                                                                                                                                                                                                                                                     |
|---------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxCalFault 7 |      | This bit is set if an error occurs during calibration for that channel and causes a bad calibration. This bit also sets bit 9 in the Module Fault word.                                                                                                                                                                                            |
| Underrange 6  |      | This bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word.                                                                                 |
| Overrange 5   |      | This bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see on page 35. This bit also sets the appropriate bit in the Channel Fault word.                                                                           |
| ChxRateAlarm  | 4(1) | This bit is set when the input channel’s rate of change exceeds the configured Rate Alarm parameter. It remains set until the rate of change drops below the configured rate. If latched, the alarm remains set until it’s unlatched.                                                                                                              |
| ChxLAlarm     | 3(1) | This bit is set when the input signal moves beneath the configured Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.         |
| ChxHAlarm     | 2(1) | This bit is set when the input signal moves above the configured High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.          |
| ChxLLAlarm    | 1 (1)      | This bit is set when the input signal moves beneath the configured Low-Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |
| ChxHHAlarm    | 0(1) | This bit is set when the input signal moves above the configured High-High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |

(1) Bits 0…4 aren't available in floating point, single-ended mode.

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-IF16 or 1756-IF16K module in integer mode.

<!-- image -->

16 channels are used in S.E. wiring Eight channels are used in Diff. wiring Four channels are used in H.S. Diff. wiring All start at bit 31

1756-IF16, 1756-IF16K Module Fault Word Bits – Integer Mode

In integer mode, Module Fault word bits (bits 15…9) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

## 1756-IF16, 1756-IF16K Channel Fault Word Bits – Integer Mode

In integer mode, Channel Fault word bits operate exactly as described in floating point mode.

This table lists the conditions that set all Channel Fault word bits in integer mode.

| Condition                                                                        | Channel Fault Word Bits                                                                                                               |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                                    | • ‘FFFF’ for single-ended operating mode • ‘00FF’ for differential operating mode • ‘000F’ for high-speed differential operating mode |
| A communications fault that occurred between the module and its owner-controller | ‘FFFF’ for all bits, regardless of the application                                                                                    |

Your logic can monitor the Channel Fault word bit for a particular input to determine the state of that point.

## 1756-IF16, 1756-IF16K Channel Status Word Bits – Integer Mode

The Channel Status word has these differences when the 1756-IF16 or 1756-IF16K module is used in integer mode.

- The module only reports Underrange and Overrange conditions.
- Alarming and Calibration Fault activities aren't available, although the Calibration Fault bit in the Module Fault word activates if a channel isn't properly calibrated.
- There's one, 32-bit Channel Status word for all 16 channels.

This table lists the conditions that set each of the word bits.

| Tag (Status Word) Bit   |                                                                                                                                    | Event That Sets This Tag                                                                                                                                                                                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxUnderrange           | Odd-numbered bits from 31…1 (bit 31 represents channel 0). For a full listing of the channels these bits represent, see page 54 .  | The underrange bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word.   |
| ChxOverrange            | Even-numbered bits from 30…0 (bit 30 represents channel 0). For a full listing of the channels these bits represent, see page 54 . | The overrange bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word. |

## 1756-IF8 Module Fault and Status Reporting

The 1756-IF8 and 1756-IF8K modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a manner as to let you choose the level of granularity that is desired when you examine fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                                                                                                                                                                                                                                                                       |
| Channel Fault Word   | This word provides underrange, overrange, and communication fault reporting. Its tag name is ChannelFaults. When examining the Channel Fault Word for faults, remember the following: • Eight channels are used in single-ended wiring. • Four channels are used in differential wiring. • Two channels are used in high-speed differential wiring. • All bytes start with bit 0. |
| Channel Status Words | These words provide individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults.                                                                                                                                                                                                                                          |

## IMPORTANT

Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.

## Module Fault Word (described on page 57)

15 = AnalogGroupFault

10 = Calibrating

9 = CalFault

14, 13, 12, and 11 aren't used

## Channel Fault Word

## (described on page 58)

7 = Ch7Fault

6 = Ch6Fault

5 = Ch5Fault

4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

0 = Ch0Fault

Eight channels are used in S.E. wiring Four channels are used in Diff. wiring Two channels are used in H.S. Diff. wiring All start at bit 0

Channel Status Words (One for each channel, described on page 58)

7 = ChxCalFault

6 = ChxUnderrange

5 = ChxOverrange

4 = ChxRateAlarm

3 = ChxLAlarm

2 = ChxHAlarm

1 = ChxLLAlarm

0 = ChxHHAlarm

## Fault Reporting in Floating Point Mode

This illustration shows an example of the fault reporting process for the 1756-IF8 or 1756-IF8K module in floating point mode.

<!-- image -->

The number of channel status words is dependent on the communication method used

1756-IF8, 1756-IF8K Module Fault Word Bits – Floating Point Mode

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module.

This table lists tags that you can further examine in ladder logic to isolate the fault.

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

## 1756-IF8, 1756-IF8K Channel Fault Word Bits – Floating Point Mode

During normal module operation, bits in the Channel Fault word are set if any of the respective channels has an Under or Overrange condition. A quick way to check for Under or Overrange conditions on the module is to check this word for a nonzero value.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

| Condition                                                                  | Display                                                                                                                                              |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                              | • ‘00FF’ for single-ended wiring applications • ‘000F’ for differential wiring applications • ‘0003’ for high-speed differential wiring applications |
| A communication fault occurred between the module and its owner-controller | ‘FFFF’ for all bits, regardless of the application                                                                                                   |

Your logic can monitor the Channel Fault word bit for a particular input to determine the state of that point.

## 1756-IF8, 1756-IF8K Channel Status Word Bits – Floating Point Mode

Any of the Channel Status words, one for each channel, display a nonzero condition if that particular channel has faulted for the conditions that are listed in the following table. Some of these bits set bits in other Fault words. When the Underrange and Overrange bits (bits 6…5) in any of the words are set, the appropriate bit is set in the Channel Fault word.

When the Calibration Fault bit (bit 7) is set in any of the words, the Calibration Fault bit (bit 9) is set in the Module Fault word.

This table lists the conditions that set each of the word bits.

|                | Tag (Status Word) Bit Event That Sets This Tag                                                                                                                                                                                                                                                                                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxCalFault 7  | This bit is set if an error occurs during calibration for that channel, which causes a bad calibration. This bit also sets bit 9 in the Module Fault word.                                                                                                                                                                                         |
| Underrange 6   | This bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word.                                                                                 |
| Overrange 5    | This bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word.                                                                              |
| ChxRateAlarm 4 | This bit is set when the input channel’s rate of change exceeds the configured Rate Alarm parameter. It remains set until the rate of change drops below the configured rate. If latched, the alarm remains set until it’s unlatched.                                                                                                              |
| ChxLAlarm 3    | This bit is set when the input signal moves beneath the configured Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.         |
| ChxHAlarm 2    | This bit is set when the input signal moves above the configured High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.          |
| ChxLLAlarm 1   | This bit is set when the input signal moves beneath the configured Low-Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |
| ChxHHAlarm 0   | This bit is set when the input signal moves above the configured High-High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |

## Module Fault Word

(described on page 59)

15 = AnalogGroupFault

10 = Calibrating

9 = CalFault

14, 13, 12, &amp; 11 aren't used by 1756-IF8 or 1756-IF8K

## Channel Fault Word (described on page 60)

7 = Ch7Fault

6 = Ch6Fault

5 = Ch5Fault

4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

0 = Ch0Fault

Eight channels are used in S.E. wiring Four channels are used in Diff. wiring Two channels are used in H.S. Diff. wiring All start at bit 0

## Channel Status Word (described on page 60)

31 = Ch0Underrange

30 = Ch0Overrange

29 = Ch1Underrange

28 = Ch1Overrange

27 = Ch2Underrange

26 = Ch2Overrange

25 = Ch3Underrange

24 = Ch3Overrange

23 = Ch4Underrange

22 = Ch4Overrange

21 = Ch5Underrange

20 = Ch5Overrange

19 = Ch6Underrange

18 = Ch6Overrange

17 = Ch7Underrange

16 = Ch7Overrange

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-IF8 or 1756-IF8K module in integer mode.

<!-- image -->

## 1756-IF8, 1756-IF8K Module Fault Word Bits – Integer Mode

In integer mode, Module Fault word bits (bits 15…9) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

1756-IF8, 1756-IF8K Channel Fault Word Bits – Integer Mode

In integer mode, Channel Fault word bits operate exactly as described in floating point mode.

This table lists the conditions that set all Channel Fault word bits in integer mode.

| Condition                                                                       | Channel Fault Word Bits                                                                                                                              |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                                   | • ‘00FF’ for single-ended wiring applications • ‘000F’ for differential wiring applications • ‘0003’ for high-speed differential wiring applications |
| A communications fault has occurred between the module and its owner-controller | ‘FFFF’ for all bits, regardless of the application                                                                                                   |

Your logic can monitor the Channel Fault word bit for a particular input to determine the state of that point.

1756-IF8, 1756-IF8K Channel Status Word Bits – Integer Mode

The Channel Status word has the following differences when the 1756-IF16 or 1756-IF16K module is used in integer mode:

- The module only reports Underrange and Overrange conditions.
- Alarming and Calibration Fault activities aren't available, although the Calibration Fault bit in the Module Fault word activates if a channel isn't properly calibrated.
- There's one, 32-bit Channel Status word for all eight channels.

This table lists the conditions that set each of the word bits.

| Tag (Status Word) Bit   |                                                                                                                                        | Event That Sets This Tag                                                                                                                                                                                                                                                       |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxUnderrange           | Odd-numbered bits from 31…1 (bit 31 represents channel 17). For a full listing of the channels these bits represent, see on page 59 .  | The underrange bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word.   |
| ChxOverrange            | Even-numbered bits from 30…16 (bit 30 represents channel 0). For a full listing of the channels these bits represent, see on page 59 . | The overrange bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 35. This bit also sets the appropriate bit in the Channel Fault word. |

## Choose a Data Format

## Non-isolated Output Module Features

<!-- image -->

## Non-isolated Analog Output Modules (1756-OF4 and 1756-OF8)

This chapter describes features specific to ControlLogix® non-isolated analog output modules. You can mix current and voltage outputs on 1756-OF4, 1756-OF4K, 1756-OF8, or 1756-OF8K modules. Analog output modules also support the features that are described in Chapter 3 .

Data format defines the format of channel data that is sent from the controller to the module, defines the format of the 'data echo' that the module produces, and determines the features that are available to your application. You choose a data format when configuring custom Module Definition parameters.

You can choose one of these data formats:

- Integer mode
- Floating point

## Features Available in Each Data Format

| Data Format Features Available                                                                                                        | Features Not Available                                  |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Integer mode Ramp to program value Ramp to fault value Hold for initialization Hold Last State or User Value in fault or program mode | Clamping Ramp in Run mode Rate and Limit alarms Scaling |
| Floating point mode All features                                                                                                      | N/A                                                     |

For details on input and output data formats, see page 78 .

## Ramping/Rate Limiting

Ramping limits the speed that an analog output signal can change. This helps prevent fast transitions in the output from damaging the devices that an output module controls. Ramping is also known as rate limiting.

## Types of Ramping

| Ramping Type Description   |                                                                                                                                                                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run mode ramping           | This type of ramping occurs when the module is in Run mode and begins operation at the configured maximum ramp rate when the module receives a new output level. IMPORTANT: Run mode ramping is only available in floating point mode. |
| Ramp to Program Mode       | This type of ramping occurs when the present output value changes to the Program value after a Program command is received from the controller.                                                                                        |
| Ramp to Fault Mode         | This type of ramping occurs when the present output value changes to the Fault value after a communication fault occurs.                                                                                                               |

The maximum rate of change in outputs is expressed in engineering units per second and called the maximum ramp rate.

## IMPORTANT

The ramp rate is rounded down to the nearest available value for:

- Series B 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules (firmware revision 2.012 or earlier)
- Series C 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules (firmware revision 3.011)

See page 86 for how to enable Run mode ramping and set the maximum ramp rate.

## Hold for Initialization

Hold for Initialization causes outputs to hold their present state until the value that is commanded by the controller matches the value at the output screw terminal within 0.1% of full scale, providing a bumpless transfer.

If Hold for Initialization is selected, outputs hold if there's an occurrence of any of these three conditions.

- Initial connection is established after power-up.
- A new connection is established after a communications fault occurs.
- There's a transition to Run mode from Program state.

The InHold bit for a channel indicates that the channel is holding.

To see how to enable the Hold for Initialization bit, see page 84 .

## Open Wire Detection

This feature detects when current flow isn't present at any channel. The 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules must be configured for 0…20 mA operation to use this feature. At least 0.1 mA of current must be flowing from the output for detection to occur.

When an open wire condition occurs at any channel, a status bit is set for that channel.

For more information on the use of status bits, see page 69 .

## Clamping/Limiting

Clamping limits the output from the analog module to remain within a range configured by the controller, even when the controller commands an output outside that range. This safety feature sets a high clamp and a low clamp.

Once clamps are determined for a module, any data that is received from the controller that exceeds those clamps sets an appropriate limit alarm and transitions the output to that limit but not beyond the requested value.

For example, if the high clamp that is configured for a module is 8V and the low clamp that is configured is -8V, and the controller sends a value of 9V to the module, the module will only apply 8V to its screw terminals.

## IMPORTANT

Clamping is only available in floating point mode.

Clamp values are in engineering scaling units and aren't automatically updated when the engineering high and low scaling units are changed. Failure to update the clamp values generates a small output signal that could be misinterpreted as a hardware problem.

To see how to set the clamping limits, see page 88 .

## Clamp/Limit Alarms

This function works directly with clamping. When a module receives a data value from the controller that exceeds clamping limits, it applies signal values to the clamping limit but also sends a status bit to the controller as notification that the value sent exceeds the clamping limits.

Using the previous example, if a module has clamping limits of 8V and -8V but then receives data to apply 9V, only 8V is applied to the screw terminals and the module sends a status bit back to the controller informing it that the 9V value exceeds the module's clamping limits.

Clamping alarms can be disabled or latched on a per-channel basis.

IMPORTANT Limit alarms are available only in floating point mode.

To see how to enable all alarms, see page 87 .

## Data Echo

Data Echo automatically multicasts channel data values that match the analog value that was sent to the module's screw terminals.

Fault and status data is also sent. This data is sent in the format (floating point or integer) selected at the requested packet interval (RPI).

## User Count Conversion to Output Signal

User counts can be computed in Integer mode for the 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules.

The straight-line formulas that can be used to calculate or program a Compute (CPT) instruction are shown in this table.

| Available Range   | User Count Formula                                     |
|-------------------|--------------------------------------------------------|
| O…20 mA           | y = 3077.9744124443446x-32768 where y = counts; x = mA |
| +/-10V            | y = 3140.5746817972704x-0.5 where y = counts; x = V    |

For example, if you have 6 mA in the 0…20 mV range, the user counts = -14300. Counts = 6281 for 2V in the +/-10V range.

For a table with related values, see Knowledgebase Technote, ControlLogix 1756-OF4 and 1756OF8 User Count Conversion to Output Signal .

## Use Module Block and Output Circuit Diagrams

Field Side

This section shows the 1756-OF4 and 1756-OF4K series A, B, and C module block diagrams.

## 1756-OF4/A, 1756-OF4K/A Module Block Diagram

<!-- image -->

Backplane Side

## 1756-OF4 and 1756-OF4K Series B and C Module Block Diagram

<!-- image -->

This section shows the 1756-OF8 and 1756-OF8K series A, B, and C module block diagrams.

## 1756-OF8/A, 1756-OF8K/A Module Block Diagram

<!-- image -->

1756-OF4 and 1756-OF4K Series B and C Module Block Diagram

<!-- image -->

## Field-side Circuit Diagrams

This section shows field-side circuitry for the 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K series A, B, and C modules.

## 1756-OF4/A, 1756-OF4K/A, 1756-OF8/A, and 1756-OF8K/A Output Circuit

<!-- image -->

## 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K Series B and C Module Output Circuit

<!-- image -->

## Wire the 1756-OF4 Module

These illustrations show wiring examples for a 1756-OF4 or 1756-OF4K module.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-OF4, 1756-OF4K Current Wiring Example

<!-- image -->

## Keep in mind the following:

- Place additional loop devices (that is, strip chart recorders, and so forth) at the A location noted in the wiring example.
- Do not connect more than two wires to any single terminal.
- All terminals marked RTN are connected internally.

## 1756-OF4, 1756-OF4K Voltage Wiring Example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- All terminals marked RTN are connected internally.

## Wire the 1756-OF8 Module

These illustrations show wiring examples for a 1756-OF8 or 1756-OF8K module.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-OF8, 1756-OF8K Current Wiring Example

<!-- image -->

## Keep in mind the following:

- Place additional loop devices (that is, strip chart recorders, and so forth) at the A location noted in the wiring example.
- Do not connect more than two wires to any single terminal.
- All terminals marked RTN are connected internally.

## 1756-OF8, 1756-OF8K Voltage wiring example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- All terminals marked RTN are connected internally.

## 1756-OF4 and 1756-OF8 Module Fault and Status Reporting

The 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a way as to let you choose the level of granularity that is desired for examining fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                             |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                             |
| Channel Fault Word   | This word provides underrange, overrange, and communications fault reporting. Its tag name is ChannelFaults.                            |
| Channel Status Words | This word provides individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults. |

## IMPORTANT

Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.

## Fault Reporting in Floating Point Mode

This illustration provides an overview of the fault reporting process for the 1756-OF4, 1756OF4K, 1756-OF8, or 1756-OF8K module in floating point mode.

Module Fault Word (described on page 70)

15 = AnalogGroupFault

12 = Calibrating

11 = Cal Fault

14 and 13 aren't used by the 1756-

OF4, 1756-OF4K, 1756-OF8, or

1756-OF8K module

## Channel Fault Word (described on page 70)

- 7 = Ch7Fault
- 6 = Ch6Fault
- 5 = Ch5Fault
- 4 = Ch4Fault
- 3 = Ch3Fault
- 2 = Ch2Fault
- 1 = Ch1Fault
- 0 = Ch0Fault

Regardless of module density, all start at bit 0

Channel Status Words (one for each channel, described on page 71)

- 7 = ChxOpenWire
- 5 = ChxNotANumber
- 4 = ChxCalFault
- 3 = ChxInHold
- 2 = ChxRampAlarm
- 1 = ChxLLimitAlarm
- 0 = ChxHLimitAlarm

<!-- image -->

## IMPORTANT

The 1756-OF4 and 1756-OF4K modules use four Channel Status words and four Channel Fault Word Bits.

The 1756-OF8 and 1756-OF8K modules use eight Channel Status words and eight Channel Fault Word Bits, as seen in this graphic.

Number six isn't used by 1756-OF4, 1756-OF4K, 1756-OF8, or 1756-OF8K

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Module Fault Word Bits - Floating Point Mode

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module.

This table lists tags that you can further examine in ladder logic to isolate the fault.

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Channel Fault Word Bits - Floating Point Mode

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

During normal module operation, Channel Fault word bits are set if any of the respective channels has a High or Low Limit Alarm or an Open Wire condition (0…20 mA configuration only). When using the Channel Fault Word, the 1756-OF4 or 1756-OF4K module uses bits 0…3, and the 1756-OF8 or 1756-OF8K module uses bits 0…7. Checking this word for a nonzero condition is a quick way to check for these conditions on a channel.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

| Condition                                                                   | Display                                                                                                         |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                               | ‘000F’ for all bits on the 1756-OF4 or 1756-OF4K module ‘00FF’ for all bits on the 1756-OF8 or 1756-OF8K module |
| A communications fault occurred between the module and its owner-controller | ‘FFFF’ for all bits on either module                                                                            |

Set your logic to monitor the Channel Fault bit for a particular output if you either:

- enable output clamping
- are checking for an open wire condition (0…20 mA configuration only).

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Channel Status Word Bits – Floating Point Mode

Any of the Channel Status words (four words for 1756-OF4 or 1756-OF4K modules and eight words for 1756-OF8 or 1756-OF8K modules), one for each channel, display a nonzero condition if that particular channel has faulted for the conditions that are listed in the following table. Some of these bits set bits in other Fault words.

When the High or Low Limit Alarm bits (bits 1 and 0) in any of the words are set, the appropriate bit is set in the Channel Fault word.

When the Calibration Fault bit (bit 4) is set in any of the words, the Calibration Fault bit (bit 11) is set in the Module Fault word.

This table lists the conditions that set each of the word bits.

|                      | Tag (Status Word) Bit Event That Sets This Tag                                                                                                                                                                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxOpenWire Bit 7    | This bit is set only if the configured Output Range is 0…20 mA, and the circuit becomes open due to a wire falling off or being cut when the output being driven is above 0.1 mA. The bit remains set until the correct wiring is restored.                                   |
| ChxNotaNumber Bit 5  | This bit is set when the output value that is received from the controller is NotANumber (the IEEE NAN value). The output channel holds its last state.                                                                                                                       |
| ChxCalFault Bit 4    | This bit is set when an error occurred when calibrating. This bit also sets the appropriate bit in the Channel Fault word.                                                                                                                                                    |
| ChxInHold Bit 3      | This bit is set when the output channel is currently holding. The bit resets when the requested Run mode output value is within 0.1% of the full-scale current echo value.                                                                                                    |
| ChxRampAlarm Bit 2   | This bit is set when the output channel’s requested rate of change would exceed the configured maximum ramp rate requested parameter. It remains set until the output reaches its target value and ramping stops. If the bit is latched, it remains set until it’s unlatched. |
| ChxLLimitAlarm Bit 1 | This bit is set when the requested output value is beneath the configured low limit value. It remains set until the requested output is above the low limit. If the bit is latched, it remains set until it’s unlatched.                                                      |
| ChxHLimitAlarm Bit 0 | This bit is set when the requested output value is above the configured high limit value. It remains set until the requested output is below the high limit. If the bit is latched, it remains set until it’s unlatched.                                                      |

IMPORTANT

The 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules do not use bit 6.

## Module Fault Word (described on page 72)

15 = AnalogGroupFault 12 = Calibrating 11 = Cal Fault 14 and 13 aren't used by the 1756-OF4, 1756-OF4K, 1756-OF8, or 1756-OF8K modules

## Channel Fault Word (described on page 73)

- 7 = Ch7Fault

- 6 = Ch6fault

- 5 = Ch5Fault

- 4 = Ch4Fault

- 3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

- 0 = Ch0Fault

- 4...7 aren’t used by the 1756-OF4 or 1756-OF4K modules

## Channel Status Word (described on page 73)

- 15 = Ch0OpenWire
- 14 = Ch0InHold

13 = Ch1OpenWire

12 = Ch1InHold

11 = Ch2OpenWire

10 = Ch2InHold

- 9 = Ch3OpenWire
- 8 = Ch3InHold
- 7 = Ch4OpenWire
- 6 = Ch4InHold
- 5 = Ch5OpenWire
- 4 = Ch5InHold
- 3 = Ch6OpenWire
- 2 = Ch6InHold
- 1 = Ch7OpenWire
- 0 = Ch7InHold

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-OF4, 1756OF4K, 1756-OF8, or 1756-OF8K module in integer mode.

<!-- image -->

Open Wire conditions (odd-numbered bits) set the appropriate bits in the Channel fault Word.

## IMPORTANT

Output in Hold conditions (even-numbered bits) must be monitored here.

Channel Status word bits 0…7 not used on 1756-OF4 or 1756-OF4K modules.

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Module Fault Word Bits – Integer Mode

In integer mode, Module Fault word bits (bits 15…11) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Channel Fault Word Bits – Integer Mode

In integer mode, Channel Fault word bits (bits 7…0) operate exactly as described in floating point mode for calibration and communications faults. During normal operation, these bits are only set for an open wire condition.

This table lists the conditions that set all Channel Fault word bits in integer mode.

| Condition                                                                   | Displays                                                                                                        |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| A channel is being calibrated                                               | ‘000F’ for all bits on the 1756-OF4 or 1756-OF4K module ‘00FF’ for all bits on the 1756-OF8 or 1756-OF8K module |
| A communications fault occurred between the module and its owner-controller | ‘FFFF’ for all bits on either module                                                                            |

Set your logic to monitor the Channel Fault bit for a particular output, if you either:

- enable output clamping.
- are checking for an open wire condition (0…20 mA configuration only).

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Channel Status Word Bits – Integer Mode

The Channel Status word has these differences when used in integer mode.

- The module only reports the Output in Hold and Open Wire conditions.
- Calibration Fault reporting isn't available in this word, although the Calibration Fault bit in the Module Fault word still activates when that condition exists on any channel.
- There's only one Channel Status word for all four channels on 1756-OF4 or 1756-OF4K module and all eight channels on 1756-OF8 or 1756-OF8K module.

This table lists the conditions that set each of the word bits.

| Tag (Status word) Bit   |                                                                                                                                                     | Event that sets this tag                                                                                                                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxOpenWire             | Odd-numbered bits from bit 15 …bit 1 (that is, bit 15 represents channel 0). For a full listing of the channels these bits represent, see page 72 . | The Open Wire bit is set only if the configured Output Range is 0…20 mA, and the circuit becomes open due to a wire falling off or being cut when the output being driven is above 0.1 mA. The bit remains set until the correct wiring is restored. |
| ChxInHold               | Even-numbered bits from bit 14…bit 0 (that is, bit 14 represents channel 0). For a full listing of the channels these bits represent, see page 72 . | The Output In Hold bit is set when the output channel is currently holding. The bit resets when the requested Run mode output value is within 0.1% of the full-scale current echo value.                                                             |

## Notes:

<!-- image -->

## Configure ControlLogix Analog I/O Modules

## IMPORTANT

This chapter describes how to configure your module with the Studio 5000 Logix Designer® application, version 21 and later.

You can use the ControlLogix® analog I/O modules in RSLogix 5000® software projects as well.

You must install AOPs to use the modules in any Logix Designer application or RSLogix 5000 software project.

You must create and properly configure your analog I/O module upon installation. The programming software uses the selected configurations, such as RTS and RPI, to get your I/O module to communicate with the owner-controller.

You can choose settings using the categories found along the left side of the Module Properties dialog box. This chapter provides basic overview instructions for creating default and custom configurations. See the Studio 5000 Logix Designer application help for additional information.

## IMPORTANT

The following sections describe how to use the Logix Designer application to configure I/O modules in a local chassis. If you plan to use an I/O module in a remote chassis, and your controller does not have built-in Ethernet capabilities, you must first add a ControlNet® or EtherNet/IP™ communication module to the I/O configuration tree. See page 92 for details.

This chapter describes how to configure ControlLogix 1756-IF16, 1756-IF16K, 1756-IF8, 1756IF8K, 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K analog modules.

See Appendix C for additional information regarding the configuration of 1756-IF6CIS, 1756IF6I, 1756-IR6I, 1756-IT6I, 1756-IT6I2, 1756-OF6CI, and 1756-OF6VI modules.

## Create a New Module

After you create a Logix Designer application project, complete the following steps to create a module in the project.

1. Under I/O Configuration, right-click 1756 Backplane and select New Module.
2. Select the module and select Create.

<!-- image -->

<!-- image -->

The New Module dialog box appears.

3. On the General category, name the module.

Make sure that the slot number in the configuration matches the physical slot number of the chassis housing the module.

<!-- image -->

4. To accept the default configuration, click OK.

## Module Definition

To create a custom configuration and specify a communication format for your module, select Change on the General category.

<!-- image -->

The Module Definition dialog box appears.

<!-- image -->

The following parameters are available on the Module Definition dialog box:

- Series - Module hardware series
- Revision - Module firmware revision
- Electronic Keying - Type of comparison that is done between the module that is defined in the project and the installed module. If keying fails, a fault occurs. For more information, see page 25 .
- Connection - Available input and output data configuration parameters. For more information, see page 78 .
- Input/Output Data - Type of data that is transferred between the module and the controller. For more information, see page 79 and page 80 .
- Data Format - Which tags are generated when configuration is complete. For more information, see page 34 or page 61 .

## IMPORTANTIMPORTANT

Make sure you select the correct communication format for your application because you cannot change the selection after the program is downloaded with the controller. You have to reconfigure the module to change the communication format.

## Connection Type

This table describes connection types used with analog I/O modules.

| Connection Type Definition   |                                                                                                                                                                                                                                 |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data                         | All available configuration, input, and output data. This connection type creates all appropriate controller tags for the module type being used.                                                                               |
| Listen Only Data             | Controller and module establish communication without the controller sending any configuration or output data to the module. A full input data connection is established but is dependent on the owner-controller’s connection. |

## IMPORTANT

IMPORTANT: When you use the Listen Only Data connection type, only the following categories appear in the New Module or Module Properties dialog box:

- General
- Connection
- Module Info

For more information, see page 22 .

## Input Module Communication Formats

This table describes the communication formats that can be used with analog input modules.

| If you want the input module to return this data                                                                                                                                                        | Select this format                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Floating point input data                                                                                                                                                                               | Float data                                                                |
| Integer input data                                                                                                                                                                                      | Integer data                                                              |
| Floating point input data with the value of the coordinated system time (from its local chassis) when the input data is sampled                                                                         | CST timestamped float data                                                |
| Integer input data with the value of the coordinated system time (from its local chassis) when the input data is sampled                                                                                | CST timestamped integer data                                              |
| Floating point input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in differential mode | CST timestamped float data - differential mode                            |
| Floating point input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in high speed mode                                                                                                                                                                                                         | CST timestamped float data - high-speed mode                              |
| Floating point input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in single ended mode                                                                                                                                                                                                         | CST timestamped float data - single-ended mode - no alarm (1)             |
| Integer input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in differential mode        | CST timestamped integer data - differential mode                          |
| Integer input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in high-speed mode          | CST timestamped integer data - high-speed mode                            |
| Integer input data with the value of the coordinated system time (from its local chassis) when the input data is sampled when the 1756-IF16 or 1756-IF8 module is operating in single-ended mode        | CST timestamped integer data - single-ended mode                          |
| Floating point input data when the 1756-IF16 or 1756-IF8 module is operating in differential mode only                                                                                                  | Float data - differential mode                                            |
| Returns floating point input data when the 1756-IF16 or 1756-IF8 module is operating in high speed mode                                                                                                                                                                                                         | Float data - high-speed mode                                              |
| Floating point input data when the 1756-IF16 or 1756-IF8 module is operating in single-ended mode                                                                                                       | Float data - single-ended mode - no alarm (1)                             |
| Integer input data when the 1756-IF16 or 1756-IF8 module is operating in differential mode Integer data - differential mode                                                                             |                                                                           |
| Integer input data when the 1756-IF16 or 1756-IF8 module is operating in high-speed mode Integer data - high-speed mode                                                                                 |                                                                           |
| Integer input data when the 1756-IF16 or 1756-IF8 module is operating in single-ended mode Integer data - single-ended mode                                                                             |                                                                           |
|                                                                                                                                                                                                         | Listen only CST timestamped float data                                    |
|                                                                                                                                                                                                         | Listen only CST timestamped integer data                                  |
|                                                                                                                                                                                                         | Listen only float data                                                    |
|                                                                                                                                                                                                         | Listen only integer data                                                  |
|                                                                                                                                                                                                         | Listen only CST timestamped float data - differential mode                |
|                                                                                                                                                                                                         | Listen only CST timestamped float data - high-speed mode                  |
| Specific input data that is used by a controller that does not own the input module                                                                                                                     | Listen only CST timestamped float data - single-ended mode - no alarm (1) |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only CST timestamped integer data - differential mode              |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only CST timestamped integer data - high-speed mode                |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only CST timestamped integer data - single-ended mode              |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only Float data - differential mode                                |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only Float data - high-speed mode                                  |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only Float data - single-ended mode - no alarm (1)                 |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only Integer data - differential mode                              |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        | Listen only Integer data - high-speed mode                                |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog input module and a listen-only controller        |                                                                           |

(1) In this mode, the 1756-IF16 module functions without alarms and the 1756-IF8 module functions with alarms.

## Output Module Communication Formats

This table describes the communication formats that can be used with analog output modules.

| If you want the output module to return this data                                                                                                                                                 | Select this format                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Floating point output data                                                                                                                                                                        | Float data                                                                      |
| Integer output data                                                                                                                                                                               | Integer data                                                                    |
| Floating point output data and receives data echo values with a CST time stamp value                                                                                                              | CST timestamped float data                                                      |
| Integer output data and receives data echo values with a CST time stamp value                                                                                                                     | CST timestamped integer data                                                    |
| Specific input data that is used by a controller that does not own the output module                                                                                                              | Listen only float data Listen only integer data                                 |
| These choices have the same definition as the preceding, similarly named options except that they represent listen-only connections between the analog output module and a listen-only controller | Listen only CST timestamped float data Listen only CST timestamped integer data |

## Modify the Configuration

To modify the configuration of a module, in the Controller Organizer, right-click the module and select Properties. Use the categories along the left side of the Module Properties dialog box to edit module configuration. Some categories show the same fields regardless of the module type that you are configuring, and other categories show fields specific to the module type.

## General Category

Use the General category to configure or view the module name and description, as well as the physical properties of the module.

The fields on this category can be used to:

- View the type and vendor of the module.
- Enter or change the name of the module.
- Enter a description for the module.
- View and change the revision, electronic keying, and connection for the module.
- Enter the slot number for the module.

<!-- image -->

## Connection Category

Use the Connection category to define controller-to-module behavior. You can complete the following tasks from the Connection category:

- Set the RPI rate. For more information about the RPI, see page 19 .
- Set whether a module connected via an EtherNet/IP network multicasts data to all devices on the network or unicasts only to a specific owner-controller.
- Inhibit the module. For more information on inhibiting the module, see page 28 .
- When available, select whether to enable Automatic Diagnostics for the module.
- Configure whether a connection failure while the controller is in Run mode causes a major or minor fault.
- The Module Fault area of the Connection category is useful during module troubleshooting. For more information on the Module Fault area, see page 125 .

<!-- image -->

## Module Info Category

The Module Info category displays module and status information when the module is online.

Use the Module Info category to:

- Determine the identity of the module.
- View the module's current operational state.
- View whether the module was configured by the owner controller.
- View whether an owner controller is currently connected to the module.
- Retrieve the latest information from the module.
- Reset a module to its power-up state.
- View the protection mode of the module.
- View Coordinated System Time (CST) status.

<!-- image -->

The data that is displayed on the Module Info category comes directly from the module.

<!-- image -->

## Channels Category

The Channels category provides the means to configure all module channels.

<!-- image -->

The number of Chxx categories available beneath the Channels category of a module varies depending on the module type and the Input/Output Data configuration settings that are selected on the Module Definition dialog box. For example, a 1756-IF16K module can have 16 channels in Single-Ended, 8 channels in Differential, or 4 channels in High Speed Data Format.

1756-IF8, 1756-IF8K, 1756-IF16, 1756-IF16K Modules

Use the Channels category to:

- Specify the input range for each channel (integer mode only).
- Specify a Real Time Sample (RTS) period for all module channels.

<!-- image -->

If the RTS value is less than or equal to the RPI, each multicast of data from the module has updated channel information. If the RTS value is greater than the RPI, the module multicasts at both the RTS value and the RPI rate. The module resets the RPI timer any time an RTS is performed.

- Select a module filter frequency for all module channels.

<!-- image -->

The individual Chxx categories that are located beneath the Channels category, when using Float Data Format, provide the ability to further configure specific channels.

<!-- image -->

## Use each individual Chxx category to:

- Select input type and range to determine the minimum and maximum signals that are detected by the module. See page 29 in Chapter 3 for a chart showing range and resolution per module.
- Enter Scaling values and Engineering Units while in floating point data format. See page 30 in Chapter 3 for details.
- Enter a sensor offset value.
- Select a digital filter time to specify the time constant for a digital first order lag filter on the input. A value of 0 disables the filter. See page 35 in Chapter 4 for an amplitude chart example.

For more information about configurable input module channel parameters, see Chapter 4 .

1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K Modules

Use the Channels category to specify module output behavior when communications fail in Program Mode.

IMPORTANT Outputs always go to Fault Mode if communications fail in Run Mode.

<!-- image -->

The Chxx categories provide the ability to further configure specific channels.

<!-- image -->

Use each individual Chxx category to:

- Specify the output type and operating range to determine the minimum and maximum signals that are detected by the module. See page 29 in Chapter 3 for a chart showing range and resolution per module.
- Specify the output state in Program and Fault Mode. You can also elect to have the module ramp to a User Defined Value in either mode. See page 61 in Chapter 5 for details.
- Enter Scaling values and Engineering Units while in floating point data format. See page 30 in Chapter 3 for details.
- Enter a sensor offset value to compensate for any sensor offset errors.
- Elect to have outputs hold their present state until the output values match the controller values. See page 62 in Chapter 5 for details.

For more information about configurable output module channel parameters, see Chapter 5 .

## Alarms Category

The 1756-IF8, 1756-IF8K, 1756-IF16, 1756-IF16K modules support alarms. The fields on the Alarms category are used to configure process and rate alarms on non-isolated analog input modules on a per-channel basis. This category is available only for input modules.

<!-- image -->

Module configuration may impact the support of alarms. For example, a 1756-IF16K module that is configured with Single-Ended Data Format as the Input/Output Data type would not display Alarms Categories beneath each Chxx Category.

Use the Alarms category for a specific channel to:

- Set high and low limits for process alarms (1). See page 36 in Chapter 4 for more information.
- Set a trigger value for a rate alarm (1). See page 37 in Chapter 4 for more information.
- Disable alarms.

## IMPORTANT

When you disable all alarms, you disable process, rate, and channel diagnostic alarms (for example, underrange and overrange). We recommend that you disable only unused channels so extraneous alarm bits are not set.

- Latch and unlatch alarms. The Unlatch buttons are enabled only when the module is online.
- Enter a deadband value that works with the process alarms. The deadband guages the input data to set or remove an alarm for a process alarm. See page 36 in Chapter 4 for an alarm deadband chart.

For information about configurable parameters, see Chapter 4 .

<!-- image -->

## Limits Category

The Limits category is available only for 1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K modules. The Limits category enables you to configure clamping and ramp limitations that can prevent damage to equipment.

Use the Limits category to:

- Enter clamp limits. See page 62 for more information.

## IMPORTANT

Clamping is only available in floating point mode. Clamp values are in engineering scaling units and are not automatically updated when the engineering high and low scaling units are changed. Failure to update the clamp values can generate a very small output signal that could be misinterpreted as a hardware problem.

- Enable ramping during Run mode
- Enter a ramp rate. See page 61 for more information.
- Disable or latch clamp alarms

## IMPORTANT

When you disable all alarms, you disable clamp and rate alarms. We recommend that you disable only unused channels so extraneous alarm bits are not set.

- Maintain the high and low limit alarms even after the condition ceases. See page 63 for more information.
- Maintain the rate alarm even after the condition ceases.

<!-- image -->

## Download Configuration Data to the Module

## Calibration Category

Calibration corrects hardware inaccuracies present on a particular channel. The calibration procedure compares a known standard, either input signal or recorded output, with the channel's performance and then calculates a linear correction factor between the measured and the ideal.

Use the Calibration category on the Module Properties dialog box to start the calibration process and view the results.

<!-- image -->

For information about how to calibrate each module type, see Chapter 8 .

After you've changed the configuration data for a module, the changes do not take effect until you download the new project containing that information to the controller. The entire project downloads to the controller, overwriting any existing projects.

Follow these steps to download the new project:

1. At the top, left corner of the Studio 5000 Logix Designer application, select the status icon and select Download from the menu.

<!-- image -->

The Download dialog box appears.

2. Select Download.

## Reconfigure Parameters in Run Mode

Your module can operate in either Remote Run or Run mode. You can change any configurable features that the programming software enables in Remote Run mode.

This example shows a Chxx category for a 1756-IF8 module in Run mode.

<!-- image -->

1. Make the necessary configuration changes.
2. Do one of the following:
- Select Apply to store a change but stay on the dialog box to select another category.
- Select OK if you're finished making changes.

When you try to download new configuration data to the module, a warning appears.

<!-- image -->

## IMPORTANT

If you change the configuration for a module, you must consider whether the module has multiple owner-controllers. If so, apply the same configuration data to all controllers.

For more information about making configuration changes in a module with multiple ownercontrollers, see page 22 .

## Reconfigure Parameters in Program Mode

To change the module from either Remote Run or Run mode to Program mode before reconfiguring parameters, complete the following steps.

1. At the top, left corner of the Studio 5000 Logix Designer application, select the status icon and select Program Mode from the menu.

<!-- image -->

A warning appears, asking if you want to change the controller mode to Remote Program mode.

<!-- image -->

2. Select Yes.
3. Make any necessary changes. For example, to avoid interrupting control and a temporary loss of connection, it's recommended that adjustments RPI be made when the controller is in Program mode.
4. Do one of the following:
- Select Apply to store a change but stay on the dialog box to select another category.
- Select OK if you're finished making changes.

Before the RPI rate is updated online, the programming software verifies your desired change.

<!-- image -->

5. Select Yes to verify any software changes.

The RPI, in this example, is changed and the new configuration data is transferred to the controller.

We recommend that you change the module back to Run mode after changes are made in Program mode.

## Configure I/O Modules in a Remote Chassis

If your controller does not have built-in Ethernet capabilities, there are separate communication modules available for different networks to configure I/O modules in a remote chassis. ControlNet or EtherNet/IP communication modules must be configured in the local chassis and the remote chassis to handle the network protocol.

Follow these steps to add and configure a communication module for the local chassis. This module handles communication between the controller chassis and the remote chassis.

1. On the Controller Organizer, right-click I/O Configuration and select New Module.

<!-- image -->

The Select Module Type dialog box appears.

2. Check the box next to the Communication filter for a list of just communication modules.
3. Select a communication module for the remote chassis and select Create. The New Module dialog box appears.
4. To accept the default major revision, select OK.
5. Configure the communication module in the local chassis.

Follow these steps to add and configure a communication module for the remote chassis.

1. On the Controller Organizer, right-click the communication module you just added in the local chassis and select New Module.

<!-- image -->

The Select Module Type dialog box appears.

2. Check the box next to the Communication filter for a list of just communication modules.
3. Select a communication module for the local chassis and select Create.

The New Module dialog box appears.

4. To accept the default major revision, select OK.
5. Configure the communication module in the remote chassis.

Now you can configure the remote I/O modules by adding them to the remote communication module. Follow the same procedures as you do for configuring local I/O modules, starting on page 76 .

For more information on the ControlLogix ControlNet module, see ControlNet Modules in Logix 5000 Control Systems, publication CNET-UM001 .

For more information on the ControlLogix EtherNet/IP module, see EtherNet/IP Modules in Logix 5000 Control Systems User Manual, publication ENET-UM001 .

## View the Module Tags

When you create a module, the Logix Designer application creates a set of tags that you can view in the Controller Tags dialog box. Each configured feature on your module has a distinct tag that is available for use in the controller's programming logic.

Complete these steps to access the tags in a module.

1. In the Controller Organizer, right-click Controller Tags and choose Monitor Tags.

<!-- image -->

The Controller Tags dialog box appears with data.

2. Expand a channel to view module tags as shown in the following graphic.

For more information on module tags, see Appendix A .

<!-- image -->

## Notes:

## Perform Runtime Services

<!-- image -->

## Use Ladder Logic To Define Module Operation

After you have created a project in the Studio 5000 Logix Designer® application, you can create programming for the control system. Ladder logic is one of the languages that are used to define module operation based on the inputs and outputs from the controllers.

Chapter 6 explains how to use the programming software to perform runtime services or set configuration parameters on your ControlLogix® analog I/O module. This chapter provides instructions and examples of how to unlatch alarms or change certain parameters using ladder logic instead.

In ladder logic, you can use message instructions to send an explicit service to the module, causing specific behavior to occur. For example, unlatching a high alarm can be performed by a message instruction.

Message instructions maintain the following characteristics:

- They use unscheduled portions of system communication bandwidth.
- One service is performed per instruction.
- Performing module services does not impede module functionality, such as sampling inputs or applying new outputs.

Services that are sent through message instructions are not as time critical as the module behavior defined during configuration and maintained by a real-time connection. Therefore, the module processes messaging services only after the needs of the I/O connection have been met.

## Add a Message Instruction to a Routine

Follow these steps to add a message instruction in the Main Routine section of the Logix Designer application.

1. Open an existing I/O project.
2. Right-click a Program Routine in the Controller Organizer and select Open.

<!-- image -->

The MainProgram - Main Routine dialog box appears. If the ladder routine is empty, the application automatically adds the first rung, ready for instruction.

3. Select the MSG (message) instruction on the Language Element toolbar and drag it to the rung.

<!-- image -->

The instruction is added to the rung in the ladder editor routine view.

4. Inside the Message Control field of the MSG instruction, right-click the question mark to access a pull-down menu.
5. Select New Tag.

<!-- image -->

The New Tag dialog box appears.

<!-- image -->

6. Configure the options in the New Tag dialog box.

## IMPORTANT

We suggest you name the tag to indicate the module slot number, target channel, and what module service the message instruction is sending.

7. Select Create.

## Configure the Message Instruction

After creating a tag for the message instruction, you must define certain parameters on the Configuration and Communication tabs of the Message Configuration dialog box.

Access the Message Configuration dialog box by selecting the box with the ellipses, which are located to the right of the Message Control field.

<!-- image -->

## Configuration Tab

The Configuration tab provides information on what module service to perform and where to perform it.

<!-- image -->

This table describes some of the fields that are found on the Configuration tab. You are required to choose a Service Type and configure the Instance.

|              | Field Description                                                                                                                                                                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service Type | Defines the type of module service to be performed. For example, unlatch alarm. The programming software defaults the Service Code, Instance, Class, and Attribute parameters based on the Service Type that you select. All values are in Hex.                                       |
|              | Class Object that you are sending a message to, such as the device object or a discrete output point.                                                                                                                                                                                 |
| Instance     | Each object can have multiple instances. For example, a discrete output can have 16 points or instances of where a message can be sent. This specifies the instance.                                                                                                                  |
| Attribute    | Further identifies the exact address for the message. An analog input can have multiple alarms so this attribute acknowledges a specific alarm and not the other alarms. If an attribute is not specified (default to 0) the Service applies to all attributes of the Class/Instance. |

## Communication Tab

The Communication tab provides information on the path of the message instruction. For example, the path of a 1756-IF8 module distinguishes exactly which module a message is designated for.

<!-- image -->

1. To see a list of the I/O modules in the system, select Browse.
2. The Message Path Browser dialog box appears.
3. To enter a path, select a module from the list.

<!-- image -->

## IMPORTANT

If an I/O module was not named during initial module configuration, the OK button will be disabled after you select an I/O module from the list. You must edit the module and enter a name before you can choose a path for your message instruction.

In the example above, the 1756-IF8 module was named during initial configuration but the other three modules were not.

4. Select OK to set the path.

## Add Bit Instructions, Rungs, and Branches

Select the tab corresponding to the instruction group from which you want to add an instruction and use the Ladder Instruction toolbar to add additional rungs, branches, or instructions as required to complete your routine.

1. Select the desired instruction and drag it into the ladder editor routine view.
2. Modify the instruction as necessary.
3. Use the Tag Browser to define each corresponding tag.
4. Verify your routine and correct any errors.

Depending upon the Service Type you chose on the Message Instruction Configuration Tab, you can create a sequential routine consisting of multiple rungs or a simultaneous routine consisting of multiple branches on a single rung. The following two examples illustrate either scenario.

Example: Unlatch Alarms in a 1756-IF8 Module Sequentially

In this example, the trigger and alarm state bit instructions that are added to the left of the message instructions on rungs 0…4 sequentially unlatch the following alarms in a 1756-IF8 module in Slot 1 of the chassis:

- Channel 0 High high alarm - Rung 0
- Channel 0 High alarm - Rung 1
- Channel 0 Low low alarm - Rung 2
- Channel 0 Low alarm - Rung 3
- Channel 0 Rate alarm - Rung 4

## IMPORTANT

An I/O module must be configured to latch alarms, see page 87 and page 88, before you can perform unlatch services using ladder logic. If a module that is not configured to latch alarms receives an unlatch service, the message instruction errors.

<!-- image -->

Alternatively, all alarms for channel 0 of this 1756-IF8 module can be simultaneously unlatched with a single message instruction.

Example: Unlatch Alarms in a 1756-IF8 Module Simultaneously

In this example, the Service Type selected on the Message Instruction Configuration tab, is Unlatch All Alarms (I). This selection automatically sets the Attribute parameter to a value of 0, where no attribute is selected, and all attributes are unlatched for that channel.

<!-- image -->

The alarm state bit instructions are added to the left of the message instruction, nested in a set of branch levels, on a single rung.

<!-- image -->

## Reconfigure a Module

It is sometimes advantageous to change the functional operation of a module in the ControlLogix system automatically via ladder logic rather than using the programming software to reconfigure it. This way, changes in the process can dictate when the reconfiguration takes place rather than you performing that function manually.

The following steps are used in this example when reconfiguring a module via ladder logic:

1. Move the new configuration parameters to the Configuration portion of the Tag Structure associated with the module.
2. Use a message instruction to send a Reconfigure Module message type to the same module.

Before the new configuration parameters are sent to the module, you must make sure that their relationship to each other is in a format the module accepts.

## IMPORTANT

Limit analog modules reconfiguration via ladder logic to functions that involve only the changing of values. We do not recommend enabling or disabling features via ladder logic. Use the programming software to enable or disable these features.

This table lists module parameters that can be changed via ladder logic.

## Permissible Analog Input Module Parameters to Change Via Ladder Logic

| Feature                | Restriction                                          |
|------------------------|------------------------------------------------------|
| High engineering value | Must not be equal to low engineering value           |
| Low engineering value  | Must not be equal to high engineering value          |
| High-high alarm value  | Must be greater than or equal to high alarm value    |
| High alarm value       | Must be greater than low alarm value                 |
| Low alarm value        | Must be less than high alarm value                   |
| Low-low alarm value    | Must be less than or equal to low alarm value        |
| Deadband               | Must be less than half of high alarm minus low alarm |

## Permissible Analog Output Module Parameters to Change Via Ladder Logic

| Feature              | Restriction                          |
|----------------------|--------------------------------------|
| High clamp value (1) | Must be greater than low clamp value |
| Low clamp value (1)  | Must be less than high clamp value   |

## Notes:

<!-- image -->

## Calibrate the ControlLogix Analog I/O Modules

The ControlLogix® analog I/O modules are calibrated during the manufacturing process. You can choose to recalibrate your module to increase its accuracy for your specific application.

Before you can calibrate the module, you must add the module to your Studio 5000 Logix Designer® project as described in Chapter 6 .

You can calibrate analog I/O modules on a channel-by-channel basis or with all channels as a group.

If you choose to calibrate your module, we recommend the following:

- Calibrate all channels on your module each time you calibrate. This maintains consistent calibration readings and improves module accuracy.
- Use an extra 1756-TBCH RTB to calibrate your module.

This chapter describes how to calibrate ControlLogix 1756-IF16, 1756-IF16K, 1756-IF8, 1756-IF8K, 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K analog modules.

See Appendix C for additional information regarding the calibration of 1756-IF6CIS, 1756-IF6I, 1756-IR6I, 1756-IT6I, 1756-IT6I2, 1756-OF6CI, and 1756-OF6VI modules.

## Difference Between Calibrating Input and Output Modules

Although the purpose of calibrating analog modules is the same for input and output modules, to improve the module's accuracy and repeatability, the procedures that are involved differ for each:

- When you calibrate non-isolated input modules, you use voltage calibrators to send a signal to the module to calibrate it.
- When you calibrate output modules, you use a digital multimeter (DMM) to measure the signal that the module is sending out.

To maintain your module's accuracy specifications, we recommend you use calibration instruments with specific ranges, as listed in this table.

| Module                                     |              | Channel Input Type Recommended Instrument Range   |
|--------------------------------------------|--------------|---------------------------------------------------|
| 1756-IF16, 1756-IF16K, 1756-IF8, 1756-IF8K | Voltage (V)  | 0…10.25V source +/-150 µV voltage                 |
| 1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K   | Current (mA) | DMM with accuracy better than 0.6 µA              |
| 1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K   | Voltage (V)  | DMM with accuracy better than 0.3 mV              |

## IMPORTANT

Do not calibrate your module with an instrument that is less accurate than recommended. The following events can result:

- Calibration appears to occur normally but the module gives inaccurate data during operation.
- A calibration fault occurs, forcing you to end calibration.
- The I.Ch[x].CalFault tag is set for the channel that you attempted to calibrate.

You can clear the tag by completing a valid calibration or cycling power to the module. In this case, you must recalibrate the module with an instrument as accurate as recommended.

## Calibrating in Program Mode or Without a Connection

Your project must be online with the controller to calibrate ControlLogix analog I/O modules via the software. Once online, select either Program mode as the state of your program or inhibit the connection while in Run mode.

- It is recommend that Series A modules be put into Program mode during calibration.
- Series B 1756-IF16 and 1756-IF8 modules must have an inhibited connection during calibration.
- Series B and C 1756-OF8 and 1756-OF4 modules can be put into Program mode or you can inhibit the connection while in Run mode during calibration.

## IMPORTANT

The module freezes the state of each channel and does not update the controller with new data until after the calibration ends. This could be hazardous if active control were attempted during calibration.

## Calibrate 1756-IF16 and 1756-IF8 Modules

Input calibration is a multi-step process that involves applying low and high signal references to the module at different steps in the process. This section provides information about the specific calibration ranges for the 1756-IF16, 1756-IF16K, 1756-IF8, or 1756-IF8K modules.

These modules are used in applications requiring voltage or current and offer four input ranges:

- -10…10V
- 0…5V
- 0…10V
- 0…20 mA

However, you can only calibrate these modules using a voltage signal.

## IMPORTANT

Regardless of what application range is selected before calibration, all calibration uses the -10…10V range.

Follow these steps to calibrate your module.

1. Connect your voltage calibrator to the module.
2. Go online with your project.
3. Right-click the module that you want to calibrate and select Properties.
4. Go to the Connection category on the Module Properties dialog box.

<!-- image -->

5. Select Inhibit Module.
6. Select Apply.
7. Go to the Calibration category on the Module Properties dialog box.
8. Select Start Calibration to access the Calibration Wizard to step through the process.

<!-- image -->

<!-- image -->

If your module is in Run mode but the connection is not inhibited, a warning message appears and Series B module calibration will error.

You must manually change the module to Run mode and inhibit the connection before selecting OK.

<!-- image -->

The Calibration Wizard dialog box appears.

9. Select the channels to be calibrated and the method to calibrate.
10. Depending upon the type of wiring that is used and whether the source is wired in parallel or must be sequentially attached to each channel, select one of the following options:

Calibrate Channels in Groups applies the low reference to all channels simultaneously and then the high reference.

Calibrate Channels One at a Time walks through the channels, one at a time, applying the low reference and then the high reference to each channel sequentially.

11. Select Next.

<!-- image -->

The Attach Low Reference Voltage Signals dialog box appears. This dialog box indicates which channels are calibrated for a low reference and the range of the calibration.

12. Set the calibrator for the low reference voltage and select Next to apply it to the module.

<!-- image -->

The Group Low Reference Results dialog box appears. This dialog box indicates the status of each channel after calibrating for a low reference.

<!-- image -->

13. If any channel reports an error, return to step 12 and select Retry until the status is OK. If the error persists indefinitely, select Stop to exit calibration. The channel remains calibrated to the accuracy level achieved at factory, or the last field, calibration. If all channels are OK, select Next.

The Attach High Reference Voltage Signals dialog box appears. This dialog box indicates which channels are calibrated for a high reference and the range of the calibration.

<!-- image -->

14. Set the calibrator for the high reference voltage and select Next to apply it to the module.

The Group High Reference Results dialog box appears. This dialog box indicates the status of each channel after calibrating for a high reference.

<!-- image -->

15. If any channel reports an error, return to step 14 and select Retry until the status is OK. If the error persists indefinitely, select Stop to exit calibration. The channel remains calibrated to the accuracy level achieved at factory, or the last field, calibration. If all channels are OK, click Next.

16. When the Calibration Completed dialog box appears, select Finish.

<!-- image -->

## Calibrate 1756-OF4 and 1756-OF8 Modules

You can calibrate the 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K module for use with the following output types:

- Current (mA)
- Voltage (V)

## IMPORTANT

This section shows how to calibrate the 1756-OF4, 1756-OF4K, 1756-OF8, and 1756-OF8K modules for use with only current outputs.

The calibration process is generally the same if you calibrate the module for use with voltage inputs except for the following differences:

- You connect a voltage meter to the module.
- The low reference signal that is measured at the module is in volts.
- The high reference signal that is measured at the module is in volts.

## Current Meter Calibrations

When calibrating an output channel for use with a current output type, the Logix Designer application commands the module to output specific levels of current. You must measure the actual level and record the results to account for any module inaccuracies.

Follow these steps to calibrate your module.

1. Connect your current meter to the module.
2. Go online with your project.
3. Right-click the module that you want to calibrate and select Properties.
4. On the Chxx category for each channel to be calibrated, make sure that the Output Type is set to Current (mA).

<!-- image -->

<!-- image -->

5. Place the controller into Program mode or go to the Connection category on the Module Properties dialog box, select Inhibit Module, and select Apply.
6. Go to the Calibration category on the Module Properties dialog box.
7. Select Start Calibration to access the Calibration Wizard to step through the process.

<!-- image -->

<!-- image -->

If your module is not in Program mode or is in Run mode but the connection is not inhibited, a warning message appears.

<!-- image -->

You must manually change the module to Program mode or Run mode with the connection inhibited before selecting OK.

The Calibration Wizard dialog box appears.

8. Select the channels to be calibrated and the method to calibrate.
9. Depending upon the type of wiring that is used and whether the source is wired in parallel or must be sequentially attached to each channel, select one of the following options:

Calibrate Channels in Groups applies the low reference to all channels simultaneously and then the high reference.

Calibrate Channels One at a Time walks through the channels, one at a time, applying the low reference and then the high reference to each channel sequentially.

10. Select Next.

<!-- image -->

The Output Reference Signals dialog box appears. This dialog box indicates which channels are calibrated for a Low Reference and the range of calibration.

<!-- image -->

## 11. Select Next.

The Measure and Record Values dialog box appears.

<!-- image -->

12. For each channel being calibrated, use your current meter to measure the reference value of each channel individually.
13. In the Recorded Reference (mA) column, enter the recorded value for each channel that was measured and select Next.

The Group Low Reference Results dialog box appears. This dialog box indicates the status of each channel.

<!-- image -->

14. If the status is not OK for any channels, return to step 12 and select Retry until the status is OK.

If the error persists indefinitely, select Stop to exit calibration. The channel remains calibrated to the accuracy level achieved at factory, or the last field, calibration. If all channels are OK, select Next.

The Output Reference Signals dialog box appears again, this time indicating the channels that are calibrated for a High Reference and the calibration range.

15. Select Next.

<!-- image -->

## The Measure and Record Values dialog box appears again.

<!-- image -->

16. For each channel being calibrated, use your current meter to measure the reference value of each channel individually.
17. In the Recorded Reference (mA) column, enter the recorded value for each channel that was measured and select Next.
3. The Group High Reference Results dialog box appears. This dialog box indicates the status of each channel.
18. If the status is not OK for any channels, return to step 17 and select Retry until the status is OK.

<!-- image -->

If the error persists indefinitely, select Stop to exit calibration. The channel remains calibrated to the accuracy level achieved at factory, or the last field, calibration.

If all channels are OK, select Next.

19. When the Calibration Completed dialog box appears, select Finish.

<!-- image -->

## Analog to Digital (A/D) Converter Accuracy

There are two types of calibration that occur on a ControlLogix analog I/O module.

- The user-directed and user-performed calibration process that is described previously in this chapter. This type of calibration occurs only when you determine it is necessary and involves an external calibration instrument.
- An Analog to Digital (A/D) Converter self-calibration process that executes internally on ControlLogix analog I/O modules each time the module cycles power or when a usercalibration cycle is initiated.

The self-calibration compensates for inaccuracies of the onboard reference signal and the A/D converter only. In other words, the self-calibration feature makes sure that the A/D converter itself is accurate regarding its onboard voltage reference that is used for a conversion of the input signal.

Together, both types of calibration maintain the overall accuracy of a module.

## Calibrated Accuracy

## Error Calculated Over Hardware Range

The Calibrated Accuracy specification represents the module's accuracy when its ambient (that is, operating) temperature is the same as the temperature at which the module was calibrated.

Immediately following a calibration, a ControlLogix analog I/O module is most accurate. Because the module was calibrated at its zero and span, the inaccuracy is largely non-linearity between zero and span. Assuming the module is operating at the exact temperature when it was calibrated and uses the same voltage source to check the post-calibration accuracy, a module can be as accurate as 0.01…0.05% of range.

Once the module begins operation, its accuracy lessens as components change over time. However, this change (in components or accuracy) differs from the Gain Drift With Temperature specification described on page 119 .

Other than non-linearity, the Calibrated Accuracy @ 25 °C (77 °F) specification represents a time drift/aging specification between calibrations. A module with a calibration accuracy of 0.01% of range immediately following calibration is estimated to be better than 0.1% of range 
°° gy g 
@ 25 °C (77 °F) for 1 year (that is, the calibration cycle).

The reason for the difference between 0.01% and 0.1% of range is that the Calibrated
°° g
Accuracy @ 25 °C (77 °F) specification must capture the effect of component aging until the next time the module is calibrated. Primarily, the module's operating conditions, such as temperature, humidity, and power cycling, affect component aging.

Because ControlLogix analog I/O modules operate in different conditions, the specific accuracy deviation from 0.01% of range cannot be measured. Typically, however, a module's
°° y gypy
Calibrated Accuracy @ 25 °C (77 °F) is closer to 0.05% of range than 0.1% of range, as the worst case scenario operating conditions determines 0.1% of range.

A ControlLogix analog I/O module's calibration accuracy at 25 °C (77 °F) is calculated over the full hardware range of the module and is not dependent on the application's use of the range. The error is the same if you are measuring it across a 10% or 100% portion of a given range.

However, a module's accuracy at 25 °C (77 °F) is dependent on the hardware range in which the module operates.

## EXAMPLE

The 1756-IT6I module offers two input ranges, -12…+30 mV and
°° g
-12…+78 mV. Because module error at 25 °C (77 °F) depends on the input range that is used, the module error is as follows when using 0.1% of range accuracy:

- +/- 42 mV for the -12…+30 mV range
- +/- 90 mV for the -12…+78 mV range

These error values are the same whether you use 10% or 100% of the chosen range.

## How Operating Temperature Changes Affect Module Accuracy

These specifications take into account how the module's operating temperature changes can affect a module's accuracy.

## Gain Drift With Temperature

The Gain Drift with Temperature specification represents the calibration inaccuracy that occurs as a module's ambient (that is, operating) temperature drifts from the temperature at which it was calibrated.

You can use the Gain Drift with Temperature specification (varies for each catalog number) to determine the module's calibration inaccuracy for each degree between calibration and operating temperature. The Gain Drift with Temperature specification represents a percentage of the full operating range that the module's calibration is inaccurate to for each degree difference. The specification is determined with the following formula:

Gain Drift with Temperature = (PPM/°C) x Module's Full Range

Because the specifications listed in publication 1756-TD002 include a typical and worst case
° pp
yp
PPM/ °C for each module, you can determine multiple Gain Drift with Temperature values for each module.

## EXAMPLE

For example, the 1756-IT6I module has a maximum Gain Drift with
° p
Temperature specification of 80 ppm/ °C. The 80 ppm represents 0.008% of the module's full operating temperature.

<!-- image -->

ATTENTION: If the module was calibrated to operate in the -12…+78mV input
°° p
range, then following formula is used: (0.008/ °C) x 90 mV = +/-7.2 µV/ °C For every degree Celsius that the module's operating temperature moves from the calibration temperature, the maximum calibration accuracy deviation is +/-7.2 µV.

## Module Error Over Full Temperature Range

The Module Error Over Full Temperature Range specification represents the error that occurs
° pgpp
if the module's ambient temperature changes a total of +/-60 degrees (that is, from 0…60 °C 
°°° pgg
(32…140 °F) or 60…0 °C (140…32 °F)). While this temperature change is extremely unlikely, it represents the worst case scenario.

This specification is determined by multiplying the temperature change by the maximum Gain Drift with Temperature for the given module. In other words, we determine Module Error Over Full Temperature Range with the following formula:

Module Error Over Full Temperature = Full Temperature Range x Gain Drift with Temperature

## EXAMPLE

The 1756-IT6I module has a maximum Gain Drift with Temperature specification = 80 ppm/ °C.

<!-- image -->

ATTENTION: Module Error over Full Temperature Range = 60 °C (full
° g
temperature range) X 80 ppm/ °C (gain drift). The result is 4800 ppm or 0.48%.

## Notes:

## Status Indicators for Input Modules

## Troubleshoot Your Module

Each ControlLogix® analog I/O module has status indicators that display module status. This chapter describes the status indicators on the front of a module and how to use these visual signals to troubleshoot anomalies.

Status indicators show the I/O module state (green), or fault (red).

This illustration and table show the status indicators that are used with analog input modules.

Series A

<!-- image -->

Series B

<!-- image -->

| Status Indicator Display Description   |                                         |                                                                                                    | Action                                                                                                                                |
|----------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| OK                                     | Steady green light                      | The inputs are in a normal operating state                                                         | None                                                                                                                                  |
| OK                                     | Flashing green light                    | The module has passed internal diagnostics but is not currently performing connected communication | None                                                                                                                                  |
| OK                                     | Flashing red light                      | Previously established communication has timed out                                                 | Check controller and chassis communication                                                                                            |
| OK                                     | Steady red light                        | The module is experiencing a Major Fault                                                           | First attempt a Reset. If that does not work, attempt removal and insertion under power (RIUP). If all else fails, replace the module |
|                                        | CAL or CALIBRATION Flashing green light | The module is in Calibration mode                                                                  | Finish calibration                                                                                                                    |

<!-- image -->

## Status Indicators for Output Modules

This illustration and table show the status indicators that are used with analog output modules.

Series A

<!-- image -->

Series B and C

<!-- image -->

| Status Indicator Display Description   |                      |                                                                                                                                                  | Action                                                                                                                                |
|----------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| OK                                     | Steady green light   | The outputs are in a normal operating state in Run mode                                                                                          | None                                                                                                                                  |
| OK                                     | Flashing green light | Either: • the module has passed internal diagnostics and is not actively controlled • a connection is open and the controller is in Program mode | None                                                                                                                                  |
| OK                                     | Flashing red light   | Previously established communication has timed out                                                                                               | Check controller and chassis communication                                                                                            |
| OK                                     | Steady red light     | The module is experiencing a Major Fault                                                                                                         | First attempt a Reset. If that does not work, attempt removal and insertion under power (RIUP). If all else fails, replace the module |
|                                        |                      | CAL or CALIBRATION Flashing green light The module is in Calibration mode Finish calibration                                                     |                                                                                                                                       |

## Use Logix Designer Application for Troubleshooting

The Logix Designer application indicates fault conditions in the following ways:

- Module Fault Icon under I/O Configuration, to the left of the module. This exclamation mark (!) with a yellow triangle around it appears when the communication connection to the module is broken.
- Fault message in the Status Line of any screen.

<!-- image -->

<!-- image -->

- On the Module Info Category, in the Status section, the Major and Minor Faults are listed along with the Internal State of the module.
- Notification in the Tag Editor - General module faults are also reported in the Tag Editor. Diagnostic faults are reported only in the Tag Editor.

<!-- image -->

The Value field indicates a fault with the number 1.

<!-- image -->

## Fault Type Determination

When you are monitoring configuration properties in the Logix Designer application and receive a communication fault message, the Connection category indicates the type of fault under Module Fault.

<!-- image -->

## Notes:

## Access the Tags

## Analog I/O Tag Definitions

Module tags are created when you add a module to the Studio 5000 Logix Designer® application project. The set of tags that are associated with any module depends on the module type and the connection type. There are three sets of tags for each module:

- Configuration
- Input
- Output

You can view tags from the Tag Editor. Complete the following steps.

1. In the Controller Organizer, right-click Controller Tags and choose Monitor Tags.

<!-- image -->

The Controller Tags dialog box appears.

2. Expand the channels as needed in order to view specific tags.

<!-- image -->

<!-- image -->

## Integer Mode Tags

## Integer Input Tags

|                               | Tag Name Data Type Applicable Modules Definition   |                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChannelFaults INT All         |                                                    | Collection of individual channel fault bits in one word. Can address individual channel fault via bit notation: ex. ChannelFaults 3 for channel 3.                                                                                                                                                                                            |
| Ch0Fault BOOL All             |                                                    | Individual channel fault status bit. Indicates a ‘hard’ fault has occurred on the channel that means: calibration is ongoing; or if an input, an overrange or underrange condition is present; or if an output, a low or high clamp condition is occurring. The controller also sets these bits if communication is lost with the I/O module. |
|                               |                                                    | ModuleFaults INT All Collection of all module level fault bits.                                                                                                                                                                                                                                                                               |
|                               |                                                    | AnalogGroupFault BOOL All Indicates if a channel fault has occurred on any channel.                                                                                                                                                                                                                                                           |
| InGroupFault BOOL All inputs  |                                                    | Indicates if a channel fault has occurred on any input channel.                                                                                                                                                                                                                                                                               |
| Calibrating BOOL All          |                                                    | Indicates if a calibration is in progress on any channel.                                                                                                                                                                                                                                                                                     |
| CalFault BOOL All             |                                                    | Status bit indicating if any channel has a ‘bad’ calibration. ‘Bad’ calibration means the last attempt to calibrate the channel failed with an error.                                                                                                                                                                                         |
|                               | CJUnderrange BOOL 1756-IT6I and 1756-IT6I2         | Status bit to indicate if the cold junction reading is beneath the lowest detectable temperature of 0.0 °C (32 ° °F).                                                                                                                                                                                                                                                                                                                                               |
|                               | CJOverrange BOOL 1756-IT6I and 1756-IT6I2          | Status bit to indicate if the cold junction reading is above the highest detectable temperature of 86.0 °C ° (186 °F).                                                                                                                                                                                                                                                                                                                                               |
| ChannelStatus INT All         |                                                    | Collection of individual channel status bits.                                                                                                                                                                                                                                                                                                 |
| Ch0Underrange BOOL All inputs |                                                    | Alarm bits indicating the channel’s input is less than the minimum detectable input signal.                                                                                                                                                                                                                                                   |
| Ch0Overrange BOOL All inputs  |                                                    | Alarms bit indicating the channel’s input is greater than the maximum detectable input signal.                                                                                                                                                                                                                                                |
|                               | Ch0Data INT All inputs                             | The channel input signal represented in counts where -32,768 counts is the minimum detectable input signal and 32,767 counts is the maximum detectable.                                                                                                                                                                                       |
|                               | CJData INT 1756-IT6I and 1756-IT6I2                | The cold junction sensor temperature in counts where -32,768 counts is 0 °C (32 °F) and 32,767 counts is °° j 86 °C (186 °F).                                                                                                                                                                                                                                                                                                                                               |
| CSTTimestamp  Array of DINT   | All (if the CST connection is selected)            | Timestamp that is taken at the time that the input data was sampled or, if an output, when the output was applied, and placed in terms of coordinated system time that is a 64-bit quantity in microseconds coordinated across the rack. Must be addressed in 32-bit chunks as an array.                                                      |
| RollingTimestamp INT All      |                                                    | Timestamp that is taken at the time that the input data was sampled or, if an output, when the output was applied, that is, in terms of milliseconds, relative solely to the individual module.                                                                                                                                               |

## Integer Output Tags

## Integer Output Tags

|                             | Tag Name Data Type Applicable Modules Definition:   |                                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Ch0Data INT All outputs                             | The value the channel is to output in counts where the minimum producible output is -32,768 counts and 32,767 counts is the maximum producible.                                                         |
| Ch0DataEcho INT All outputs |                                                     | The value the channel is outputting in counts where -32,768 counts is the minimum producible output signal and 32,767 counts is the maximum producible.                                                 |
|                             |                                                     | OutGroupFault BOOL All outputs Indicates if a channel fault has occurred on any output channel.                                                                                                         |
|                             | Ch0InHold BOOL All outputs                          | Bit that indicates if the output channel is holding until the Output value sent to the module (O tag Ch0Data) matches the current output value (I tag Ch0Data) within 0.1% of the channel’s full scale. |

The tables in this section list all tags that are available on ControlLogix® analog modules operating in integer mode. The series of tags that are found in each application may vary.

## Integer Input Tags

## Integer Configuration Tags

|                                 | Tag Name Data Type Applicable Modules Definition               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CJDisable BOOL                  | All inputs (only used for the 1756-IT6I and 1756-IT6I2)        | Disables the cold junction sensor that turns off cold junction compensation when linearizing thermocouple inputs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RealTimeSample INT All input    |                                                                | Determines how often the input signal is to be sampled in terms of milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ch0RangeNotch SINT              | 1756-IF6CIS, 1756- IF6I, 1756-IR6I, 1756- IT6I, and 1756-IT6I2 | Configures the channel’s input range and notch filter settings. The input range is the upper nibble (bits 4…7) and determines the signal range the input channel can detect. Input range values are as listed. 0 = -10…10V (1756-IF6I) 1 = 0…5V (1756-IF6I) 2 = 0…10V (1756-IF6I) 3 = 0…20 mA (1756-IF6CIS and 1756-IF6I) 4 = -12…+78 mV (1756-IT6I and 1756-IT6I2) 5 = -12…+30 mV (1756-IT6I and 1756-IT6I2) 6 = 1…487  (1756-IR6I) 7 = 2…1000 (1756-IR6I) 8 = 4…2000  (1756-IR6I) 9 = 8…4020  (1756-IR6I) The notch filter provides excellent frequency filtering at the selected value and its harmonics. The notch filter is the lowest nibble (bits 0…3). 0 = 10 Hz 1 = 50 Hz 2 = 60 Hz 3 = 100 Hz |
| ProgToFaultEn BOOL All outputs  |                                                                | The program to fault enable bit determines how the outputs are expected to behave if a communication fault were to occur while the output module is in the Program mode. When set, the bit causes the outputs to transition to their programmed Fault state if a communication fault occurs while in the Program state. If not set, outputs remain in their configured program state despite a communication fault occurring.                                                                                                                                                                                                                                                                                |
|                                 |                                                                | Ch0Config SINT All outputs Contains all individual configuration bits for a channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ch0HoldForInit BOOL All outputs |                                                                | When set configures the channel to hold, or not change, until initialized with a value within 0.1% of the full scale of its current value when one of the following conditions occurs. 1 = Module initial connection (power up). 2 = Module transition from Program mode back to Run mode. 3 = Module re-establishes communication after a fault.                                                                                                                                                                                                                                                                                                                                                            |
| Ch0Fault Mode BOOL All outputs  |                                                                | Selects the behavior that the output channel is expected to take if a communication fault occurs. Either hold last state (0) or go to a user-defined value (1). Ch0FaultValue defines the value to go to on fault if the bit is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ch0ProgMode BOOL All outputs    |                                                                | Selects the behavior the output channel when transitioned into Program mode. Either hold last state (0) or go to a user-defined value (1). Ch0ProgValue defines the value to go to on fault if the bit is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ch0RampToProg BOOL All outputs  |                                                                | Enables ramping of the output value to a use-defined Program value, Ch0ProgValue, when set. Ramping defines the maximum rate that the output is allowed to transition based on the configured Ch0RampRate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Ch0RampToFault BOOL All outputs |                                                                | Enables ramping of the output value to a user-defined Fault value, Ch0FaultValue, when set. Ramping defines the maximum rate that the output is allowed to transition based on the configured Ch0RampRate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Ch0FaultValue INT All outputs   |                                                                | Defines the value, in counts, the output takes if a communication fault occurs when the Ch0FaultMode bit is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ch0ProgValue INT All outputs    |                                                                | Defines the value, in counts, the output takes when the connection transitions to Program mode if the Ch0ProgMode bit is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Ch0RampRate INT All outputs     |                                                                | Configures the maximum rate that the output value can change when transitioning to either the Ch0FaultValue or Ch0ProgValue if either the Ch0RampToFault or Ch0RampToProg bits are set, respectively. In terms of percent full-scale per second.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Integer Configuration Tags

## Floating Point Mode Tags

## Floating Point Input Tags

|                                 | Tag Name Data Type Applicable Modules Definition   |                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChannelFaults INT All           |                                                    | Collection of individual channel fault bits in one word. Can address individual channel fault via bit notation: ex. ChannelFaults 3 for channel 3.                                                                                                                                                                                                                    |
| Ch0Fault BOOL All               |                                                    | Individual channel fault status bit. Indicates a ‘hard’ fault has occurred on the channel that means: calibration is ongoing; or if an input, an overrange or underrange condition is present; or if an output, a low or high clamp condition is occurring. These bits are also set by the controller if communication is lost with the I/O module.                   |
|                                 |                                                    | ModuleFaults INT All Collection of all module level fault bits.                                                                                                                                                                                                                                                                                                       |
|                                 |                                                    | AnalogGroupFault BOOL All Indicates if a channel fault has occurred on any channel.                                                                                                                                                                                                                                                                                   |
|                                 |                                                    | InGroupFault BOOL All inputs Indicates if a channel fault has occurred on any input channel.                                                                                                                                                                                                                                                                          |
| Calibrating BOOL All            |                                                    | Indicates if a calibration is in progress on any channel.                                                                                                                                                                                                                                                                                                             |
| CalFault BOOL All               |                                                    | Status bit indicating if any channel has a ‘bad’ calibration. ‘Bad’ calibration means the last attempt to calibrate the channel failed with an error and was aborted.                                                                                                                                                                                                 |
| CJUnderrange BOOL               | 1756-IT6I 1756-IT6I2                               | Status bit to indicate if the cold junction reading is beneath the lowest detectable temperature of 0.0°C (32 °F).                                                                                                                                                                                                                                                    |
| CJOverrange BOOL                | 1756-IT6I 1756-IT6I2                               | Status bit to indicate if the cold junction reading is above the highest detectable temperature of 86.0 °C (186.8 ° °F).                                                                                                                                                                                                                                                                                                                                                                       |
| Ch0Status INT All               |                                                    | Collection of individual channel status bits.                                                                                                                                                                                                                                                                                                                         |
| Ch0CalFault BOOL All inputs     |                                                    | Status bit indicating if the channel has a ‘bad’ calibration. ‘Bad’ calibration means the last attempt to calibrate the channel failed with an error and was aborted.                                                                                                                                                                                                 |
|                                 |                                                    | Ch0Underrange BOOL All inputs Alarm bits indicating the channel’s input is less than the minimum detectable input signal.                                                                                                                                                                                                                                             |
| Ch0Overrange BOOL All inputs    |                                                    | Alarms bit indicating the channel’s input is greater than the maximum detectable input signal.                                                                                                                                                                                                                                                                        |
| Ch0RateAlarm BOOL All inputs    |                                                    | Alarm bit that sets when the input channel’s rate of change exceeds the configured Ch0ConfigRateAlarmLimit. Remains set until the rate change drops below the configured limit unless latched via Ch0ConfigRateAlarmLatch in the configuration.                                                                                                                       |
| Ch0LAlarm BOOL All inputs       |                                                    | Low alarm bits that set when the input signal moves beneath the configured low alarm trigger point, Ch0ConfigLAlarmLimit. Remains set until the input signal moves above the trigger point, unless latched via Ch0ConfigProcAlarmLatch or the input is still within the configured alarm deadband, Ch0ConfigAlmDeadband, of the low alarm trigger point.              |
| ChOHAlarm BOOL All inputs       |                                                    | High alarm bit that sets when the input signal moves above the configured high alarm trigger point, Ch0ConfigHAlarmLimit. Remains set until the input signal moves below the trigger point, unless latched viaCh0ConfigProcAlarmLatch or the input is still within the configured alarm deadband, Ch0ConfigAlmDeadband, of the high alarm trigger point.              |
| Ch0LLAlarm BOOL All inputs      |                                                    | Low low alarm bit that sets when the input signal moves beneath the configured low low alarm trigger point, Ch0ConfigLLAlarmLimit. Remains set until the input signal moves above the trigger point, unless latched via Ch0ConfigProcAlarmLatch or the input is still within the configured alarm deadband, Ch0ConfigAlmDeadband, of the low low alarm trigger point. |
| CH0HHAlarm BOOL All inputs      |                                                    | High high alarm bit that sets when the input signal moves above the configured high high alarm trigger point, Ch0ConfigProcAlarmLimit. Remains set until the input signal moves below the trigger point, unless latched via Ch0ConfigAlmDeadband, of the high high alarm trigger point.                                                                               |
|                                 | Ch0Data REAL All inputs                            | The channel input signal represented in engineering units. The input signal is measured and then scaled based on the user configuration.                                                                                                                                                                                                                              |
| CJData REAL                     | 1756-IT6I 1756-IT6I2                               | The cold junction sensor temperature in °C or °F.                                                                                                                                                                                                                                                                                                                     |
| CSTTimestamp  Array of DINT     | All (if the CST connection is selected)            | Timestamp that is taken at the time that the input data was sampled or, if an output, when the output was applied, and placed in terms of coordinated system time that is a 64-bit quantity in microseconds coordinated across the rack. Must be addressed in 32-bit chunks as an array.                                                                              |
| RollingTimestamp INT All inputs |                                                    | Timestamp that is taken at the time that the input data was sampled or, if an output, when the output was applied, which is, in terms of milliseconds, relative solely to the individual module.                                                                                                                                                                      |

The tables in this section list the tags that are available on ControlLogix analog modules operating in floating point mode. The series of tags that are found in each application vary.

## Floating Point Input Tags

## Floating Point Output Tags

|                                 | Tag Name Data Type Applicable Modules Definition:   |                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 |                                                     | Ch0Data REAL All outputs The value the channel is set to output in engineering units based on the configured scaling for the channel.                                                                                                                                                                                            |
| Ch0DataEcho REAL All outputs    |                                                     | The value the channel is outputting in engineering units based on the configured user scaling. This value matches the requested output value, O tag Ch0Data, unless: in Program mode, calibrating, beneath Low Limit, above High Limit, currently ramping or In Hold.                                                            |
|                                 |                                                     | OutGroupFault BOOL All outputs Indicates if a channel fault has occurred on any output channel.                                                                                                                                                                                                                                  |
| Ch0NotANumber BOOL All outputs  |                                                     | Bit indicating the received output value from the controller, O tag Ch0Data, was an invalid IEEE floating point value. When an invalid value is received, the output value holds its last known valid state.                                                                                                                     |
|                                 | Ch0InHold BOOL All outputs                          | Bit that indicates if the output channel is holding until the Output value sent to the module (O tag Ch0Data) matches the current output value (I tag Ch0Data) within 0.1% of the channel’s full scale.                                                                                                                          |
| CH0RampAlarm BOOL All outputs   |                                                     | Alarm bit that sets when the requested output value, Ch0ConfigRampToRun set, and the difference between the new output value that is requested and the current output exceeds the configured ramp limit, Ch0ConfigMaxRampRate. The bit remains set until ramping ceases unless the alarm is latched via Ch0ConfigRampAlarmLatch. |
| Ch0LLimitAlarm BOOL All outputs |                                                     | Alarm bit that sets when the requested output value, Ch0Data, is below the configured low limit, Ch0ConfigLowLimit, in which case the output stops at the configured low limit that the echo reflects. Remains set until the requested output moves above the low limit unless latched by Ch0ConfigLimitAlarmLatch.              |
| Ch0HLimitAlarm BOOL All outputs |                                                     | Alarm bit that sets when the requested output value, Ch0Data, is above the configured high limit, Ch0ConfigHighLimit, in which case the output stops at the configured high limit that the echo reflects. Remains set until the requested output moves below the high limit unless latched by Ch0ConfigLimitAlarmLatch.          |

## Floating Point Configuration Tags

## Floating Point Configuration Tags

| Tag Name                       |            | Data Type Applicable Modules Definition   |                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RemoteTermination BOOL         |            | 1756-IT6I and 1756-IT6I2                  | Indicates if the cold junction sensor is mounted on a remote termination block when set, rather than on the local terminal block. Needed for proper cold junction compensation when linearizing thermocouples.                                                                                                                                                                                         |
| CJDisable                      | BOOL       | 1756-IT6I and 1756-IT6I2                  | Disables the cold junction sensor that turns off cold junction compensation when linearizing thermocouple inputs.                                                                                                                                                                                                                                                                                      |
| TempMode                       | BOOL       | 1756-IR6I, 1756-IT6I, and 1756-IT6I2      | Controls the temperature scale to use on the module. 0 = Celsius 1 = Fahrenheit                                                                                                                                                                                                                                                                                                                        |
| ProgToFaultEn BOOL All outputs |            |                                           | The program to fault enable bit determines how the outputs behave if a communication fault occurs while the output module is in the Program mode. When set, the bit causes the outputs to transition to their programmed Fault state if a communication fault occurs while in the Program state. If not set, outputs remain in their configured Program state despite a communication fault occurring. |
|                                |            |                                           | RealTimeSample INT All input Determines how often the input signal is to be sampled in terms of milliseconds.                                                                                                                                                                                                                                                                                          |
| CJOffset                       | REAL       | 1756-IT6I and 1756-IT6I2                  | Provides a user-defined offset to add into the read cold junction sensor value. Allows a sensor with a built-in bias to be compensated for.                                                                                                                                                                                                                                                            |
| Ch0Config                      | Struct All |                                           | Structure beneath which the channel’s configuration parameters are set.                                                                                                                                                                                                                                                                                                                                |

## Floating Point Output Tags

## Floating Point Configuration Tags (Continued)

| Tag Name                    | Data Type Applicable Modules Definition                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ch0Config RangeTypeNotch    | INT 1756-IF6CIS, 1756-IF6I, 1756-IR6I, 1756-IT6I, and 1756-IT6I2 | determines the signal range the input channel can detect. Input range values are as listed. 0 = -10…10V (1756-IF6I) 1 = 0…5V (1756-IF6I) 2 = 0…10V (1756-IF6I) 3 = 0…20 mA (1756-IF6CIS and 1756-IF6I) 4 = -12…+78 mV (1756-IT6I and 1756-IT6I2) 5 = -12…+30 mV (1756-IT6I and 1756-IT6I2) 6 = 1…487  (1756-IR6I) 7 = 2…1000 (1756-IR6I) 8 = 4…2000  (1756-IR6I) 9 = 8…4020  (1756-IR6I) Sensor type is bits 4…7 and selects the sensor type to use for linearization on the 1756-IR6I, IT6I. Sensor types values are as listed. 0 =no linearization,  (1756-IR6I), mV (1756-IT6I and 1756-IT6I2) 1 = 100 Platinum 385 (1756-IR6I) B (1756-IT6I and 1756-IT6I2) 2 = 200  Platinum 385 (1756-IR6I), C (1756-IT6I and 1756-IT6I2) 3 = 500  Platinum 385 (1756-IR6I), E (1756-IT6I and 1756-IT6I2) 4 = 1000  Platinum 385 (1756-IR6I), J (1756-IT6I and 1756-IT6I2) 5 = 100  Platinum 3916 (1756-IR6I), K (1756-IT6I and 1756-IT6I2) 6 = 200 Platinum 3916 (1756-IR6I), N (1756-IT6I and 1756-IT6I2) 7 = 500 Platinum 3916 (1756-IR6I), R (1756-IT6I and 1756-IT6I2) 8 = 1000  Platinum 3916 (1756-IR6I), S (1756-IT6I and 1756-IT6I2) 9 = 10 Copper 427 (1756-IR6I), T (1756-IT6I and 1756-IT6I2) 10 = 120  Nickel 672 (1756-IR6I), TXK/XK (L) (1756-IT6I2) 11 = 100  Nickel 618 (1756-IR6I), D (1756-IT6I2) 12 = 120  Nickel 618 (1756-IR6I) 13 = 200 Nickel 618 (1756-IR6I) 14 = 500 Nickel 618 (1756-IR6I) The notch filter provides excellent frequency filtering at the selected value and its harmonics. The notch filter is the lower nibble (bits 0…3). 0 = 10 Hz 1 = 50 Hz 2 = 60 Hz 3 = 100 Hz 4 = 250 Hz |
| Ch0ConfigAlarm Disable      | BOOL All                                                         | Disables all alarms for the channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Ch0ConfigProcess AlarmLatch | BOOL All inputs                                                  | Enables latching for all four process alarms: low, low low, high, and high high. Latching causes the process alarm to remain set until an unlatch service is explicitly sent to the channel or alarm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Ch0ConfigRate AlarmLatch    | BOOL All inputs                                                  | Enables latching for the rate alarm. Latching causes the rate alarm to remain set until an unlatch service is explicitly sent to the channel or alarm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ch0ConfigDigital Filter     | INT All inputs                                                   | A nonzero value enables the filter, providing a time constant in milliseconds used in a first order lag filter to smooth the input signal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ch0ConfigTenOhm Offset      | INT 1756-IR6I                                                    | A value from -100…+100 that represents -1.00…+1.00  and is an offset used when linearizing a 10  copper sensor type’s input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Ch0ConfigRate AlarmLimit    | INT All inputs                                                   | The trigger point for the rate alarm status bit that sets if the input signal changes at a rate faster than the configured rate alarm. Configured in percent full scale per second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ch0ConfigLow Signal         | REAL All                                                         | One of the four points used in scaling. The low signal is in terms of the inputs signal units and corresponds to the low engineering term when scaled. The scaling equation is as follows. Data =  + LowEngineering (Signal - Low Signal) x (High Engineering - Low Engineering) (High Signal - Low Signal)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Ch0ConfigHigh Signal        | REAL All                                                         | One of the four points used in scaling. The high signal is in terms of the inputs signal units and corresponds to the high engineering term when scaled. The scaling equation is as follows. Data =  + LowEngineering (Signal - Low Signal) x (High Engineering - Low Engineering) (High Signal - Low Signal)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Ch0ConfigLow Engineering    | REAL All                                                         | One of the four points used in scaling. The low engineering helps determine the engineering units the signal values scale into. The low engineering term corresponds to the low signal value. The scaling equation is as follows. Data =  + LowEngineering (Signal - Low Signal) x (High Engineering - Low Engineering) (High Signal - Low Signal)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Floating Point Configuration Tags (Continued)

| Tag Name                               | Data Type Applicable Modules Definition   |                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C0ConfigHigh Engineering               | REAL All                                  | One of the four points used in scaling. The high engineering helps determine the engineering units the signal values scale into. The high engineering term corresponds to the high signal value. The scaling equation is as follows. Data =  + LowEngineering (Signal - Low Signal) x (High Engineering - Low Engineering) (High Signal - Low Signal) |
| Ch0ConfigLAlarm Limit                  | REAL All inputs                           | The low alarm trigger point. Causes the Ch0LAlarm to trigger when the input signal moves beneath the configured trigger point. In terms of engineering units.                                                                                                                                                                                         |
| Ch0ConfigHAlarm Limit                  | REAL All inputs                           | The high alarm trigger point. Causes the Ch0HAlarm to trigger when the input signal moves above the configured trigger point. In terms of engineering units.                                                                                                                                                                                          |
| Ch0ConfigLLAlarm Limit                 | REAL All inputs                           | The low low alarm trigger point. Causes the Ch0LLAlarm to trigger when the input signal moves beneath the configured trigger point. In terms of engineering units.                                                                                                                                                                                    |
| Ch0ConfigHH AlarmLimit                 | REAL All inputs                           | The high high alarm trigger point. Causes the Ch0HHAlarm to trigger when the input signal moves above the configured trigger point. In terms of engineering units.                                                                                                                                                                                    |
| Ch0ConfigAlarm Deadband                | REAL All inputs                           | Forms a deadband around the process alarms that causes the corresponding process alarm status bit to remain set until the input moves beyond the trigger point by greater than the amount of the alarm deadband.                                                                                                                                      |
|                                        |                                           | Ch0ConfigCalBias REAL All inputs A user-defined offset added directly into the data, Ch0Data. used to compensate for inherent sensor offset.                                                                                                                                                                                                          |
|                                        |                                           | Ch0ConfigConfig Bits INT All outputs Collection of channel’s individual configuration bits.                                                                                                                                                                                                                                                           |
| Ch0ConfigHoldForInit BOOL All outputs  |                                           | When set configures the channel to hold, or not change, until initialized with a value within 0.1% of full scale of its current value when one of the following conditions occurs. 1 = Module initial connection (power up) 2 = Module transition from Program mode back to Run mode 3 = Module re-establishes communication after a fault            |
| Ch0ConfigRamp AlarmLatch               | BOOL All outputs                          | Enables latching for the rate alarm. Latching causes the rate alarm to remain set until an unlatch service is explicitly sent to the channel or alarm.                                                                                                                                                                                                |
| Ch0ConfigLimit AlarmLatch              | BOOL All outputs                          | Enables latching for the clamp limit alarms. Latching causes the limit alarms to remain set until an unlatch service is explicitly sent to the channel or alarm.                                                                                                                                                                                      |
| Ch0ConfigFault Mode                    | BOOL All outputs                          | Selects the behavior that the output channel takes if a communication fault is to occur. Either hold last state (0) or go to a user-defined value (1). Ch0ConfigFaultValue defines the value to go to on fault if the bit is set.                                                                                                                     |
| Ch0ConfigProg Mode                     | BOOL All outputs                          | Selects the behavior that the output channel takes when transitioned into Program mode. Either hold last state (0) or go to a user-defined value (1). Ch0ConfigProgValue defines the value to go to on program if the bit is set.                                                                                                                     |
| Ch0ConfigRampTo Run                    | BOOL All outputs                          | Enables ramping of the output value during Run mode between the current output level and a newly requested output. Ramping defines the maximum rate that the output is allowed to transition based on the configured Ch0ConfigRampRate.                                                                                                               |
| Ch0ConfigRampTo Prog BOOL All outputs  |                                           | Enables ramping of the output value to a user-defined program value, Ch0ConfigProgValue, when set. Ramping defines the maximum rate that the output is allowed to transition based on the configured Ch0ConfigRampRate.                                                                                                                               |
| Ch0ConfigRampTo Fault BOOL All outputs |                                           | Enables ramping of the output value to a user-defined Fault value, Ch0FaultValue, when set. Ramping defines the maximum rate that the output is allowed to transition based on the configured Ch0ConfigRampRate.                                                                                                                                      |
| Ch0ConfigMax RampRate                  | INT All outputs                           | Configures the maximum rate that the output value can change when transitioning to either the Ch0ConfigFaultValue or Ch0ConfigProgValue if either the Ch0ConfigRampToFault or Ch0ConfigRampToProg bits are set, respectively, or in Run mode if Ch0ConfigRampToRun is set. In terms of percent full-scale per second.                                 |
| Ch0ConfigFault Value                   | REAL All outputs                          | Defines the value, in engineering terms, the output takes if a communication fault occurs when the Ch0ConfigFaultMode bit it set.                                                                                                                                                                                                                     |
| Ch0ConfigProg Value                    | REAL All outputs                          | Defines the value, in engineering units, the output takes when the connection transitions to Program mode if the Ch0ConfigProgMode bit is set.                                                                                                                                                                                                        |
| Ch0ConfigLow Limit                     | REAL All outputs                          | Defines the minimum value that the output is allowed to take within the process. If an output beneath the low limit is requested, the Ch0LLimit alarm is set and the output signal remains at the configured low limit.                                                                                                                               |
| Ch0ConfigHigh Limit                    | REAL All outputs                          | Defines the maximum value that the output is allowed to take within the process. If an output above the high limit is requested, the Ch0HLimit alarm is set and the output signal remains at the configured high limit.                                                                                                                               |

## Notes:

## Module Wiring Options

<!-- image -->

## 1492 AIFMs for Analog I/O Modules

As an alternative to buying RTBs and connecting the wires yourself, you can buy a wiring system that connects to I/O modules through pre-wired and pre-tested cables.

## IMPORTANT

The ControlLogix® system has been agency certified using only the ControlLogix RTBs (1756-TBCH, 1756-TBNH, 1756-TBSH, and 1756-TBS6H). Any application that requires agency certification of the ControlLogix system using other wiring termination methods can require application specific approval by the certifying agency.

The combinations include the following:

- Analog interface modules (AIFMs) mount on DIN rails to provide the output terminal blocks for the I/O module. Use the AIFMs with the pre-wired cables that match the I/O module to the interface module.

<!-- image -->

Feed-through and fusible AIFMs let you customize the wiring system to your application. The fused AIFMs have 24V DC blown fuse indicators to locate and replace blown fuses.

For a complete list of the AIFMs available for use with ControlLogix analog I/O modules, see the table on page 136 .

- Pre-wired cables have a pre-wired RTB on one end to connect to the front of an analog
- I/O module and a D-shell connector on the other end to plug into a D-shell terminal.

The D-shell connectors, with either 15 or 25 pins, have a slide-locking mechanism for a more secure connection.

For a complete list of the pre-wired cables available for use with ControlLogix analog I/ O modules, see the table on page 137 .

## Pre-wired and AIFM Cables

This table lists the AIFMs and pre-wired cables that can be used with ControlLogix analog I/O modules.

| IMPORTANT   | IFMs and prewired cables are not rated for harsh environments (corrosive atmosphere, extended temperature, etc.). When they are used in a system with products that are rated for harsh environments, the system is derated to the specification values of the IFMs and cables.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

IMPORTANT

For the latest list, see the Digital/Analog Programmable Controller Wiring Systems Technical Data, publication 1492-TD008 .

| I/O Cat. No.(1) Mode   |                      | AIFM Cat. No. (Fixed Terminal Block)   | AIFM Cat. No. (RTB Socket Assembly)   | AIFM Type Description                                                                             | Pre-wired Cable(2) (x=cable length)   |
|------------------------|----------------------|----------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------|
| 1756-IF6CIS            | 1756-IF6CIS          | 1492-AIFM6S-3                          | 1492-RAIFM6S-3(3)                     |                                                                                                   | 1492-ACABLExZ                         |
| 1756-IF6I              | Current              | 1492-AIFM6S-3                          | 1492-RAIFM6S-3(3)                     | 6-channel isolated with 3…4 terminals/channel                                                     | 1492-ACABLExX                         |
| 1756-IF6I              | Voltage              | 1492-AIFM6S-3                          | 1492-RAIFM6S-3(3)                     | Feed-through                                                                                      | 1492-ACABLExY                         |
| 1756-IF8, 1756-IF8K    | Single-ended current | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | 8- or 16-channel input or output with 3 terminals/channel                                         | 1492-ACABLExTB                        |
| 1756-IF8, 1756-IF8K    | Single-ended current |                                        |                                       | 1492-AIFM8-F-5 N/A Fusible 8-channel input with 24V DC blown fuse indicators, 3 terminals/channel | 1492-ACABLExTB                        |
| 1756-IF8, 1756-IF8K    | Single-ended voltage | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExTA                        |
| 1756-IF8, 1756-IF8K    | Single-ended voltage |                                        |                                       | 1492-AIFM8-F-5 N/A Fusible 8-channel input with 24V DC blown fuse indicators, 3 terminals/channel | 1492-ACABLExTA                        |
| 1756-IF8, 1756-IF8K    | Differential current | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExTD                        |
| 1756-IF8, 1756-IF8K    | Differential current |                                        |                                       | 1492-AIFM8-F-5 N/A Fusible 8-channel input with 24V DC blown fuse indicators, 3 terminals/channel | 1492-ACABLExTD                        |
| 1756-IF8, 1756-IF8K    | Differential voltage | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExTC                        |
| 1756-IF8, 1756-IF8K    | Differential voltage |                                        |                                       | 1492-AIFM8-F-5 N/A Fusible 8-channel input with 24V DC blown fuse indicators, 3 terminals/channel | 1492-ACABLExTC                        |
| 1756-IF16, 1756-IF16K  | Single-ended current | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExUB                        |
| 1756-IF16, 1756-IF16K  | Single-ended current | 1492-AIFM16-F-3                        |                                       | 16-channel input with 24V DC blown fuse indicators, 3 terminals/channel                           | 1492-ACABLExUB                        |
| 1756-IF16, 1756-IF16K  | Single-ended current | 1492-AIFM16-F-5                        | N/A                                   | Fusible  16-channel input with 24V DC blown fuse indicators, 5 terminals/channel                  | 1492-ACABLExUB                        |
| 1756-IF16, 1756-IF16K  | Single-ended voltage | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExUA                        |
| 1756-IF16, 1756-IF16K  | Single-ended voltage | 1492-AIFM16-F-3                        | N/A                                   | Fusible  16-channel input with 24V DC blown fuse indicators, 3 terminals/channel                  | 1492-ACABLExUA                        |
| 1756-IF16, 1756-IF16K  | Single-ended voltage | 1492-AIFM16-F-5                        | N/A                                   | 16-channel input with 24V DC blown fuse indicators, 5 terminals/channel                           | 1492-ACABLExUA                        |
| 1756-IF16, 1756-IF16K  | Differential current | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExUD                        |
| 1756-IF16, 1756-IF16K  | Differential current | 1492-AIFM8-F-5                         | N/A                                   | 8-channel input with 24V DC blown fuse indicators, 5 terminals/channel                            | 1492-ACABLExUD                        |
| 1756-IF16, 1756-IF16K  | Differential current | 1492-AIFM16-F-3                        | N/A                                   | Fusible 16-channel input with 24V DC blown fuse indicators, 3 terminals/channel                   | 1492-ACABLExUD                        |
| 1756-IF16, 1756-IF16K  | Differential current | 1492-AIFM16-F-5                        | N/A                                   | 16-channel input with 24V DC blown fuse indicators, 5 terminals/channel                           | 1492-ACABLExUD                        |
| 1756-IF16, 1756-IF16K  | Differential voltage | 492-AIFM8-3                            | 1492-RAIFM8-3(4)                      | Feed-through 8- or 16-channel input or output with 3 terminals/channel                            | 1492-ACABLExUC                        |
| 1756-IF16, 1756-IF16K  | Differential voltage | 1492-AIFM8-F-5                         | N/A                                   | 8-channel input with 24V DC blown fuse indicators, 5 terminals/channel                            | 1492-ACABLExUC                        |
| 1756-IF16, 1756-IF16K  | Differential voltage | 1492-AIFM16-F-3                        | N/A                                   | Fusible 16-channel input with 24V DC blown fuse indicators, 3 terminals/channel                   | 1492-ACABLExUC                        |
| 1756-IF16, 1756-IF16K  | Differential voltage | 1492-AIFM16-F-5                        | N/A                                   | 16-channel input with 24V DC blown fuse indicators, 5 terminals/channel                           | 1492-ACABLExUC                        |
| 1756-IR6I              |                      | 1492-AIFM6S-3                          | 1492-RAIFM6S-3(3)                     | Feed-through 6-channel isolated with 3…4 terminals/channel 1492-ACABLExZ                          |                                       |
| 1756-IT6I              |                      |                                        |                                       | 1492-AIFM6TC-3 N/A Thermocouple 6-channel with 3 terminals/channel                                | 1492-ACABLExY                         |
| 1756-IT6I2             |                      |                                        |                                       | 1492-AIFM6TC-3 N/A Thermocouple 6-channel with 3 terminals/channel                                | 1492-ACABLExYT                        |
| 1756-OF4,              | Current              | 1492-AIFM4-3                           | 1492-RAIFM4-3(5)                      | 4-channel input, output, or 2-in/2-out combination with 3 terminals/channel                       | 1492-ACABLExVB                        |
| 1756-OF4K 1756-OF6CI   | Voltage              | 1492-AIFM4-3                           | 1492-RAIFM4-3(5)                      | 4-channel input, output, or 2-in/2-out combination with 3 terminals/channel                       | 1492-ACABLExVA                        |
| 1756-OF6VI             |                      | 1492-AIFM6S-3                          | 1492-RAIFM6S-3(3)                     | Feed-through 6-channel isolated with 3…4 terminals/channel 1492-ACABLExY                          |                                       |
| 1756-OF8,              | Current              | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      | 8- or 16-channel input or output with 3 terminals/channel                                         | 1492-ACABLExWB                        |
| 1756-OF8K              | Voltage              | 1492-AIFM8-3                           | 1492-RAIFM8-3(4)                      |                                                                                                   | 1492-ACABLExWA                        |

(1) Some analog I/O modules can be operated in up to four modes (current/voltage, single-ended/differential) based on connections. In all cases, each channel is factory-configured for the same mode. However, you can field configure any channel for another mode. You may need to alter the terminal block wiring to match the application. See the controller installation manual for further information.

(2) Cables are available in lengths of 0.5 m (1.6 ft), 1.0 m (3.3 ft), 2.5 m (8.2 ft), and 5.0 m (16.4 ft). To order, insert the code for the desired cable length into the catalog number in place of the x: 005=0.5 m, 010=1.0 m, 025=2.5 m, 050=5 m. Example: 1492-ACABLE025TB is for a 2.5 m (8.2 ft) cable, and the letters TB.

(3) Compatible RTB plug; 1492-RTB12N (screw-style terminals) or 1492-RTB12P (push-in style terminals). Order plugs separately.

(4) Compatible RTB plug; 1492-RTB16N (screw-style terminals) or 1492-RTB16P (push-in style terminals). Order plugs separately

(5) Compatible RTB plug; 1492-RTB8N (screw-style terminals) or 1492-RTB8P (push-in style terminals). Order plugs separately.

## Module-ready Pre-wired Cables

This table describes the I/O module-ready pre-wired cables available for use with your ControlLogix analog I/O modules.

| Cat. No.(1)    | No. of Conductors(2) (3)                  | Conductor Size   |                    | Nominal Outer Diameter RTB at the I/O Module End   |
|----------------|------------------|------------------|--------------------|----------------------------------------------------|
| 1492-ACABLExM  | 11 twisted pairs | 22 AWG           | 11.5 mm (0.45 in.) | 1756-TBCH                                          |
| 1492-ACABLExX  | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBNH                                          |
| 1492-ACABLExY  | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBNH                                          |
| 1492-ACABLExYT | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBNH                                          |
| 1492-ACABLExZ  | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBNH                                          |
| 1492-ACABLExTA | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExTB | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExTC | 5 twisted pairs  | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExTD | 5 twisted pairs  | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExUA | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExUB | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBCH                                          |
| 1492-ACABLExUC | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBCH                                          |
| 1492-ACABLExUD | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBCH                                          |
| 1492-ACABLExVA | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBNH                                          |
| 1492-ACABLExVB | 20 conductors    | 22 AWG           | 8.4 mm (0.33 in.)  | 1756-TBNH                                          |
| 1492-ACABLExWA | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBNH                                          |
| 1492-ACABLExWB | 9 twisted pairs  | 22 AWG           | 6.8 mm (0.27 in.)  | 1756-TBNH                                          |

## Notes:

## 1756-IF6CIS and 1756-IF6I Module Features

<!-- image -->

## 6-channel Isolated Analog I/O Modules

This appendix offers reference information regarding the discontinued 6-channel 1756-IF6CIS, 1756-IF6I, 1756-OF6CI, and 1756-OF6VI ControlLogix® isolated analog I/O modules.

For information about how to migrate from 6-channel 1756 isolated analog I/O modules to newer 8-channel modules, see Migrating 6-Channel to 8-Channel 1756 Analog Modules , publication 1756-RM011 .

This section describes features specific to the ControlLogix sourcing current loop input module (1756-IF6CIS) and the isolated analog voltage/current input module (1756-IF6I).

## IMPORTANT

The 1756-IF6CIS and 1756-IF6I modules primarily operate the same with a few exceptions, including:

- The 1756-IF6CIS only operates in current mode.
- The 1756-IF6CIS offers an isolated power source for each channel that supplies power to external transmitters.

## 1756-IF6CIS Module Isolated Power Source

The 1756-IF6CIS module offers an internal power source on each channel. The source is current limited to 28 mA and allows the module to power a two-wire transmitter directly without the need for an external power supply. The transmitter can then vary the current to the analog input in proportion to the process variable being measured. The inclusion of an internal onboard current source saves you the expense of extra power supplies and greatly simplifies the interface wiring to field devices.

In addition to supplying loop power to two-wire transmitters, the module can also accommodate current loops that are powered by an external supply and loops that use fourwire transmitters.

Power Calculations with the 1756-IF6CIS Module

The 1756-IF6CIS module uses the system power supply (1756-Px7x) as the source for loop power. Because of the demands placed on that supply (that is, the 1756-IF6CIS module consumes 7.9 W of backplane power), special care must be taken when calculating the power requirements for modules in the same chassis as a 1756-IF6CIS module.

For example, when used with the 1756-L55M13 controller, you can place only eight 1756-IF6CIS modules in the chassis before exceeding the wattage capacity of the power supply.

Other Devices in the Wiring Loop

The voltage source on each channel can drive loop impedance of up to 1000 ohms. This lets you include other devices, such as chart recorders and meters, in the current loop.

For more information on wiring the 1756-IF6CIS module, see page 148 .

## Available Notch Filter Settings

| Notch Setting                                                        | 10 Hz 50 Hz 60 Hz (Default) 100 Hz 250 Hz 1000 Hz                       |                                      |
|----------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------|
| Minimum Sample Time (RTS) – Integer mode (1)                                                                      |                                                                         | 102 ms 22 ms 19 ms 12 ms 10 ms 10 ms |
| Minimum Sample Time (RTS) – Floating point mode (2)                                                                      | 102 ms 25 ms 25 ms 25 ms 25 ms 25 ms                                    |                                      |
| 0…100% Step Response Time (2)                                        | 400 ms + RTS 80 ms + RTS 68 ms + RTS 40 ms + RTS 16 ms + RTS 4 ms + RTS |                                      |
| -3 dB Frequency 3 Hz 13 Hz 15 Hz 26 Hz 66 Hz 262 Hz                  |                                                                         |                                      |
| Effective Resolution 16 bits 16 bits 16 bits 16 bits 15 bits 10 bits |                                                                         |                                      |

## Data Format Options

Data format determines the format of the data that is returned from the module to the ownercontroller and the features that are available to your application.

## Features Available in Each Data Format

| Data Format                      | Features Available                                    | Features Not Available                               |
|----------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Integer mode                     | Multiple input ranges Notch filter Real-time sampling | Digital filtering Process alarms Rate alarms Scaling |
| Floating point mode All features |                                                       | N/A                                                  |

## Multiple Input Ranges

You can only use the 1756-IF6CIS module in current applications. Unlike other analog input modules, this module does not let you choose an input range. All channels use the 0…20 mA input range.

For the 1756-IF6I module, however, you can select from a series of operational ranges for each channel on your module. The range designates the minimum and maximum signals that are detectable by the module. The 1756-IF6I module offers multiple input ranges in both current and voltage applications.

## Possible Input Ranges Available For Use With the 1756-IF6CIS and 1756-IF6I Modules

| Module      | Input Ranges               |
|-------------|----------------------------|
| 1756-IF6CIS | 0…20 mA                    |
| 1756-IF6I   | -10…10V 0…5V 0…10V 0…20 mA |

## Notch Filter

An analog-to-digital converter (ADC) filter removes line noise in your application for each channel .

Choose a notch filter that most closely matches the anticipated noise frequency in your application. Each filter time affects the response time of your module and the highest frequency notch filter settings also limit the effective resolution of the channel.

| IMPORTANT   | 60 Hz is the default setting for the notch filter.   |
|-------------|------------------------------------------------------|

## Real-time Sampling

This parameter instructs the module to scan its input channels and obtain all available data. After the channels are scanned, the module multicasts that data.

During module configuration, you specify a real-time sampling (RTS) period and a requested packet interval (RPI) period. These features both instruct the module to multicast data, but only the RTS feature instructs the module to scan its channels before multicasting.

## Underrange/Overrange Detection

This alarm feature detects when the isolated input module is operating beyond limits set by the input range.

This table lists the input ranges of the 1756-IF6CIS and 1756-IF6I modules and the lowest/ highest signal available in each range before the module detects an underrange/overrange condition.

| Input Module   | Range                           |                       | Lowest Signal in Range Highest Signal in Range   |
|----------------|---------------------------------|-----------------------|--------------------------------------------------|
| 1756-IF6CIS    | 0 mA…20 mA                      | 0 mA                  | 21.09376 mA                                      |
| 1756-IF6I      | +/- 10V 0V…10V 0V…5V 0 mA…20 mA | -10.54688V 0V 0V 0 mA | 10.54688V 10.54688V 5.27344V 21.09376 mA         |

## IMPORTANT

Be careful when 'disabling all alarms' on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not 'disable all alarms'.

We recommend that you disable only unused channels so extraneous alarm bits aren't set.

## Digital Filter

The digital filter smooths input data noise transients on each input channel. This value specifies the time constant for a digital, first-order lag filter on the input. It's specified in units of milliseconds. A value of 0 (zero) disables the filter.

IMPORTANT The digital filter is available only in applications that use floating point mode.

The digital filter equation is a classic, first order lag equation.

<!-- formula-not-decoded -->

Yn = Present output, filtered peak voltage (PV)

Yn-1 = Previous output, filtered PV

t = Module channel update time (seconds)

TA = Digital filter time constant (seconds)

Xn = Present input, unfiltered PV

As shown in this illustration, by using a step input change to illustrate the filter response, you see that 63.2% of the total response is reached when the digital filter time constant elapses. Each additional time constant achieves 63.2% of the remaining response.

<!-- image -->

## Process Alarms

Process alarms alert you when the module has exceeded configured high or low limits for each channel. You can latch process alarms. These are set at four, user-configurable, alarm trigger points.

- High high
- High
- Low
- Low low

## IMPORTANT

## Alarm Deadband

You can configure an alarm deadband to work with these alarms. The deadband allows the process alarm status bit to remain set, despite the alarm condition disappearing, as long as the input data remains within the deadband of the process alarm.

This illustration shows input data that sets each of the four alarms at some point during module operation. In this example, latching is disabled; therefore, each alarm turns Off when the condition that caused it to set ceases to exist.

## Process Alarms Set by Input Data

<!-- image -->

Process alarms are available only in applications that use floating point mode. The values for each limit are entered in scaled engineering units.

## Rate Alarm

The rate alarm triggers if the rate of change between input samples for each channel exceeds the specified trigger point for that channel.

## IMPORTANT

The rate alarm is available only for applications that use floating point mode.

## EXAMPLE

## EXAMPLE

1756-IF6CIS Module

If you set a 1756-IF6CIS module (with normal scaling in mA) to a rate alarm of 1.0 mA/s, the rate alarm only triggers if the difference between measured input samples changes at a rate &gt; 1.0 mA/s.

If the module's RTS is 100 ms (that is, sampling new input data every 100 ms) and at time 0, the module measures 5.0 mA and at time 100 ms measures 5.08 mA, the rate of change is (5.08 mA-5.0 mA)/(100 ms) = 0.8 mA/s. The rate alarm wouldn't set as the change is less than the trigger point of 1.0 mA/s.

If the next sample taken is 4.9 mA, the rate of change is

(4.9 mA-5.08V)/(100 ms)=-1.8 mA/s. The absolute value of this result is &gt; 1.0 mA/s, so the rate alarm sets. Absolute value is used because the rate alarm checks for the magnitude of the rate of change being beyond the trigger point, whether a positive or negative excursion.

1756-IF6I Module

If you set a 1756-IF6I module (with normal scaling in volts) to a rate alarm of 1.0V/s, the rate alarm only triggers if the difference between measured input samples changes at a rate &gt; 1.0V/s.

If the module's RTS is 100 ms (that is, sampling new input data every 100 ms) and at time 0, the module measures 5.0V and at time 100 ms measures 5.08V, the rate of change is (5.08V-5.0V)/(100 ms) = 0.8V/s. The rate alarm wouldn't set as the change is less than the trigger point of 1.0V/s.

If the next sample taken is 4.9V, the rate of change is (4.9V-5.08V)/(100 ms)=-1.8V/s. The absolute value of this result is &gt; 1.0V/s, so the rate alarm sets. Absolute value is used because the rate alarm checks for the magnitude of the rate of change being beyond the trigger point, whether a positive or negative excursion.

## Wire Off Detection

| IMPORTANT   | Be careful when ‘disabling all alarms’ on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not ‘disable all alarms’. We recommend that you disable only unused channels so extraneous alarm bits aren’t set.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The 1756-IF6CIS and 1756-IF6I modules alert you when a wire has been disconnected from one of its channels or the RTB has been removed from the module. Two events occur when a wire off condition occurs for this module.

- Input data for that channel changes to a specific scaled value.
- A fault bit is set in the owner-controller that can indicate the presence of a wire off condition.

Because the 1756-IF6I module can be used in voltage or current applications, differences exist as to how a wire off condition is detected in each application. The 1756-IF6CIS module can only be used in current mode.

## Wire Off Conditions in Various Applications

| Wire Off Condition Occurrence               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Voltage Applications 1756-IF6I Modules Only | • Input data for that channel changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,767 counts in integer mode. • The ChxOverrange (x=channel number) tag is set to 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Current Applications                        | When the condition occurs because a wire is disconnected: • Input data for that channel changes to the scaled value associated with the underrange signal value of the selected operational range in floating point mode (minimum possible scaled value) or -32,768 counts in integer mode. • The ChxUnderrange (x=channel number) tag is set to 1. When the condition occurs because the RTB has been disconnected from the module (1756-IF6I module only): • Input data for that channel changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,767 counts in integer mode. • The ChxOverrange (x=channel number) tag is set to 1. |

For more tag information, see Appendix A .

## Module Block and Input Circuit Diagrams

This section shows the block and input circuit diagrams for the 1756-IF6CIS and 1756-IF6I modules.

## 1756-IF6CIS and 1756-IF6I Module Block Diagram

<!-- image -->

= Channel Isolation

## Field-side Circuit Diagrams

These diagrams show field-side circuitry for the 1756-IF6CIS and 1756-IF6I modules.

## 1756-IF6CIS Module Input Circuit

<!-- image -->

## 1756-IF6I Module Input Circuit

<!-- image -->

## 1756-IF6CIS Module Wiring

This section details current and voltage wiring examples for the 1756-IF6CIS module.

Two-wire Transmitter Connected to a 1756-IF6CIS Module Providing 24V DC Loop Power

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Place additional loop devices (that is, strip chart recorders) at either 'A' location in the current loop.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## Four-wire Transmitter Connected to a 1756-IF6CIS Module and an External, User-provided Power Supply Providing 24V DC Loop Power

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Place additional loop devices (that is, strip chart recorders) at either 'A' location in the current loop.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## Two-wire Transmitter Connected to a 1756-IF6CIS Module and an External, User-provided Power Supply Providing 24V DC Loop Power

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Place additional loop devices (that is, strip chart recorders) at either 'A' location in the current loop.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF6I Module Wiring

This illustration shows a wiring example for the 1756-IF6I module.

<!-- image -->

Keep in mind the following:

- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF6I Module Current Wiring Example with a Four-Wire Transmitter

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Place additional loop devices (that is, strip recorders) at either 'A' location.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IF6I Module Current Wiring Example with a Two-Wire Transmitter

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Place additional loop devices (that is, strip recorders) at either 'A' location.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## Module Fault Word

(described on page 155

15 = AnalogGroupFault

14 = InGroupFault

12 = Calibrating

11 = Cal Fault

13 isn't used by the 1756-IF6CIS

or 1756-IF6I

## Channel Fault Word

(described on page 155)

5 = Ch5Fault

4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

0 = Ch0Fault

## Channel Status Words

(one for each channel, described on page 155)

7 = ChxCalFault

6 = ChxUnderrange

5 = ChxOverrange

4 = ChxRateAlarm

3 = ChxLAlarm

2 = ChxHAlarm

1 = ChxLLAlarm

0 = ChxHHAlarm

## 1756-IF6CIS or 1756-IF6I Module Fault and Status Reporting

The 1756-IF6CIS and 1756-IF6I modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a manner as to let you choose the level of granularity that is desired for examining fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                                                        |
| Channel Fault Word   | This word provides underrange, overrange, and communications fault reporting. Its tag name is ChannelFaults.                                                       |
| Channel Status Words | This word provides individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults. Its tag name is ChxStatus. |

## IMPORTANT

Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.

Fault Reporting in Floating Point Mode

This illustration provides an overview of the fault reporting process for the 1756-IF6CIS or 1756-IF6I module in floating point mode.

<!-- image -->

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module. You can examine further down to isolate the fault.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-IF6CIS, 1756-IF6I Module Fault Word Bits – Floating Point Mode

| Tag         | Description                                                                                                             | Tag Name    |
|-------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
|             | Analog Group Fault This bit is set when any bits in the Channel Fault word are set. AnalogGroupFault                    |             |
|             | Input Group Fault This bit is set when any bits in the Channel Fault word are set. InGroupFault                         |             |
| Calibrating | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. | Calibrating |
|             | Calibration Fault This bit is set when any individual Channel Calibration Fault bits are set. CalFault                  |             |

During normal module operation, bits in the Channel Fault word are set if any of the respective channels has an Under or Overrange condition. Checking this word for a nonzero value is a quick way to check for Under or Overrange conditions on the module.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

## 1756-IF6CIS, 1756-IF6I Channel Fault Word Bits – Floating Point Mode

| Condition                                                                                        | Display              |
|--------------------------------------------------------------------------------------------------|----------------------|
| A channel is being calibrated.                                                                   | ’003F’ for all bits. |
| A communication fault occurred between the module and its owner-controller. ’FFFF’ for all bits. |                      |

Your logic can monitor the Channel Fault Word bit for a particular input to determine the state of that point.

Any of the six Channel Status words, one for each channel, displays a nonzero condition if that particular channel has faulted for the conditions that are listed in the following table. Some of these bits set bits in other Fault words. When the Underrange and Overrange bits (bits 6 &amp; 5) in any of the words are set, the appropriate bit is set in the Channel Fault word.

When the Calibration Fault bit (bit 7) is set in any of the words, the Calibration Fault bit (bit 11) is set in the Module Fault word.

This table lists the conditions that set each of the word bits.

## 1756-IF6CIS, 1756-IF6I Channel Status Word Bits – Floating Point Mode

|                    | Tag (Status Word) Bit Event That Sets This Tag                                                                                                                                                                                                                                                                                                     |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxCalFault Bit 7  | This bit is set if an error occurs during calibration for that channel, causing a bad calibration. This bit also sets bit 11 in the Module Fault word.                                                                                                                                                                                             |
| Underrange Bit 6   | This bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 141. This bit also sets the appropriate bit in the Channel Fault word.                                                                                |
| Overrange Bit 5    | This bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 141. This bit also sets the appropriate bit in the Channel Fault word.                                                                             |
| ChxRateAlarm Bit 4 | This bit is set when the input channel’s rate of change exceeds the configured Rate Alarm parameter. It remains set until the rate of change drops below the configured rate. If latched, the alarm remains set until it’s unlatched.                                                                                                              |
| ChxLAlarm BIt 3    | This bit is set when the input signal moves beneath the configured Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.         |
| ChxHAlarm Bit 2    | This bit is set when the input signal moves above the configured High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.          |
| ChxLLAlarm Bit 1   | This bit is set when the input signal moves beneath the configured Low-Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |
| ChxHHAlarm Bit 0   | This bit is set when the input signal moves above the configured High-High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-IF6CIS or 1756-IF6I module in integer mode.

<!-- image -->

In integer mode, Module Fault word bits (bits 15-8) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-IF6CIS and 1756-IF6I Module Fault Word Bits – Integer Mode

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
|                    | Input Group Fault This bit is set when any bits in the Channel Fault word are set. Its tag name is InGroupFault.                                     |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

In integer mode, Channel Fault word bits operate exactly as described in floating point mode.

This table lists the conditions that set all Channel Fault word bits in integer mode.

## 1756-IF6CIS, 1756-IF6I Channel Fault Word Bits – Integer Mode

| Condition                                                                                               | Displays            |
|---------------------------------------------------------------------------------------------------------|---------------------|
| A channel is being calibrated                                                                           | ’003F’ for all bits |
| A communications fault that is occurred between the module and its owner-controller ’FFFF’ for all bits |                     |

Your logic can monitor the Channel Fault Word bit for a particular input to determine the state of that point.

The Channel Status word has the following differences when used in integer mode:

- The module only reports Underrange and Overrange conditions.
- Alarming and Calibration Fault activities aren't available, although the Calibration Fault bit in the Module Fault word activates if a channel isn't properly calibrated.
- There's only one Channel Status word for all six channels.

This table lists the conditions that set each of the word bits.

## 1756-IF6CIS, 1756-IF6I Channel Status Word Bits – Integer Mode

| Tag (Status Word) Bit   |                                                                                                                                         | Event That Sets This Tag                                                                                                                                                                                                                                                        |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxUnderrange           | Odd-numbered bits from bit 15…bit 5 (bit 15 represents channel 0). For a full listing of the channels these bits represent, page 156 .  | The underrange bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 141. This bit also sets the appropriate bit in the Channel Fault word.   |
| ChxOverrange            | Even-numbered bits from bit 14…bit 4 (bit 14 represents channel 0). For a full listing of the channels these bits represent, page 156 . | The overrange bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 141. This bit also sets the appropriate bit in the Channel Fault word. |

## 1756-OF6CI and 1756-OF6VI Module Features

This section describes features specific to ControlLogix isolated analog output modules that provide a high level of noise immunity. The 'C' and 'V' in the respective catalog numbers indicate 'current' and 'voltage'.

## Data Format Options

Data format defines the format of channel data that is sent from the controller to the module, defines the format of the 'data echo' that the module produces, and determines the features that are available to your application.

This table shows the features that are available in each format.

## Features Available in Each Data Format

| Data Format                      | Features Available                                                                                                       | Features Not Available                                  |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Integer mode                     | Ramp to program value Ramp to fault value Hold for initialization Hold Last State or User Value in fault or program mode | Clamping Ramp in Run mode Rate and Limit alarms Scaling |
| Floating point mode All features |                                                                                                                          | N/A                                                     |

## Ramping/Rate Limiting

Ramping limits the speed at which an analog output signal can change. This helps prevent fast transitions in the output from damaging the devices that an output module controls. Ramping is also known as rate limiting.

This table describes the types of ramping that are possible.

| Ramping Type Description   |                                                                                                                                                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run mode ramping           | This type of ramping occurs when the module is in Run mode and begins operation at the configured maximum ramp rate when the module receives a new output level. IMPORTANT: This is only available in floating point mode. |
| Ramp to Program mode       | This type of ramping occurs when the present output value changes to the Program value after a Program command is received from the controller.                                                                            |
| Ramp to Fault mode         | This type of ramping occurs when the present output value changes to the Fault value after a communications fault occurs.                                                                                                  |

The maximum rate of change in outputs is expressed in engineering units per second and called the maximum ramp rate.

## Hold for Initialization

Hold for Initialization causes outputs to hold their present state until the value the controller commands matches the value at the output screw terminal within 0.1% of full scale, providing a bumpless transfer.

If Hold for Initialization is selected, outputs hold if there's an occurrence of any of these three conditions.

- Initial connection is established after power-up.
- A new connection is established after a communications fault occurs.
- There's a transition to Run mode from Program state.

The InHold bit for a channel indicates that the channel is holding.

## Clamping/Limiting

Clamping limits the output from the analog module to remain within a range configured by the controller, even when the controller commands an output outside that range. This safety feature sets a high clamp and a low clamp.

Once clamps are determined for a module, any data that is received from the controller that exceeds those clamps sets an appropriate limit alarm and transitions the output to that limit but not beyond the requested value.

For example, if the high clamp that is configured for a module is 8V and the low clamp that is configured is -8V, and the controller sends a value of 9V to the module, the module will only apply 8V to its screw terminals.

Clamping alarms can be disabled or latched on a per channel basis.

## IMPORTANT

Clamping is only available in floating point mode.

Clamp values are in engineering scaling units and aren't automatically updated when the engineering high and low scaling units are changed. Failure to update the clamp values generates a small output signal that could be misinterpreted as a hardware problem.

## Clamp/Limit Alarms

This function works directly with clamping. When a module receives a data value from the controller that exceeds clamping limits, it applies signal values to the clamping limit and sends a status bit to the controller as notification that the value sent exceeds the clamping limits.

Using the previous example, if a module has clamping limits of 8V and -8V but then receives data to apply 9V, only 8V is applied to the screw terminals and the module sends a status bit back to the controller informing it that the 9V value exceeds the module's clamping limits.

## IMPORTANT

Limit alarms are available only in floating point mode.

## Data Echo

Data Echo automatically multicasts channel data values that match the analog value that was sent to the module's screw terminals.

Fault and status data is also sent. This data is sent in the format (floating point or integer) selected at the requested packet interval (RPI).

## User Count Conversion to Output Signal

User counts can be computed in Integer mode for the 1756-OF6CI and 1756-OF6VI modules.

The straight-line formulas that can be used to calculate or program a Compute (CPT) instruction are shown in this table.

| Available Range   | User Count Formula                                     |
|-------------------|--------------------------------------------------------|
| O…20 mA           | y = 3109.7560975609754x-32768 where y = counts; x = mA |
| +/-10V            | y = 3115.669867833032x-0.5 where y = counts; x = V     |

For example, if you have 3.5 mA in the 0…20 mV range, the user counts = -21884. Counts = 6231 for 2V in the +/-10V range.

For a table with related values, see Knowledgebase Technote, ControlLogix 1756-OF6CI User Count Conversion to Output Signal and ControlLogix 1756-OF6VI User Count Conversion to Output Signal .

## Module Block and Output Circuit Diagrams

This section details the 1756-OF6CI and 1756-OF6VI module block and output circuit diagrams.

<!-- image -->

<!-- image -->

## Field-side Circuit Diagrams

This diagram shows the field-side circuitry for the 1756-OF6CI module.

## 1756-OF6CI Output Circuit

<!-- image -->

Drive Different Loads with the 1756-OF6CI

The 1756-OF6CI module's output stage provides a constant current that flows through its internal electronics and out through the external output load. Because the output current is constant, the only variable in the current loop is the voltage across the output electronics and the voltage across the load. For a given termination option, the sum of the individual voltage drops around the loop components must add up to the total available voltage (13V for OUT-x/ RTN-x termination and 26V for OUT-x / ALT-x).

As seen in the previous diagram, a larger external output load drops a larger portion of the available loop voltage, allowing the module to drop fewer volts across its internal output electronics. This lower drop allows the power dissipation in the module to be lower, minimizing the thermal effect to adjacent modules in the same chassis.

For loads under 550 , the module's +13V internal voltage source can supply voltage for currents up to 21 mA. For loads over 550 , an additional compliance voltage is required. In this case, you must use the ALT terminal to provide the additional -13V source.

For any size load (that is, 0…1000 ), the output channels function if terminated between OUT-x and ALT-x. To improve module reliability and product life, we recommend you:

- Terminate the output channels between the OUT-x and RTN-x terminals for loads of 0…550 
- Terminate the output channels between the OUT-x and ALT-x terminals for loads of 551…1000  .

## IMPORTANT

If you're unsure of the load, you can terminate the output channels between OUT-x and ALT-x and the module operates but reliability can be compromised at elevated temperatures.

For example, if you terminate the output channels between OUT-x and ALT-x and use a 250 W load, the module operates but the lower load results in higher operating temperatures.

To maintain module reliability over time, we recommend you terminate the output channels as previously described whenever possible.

This diagram shows the field-side circuitry for the 1756-OF6VI module.

## 1756-OF6VI Output Circuit

<!-- image -->

## 1756-OF6CI Module Wiring

This illustration shows wiring examples for the 1756-OF6CI module.

## 1756-OF6CI Wiring Example for Loads of 0...550 

<!-- image -->

## Keep in mind the following:

- Place additional devices anywhere in the loop.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-OF6CI Wiring Example for Loads of 551-1000

<!-- image -->

## Keep in mind the following:

- Place additional devices anywhere in the loop.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-OF6VI Module Wiring

This illustration shows wiring examples for the 1756-OF6VI module.

## 1756-OF6VI Wiring example

<!-- image -->

## Keep in mind the following:

- Place additional devices anywhere in the loop.
- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## Module Fault Word (described on page 167)

- 15 = AnalogGroupFault
- 13 = OutGroupFault
- 12 = Calibrating
- 11 = Cal Fault
- 14 isn't used by the OF6CI or OF6VI

## Channel Fault Word (described on page 167)

- 5 = Ch5Fault
- 4 = Ch4Fault
- 3 = Ch3Fault
- 2 = Ch2Fault
- 1 = Ch1Fault
- 0 = Ch0Fault

Channel Status Words (one for each channel, described ion page 167)

- 5 = ChxNotANumber
- 4 = ChxCalFault
- 3 = ChxInHold
- 2 = ChxRampAlarm
- 1 = ChxLLimitAlarm
- 0 = ChxHLimitAlarm

## 1756-OF6CI and 1756-OF6VI Module Fault and Status Reporting

The 1756-OF6CI and 1756-OF6VI modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a manner as to let you choose the level of granularity that is desired for examining fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                                                        |
| Channel Fault Word   | This word provides underrange, overrange, and communications fault reporting. Its tag name is ChannelFaults.                                                       |
| Channel Status Words | This word provides individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults. Its tag name is ChxStatus. |

## IMPORTANT

Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.

Fault Reporting in Floating Point Mode

This illustration provides an overview of the fault reporting process for the 1756-OF6CI or 1756OF6VI module in floating point mode.

7 &amp; 6 aren't used by OF6CI or OF6VI

<!-- image -->

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-OF6CI, 1756-OF6VI Module Fault Word Bits – Floating Point Mode

| Tag         | Description                                                                                                             | Tag Name    |
|-------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
|             | Analog Group Fault This bit is set when any bits in the Channel Fault word are set. AnalogGroupFault                    |             |
|             | Output Group Fault This bit is set when any bits in the Channel Fault word are set. OutputGroupFault                    |             |
| Calibrating | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. | Calibrating |
|             | Calibration Fault This bit is set when any individual Channel Calibration Fault bits are set. CalFault                  |             |

During normal module operation, Channel Fault word bits are set if any of the respective channels has a High or Low Limit Alarm. A quick way to check for High or Low Limit Alarm condition on a channel is to check this word for a nonzero condition.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

## 1756-OF6CI, 1756-OF6VI Channel Fault Word Bits – Floating Point Mode

| Condition                                                                   | Display             |
|-----------------------------------------------------------------------------|---------------------|
| A channel is being calibrated                                               | ’003F’ for all bits |
| A communications fault occurred between the module and its owner-controller | ’FFFF’ for all bits |

Set your logic to monitor the Channel Fault bit for a particular output, if you either:

- set the high and low limit alarms outside your operating range.
- disable output limiting.

Any of the six Channel Status words, one for each channel, displays a nonzero condition if that particular channel has faulted for the conditions that are listed below. Some of these bits set bits in other Fault words.

When the High or Low Limit Alarm bits (bits 1 and 0) in any of the words are set, the appropriate bit is set in the Channel Fault word.

When the Calibration Fault bit (bit 4) is set in any of the words, the Calibration Fault bit (bit 11) is set in the Module Fault word.

This table lists the conditions that set each of the word bits.

## 1756-OF6CI, 1756-OF6VI Channel Status Word Bits – Floating Point Mode

|                      | Tag (Status word) Bit Event that sets this tag                                                                                                                                                                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxNotaNumber Bit 5  | This bit is set when the output value that is received from the controller is NotaNumber (the IEEE NAN value). The output channel holds its last state.                                                                                                                       |
| ChxCalFault Bit 4    | This bit is set when an error occurred when calibrating. This bit also sets the appropriate bit in the Channel Fault word.                                                                                                                                                    |
| ChxInHold Bit 3      | This bit is set when the output channel is holding. The bit resets when the requested Run mode output value is within 0.1% of the current full-scale echo value.                                                                                                              |
| ChxRampAlarm Bit 2   | This bit is set when the output channel’s requested rate of change would exceed the configured maximum ramp rate requested parameter. It remains set until the output reaches its target value and ramping stops. If the bit is latched, it remains set until it’s unlatched. |
| ChxLLimitAlarm Bit 1 | This bit is set when the requested output value is beneath the configured low limit value. It remains set until the requested output is above the low limit. If the bit is latched, it remains set until it’s unlatched.                                                      |
| ChxHLimitAlarm Bit 0 | This bit is set when the requested output value is above the configured high limit value. It remains set until the requested output is below the high limit. If the bit is latched, it remains set until it’s unlatched.                                                      |

IMPORTANT

The 1756-OF6CI and 1756-OF6VI modules do not use bits 6 or 7 in this mode.

## Module Fault Word (described on page 168)

15 = AnalogGroupFault 13 = OutGroupFault 12 = Calibrating 11 = Cal Fault 14 isn't used by the 1756OF6CI or 1756-OF6VI.

## Channel Fault Word (described on page 169)

5 = Ch5Fault

4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

1 = Ch1Fault

0 = Ch0Fault

Channel Status Word (described on page 169)

14 = Ch0InHold

12 = Ch1InHold

10 = Ch2InHold

8 = Ch3InHold

6 = Ch4InHold

4 = Ch5InHold

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-OF6CI or 1756OF6VI module in integer mode.

<!-- image -->

<!-- image -->

15, 13, 11, 9, 7, &amp; 5 aren't used by the 1756-OF6CI and 1756-OF6VI in integer mode.

Output in Hold conditions must be monitored here.

In integer mode, Module Fault word bits (bits 15…11) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-OF6CI, 1756-OF6VI Module Fault Word Bits – Integer Mode

| Tag                | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Output Group Fault | This bit is set when any bits in the Channel Fault word are set. Its tag name is OutputGroupFault.                                                   |
| Calibrating        | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault  | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |

In integer mode, Channel Fault word bits (bits 5…0) operate exactly as described in floating point mode for calibration and communications faults.

This table lists the conditions that set all Channel Fault word bits in integer mode.

## 1756-OF6CI, 1756-OF6VI Channel Fault Word Bits – Integer Mode

| Condition                                                                                       | Displays            |
|-------------------------------------------------------------------------------------------------|---------------------|
| A channel is being calibrated                                                                   | ’003F’ for all bits |
| A communications fault occurred between the module and its owner-controller ’FFFF’ for all bits |                     |

Set your logic to monitor the Channel Fault bit for a particular output, if you either:

- set the high and low limit alarms outside your operating range
- disable output limiting.

The Channel Status word has the following differences when used in integer mode.

- The module only reports the Output in Hold condition.
- Calibration Fault reporting isn't available in this word, although the Calibration Fault bit in the Module Fault word still activates when that condition exists on any channel.
- There's only one Channel Status word for all six channels.

This table lists the conditions that set each of the word bits.

## 1756-OF6CI, 1756-OF6VI Channel Status Word Bits in Integer Mode

| Tag (Status word) Bit   |                                                                                                                                                      | Event that sets this tag                                                                                                                                                                 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxInHold               | Even-numbered bits from bit 14…bit 4 (that is, bit 14 represents channel 0). For a full listing of the channels these bits represent, see page 168 . | The Output In Hold bit is set when the output channel is currently holding. The bit resets when the requested Run mode output value is within 0.1% of the current full-scale echo value. |

| IMPORTANT   | The 1756-OF6CI and 1756-OF6VI modules do not use bits 15, 13, 11, 9, 7, 5, 3, 2, 1, or 0 in this mode.   |
|-------------|----------------------------------------------------------------------------------------------------------|

## Calibrate 1756-IF6CIS and 1756-IF6I Modules

This section describes how to calibrate discontinued 1756-IF6CIS and 1756-IF6I ControlLogix analog I/O modules.

When you calibrate input modules, you use current, voltage, or ohms calibrators to send a signal to the module to calibrate it.

To maintain your module's accuracy specifications, we recommend you use calibration instruments with specific ranges, as listed in this table.

| Module      | Recommended Instrument Range                                              |
|-------------|---------------------------------------------------------------------------|
| 1756-IF6CIS | 1.00…20.00 mA source +/-0.15 µA current                                   |
| 1756-IF6I   | 0…10.00V source +/-150 µV voltage 1.00…20.00 mA source +/-0.15 µA current |

The 1756-IF6CIS module can be used for applications that require current only.

The 1756-IF6I module can be used for applications requiring voltage or current. Calibrate the modules for your specific application.

## Calibrating the 1756-IF6I for Voltage Applications

During 1756-IF6I module calibration, 0.0V and +10.0V external references are applied consecutively to the module's terminals. The module records the deviation from these reference values (that is, 0.0V and +10.0V) and stores it as calibration constants in the module's firmware. The internal calibration constants are then used in every subsequent signal conversion to compensate for circuit inaccuracies. The 0/10V user calibration compensates for all voltage ranges on the 1756-IF6I module (0-10V, +/-10V, and 0-5V) and compensates for inaccuracies of the module's entire analog circuitry, including the input amplifier, resistors, and the A/D converter.

The 1756-IF6I offers three input voltage ranges:

- -10…10V
- 0…5V
- 0…10V

## IMPORTANT

Regardless of what voltage application range is selected before calibration, all voltage calibration uses a +/-10V range.

## Calibrating the 1756-IF6CIS or 1756-IF6I for Current Applications

The 1756-IF6CIS and 1756-IF6I modules offer a 0…20 mA current range. Calibrating the modules for current uses the same process as calibrating the 1756-IF6I for voltage except the change in input signal.

Follow these steps to calibrate your module.

## IMPORTANT

The following examples show how you calibrate the 1756-IF6I module for voltage. Calibrating the modules for current uses the same process as calibrating the 1756-IF6I module for voltage except the change in input signal.

1. Connect your voltage calibrator to the module.
2. Go to the Configuration tab on the Module Properties dialog box.
3. At the Input Range, select the range from the pull-down menu to calibrate the channels.
4. Select OK.
5. Select the Calibration tab on the Module Properties dialog box.

<!-- image -->

<!-- image -->

6. Select Start Calibration to access the Calibration Wizard to step through the process. If your module is not in Program mode, a warning message appears. You must change

the module to Program mode before selecting Yes.

<!-- image -->

7. Set the channels to be calibrated.

<!-- image -->

<!-- image -->

You can select whether to calibrate channels in groups all at once or each channel at a time. The example above shows that all channels are set to calibrate simultaneously.

We recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

8. Select Next.

The Low Reference Voltage Signals wizard appears to show which channels are calibrated for a low reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

9. Select Next.

<!-- image -->

Select Back to return to the last window to make any necessary changes. Select Stop to halt the calibration process, if necessary.

10. Set the calibrator for the low reference and apply it to the module.

A Results wizard displays the status of each channel after calibrating for a low reference. If channels are OK, continue. If any channel reports an error, retry step 10 until the status is OK.

<!-- image -->

11. Set the calibrator for the high reference voltage and apply it to the module.

The High Reference Voltage Signals wizard appears to show which channels are calibrated for a high reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

12. Select Next.

A Results wizard displays the status of each channel after calibrating for a high reference. If all channels are OK, continue. If any channels report an error, retry step 11 until the status is OK.

<!-- image -->

After you have completed both low and high reference calibration, this window shows the status of both.

<!-- image -->

13. Select Finish.

The Calibration tab on the Module Properties dialog box shows the changes in the Calibration Gain and Calibration Offset, and the date of the latest calibration.

<!-- image -->

14. Select OK.

## Calibrate 1756-OF6VI and 1756-OF6CI Modules

This section describes how to calibrate a discontinued 1756-OF6VI and 1756-OF6CI ControlLogix analog I/O modules.

When you calibrate output modules, you use a digital multimeter (DMM) to measure the signal the module is sending out.

To maintain your module's accuracy specifications, we recommend you use calibration instruments with specific ranges, as listed in this table.

| Module     | Recommended Instrument Range           |
|------------|----------------------------------------|
| 1756-OF6VI | DMM with resolution better than 0.5 µV |
| 1756-OF6CI | DMM with resolution better than 1.0 µA |

Output calibration is a multi-step process that involves measuring a signal from the module. This section details both current and voltage meter calibrations.

The 1756-OF6CI module must be calibrated for current only, while the 1756-OF6VI module must be calibrated for voltage only.

## Current Meter Calibrations

RSLogix 5000® software commands the module to output specific levels of current. You must measure the actual level and record the results. This measurement allows the module to account for any inaccuracies.

While you are online, you must access the Module Properties dialog box.

Follow these steps to calibrate your module.

1. Connect your current meter to the module.
2. Select the Calibration tab on the Module Properties dialog box.
3. Select Start Calibration to access the Calibration Wizard to step through the process.

<!-- image -->

If your module is not in Program mode, a warning message appears. You must manually change the module to Program mode before selecting Yes.

<!-- image -->

4. Set the channels to be calibrated.

<!-- image -->

<!-- image -->

You can select whether to calibrate channels in groups all at once or each channel at a time.

We recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

5. Select Next.

The Output Reference Signals wizard appears to show which channels are calibrated for a low reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

6. Select Next.

<!-- image -->

Select Back to return to the last window to make any necessary changes. Select Stop to halt the calibration process, if necessary.

7. Record the results of your measurement.

<!-- image -->

A Results wizard displays the status of each channel after calibrating for a low reference. If channels are OK, continue. If any channel reports an error, retry steps 4 … 6 until the status is OK.

<!-- image -->

8. Select Next.
9. Set the channels to be calibrated for a high reference.

The Output Reference Signals wizard appears to show which channels are calibrated for a high reference and the range of the calibration. It also shows what reference signal is expected at the input.

10. Select Next.

<!-- image -->

11. Record the measurement.

<!-- image -->

## 12. Select Next.

A Results wizard displays the status of each channel after calibrating for a high reference. If channels are OK, continue. If any channels report an error, retry steps 9 … 12 until the status is OK.

<!-- image -->

After you have completed both low and high reference calibration, this window shows the status of both.

<!-- image -->

13. Select Finish.

The Calibration tab on the Module Properties dialog box shows the changes in the Calibration Gain and Calibration Offset, and the date of the latest calibration.

14. Select OK.

<!-- image -->

## Voltage Meter Calibrations

RSLogix 5000 software commands the module to output specific levels of voltage. You must measure the actual level and record the results. This measurement allows the module to account for any inaccuracies.

The 1756-OF4, 1756-OF4K, 1756-OF8, 1756-OF8K, and 1756-OF6VI modules use basically the same procedures for being calibrated by a voltage meter.

While you are online, you must access the Module Properties dialog box.

Follow these steps to calibrate your module.

1. Connect your voltage meter to the module.
2. Go to the Calibration tab on the Module Properties dialog box.

<!-- image -->

3. Select Start Calibration to access the Calibration Wizard to step through the process.

## IMPORTANT

The 'Error' status for all the channels denotes that the previous calibration process was not successful. We suggest a valid calibration be performed for all channels.

See page 185 for a successful calibration for channel 0.

If your module is not in Program mode, a warning message appears. You must manually change the module to Program mode before selecting Yes.

<!-- image -->

4. Set the channels to be calibrated.

<!-- image -->

<!-- image -->

You can select whether to calibrate channels in groups all at once or each channel at a time.

We recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

5. Select Next.

The Output Reference Signals wizard appears to show which channels are calibrated for a low reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

6. Select Next.

<!-- image -->

Select Back to return to the last window to make any necessary changes. Select Stop to halt the calibration process, if necessary.

7. Record the measurement.

<!-- image -->

8. Select Next.

A Results wizard displays the status of each channel after calibrating for a low reference. If channels are OK, continue. If any channel reports an error, retry steps 4 … 6 until the status is OK.

<!-- image -->

9. Select Next.
10. Set the channels to be calibrated for a high reference.

The Output Reference Signals wizard appears to show which channels are calibrated for a high reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

11. Select Next.

12. Record the measurement.
13. Select Next.

<!-- image -->

A Results wizard displays the status of each channel after calibrating for a high reference. If channels are OK, continue. If any channels report an error, retry steps 10 … 13 until the status is OK.

<!-- image -->

After you have completed both low and high reference calibration, this window shows the status of both.

<!-- image -->

14. Select Finish.

The Calibration tab on the Module Properties dialog box shows the changes in the Calibration Gain and Calibration Offset, and the date of the latest calibration.

<!-- image -->

15. Select OK.

## Notes:

## 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Features

<!-- image -->

## 6-channel Temperature-measuring Isolated Analog I/O Modules

This appendix offers reference information regarding the discontinued 6-channel 1756-IR6I, 1756-IT6I, and 1756-IT6I2 ControlLogix® temperature-measuring isolated analog I/O modules.

For information about how to migrate from 6-channel 1756 isolated analog I/O modules to newer 8-channel modules, see Migrating 6-Channel to 8-Channel 1756 Analog Modules , publication 1756-RM011 .

This section describes features specific to temperature-measuring ControlLogix analog modules. These units linearize their respective sensor inputs into a temperature value. The 1756-IR6I module uses ohms for temperature conversions and the two thermocouple modules (1756-IT6I and 1756-IT6I2) convert millivolts.

## Data Format Options

Data format determines how the data is returned from the module to the owner-controller and the features that are available to your application.

## Features Available in Each Data Format

| Data Format                      | Features Available:                                                                                                         | Features Not Available                                                 |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Integer mode                     | Multiple input ranges Notch filter Real-time sampling Cold junction temperature is on 1756-IT6I and 1756-IT6I2 modules only | Temperature linearization Process alarms Digital filtering Rate alarms |
| Floating point mode All features |                                                                                                                             | N/A                                                                    |

## IMPORTANT

Integer mode does not support temperature conversion on temperature-measuring modules. If you choose integer mode, the 1756-IR6I is strictly an ohms (W) module and the 1756-IT6I and 1756-IT6I2 are strictly millivolts (mV) modules.

## Multiple Input Ranges

You can select from a series of operational ranges for each channel on your module. The range designates the minimum and maximum signals that are detectable by the module.

## Possible Input Ranges

| Module                   | Range                              |
|--------------------------|------------------------------------|
| 1756-IR6I                | 1…487  2…1000  4…2000  8…4080  |
| 1756-IT6I and 1756-IT6I2 | -12…+78 mV -12…+30 mV              |

## Available Notch Filter Settings

| Notch Setting  10 Hz                                                 | 50 Hz                                                                   |       | 60 Hz (Default) 100 Hz 250 Hz 1000 Hz   |
|----------------------------------------------------------------------|-------------------------------------------------------------------------|-------|-----------------------------------------|
| Minimum Sample Time (RTS – Integer mode)( )(1)                                                                      | 102 ms 22 ms 19 ms                                                      | 12 ms | 10 ms  10 ms                            |
| Minimum Sample Time (RTS – Floating point mode)( )(2)                | 102 ms 25 ms 25 ms 25 ms 25 ms 25 ms                                    |       |                                         |
| 0…100% Step Response Time (3)                                        | 400 ms + RTS 80 ms + RTS 68 ms + RTS 40 ms + RTS 16 ms + RTS 4 ms + RTS |       |                                         |
| -3 dB Frequency 3 Hz 13 Hz 15 Hz 26 Hz 66 Hz 262 Hz                  |                                                                         |       |                                         |
| Effective Resolution 16 bits 16 bits 16 bits 16 bits 15 bits 10 bits |                                                                         |       |                                         |

(3) Worst case setting time to 100% of a step change would include 0…100% step response time plus one RTS sample time.

## Real-time Sampling

This parameter instructs the module to scan its input channels and obtain all available data. After the channels are scanned, the module multicasts that data.

During module configuration, you specify a real-time sampling (RTS) period and a requested packet interval (RPI) period. These features both instruct the module to multicast data, but only the RTS feature instructs the module to scan its channels before multicasting.

## Underrange/Overrange Detection

This feature detects when a temperature-measuring input module is operating beyond limits set by the input range. For example, if you're using the 1756-IR6I module in the 2…1000  input range and the module resistance increases to 1050 , the overrange detection detects this condition.

This table lists the input ranges of non-isolated input modules and the lowest/highest signal available in each range before the module detects an underrange/overrange condition.

## Low and High Signal Limits on Temperature-measuring Input Modules

|                          |          |                                   | Input Module Available Range Lowest Signal in Range Highest Signal in Range   |
|--------------------------|----------|-----------------------------------|-------------------------------------------------------------------------------|
| 1756-IR6I                | 1…487   | 0.859068653                      | 507.862                                                                      |
| 1756-IR6I                | 2…1000  | 2                                | 1016.502                                                                     |
| 1756-IR6I                | 4…2000  | 4                                | 2033.780                                                                     |
| 1756-IR6I                | 8…4020  | 8                                | 4068.392                                                                     |
| 1756-IT6I and 1756-IT6I2 |          | -12…+30 mV -15.80323 mV 31.396 mV |                                                                               |
| 1756-IT6I and 1756-IT6I2 |          | -12…+78 mV -15.15836 mV 79.241 mV |                                                                               |

## Notch Filter

An Analog-to-Digital Converter (ADC) filter removes line noise in your application for each channel.

Choose a notch filter that most closely matches the anticipated noise frequency in your application. Each filter time affects the response time of your module. Also, the highest frequency notch filter settings also limit the effective resolution of the channel.

IMPORTANT

60 Hz is the default setting for the notch filter.

Amplitude

## IMPORTANT

## Digital Filter

## IMPORTANT

The digital filter is available only in applications using floating point mode.

The digital filter smooths input data noise transients on each input channel. This value specifies the time constant for a digital first order lag filter on the input. It's specified in units of milliseconds. A value of 0 disables the filter.

The digital filter equation is a classic first order lag equation.

<!-- formula-not-decoded -->

Yn = present output, filtered peak voltage (PV)

Yn-1 = previous output, filtered PV

t = module channel update time (seconds)

TA = digital filter time constant (seconds)

Xn = present input, unfiltered PV

Using a step input change to illustrate the filter response, you can see that when the digital filter time constant elapses, 63.2% of the total response is reached. Each additional time constant achieves 63.2% of the remaining response.

<!-- image -->

Be careful when 'disabling all alarms' on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not 'disable all alarms'.

We recommend that you disable only unused channels so extraneous alarm bits aren't set.

## Process Alarms

Process alarms alert you when the module has exceeded configured high or low limits for each channel. You can latch process alarms. These are set at four user-configurable alarm trigger points.

- High high
- High
- Low
- Low low

## IMPORTANT

## Alarm Deadband

You can configure an alarm deadband to work with these alarms. The deadband allows the process alarm status bit to remain set, despite the disappearance of the alarm condition, as long as the input data remains within the deadband of the process alarm.

This illustration shows input data that sets each of the four alarms at some point during module operation. In this example, latching is disabled; therefore, each alarm turns Off when the condition that caused it to set ceases to exist.

<!-- image -->

Process alarms are available only in applications using floating point mode. The values for each limit are entered in scaled engineering units.

## Rate Alarm

| IMPORTANT   | You must use RSLogix 5000® software, version 12 or later, and module firmware revision 1.100 or later, to use the rate alarm for a non-ohm input on the 1756-IR6I module and a non-millivolt input on the 1756-IT6I and 1756-IT6I2 modules.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The rate alarm triggers if the rate of change between input samples for each channel exceeds the specified trigger point for that channel. This feature is available only in applications using floating point.

## EXAMPLE

## 10 Ohm Offset

With this feature, you can compensate for a small offset error in a 10  copper RTD. Values can range from -0.99…0.99  in units of

0.01 . For example, if the resistance of a copper RTD used with a channel is 9.74  at 25 o C, you would enter -0.26 in this field.

If you set a 1756-IT6I2 module (with normal scaling in Celsius) to a rate
° yg 
alarm of 100.1 °C/s, the rate alarm only triggers if the difference
° y gg
between measured input samples changes at a rate &gt; 100.1 °C/s.

If the module's RTS is 100 ms (that is, sampling new input data every 100
° pg py 
ms) and at time 0, the module measures 355 °C and at time 100 ms measures 363 °C, the rate of change is (363…355 °C) / (100 ms) = 80 °C/ s. The rate alarm wouldn't set as the change is less than the trigger
° point of 100.1 °C/s.

If the next sample taken is 350.3 °C, the rate of change is
°° pg
(350.3…363 °C)/(100 ms)=-127 °C/s. The absolute value of this result is &gt; 100.1 °C/s, so the rate alarm sets. Absolute value is used because the rate alarm checks for the magnitude of the rate of change being beyond the trigger point, whether a positive or negative excursion.

## Wire Off Conditions

|                                                            | In this application This causes a wire off condition                                                                                                                                            | And if the wire off condition is detected, this occurs                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-IR6I Module in Temperature Applications               | Either of the following: 1. When only the wire that is connected to terminal A is lost 2. When any other combination of wires is disconnected from the module See page 201 for a wiring diagram | If possibility number 1 (in the previous column) is the cause: • Input data for the channel changes to the highest scaled temperature value associated with the selected RTD type • The ChxOverrrange (x=channel number) tag is set to 1 If possibility number 2 (in the previous column) is the cause: • Input data for the channel changes to the lowest scaled temperature value associated with the selected RTD type. • The ChxUnderrange (x=channel number) tag is set to 1 |
| 1756-IR6I Module in Ohms Applications                      | Either of the following: 1. When only the wire that is connected to terminal A is lost 2. When any other combination of wires is disconnected from the module See page 201 for a wiring diagram | If possibility number 1 (in the previous column) is the cause: • Input data for the channel changes to the highest scaled ohm value associated with the selected ohms range • The ChxOverrange (x=channel number) tag is set to 1 If possibility number 2 (in the previous column) is the cause: • Input data for the channel changes to the lowest scaled ohm value associated with the selected ohms range • The ChxUnderrange (x=channel number) tag is set to 1               |
| 1756-IT6I or 1756-IT6I2 Module in Temperature Applications | A wire is disconnected from the module                                                                                                                                                          | • Input data for the channel changes to the highest scaled temperature value associated with the selected thermocouple type • The ChxOverrange (x=channel number) tag is set to 1                                                                                                                                                                                                                                                                                                 |
| 1756-IT6I Module or 1756-IT6I2 in Millivolt Applications   | A wire is disconnected from the module                                                                                                                                                          | • Input data for the channel changes to the scaled value associated with the overrange signal value of the selected operational range in floating point mode (maximum possible scaled value) or 32,767 counts in integer mode • The ChxOverrange (x=channel number) tag is set to 1                                                                                                                                                                                               |

## Wire Off Detection

The ControlLogix temperature-measuring modules alert you when a wire has been disconnected from one of their channels. When a wire off condition occurs, two events occur:

- Input data for that channel changes to a specific scaled value.
- A fault bit is set in the owner-controller that can indicate the presence of a wire off condition.

## IMPORTANT

Be careful when 'disabling all alarms' on the channel because it also disables the underrange/overrange detection feature. If alarms are disabled, overrange/underrange is zero and the only way you can discover a wire-off detection is from the input value itself. If you must detect a wire-off status, do not 'disable all alarms'.

We recommend that you disable only unused channels so extraneous alarm bits aren't set.

Because these modules can each be used in various applications, differences exist when a wire off condition is detected in each application. This table lists the differences that occur when a wire off condition occurs in various applications.

## Sensor Type

Three analog modules, the RTD (1756-IR6I) and Thermocouple modules (1756-IT6I and 1756IT6I2), let you configure a sensor type for each channel that linearizes the analog signal into a temperature value. The RTD module linearizes ohms into temperature and the Thermocouple modules linearize millivolts into temperature.

## IMPORTANT

Sensor type modules can only linearize signals to temperature values in the floating point mode.

## Available Sensors for Temperature Measuring Modules

| Module     | Available sensors or thermocouples                                                                                                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1756-IR6I  | 10  - Copper 427 type. 100  - Platinum 385, Platinum 3916, and Nickel 618 types. 120 - Nickel 618 and Nickel 672 types. 200 - Platinum 385, Platinum 3916, and Nickel 618 types. 500 - Platinum 385, Platinum 3916, and Nickel 618 types. 1000  - Platinum 385 and Platinum 3916 types. |
| 1756-IT6I  | B, E, J, K, R, S, T, N, C.                                                                                                                                                                                                                                                                       |
| 1756-IT6I2 | B, E, J, K, R, S, T, N, C, D, TXK/XK (L).                                                                                                                                                                                                                                                        |

When you select any of the sensor or thermocouple types during configuration, the programming software uses the default values in the scaling box.

## Default Signal and Engineering Values

| 1756-IR6I   | 1756-IT6I and 1756-IT6I2                                                        | 1756-IT6I and 1756-IT6I2   |
|-------------|---------------------------------------------------------------------------------|----------------------------|
|             | Low signal = 1 Low engineering = 1 Low signal = -12 Low engineering = -12       |                            |
|             | High signal = 487 High engineering = 487 High signal = 78 High engineering = 78 |                            |

## IMPORTANT

The module sends back temperature values over the entire sensor range as long as the low signal value equals the low engineering value and the high signal value equals the high engineering value. The actual numbers that are used in the signal and engineering fields are irrelevant as long as they're equal.

## Temperature Limits for 1756-IR6I Sensor Types

| 1756-IR6I Sensor   |                       |                     |                      |                       | Copper 427 Nickel 618 Nickel 672 Platinum 385 Platinum 3916   |
|--------------------|-----------------------|---------------------|----------------------|-----------------------|---------------------------------------------------------------|
| Low temperature    | -200.0 °C (-328.0 °F) | -60.0 °C (-76.0 °F) | -80.0 °C (-112.0 °F) | -200.0 °C (-328.0 °F) | -200.0 °C (-328.0 °F)                                         |
| High temperature   | 260.0 °C (500.0 °F)   | 250.0 °C (482.0 °F) | 320.0 °C (608.0 °F)  | 870.0 °C (1598.0 °F)  | 630.0 °C (1166.0 °F)                                          |

To see how to choose an RTD sensor type, see page 209 .

| IMPORTANT   | This table lists temperature limits for sensors using the -12…+78 mV range only. When the -12…+30 mV range is used, temperature limits are truncated to the temperature value that corresponds to 30 mV.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Temperature Limits for 1756-IT6I and 1756-IT6I2 Sensor Types

| Thermocouple B C E J K N R S T   |                       |                       |                       |                       |                       |                       |                       |                       |                       | D(1)              | TXK/XK (L)(1)     |
|----------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-------------------|-------------------|
| Low temperature                  | 300.0 °C (572.0 °F)   | 0.0 °C (32.0 °F)      | -270.0 °C (-454.0 °F) | -210.0 °C (-346.0 °F) | -270.0 °C (-454.0 °F) | -270.0 °C (-454.0 °F) | -50.0 °C (-58.0 °F)   | -50.0 °C (-58.0 °F)   | -270.0 °C (-454.0 °F) | 0 °C (32.0 °F)    | -200 °C (-328 °F) |
| High temperature                 | 1820.0 °C (3308.0 °F) | 2315.0 °C (4199.0 °F) | 1000.0 °C (1832.0 °F) | 1200.0 °C (2192.0 °F) | 1372.0 °C (2502.0 °F) | 1300.0 °C (2372.0 °F) | 1768.1 °C (3215.0 °F) | 1768.1 °C (3215.0 °F) | 400.0 °C (752.0 °F)   | 2320 °C (4208 °F) | 800 °C (1472 °F)  |

To see how to choose a thermocouple sensor type, see page 210 .

## Temperature Units

The 1756-IR6I, 1756-IT6I, and 1756-IT6I2 modules provide the choice of working in Celsius or Fahrenheit. This choice affects all channels per module.

To see how to choose temperature units, see page 209 .

## Input Signal to User Count Conversion

Integer mode does not support temperature conversion on temperature-measuring modules. However, the 1756-IT6I and 1756-IT6I2 modules can use this mode to calculate user counts for both available millivolt ranges.

The straight-line formulas that can be used to calculate or program a Compute (CPT) instruction are shown in this table.

|            | Available Range User Count Formula                                  |
|------------|---------------------------------------------------------------------|
| -12…+30 mV | y = 1388.4760408167676x-10825.593777483234 where y = counts; x = mV |
| 12…78 mV   | y = 694.2314015688241x-22244.5904917152 where y = counts; x = mV    |

For example, if you have 24 mV in the -12…+30 mV range, the user counts = 22498. Counts = 20856 for 2 mV in the 12…78 mV range.

For a table with related values, see Knowledgebase Technote, ControlLogix 1756-IT6I and 1756IT6I2 mV Input Signal to User Count Conversion .

## Wire Length Calculations

The rule for determining the maximum thermocouple lead length without error is that the lead length's error must be less than half of the module resolution. This error implies no error is observed nor is recalibration required.

The resolution for the 1756-IT6I and 1756-IT6I2 module, respectively, is:

```
-12…+30 mV range = 0.7 uV/bit
```

- -12…+78 mV range = 1.4 uV/bit

Based on the schematic on page 200, the module leakage per open-wire current is the bias voltage/pull-up resistance = 0.44V / 20 M= 22 nA. Hence, the maximum thermocouple loop resistance is the sum of total loop resistance = both leads.

Using this equation, for the -12…+30 mV range the maximum lead resistance is 16 for a maximum of half resolution error (1/2*(0.7uV/bit) / 22 nA).

For the -12…+78 mV range, the maximum lead resistance is 32 for a maximum of half resolution error (1/2*(1.4uV/bit) / 22 nA).

For more information, see Knowledgebase Technote, 1756-IT6I and 1756-IT6I2 Thermocouple Lead Length Calculations .

## Differences Between the 1756-IT6I and 1756-IT6I2 Modules

The 1756-IT6I and 1756-IT6I2 modules support grounded and ungrounded thermocouples. However, in addition to offering access to two more thermocouple types (D and TXK/XK [L]), the 1756-IT6I2 module offers the following:

- A greater cold junction compensation accuracy
- Improved module accuracy
- See page 198 for details.

While the 1756-IT6I module can report cold junction temperature differences between
°° j
channels as high as 3 °C (0.54 °F) from the actual temperature, the 1756-IT6I2 module, because it has two cold-junction sensors (CJS), reduces the potential cold-
°° j
junction error from the actual temperature to 0.3 °C (0.54 °F).

It's important that you check that the CJS is fitted locally or remotely, and enabled so in the module channel configuration. If the CJS isn't fitted or if the sensor wiring leads are incorrect (for example, swapped over at the thermocouple cards input), there's a possibility of a negative or positive temperature fluctuation when the thermocouple sensor is warmed.

This table lists the cold junction error from actual temperature, depending on the type of cold junction compensation that is used.

## Cold Junction Compensation Types

| If you use this module   | With this type of cold junction compensation                       | The cold junction error from actual temperature is   |
|--------------------------|--------------------------------------------------------------------|------------------------------------------------------|
|                          | 1756-IT6I2 Two cold-junction sensors on an RTB +/-0.3 °C (0.54 °F) |                                                      |
| 1756-IT6I2               | IFM                                                                | +/-0.3 °C (0.54 °F)                                  |
| 1756-IT6I                | One cold junction sensor on an RTB                                 | +/-3.2 °C (5.76 °F), max(1)                          |
| 1756-IT6I                | IFM                                                                | +/-0.3 °C (0.54 °F)                                  |

## Cold Junction Compensation

When using the thermocouple (1756-IT6I and 1756-IT6I2) modules, you must account for additional voltage that can alter the input signal. A small voltage generates at the junction of the thermocouple field wires and the screw terminations of an RTB or IFM. This thermoelectric effect alters the input signal.

To compensate the input signal from your module accurately, you must use a cold junction sensor (CJS) to account for the increased voltage. Because there are differences if you choose to connect sensors via an RTB or IFM, you must configure the module via the programming software to work with the type of CJS used in your application.

Connecting a Cold Junction Sensor Via a Removable Terminal Block

When you connect a CJS to your thermocouple module via an RTB, the following occurs, depending on module type:

- The 1756-IT6I module uses one CJS in the middle of the module and estimates the temperature deviation elsewhere on the connector.
- The 1756-IT6I2 module uses two CJSs at the top and bottom of the module and calculates the temperature at each channel's input terminals; this usage of multiple sensors results in increased accuracy.

If you connect a CJS via an RTB, configure the module as shown on the Module Properties Configuration tab.

Leave both boxes unselected.

<!-- image -->

See page 197 for how to connect a CJS to either thermocouple module.

Connecting a Cold Junction Sensor Via an Interface Module

The IFMs use an isothermal bar to maintain a steady temperature at all module terminations. When you use the IFM, we recommend you mount it so that the black anodized aluminum bar is in the horizontal position.

If you connect a CJS via an IFM, configure the module as shown on the Module Properties Configuration tab.

Select the Remote CJ Compensation box.

<!-- image -->

## Connecting a Cold Junction Sensor to the 1756-IT6I Module

You must connect the CJS to the 1756-IT6I module at terminals 10 and 14. To ease installation, wire terminal #12 (RTN-3) before connecting the cold junction sensor.

<!-- image -->

Contact your local distributor or Rockwell Automation sales representative to order additional sensors.

Connecting a Cold Junction Sensor to the 1756-IT6I2 Module

You must connect two CJSs to the 1756-IT6I2 module when using an RTB. The additional CJS offers greater accuracy when measuring the temperature on the module. Connect the cold junction sensors to terminals 3, 4, 17, 18 as shown.

<!-- image -->

Contact your local distributor or Rockwell Automation sales representative to order additional sensors.

## Cold Junction Disable Option

The Cold Junction Disable box on the Module Properties Configuration tab disables cold junction compensation on all module channels. Typically, this option is used only in systems that have no thermoelectric effect, such as test equipment in a controlled lab.

In most applications, we recommend that you do not use the cold junction disable option.

## Cold Junction Offset Option

The Cold Junction Offset box on the Module Properties Configuration Tab lets you make module-wide adjustments to cold junction compensation values. If you know that your cold
° jjyy
junction compensation values are consistently inaccurate by some level, for example, 1.2 °C 
° jpy y 
(2.16 °F), you can enter the value into the box to account for this inaccuracy.

## Improved Module Accuracy

The 1756-IT6I2 offers improved Gain Drift with Temperature and Module Error over Temperature Range specifications when compared to the 1756-IT6I module. This table highlights the differences.

| Cat. No.  Gain Drift with Temperature(1)   | Module Error over Temperature Range (1)   |
|--------------------------------------------|-------------------------------------------|
| 1756-IT6I 80 ppm                           | 0.5%                                      |
| 1756-IT6I2 25 ppm                          | 0.15%                                     |

For the latest I/O module specifications, see the 1756 ControlLogix I/O Modules Technical Specifications, publication 1756-TD002 .

## Module Block and Input Circuit Diagrams

This section shows the 1756-IR6I, 1756-IT6I, and 1756-IT6I2 modules' block diagrams and input circuit diagrams. This figure shows two channels. There are six channels on the temperaturemeasuring modules.

1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Block Diagram

<!-- image -->

= Channel Isolation

The cold junction compensation (CJC) channel is used on Thermocouple modules only. The 1756-IT6I module has one CJC channel, and the 1756-IT6I2 module has two CJC channels.

IMPORTANT

## Field-side Circuit Diagrams

These diagrams show field-side circuitry for the 1756-IR6I, 1756-IT6I, and 1756-IT6I2 modules.

## 1756-IR6I Input Circuit

<!-- image -->

## 1756-IT6I and 1756-IT6I2 Input Circuit

<!-- image -->

## 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Wiring

The illustrations in this section show wiring examples for the 1756-IR6I, 1756-IT6I, and 1756IT6I2 modules.

## 1756-IR6I 3-Wire RTD Wiring Example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

IMPORTANT

For two-wire resistor applications including calibration, make sure IN-x/B and RTN-x/C are shorted together as shown.

## 1756-IR6I 4-Wire RTD Wiring Example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.
- Wiring is the same as the 3-Wire RTD with one wire left open.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IT6I Wiring Example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

## 1756-IT6I2 Wiring Example

<!-- image -->

## Keep in mind the following:

- Do not connect more than two wires to any single terminal.

<!-- image -->

ATTENTION: If you use a separate power source, do not exceed the specific isolation voltage.

Module Fault Word

(described on page 206)

- 15 = AnalogGroupFault
- 14 = InGroupFault
- 12 = Calibrating
- 11 = Cal Fault
- 9 = CJUnderrange (IT6I only)
- 8 = CJOverrange (IT6I only)
- 13 and 10 aren't used by 1756-IR6I
- or 1756-IT6I

Channel Fault Word

(described on page 206)

- 5 = Ch5Fault
- 4 = Ch4Fault
- 3 = Ch3Fault
- 2 = Ch2Fault
- 1 = Ch1Fault
- 0 = Ch0Fault

Channel Status Words (one for each channel, described on page 206)

- 7 = ChxCalFault

- 6 = ChxUnderrange

- 5 = ChxOverrange

- 4 = ChxRateAlarm

- 3 = ChxLAlarm

- 2 = ChxHAlarm

- 1 = ChxLLAlarm

- 0 = ChxHHAlarm

## 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Fault and Status Reporting

The 1756-IR6I, 1756-IT6I, and 1756-IT6I2 modules multicast status and fault data to the owner and/or listening controller with its channel data. The fault data is arranged in such a manner as to let you choose the level of granularity that is desired for examining fault conditions.

Three levels of tags work together to provide an increasing degree of detail as to the specific cause of faults on the module.

This table lists tags that can be examined in ladder logic when a fault occurs.

| Tag                  | Description                                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Module Fault Word This word provides fault summary reporting. Its tag name is ModuleFaults.                                                                        |
| Channel Fault Word   | This word provides underrange, overrange, and communication fault reporting. Its tag name is ChannelFaults.                                                        |
| Channel Status Words | This word provides individual channel underrange and overrange fault reporting for process alarms, rate alarms, and calibration faults. Its tag name is ChxStatus. |

## IMPORTANT

Differences exist between floating point and integer modes as they relate to module fault reporting. These differences are explained in the following two sections.

Fault Reporting in Floating Point Mode

This illustration provides an overview of the fault reporting process for the 1756-IR6I, 1756-IT6I, or 1756-IT6I2 module in Floating Point mode.

<!-- image -->

Bits in this word provide the highest level of fault detection. A nonzero condition in this word reveals that a fault exists on the module.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Module Fault Word Bits – Floating Point Mode

| Tag                                                      | Description                                                                                                                                          |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault                                       | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Input Group Fault                                        | This bit is set when any bits in the Channel Fault word are set. Its tag name is InGroupFault.                                                       |
| Calibrating                                              | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault                                        | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |
| Cold Junction Underrange – 1756-IT6I and 1756-IT6I2 only | This bit is set when the ambient temperature around the cold junction sensor is below 0  o C. Its tag name is CJUnderrange.                          |
| Cold Junction Overrange – 1756-IT6I and 1756-IT6I2 only  | This bit is set when the ambient temperature around the cold junction sensor is above 86  o C. Its tag name is CJOverrange.                          |

During normal module operation, bits in the Channel Fault word are set if any of the respective channels has an Under or Overrange condition. A quick way to check for Under or Overrange conditions on the module is to check this word for a nonzero value.

This table lists the conditions that set all Channel Fault word bits in floating point mode.

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Channel Fault Word Bits – Floating Point Mode

| Condition                                                                                      | Display             |
|------------------------------------------------------------------------------------------------|---------------------|
| A channel is being calibrated                                                                  | “003F” for all bits |
| A communication fault occurred between the module and its owner-controller “FFFF” for all bits |                     |

Your logic can monitor the Channel Fault Word bit for a particular input to determine the state of that point.

Any of the six Channel Status words, one for each channel, display a nonzero condition if that particular channel has faulted for the conditions that are listed in the following table. Some of these bits set bits in other Fault words. When the Underrange and Overrange bits (bits 6 and 5) in any of the words are set, the appropriate bit is set in the Channel Fault word.

When the Calibration Fault bit (bit 7) is set in any of the words, the Calibration Fault bit (bit 11) is set in the Module Fault word.

This table lists the conditions that set each of the word bits.

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Channel Status Word Bits – Floating Point Mode

|                    | Tag (Status word) Bit Event that sets this tag                                                                                                                                                                                                                                                                                             |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxCalFault Bit 7  | This bit is set if an error occurs during calibration for that channel and causes a bad calibration. This bit also sets bit 11 in the Module Fault word.                                                                                                                                                                                   |
| Underrange Bit 6   | This bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 188. This bit also sets the appropriate bit in the Channel Fault word.                                                                        |
| Overrange Bit 5    | This bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 188. This bit also sets the appropriate bit in the Channel Fault word.                                                                     |
| ChxRateAlarm Bit 4 | This bit is set when the input channel’s rate of change exceeds the configured Rate Alarm parameter. It remains set until the rate of change drops below the configured rate. If latched, the alarm remains set until it’s unlatched.                                                                                                      |
| ChxLAlarm Bit 3    | This bit is set when the input signal moves beneath the configured Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband. |

## Module Fault Word (described on page 208)

15 = AnalogGroupFault

14 = InGroupFault

12 = Calibrating

11 = Cal Fault

- 9 and 8 = CJUnderOver

13 and 10 aren't used by 1756-

IR6I or IT6I

## Channel Fault Word (described on page 208)

5 = Ch5Fault

- 4 = Ch4Fault

3 = Ch3Fault

2 = Ch2Fault

- 1 = Ch1Fault
- 0 = Ch0Fault

## Channel Status Word (described on page 208)

15 = Ch0Underrange

14 = Ch0Overrange

13 = Ch1Underrange

12 = Ch1Overrange

11 = Ch2Underrange

10 = Ch2Overrange

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Channel Status Word Bits – Floating Point Mode

|                  | Tag (Status word) Bit Event that sets this tag                                                                                                                                                                                                                                                                                                     |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxHAlarm Bit 2  | This bit is set when the input signal moves above the configured High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains set as long as the signal remains within the configured deadband.          |
| ChxLLAlarm Bit 1 | This bit is set when the input signal moves beneath the configured Low-Low Alarm limit. It remains set until the signal moves above the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |
| ChxHHAlarm Bit 0 | This bit is set when the input signal moves above the configured High-High Alarm limit. It remains set until the signal moves below the configured trigger point. If latched, the alarm remains set until it’s unlatched. If a deadband is specified, the alarm also remains latched as long as the signal remains within the configured deadband. |

## Fault Reporting in Integer Mode

This illustration provides an overview of the fault reporting process for the 1756-IR6I, 1756-IT6I, or 1756-IT6I2 module in integer mode.

<!-- image -->

9 = Ch3Underrange

8 = Ch3Overrange

7 = Ch4Underrange

6 = Ch4Overrange

5 = Ch5Underrange

4 = Ch5Overrange

Underrange and overrange conditions set the corresponding Channel Fault word bit for that channel.

In integer mode, Module Fault word bits (bits 15…8) operate exactly as described in floating point mode.

This table lists tags that you can further examine in ladder logic to isolate the fault.

## 1756-IR6I, 1756-IT6I, and 1756-IT6I2 Module Fault Word Bits – Integer Mode

| Tag                                       | Description                                                                                                                                          |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Group Fault                        | This bit is set when any bits in the Channel Fault word are set. Its tag name is AnalogGroupFault.                                                   |
| Input Group Fault                         | This bit is set when any bits in the Channel Fault word are set. Its tag name is InGroupFault.                                                       |
| Calibrating                               | This bit is set when any channel is being calibrated. When this bit is set, all bits in the Channel Fault word are set. Its tag name is Calibrating. |
| Calibration Fault                         | This bit is set when any of the individual Channel Calibration Fault bits are set. Its tag name is CalFault.                                         |
| Cold Junction Underrange – 1756-IT6I only | This bit is set when the ambient temperature around the cold junction sensor is below 0  o C. Its tag name is CJUnderrange.                          |
| Cold Junction Overrange – 1756-IT6I only  | This bit is set when the ambient temperature around the cold junction sensor is above 86  o C. Its tag name is CJOverrange.                          |

In integer mode, Channel Fault word bits operate exactly as described in floating point mode.

This table lists the conditions that set all Channel Fault word bits in integer mode.

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Channel Fault Word Bits – Integer Mode

| Condition                                                                                        | Displays             |
|--------------------------------------------------------------------------------------------------|----------------------|
| A channel is being calibrated.                                                                   | “003F” for all bits. |
| A communication fault occurred between the module and its owner-controller. “FFFF” for all bits. |                      |

Your logic can monitor the Channel Fault Word bit for a particular input to determine the state of that point.

The Channel Status word has the following differences when used in integer mode:

- The module only reports Underrange and Overrange conditions.
- Alarming and Calibration Fault activities aren't available, although the Calibration Fault bit in the Module Fault word activates if a channel isn't properly calibrated.
- There's only one Channel Status word for all six channels.

This table lists the conditions that set each of the word bits.

## 1756-IR6I, 1756-IT6I, 1756-IT6I2 Channel Status Word Bits – Integer Mode

| Tag (Status word) Bit   |                                                                                                                                             | Event that sets this tag                                                                                                                                                                                                                                                        |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChxUnderrange           | Odd-numbered bits from bit 15…bit 5 (bit 15 represents channel 0). For a full listing of the channels these bits represent, see page 207 .  | The underrange bit is set when the input signal at the channel is less than or equal to the minimum detectable signal. For more information on the minimum detectable signal for each module, see page 188. This bit also sets the appropriate bit in the Channel Fault word.   |
| ChxOverrange            | Even-numbered bits from bit 14…bit 4 (bit 14 represents channel 0). For a full listing of the channels these bits represent, see page 207 . | The overrange bit is set when the input signal at the channel is greater than or equal to the maximum detectable signal. For more information on the maximum detectable signal for each module, see page 188. This bit also sets the appropriate bit in the Channel Fault word. |

## Configuring RTD and Thermocouple Modules

## Configure the RTD Module (1756-IR6I)

The Resistance Temperature Detector (RTD) module (1756-IR6I) has additional configurable points, temperature units, and 10  copper offset options.

All of the configuration options for this module match those of other 6-channel input modules, except for the Configuration Tab. The dialog box example and table show the additional settings for the temperature-measuring capability of the 1756-IR6I module.

<!-- image -->

1. Select from the additional options on the Configuration tab.
2. After the channels are configured, do one of the following:
- Select Apply to store a change but stay on the dialog box to select another tab.
- Select OK to apply the change and close the dialog box.
- Select Cancel to close the dialog box without applying changes.

|                                      | Field Name Description                                                                                                       |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|                                      | Sensor Type Select an RTD sensor type.                                                                                       |
| 10 Ohm Copper Offset                 | This feature must be set only if you select a Copper Sensor Type. Select a value to compensate for any copper offset errors. |
| Temperature Units Celsius Fahrenheit | Select the temperature unit that affects all channels per module.                                                            |

## Configure the Thermocouple Modules (1756-IT6I and 1756-IT6I2)

The 1756-IT6I and 1756-IT6I2 modules have additional configurable points, temperature units, and cold junction options.

All of the configuration options for this module match those of other 6-channel input modules, except for the Configuration Tab. The dialog box example and table show the additional settings for the temperature-measuring capability of the 1756-IT6I and 1756-IT6I2 modules.

<!-- image -->

1. Select from the additional options on the Configuration tab.

| Field Name                           | Description                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Sensor Type                          | Select a thermocouple sensor type.                                                                               |
| Cold Junction Offset                 | Select a value to compensate for the additional voltage that affects the input signal. See page 195 for details. |
|                                      | Cold Junction Disable Select the box to disable the cold junction.                                               |
|                                      | Remote CJ Compensation Select the box to enable cold junction compensation for a remote module.                  |
| Temperature Units Celsius Fahrenheit | Select the temperature unit that affects all channels per module.                                                |

## IMPORTANT

The module sends back temperature values over the entire sensor range as long as the High signal value equals the High engineering value and the Low signal value equals the Low engineering value.

Using the previous example, if:

High signal = 78.0 °C (172.4. °F), High engineering must = 78.0.

Low signal = -12.0 °C (10.4. °F), Low engineering must = -12.0

2. After the channels are configured, do one of the following:
- Select Apply to store a change but stay on the dialog box to select another tab.
- Select OK to apply the change and close the dialog box.
- Select Cancel to close the dialog box without applying changes.

## Calibrate 1756-IR61 Modules

This section describes how to calibrate discontinued 1756-IR6I ControlLogix analog I/O modules.

To maintain your module's accuracy specifications, we recommend you use calibration instruments with specific ranges, as listed in this table.

| Module    | Recommended Instrument Range      |
|-----------|-----------------------------------|
| 1756-IR6I | 1.0…487.0  resistors(1) +/-0.01% |

- (1) We suggest you use these precision resistors: KRL Electronics - 534A1-1R0T 1.0  0.01% / 534A1-487R0T 487  0.01%

A precision decade resistor box also can be used that meets or exceeds the required accuracy specifications. You are responsible for assuring that the decade box maintains accuracy by periodic calibration.

This module does not calibrate for voltage or current. It uses two precision resistors to calibrate the channels in ohms. You must connect a 1  precision resistor for low reference calibration and a 487  precision resistor for high reference calibration. The 1756-IR6I only calibrates in the 1…487  range.

## IMPORTANT

When you are wiring precision resistors for calibration, follow the wiring example on page 201. Make sure terminals IN-x/B and RTN-x/C are shorted together at the RTB.

While you are online, you must access the Calibration tab on the Module Properties dialog box.

Follow these steps to calibrate your module.

1. Go to the Calibration tab on the Module Properties dialog box.
2. Select Start Calibration to access the Calibration Wizard to step through the process.

<!-- image -->

## IMPORTANT

Regardless of what ohms application range is selected before calibration, the 1756-IR6I only calibrates in the 1…487 range.

3. Set the channels to be calibrated.

<!-- image -->

<!-- image -->

You can select whether to calibrate channels in groups all at once or each channel at a time. The example above shows that all channels are set to calibrate simultaneously.

We recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

4. Select Next.

The Low Reference Ohm Sources wizard appears to show which channels are calibrated for a low reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

5. Select Next.

<!-- image -->

Select Back to return to the last window to make any necessary changes. Select Stop to halt the calibration process, if necessary.

6. Connect a 1  resistor to each channel being calibrated.

A Results wizard displays the status of each channel after calibrating for a low reference. If channels are OK, continue. If any channel reports an error, retry step 6 until the status is OK.

<!-- image -->

7. Connect a 487  resistor to each channel being calibrated.

The High Reference Ohm Sources wizard appears to show which channels are calibrated for a high reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

8. Select Next.

A Results wizard displays the status of each channel after calibrating for a high reference. If channels are OK, continue. If any channels report an error, retry step 7 until the status is OK.

<!-- image -->

After you have completed both low and high reference calibration, this window shows the status of both.

<!-- image -->

9. Select Finish.

The Calibration tab on the Module Properties dialog box shows the changes in the Calibration Gain and Calibration Offset, and the date of the latest calibration.

10. Select OK.

<!-- image -->

## Calibrate 1756-IT6I and 1756-IT612 Modules

This section describes how to calibrate discontinued 1756-IT6I and 1756-IT6I2 ControlLogix analog I/O modules.

To maintain your module's accuracy specifications, we recommend you use calibration instruments with specific ranges, as listed in this table.

| Module     | Recommended Instrument Range   |
|------------|--------------------------------|
| 1756-IT6I  | -12 mV…78 mV source +/-0.3 µV  |
| 1756-IT6I2 | -12 mV…78 mV source +/-0.3 µV  |

This module only calibrates in millivolts. You can calibrate the module to either a -12…+30 mV range or -12…+78 mV range, depending upon your specific application.

## IMPORTANT

The following examples show a 1756-IT6I module being calibrated for a -12 mV…+78 mV range. You use the same steps to calibrate a 1756-IT6I2 module or to calibrate for a -12 mV…+30 mV range.

While you are online, you must access the Module Properties dialog box.

Follow these steps to calibrate your module.

1. Connect your voltage calibrator to the module.
2. Go to the Configuration tab on the Module Properties dialog box.
3. At the Input Range, select the range from the pull-down menu to calibrate the channels.
4. Select OK.

<!-- image -->

5. Select the Calibration Tab on the Module Properties dialog box.

<!-- image -->

## IMPORTANT

The 'Error' for channel 5 shows that, during the previous calibration, the process was not successful for this channel. We suggest a valid calibration be performed for all channels.

See page 219 for a successful calibration status.

6. Select Start Calibration to access the Calibration Wizard to step through the process. If your module is not in Program mode, a warning message appears. You must manually change the module to Program mode before selecting Yes.
7. Set the channels to be calibrated.

<!-- image -->

<!-- image -->

<!-- image -->

You can select whether to calibrate channels in groups all at once or each channel at a time. The previous example shows that all channels are set to calibrate simultaneously.

We recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

8. Select Next.

The Low Reference Voltage Signals wizard appears to show which channels are calibrated for a low reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

9. Select Next.

<!-- image -->

Select Back to return to the previous window to make any necessary changes. Select Stop to halt the calibration process, if necessary.

10. Set the calibrator for the low reference and apply it to the module.

A Results wizard displays the status of each channel after calibrating for a low reference. If all channels are OK, continue. If any channel reports an error, retry step 10 until the status is OK.

<!-- image -->

.

11. Set the calibrator for the high reference and apply it to the module.

The High Reference Voltage Signals wizard appears to show which channels are calibrated for a high reference and the range of the calibration. It also shows what reference signal is expected at the input.

<!-- image -->

## 12. Select Next.

A Results wizard displays the status of each channel after calibrating for a high reference. If all channels are OK, continue. If any channels report an error, retry step 11 until the status is OK.

<!-- image -->

After you have completed both low and high reference calibration, this window shows the status of both.

<!-- image -->

13. Select Finish.

The Calibration tab on the Module Properties dialog box shows the changes in the Calibration Gain and Calibration Offset, and the date of the latest calibration.

<!-- image -->

14. Select OK.

## RTD and Thermocouple Error Calculations

When you use the temperature-measuring modules (1756-IR6I, 1756-IT6I, and 1756-IT6I2), error calculations are achieved in a two-step process.

1. Calculate the module's error in ohms or volts.
2. Convert the ohm/volt error to temperature for the specific sensor and at the correct application temperature.

## RTD Error

Module error on the 1756-IR6I module is defined in ohms and is calculated across the entire input range that is selected, not the available range of a sensor used with the module. For example, if the 1…487  input range is used, the module error is calculated across 507  (actual range = 0.86…507.86 ).

The error in ohms translates to temperature, but that translation varies because the relationship is non-linear. The most effective way to check a 1756-IR6I module error is to calculate the error in ohms and use that value in a linearization table to check the temperature error.

If the module is calibrated at operating temperature and the operating temperature remains relatively stable, calibration accuracy is better than 0.1% of the full range for the first year after calibration. This 0.1% value is a worst case value. In other words, with the 1…487  input range that is selected, the worst case module error is 0.507  .

Finally, you must check an RTD linearization table to determine the temperature error to which an error of 0.507  translates. For example, if the 1756-IR6I has a 0.1% (or 0.507 ) error and is operating at 0 °C (32 °F), the temperature error is -1.25…1.2 °C (-2.25…2.16 °F) when the Platinum 385 sensor type is used. However, this same ohms error, when calculated in an
°° yp
operating temperature of 200 °C (392 °F), translates to a temperature error of
°°° g 
-1.4 °C…1.4 °C (-2.52…2.52 °F).

## Thermocouple Error

Thermocouple error at 25 °C (77 °F) indicates the module's accuracy in measuring temperature. This accuracy varies depending on these factors:

- Input range used, either:
- -12…+30 mV
- -12…+78 mV
- Thermocouple type, any of the following:
- B, R, S, E, J, K, N, T, L, or D (L and D types can be used with the 1756-IT6I2 only)
- Application temperature (that is, the temperature of the physical location where the thermocouple is being used).

## EXAMPLE

For example, when the 1756-IT6I module is operating in the following conditions:

- -12…+30 mV input range
- connected to a type S thermocouple
- ppp
the module error at 25 °C (77 °F) is +/-1.75 degrees.
- y
· application temperature of 1200 °C (2192 °F)
°°

In other words, the difference between the temperature the module reports and the actual application temperature can be +/- 1.75°.

The module can report an application temperature of 1200 °C (2192 °F) in this case when the actual temperature can be in the range from
°° 1196.26…1203.74 °C (2185.268…2198.732 °F).

| IMPORTANT   | When determining the thermocouple error, we used a typical error of 0.05% of the temperature range. The error calculations are listed for each range (that is, -12…+30 mV and -12…+78 mV) in the rest of this section.                                                   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | However, keep in mind that if cold junction compensation is performed on the thermocouple modules, the cold junction sensor error values must be added to the +/-1.75 degrees value in the previous example and the numbers that are listed in the rest of this section. |

## Module Error at 25 °C (77 °F) (-12…+30 mV Range)

This table lists the ControlLogix thermocouple modules' error at 25 °C (77 °F) when used in the -12…+30 mV input range.

## Thermocouple Module Error at 25 °C (77 °F)

| Application Temperature                                |      |      |    |
|--------------------------------------------------------|------|------|----|
| BRS  J(2) N(4)                                         | E(1) | K(3) | T  |
| -200 °C (-328 °F) 0.836 0.96 1.376 2.115 1.334         |      |      |    |
| 0 °C (32 °F) 0.358 0.42 0.532 0.803 0.542              |      |      |    |
| 200 °C (392 °F) 2.37 2.48 0.284 0.38 0.525 0.637 0.395 |      |      |    |
| 400 °C (752 °F) 2.02 2.19 0.262 0.38 0.497 0.566 0.340 |      |      |    |
| 600 °C (1112 °F) 3.53 1.85 2.06 0.494 0.539            |      |      |    |
| 800 °C (1472 °F) 2.75 1.71 1.93 0.535                  |      |      |    |
| 1000 °C (1832 °F) 2.30 1.59 1.82                       |      |      |    |
| 1200 °C (2192 °F) 2.03 1.51 1.75                       |      |      |    |
| 1400 °C (2552 °F) 1.86 1.49 1.73                       |      |      |    |
| 1600 °C (2919 °F) 1.80 1.51 1.77                       |      |      |    |
| 1800 °C (3272 °F) 1.83 1.71 2.04                       |      |      |    |

These illustrations depict the same information in graphic form.

## Thermocouple Module Error at 25 °C (77 °F) - Type B Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) ) - Type R Thermocouple Connection in a -12…+30 mV Input Range

Thermocouple Module Error at 25 °C (77 °F) - Type R Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type S Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type E Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type J Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type K Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type N Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type T Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

## Module Error at 25 °C (77 °F) ( (-12…+78 mV Range)

This table lists the ControlLogix thermocouple modules' error at 25 °C (77 °F) when used in the -12…+78 mV input range.

| Application Temperature                                 |                                        |                                        |
|---------------------------------------------------------|----------------------------------------|----------------------------------------|
| Application Temperature                                 | BRSEJKNT                               |                                        |
| -200 °C (-328 °F) 1.791 2.06 2.949 4.532 2.859          |                                        |                                        |
| 0 °C (32 °F) 0.767 0.89 1.141 1.720 1.161               |                                        |                                        |
| 200 °C (392 °F)                                         |                                        | 5.09 5.32 0.608 0.81 1.126 1.364 0.847 |
| 400 °C (752 °F)                                         | 4.34 4.70 0.562 0.82 1.065 1.212 0.728 |                                        |
| 600 °C (1112 °F) 7.56 3.96 4.41 0.558 0.77 1.059 1.155  |                                        |                                        |
| 800 °C (1472 °F) 5.89 3.65 4.14 0.574 0.70 1.098 1.146  |                                        |                                        |
| 1000 °C (1832 °F) 4.93 3.40 3.90 0.599 0.76 1.154 1.165 |                                        |                                        |
| 1200 °C (2192 °F) 4.35 3.23 3.74                        | 0.79 1.233 1.210                       |                                        |
| 1400 °C (2552 °F) 3.99 3.18 3.71                        | 1.328                                  |                                        |
| 1600 °C (2912 °F) 3.85 3.24 3.80                        |                                        |                                        |
| 1800 °C (3272 °F) 3.92 3.67 4.36                        |                                        |                                        |

These illustrations depict the same information in graphic form.

Thermocouple Module Error at 25 °C (77 °F) - Type B Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type R Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type R Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type E Thermocouple Connection in a -12…+78 mV Input Range

Thermocouple Module Error at 25 °C (77 °F) - Type J Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Module Error (+/-)

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type K Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type N Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Error at 25 °C (77 °F) - Type T Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

## Thermocouple Resolution

Thermocouple resolution indicates the degrees that an application temperature must change before the ControlLogix thermocouple module reports a change. Resolution varies depending on these factors.

- Input range used, either:
- -12…+30 mV
- -12…+78 mV
- Thermocouple type, any of the following:
- B, R, S, E, J, K, N, T, L, and D (L and D are used on the 1756-IT6I2 module only)
- Application temperature that is, the temperature of the physical location where the thermocouple is being used

## EXAMPLE

For example, when the 1756-IT6I module is operating in the following conditions:

- -12…+30 mV input range
- connected to a type K thermocouple
- ypp
· application temperature of 400 °C (752 °F) the resolution is 0.017 degrees.

In other words, the application temperature must change by 0.017 degrees or greater for the 1756-IT6I module to record a change. If the
° gg
temperature stays in a range from 399.984…400.0169 °C
° pyg
(751.971…752.030 °F), the module continues to report an application 
°°

temperature of 400 °C (752 °F).

## Module Resolution (-12…+30 mV Range)

This table lists the resolution of ControlLogix thermocouple modules when used in the -12…+30 mV input range.

| Application Temperature                                      |                                         |                                         |                               |
|--------------------------------------------------------------|-----------------------------------------|-----------------------------------------|-------------------------------|
| BRS                                                          | E(1) J(2)                               | N(4)                                    | K(3) T                        |
| -200 °C (-328 °F)                                            |                                         |                                         | 0.028 0.032 0.046 0.071 0.044 |
| 0 °C (32 °F)                                                 |                                         | 0.13 0.13 0.012 0.014 0.018 0.027 0.018 |                               |
| 200 °C (392 °F)                                              | 0.08 0.08 0.009 0.013 0.018 0.021 0.013 |                                         |                               |
| 400 °C (752 °F) 0.17 0.07 0.07 0.009 0.013 0.017 0.019 0.011 |                                         |                                         |                               |
| 600 °C (1112 °F) 0.12 0.06 0.07                              |                                         | 0.016 0.02                              |                               |
| 800 °C (1472 °F) 0.09 0.06 0.06                              |                                         | 0.02                                    |                               |
| 1000 °C (1832 °F) 0.08 0.05 0.06                             |                                         |                                         |                               |
| 1200 °C (2192 °F) 0.07 0.05 0.06                             |                                         |                                         |                               |
| 1400 °C (2552 °F) 0.06 0.05 0.06                             |                                         |                                         |                               |
| 1600 °C (2919 °F) 0.06 0.05 0.06                             |                                         |                                         |                               |
| 1800 °C (3272 °F) 0.06 0.06 0.07                             |                                         |                                         |                               |

These illustrations depict the same information in graphic form.

Thermocouple Module Resolution - Type B Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type R Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type S Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

<!-- image -->

Thermocouple Module Resolution - Type J Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type K Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type N Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type T Thermocouple Connection in a -12…+30 mV Input Range

<!-- image -->

## Module Resolution (-12…+78 mV Range)

This table lists the resolution of ControlLogix thermocouple modules when used in the -12…+78 mV input range.

| Application Temperature                                      |                                         |
|--------------------------------------------------------------|-----------------------------------------|
| Application Temperature                                      | BRSEJKNT                                |
| -200 °C (-328 °F) 0.056 0.064 0.046 0.141 0.089              |                                         |
| 0 °C (32 °F) 0.26 0.26 0.024 0.028 0.092 0.054 0.036         |                                         |
| 200 °C (392 °F)                                              | 0.16 0.17 0.019 0.025 0.035 0.042 0.026 |
| 400 °C (752 °F) 0.28 0.14 0.15 0.017 0.025 0.035 0.038 0.023 |                                         |
| 600 °C (1112 °F) 0.23 0.12 0.14 0.017 0.024 0.033 0.04       |                                         |
| 800 °C (1472 °F) 0.18 0.11 0.13 0.018 0.022 0.033 0.04       |                                         |
| 1000 °C (1832 °F) 0.15 0.11 0.12 0.019 0.024 0.034 0.04      |                                         |
| 1200 °C (2192 °F) 0.14 0.10 0.12                             | 0.024 0.036 0.04                        |
| 1400 °C (2552 °F) 0.12 0.10 0.12                             | 0.038                                   |
| 1600 °C (2912 °F) 0.12 0.10 0.12                             |                                         |
| 1800 °C (3272 °F) 0.12 0.11 0.14                             |                                         |

These illustrations depict the same information in graphic form.

Thermocouple Module Resolution - Type B Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type R Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

<!-- image -->

Application Temperature in °C
Application Temperature in C

## Thermocouple Module Resolution - Type N Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

Thermocouple Module Resolution - Type T Thermocouple Connection in a -12…+78 mV Input Range

<!-- image -->

## Dealing with Incorrect Thermocouple Temperature Readings

The first thought when an incorrect temperature reading is reported back in a thermocouple input module is that the module is out of calibration. This is typically not the case, particularly if the module has just been installed out-of-the-box.

All thermocouple input modules are shipped factory-calibrated so it is unlikely that they would need to be calibrated upon installation.

To determine the cause of the incorrect reading, the nature of the incorrect reading must be discerned first. The module:

1. Always reads maximum.
2. Always reads minimum.
3. Reads erratic (data jumping around).
4. Reads with an offset over the entire range.

In general, if incorrect readings appear on a new install then checking for proper installation and configuration would typically prevail as a cause versus an existing working module where a hardware failure of some type (channel or module) would be more likely the cause.

Also, if multiple channels are experiencing these symptoms, disconnect all thermocouples except one. This can help determine if it is external hardware or the module itself is the cause.

Before attempting to troubleshoot these symptoms, a great deal of work can be saved by first, visually inspecting the module, and second, applying a thermocouple emulator directly to the module input in question. Make sure that the module is powered and communicating based on the status indicators. Red or flashing green status indicators signify a problem.

Make sure that the wiring is intact and correct and the cold junction sensors (CJS) are installed correctly for the correct wiring arm, terminal base, or removable terminal block. If all looks correct, then remove the thermocouple from the channel in question and apply the emulator.

The emulator is designed to provide a voltage at the terminals equivalent to the voltage expected for the thermocouple type it is emulating. If the temperature reports back correctly, then the module is performing as expected and the thermocouple and wiring are suspect. If the emulator temperature is not reporting back correctly, then the module hardware, configuration, or the software application are suspect.

We highly recommend using a thermocouple emulator for initial troubleshooting. In lieu of an emulator, a millivolt signal can be applied to the input. To make this work, the module would have to be reconfigured to read a millivolt signal. If the module is reading back the millivolt correctly, then the module is performing as expected.

## Troubleshooting Checklist

Check for these symptoms when troubleshooting a module.

1. Thermocouple reading maximum (upscale) usually means that there is an open circuit. Thermocouple modules provide open-circuit detection and the data reports back upscale when an open circuit is detected. Check the wiring, terminations, and for an open thermocouple. Make sure that the length of the thermocouple cable is within module specifications, where too long a length, thus a higher impedance, could be interpreted as an open circuit.
2. Thermocouple reading minimum (downscale) usually means that there is a shortcircuited input. Check wiring and correct terminations.
3. Erratic readings (data jumping around) are a symptom of noise. The magnitude of noise can be seen with an oscilloscope. Disconnect all but one thermocouple to see if other channels are affecting each other (bleed-over). The effect of noise can be reduced by removing or suppressing the source of the noise or by employing the hardware and or software filters that are provided by the thermocouple module.
4. Offset readings can be caused by a DC signal riding on top of the thermocouple signal. The magnitude of the offset can be seen with an oscilloscope. Again, by disconnecting all but one thermocouple, one can see if other channels are affecting each other (bleedover).
5. Make sure that the module is not in calibration mode. This is module-dependent, but in general, specific bits have to be turned on to enable calibration.

The 1756-IT6I Thermocouple module, when configured with all channels for the same configuration and measuring the same (ambient) temperature, has a temperature reading difference between upper and lower channels up to

- -13.33…-12.22 °C (8…10 °F). To improve the accuracy of the module's reading, we recommend that you select remote CJ compensation and wire to a 1492-AIFM6TC-3.

Offset readings can also be seen if the CJS is defective or not installed properly. When, provided, check the module input data for a CJS defective diagnostic bit. Thermocouples also report back ambient temperature and provide an accurate ambient temperature if the CJS is healthy, wired properly, and the module is operating within specifications.

## Using RSNetWorx and RSLogix 5000 Software

<!-- image -->

## Remote Connections Via a ControlNet Network

This appendix offers reference information regarding connecting with ControlLogix® analog I/ O modules in a remote chassis via a ControlNet® network.

For more information about ControlLogix ControlNet modules, see the ControlNet Network Configuration User Manual, publication CNET-UM001 .

For information about how to migrate from a ControlNet network to an EtherNet/IP™ network, see the ControlNet to EtherNet/IP Migration Reference Manual, publication CNET-IN005 .

The I/O configuration portion of the RSLogix 5000® programming software generates the configuration data for each I/O module in the control system, whether the module is in a local or remote chassis. A remote chassis, also known as networked, contains the I/O module but not the module's owner-controller. A remote chassis can be connected to the controller via a scheduled connection on the ControlNet network or an EtherNet/IP network.

RSLogix 5000 configuration data is transferred to the controller during the program download and later transferred to the appropriate I/O modules. I/O modules in the local chassis, and modules in a remote chassis connected via the EtherNet/IP network, or unscheduled connections on the ControlNet network, are ready to run as soon as the configuration data has been downloaded. However, to enable scheduled connections to I/O modules on the ControlNet network, you must schedule the network by using RSNetWorx for ControlNet software.

Running RSNetWorx™ software transfers configuration data to I/O modules on a scheduled ControlNet network and establishes a network update time (NUT) for the ControlNet network that is compliant with the desired communication options specified for each module during configuration.

Anytime a controller references a scheduled connection to I/O modules on a scheduled ControlNet network, you must run RSNetWorx software to configure the ControlNet network.

See the following general steps when configuring I/O modules.

1. Configure all I/O modules for a given controller by using RSLogix 5000 programming software and download that information to the controller.
2. If the I/O configuration data references a scheduled connection to a module in a remote chassis that is connected via the ControlNet network, run RSNetWorx for ControlNet software to schedule the network.
3. After running RSNetWorx software, perform an online save of the RSLogix 5000 project so the configuration information that RSNetWorx software sends to the controller is saved.

## IMPORTANT

You must run RSNetWorx for ControlNet software whenever a new I/O module is added to a scheduled ControlNet chassis. When a module is permanently removed from a remote chassis, we recommend that you run RSNetWorx for ControlNet software to reschedule the network and optimize the allocation of network bandwidth.

## Remote Input Modules Connected Via a ControlNet Network

When remote analog I/O modules are connected to the owner-controller via a scheduled ControlNet network, the RPI and RTS intervals still define when the module multicasts data within its own chassis (as described in the previous section). However, only the value of the RPI determines how often the owner-controller receives it over the network.

When an RPI value is specified for an input module in a remote chassis that is connected by a scheduled ControlNet network, the RPI also 'reserves' a spot and instructs the module to multicast data within its own chassis.

Whether the timing of this 'reserved' spot coincides with the exact value of the RPI, the control system helps the owner-controller receive data at least as often as the specified RPI.

This illustration shows that the input data within the remote chassis is multicast at the configured RPI. The ControlNet bridge module sends input data back to the owner-controller at least as often as the RPI.

<!-- image -->

The 'reserved' spot on the network and the module's RTS are asynchronous to each other. This means that there are best and worst Case scenarios as to when the owner-controller receives updated channel data from the module in a networked chassis.

## Best Case RTS Scenario

In the best case scenario, the module performs an RTS multicast with updated channel data just before the 'reserved' network slot is made available. In this case, the remotely located owner-controller receives the data almost immediately.

## Worst Case RTS Scenario

In the worst case scenario, the module performs an RTS multicast just after the 'reserved' network slot has passed. In this case, the owner-controller does not receive data until the next scheduled network slot.

<!-- image -->

Because it's the RPI and not the RTS that dictates when the module's data is sent over the network, we recommend that the RPI value is set less than or equal to the RTS to make sure that the owner-controller receives updated channel data with each receipt of data.

## Remote Output Modules Connected Via a ControlNet Network

When remote analog output modules are connected to the owner-controller via a scheduled ControlNet network, and are instructing the controller to multicast the output data within its own chassis, the RPI also 'reserves' a spot in the stream of data flowing across the ControlNet network.

Whether the timing of this 'reserved' spot coincides with the exact value of the RPI, the control system helps the output module receive data at least as often as the specified RPI.

<!-- image -->

The 'reserved' spot on the network and when the controller sends the output data are asynchronous to each other. This means that there are best and worst case scenarios as to when the module receives the output data from the controller in a networked chassis.

## Best Case RPI Scenario

In the best case scenario, the controller sends the output data just before the 'reserved' network slot is available. In this case, the remote output module receives the data almost immediately.

## Worst Case RPI Scenario

In the worst case scenario, the controller sends the data just after the 'reserved' network slot has passed. In this case, the module does not receive the data until the next scheduled network slot.

## IMPORTANT

These best and worst case scenarios indicate the time that is required for output data to transfer from the controller to the module once the controller has produced it.

The scenarios do not take into account when the module receives new data (updated by the user program) from the controller. That is a function of the length of the user program and its asynchronous relationship with the RPI.

## Notes:

<!-- image -->

analog interface module (AIFM)

Modules connect to pre-wired cables to provide the output terminal blocks for the analog I/O module. These modules can be mounted on a DIN rail.

broadcast

Data transmissions to all addresses or functions.

communication format

Format that defines the type of information transferred between an I/O module and its owner- controller. This format also defines the tags created for each I/O module.

compatible match An electronic keying protection mode that requires that the physical module and the module configured in the software to match according to vendor and catalog number. In this case, the minor revision of the module must be greater than or equal to that of the configured slot.

connection

The communication mechanism from the controller to another module in the control system.

coordinated system time (CST) Timer value that is kept synchronized for all modules within a single ControlBus chassis.

direct connection

An I/O connection where the controller establishes an individual connection with I/O modules.

disable keying An electronic keying protection mode that requires no attributes of the physical module and the module configured in the software to match.

download

The process of transferring the contents of a project on the workstation into the controller.

electronic keying A feature where modules can be requested to perform an electronic check to make sure that the physical module is consistent with what was configured by the software.

exact match

An electronic keying protection mode that requires the physical module and the module configured in the software to match according to vendor, catalog number, major revision and minor revision.

field side

Interface between user field wiring and I/O module.

inhibit

A ControlLogix® process that lets you configure an I/O module but prevent it from communicating with the owner-controller. In this case, the controller behaves as if the I/O module does not exist at all.

interface module (IFM) A module that uses pre-wired cable to connect wiring to an I/O module.

listen-only connection An I/O connection where another controller owns/provides the configuration and data for the module.

major revision A module revision that is updated any time there is a functional change to the module.

minor revision

A module revision that is updated any time there is a change to the module that does not affect its function or interface.

multicast

Data transmissions that reach a specific group of one or more destinations.

multiple owners A configuration set-up where multiple owner-controllers use exactly the same configuration information to simultaneously own an input module.

network update time (NUT) The smallest repetitive time interval in which the data can be sent on a ControlNet® network. The NUT ranges from 2 ms to 100 ms.

owner-controller

The controller that creates and stores the primary configuration and communication connection to a module.

Program mode

In this mode the following events occur:

- Controller program is not executing.

- Inputs are still actively producing data.

- Outputs are not actively controlled and go to their configured Program mode.

rack connection

An I/O connection where the 1756-CNB module collects digital I/O words into a rack image to conserve ControlNet connections and bandwidth.

rack optimization

A communication format in which the 1756-CNB module collects all digital I/O words in the remote chassis and sends them to controller as a single rack image.

remote connection

An I/O connection where the controller establishes an individual connection with I/O modules in a remote chassis.

removal and insertion under power (RIUP)

ControlLogix feature that allows a user to install or remove a module or RTB while power is

applied.

removable terminal block (RTB)

Field wiring connector for I/O modules.

requested packet interval (RPI)

The maximum amount of time between broadcasts of I/O data.

Run mode

In this mode, the following events occur:

- Controller program is executing

- Inputs are actively producing data

- Outputs are actively controlled

service

A system feature that is performed on user demand, such as fuse reset or diagnostic latch reset.

system side

Backplane side of the interface to the I/O module.

tag

A named area of the controller’s memory where data is stored.

timestamping A ControlLogix process that stamps a change in input data with a relative time reference of when that change occurred.

## Numerics

## 10 Ohm offset

1756-IR6I, 1756-IT6I, and 1756-IT6I2 module 191

## A

## agency

certification 11

alarm deadband 36 , 143 , 190

alarms 87

latching 27

limit alarm 63 , 159

process alarm 36 , 143 , 190

rate alarm 37 , 144 , 191

## analog I/O 11

## C

## calibration

1756-IF6CIS and 1756-IF6I modules 170 , 176

1756-IF8 module 89

1756-OF8 module 89

using RSLogix 5000 103

## certification

agency 11

## channel fault word

1756-IF16 module 51

1756-IF6CIS and 1756-IF6I modules 154

1756-IF8 module 56

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules

1756-OF4 and 1756-OF8 modules 69

1756-OF6CI and 1756-OF6VI modules 166

floating point mode 52 , 53 integer mode 54 , 55 floating point mode 154 , 156 floating point mode 57 integer mode 59 205 floating point mode 205 integer mode 207 floating point mode 69 , 70 integer mode 72 , 73 floating point mode 166 integer mode 168

## channel status word

1756-IF16 module 51

floating point mode 52 integer mode 54 , 55 1756-IF6CIS and 1756-IF6I modules 154 floating point mode 154 , 156 1756-IF8 module 56 floating point mode 57 integer mode 59 1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 205 floating point mode 205 integer mode 207 1756-OF4 and 1756-OF8 modules 69 floating point mode 69 , 71 integer mode 72 , 73

1756-OF6CI and 1756-OF6VI modules 166

## clamping

1756-OF4 and 1756-OF8 modules 62 , 159 as related to limit alarms 63 , 159

## cold junction compensation

1756-IT6I and 1756-IT6I2 modules 195 - 198

cold junction disable 197 cold junction offset 198 connecting a sensor to the 1756-IT6I module 197 connecting a sensor to the 1756-IT6I2 module 197 using an IFM 196 using an RTB 196

## communication format

output modules 80

## configuration 75

configuring modules in remote chassis 92

downloading data 89

## connections

direct connections 17 input data connections 78 listen-only connections 22 module inhibiting 82

ControlNet network 236 , 237

## coordinated system time (CST) 11

rolling timestamp 26

timestamp 26

## D

## DAC

See digital to analog converter data echo 63 , 159

data format 11 , 28

as related to module resolution and scaling

30

floating point mode 28

integer mode 28

## differential wiring method

1756-IF16 and 1756-IF8 modules 33 high speed mode 33

## digital filter

1756-IF16 and 1756-IF8 modules 35 1756-IF6CIS and 1756-IF6I modules 142 1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 189

digital to analog converter 26

direct connections 17

downloading configuration data 89

driving loads on the 1756-OF6CI module 162

## E

electronic keying 77

electrostatic discharge preventing 15

event tasks 20

floating point mode 166 168

integer mode

## F

## fault and status reporting

1756-IF16 module 51

1756-IF6CIS and 1756-IF6I modules 154

1756-IF8 module 56

1756-OF4 and 1756-OF8 modules 69

1756-OF6CI and 1756-OF6VI modules 166

## H

## hold for initialization

1756-OF4 and 1756-OF8 modules 62

1756-OF6CI and 1756-OF6VI modules 158

## I

## inhibiting the module

in RSLogix 5000 28

## input circuit diagram

1756-IF16 and 1756-IF8 current 41

1756-IF16 and 1756-IF8 voltage 41

1756-IF6CIS module 147

1756-IF6I module 147

## input ranges

1756-IF16 &amp; 1756-IF8 modules 34

1756-IF6CIS module 140

1756-IF6I module 140

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules

187

## interface module 12

## K

## keying

electronic 77

mechanical 13

## L

## ladder logic

reconfiguring a module 101

unlatching alarms in the 1756-IF8 module

99

,

100

## latching alarms 27

limit alarms

63

,

159

## limiting

1756-OF4 and 1756-OF8 modules 62 , 159

listen-only connections 22

locking tab 13

## M

## mechanical

keying 13

## module block diagrams

1756-IF16 module 39

1756-IF6CIS and 1756-IF6I modules 146

1756-IF8 module 40

1756-OF4 module 64

1756-OF6CI module 160

1756-OF6VI module 161

1756-OF8 module 65

## module fault word

1756-IF16 module 51

floating point mode

52

integer mode 54

1756-IF6CIS and 1756-IF6I modules 154

floating point mode 154 , 156

1756-IF8 module 56

floating point mode 57 , 58 , 59 , 60

integer mode 59

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 205

floating point mode 205

integer mode 207

1756-OF4 and 1756-OF8 modules 69

floating point mode 69 , 70

integer mode 72

1756-OF6CI and 1756-OF6VI modules 166

floating point mode 166

integer mode 168

## module filter

1756-IF16 &amp; 1756-IF8 modules 34

## module identification information 14

ASCII text string 14

catalog code 14

major revision 14

minor revision 14

product type 14

serial number 14

status 14

vendor ID 14

module inhibit 82

## module resolution 11

as related to scaling and data format 29

## module status

retrieving 14

## N

## notch filter

1756-IF6CIS and 1756-IF6I modules 140 1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 188

## O

## open wire detection

1756-OF4 and 1756-OF8 modules 62

## output circuit diagrams

1756-OF4 and 1756-OF8 modules 66

1756-OF6CI module 161

1756-OF6VI module 162

## output data echo 21

## ownership 17

changing configuration in multiple owner-

controllers 23

multiple owners 22 , 23

## P

## preventing electrostatic discharge 15 process alarms

1756-IF16 &amp; 1756-IF8 modules 36 1756-IF6CIS and 1756-IF6I modules 143 1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 190

## producer/consumer model 11 , 27

## ramping

limiting the rate of change in an output signal 61 , 158 maximum ramp rate 61 , 158

## rate alarm

1756-IF16 &amp; 1756-IF8 modules 37

1756-IF6CIS and 1756-IF6I modules 144 1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 191

## rate limiting 61 , 158

## rate of change

trigger point 191

real time sample (RTS) 18 , 35 , 141 , 188

in a local chassis 18

## remote chassis

configuring remote I/O modules 92 connecting via ControlNet network 236 , 237

## removable terminal block (RTB) 12

removal and insertion under power (RIUP) 11 ,

25

requested packet interval (RPI) 19

retrieving module identification information 1 14

retrieving module status 14

rolling timestamp 11

RPI

set the rate 82

## RSLogix 5000

calibration 103

downloading configuration data

## RSNetWorx

using with RSLogix 5000 235

## S

## scaling

as related to module resolution and data format 30

## sensor type

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 193

## single-ended wiring method

1756-IF16 and 1756-IF8 modules 33

## software

module configuration 75

troubleshooting 123

## software tags

floating point mode integer mode

130 - 133

128 - 129

status indicators 13 , 27

input modules 121

output modules 122

## T

## tasks

event 20

## temperature units

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules 194

## timestamp 26

rolling 11

triggering event tasks 20

## R

89

## troubleshooting 121 - 125

module status indicators 13

## U

## underrange/overrange detection

1756-IF16 &amp; 1756-IF8 modules 35

1756-IF6CIS and 1756-IF6I modules 141

1756-IR6I, 1756-IT6I and 1756-IT6I2 modules

188

## W

## wire off detection

1756-IF16 and 1756-IF8 modules differential current applications 38 differential voltage applications 38 single-ended current applications 38 single-ended voltage applications 38 1756-IF6CIS and 1756-IF6I modules 145 current applications 145 voltage applications 145 1756-IR6I module ohms applications 192 temperature applications 192

1756-IT6I and 1756-IT6I2 modules

millivolt applications 192

temperature applications 192

## wiring

using the IFM 12

using the RTB 12

## wiring examples

1756-IF16 module 43 - 46

1756-IF6CIS module 148 - 150

1756-IF6I module 151 - 153

1756-IF8 module 47 - 48

1756-IR6I module 201

1756-IT6I2 modules

1756-OF4 module

204 67

1756-OF6CI module 163

1756-OF6VI module 165

1756-OF8 module 68

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

Allen-Bradley, ControlLogix, expanding human possibility, FactoryTalk, Logix 5000, Rockwell Automation, RSLogix 5000, RSLinx, and RSNetWorx are trademarks of Rockwell Automation, Inc. ControlNet and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## rockwellautomation.com

expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 UNITEDKINGD0M:RockwellAutomationLtd.Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:（44)（1908)838-800