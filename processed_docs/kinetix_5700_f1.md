<!-- image -->

## Kinetix 5700 Safe Monitor Functions

Catalog Numbers 2198-D006-ERS3, 2198-D012-ERS3,

2198-D020-ERS3, 2198-D032-ERS3, 2198-D057-ERS3,

2198-S086-ERS3, 2198-S130-ERS3, 2198-S160-ERS3,

2198-D006-ERS4, 2198-D012-ERS4, 2198-D020-ERS4,

2198-D032-ERS4, 2198-D057-ERS4, 2198-S086-ERS4,

2198-S130-ERS4, 2198-S160-ERS4, 2198-S263-ERS3,

2198-S263-ERS4, 2198-S312-ERS3, 2198-S312-ERS4

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

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property 
iiiifii j
damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential 
iijii() y qppppp
Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory 
iffifii() jy pp
requirements for safe work practices and for Personal Protective Equipment (PPE).

## Table of Contents

|                                  | Preface                                                                                             |                                                   |
|----------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
|                                  | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . 5                                   |
|                                  | Conventions. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . 6                               |
|                                  | Terminology. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . 6                               |
|                                  | Additional Resources . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . . . . . . 7                         |
|                                  | Chapter 1                                                                                           |                                                   |
| About Safe Stop and Safe Monitor | Safety Concept. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . . . . . . . 10                                |
| Functions                        | Certification . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 10                                |
|                                  | Important Safety Considerations . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . 11   |
|                                  | Stop Category Definition . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 11                  |
|                                  | Performance Level (PL) and Safety Integrity Level (SIL) . . . . . . . . . 11                        |                                                   |
|                                  | Average Frequency of a Dangerous Failure . . . . . . . . . . . . . . . . . . . . . 11               |                                                   |
|                                  | Kinetix Safe Motion-monitoring Operation . . .                                                      | . . . . . . . . . . .  . . . . . . . . . 12       |
|                                  | Compatible Safety Controllers .  . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 13                    |
|                                  | Motion and Safety Tasks . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 14                  |
|                                  | Motion Safety Instances. . . . .  . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 14                  |
|                                  | Safety Function Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15  |                                                   |
|                                  | Safe Monitor Network Communication. . . . .                                                         | . . . . . . . . . . .  . . . . . . . . 16         |
|                                  | Explicit Messages. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 18                |
|                                  | Out of Box State . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . . . 20                                |
|                                  | Restore Hardwired STO mode by Using the Drive Display . . . . . . . 20                              |                                                   |
|                                  | Chapter 2                                                                                           |                                                   |
| Safe Stop Functions              | Timed SS1 (drive-based) Stopping Function . . . . . . . . . . . . . . . . . . . . . . . 23          |                                                   |
|                                  | Monitored SS1 (drive-based) Stopping Function . . . . . . . . . . . . . . . . . . . 24              |                                                   |
|                                  | Ramp Monitored Function . . . .  . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 25                  |
|                                  | Monitored SS1 With Fault . . . . .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 27                  |
|                                  | Monitored SS1 Request Removed .  . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . 28                      |
|                                  | Safe Torque-off Function . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . 29              |
|                                  | Safe Stop Functions (drive-based) Assembly Tags . . . . . . . . . . . . . . . . . . 29              |                                                   |
|                                  | Drive-based Safe Stopping Application Requirements . . . . . . . . . . . . . . 31                   |                                                   |
|                                  | Safety Application Requirements. . . . . . . .                                                      | . . . . . . . . . . . .  . . . . . . . . . . 31   |
|                                  | System Safety Reaction Time .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 32                  |
|                                  | Chapter 3                                                                                           |                                                   |
| Configure the Motion Safety      | Understand Module Properties Categories . . . . . . . . . . . . . . . . . . . . . . . . 33          |                                                   |
| Instances                        | Module Properties>General Category. . . . .                                                         | . . . . . . . . . . . .  . . . . . . . . . 35     |
|                                  | Module Properties>Connection and Safety Categories . . . . . . . . . . 38                           |                                                   |
|                                  | Motion Safety>Actions Category  . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 39                    |
|                                  | Motion Safety>Primary Feedback Category . . . . . . . . . . . . . . . . . . . . 40                  |                                                   |
|                                  | Motion Safety>Secondary Feedback Category . . . . . . . . . . . . . . . . . . 44                    |                                                   |
|                                  | Motion Safety>Scaling Category   . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 44                  |
|                                  | Motion Safety>Discrepancy Checking Category . . . . . . . . . . . . . . . . 47                      |                                                   |
|                                  | Motion Safety>STO Category . . . . . . . . . .                                                      | . . . . . . . . . . . .  . . . . . . . . . . . 49 |

|                            | Motion Safety>SS1 Category . . . . . . . . . . .  . . . . . . . . . . . .                                                                                                                 | . . . . . . . . . . . 50                          |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
|                            | Primary Safety Feedback Example (DSL SIL 2 encoder) . . . . . . . . . . . . . 51                                                                                                          |                                                   |
|                            | Dual Feedback Monitoring Example (DSL SIL 2 encoder) . . . . . . . . . . . 54                                                                                                             |                                                   |
|                            | Primary Safety Feedback Example (Hiperface or Hiperface SIL 2 encoder) . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 59 |                                                   |
|                            | Encoder Feedback Types and SIL Ratings . . . . . . . . . . . . . . . . . . . . . . . . . 62                                                                                               |                                                   |
|                            | Chapter 4                                                                                                                                                                                 |                                                   |
| Controller-based Safety    | Drive Safety Instructions  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                        | . . . . . . . . . . . . 65                        |
| Functions                  | Before Adding the Safety Instructions . . . . . . . . . . . . . . . . . . . . . . . . . 66                                                                                                |                                                   |
|                            | Drive Safety Instruction Example . . . . . . .                                                                                                                                            | . . . . . . . . . . . .  . . . . . . . . . . 67   |
|                            | Pass-through Data . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                                              | . . . . . . . . . . . . . . . . . 68              |
|                            | SFX Instruction. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                         | . . . . . . . . 69                                |
|                            | SFX Instruction Example. . . . .  . . . . . . . . . . . . . . . . .                                                                                                                       | . . . . . . . . . . . . . . . 69                  |
|                            | Chapter 5                                                                                                                                                                                 |                                                   |
| Troubleshoot Safety Faults | Safety Fault Names. . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                                              | . . . . . . . . . . . . . . . . . 73              |
|                            | Understand Safety Faults . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                                                 | . . . . . . . . . . . . . . . . 74                |
|                            | Safety Core Fault . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                              | . . . . . . . 74                                  |
|                            | Safe Torque-off Fault . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                                                  | . . . . . . . . . . . . . . . 74                  |
|                            | Safe Stop 1 Fault . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                                              | . . . . . . . . . . . . . . . . 75                |
|                            | SS2, SOS, SBC, SLS, SLP, and SDI Faults . . . . . . . . . . . . . . . . . . . . . . . 75                                                                                                  |                                                   |
|                            | Safety Feedback Faults . . . . .  . . . . . . . . . . . . . . . . . .                                                                                                                     | . . . . . . . . . . . . . . . . 76                |
|                            | Troubleshoot the Safety Function . . . . . . .                                                                                                                                            | . . . . . . . . . . . .  . . . . . . . . . . 77   |
|                            | Safety Fault Reset. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                                                  | . . . . . . . . . . . . . . . . . 78              |
|                            | Appendix A                                                                                                                                                                                |                                                   |
| Controller Tags and Safety | Motion Connection Axis Tags  . . . . . . . . . . . . . . . . . . .                                                                                                                        | . . . . . . . . . . . . . . . . . 81              |
| Attributes                 | Safety Assembly Tags. . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                        | . . . . . . . . . . . . . 84                      |
|                            | Safety Feedback Attributes  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                         | . . . . . . . . . . . . 86                        |
|                            | Safe Stop Function Attributes . .  . . . . . . . . . . . . . . . . . .                                                                                                                    | . . . . . . . . . . . . . . . . 88                |
|                            | Dual Channel Feedback Attributes . . . . . . . . .                                                                                                                                        | . . . . . . . . . . . . .  . . . . . . . . . . 91 |
|                            | Appendix B                                                                                                                                                                                |                                                   |
| Safety Function Validation | Safe Stop 1 (SS1) . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                      | . . . . . . . 93                                  |
| Checklist                  | Safe Stop 2 (SS2) . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                  | . . . . . . . . . . . . . 95                      |
|                            | Safe Operating Stop (SOS) .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                  | . . . . . . . . 97                                |
|                            | Safely Limited Speed (SLS). . . .  . . . . . . . . . . . . . . . . . .                                                                                                                    | . . . . . . . . . . . . . . . . . 99              |
|                            | Safely Limited Position (SLP). .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                   | . . . . . . . 100                                 |
|                            | Safe Direction (SDI). . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . . . . . . . . . . . 101                         |
|                            | Safe Feedback Interface (SFX). .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                   | . . . . . . 102                                   |
|                            | Safe Brake Control (SBC) .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                       | . . . . . . . . . . 103                           |
|                            | Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                | . . . . . . . 105                                 |

## Summary of Changes

This publication explains how the Kinetix® 5700 drives can be used in up to Safety Integrity Level (SIL 3), Performance Level (PLe) applications. It describes the safety requirements, including PFH values and application verification information, and provides information to configure and troubleshoot the Kinetix 5700 drives with safe-stopping and safe-monitoring functions.

Use this publication if you are responsible for designing, configuring, or troubleshooting safety applications that use the Kinetix 5700 drives. You must have a basic understanding of electrical circuitry and familiarity with Kinetix 5700 drives.

<!-- image -->

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

To install, configure, startup, and troubleshoot your Kinetix 5700 servo drive system, refer to the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002. For Kinetix 5700 drive specifications, see the Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications Technical Data, publication KNX-TD003 .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic Page                                                         |            |
|--------------------------------------------------------------------|------------|
| Added information for Series change for Kinetix 5700 Servo Drives. | Throughout |

## Conventions

## Terminology

Table 1 - Abbreviations and Definitions

| Abbreviation Full Term   |                                                | Definition                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          |                                                | Timed SS1 Timed Safe Stop 1 Timed SS1 and Safe Stop 1 time-controlled (SS1-t) are synonymous. Both mean safe stop where the motor speed is decelerated to zero and once the maximum stop-time elapses, torque is removed from the motor. pp, q Safe Stop 1 time-controlled (SS1-t) is according to IEC 61800-5-2. SS1-t Safe Stop 1 time-controlled                                                                                                                                                                                                                                                                                                                                                                                    |
|                          |                                                | Monitored SS1 Monitored Safe Stop 1 Monitored SS1and Safe Stop 1 ramp-monitored (SS1-r) are synonymous. Both mean a safe stop where the motor speed is reduced to standstill within deceleration limits and once standstill speed is reached or the maximum stop-time elapses, torque is removed from the motor. Safe Stop 1 ramp-monitored (SS1-r) is according to IEC 61800-5-2. |
|                          | SS1-r Safe Stop 1 ramp-monitored               | Monitored SS1 Monitored Safe Stop 1 Monitored SS1and Safe Stop 1 ramp-monitored (SS1-r) are synonymous. Both mean a safe stop where the motor speed is reduced to standstill within deceleration limits and once standstill speed is reached or the maximum stop-time elapses, torque is removed from the motor. Safe Stop 1 ramp-monitored (SS1-r) is according to IEC 61800-5-2. |
|                          |                                                | Hardwired STO Hardwired Safe Torque Off Safe Torque Off safety function activated by external safety device with connections to drive safety input terminals.                                                                                                                                                                                                                      |
|                          |                                                | Integrated STO Integrated Safe Torque Off Safe Torque Off safety function activated over the network.                                                                                                                                                                                                                                                                              |
| –                        |                                                | Control application Program that is designed using Studio 5000 Logix Designer® and downloaded to the controller.                                                                                                                                                                                                                                                                   |
| –                        | Safety control application                     | Safety program that is designed using Studio 5000 Logix Designer and downloaded to the GuardLogix controller for functional safety.                                                                                                                                                                                                                                                |
| –                        | Safe motion monitoring drive                   | A drive that supports safety feedback and communicates safety function status or control over the EtherNet/IP™ network.                                                                                                                                                                                                                                                            |
|                          |                                                | DSL Digital Servo Link HIPERFACE DSL is a digital protocol that is trademarked by SICK AG.                                                                                                                                                                                                                                                                                         |
|                          |                                                | CIP™ Common Industrial Protocol Protocol for industrial automation applications and trademarked by ODVA, Inc.                                                                                                                                                                                                                                                                      |
|                          | 1oo2 One out of Two                            | Refers to the behavioral design of a dual-channel safety system.                                                                                                                                                                                                                                                                                                                   |
|                          | CAT Category                                   | ISO 13849-1 safety category.                                                                                                                                                                                                                                                                                                                                                       |
| IEC                      | International Electrotechnical Commission      | Non-profit, non-governmental international standards organization that prepares and publishes international standards for all electrical, electronic, and related technologies, collectively known as electrotechnology.                                                                                                                                                           |
| EN                       | European Norm                                  | European Standards (EN specifications) developed by the European Committee for Standardization for the European Union.                                                                                                                                                                                                                                                             |
| IGBT                     | Insulated Gate Bi-polar Transistors            | Typical power switch used to control main current.                                                                                                                                                                                                                                                                                                                                 |
| ISO                      | International Organization for Standardization | Voluntary organization whose members are recognized authorities on standards, each one representing another country.                                                                                                                                                                                                                                                               |
| PES                      | Programmable Electronic Systems                | System for control, protection, or monitoring based on one or more programmable electronic devices, including all elements of the system such as power supplies, sensors and other input devices, data highways and other communication paths, and actuators and other output devices.                                                                                             |
| PFH                      | Average Frequency of a Dangerous Failure       | The average frequency of a system to have a dangerous failure occur.                                                                                                                                                                                                                                                                                                               |
|                          | HFT Hardware Fault Tolerance                   | Hardware fault tolerance is the minimum number of faults that can cause a loss of the safety function as defined by IEC 61508- 2.                                                                                                                                                                                                                                                  |
| PL                       |                                                | Performance Level ISO 13849-1 safety category.                                                                                                                                                                                                                                                                                                                                     |
| SIL                      |                                                | Safety Integrity Level A measure of a products ability to lower the risk that a dangerous failure could occur.                                                                                                                                                                                                                                                                     |

These conventions are used throughout this publication:

- Bulleted lists such as this one provide information, not procedural steps
- Numbered lists provide sequential steps or hierarchical information
- When the phrase 'GuardLogix® controller' is used in this publication, it refers to either of the following controller families:
- GuardLogix 5580
- Compact GuardLogix 5380
- When the phrase 'Logix 5000™ controller' is used in this publication, it refers to any of the following controller families:
- ControlLogix® 5570, CompactLogix™ 5370, or GuardLogix 5570
- ControlLogix 5580 or GuardLogix 5580
- CompactLogix 5380 or Compact GuardLogix 5380
- When catalog number 2198-xxxx-ERS3 appears in this publication without series designation, the topic applies to all drive series

This table defines the abbreviations that are used in this manual.

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001                                                                                                                                                                                                                                                     | Product specifications for Kinetix VPL, VPC, VPF, VPH, VPS, Kinetix MPL, MPM, MPF, MPS; Kinetix TL and TLY, Kinetix RDB, Kinetix MMA, and Kinetix HPK rotary motors.                    |
| Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002                                                                                                                                                                                                                                                     | Provides product specifications for Kinetix MPAS and MPMA linear stages, Kinetix VPAR, MPAR, and MPAI electric cylinders, Kinetix LDAT linear thrusters, and Kinetix LDC linear motors. |
| Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications Technical Data, publication KNX-TD003                                                                                                                                                                                                                           | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network and EtherNet/IP networking servo drive families.                                             |
| Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004                                                                                                                                                                                                                                    | Product specifications for Kinetix 2090 motor and interface cables.                                                                                                                     |
| Kinetix Servo Drive Performance Specifications per Ecodesign Regulation (EU) 2019/1781 Technical Data, publication KNX-TD006                                                                                                                                                                                                   | Provides energy efficiency performance data for Rockwell Automation Kinetix servo drives. This data supports IE2 compliance of Kinetix servo drives per EU 2019/1781.                   |
| Kinetix 5700 Servo Drives User Manual, publication 2198-UM002                                                                                                                                                                                                                                                                  | Provides information to install, configure, startup, and troubleshoot your Kinetix 5700 servo drive system.                                                                             |
| Vertical Load and Holding Brake Management Application Technique, publication MOTION-AT003                                                                                                                                                                                                                                     | Provides information on vertical loads and how the servo motor holding-brake option can be used to help keep a load from falling.                                                       |
| GuardLogix 5570 and Compact GuardLogix 5370 Controller Systems Safety Reference Manual, publication 1756-RM099  GuardLogix controller-based safety system that uses the Studio 5000 Logix Designer application. GuardLogix 5580 and Compact GuardLogix 5380 Controller Systems Safety Reference Manual, publication 1756-RM012 | Provides information for development, operation, or maintenance of a GuardLogix or Compact                                                                                              |
| GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095                                                                                                                                                                                                                                         | Provides information that describes the GuardLogix Safety Application Instruction Set.                                                                                                  |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                                                                                                                                                                                                                                    | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                     |
| Product Certifications website, rok.auto/certifications                                                                                                                                                                                                                                                                        | Provides declarations of conformity, certificates, and other certification details.                                                                                                     |

You can view or download publications at rok.auto/literature .

## Notes:

Table 2 - Integrated Functional Safety Support

| Integrated Safety Over the EtherNet/IP Network Safety Function   |                                                                                                                   | Dual-axis Inverters Cat. No.                          | Single-axis Inverters Cat. No.                        |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Drive-based stopping functions                                   | Timed Safe Stop 1 (SS1)                                                                                           | • 2198-Dxxx-ERS3 (series B or later) • 2198-Dxxx-ERS4 | • 2198-Sxxx-ERS3 (series B or later) • 2198-Sxxx-ERS4 |
| Drive-based stopping functions                                   | Monitored Safe Stop 1 (SS1)                                                                                       | 2198-Dxxx-ERS4                                        | 2198-Sxxx-ERS4                                        |
| Controller-based stopping functions                              | • Monitored Safe Stop 1 (SS1) • Safe Stop 2 (SS2)                                                                 | 2198-Dxxx-ERS4                                        | 2198-Sxxx-ERS4                                        |
| Controller-based monitoring functions                            | • Safe Operational Stop (SOS) • Safely-limited Speed (SLS) • Safety-limited position (SLP) • Safe Direction (SDI) | 2198-Dxxx-ERS4                                        | 2198-Sxxx-ERS4                                        |
| Safety feedback function                                         | Safety Feedback Interface (SFX)                                                                                   | 2198-Dxxx-ERS4                                        | 2198-Sxxx-ERS4                                        |
| Integrated STO mode                                              | Safe Torque-off (STO)                                                                                             | • 2198-Dxxx-ERS3 • 2198-Dxxx-ERS4                     | • 2198-Sxxx-ERS3 • 2198-Sxxx-ERS4                     |

The 2198-xxxx-ERS4 drives also support the safety feedback (SFX) instruction that provides safety position and velocity data to a GuardLogix safety controller for use in controller-based monitoring functions.

<!-- image -->

## About Safe Stop and Safe Monitor Functions

Use this chapter to become familiar with the safe stop and safe monitor functions that are built into Kinetix® 5700 dual-axis and single-axis inverters.

| Topic                                    |   Page |
|------------------------------------------|--------|
| Safety Concept                           |     10 |
| Kinetix Safe Motion-monitoring Operation |     12 |
| Out of Box State                         |     20 |

The Kinetix 5700 dual-axis and single-axis inverters are equipped for integrated (drive-based) Monitored SS1 and Timed SS1 stopping functions over the EtherNet/IP™ network. Drive-based safety functions operate in the drive and are activated through the network safety connection.

The Kinetix 5700 inverters also support controller-based monitoring functions. Controller-based safety functions operate in the GuardLogix® 5580 or Compact GuardLogix 5380 controllers and use the EtherNet/IP network to communicate with the safety I/O. This includes the safety functions provided by the Drive Safety tab of your Studio 5000 Logix Designer® project.

- The drive-based (Monitored SS1 and Timed SS1) stopping functions and controller-based monitoring functions apply to the 2198-xxxx-ERS4 drives
- The drive-based Timed SS1 stopping function and STO with configurable delay applies to the 2198-xxxx-ERS3 (series B or later) drives
- When catalog number 2198-xxxx-ERS3 appears in this publication without series designation, the topic applies to all drive series

## Safety Concept

The Kinetix 5700 dual-axis and single-axis inverters are also equipped for hardwired and integrated Safe Torque Off (STO). These STO modes apply to 2198-xxxx-ERS3 and 2198-xxxx-ERS4 dual-axis and single-axis inverters. For Safe Torque Off (STO) operation, see the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 .

Table 3 - Achievable Safety Function Ratings

| Function   | Mode           | Achievable Safety Rating (1) (2)            |
|------------|----------------|------------|
| SS1(3)     | Monitored      | SIL 3, PLe |
| SS2(3)     | Velocity check | SIL 3, PLe |
| SOS(3)     | Velocity check | SIL 3, PLe |
| SLS(3)     | –              | SIL 3, PLe |
| SS2        | Position check | SIL 2, PLd |
| SOS        | Position check | SIL 2, PLd |
| SDI        | –              | SIL 2, PLd |
| SLP        | –              | SIL 2, PLd |

The safe motion-monitoring drives can be configured for single feedback or dual feedback per axis to achieve the following safety rating:

- Single feedback configurations provide up to SIL 2 (PLd) capability.
- Dual feedback configurations provide up to SIL 3 (PLe) capability using velocity discrepancy checking. Safety functions that use position check with dual feedback have up to SIL 2 (PLd) capability.

This section introduces you to the functional safety specifications and how the Kinetix 5700 drives meet those requirements.

## Certification

The TÜV Rheinland group has approved the 2198-Dxxx-ERS4 and 2198-Sxxx-ERS4 inverters with support for Monitored SS1 and Timed SS1 safety functions in addition to the STO safety function. These safety functions are for use in safety-related applications up to ISO 13849-1 Performance Level e (PLe) SIL CL 3 per IEC 61508, IEC 61800-5-2, and IEC 62061. Removing the motion producing power is considered to be the safe state.

## IMPORTANT

Hardwired STO mode is the default setting. Integrated STO mode and the Safe Stop 1 functions (Monitored SS1 and Timed SS1) must be configured from the Studio 5000 Logix Designer application.

TÜV Rheinland 2198-xxxx-ERS4 certification applies to only STO, drive-based Monitored SS1, and drive-based Timed SS1 safety functions.

See the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095, for more information on safe motion-monitoring instructions.

For product certifications currently available from Rockwell Automation, go to rok.auto/certifications .

## Important Safety Considerations

The system user is responsible for the following:

- Validation of any sensors or actuators that are connected to the system
- Completing a machine-level risk assessment
- Certification of the machine to the desired ISO 13849 Performance Level or IEC 62061 SIL level
- Project management and proof testing in accordance with ISO 13849

## Stop Category Definition

You must use a risk assessment to determine the selection of a stop category for each stop function.

- Stop Category 0, as defined in IEC 60204, or Safe Torque-off as defined by IEC 61800-5-2, is achieved with immediate removal of power to the actuator, which results in an uncontrolled coast-to-stop.
- Stop Category 1, as defined in IEC 60204, or Safe Stop 1 (Monitored SS1 and Timed SS1), as defined by IEC 61800-5-2, is achieved with power available to the machine actuators to achieve the stop. Power is removed from the actuators when the configured stop is achieved.

## Performance Level (PL) and Safety Integrity Level (SIL)

For safety-related control systems, Performance Level (PL), according to ISO 13849-1, and SIL levels, according to IEC 61800-5-2, IEC 61508, and IEC 62061, include a rating of the systems ability to perform its safety-related functions. All safety-related components of the control system must be included in both a risk assessment and the determination of the achieved levels.

See the ISO 13849-1, IEC 61508, and IEC 62061 standards for complete information on requirements for PL and SIL determination.

## Average Frequency of a Dangerous Failure

Safety-related systems are classified as operating in a High-demand/ continuous mode. The SIL value for a High-demand/continuous mode safetyrelated system is directly related to the average frequency of a dangerous failure per hour (PFH). PFH calculation is based on the equations from IEC 61508 and show worst-case values. Table 4 demonstrates the worst-case effect of various configuration changes on the data.

## IMPORTANT

Determination of safety parameters is based on the assumptions that the system operates in High-demand mode and that the safety function is requested at least once every three months.

## Table 4 - PFH for 20-year Proof Test Interval

| Attribute                        | 2198-Sxxx-ERS4  (1) Single-axis Inverters   | 2198-Dxxx-ERS4 (1) Dual-axis Inverters   |
|----------------------------------|---------------------------------------------|------------------------------------------|
| PFH (1e-9) 3.85 3.85             |                                             |                                          |
| HFT (hardware fault tolerance) 1 |                                             | 1                                        |
| Proof test (years)               | 20                                          | 20                                       |

## Kinetix Safe Motionmonitoring Operation

In safe motion-monitoring applications, the 2198-Dxxx-ERS4 dual-axis inverters 2198-Sxxx-ERS4 single-axis inverters provide safety position and velocity information over the EtherNet/IP network.

The following components are included in typical safe motion-monitoring drive systems.

Table 5 - Safe Motion-monitoring System Components

| Safety System Component                          | Bulletin/Cat. No.                                                          | Description                                                                                                  |
|--------------------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Kinetix 5700 servo drives                        | 2198-Dxxx-ERS4                                                             | Dual-axis inverter with safe-motion monitoring support.                                                      |
| Kinetix 5700 servo drives                        | 2198-Sxxx-ERS4                                                             | Single-axis inverter with safe-motion monitoring support.                                                    |
| Compact GuardLogix controller Bulletin 5380      |                                                                            | Safety controllers required for use in safe motion-monitoring applications with 2198-xxxx-ERS4 servo drives. |
| GuardLogix controller                            | Bulletin 5580                                                              | Safety controllers required for use in safe motion-monitoring applications with 2198-xxxx-ERS4 servo drives. |
| Studio 5000 Logix Designer                       | Version 31.00 or later                                                     | Application environment                                                                                      |
| External SIN/COS encoder                         | Bulletin 842HR                                                             | Used in Dual Feedback Monitoring applications.                                                               |
| Kinetix VP rotary motors  (1)                    | VPL-Bxxxx-W, VPL-Bxxxx-Q VPF-Bxxxx-W, VPF-Bxxxx-Q VPH-Bxxxx-W, VPH-Bxxxx-Q | Kinetix VPL, VPF, or VPH servo motors with SIL 2 (PLd) rated (-W or -Q) encoders.                            |
| Kinetix VP rotary motors  (1)                    |                                                                            | VPC-Bxxxx-Q Kinetix VPC servo motors with SIL 2 (PLd) rated (-Q) encoders.                                   |
| Kinetix VP electric cylinders                    |                                                                            | VPAR-Bxxxx-W, VPAR-Bxxxx-Q Kinetix VPAR electric cylinder with SIL 2 (PLd) rated (-W or -Q) encoders         |
| Kinetix MP rotary motors  (1)                    | MPL-Bxxxx-S, MPL-Bxxxx-M MPF-Bxxxx-S, MPF-Bxxxx-M MPM-Bxxxx-S, MPM-Bxxxx-M | Kinetix MP servo motors with single-turn (-S) and multi-turn (-M) encoders.                                  |
| Universal feedback connector kit 2198-K57CK-D15M |                                                                            | Used with Kinetix MP servo motors.                                                                           |
| Kinetix MM rotary motor                          | MMA-Bxxxxxx-S2 MMA-Bxxxxxx-M2                                              | Kinetix MM main motors with SIL 2 single-turn (-S) and multi-turn (-M) encoders.                             |

In this example, the components that are described in Table 5 are used in a motion and safety control system with dual-feedback monitoring.

Figure 1 - Safe Motion-monitoring Configuration

<!-- image -->

## Compatible Safety Controllers

A GuardLogix 5580 or Compact GuardLogix 5380 safety controller is required for integrated safety control of the Kinetix 5700 stopping and monitoring functions.

The Studio 5000 Logix Designer application, version 31.00 or later, supports programming, commissioning, and maintaining GuardLogix safety controllers with Kinetix 5700 drive systems.

The safety connection can originate from either of these GuardLogix controllers:

- A GuardLogix 5580 or Compact GuardLogix 5380 safety controller that provides both safety and motion control
- A GuardLogix 5580 or Compact GuardLogix 5380 safety controller that controls only the safety connection, while a separate ControlLogix® 5570, ControlLogix 5580, CompactLogix™ 5370, or CompactLogix 5380 controller that controls the motion connection

## Motion and Safety Tasks

Motion systems that are built using Rockwell Automation® Integrated Architecture® components have separate motion and safety functions. In a typical control application with motion and safety connections, motion and safety tasks run in the following Logix 5000™ controllers:

- Motion functions operate in a motion task of any ControlLogix or CompactLogix (Logix 5000) controller
- Safety functions operate in a safety task of only GuardLogix 5580 or Compact GuardLogix 5380 controllers
- Motion tasks and safety tasks can operate in the same GuardLogix controller or in separate controllers
- The safety task, operating in a GuardLogix controller, communicates with the drive module with a safety connection over the EtherNet/IP network. See Safety Task in Figure 3 on page 16 .
- The motion task, operating in any of these controllers, communicates with the drive module Associated Axes with a motion connection over the EtherNet/IP network. See Motion Task in Figure 3 on page 16 .
- The Kinetix 5700 (2198-xxxx-ERS4) drives contain one or two inverters for the control of one or two motors, each associated with an axis controlled by the motion task.
- Feedback from position encoders, supplied to the motion tasks, is also associated with the axis.

<!-- image -->

## Motion Safety Instances

The Kinetix 5700 (2198-xxxx-ERS4) drives also contain one or two motion safety instances to provide integrated safety functions. The safety instances operate independently of the inverters and feedback that is used for motion. The drive module safety instances receive encoder safety feedback for use with the integrated safety functions. The safety feedback is also supplied to the controller safety task over the safety connection, for use with controller-based safety functions that may operate in the controller.

A motion and safety system can be configured so that a safety function operates in the controller. This type of configuration is referred to as a controller-based safety function. The system can also be configured so that the safety function operates in the drive module, with the initiation and monitoring of the function in the safety task. This type of safety function is referred to as drivebased safety. A motion system can have both controllerbased and drive-based safety functions.

<!-- image -->

## Safety Function Operation

In this example, we describe how a motion and safety control system operates and how motion and safety tasks are coordinated. In typical motion and safety system applications, an E-stop switch is used to stop the system. In the following example, the switch is used to initiate the process that brings the axis to a controlled stop before removing power. This type of stop is called Stop Category 1. The motion task and drive inverter are responsible for bringing the axis to a Category 1 stop. Simultaneously, to make sure that the Stop Category 1 is correctly executed by the motion system, the safety task initiates a Monitored SS1 safety function. The SS1 safety function can be configured to use the drive-based SS1 function or it can be configured to use the controllerbased SS1 function.

This sequence of events represents the steps that are required for a Monitored SS1 drive-based safety function.

<!-- image -->

The words module , instance, and axis (italic) in these steps represent the module, instance, and axis name assigned in the Logix Designer application.

1. The safety task reads the E-stop input and detects the switch actuation.
2. The safety task communicates an SS1 request by setting the bit: module:SO.SS1Request[instance] tag of the drive (inverter) motion-safety instance.
3. The motion-safety instance in the drive communicates to the drive motion core of the Axis Safety Status.
4. The motion core communicates with the motion controller running the motion task by updating the motion axis tag axis.SS1ActiveStatus.
5. The motion task controls the axis to bring the motor to a stop within the Monitored SS1 limits for speed and time.
6. While the axis is stopping, the SS1 function (in the motion-safety instance) monitors the axis speed to make sure it remains below the speed limit and maximum stopping time.
7. When the axis reaches standstill speed, the motion-safety core activates the Safe Torque-off function.

This sequence of events represents the steps that are required for a Monitored SS1 controller-based safety function.

<!-- image -->

The words module , instance, and axis (italic) in these steps represent the module, instance, and axis name assigned in the Logix Designer application.

1. The safety task reads the E-stop input and detects the switch actuation.
2. The safety task activates the SS1 safety instruction running in the safety task.
3. The SS1 instruction communicates an SS1 active by setting the bit: module:SO.SS1Active[instance] tag of the drive (inverter) motion-safety instance.
4. The motion-safety instance in the drive communicates to the drive motion core of the Axis Safety Status.
5. The motion core communicates with the motion controller running the motion task, by updating the motion axis tag axis.SS1ActiveStatus.
6. The motion task controls the axis to bring the motor to a stop within the Monitored SS1 limits for speed and time.
7. While all events are occurring, the motion-safety instance updates the Feedback Velocity tag, module:SI.FeedbackVelocity[instance], in the safety controller. The SS1 function running in the safety task receives the speed that is scaled by the SFX safety instruction and makes sure that the axis remains below the speed limit and maximum stopping time.

8. When the axis reaches standstill speed the SS1 safety instruction outputs SS1 complete.
9. The safety task communicates to the drive motion safety instance to activate STO by clearing the bit: module:SO.STOOutput[instance] tag of the drive motion-safety instance.

This figure shows how the safety task and motion tasks communicate with the drive.

Figure 2 - Safe Monitor System Communication

<!-- image -->

- (1) Motion and Safety connections can be made from a single Safety controller or two separate Motion and Safety controllers.

(2) The secondary encoder is required to meet a SIL 3 system rating.

## Safe Monitor Network Communication

The safe monitor network executes motion and safety tasks by using CIP™ protocol.

Figure 3 - Motion and Safety Connections

<!-- image -->

Table 6 - Motion Connection Axis Tags

| Axis Tag Name (motion controller)   | Motion Connection Attribute #   |      | Data Type Description                                                                                                                        | Safety Output Assembly Tag Name (safety controller)   |
|-------------------------------------|---------------------------------|------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Axis.AxisSafetyState 760 DINT       |                                 |      | Drive module Safety Supervisor state. See the Safety Supervisor State on page 19 for more details.                                           | None                                                  |
| Axis.AxisSafetyDataA 986 DINT       |                                 |      | 32-bit data container holding general purpose safety-data passed from the safety controller.                                                 | module:SO:PassThruDataA[instance]                     |
| Axis.AxisSafetyDataB 987 DINT       |                                 |      | 32-bit data container holding general purpose safety-data passed from the safety controller.                                                 | module:SO:PassThruDataB[instance]                     |
| Axis.AxisSafetyStatus 761 DINT      |                                 |      | Collection of bits indicating the status of the standard safety functions for the axis as reported by Drive Safety Instance.                 | See individual bits in Table 37 on page 81 .          |
| Axis.AxisSafetyStatusRA             | 762                             | DINT | Collection of bits indicating the status of Rockwell Automation specific safety functions for the axis as reported by Drive Safety Instance. | See individual bits in Table 37 on page 81 .          |
| Axis.AxisSafetyFaults               | 763                             | DINT | Collection of bits indicating the Safety Fault status of the drive-module safety instances and integrated safety functions.                  | See individual bits in Table 37 on page 81 .          |
| Axis.AxisSafetyFaultsRA             | 764                             | DINT | Collection of bits indicating the safety fault status of Rockwell Automation safety functions.                                               | See individual bits in Table 37 on page 81 .          |
| Axis.AxisSafetyAlarms               | 753                             |      | DINT Reserved for future use.                                                                                                                | –                                                     |

## Pass-through Data

Some of the Motion Connection axis tags are updated from information received from the Safety Connection. This data originates in the safety controller as Safety Output assembly tags and are passed through the drive and on to the motion controller where the corresponding axis tag is updated. These data are called pass-through data. The pass-through data includes items such as status and faults for controller-based safety functions. Two general purpose 32-bit words are provided in the output assembly from the safety controller and appear as AxisSafetyDataA and Axis SafetyDataB in the motion controller associated axis. Safety Data A and B are provided for the safety and motion application for additional safety program status. A typical use of Safety Data A and Safety Data B can be to indicate the value of a safety limit that is currently in effect for the motion application to accordingly control the motion.

## IMPORTANT

Axis tags are for status only and are not used by the safety function. For more information on pass-through data, see Pass-through Data on page 68 .

## Motion Connection

The motion connection communicates drive motion and safety status to the motion task. The motion connection also receives motion commands from the motion task in the motion controller. Data is exchanged at a periodic rate over the connection. To configure the drive-module motion connection Axis Properties in the Logix Designer application, see the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 .

Some of the axis tags are updated from fault and safety status provided by the safety instance in the drive module. The safety instance sends this status to the motion core and then on to the motion controller. Axis tags show the updated status. See Motion and Safety Connections figure on page 16 for an illustration on how status is sent to the motion controller.

IMPORTANT Axis tags are for status only and are not used by the safety function.

Table 7 - Safety Input Assembly Tags

| Safety Input Assembly Tag Name (input to safety controller)   | Type/ [bit]  Description                                                                                                                       |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| module:SI.ConnectionStatus                                    | SINT See individual bits in Table 38 on page 84 .                                                                                              |
|                                                               | module:SI.FeedbackPosition[instance] DINT Primary Feedback Position from drive-module safety instance. Value is in feedback counts.            |
|                                                               | module:SI.FeedbackVelocity[instance] REAL Primary Feedback Velocity from drive-module safety instance. Value is in revolutions/second.         |
|                                                               | module:SI.SecondaryFeedbackPosition[instance] DINT Secondary Feedback Position from drive-module safety instance. Value is in position counts. |
| module:SI.SecondaryFeedbackVelocity[instance]                 | REAL Secondary Feedback Velocity from drive-module safety instance. Value is in revolutions/second.                                            |
| module:SI.StopStatus[instance]                                | SINT See individual bits in Table 38 on page 84 .                                                                                              |
| module:SI.SafeStatus[instance]                                | SINT See individual bits in Table 38 on page 84 .                                                                                              |
|                                                               | module:SI.FunctionSupport[instance] SINT See individual bits in Table 38 on page 84 .                                                          |

## Table 8 - Safety Output Assembly Tags

| Safety Output Assembly Tag Name (output to safety controller)   | Type/ [bit]  Description                                                                                                                       |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                 | module:SO.PassThruDataA[instance] DINT 32-bit data container holding general purpose safety data passed from the safety controller.            |
|                                                                 | module:SO.PassThruDataB[instance] DINT 32-bit data container holding general purpose safety data passed from the safety controller.            |
|                                                                 | module:SO.PassThruStopStatus[instance] SINT Collection of Safe Stop Function Status bits.                                                      |
| module:SO.PassThruSpeedLimitStatus[instance]                    | SINT Collection of Limit Function Status bits.                                                                                                 |
| module:SO.PassThruPositionLimitStatus[instance] SINT            | Collection of bits indicating the Monitoring Function Limit status of controller-based functions. See individual bits in Table 39 on page 85 . |
| module:SO.PassThruStopFaults[instance] SINT                     | Collection of bits indicating the Safety Fault status of controller-based safety functions. See individual bits in Table 39 on page 85 .       |
| module:SO.PassThruLimitFaults[instance] SINT                    | Collection of bits indicating the Safety Fault status of controller-based safety functions. See individual bits in Table 39 on page 85 .       |
|                                                                 | module:SO.SafetyStopFunctions[instance] SINT A collection of bits used to activate (request) safety functions as in Table 39 on page 85 .      |

## Explicit Messages

Use explicit messages to communicate with a drive and obtain additional fault, status, or configuration information that is not be available in the Safety I/O Tag structure. Attribute data is useful for additional diagnostic information. An explicit message can be sent by any controller on the network and used to read any drive module attribute. See Motion Connection Axis Tags on page 81 for the drive-module safety attribute names, and numbers to read the attribute values by using an MSG instruction. Refer to Figure 3 on page 16 to see how explicit messages are part of motion and safety communication.

When an explicit message is used, a class ID must be specified. The class ID identifies the safety object type in the drive module that is accessed.

## Safety Connection

The safety controller communicates with the safety instances in the drive module over the safety connection. Cyclic data are passed in each direction over the safety connection that appears in Safety Controller tag structures called input and output assemblies. The safety connection cyclic rate is configured in the Logix Designer application. The Safety Input Assembly tag structure is data from the drive module safety instances to the safety controller. The Safety Output Assembly tag structure is data from the safety controller to the drive module safety instances. There is only one safety assembly per drive, so a different assembly structure is used for single-axis and dual-axis inverters.

Table 9 - Object Classes Available in Motion Safety Instances

| Object Class                   | Motion Safety Instances                   | Motion Safety Instances   |
|--------------------------------|-------------------------------------------|---------------------------|
| Object Class                   | Single-axis Inverters Dual-axis Inverters |                           |
| Safety Supervisor              | 1                                         | 1                         |
| Safe Stop Functions            | 1                                         | 2                         |
| Safety Feedback                | 2                                         | 4                         |
| Dual-channel Safety Feedback 1 |                                           | 2                         |

IMPORTANT Explicit messages must not be used for any safety related function.

Safety Supervisor State

In the drive module, the connection to the safety instance or instances is controlled by a safety supervisor. The supervisor status can be read by the motion controller through the motion connection and the safety controller through the Safety Input Assembly or by an explicit message.

The safety supervisor state provides information on the state of the integrated safety connection and the mode of operation. There is only one safety supervisor object per drive module. Therefore, for dual-axis inverters, the safety supervisor is the same on both axes.

Table 10 - Safety Supervisor State: MSG

| Parameter Value   | Description                                          |
|-------------------|------------------------------------------------------|
| Service Code 0x0E | Get attribute single                                 |
| Class  0x39       | Safety supervisor                                    |
| Instance 1        | Drive-module safety instance associated with an axis |
| Attribute 0x0B    | Device status                                        |
| Data Type SINT    | Short integer                                        |

Table 11 - Safety Supervisor States

| Value Safety Supervisor State Definition                             |                                          | Safety Mode                |
|----------------------------------------------------------------------|------------------------------------------|----------------------------|
| 2 Configured (no safety connection) No active connections Integrated |                                          |                            |
| 4 Running                                                            | Normal running state Integrated          |                            |
| 7 Configuring                                                        | Transition state                         | Integrated                 |
| 8 Not Configured                                                     | Hardwired STO mode with torque disabled  | Hardwired (out of the box) |
| 51 Not Configured (torque permitted)                                 | Hardwired STO mode with torque permitted | Hardwired (out of the box) |
| 52 Running (torque permitted) STO bypass state                       |                                          | Integrated                 |

Figure 4 - Explicit Message Example

<!-- image -->

## Out of Box State

## Safe Torque-off Mode

You can use the attribute STO Mode to check if the Kinetix 5700 inverter is in STO Bypass mode. STO Bypass mode is used to allow motion while commissioning or troubleshooting a system when Motion Direct Commands (MDC) are needed. See the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002, for more about Safety Bypass and MDC commands.

Table 12 - Safe Torque-off Mode: MSG

| Parameter Value   | Description                                          |
|-------------------|------------------------------------------------------|
| Service Code 0x0E | Get attribute single                                 |
| Class  0x5A       | Safety stop functions                                |
| Instance 1 or 2   | Drive-module safety instance associated with an axis |
| Attribute 0x104   | STO mode                                             |
| Data Type SINT    | Short integer                                        |

Table 13 - Safe Torque-off Mode: Values

|   Value | Definition       |
|---------|------------------|
|       1 | Normal operation |
|       2 | STO bypass mode  |

Kinetix 5700 servo drives are capable of safe torque-off (STO) functionality in Hardwired STO mode or Integrated STO mode. Out of the box, the Kinetix 5700 servo drives are in Hardwired STO mode, which means they are ready for hardwired connections to the safety (STO) connector. To enable motion, jumper wires must be installed in the STO connector. Refer to the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 for a wiring example.

Alternatively, you can establish a connection to a safety controller and the safety task must enable torque by setting the STO output bit in the SO tag for the drive module.

## IMPORTANT

Out of the box, Kinetix 5700 servo drives are in Hardwired STO mode.

## IMPORTANT

To bypass the STO feature while commissioning or testing the drive, the drive must be configured for Hardwired STO mode. Refer to the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 for a wiring example.

Out of the box, you can use Kinetix 5700 servo drives in Integrated STO mode only after a Motion and Safety or Safety-only connection has been established at least once in the Logix Designer application.

## Restore Hardwired STO mode by Using the Drive Display

After the integrated safety connection configuration is applied to the Kinetix 5700 servo drive at least once, you can restore the drive to Hardwired STO mode by using the drive display and navigation buttons.

## IMPORTANT

Only authorized personnel should attempt Reset Ownership. The safety connection must be inhibited before the reset is attempted. If any active connection is detected, the safety reset is rejected and Reset Failed appears on the display.

Follow these steps to restore your Kinetix 5700 drive to the Hardwired STO mode.

1. Disable any Motion and Safety connections configured in the Logix Designer application.

You can do this in Module Properties or by unplugging the Ethernet cable.

2. From the Home screen on the drive display, press the settings button.
3. From the SETTINGS menu, scroll down by using the arrows and select SAFETY.
4. Press to request a Reset Ownership. Are You Sure? appears on the display.
5. Press to acknowledge and begin the reset ownership. If a reset ownership is requested, but not acknowledged within 30 seconds, the display automatically reverts back to the Home screen and the drive does not complete the reset ownership. If a reset ownership is requested and acknowledged within 30 seconds, the drive reverts back to Hardwired STO mode.

## Notes:

## Timed SS1 (drive-based) Stopping Function

## Safe Stop Functions

Use this chapter to learn more about the Monitored SS1 and Timed SS1 stopping functions that are built into Kinetix® 5700 dual-axis and single-axis inverters.

| Topic                                              |   Page |
|----------------------------------------------------|--------|
| Timed SS1 (drive-based) Stopping Function          |     23 |
| Monitored SS1 (drive-based) Stopping Function      |     24 |
| Safe Torque-off Function                           |     29 |
| Safe Stop Functions (drive-based) Assembly Tags    |     29 |
| Drive-based Safe Stopping Application Requirements |     31 |

Monitored SS1 and Timed SS1 meet the requirements of Performance Level e (PL e) per ISO 13849-1 and SIL CL 3 per IEC 61508, IEC 61800-5-2, and IEC 62061.

In drive-based SS1 mode, the GuardLogix® 5580 or Compact GuardLogix 5380 safety controller issues the SS1 command over the EtherNet/IP™ network and the 2198-Dxxx-ERS4 and 2198-Sxxx-ERS4 inverters execute the SS1 command.

Timed SS1 is a safe stop function where a fixed amount of time is given for the drive to stop. Timed SS1 does not monitor the speed of the drive or detect standstill. Timed SS1 is initiated by setting the SS1 Request tag in the Safety Output Assembly for the drive module. When SS1 Request is received by the drive, the axis safety status is updated with SS1 Active. Once SS1 Active is set high (1), either the motion controller or the drive itself must stop the axis within the SS1 Max Stop Time. When Max Stop Time expires, SS1 Complete transitions to high (1), which activates STO. Once activated, STO operates as described in the section on STO Stop Function.

<!-- image -->

## Monitored SS1 (drive-based) Stopping Function

Figure 5 - Timed SS1 Normal Operation

<!-- image -->

(1) For more information on STO Delay, see Motion Safety&gt;STO Category on page 49 .

| Attribute Name Tag Name   |                                                                                    | Description                                                                                                                                | Value                                    |
|---------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| SS1 Request               | module:SO.SS1Request[instance]                                                     | An Output Assembly member that requests the drive to initiate it's Safe Stop 1 function.                                                   | 0 – No Request 1 – Request               |
| SS1 Active                | module:SO.SS1Active[instance]                                                      | The SS1 Active attribute is set to Active when any bit in SS1 Activation is set.                                                           | 0 – Not Active 1 – Active                |
| SS1 Complete              | Tag Name does not apply. See Safe Stop Function Attributes (Class 0x5A) on page 88 | . When using SS1-Timed, the STO Activation Bit SS1-Complete is set when the SS1 Timer expires, setting STO Active to Disable Torque.       | 0 – Not Active 1 – Active                |
| STO Active                | module:SI.STOActive[instance]                                                      | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active                |
| Torque Disabled           |                                                                                    | module:SI.TorqueDisabled[instance] Output status of the Safe Toque Off control.                                                            | 0 – Torque Permitted 1 – Torque Disabled |

Both elements of the Timed SS1 safety function design have SIL 3/PL e (Cat 3) rating.

<!-- image -->

The words module and instance (italic) in these tag names represent the module and instance name assigned in the Logix Designer application.

Monitored SS1 is a ramped safe-stop where the motion safety instance monitors the speed ramp to standstill speed, while either the motion task or the drive itself controls the deceleration to standstill speed. When standstill is reached, then the motion safety instance removes torque from the motor.

## IMPORTANT

In the event of a malfunction, the most likely stop category is Stop Category 0. When designing the machine application, timing and distance must be considered for a coast to stop. For more information regarding stop categories, refer to IEC 60204-1.

When active, the Axis Speed is monitored and must remain below the Speed Limit ramp shown in Figure 6. The axis motion control application must be coordinated with the SS1 activation to bring the axis to Standstill Speed, also known as a Stop Category 1. This section explains several ways to configure the drive and controller for a Monitored SS1 safety function.

<!-- image -->

Figure 6 - Monitored SS1 Normal Operation

| Attribute Name Tag Name   |                                                                                    | Description                                                                                                                                  | Value                                    |
|---------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| SS1 Request               | module:SO.SS1Request[instance]                                                     | An Output Assembly member that requests the drive to initiate it's Safe Stop 1 function.                                                     | 0 – No Request 1 – Request               |
| SS1 Active                | module:SO.SS1Active[instance]                                                      | The SS1 Active attribute is set to Active when any bit in SS1 Activation is set.                                                             | 0 – Not Active 1 – Active                |
| SS1 Complete              | Tag Name does not apply. See Safe Stop Function Attributes (Class 0x5A) on page 88 | . When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active                |
| STO Active                | module:SI.STOActive[instance]                                                      | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque.   | 0 – Not Active 1 – Active                |
| Torque Disabled           |                                                                                    | module:SI.TorqueDisabled[instance] Output status of the Safe Toque Off control.                                                              | 0 – Torque Permitted 1 – Torque Disabled |

## Ramp Monitored Function

The Monitored SS1 (ramp monitored) function is the ramped deceleration of the axis. A ramp function represents the maximum speed while the axis is stopping as a function of time (t).

The ramp function depends on several variables as stated in this equation:

<!-- formula-not-decoded -->

- Speed 0 is the actual speed captured at the end of the monitoring delay in rev/s.
- S tol is a speed tolerance that is added to account for instantaneous speed variations as the actual speed ramps down to standstill.
- D R is the slope (deceleration) of the ramp function in rev/s 2 . The slope is calculated by entering the Decel Reference speed and the Stop Delay.

You enter the Decel Reference Speed and the Stop Delay while configuring SS1 in the Logix Designer application to calculate DR and display the value.

When choosing a value for Stol there are several considerations that depend on the velocity average time. If the velocity average time is too small, the instantaneous speed calculated by the motion safety instance can exceed the ramped speed-limit function. If the velocity average time is too large, the result can be more delay in the speed calculated and compared to the ramped speedlimit function. Refer to Instantaneous Velocity in Figure 15 on page 43 .

<!-- image -->

- Use your maximum axis speed for the Decel Reference Speed and the maximum time to bring the axis to Standstill Speed for the Stop Delay.

<!-- image -->

For more information see the Actions Definitions table in Chapter 7 of the Kinetix 5700 .

- Servo Drives User Manual, publication 2198-UM002

## Monitored SS1 Example

In this example, an axis is running at 1200 rpm when SS1 Request goes high (1), which sets SS1 Active high (1). SS1 Active is read by the Main task and prepares to decelerate the axis. At the end of Stop Monitor Delay, the axis speed is 1200 rpm.

## Data summary for this Monitored SS1 example:

- The Deceleration Reference Speed is 2400 rpm because the original application sizing calculated this value as the maximum axis speed.
- A 10 second Stop Delay value is used, based on the control system ability and the safety evaluation.
- Stop Monitor Delay is set to 2 seconds. At the end of the Stop Monitor Delay, the motor speed is measured at 1200 rpm.
- Deceleration Speed Tolerance is set to 240 rpm, based on machine characteristics and safety evaluation.

At the end of Stop Monitor Delay and the beginning of Stop Delay time, t = 0 for the ramp function. Figure 7 shows the data summary values inserted into the equation.

## Figure 7 - Monitored SS1 Example

<!-- image -->

Values of t in the equation are only valid during the Stop Delay where t starts at 0 and increases to a maximum of Stop Delay.

## Figure 8 - Final Monitored SS1 Example

<!-- formula-not-decoded -->

For any value of t between 0…5 seconds, if the actual speed exceeds Speed (t), a Deceleration Rate fault is set by the SS1 function.

## Monitored SS1 With Fault

This figure shows how the Monitored SS1 behaves when the axis speed does not stay below the ramp function limit.

Figure 9 - Deceleration Rate Fault

<!-- image -->

| Attribute Name Tag Name     |                                                                                      | Description                                                                                                                                | Value                                         |
|-----------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| SS1 Request                 | module:SO.SS1Request[instance]                                                       | An Output Assembly member that requests the drive to initiate it's Safe Stop 1 function.                                                   | 0 – No Request 1 – Request                    |
| SS1 Active                  | module:SO.SS1Active[instance]                                                        | The SS1 Active attribute is set to Active when any bit in SS1 Activation is set.                                                           | 0 – Not Active 1 – Active                     |
| SS1 Complete                | Tag Name does not apply. See Safe Stop Function Attributes (Class 0x5A) on page 88 . | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active                     |
| SS1 Deceleration Rate Fault | Tag Name does not apply. See Safe Stop Function Attributes (Class 0x5A) on page 88 . | Describes detailed information about the fault.                                                                                            | 1 = No Fault 3 = Deceleration Rate            |
| STO Active                  | module:SI.STOActive[instance]                                                        | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active                     |
| Torque Disabled             |                                                                                      | module:SI.TorqueDisabled[instance] Output status of the Safe Toque Off control.                                                            | 0 – Torque Permitted 1 – Torque Disabled      |
| Restart Required            |                                                                                      | module:SI.RestartRequired[instance] Performs restart of safety instance attribute.                                                         | 0 – Restart Not Required 1 – Restart Required |
| Safety Reset                |                                                                                      | module:SO.ResetRequest[instance] Performs reset of safety instance attribute.                                                              | 0 – No Restart 1 – Restart                    |

Series of events when a Monitored SS1 fault occurs.

1. If an SS1 fault occurs, STO Active goes high (1), and Torque Disabled goes high (1) immediately and ignores STO Delay.

The safety instance detects a fault and activates the STO function within 6.0 ms of when the fault condition occurred.

## IMPORTANT

The fault condition for a deceleration fault is measured after velocity averaging. Velocity averaging adds additional delay before STO activation in this case.

2. Restart Required goes high (1) whenever an SS1 fault is present.
3. To reset the SS1 fault, SS1 Request must go low (0), followed by Reset (0-1 transition).

## Monitored SS1 Request Removed

This figure shows what happens when SS1 Request goes low (0) before completion.

Figure 10 - Monitored SS1 Request Removed Before Completion

<!-- image -->

| Attribute Name Tag Name   |                                                                                      | Description                                                                                                                                | Value                      |
|---------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| SS1 Request               | module:SO.SS1Request[instance]                                                       | An Output Assembly member that requests the drive to initiate it's Safe Stop 1 function.                                                   | 0 – No Request 1 – Request |
| SS1 Active                | module:SO.SS1Active[instance]                                                        | The SS1 Active attribute is set to Active when any bit in SS1 Activation is set.                                                           | 0 – Not Active 1 – Active  |
| SS1 Complete              | Tag Name does not apply. See Safe Stop Function Attributes (Class 0x5A) on page 88 . | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active  |
| STO Active                | module:SI.STOActive[instance]                                                        | When the drive speed is at or below SS1Standstill Speed, the STO Activation bit SS1 Complete is set, setting STO Active to Disable Torque. | 0 – Not Active 1 – Active  |

<!-- image -->

The words module and instance (italic) in these tag names represent the module and instance name assigned in the Logix Designer application.

Series of events when SS1 Request is removed before completion.

1. When SS1 Request goes low (0) before completion, SS1 function is reset and ready for another operation.
2. Main task reads the SS1 Active axis tag and resumes normal operation.

## Safe Torque-off Function

## Safe Stop Functions (drivebased) Assembly Tags

The safe torque-off (STO) function provides a method, with sufficiently low probability of failure, to force the power-transistor control signals to a disabled state. When the command to execute the STO function is received from the GuardLogix controller, all of the drive output-power transistors are released from the ON-state. This results in a condition where the motor is coasting. Disabling the power transistor output does not provide isolation of the electrical output that is required for some applications.

<!-- image -->

ATTENTION: The STO function removes motion-producing power from the motor and must be considered in vertical load applications.

These conditions must be met for integrated control of the STO function:

- The Kinetix 5700 drive module must be added to the GuardLogix 5570 or Compact GuardLogix 5370 controller I/O Configuration.
- The module must be configured for Safety Only or Motion and Safety connections
- The safety bypass jumper wires must be removed.

## IMPORTANT

If the STO bypass jumper wires were applied during machine commissioning or maintenance, they must be removed before the drive will operate in Integrated STO mode.

The Kinetix 5700 drive STO function reaction time is less than 10 ms. Reaction time for the drive is the delay between the time the drive STO command receives the CIP Safety™ packet with an STO request and the time when motion producing power is removed from the motor.

Table 14 - Safe Torque-off Specifications

| Attribute                              | Value                      |
|----------------------------------------|----------------------------|
| STO function reaction time             | 10 ms, max                 |
| Safety connection RPI, min             | 6 ms                       |
| Input assembly connections  (1)        | 1                          |
| Output assembly connections  (1)       | 1                          |
| Integrated safety open request support | Type 1 and Type 2 requests |

In Integrated safe torque-off (STO) mode, a GuardLogix or Compact GuardLogix safety controller controls the Kinetix 5700 safe torque-off function through the SO.STOOutput tag in the safety output assembly.

Table 15 - Safety Output Assembly Tag Name Description

| Tag Name  (1)                  | Value                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------|
| module:SO.STOOutput[instance]  | 0 = Activate STO Function 1 = Permit Torque                                               |
| module:SO.SS1Request[instance] | 0 = Remove SS1 Request 1 = Activate Drive Based SS1 Function                              |
|                                | module:SO.ResetRequest[instance] 0 = One transition resets drive-based Safe Stop function |

The SO.Command tags are sent from the GuardLogix safety output assembly to the Kinetix 5700 safety output assembly to control the safe torque-off function.

The SI.Status tags are sent from the Kinetix 5700 inverter to the GuardLogix safety input assembly and indicate the Kinetix 5700 safety control status.

Table 16 - Safety Input Assembly Tag Name Description

| Tag Name (1)                        | Value                                                                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| module:SI.SafetyFault[instance]     | 0 = Safety fault not present 1 = Safety fault present                                                                        |
| module:SI.RestartRequired[instance] | 0 = Reset is not required 1 = Reset is required                                                                              |
| module:SI.STOActive[instance]       | Indicates STO function status 0 = STO function not active 1 = STO function active                                            |
| module:SI.SS1Active[instance]       | Indicates drive-based SS1 active status 0 = SS1 function not active 1 = SS1 function active                                  |
| module:SI.SS1Ready[instance]        | 0 = Drive-based SS1 function is not configured or faulted 1 = Drive-based SS1 function is configured and ready for operation |

The SI.ConnectionStatus tags indicate the safety input connection status.

<!-- image -->

The words module and instance (italic) in these tag names represent the module and instance name assigned in the Logix Designer application.

Controller Tags in Logix Designer

Double-click Controller Tags in the Controller Organizer to see the SS1 controller tags.

The controller tags created for your drive configuration appears.

<!-- image -->

Safety Assembly Tags on page 84 list the safety tags added to the controller tags when a Kinetix 5700 servo drive is added to a GuardLogix I/O configuration and the connection is configured for Safety Only.

In this example, the SO.STOOutput bit permits torque when the bit is high.

<!-- image -->

Figure 11 - Safe Torque-off Function Safety Logic Example

<!-- image -->

## Drive-based Safe Stopping Application Requirements

This section describes some of the safety information required to design your safety application.

Table 17 - Achievable Safety Ratings

| Safety Function   | Achievable Functional Safety Rating (1)                                                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STO               | SIL 3, PL e (independently if hardwired or integrated option is used)                                                                                                                                                    |
|                   | Timed SS1 SIL 3, PL e                                                                                                                                                                                                    |
| Monitored SS1     | • SIL 2, PL d in a single feedback sensor configuration when used with SIL 2, PL d compliant feedback sensor • SIL 3, PL e in a dual feedback sensor configuration when primary feedback sensor is SIL 2, PL d compliant |

The 2198-xxxx-ERS4 STO circuit is designed to turn off all of the output-power transistors when the STO function is requested. You can use the 2198-xxxx-ERS4 STO circuit in combination with other safety devices to achieve the Stop Category 0 as described in Stop Category Definition on page 11, and protection-against-restart as specified in IEC 60204-1.

<!-- image -->

ATTENTION: The safe torque-off (STO) feature is suitable only for performing mechanical work on the drive system or affected area of a machine. It does not provide electrical safety.

<!-- image -->

<!-- image -->

SHOCK HAZARD: In Safe Torque-off mode, hazardous voltages can still be present at the drive. To avoid an electric shock hazard, disconnect power to the system and verify that the voltage is zero before performing any work on the drive.

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

## Safety Application Requirements

Safety application requirements include evaluating probability of failure rates (PFH), system reaction time settings, and functional verification tests that fulfill your required SIL level criteria. Refer to Average Frequency of a Dangerous Failure on page 11 for more PFH information.

Creating, recording, and verifying the safety signature is also a required part of the safety application development process. Safety signatures are created by the safety controller. The safety signature consists of an identification number, date, and time that uniquely identifies the safety portion of a project. This includes all safety logic, data, and safety I/O configuration.

For safety system requirements, including information on the safety network number (SNN), verifying the safety signature, and functional verification tests refer to the appropriate GuardLogix controller publication as defined in Additional Resources on page 7 .

## IMPORTANT

You must read, understand, and fulfill the requirements detailed in the GuardLogix controller systems safety reference manual prior to operating a safety system that uses a GuardLogix controller and Kinetix 5700 drive.

## System Safety Reaction Time

System safety reaction time is the sum of sensor reaction time, GuardLogix controller system reaction time and actuator reaction time. GuardLogix controller system reaction time is estimated based on a number of factors that include:

- Fixed delay time per selected Input/Output module
- Non-configurable variables that are determined by the amount of network communication traffic and the EMC environment
- Configurable values for your specific settings (for example, Safety Input RPI and Safety Task Period)

For a complete list of the factors that affect GuardLogix controller reaction time, refer to the appropriate GuardLogix controller publication as defined in Additional Resources on page 7 .

To optimize the configurable factors and minimize the safety reaction time, the GuardLogix Safety Estimator tool can be used to determine the reaction time under these three conditions:

- If there are no faults or errors, the safety function is demanded under normal operation
- Considering a Single Fault (Max) - Safety function is demanded when there is a single delay in the system (for example, loss of a packet)
- Considering Multiple Faults (Max) - Safety function is demanded when there are multiple delays in the system

The GuardLogix Safety Estimator tool, in Microsoft Excel format, is available from the Product Compatibility Download Center (PCDC) to help you determine the reaction time of your particular control loop. Go to website: http://compatibility.rockwellautomation.com/Pages/home.aspx, click Find Downloads and, in the Search PCDC box under Compatibility and Downloads, search for GLX Safety Tools.

## IMPORTANT

Using this tool does not substitute for taking proper validation and verification measures. See Appendix B on page 93 for more information.

## Understand Module Properties Categories

<!-- image -->

## Configure the Motion Safety Instances

Use this chapter to configure Kinetix® 5700 dual-axis and single-axis inverters for safety applications with servo motors.

| Topic                                                                     | Page   |
|---------------------------------------------------------------------------|--------|
| Understand Module Properties Categories                                   | 33     |
| Primary Safety Feedback Example (DSL SIL 2 encoder)                       | 51     |
| Dual Feedback Monitoring Example (DSL SIL 2 encoder)                      | 54     |
| Primary Safety Feedback Example (Hiperface or Hiperface SIL 2 encoder) 59 |        |
| Encoder Feedback Types and SIL Ratings                                    | 62     |

The following safety configuration examples are included:

- Primary feedback for Kinetix VPC motors (-Q, SIL 2 encoder option) with Motion and Safety connections to the same Logix 5000™ controller
- Primary feedback for Kinetix VPC motors (-Q, SIL 2 encoder option) and an external sin/cos encoder for dual-feedback monitoring with Motion and Safety connections to the same Logix 5000 controller
- Primary feedback for Kinetix MPL motors (-M or -S, Hiperface encoder options) or Kinetix MMA motors (-S2 or -M2, Hiperface SIL2 encoder option) with Motion and Safety connections to separate Logix 5000 controllers

Kinetix VPL, VPC, VPF, and VPH motors, and Kinetix VPAR electric cylinders with -Q or -W encoder options are SIL 2 PL d rated encoders. Kinetix MMA motors with -S2 or -M2 encoder options are SIL2 PL d rated encoders. See the Kinetix Rotary Motion Technical Data, publication KNX-TD001, for motor specifications. See the Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002, for electric cylinder specifications.

The safe monitor functions are configured in the Studio 5000 Logix Designer® application. Follow these guidelines when configuring your motion monitoring application.

## IMPORTANT

For access to Motion Safety module properties, the Connection pull-down menu in the Module Definition dialog box must be configured for Motion and Safety or Safety Only.

Right-click your Kinetix 5700 single-axis or dual-axis inverter and choose Properties. The Module Properties dialog box appears.

Figure 12 - Module Definition Configured With Dual Feedback Monitoring

<!-- image -->

Module properties categories are listed along the left side panel.

- For dual-axis inverters, two sets of Motion Safety categories are listed under Motion Safety 1 and Motion Safety 2 (one for each axis)
- For single-axis inverters, only one set of the same categories are listed under Motion Safety

Motion Safety and Motion Safety 1 align with Axis 1 configured in Associated Axes. Motion Safety 2 aligns with Axis 3 configured in Associated Axes.

Figure 13 - Dual-axis Inverter Feedback

<!-- image -->

In this 2198-Dxxx-ERS4 (dual-axis inverter) example, the Connection mode is Motion and Safety and the Motion Safety instances are configured as Dual Feedback Monitoring.

| Module Properties Category   | Page    |
|------------------------------|---------|
| General                      | page 35 |
| Connection and Safety        | page 38 |
| Motion Safety                |         |
| Actions                      | page 39 |
| Primary Feedback             | page 40 |
| Secondary Feedback           | page 44 |
| Scaling                      | page 44 |
| Discrepancy Checking         | page 47 |
| STO                          | page 49 |
| SS1                          | page 50 |

## Module Properties&gt;General Category

Follow these steps to configure the Module Definition dialog box properties.

1. Select the General category and click Change to open the Module Definition dialog box.
2. From the Revision pull-down menu, choose the drive firmware revision. Depending on the Module Definition revision selection, alternate product features and feedback types can be selected. However, 2198-xxxx-ERS4 drives only appear in firmware revision 9.001 or later.
3. From the Safety Application pull-down menu, choose between Hardwired for Hardwired STO mode or Networked for an integrated safety application (see Table 18 for definitions).

<!-- image -->

## IMPORTANT

<!-- image -->

If the STO bypass jumper wires were applied during machine commissioning or maintenance, they must be removed before the drive will operate in Integrated (Networked) safety mode.

Table 18 - Safety Application Definitions

| Safety Application Mode  (1)   | Safety Functions                                                | Minimum Drive Module (2) Required     | Drive Module Connection Options   | Minimum Controller Required  (3)          |
|--------------------------------|-----------------------------------------------------------------|---------------------------------------|-----------------------------------|-------------------------------------------|
| Hardwired                      | Safe Torque-off (STO)                                           | 2198-xxxx-ERS3 (series A) Motion Only |                                   | • ControlLogix® 5570 • CompactLogix™ 5370 |
| Networked (integrated)         | Safe Torque-off (STO)                                           | 2198-xxxx-ERS3 (series A)             | • Motion and Safety • Safety Only | • GuardLogix® 5570                        |
| Networked (integrated)         | Timed SS1                                                       | 2198-xxxx-ERS3 (series B or later)    | • Motion and Safety • Safety Only | • GuardLogix® 5580 • CompactLogix 5380    |
| Networked (integrated)         | • Timed SS1 • Monitored SS1 • Controller-based safety functions | 2198-xxxx-ERS4                        | • Motion and Safety • Safety Only | • GuardLogix® 5580 • CompactLogix 5380    |

Where a 2198-xxxx-ERS3 (series A) drive is specified, a 2198-xxxx-ERS3 (series B or later) drive is backwards compatible.

(3) Where a ControlLogix or CompactLogix (non-safety) controller is specified, a GuardLogix or Compact GuardLogix controller is backwards compatible. Also, GuardLogix 5580 and Compact GuardLogix 5380 controllers are backwards compatible with GuardLogix 5570 and Compact GuardLogix 5370 controllers.

4. From the Connection pull-down menu, choose the Connection mode for your motion application (see Table 19 for definitions).

<!-- image -->

<!-- image -->

When 'Safety' appears in the Connection mode, integrated safety is implied.

Table 19 - Module Connection Definitions

| Connection Mode Safety Options    |                                                                                  | Description                                                                                                                                                                                                      |
|-----------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Motion and Safety Integrated mode |                                                                                  | Motion connections and integrated STO are managed by this controller.                                                                                                                                            |
| Motion Only                       | • Hardwired STO mode • Integrated mode if there is a secondary safety controller | • Motion connections are managed by this controller. • Hardwired STO is controlled by the hardwired safety inputs or Integrated is managed by another controller that has a Safety-only connection to the drive. |
| Safety Only  (1)                  | Integrated mode                                                                  | • Integrated STO is managed by this controller. • Motion connections are managed by another controller that has a Motion-only connection to the drive.                                                           |

5. From the Motion Safety x pull-down menu, choose the integrated safety type (see Table 20 on page 37 for definitions).

<!-- image -->

'Motion Safety' applies to 2198-Sxxx-ERS4 (single-axis) inverters. 'Motion Safety 1' and 'Motion Safety 2' applies to 2198-Dxxx-ERS4 (dual-axis) inverters.

Table 20 - Motion Safety Instance Definitions

| Motion Safety Instance Mode   | Safety Application Mode   | Module Connection Options         | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------|---------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safe Stop Only - No Feedback  | Networked                 | • Motion and Safety • Safety only | • 2198-xxxx-ERS4: STO function and Timed SS1 Safe Stop functions are available. • 2198-xxxx-ERS3 (series B or later): STO function and Timed SS1 Safe Stop functions are available.                                                                                                                                                                                                           |
| Single Feedback Monitoring    | Networked                 | • Motion and Safety • Safety only | Primary feedback is used in the safety object for safe monitoring. The feedback can be a SIL rated Hiperface DSL encoder, for example, a VPL-B1003P-Q or W motor used in the DSL Feedback port. A Sine/Cosine device can be used for Primary Feedback, for example, an MPL-B310P-m motor used in the Universal Feedback port. The user is responsible for determining the SIL level achieved. |
| Dual Feedback Monitoring      | Networked                 | • Motion and Safety • Safety only | In addition to primary feedback, an external feedback device is used to improve SIL levels. For example, the Bulletin 842HR type encoder can be used in the Universal Feedback port as a Sine/Cosine device.                                                                                                                                                                                  |

If a Motion and Safety connection is configured, the Motion Safety categories appear and can be configured for feedback options (see Table 20 on page 37).

In this example, the Motion Safety categories are configured for Single Feedback Monitoring, so only Primary Feedback appears.

If a Motion Only connection is configured, the Motion Safety category does not appear.

If a Safety Only connection is configured, the Motion Safety categories appear, but the Motion categories do not. The Motion Safety categories can be configured for feedback options (see Table 20 on page 37).

In this example, Motion Safety 2 is configured for Dual Feedback Monitoring, so the Secondary Feedback and Discrepancy Checking categories also appear.

<!-- image -->

Figure 14 - Configure Motion Safety

<!-- image -->

- If Motion Safety is configured for Safe Stop Only - No Feedback, the feedback options do not appear.
- If Motion Safety is configured for Dual Feedback Monitoring, the Primary Feedback and Secondary Feedback categories appear.
- Discrepancy Checking monitors the Primary versus Secondary feedback values for consistency within the specified tolerance. This applies only when the motion safety instance is configured as Dual Feedback Monitoring.
6. Click OK to close the Module Definition dialog box.
7. Click Apply.

## Module Properties&gt;Connection and Safety Categories

Follow these steps to configure the Safety Output and Safety Input values.

1. Select the Connection category.

<!-- image -->

From the Connection category you can observe the status of the Safety Output and Safety Input requested packet interval (RPI) values. The default values are shown.

IMPORTANT

The Safety Output and Safety Input values, when viewed from the Connection category, is for status only. To set the Safety Output and Safety Input values, continue with step 2 through step 6 .

2. To set the Safety Output value, right-click SafetyTask in the Controller Organizer and click Properties.
3. Click the Configuration tab.

<!-- image -->

The default safety task Period value (and output RPI) is 20 ms.

IMPORTANT

The period is the interval at which the safety task executes. The watch dog must be less than the period.

For more safety task information, see the GuardLogix 5580 and Compact GuardLogix 5380 Controller Systems Safety Reference Manual, publication 1756-RM012 .

4. Click OK.
5. To set the Safety Input value, select the Safety category.

<!-- image -->

The default Safety Input RPI value is 10 ms. Edit as appropriate for your application.

6. Click Apply.

## Motion Safety&gt;Actions Category

The Actions category provides fault behavior options. Determine the preferred machine function when a connection loss or connection idle condition occurs. Safe Torque-off (STO) means that the drive immediately disables the motor power outputs causing a coast condition for the motor and load. Safe Stop 1 (SS1) means that the drive decelerates the load to zero speed before removing the motor power outputs causing a controlled stop for the motor and load.

Follow these steps to configure the Actions to Take Upon Conditions dialog box.

1. Select the Motion Safety 1&gt;Actions category.

<!-- image -->

## Table 21 - Motion Safety Actions

|                        | Attribute Description                                                                                                                                                 |           | Values Description                                                                                                                |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| Connection Loss Action | • Connection Loss is caused by someone removing the Ethernet cable from the 2198-xxxx-ERS4 drive. to lose synchronization to the grandmaster clock/motion controller. | SS1       | Drive-based Safe Stop 1 instruction is initiated and operates according to the SS1 configuration for each motion safety instance. |
| Connection Loss Action | • The loss could also be an indication of excessive traffic causing the drive                                                                                         | STO       | Torque is removed from the associated axis according to the STO configuration of each motion safety instance.                     |
| Connection Idle Action | Connection Idle is caused by the safety output task becoming disabled because the controller is in Remote Program mode.                                               | SS1       | Drive-based Safe Stop 1 instruction is initiated and operates according to the SS1 configuration for each motion safety instance. |
| Connection Idle Action |                                                                                                                                                                       | STO       | Torque is removed from the associated axis according to the STO configuration of each motion safety instance.                     |
| Restart Type           | Restart type means that the safety function resets and will be ready for subsequent operation when the request is removed. See specific function for more detail.     | Automatic | Automatic is the only choice.(1)                                                                                                  |
| Cold Start Type        | Cold start type means that the configured safety function is ready for operation immediately after the controller enters run mode.                                    | Automatic | Automatic is the only choice. (1)                                                                                                 |

2. From the Connection Loss Action and Connection Idle Action pull-down menus, choose SS1 or STO as required for your application.
3. Click Apply.

## Motion Safety&gt;Primary Feedback Category

Configure primary feedback if you intend to use any drive-based or controllerbased safety function that monitors motion. There are many different combinations of feedback for motion control and safety that can be configured. See Table 24 on page 62 for single feedback instances where only primary feedback is configured. See Table 24 on page 62 for dual feedback instances that require a primary and secondary feedback configuration.

Follow these steps to configure the Primary Feedback dialog box.

1. Select the Motion Safety 1&gt;Primary Feedback category.

## IMPORTANT

Only Kinetix VPL, VPF, VPH, and VPC motors, Kinetix MMA with -S2 or M2 encoder options, or VPAR electric cylinders, with -Q or -W encoder options are SIL 2 rated. Other motors can be selected, but will not support the SIL 2 rating.

<!-- image -->

2. From the Device pull-down menu, choose between the DSL Feedback Port and Universal Feedback Port. This is where the feedback device is wired to the drive.

<!-- image -->

<!-- image -->

3. From the Type pull-down menu, choose the feedback type.
2. These are the choices when DSL Feedback Port is chosen.

These are the choices when Universal Feedback Port is chosen.

4. Click Change Catalog and configure the same motor catalog number as done in Axis Properties for the Motion connection.

<!-- image -->

<!-- image -->

If you configure the Axis Properties&gt;Motor category with the VPC-Bxxxx-Q motor, that is for the Motion connection. In this Safety connection example, the primary feedback is the same Kinetix VPC motor, with the same -Q encoder.

5. Click Apply.

Because this example includes a -Q (SIL 2) encoder, the Device pull-down menu is pre-populated with DSL Feedback 1 Port and the Type is Hiperface DSL. The Primary Feedback category is also where you configure the Velocity Average Time and Standstill Speed attributes.

6. Set the remaining Primary Feedback attributes.

|                       | Attribute Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       | Units Default value is revolutions (Rev) that supports rotary motors.                                                                                                                                                                                                                                                                                                                                                                                                   |
|                       | Resolution Units Default value is Cycles/Revolution (Rev).                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cycle Resolution      | Used in the Effective Resolution calculation. The actual motor encoder cycle resolution. This is the raw encoder cycle resolution of the motor or encoder device type. For example, when DSL Hiperface (VPC-Bxxxx-Q motors) is the chosen primary feedback Type, the value is 4096 cycles/rev. VPL-B063xxx and VPL-B075xxx motors have 512 cycle resolution.                                                                                                            |
| Cycle Interpolation   | Used in the Effective Resolution calculation. The safety primary-feedback interpolated counts as oppose to the motion axis-feedback interpolated counts. For DSL encoders this value is 1. For sin/cos encoders this value is 4.                                                                                                                                                                                                                                        |
| Effective Resolution  | The product of cycle resolution and cycle interpolation for the primary safety function evaluation.                                                                                                                                                                                                                                                                                                                                                                     |
| Polarity              | Based on encoder rotation and evaluation requirements. Choose between Normal (default) or Inverted as appropriate for your application. Normal Normal Inverted                                                                                                                                                                                                                                                                                                          |
| SIL Capability        | Kinetix VP motors with -Q or -W, and Kinetix MMA motors with -S2 or -M2 types are SIL 2 capable and 2 is shown. For non SIL-rated motor or encoder, this field indicates Unknown.                                                                                                                                                                                                                                                                                       |
| Velocity Average Time | The velocity average time attribute is a moving-average window of time for which the velocity samples are averaged. A small value results in more deviation in the velocity evaluation. A large value results in less deviation in the velocity evaluation, but also adds more delay to the resulting evaluation.This delay should be considered with system requirements for over-speed response. See Velocity Average Time Parameter on page 42 for more information. |
| Standstill Speed      | Used in the safe-monitoring process to indicate to the safety controller that the motor has stopped rotating. The system is at standstill when the speed detected is less than or equal to the configured Standstill Speed. This parameter sets the speed at which module:SI.MotionPositive[instance] or module:SI.MotionNegative[instance] tags are set in the safety input assembly.                                                                                  |

7. Click Apply.

## Velocity Average Time Parameter

The Velocity Average Time parameter sets the time period for a moving average filter that is applied to velocity samples reported in Velocity Feedback.

The Velocity Average Time is important for 2 reasons:

1. For low resolution encoders there is not enough shaft movement between position samples to allow for a smooth velocity signal. Instead it will jump between zero and a higher value than the actual velocity. This determines the minimum velocity that can be resolved and used in the safety application.
2. The safety input connection cycle time or input RPI may be slow compared to changes in the velocity signal. If the velocity changes several times between these Input Assembly updates to the drive, then all of the changes will not be seen at the safety controller. This is known as aliasing. Aliasing has the potential to report velocities that are different from the actual velocity. To avoid aliasing set Velocity Average Time parameter to greater than the safety input connection RPI time.

The motion safety instance of the drive calculates velocity by taking the differences in position count samples that are divided by the sample period. The safety feedback position and velocity, in the motion safety instance, are updated every 3 ms.

Velocity average time determines the number of most recent velocity samples that are averaged. The number of samples averaged is given by the Velocity Average Time/3 ms. Any remainder is truncated. At low velocities with lowresolution encoders, the encoder shaft position does not have enough movement for a change in the encoder output with each sample. This results in delta positions of zero followed by a position increment of one count. The reported velocity in this case jumps between zero and a large value. On average, the velocity is correct.

Large velocity fluctuations are avoided by averaging velocity samples. Figure 15 on page 43 shows the relationships between the encoder cycles, counts, sample points, velocity with no averaging, and averaging. The figure also shows that as the averaging time is increased, the effective velocity resolution is improved. However, with higher resolution comes a longer delay in reporting the velocity due to the N point average. To determine the Velocity Average Time for a given encoder and Velocity Resolution, use the following equation.

<!-- image -->

Where:

- Velocity Average Time is in seconds.
- Velocity Resolution is in RPM (Revolutions Per Minute).

- Encoder Cycle Count is the number of cycles per revolution.
- For motors with Q type feedback, the count is 4096 cycles.
- For motors with W type feedback, the count is 512 cycles.
- For motors with sin/cos feedback the number of sinusoidal cycles per revolution. For example:
- a. For MPL motors with V type feedback, the count is 128 cycles.
- b. For MPL motors with M type feedback, the count is 1024 cycles.
- c. For Kinetix MMA motors with M2 type feedback, the count is 128 cycles.
- Encoder interpolation is either 4 or 1.
- For motors with Q or W type feedback, the value is 1.
- For motors with Sin/Cos feedback, the value is 4 (Figure 15 shows interpolation with Sin/Cos signals).

For velocity average time in the equation, use the following conversion for the value entered:

| Average Time Setting in Studio 5000 Logix Designer Effective Value   |
|----------------------------------------------------------------------|
| 0…5 ms 3 ms                                                          |
| 6…8 ms 6 ms                                                          |
| 9…11 ms 9 ms                                                         |
| 12…14 ms 12 ms                                                       |

and so on…(1)

(1) Effective Value = (floor(Average Time Setting ÷ 3 ms)) · 3 ms. Floor(x) is the greatest integer ≤ x.

Figure 15 - Encoder Sampling and Velocity

<!-- image -->

This table shows different values of velocity resolution based on the encoder cycle count and the velocity average time.

Table 22 - Velocity Resolution vs Velocity Average Time for Different Interpolated Encoder Cycle Counts

| Velocity Resolution                             | Velocity Resolution                                        | Velocity Resolution   |
|-------------------------------------------------|------------------------------------------------------------|-----------------------|
| Interpolated Count Velocity Average Time 100 ms | Velocity Average Time 500 ms Velocity Average Time 1000 ms |                       |
| 64 9.375 rpm 1.875 rpm 0.9375 rpm               |                                                            |                       |
|                                                 | 512 1.171875 rpm 0.234375 rpm 0.117188 rpm                 |                       |
|                                                 | 2048 0.292969 rpm 0.058594 rpm 0.029297 rpm                |                       |
|                                                 | 4096 0.146484 rpm 0.029297 rpm 0.014648 rpm                |                       |

## Motion Safety&gt;Secondary Feedback Category

Configure secondary feedback for your motion monitoring application that requires SIL 3 or PL e for drive-based or controller-based safety functions. There are different combinations of feedback for motion control and safety that can be configured. See Table 24 on page 62 for dual feedback instances that require a primary and secondary feedback configuration.

IMPORTANT

For Motion Safety Dual Channel Feedback configurations, the primary feedback must be a SIL 2 rated encoder.

Secondary feedback devices are typically Sine/Cosine or EnDat Sine/Cosine outputs.

<!-- image -->

## IMPORTANT

The secondary feedback device cannot be the same as your primary feedback device. For example, if a Kinetix VPC (SIL 2, PL d) motor is used, the primary feedback device is the DSL Feedback Port and the secondary feedback device (if used) must be the Universal Feedback Port.

Configure polarity so that when the primary encoder position increments, the secondary encoder position increments too.

To configure the Secondary Feedback dialog box, see step 1 through step 6 beginning on page 40. Secondary feedback module properties have the same attributes and drop-down menus as the primary feedback category.

## Motion Safety&gt;Scaling Category

The Primary Feedback category set safety resolution in terms of counts per revolution. The Scaling category configures the position and time to be used in terms of counts per position unit in the safe monitoring functions.

Figure 16 - Scaling Category (default settings)

<!-- image -->

Table 23 - Scaling Category Attributes

<!-- image -->

|                     | Attribute Description                                                                                                                                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback Resolution | The number of counts per motor revolution, which is determined by the Primary Feedback category.                                                                                 |
|                     | Position Units The position units for this safety application. Enter text for the name of your units.                                                                            |
| Time                | The evaluation of position per unit of time for a velocity evaluation. Choose between Seconds (default) and Minutes as appropriate for your application. Seconds Seconds Minutes |
| Position            | The conversion constant showing the counts per position units. This is the number of counts for one of your position units.                                                      |

Refer to Scaling Example 1 on page 45 and Scaling Example 2 on page 46 to see how scaling is configured for two rotary knife applications.

## Scaling Example 1

In the following example, a rotary knife with one blade is directly coupled to the motor. The servo motor is a Kinetix VPC-Bxxxx-Q with SIL 2 encoder that generates 4096 counts per revolution.

<!-- image -->

Figure 18 - Scaling Example 1 Dialog Box

<!-- image -->

## Data summary for this scaling example:

- Kinetix VPC-Bxxxx-Q motor with DSL Hiperface encoder that generates 4096 counts per revolution
- Units = Knife Revolutions (one revolution evaluated in seconds)

<!-- image -->

## Scaling Example 2

In this example, a rotary knife with two blades is driven by a 10:1 gear reduction and servo motor. The servo motor is a Kinetix VPC-Bxxxx-Q with SIL 2 encoder that generates 4096 counts per revolution.

<!-- image -->

Figure 20 - Scaling Example 2 Dialog Box

<!-- image -->

## Data summary for this scaling example:

- Kinetix VPC-Bxxxx-Q motor with DSL Hiperface encoder that generates 4096 counts per revolution
- Motor connects with a 10:1 gear reduction to drive the knife blades
- Units = Knife Cuts (two cuts per load revolution evaluated in seconds)
- Secondary encoder used to improve safety rating

<!-- image -->

## Motion Safety&gt;Discrepancy Checking Category

Discrepancy checking is only used in applications where the Module Definition&gt;Safety Instance is configured for Dual Feedback Monitoring. Its purpose is to perform an evaluation of the speed discrepancy between primary and secondary feedback. Primary Feedback is used for safe monitoring functions. Secondary feedback is used for fault diagnostics.

If primary feedback and secondary feedback differ in the velocity deadband value for longer than the time entry, a velocity discrepancy fault occurs.

Figure 21 - Discrepancy Checking Dialog Box (default attributes)

<!-- image -->

## IMPORTANT

When setting discrepancy tolerances in terms of the velocity deadband attribute, consider that configuring a high gear-ratio between primary feedback and secondary feedback can lead to unexpected dual-feedback position faults. This is because a very large primary feedback movement translates into very small secondary feedback increments.

When Module Definition&gt;Safety Instance is configured for Single Feedback Monitoring, use the No Check (default) setting.

Follow these steps to configure the Discrepancy Checking attribute.

1. From the Mode pull-down menu, choose Dual Velocity Check.

<!-- image -->

Use Dual Velocity Check to measure the difference between primary feedback speed and secondary feedback speed to see if that tolerance is greater than the velocity deadband for more than the time tolerance.

2. Set the remaining Discrepancy Checking attributes.
3. Click Apply.

|                   | Attribute Description                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------|
| Time              | The amount of time (ms) specified for velocity deadband to be evaluated and trigger a safety fault condition. |
| Ratio             | The gear ratio of one primary feedback revolution to one secondary feedback revolution.                       |
| Velocity Deadband | The velocity units of the difference between primary and secondary feedback speed for the discrepancy check.  |

Discrepancy Checking Example

This example uses Scaling Example 2 on page 46 to show how discrepancy checking is used to measure the speed discrepancy between primary and secondary feedback and avoid dual-feedback position faults.

Figure 22 - Discrepancy Checking Example

<!-- image -->

Data summary for this scaling example:

- The primary feedback encoder is rotating at 600 rpm
- Hence, the secondary feedback encoder is rotating at 60 rpm (10:1 gear reduction)
- Time = 1000 ms

To calculate the secondary feedback speed:

<!-- formula-not-decoded -->

Primary encoder feedback speed is calculated in the same safety units, but rotating at 20 knife cuts/s.

If primary versus secondary feedback speed differs by more than the Velocity Deadband value (0.1 knife cuts/s), for the Time (1000 ms) duration, a velocity discrepancy fault occurs.

## Motion Safety&gt;STO Category

The STO category provides a disable and coast fault action. However, if a torque disable delay is needed following STO Active, you can enter a value in the Delay field.

<!-- image -->

The STO Delay feature is also available with 2198-xxxx-ERS3 (series B or later) drives when the Module Definition is configured for Safe Stop Only - No Feedback.

STO Output is a tag in the safety output assembly, used to activate the STO function, and is written by the GuardLogix controller. When any source for STO is asserted, STO Active becomes high to indicate that the STO function is operating.

Figure 23 - Motion Safety STO

<!-- image -->

STO becomes active if any of the following inputs to STO are asserted:

- STO Output = 0
- Safety Connection Loss and Connection Loss Action = STO
- Safety Connection is Idle and Connection Idle Action = STO
- Drive-based SS1 Function is Complete (= 1)
- Safety Stop Fault = 1
- Critical Safety fault occurs

See Safe Stop Function attribute 265 (STO Activation) on page 90 .

STO Delay follows this sequence of events.

1. STO becomes active and the STO delay timer begins.
2. The STO delay timer expires.

Torque producing power is removed from the inverter output.

- If STO is activated by a Safety Stop fault or Critical Safety fault, torque is removed immediately without the STO delay.

- If STO is reset by removing all inputs, torque is immediately permitted without delay.

## Motion Safety&gt;SS1 Category

The Motion Safety&gt;SS1 category is configured when a Timed or Monitored Safe Stop 1 (SS1) function is desired.

<!-- image -->

Timed SS1 is also available with 2198-xxxx-ERS3 (series B or later) drives when the Module Definition is configured for Safe Stop Only - No Feedback.

Timed SS1 mode is the default setting. Monitored SS1 and Not Used are also available.

Figure 24 - SS1 Dialog Box (Timed SS1, default)

<!-- image -->

<!-- image -->

Timed SS1 is a fixed time for the motor to stop before removing torque. Motor feedback is not monitored. Stop Delay is the only parameter used for Timed SS1 and determines the Max Stop Time.

Figure 25 - SS1 Dialog Box (Monitored SS1)

<!-- image -->

Monitored SS1 is a ramped safe-stop where the motion safety instance monitors the speed ramp to standstill speed, while either the motion task or the drive controls the deceleration to standstill speed. When standstill is reached, the motion safety instance removes torque from the motor.

## Primary Safety Feedback Example (DSL SIL 2 encoder)

...Artionc

This example applies to any Kinetix 5700 (2198-xxxx-ERS4) inverter that is paired with Kinetix VPL, VPF, VPH, or VPC motors or Kinetix VPAR electric cylinders that are equipped with -Q or -W (SIL 2, PL d rated) encoders.

This example assumes you have configured the 2198-xxxx-ERS4 drive as a motion and safety connection and configured the motion associated axis for specific motion functions. To review these categories, see Understand Module Properties Categories on page 33 .

## IMPORTANT

This example assumes you have evaluated the system safety requirements through a risk assessment and that a Monitored SS1 action is configured in the event of an Ethernet connection loss or the controller being switched to remote program mode.

Figure 26 - Module Definition for Motion and Safety (single feedback monitoring)

<!-- image -->

Follow these steps to configure primary feedback for Kinetix VPC-Bxxxx-Q motors.

1. In the Controller Organizer, right-click the 2198-xxxx-ERS4 inverter and choose Properties.
2. Select the Motion Safety 1&gt;Actions category.
3. From the Connection Loss Action and Connection Idle Action pull-down menus, choose SS1 (default).

<!-- image -->

In this example, SS1 settings are used.

STO

## IMPORTANT

4. Click Apply.
5. Select the Motion Safety 1&gt;Primary Feedback category.
6. From the Device pull-down menu, choose DSL Feedback Port because the motion connection is associated with a VPC-Bxxxx-Q motor.
4. VPC-Bxxxx-Q motors are not available on the Universal Feedback Port.
7. Click Change Catalog.
6. The Change Catalog Number dialog box appears.
8. Select the motor catalog number appropriate for your SIL 2 application. To verify the motor catalog number, refer to the motor name plate.
9. Click OK to close the Change Catalog Number dialog box.

<!-- image -->

<!-- image -->

<!-- image -->

The SS1 action only occurs with a connection loss or connection idle fault. If a safety or other motion fault occurs, consult the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 to determine the appropriate action to take.

10. Set the Velocity Average Time and Standstill Speed attributes. In this example, the Velocity Average Time is set to 100 ms and the Standstill Speed is set to 1.000 rev/s (default setting). For calculations, see V Velocity Average Time Parameter on page 42 . This parameter sets the speed at which module:SI.MotionPositive [instance] or module:SI.MotionNegative [instance] tags are set in the safety input assembly.

11. From the Polarity pull-down menu, choose Normal (default) or Inverted as appropriate for your application.
12. Click Apply.
13. Select the Motion Safety 1&gt;Scaling category.
14. In the Position Units field, type revolutions.

<!-- image -->

In this application, the position units are in revolutions. 1 motor revolution = 1 revolution.

15. Select the Axis Properties&gt;Scaling category.
16. Click Apply.

Both the Motion Safety and Axis Properties&gt;Scaling (motion) categories match as shown.

<!-- image -->

<!-- image -->

## 17. Select the Motion Safety 1&gt;SS1 category.

18. From the Mode pull-down menu, choose the SS1 - Safe Stop 1 mode. In this example, a Monitored SS1 is used to monitor the deceleration rate and tolerance.
19. Enter the Stop Monitor, Stop Delay, Decel Reference, Decel Speed, and Standstill values.

In this example, the values are as shown. For more about making calculations see Figure 25 on page 50 .

20. Click Apply.
21. If Motion Safety 2 categories requires configuring Axis B of your dualaxis inverter, repeat step 1 through step 20 .

This example applies to any Kinetix 5700 (2198-xxxx-ERS4) inverter that is paired with Kinetix VPL, VPF, VPH, or VPC motors that are equipped with -Q or -W (SIL 2, PL d rated) encoders. In this example, the application has an external Bulletin 842HR sin/cos encoder for dual feedback monitoring.

This example assumes you have configured the 2198-xxxx-ERS4 drive as a motion and safety connection and configured the motion associated axis for specific motion functions. To review these categories, see Understand Module Properties Categories on page 33 .

## IMPORTANT

This example assumes you have evaluated the system safety requirements through a risk assessment and that a Monitored SS1 action is configured in the event of a safety connection loss or the controller being switched to program mode.

## Dual Feedback Monitoring Example (DSL SIL 2 encoder)

Figure 27 - Module Definition for Motion and Safety (dual feedback monitoring)

<!-- image -->

Follow these steps to configure primary feedback for a Kinetix VPC-Bxxxx-Q motor with an external Bulletin 842HR sin/cos encoder for dual feedback monitoring.

1. In the Controller Organizer, right-click the 2198-xxxx-ERS4 inverter and choose Properties.
2. Select the Motion Safety 1&gt;Actions category.
3. From the Connection Loss Action and Connection Idle Action pull-down menus, choose SS1 (default).

<!-- image -->

In this example, SS1 settings are used.

IMPORTANT

The SS1 action only occurs with a connection loss or connection idle fault. If a safety or other motion fault occurs, consult the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 to determine the appropriate action to take.

4. Click Apply.

5. Select the Motion Safety 1&gt;Primary Feedback category.
6. From the Device pull-down menu, choose DSL Feedback Port because the motion connection is associated with a VPC-Bxxxx-Q motor.

<!-- image -->

## IMPORTANT

Because this safety configuration is using the DSL Feedback Port, the motion configuration (if used with this port) must use the same device with this port.

7. Click Change Catalog.

The Change Catalog Number dialog box appears.

<!-- image -->

8. Select the motor catalog number appropriate for your SIL 2 application. To verify the motor catalog number, refer to the motor name plate.
9. Click OK to close the Change Catalog Number dialog box.
10. Set the Velocity Average Time and Standstill Speed attributes.

<!-- image -->

In this example, the Velocity Average Time is set to 100 ms and the Standstill Speed is set to 1.000 rev/s (default setting). For calculations, see V Velocity Average Time Parameter on page 42 .

- This parameter sets the speed at which module:SI.MotionPositive [instance] or module:SI.MotionNegative [instance] tags are set in the safety input assembly.
11. From the Polarity pull-down menu, choose Normal (default) or Inverted as appropriate for your application.
12. Click Apply.
13. Select the Motion Safety 1&gt;Secondary Feedback category.
14. From the Device pull-down menu, choose Universal Feedback Port. In this example, the Bulletin 842HR sine/cosine encoder is used, which requires the 15-pin UFB connector.

<!-- image -->

## IMPORTANT

Because this safety configuration is using the Universal Feedback Port, the motion configuration (if used with this port) must use the same device with this port.

15. From the Type pull-down menu, choose Sine/Cosine and enter 1024 (default) in the Cycle Resolution field, which is required for the Bulletin 842HR encoder.
16. Set the Velocity Average Time and Standstill Speed attributes.

In this example, the Velocity Average Time is set to 100 ms and the Standstill Speed is set to 1.000 rev/s (default setting). For calculations, see V Velocity Average Time Parameter on page 42 .

<!-- image -->

The Standstill Speed attribute for secondary feedback is not used by the drive safety instance safety functions and does not affect the input assembly motion positive or motion negative bits. Only secondary feedback motion status bits are affected by this attribute. See Table 41 on page 86 for safety attributes.

17. From the Polarity pull-down menu, choose Normal (default) or Inverted as appropriate for your application.

18. Select the Motion Safety 1&gt;Scaling category.
19. In the Position Units field, type revolutions.
3. In this application, the position units are in revolutions. 1 motor revolution = 1 revolution.
20. Select the Axis Properties&gt;Scaling category.
21. Click Apply.
22. Select the Motion Safety 1&gt;SS1 category.
23. From the Mode pull-down menu, choose the SS1 - Safe Stop 1 mode. In this example, Monitored SS1 is used to control the deceleration rate and tolerance.

<!-- image -->

Both the Motion Safety and Axis Properties&gt;Scaling (motion) categories match as shown.

<!-- image -->

<!-- image -->

## Primary Safety Feedback Example (Hiperface or Hiperface SIL 2 encoder)

24. Enter the Stop Monitor, Stop Delay, Decel Reference, Decel Speed, and Standstill values.

In this example, the values are as shown. For more about making calculations see Figure 25 on page 50 .

25. Click Apply.
26. If Motion Safety 2 categories require configuration of your dual-axis inverter, repeat step 1 through step 25 .

This procedure applies to any Kinetix 5700 (2198-xxxx-ERS4) inverter where the Motion Only connection is controlled by one Logix 5000 controller and the Safety Only connection is controlled by another GuardLogix controller. In this example, the Kinetix 5700 inverter is paired with an Kinetix MPL-Bxxxx-M (multi-turn) motor, or Kinetix MMA motors with SIL 2 rated encoders.

This procedure assumes you have already configured the 2198-xxxx-ERS4 drive with a Motion Only connection and configured the motion associated axis for specific motion functions. To review these categories, see Understand Module Properties Categories on page 33 .

## IMPORTANT

This procedure assumes you have evaluated the system safety requirements through a risk assessment and that a Monitored SS1 action is taken in the event of a safety connection loss or the controller being switched to program mode.

Figure 28 - Module Definition for Safety Only (single feedback monitoring)

<!-- image -->

Follow these steps to configure primary feedback for the Safety Only connection with a Kinetix MPL-Bxxxx-M motor.

1. In the Controller Organizer, right-click the 2198-xxxx-ERS4 inverter and choose Properties.

2. Select the Motion Safety 1&gt;Actions category.
3. From the Connection Loss Action and Connection Idle Action pull-down menus, choose SS1 (default).

<!-- image -->

In this example, the SS1 setting is used.

## IMPORTANT

The SS1 action only occurs with a connection loss or connection idle fault. If a safety or other motion fault occurs, consult the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 to determine the appropriate action to take.

4. Click Apply.
5. Select the Motion Safety 1&gt;Primary Feedback category.
6. From the Device pull-down menu, choose the Univeral Feedback Port.
7. From the Type pull-down menu, choose Hiperface because the motion connection is associated with an MPL-Bxxxx-M motor.
8. Enter a value in the Cycle Resolution field. 1024 Cycles/rev is the default value when Hiperface is the encoder type.
9. Set the Velocity Average Time and Standstill Speed attributes. In this example, the Velocity Average Time is set to 100 ms and the Standstill Speed is set to 1.000 rev/s (default setting). For calculations, see V Velocity Average Time Parameter on page 42 .
10. From the Polarity pull-down menu, choose Normal (default) or Inverted as appropriate for your application.
11. Click Apply.

<!-- image -->

12. Select the Motion Safety 1&gt;Scaling category.
13. In the Position Units field, type revolutions.
3. In this application, the position units are in revolutions. 1 motor revolution = 1 revolution.
14. Select the Axis Properties&gt;Scaling category.

<!-- image -->

<!-- image -->

The Motion Safety&gt;Scaling and Axis Properties&gt;Scaling (motion) categories match as shown.

15. Click Apply.
16. Select the Motion Safety 1&gt;SS1 category.
17. From the Mode pull-down menu, choose the SS1 - Safe Stop 1 mode. In this example, a Monitored SS1 is used to control the deceleration rate and tolerance.
18. Enter the Stop Monitor, Stop Delay, Decel Reference, Decel Speed, and Standstill values.

<!-- image -->

In this example, the values are as shown. For more about making calculations see Figure 25 on page 50 .

## Encoder Feedback Types and SIL Ratings

19. Click Apply.
20. If Motion Safety 2 categories requires configuring Axis B of your dualaxis inverter, repeat step 1 through step 19 .

Use encoder feedback for motion control, safety motion monitoring, or both. The drive must be configured to use a feedback device for motion and/or for safety. The motion and safety functions in the drive are independent with respect to the encoder feedback. For SIL 2 PL d safety applications, a single encoder can be used. The encoder for SIL 2 applications has restrictions. Table 24 shows how different feedback types can be used with a drive to achieve the desired motion control and safety for SIL 2 PL d applications.

For SIL 3 PL e applications, two encoders must be used. One of the encoders must be a SIL 2 rated Hiperface DSL encoder provided in a Kinetix VPL, VPF, VPH, or VPC servo motor. The secondary encoder must be a Sin/Cos type that meets specific requirements for diagnostic coverage. Table 24 shows feedback types that can be used for motion and SIL 3 PL e safety applications.

Table 24 - Feedback Types Assigned to Feedback Ports for SIL 2 and PL d Applications

| Motor Feedback (MF) Connector (1)                                                                                      | Motor Feedback (MF) Connector (1)   | Motor Feedback (MF) Connector (1)    | Universal Feedback (UFB) Connector (1)                                               | Universal Feedback (UFB) Connector (1)   | Universal Feedback (UFB) Connector (1)      | Achievable System Safety Rating                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encoder Source                                                                                                         | Encoder Safety Function             | Encoder Motion Function              | Encoder Source                                                                       | Encoder Safety Function                  | Encoder Motion Function                     |                                                                                                                                                       |
| VPL-Bxxxxx-Q VPL-Bxxxxx-W VPF-Bxxxxx-Q VPF-Bxxxxx-W VPH-Bxxxxx-Q VPH-Bxxxxx-W VPC-Bxxxxx-Q VPAR-Bxxxxx-Q VPAR-Bxxxxx-W |                                     | Primary Motor feedback               | • No encoder • Any encoder supported by the drive                                    | Not used                                 | • None • 1/2 axis • Dual-loop load feedback | Single Channel SIL 2/PL d                                                                                                                             |
| VPL-Bxxxxx-C VPL-Bxxxxx-P VPF-Bxxxxx-C VPF-Bxxxxx-P VPH-Bxxxxx-C VPAR-Bxxxxx-C                                         |                                     | Not used Motor feedback              | Any Sin/Cos encoder compatible with drive                                            | Primary                                  | • None • 1/2 axis • Dual-loop load feedback | • Single Channel SIL 2/PL d for rated encoders. • PLd according to machinery safety standard and additional (customer-supplied) safety measures.  (3) |
| MMA-Bxxxxxx                                                                                                            |                                     | Not used Not used                    | • MMA-Bxxxxxx-S2 • MMA-Bxxxxxx-M2                                                    |                                          |                                             | Primary Motor Feedback • Single channel SIL 2/PLd.                                                                                                    |
| Hiperface-to-DSL Converter kit with motor and Hiperface Sin/Cos encoder                                                |                                     | Not used Motor feedback              | Any Sin/Cos encoder compatible with drive                                            | Primary                                  | • None • 1/2 axis • Dual-loop load feedback | • Single Channel SIL 2/PL d for rated encoders. • PL d according to machinery safety standard and additional (customer supplied) safety measures.  (2)                                                                                                                                                       |
| Hiperface-to-DSL Converter kit with stand-alone Hiperface encoder                                                      | Not used                            | • 1/2 axis • Dual-loop load feedback | • Any Sin/Cos encoder compatible with drive • Hiperface encoder on Kinetix MP motors |                                          | Primary Motor Feedback                      | • PL d according to machinery safety standard and additional (customer supplied) safety measures.  (3) • Applies to Kinetix MP motors with -M and -S encoder option.                                                                                                                                                       |

Table 24 - Feedback Types Assigned to Feedback Ports for SIL 2 and PL d Applications (Continued)

| Motor Feedback (MF) Connector (1)   | Motor Feedback (MF) Connector (1)   | Motor Feedback (MF) Connector (1)   | Universal Feedback (UFB) Connector (1)                       | Universal Feedback (UFB) Connector (1)   | Universal Feedback (UFB) Connector (1)   | Achievable System                                                                                                                             |
|-------------------------------------|-------------------------------------|-------------------------------------|--------------------------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Encoder Source                      | Encoder Safety Function             | Encoder Motion Function             | Encoder Source                                               | Encoder Safety Function                  | Encoder Motion Function                  | Safety Rating (Continued)                                                                                                                     |
| No encoder Not used Not used        |                                     |                                     | • SIL 2 Safety rated Sin/ Cos encoder compatible with drive(3) (4)(5)                                                              |                                          | Primary Motor Feedback                   | • Single Channel SIL 2/PL d for rated encoders according to machinery safety standard and additional (customer supplied) safety measures. (2) |
| No encoder Not used Not used        |                                     |                                     | • Any Sin/Cos encoder compatible with driver (3) (4) (5) (6) |                                          | Primary Motor Feedback                   | • PL d according to machinery safety standard and additional (customer supplied) safety measures.  (2) • Applies for Kinetix MP motors with -M and -S encoder options.                                                                                                                                               |

Table 25 - Feedback Types Assigned to Feedback Ports for SIL 3/PL e Applications

| Motor Feedback (MF) Connector (1)                                                                                      | Motor Feedback (MF) Connector (1)   | Motor Feedback (MF) Connector (1)   | Universal Feedback (UFB) Connector (1)                               | Universal Feedback (UFB) Connector (1)   | Universal Feedback (UFB) Connector (1)      | Achievable System Safety Rating   |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------------------------------------|----------------------------------------------------------------------|------------------------------------------|---------------------------------------------|-----------------------------------|
| Encoder Source                                                                                                         | Encoder Safety Function             | Encoder Motion Function             | Encoder Source                                                       | Encoder Safety Function                  | Encoder Motion Function                     |                                   |
| VPL-Bxxxxx-Q VPL-Bxxxxx-W VPF-Bxxxxx-Q VPF-Bxxxxx-W VPH-Bxxxxx-Q VPH-Bxxxxx-W VPC-Bxxxxx-Q VPAR-Bxxxxx-Q VPAR-Bxxxxx-W |                                     | Primary Motor Feedback              | Any Sin/Cos encoder compatible with drive (includes Hiperface  (2) ) | Secondary                                | • None • 1/2 axis • Dual-loop load feedback | Dual Channel SIL 3/PL e (3)       |

## Notes:

## Drive Safety Instructions

## Controller-based Safety Functions

Use this chapter to become familiar with the GuardLogix® controller-based Drive Safety instructions and how they interact with the Kinetix® 5700 dualaxis and single-axis inverters.

| Topic                     |   Page |
|---------------------------|--------|
| Drive Safety Instructions |     65 |
| Pass-through Data         |     68 |
| SFX Instruction           |     69 |

Refer to the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095, for more information on the Drive Safety
Ü p
instructions and TÜV Rheinland certification.

The Drive Safety instructions are designed to work with the 2198-Dxxx-ERS4 dual-axis inverters and 2198-Sxxx-ERS4 single-axis inverters. They are available in the Studio 5000 Logix Designer® application, version 31.00 or later, under the Drive Safety tab when a Safety Task routine is active.

Controller-based safety functions operate in GuardLogix 5580 or Compact GuardLogix 5380 controllers and use the EtherNet/IP™ network to communicate with the safety I/O. Drive Safety instructions use safety feedback, provided by Kinetix 5700 drives in the Safety Task of the controller, to preform safe monitoring functions.

| Safety Instruction            | Safety Instruction   | Description                                                                                                                                                                                                                                   |
|-------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Feedback Interface SFX |                      | The SFX function scales feedback position into position units and feedback velocity into position units per time unit. SFX is used with other Drive Safety instructions.SFX also provides unwind for rotary applications and position homing. |
| Safe Stop 1                   | SS1                  | The SS1 function monitors the motor deceleration rate within set limits during motor stopping and provides an indication to initiate safe torque-off (STO) function when the motor speed is below the specified limit.                        |
| Safe Stop 2                   | SS2                  | The SS2 function monitors the motor deceleration rate within set limits during motor stopping and initiates the safe operating stop (SOS) function when the motor speed is below the specified limit.                                         |
| Safe Operational Stop SOS     |                      | The SOS function prevents the motor from deviating more than a defined amount from the stopped position.                                                                                                                                      |
| Safely Limited Speed SLS      |                      | The SLS function prevents the motor from exceeding the specified speed limit.                                                                                                                                                                 |
| Safely Limited Position SLP   |                      | The SLP function prevents the motor shaft from exceeding the specified position limits.                                                                                                                                                       |
| Safe Direction                | SDI                  | The SDI function prevents the motor shaft from moving in the unintended direction.                                                                                                                                                            |
| Safe Brake Control SBC        |                      | The SBC function provides safe output signals to control an external brake.                                                                                                                                                                   |

Table 26 - Drive Safety Instructions

<!-- image -->

Figure 29 - Drive Safety Tab and Instructions

<!-- image -->

## Before Adding the Safety Instructions

Before adding Drive Safety instructions to your Logix Designer application, you must perform the following:

1. Add the 2198-xxxx-ERS4 drive module to the I/O Configuration folder, set Safety Application as Networked, set Connection as either Motion and Safety or Safety Only and set Motion Safety Feedback as required for your application.
2. Configure drive module Motion Safety instance.
3. Add and configure an axis in the Motion Group.

<!-- image -->

<!-- image -->

<!-- image -->

- For help with these Logix Designer configuration examples (steps 1 , 2 , and 3), see the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 .
4. Configure the Safety Actions in the axis property action tab. Refer to the Safety Actions section in Chapter 7 of the Kinetix 5700 Servo Drives User Manual, publication 2198-UM002 .
5. Add Drive Safety instructions to your Safety Task safety program.

## Drive Safety Instruction Example

Drive Safety instructions provide the following information. In this example, the Safely Limited Speed (SLS) instruction is shown.

Figure 30 - SLS Drive Safety Instruction

<!-- image -->

Table 27 - Drive Safety Instruction Definitions

| Instruction Information   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           | Configurable Inputs Safety function parameters used to define how the safety function operates.                                                                                                                                                                                                                                                                                                                                                                       |
| Inputs                    | • Feedback SFX is the link to the SFX instruction for an axis. • Request initiates the safe monitoring function. • Reset initiates a safety instruction reset.                                                                                                                                                                                                                                                                                                        |
| Pass Through              | Safety Output assembly object tags pass safety function status information from the Safety Task of the safety controller to the safety instance of the drive module. The status is made available to the motion controller.                                                                                                                                                                                                                                           |
| Outputs                   | • Fault Type is the instruction fault code that indicates the type of fault that occurred. • Diagnostic Code provides additional details on the fault. • O1 - Output 1 indicates the status of the instruction. When ON (1), it indicates that the input conditions are satisfied. • RR- Reset Required indicates when a reset is needed to restart the instruction or to clear faults. • FP - Fault Present indicates whether a fault is present in the instruction. |

## Pass-through Data

The Drive Safety instructions provide safety function monitoring in the Safety Task of the controller. Control of the drive is done in the motion programming within the Standard Task of the controller. For the motion program to receive status information from the Drive Safety instruction, tag data in the output assembly for the drive module (Safety Task) are passed to the drive and then to the corresponding tag in the axis structure (Standard Task).

This is especially useful when the motion program is in a separate controller from the safety program that is in a safety controller. Figure 31 shows how this works for the SLS instruction.

## IMPORTANT

Pass-through data is for status information only and does not impact configured safety functions.

<!-- image -->

ATTENTION: Tags used for the safety pass through attributes of instructions should only be used once. Re-use of the pass through tag in other instructions can cause unintended operation. This may result in damage to equipment or personal injury.

Figure 31 - Pass Through Data Path

<!-- image -->

Table 28 - SLS Tag Information

| Safety Output Assembly Tag    | Axis Tag             |
|-------------------------------|----------------------|
| module:SO.SLSActive[instance] | Axis.SLSActiveStatus |
| module:SO.SLSLimit[instance]  | Axis.SLSLimitStatus  |
| module:SO.SLSFault[instance]  | Axis.SLSFault        |

<!-- image -->

The words module , instance, and axis (italic) in these tag names represent the module, instance, and axis name assigned in the Logix Designer application.

The following steps correspond to the activity in Figure 31 .

1. Safety device reports a request to the safety zone. Initiates monitoring by the SLS instruction (Safety Task).
2. SLS Active status is passed to the motion program (Safety Task to Standard Task via the drive).

## SFX Instruction

3. The motion program adjusts the drive's speed to below the SLS Active Limit during the Check Delay (Standard Task).
4. If the drive speed exceeds the SLS Active Limit (Safety Task) during SLS monitoring, the SLS Limit output is set.
- Optionally, a stopping safety function can be initiated within the safety program.

The Safety Feedback Interface (SFX) instruction scales feedback position into position units and feedback velocity into speed units per unit of time. Feedback position and velocity are read from the safety input assembly and become inputs to the instruction. The SFX instruction also sets a reference position from a home input and performs position unwind in rotary applications.

The 2198-xxxx-ERS4 safe motion-monitoring drive provides safe position and velocity feedback. Up to SIL 3 PL e safety rating can be achieved by using dual feedback with velocity discrepancy checking. Up to SIL 2 PL d safety rating can be achieved by using single or dual feedback for functions that require position checking.

The outputs of the SFX instruction are used as inputs to other Drive Safety instructions. For any 2198-xxxx-ERS4 drive to execute a controller-based safety function, an SFX instruction is required. Although the SFX instruction is a safety instruction, it alone does not perform a safety function.

In Figure 32, the SS1 instruction uses the Actual Speed output from the SFX instruction during execution of the SS1 safety function.

Figure 32 - SFX Instruction Feeds Data to SS1 Instruction

<!-- image -->

## SFX Instruction Example

In this SFX example, a VPL-B0631T-W motor is used in the safety function. The motor has 512 feedback counts per motor revolution and is scaled for position to have 512 counts per motor revolution.

The SFX instruction scales the applicable safety instructions with feedback position units from the safety encoder/motor, into position feedback units used in applicable safety instructions. It also scales feedback velocity units from the safety encoder/motor into position feedback units per time unit.

## Scaling Setup

When configuring the SFX instruction, calculate the value for Position Scaling so that the Actual Position and Actual Speed output from the instruction matches the Actual Position and Actual Velocity in the motion controller.

Values from Axis Properties&gt;Scaling and Motion Safety&gt;Primary Feedback are required to calculate the instruction input.

The Feedback Resolution is determined based on the feedback device and the Effective Resolution of the feedback. This information is configured on the Module Properties&gt;Motion Safety&gt;Primary Feedback category.

Figure 33 - Effective Resolution Parameter

<!-- image -->

The VPL-B0631T-W motor is used in a rotary application where the unwind is set to rollover each motor revolution. Therefore, the unwind of 512 counts/rev was added in the SFX instruction appropriately.

Figure 34 - Scaling

<!-- image -->

## Homing

Setting the Actual Position output to the Home Position input (homing) of the instruction is required if using a position-based drive safety instruction like Safely-limited Position (SLP). If a position-based drive safety instruction is not being used on an axis, homing the SFX instruction is not required.

## IMPORTANT

Homing as described here is for the safety position and is not related to axis homing on the Motion Redefine Position (MRP) instruction.

The data in the Primary Feedback category, Scaling category, and motor unwind value is used to populate the SFX instruction.

Figure 35 - SFX Instruction Example

<!-- image -->

Refer to the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095, for more information on the Drive Safety instructions.

## Notes:

## Safety Fault Names

## Troubleshoot Safety Faults

This chapter provides troubleshooting tables and related information for Kinetix® 5700 drive systems that include 2198-Dxxx-ERS4 (dual-axis) and 2198-Sxxx-ERS4 (single-axis) inverters.

| Topic                    |   Page |
|--------------------------|--------|
| Safety Fault Names       |     73 |
| Understand Safety Faults |     74 |

The Motion Safety instance in the 2198-xxxx-ERS4 drive reports faults to the drive through the AxisSafetyFaults and AxisSafetyFaultsRA tags. Each bit in these tags indicates a specific fault. This information is used by the drive to log and display faults.

The Logix Designer application displays axis faults and status. When an axis is selected in the Controller Organizer, axis faults and status are displayed in the quick-view window.

Figure 36 - Axis Faults and Status

<!-- image -->

The safety faults named in Table 29 appear as Safety Faults when they occur. In addition, if any of these faults are present, a safety fault appears under the axis fault. Corresponding axis tags are set with any of the faults.

<!-- image -->

## Understand Safety Faults

Table 29 - Safety Fault Names

| Fault Name          | Description                                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
|                     | SafetyCoreFault Internal fault in the drive’s safety processor                                                        |
| STOFault            | A fault was detected by the Safe Torque-off function                                                                  |
| SS1Fault (1)        | A fault was detected by the Safe Stop 1 function                                                                      |
| SS2Fault            | A fault was detected by the Safe Stop 2 function                                                                      |
| SOSFault            | A fault was detected by the Safe Operating Stop function                                                              |
| SBCFault            | A fault was detected by the Safe Brake Control function                                                               |
| SLSFault            | A fault was detected by the Safe Limited Speed function                                                               |
| SDIFault            | A fault was detected by the Safe Direction function                                                                   |
| SLPFault            | A fault was detected by the Safe Limited Position function                                                            |
| SafetyFeedbackFault | The Safety processor has detected a problem with one or more of the safety feedback devices associated with the axis. |

To obtain more detailed information about any faults that are detected, most faults have a corresponding fault-type attribute. These attributes are read by using an MSG instruction in the ladder program to read the specific attribute information. Details of the various fault-type attributes are described in the following sections.

See Explicit Messages on page 18 for an example of using the MSG instruction to read status. See Motion Connection Axis Tags on page 81 for a list of attributes including fault information that can be read by using a MSG instruction.

## Safety Core Fault

The Motion Safety instance has detected a non-recoverable fault or internal error. When this happens, the Motion Safety instance reboots itself and attempts to re-establish normal operation.

## Safe Torque-off Fault

The safe torque-off (STO) function detected a fault. The safe stop function in the Motion Safety instance records the specific fault type in the attribute. Explicit messaging can be used to read the fault type information from the drive. For example, for STO Fault Type (Safe Stop Function [class code 0x5A], attribute ID 0x108). The drive immediately disables torque if an STO fault is detected.

Table 30 - Safe Torque-off Fault Type: MSG

| Parameter Value   | Description                                          |
|-------------------|------------------------------------------------------|
| Service Code 0x0E | Get attribute single                                 |
| Class  0x5A       | Safety stop functions                                |
| Instance 1 or 2   | Drive-module safety instance associated with an axis |
| Attribute 0x108   | STO fault type                                       |
| Data Type SINT    | Short integer                                        |

Table 31 - STO Fault Types

| STO Fault Type Value   | STO Fault Type Name Description               |                                                                                                                          |
|------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|                        | 0 Reserved Not used                           |                                                                                                                          |
| 1                      | No Fault                                      | No Fault is present                                                                                                      |
|                        | 2 Invalid Configuration                       | A safe stop function has been requested when it is not in the Ready state.                                               |
|                        | 3 Circuit Error                               | Safety diagnostics have detected an error in the hardwired STO input circuits.                                           |
|                        | 102 Hardwired Input Discrepancy               | The two STO hardwired input channels did not transition to the same state within the debounce time.                      |
| 104                    | Hardwired input active in Network Safety Mode | One or more hardwired STO inputs detected in the active state when the drive is configured for Network Safety operation. |

## Safe Stop 1 Fault

The safe stop 1 (SS1) function detected a fault. The safe stop function in the Motion Safety instance records the specific fault type in the attribute. Explicit messaging can be used to read the fault type information from the drive. For example, for SS1 Fault Type (Safe Stop Function object [class code 0x5A], safety instance 1 or 2, attribute ID 0x11C). The drive immediately disables torque, ignoring STO delay, if an SS1 fault is detected. If the SS1 Fault Type is reported as 1 (no fault), the SS1 fault was generated by the connected safety controller and reported to the drive over the safety connection.

Table 32 - SS1 Fault Types

| SS1 Fault Type Value  SS1 Fault Type Name Description   |                                                                                                                                                                              |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 Reserved Not used                                     |                                                                                                                                                                              |
| 1  No Fault                                             | No Fault is present                                                                                                                                                          |
| 2 Invalid Configuration                                 | The SS1 function has been requested when it has been configured as ‘not used’.                                                                                               |
| 3 Decel Rate error                                      | Applies only when SS1 is configured for Monitored SS1 mode. The SS1 function has detected that the feedback speed is not decelerating as fast as expected.                   |
| 4 Maximum Time exceeded                                 | Applies only when SS1 is configured for Monitored SS1 mode. The SS1 function has detected that the device has not reached standstill speed within the maximum stopping time. |
|                                                         | 100 STO Request Received An STO request was received during execution of the SS1 function.                                                                                   |
| 101 Feedback Invalid                                    | The Monitored SS1 function was requested when the associated safety feedback is not valid.                                                                                   |

## SS2, SOS, SBC, SLS, SLP, and SDI Faults

The Motion Safety instance in the 2198-xxxx-ERS4 drive does not support the SS2, SOS, SBC, SLS, SLP, and SDI safe stop/safety limit functions. If the drive reports one of these faults, then the fault was detected by the safety controller and reported to the drive over the safety output connection. Additional information for these faults must be obtained from the safety controller associated with the drive. In addition, the safety controller is responsible for issuing a torque disable request.

Table 33 - Safety Feedback Faults

| Safe Feedback Fault Type Value Safe Feedback Fault Type Name   | Description                                                                                                                                                                                                                         | Duplicated to Other Axis?   |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 0 Reserved Not used                                            |                                                                                                                                                                                                                                     | –                           |
|                                                                | 1 No Fault No Fault is present –                                                                                                                                                                                                    |                             |
| 2 Invalid Configuration                                        | The DSL safety feedback diagnostics have detected that the actual resolution of the connected DSL feedback device does not match the configured resolution of the corresponding Motion Safety instance.                             | No                          |
| 5  Sin2  + Cos2 Error                                                                | Analog signal diagnostics for Sin/Cos feedback have detected an error in the signal levels. This could indicate an open or short circuit in the Sin/Cos feedback wiring, or device failure.                                         | Yes                         |
| 7 Discrepancy Error                                            | Safety Dual Channel Feedback has detected a discrepancy in the velocity reported by the two monitored feedback devices.                                                                                                             | No                          |
|                                                                | 8 Partner Faulted Safety Dual Channel Feedback has detected a safety feedback fault with the partner feedback device. No                                                                                                            |                             |
| 9 Supply Voltage Error                                         | Safety diagnostics have detected that the power supply for the configured safety feedback device is out of range. This can indicate a problem in feedback wiring or internal failure of the drive circuits.                         | Yes                         |
| 11 Feedback Signal Lost                                        | The safety diagnostics for Sin/Cos feedback have detected loss of signal (below the minimum level) from the Sin/Cos encoder. This can indicate open or short circuit in the feedback device connection, or feedback device failure. | Yes                         |
| 12 Feedback Data Loss                                          | The safety diagnostics for DSL feedback have detected loss of data from the DSL encoder. This can indicate an open circuit in the feedback connections or feedback device failure.                                                  | No                          |
| 13 Feedback Device Failure                                     | • The safety diagnostics for Sin/Cos feedback have detected an internal error with the feedback interface. • The safety diagnostics for DSL feedback have detected an internal data error with the encoder.                         | Yes                         |
| 100 Unsupported DSL Device                                     | The safety diagnostics for DSL feedback have detected that the connected DSL feedback device is not supported by the drive.                                                                                                         | No                          |
| 101 DSL Unexpected UEI                                         | The safety diagnostics for DSL feedback have detected that the device for one axis is connected to the other axis. Occurs only during startup or re-configuration. This applies to only dual-axis inverters.                        | Yes                         |
| 102  DSL Position Comparison Failure                           | The safety diagnostics for DSL feedback have detected an error with the reported position from the DSL encoder. This can be an indication of encoder failure.                                                                       | No                          |
| 103 DSL Position Checksum Error                                | The safety diagnostics for DSL feedback have detected an error with the data received from the DSL encoder. This can indicate noise on the DSL signals or an encoder failure.                                                       | No                          |
| 104 DSL Multi Implementation error                             | The safety diagnostics have detected that the feedback device for one axis is connected to the other axis. This applies to only dual-axis inverters.                                                                                | Yes                         |
| 105 DSL Test Message error                                     | The safety diagnostics for DSL feedback have detected an error with the DSL encoder. This indicates an encoder failure.                                                                                                             | No                          |
| 106 DSL Power On Self-Test failure                             | The safety diagnostics for DSL feedback have detected that the DSL encoder did not complete its internal power-on self-test diagnostics. Repeated occurrence of this error likely indicates an encoder failure.                     | No                          |

## Safety Feedback Faults

When configured for safety feedback, the Motion Safety instance performs periodic diagnostics to make sure that the feedback device is operating correctly. Explicit messaging can be used to read the fault type information from the drive. For example, if an error is detected, the Safe Feedback object (class code 0x58) updates the Safe Feedback Fault Type attribute (attribute ID 0x09) with the reason for the fault. A safety feedback fault does not immediately result in torque disable of the drive. A safety feedback fault only causes a torque disable under these two conditions:

- SS1 is configured for Monitored SS1 mode
- SS1 request is received from the safety controller

## IMPORTANT

For dual-axis inverters, certain safety feedback faults detected on one axis can result in the same fault on the other axis. The following table indicates which faults are duplicated to the other axis when detected.

When a safety feedback fault is duplicated to the other axis, check the feedback devices and associated wiring for both axes to determine if one or both axes triggered the fault.

Table 34 - Safe FLT Sxx Fault Codes

| Exception Code on Drive Display             | Fault Message Logix Designer   |                                                                                                                           | Problem Possible Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SAFE FLT S01 - Safety Core Internal Fault   | SafetyFault                    | Drive safety diagnostic detected internal STO design failure.                                                             | • Cycle control power • Return drive for repair if fault continues                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SAFE FLT S02 - Safety Feedback Fault        | SafetyFeedbackFault            | Safety feedback has detected a fault.                                                                                     | Use explicit messages to read the fault reason from the primary feedback device. See Safety Feedback Attributes on page 86 for fault reasons.                                                                                                                                                                                                                                                                                                                                                      |
| SAFE FLT S03 - Safe Torque Off Fault        | SafeTorqueOffFault (1)         | Drive safety diagnostic detected internal STO design failure or hardwired input received while in integrated safety mode. | • Check the cause of the fault using a Safe Torque-off faults explicit message. Refer to Explicit Messages on page 18 . • Remove any connection to the hardwired safety inputs and reset using the STO Fault Reset procedure. Refer to Safety Fault Reset on page 78 . • Execute STO function. • Return drive for repair if fault continues.                                                                                                                                                       |
| SAFE FLT S04 - Safe Stop 1 Fault SS1Fault   |                                | SS1 safety function has detected a fault.                                                                                 | • If a controller-based SS1 function has faulted, check the SS1 controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix® Safety Application Instruction Set Reference Manual, publication 1756-RM095 . • If the drive-based SS1 function has faulted, check attribute 284 (SS1 Fault Type) by using explicit messaging to the drive module safety instance operating the SS1 function. See Safe Stop Function Attributes on page 88 . |
| SAFE FLT S05 - Safe Stop 2 Fault SS2Fault   |                                | Controller-based SS2 instruction has detected a fault.                                                                    | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095                                                                                                                                                                                                                                                                                         |
| SAFE FLT S06 - Safe Operating Stop Fault    | SOSFault                       | Controller-based SOS instruction has detected a fault.                                                                    | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095                                                                                                                                                                                                                                                                                         |
| SAFE FLT S07 - Safe Brake Fault SBCFault    |                                | Controller-based SBC instruction has detected a fault.                                                                    | .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SAFE FLT S16 - Safe Speed Monitor Fault     | SSMFault                       | Controller-based SSM instruction has detected a fault.                                                                    | This fault is not used. Check your application program for correct tag values.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SAFE FLT S17 - Safe Limited Speed Fault     | SLSFault                       | Controller-based SLS instruction has detected a fault.                                                                    | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095 .                                                                                                                                                                                                                                                                                       |
| SAFE FLT S19 - Safe Limited Direction Fault | SDIFault                       | Controller-based SDI instruction has detected a fault.                                                                    | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095 .                                                                                                                                                                                                                                                                                       |
| SAFE FLT S20 - Safe CAM Fault SCAFault      |                                | Controller-based SCA instruction has detected a fault.                                                                    | This fault is not used. Check your application program for correct tag values.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SAFE FLT S21 - Safe Limited Position Fault  | SLPFault                       | Controller-based SLP instruction has detected a fault.                                                                    | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095 .                                                                                                                                                                                                                                                                                       |

Table 35 - Init FLT Invalid Safety Firmware Fault Code

| Exception Code on Drive Display   | Fault Message Logix Designer   |                          | Problem Possible Solutions                                                                                                   |
|-----------------------------------|--------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------|
| INIT FLT M14 - Safety Firmware    | InvalidSafetyFirmwareFault (1) | Invalid safety firmware. | • Cycle control power. • Upgrade the drive firmware. • Call Technical Support. • Return drive for repair if fault continues. |

Table 36 - SAFE FLT SFX Fault Code

| Exception Code on Drive Display                | Fault Message Logix Designer   |                                                        | Problem Possible Solutions                                                                                                                                                                                   |
|------------------------------------------------|--------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SAFE FLT M01 - Safety Feedback Interface Fault | SFXFault                       | Controller-based SFX instruction has detected a fault. | Check the controller instruction fault code and diagnostic codes for more information in the controller help or the GuardLogix Safety Application Instruction Set Reference Manual, publication 1756-RM095 . |

## Troubleshoot the Safety Function

## Safety Fault Reset

If the drive motion safety instance detects a fault, the input assembly tag module:SI.SafetyFault[instance] is set to 1. The associated axis.SafetyFault tag is also set to 1.

<!-- image -->

The words module and instance (italic) in these tag names represent the module and instance name assigned in the Logix Designer application.

A SafetyFault can result from the SS1 stopping function, STO function, safety feedback, or other safety diagnostics.

To clear (reset) the SafetyFault, the fault conditions must be removed first and then a transition from logic 0 to 1 of the module:SO.ResetRequest[instance] tag is required. It is only the 0 to 1 transition that clears the fault. For a dual-axis inverter, if each safety instance is faulted, you must clear both faults within the same safety cycle. To clear both faults in a dual-axis inverter, you must transition module:SO.ResetRequest1 and module:SO.ResetRequest2 from 0 to 1 within the same scan of your safety task.

To clear an axis fault associated with a SafetyFault, first clear the SafetyFault from the safety task of your application, then clear the axis fault using the MAFR command from the motion application.

## Faults after Download

Whenever an axis is configured with Hiperface DSL feedback and the motion connection is closed, a SafetyFeedbackFault is generated.

When a single controller is used for motion and safety connections, and Hiperface DSL is the configured feedback type, a SafetyFeedbackFault is generated after program download due to DSL feedback signal loss. To clear the SafetyFeedbackFault, first clear the fault and then use the MAFR command to clear the axis fault.

When separate controllers are used for motion and safety connections, a SafetyFeedbackFault is generated after program download to the controller that manages the motion connection.

| IMPORTANT   | Transition of the SO.STOOutput tag to logic 1 must always be executed prior to transition of the SO.ResetRequest tag to logic 1.                                  |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | All Kinetix 5700 inverter axes enter the faulted state if any STO function fault is detected. Refer to Table 34 on page 77 for integrated safety troubleshooting. |

Refer to Figure 37 on page 79 for an understanding of the Kinetix 5700 STO state restart function.

## Figure 37 - Reset Safe Stop Fault Diagram

Drv:SO.STOOutput

Drv:SO.ResetRequest

Drv:SI.SafetyFault

Drv:SI.TorqueDisabled

Axis.SafeTorqueOffActiveStatus

Axis.SafeTorqueOffActiveInhibit

Axis.SafeTorqueDisabledStatus

Axis.SafetyResetRequestStatus

Axis.SafetyResetRequiredStatus

Disable Torque

Permit Torque

Torque Permited

Torque Disabled

No Fault

Drv:SI.RestartRequired

Axis.SafetyFault

No Fault

Faulted (cleared by MAFR)

Start Permitted

Start Inhibitted

Reset Not Required

Axis.SafetyFaultStatus

No Fault

Faulted

S0.ResetRequest

Reset Required

Permit Torque

Disable Torque

Torque Permited

Torque Disabled

Axis.SafeStopFault

No Fault

Safety Fault Occurs

Restart Not Required

Restart Required

## Notes:

| Axis Tag Name (motion controller) Motion Connection Attribute Number   | Data Type Description                                                                                                                                                                                                                                                    | Safety Output Assembly Tag Name (safety controller)   |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Axis.AxisSafetyState 760 DINT                                          | Drive module Safety Supervisor state. See the Safety Supervisor State on page 19 for more details.                                                                                                                                                                       | None                                                  |
| Axis.AxisSafetyDataA 986 DINT                                          | 32-bit data container holding general purpose safety-data passed from the safety controller.                                                                                                                                                                             | module:SO:PassThruDataA[instance]                     |
| Axis.AxisSafetyDataB 987 DINT                                          | 32-bit data container holding general purpose safety-data passed from the safety controller.                                                                                                                                                                             | module:SO:PassThruDataB[instance]                     |
| Axis.AxisSafetyStatus 761 DINT                                         | Collection of bits indicating the status of the standard safety functions for the axis as reported by Drive Safety Instance.                                                                                                                                             | See individual bits below.                            |
| Axis.SafetyFaultStatus [0] BOOL                                        | Any Safe Stop Fault occurring in the Safety Instance. 0 = Not Faulted 1 = Safety Fault                                                                                                                                                                                   | None                                                  |
| Axis.SafetyResetRequestStatus [1] BOOL                                 | Indicates that the state of the reset request output from the safety controller (in the safety output assembly) connected with the drive safety instance. This is the reset input to the safety instance in the drive module. 0 = Reset Request OFF 1 = Reset Request ON | module:SO.ResetRequest[instance]                      |

Table 37 - Motion Connection Axis Tags

<!-- image -->

## Controller Tags and Safety Attributes

Controller axis tags are used by the motion controller motion task to read the status of safety functions and coordinate motion. This appendix lists the motion controller tags that are associated with the safety instances and with safety functions operating in the safety task of the controller.

| Topic                            |   Page |
|----------------------------------|--------|
| Motion Connection Axis Tags      |     81 |
| Safety Assembly Tags             |     84 |
| Safety Feedback Attributes       |     86 |
| Safe Stop Function Attributes    |     88 |
| Dual Channel Feedback Attributes |     91 |

Safety attributes provide additional information not available through the tag structure. Attributes are read using explicit messages.

IMPORTANT

The controller axis tags and the safety attributes read by using explicit messages must not be used in the operation of a safety function.

Motion Connection Axis Tags This table provides motion-connection axis tag names that are updated to
hfillbd ffi show safety instance status or controller-based safety function status.

<!-- image -->

The words module , instance, and axis (italic) in these tag names represent the module, instance, and axis name assigned in the Logix Designer application.

Table 37 - Motion Connection Axis Tags (Continued)

| Axis Tag Name (motion controller)       | Motion Connection Attribute Number   |      | Data Type Description                                                                                                                                                                                                             | Safety Output Assembly Tag Name (safety controller)   |
|-----------------------------------------|--------------------------------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Axis.SafetyResetRequiredStatus [2] BOOL |                                      |      | Indicates that the drive-module safety instance associated with this Axis requires a reset of the safety function. 0 = Normal 1 = Reset Required                                                                                  | None                                                  |
| Axis.SafeTorqueOffActiveStatus [3] BOOL |                                      |      | Indicates that the state of the STO output from the safety controller, which is the STO input to the drive-module safety instance associated with this axis. 0 = STO Output Is active 1 = STO is not active, STO is not requested | module:SO.STOOuput[instance]                          |
| Axis.SafeTorqueDisabledStatus [4]       |                                      | BOOL | Indicates that the drive-module safety instance Torque Disabled Status. 0 = Axis power structure is not inhibited by the safety instance 1 = Axis power structure is inhibited                                                    | None                                                  |
| Axis.SBCActiveStatus                    | [5]                                  | BOOL | Indicates that the SBC function is active and the sequence to set the Safety Brake has started. This function is only available as a controller based function. 0 = SBC Function is not Active 1 = SBC Function is Active                                                                                                                                                                                                                                   | module:SO.SBCActive                                   |
| Axis.SBCEngagedStatus                   | [6]                                  | BOOL | Indicates that the External Safety Brake is engaged by the controller based SBC function. 0 = Brake is Engaged 1 = Brake is Released                                                                                                                                                                                                                                   | module:SO.SBCBrakeEngaged                             |
| Axis.SS1ActiveStatus                    | [7]                                  | BOOL | Indicates that the controller-based or the drive-based SS1 function is active. 0 = SS1 Function is not Active 1 = SS1 Function is Active                                                                                          | module:SO.SSActive[instance]                          |
| Axis.SS2ActiveStatus                    | [8]                                  | BOOL | Indicated that the controller-based SS2 function is active. 0 = SS2 Function is not Active 1 = SS2 Function is Active                                                                                                             | module:SO.SSActive [instance]                         |
| Axis.SOSActiveStatus                    | [9]                                  | BOOL | Indicates that the controller-based SOS function is active. 0 = SOS Function is not Active 1 = SOS Function is Active                                                                                                             | module:SO.SOSActive[instance]                         |
| Axis.SOSStandstillStatus                | [10]                                 | BOOL | Indicates that the controller-based SOS function has detected standstill according to the function configuration. 0 = monitored axis is not at Standstill 1 = monitored axis is at standstill                                     | module:SO.SOSLimit[instance]                          |
| Axis.SMTActiveStatus                    | [11]                                 |      | BOOL Always 0. This function is not available                                                                                                                                                                                     | None                                                  |
| Axis.SMTOvertemperatureStatus [12]      |                                      |      | BOOL Always 0. This function is not available.                                                                                                                                                                                    | None                                                  |
| Axis.SSMActiveStatus                    | [16]                                 |      | BOOL For use with a controller-based SSM function.                                                                                                                                                                                | module:SO.SSMActive[instance]                         |
| Axis.SSMStatus                          | [17]                                 |      | BOOL For use with a controller-based SSM function.                                                                                                                                                                                | module:SO.SSMStatus[instance]                         |
| Axis.SLSActiveStatus                    | [18]                                 | BOOL | Indicates that the controller-based SLS function is active. 0 = SLS Function is not Active 1 = SLS Function is Active                                                                                                             | module:SO.SLSActive[instance]                         |
| Axis.SLSLimitStatus                     | [19]                                 | BOOL | Indicates that the controller-based SLS function has detected the monitored axis speed above the limit set-point. 0 = axis is below set-point speed 1 = axis is greater than or equal to the set-point speed                      | module:SO.SLSILimit[instance]                         |
| Axis.SLAActiveStatus                    | [20]                                 |      | BOOL Always 0. This function is not available.                                                                                                                                                                                    | None                                                  |
| Axis.SLALimitStatus                     | [21]                                 |      | BOOL Always 0. This function is not available.                                                                                                                                                                                    | None                                                  |
| Axis.SDIActiveStatus                    | [22]                                 | BOOL | Indicates that the controller-based SDI function is active. 0 = SDI Function is not Active 1 = SDI Function is Active                                                                                                             | module:SO.SDIActive[instance]                         |
| Axis.SDILimitStatus                     | [23]                                 | BOOL | Indicates that the controller-based SDI function detected motion greater than the limit in the unintended direction. 0 = Limit not reached 1 = Unintended motion                                                                  | module:SO.SDILimit[instance]                          |
| Axis.SafePositiveMotionStatus [24]      |                                      |      | BOOL Always 0. This function is not available.                                                                                                                                                                                    | None                                                  |
| Axis.SafeNegativeMotionStatus [25]      |                                      |      | BOOL Always 0. This function is not available.                                                                                                                                                                                    | None                                                  |
| Axis.SCAActiveStatus                    | [26]                                 |      | BOOL For use with a controller-based SCA function.                                                                                                                                                                                | module:SO.SCAActive[instance]                         |
| Axis.SCAStatus                          | [27]                                 |      | BOOL For use with a controller-based SCA function.                                                                                                                                                                                | module:SO.SCAStatus[instance]                         |
| Axis.SLPActiveStatus                    | [28]                                 | BOOL | Indicates that the controller-based SLP function is active. 0 = SLP Function is not Active 1 = SLP Function is Active                                                                                                             | module:SO.SLPActive[instance]                         |
| Axis.SLPLimitStatus                     | [29]                                 | BOOL | Indicates that the controller-based SLP function has detected the monitored axis position outside of the set-point limits. 0 = axis position is within the limits 1 = axis position is outside of the limits                      | module:SO.SLPLimit[instance]                          |

Table 37 - Motion Connection Axis Tags (Continued)

| Axis Tag Name (motion controller)                 | Motion Connection Attribute Number   |      | Data Type Description                                                                                                                                                         | Safety Output Assembly Tag Name (safety controller)   |
|---------------------------------------------------|--------------------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Axis.SafetyOutputConnectionClosedStatus [30] BOOL |                                      |      | Indicates the safety connection status from the controller to the drive module. 0 = connection open 1 = connection closed                                                     | None                                                  |
| Axis.SafetyOutputConnectionIdleStatus [31] BOOL   |                                      |      | Indicates the safety connection status from the controller to the drive module. 0 = connection active 1 = connection idle                                                     | None                                                  |
| Axis.AxisSafetyStatusRA 762 DINT                  |                                      |      | Collection of bits indicating the status of Rockwell Automation specific safety functions for the axis as reported by Drive Safety Instance.                                  | See individual bits below.                            |
| Axis.SafeBrakeIntegrityStatus [0] BOOL            |                                      |      | Status of an external safety brake controlled by SBC instruction. The brake status, released or engaged, is undetermined. 0 = SBC fault 1 = No faults detected                | module:SO.SBCIntegrity[instance]                      |
|                                                   |                                      |      | Axis.SafeFeedbackHomedStatus [1] BOOL Status of the controller-based SFX position homing function.                                                                            | module:SO.SFHome[instance]                            |
| Axis.AxisSafetyFaults 763 DINT                    |                                      |      | Collection of bits indicating the Safety Fault status of the drive-module safety instances and integrated safety functions.                                                   | See individual bits below.                            |
| Axis.SafetyCoreFault [0] BOOL                     |                                      |      | Indicates an internal fault occurred within the drive-module safety instance. In the case of dual-axis inverters, both safety instances fault. 0 = Normal Operation 1 = Fault | None (use explicit message)                           |
| Axis.SafetyFeedbackFault [2] BOOL                 |                                      |      | Indicates a fault occurred with the safety feedback or with the safety dual-channel feedback. 0 = Normal Operation 1 = Fault                                                  | None (use explicit message)                           |
| Axis.SafeTorqueOffFault [3] BOOL                  |                                      |      | Indicates a fault occurred within the STO function of the drive-module safety instance. 0 = Normal Operation 1 = Fault                                                        | None (use explicit message)                           |
| Axis.SS1Fault [4] BOOL                            |                                      |      | Indicates that a fault occurred with the drive-based or a controller based SS1 function. 0 = Normal Operation 1 = Fault                                                                                                                                                                               | module:SO.SSFault[instance]                           |
| Axis.SS2Fault                                     | [5]                                  | BOOL | Indicates that a fault occurred with the drive-based SS2 function. 0 = Normal Operation 1 = Fault                                                                             | module:SO.SSFault[instance]                           |
| Axis.SOSFault                                     | [6]                                  | BOOL | Indicates that a fault occurred with the drive-based SOS function. 0 = Normal Operation 1 = Fault                                                                             | module:SO.SOSFault[instance]                          |
| Axis.SBCFault                                     | [7]                                  | BOOL | Indicates that a fault occurred with the controller-based SS2 function. 0 = Normal Operation 1 = Fault                                                                        | module:SO.SBCFault[instance]                          |
| Axis.SMTFault                                     | [8]                                  |      | BOOL Always 0. This function is not available.                                                                                                                                | –                                                     |
| Axis.SSMFault                                     | [16]                                 | BOOL | Controller-based SSM fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SSMFault[instance]                          |
| Axis.SLSFault                                     | [17]                                 | BOOL | Controller-based SLS fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SLSFault[instance]                          |
| Axis.SLAFault                                     | [18]                                 |      | BOOL Always 0. This function is not available.                                                                                                                                | –                                                     |
| Axis.SDIFault                                     | [19]                                 | BOOL | Controller-based SDI fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SDIFault[instance]                          |
| Axis.SCAFault                                     | [20]                                 | BOOL | Controller-based SCA fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SCAFault[instance]                          |
| Axis.SLPFault                                     | [21]                                 | BOOL | Controller-based SLP fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SLPFault[instance]                          |
| Axis.SafetyValidatorFault                         | [30]                                 |      | BOOL Always 0. This function is not available.                                                                                                                                | –                                                     |
| Axis.SafetyUNIDFault                              | [31]                                 |      | BOOL Always 0. This function is not available.                                                                                                                                | –                                                     |
| Axis.AxisSafetyFaultsRA                           | 764                                  | DINT | Collection of bits indicating the safety fault status of Rockwell Automation safety functions.                                                                                | See individual bits below.                            |
| Axis.SFXFault                                     | [1]                                  | BOOL | Controller-based SFX fault. 0 = Normal Operation 1 = Fault                                                                                                                    | module:SO.SFXFault[instance]                          |
| Axis.AxisSafetyAlarms                             | 753                                  |      | DINT Reserved for future use.                                                                                                                                                 | –                                                     |

## Safety Assembly Tags

Table 38 - Safety Input Assembly Tags

| Safety Input Assembly Tag Name (input to safety controller)   | Type/ [bit]   | Description                                                                                                                  |
|---------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------|
| module:SI.ConnectionStatus                                    |               | SINT Collection of bits listed below.                                                                                        |
| module:SI.RunMode                                             |               | [0] Safety Connection 0= idle 1 = Run                                                                                        |
| module:SI.ConnectionFaulted                                   |               | [1] Safety Connection 0=normal 1= Faulted                                                                                    |
| module:SI.FeedbackPosition[instance]                          |               | DINT Primary Feedback Position from drive-module safety instance. Value is in feedback counts.                               |
| module:SI.FeedbackVelocity[instance]                          |               | REAL Primary Feedback Velocity from drive-module safety instance. Value is in revolutions/second.                            |
| module:SI.SecondaryFeedbackPosition[instance]                 |               | DINT Secondary Feedback Position from drive-module safety instance. Value is in position counts.                             |
| module:SI.SecondaryFeedbackVelocity[instance]                 |               | REAL Secondary Feedback Velocity from drive-module safety instance. Value is in revolutions/second.                          |
| module:SI.StopStatus[instance]                                |               | SINT Collection of bits listed below.                                                                                        |
| module:SI.STOActive[instance] [0]                             |               | Indicates STO function status. 0 = STO function not active 1 = STO function active                                           |
| module:SI.SBCActive[instance] [1]                             |               | Always 0                                                                                                                     |
| module:SI.SS1Active[instance] [2]                             |               | Indicates drive-based SS1 active status. 0 = SS1 function not active 1 = SS1 function active                                 |
| module:SI.SS2Active[instance] [3]                             |               | Always 0                                                                                                                     |
| module:SI.SOSStandstill[instance] [4]                         |               | Always 0                                                                                                                     |
| module:SI.SafetyFault[instance]                               |               | [6] 1 = Safe Stop Fault present                                                                                              |
| module:SI.RestartRequired[instance]                           |               | [7] 1 = Reset is required                                                                                                    |
| module:SI.SafeStatus[instance]                                |               | SINT Collection of bits listed below.                                                                                        |
| module:SI.TorqueDisabled[instance] [0]                        |               | 0 = Torque Permitted 1 = Torque Disabled                                                                                     |
| module:SI.BrakeEngaged[instance] [1]                          |               | Always 0                                                                                                                     |
| module:SI.MotionStatus[instance]                              |               | SINT Collection of bits listed below.                                                                                        |
| module:SI.MotionPositive[instance] [0]                        |               | 0 = no positive motion 1 = motion in positive direction                                                                      |
| module:SI.MotionNegative[instance] [1]                        |               | 0 = no negative motion 1 = motion in negative direction                                                                      |
| module:SI.FunctionSupport[instance]                           |               | SINT Collection of bits listed below.                                                                                        |
| module:SI.PrimaryFeedbackValid[instance] [0]                  |               | 0 = Primary Feedback not configured or Faulted 1 = Primary Feedback Value is valid                                           |
| module:SI.SecondaryFeedbackValid[instance]                    |               | [1] Collection of bits listed below.                                                                                         |
| module:SI.DiscrepancyCheckingActive[instance]                 |               | [2] 1 = Feedback Velocity Discrepancy checking is active                                                                     |
| module:SI.SBCReady[instance] [3]                              |               | Always 0                                                                                                                     |
| module:SI.SS1Ready[instance] [4]                              |               | 0 = Drive-based SS1 function is not configured or faulted 1 = Drive-based SS1 function is configured and ready for operation |
| module:SI.SS2Ready[instance] [5]                              |               | Always 0                                                                                                                     |
| module:SI.SOSReady[instance] [6]                              |               | Always 0                                                                                                                     |

Safety assembly tags are associated with a safety connection from a safety controller to a drive module. The data in these tags are communicated at the configured connection rate.

<!-- image -->

The words module and instance (italic) in these tag names represent the module and instance name assigned in the Logix Designer application.

Data from the drive module to the safety controller is in the safety input assembly. Data from the safety controller to the drive module is in the safety output assembly.

Table 39 - Safety Output Assembly Tags

| Safety Output Assembly Tag Name (output to safety controller)   | Type/ [bit]  Description                                                                                                                                                                                                  |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                 | module:SO.PassThruDataA[instance] DINT 32-bit data container holding general purpose safety data passed from the safety controller.                                                                                       |
|                                                                 | module:SO.PassThruDataB[instance] DINT 32-bit data container holding general purpose safety data passed from the safety controller.                                                                                       |
|                                                                 | module:SO.PassThruStopStatus[instance] SINT Collection of Safe Stop Function Status bits.                                                                                                                                 |
| module:SO.SBCIntegrity[instance] [0]                            | Status of an external Safety Brake controlled by SBC function. 0 = SBC fault. The brake status, released or engaged, is undetermined. 1 = No faults detected.                                                             |
| module:SO.SBCActive[instance] [1]                               | Indicates that the SBC function is active and the sequence to set the Safety Brake has started. This function is only available as a controller-based function. 0 = SBC Function is not Active 1 = SBC Function is Active |
| module:SO.SBCBrakeEngaged[instance] [2]                         | Indicates that the External Safety Brake is engaged by the controller-based SBC function. 0 = Brake is Engaged 1 = Brake is Released                                                                                      |
| module:SO.SS1Active[instance] [3]                               | Indicates that the controller-based SS1 function is active. 0 = SS1 Function is not Active 1 = SS1 Function is Active                                                                                                     |
| module:SO.SS2Active[instance] [4]                               | Indicated that the controller-based SS2 function is active. 0 = SS2 Function is not Active 1 = SS2 Function is Active                                                                                                     |
| module:SO.SOSActive[instance] [5]                               | Indicates that the controller-based SOS function is active. 0 = SOS Function is not Active 1 = SOS Function is Active                                                                                                     |
| module:SO.SOSStandstill[instance] [6]                           | Indicates that the controller-based SOS function has detected Standstill according to the function configuration. 0 = Monitored axis is not at Standstill                                                                 |
| module:SO.PassThruSpeedLimitStatus[instance]                    | SINT Collection of Limit Function Status bits.                                                                                                                                                                            |
| module:SO.SLSActive[instance] [2]                               | Indicates that the controller-based SLS function is active. 0 = SLS Function is not active 1 = SLS Function is active                                                                                                     |
| module:SO.SLSLimit[instance] [3]                                | Indicates that the controller-based SLS function has detected the monitored axis speed above the limit set-point. 0 = axis is below set-point speed 1 = axis is greater than or equal to the set-point speed              |
| module:SO.SDIActive[instance] [6]                               | Indicates that the controller-based SDI function is active. 0 = SDI Function is not active 1 = SDI Function is active                                                                                                     |
| module:SO.SDILimit[instance] [7]                                | Indicates that the controller-based SDI function detected motion greater than the limit in the unintended direction. 0 = Limit not reached 1 = Unintended motion                                                          |
| module:SO.PassThruPositionLimitStatus[instance] SINT            | Collection of bits indicating the Monitoring Function Limit status of controller-based functions. The bits are listed below.                                                                                              |
| module:SO.SLPActive[instance] [2]                               | Indicates that the controller-based SLP function is active. 0 = SLP Function is not active 1 = SLP Function is active                                                                                                     |
| module:SO.SLPLimit[instance] [3]                                | Indicates that the controller-based SLP function has detected the monitored axis position outside of the set-point limits. 0 = axis position is within the limits 1 = axis position is outside of the limits              |
| module:SO.SFHomed[instance] [7]                                 | Status of the controller-based SFX position homing function. 1 = SFX Homed                                                                                                                                                |
| module:SO.PassThruStopFaults[instance] SINT                     | Collection of bits indicating the Safety Fault status of controller-based safety functions The bits are listed below.                                                                                                     |
| module:SO.SFXFault[instance] [0]                                | Indicates that a fault occurred with the controller-based SFX function. 0 = Normal Operation 1 = Fault                                                                                                                    |
| module:SO.SBCFault[instance] [1]                                | Indicates that a fault occurred with the controller-based SBC function. 0 = Normal Operation 1 = Fault                                                                                                                    |
| module:SO.SS1Fault[instance] [2]                                | Indicates that a fault occurred with the controller-based SS1 function. 0 = Normal Operation 1 = Fault                                                                                                                    |
| module:SO.SS2Fault[instance] [3]                                | Indicates that a fault occurred with the controller-based SS2 function. 0 = Normal Operation 1 = Fault                                                                                                                    |
| module:SO.SOSFault[instance] [4]                                | Indicates that a fault occurred with the controller-based SOS function. 0 = Normal Operation 1 = Fault                                                                                                                    |

Table 39 - Safety Output Assembly Tags (Continued)

| Safety Output Assembly Tag Name (output to safety controller)   | Type/ [bit]   | Description                                                                                                            |
|-----------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------|
| module:SO.PassThruLimitFaults[instance] SINT                    |               | Collection of bits indicating the Safety Fault status of controller-based safety functions. The bits are listed below. |
| module:SO.SLSFault[instance] [1]                                |               | Controller-based SLS fault. 0 = Normal Operation 1 = Fault                                                             |
| module:SO.SDIFault[instance] [2]                                |               | Controller-based SDI fault. 0 = Normal Operation 1 = Fault                                                             |
| module:SO.SLPFault[instance] [4]                                |               | Controller-based SLP fault. 0 = Normal Operation 1 = Fault                                                             |
| module:SO.SafetyStopFunctions[instance]                         |               | SINT A collection of bits used to activate (request) safety functions as listed below.                                 |
| module:SO.STOOutput[instance]                                   | [0]           | 0 = Activate STO Function 1 = Permit Torque                                                                            |
| module:SO.SBCOutput[instance]                                   |               | [1] Drive-based function not available.                                                                                |
| module:SO.SS1Request[instance] [2]                              |               | 0 = Remove SS1 Request 1 = Activate Drive-based SS1 Function                                                           |
| module:SO.SS2Request[instance]                                  |               | [3] Drive-based function not available.                                                                                |
| module:SO.SOSRequest[instance]                                  |               | [4] Drive-based function not available.                                                                                |
| module:SO.ResetRequest[instance]                                |               | [7] 0 -> 1 transition resets drive-based Safe Stop function.                                                           |

## Safety Feedback Attributes

Safety feedback attributes provide configuration and status information for safety feedback. Single-axis drives (inverters) have two safety feedback instances and dual-axis drives have four safety feedback instances. Safety feedback attributes provide status and configuration data. All attributes can be read by using explicit messages. Attributes that can be written are indicated in Table 41. Configuration attributes can only be read using explicit messages.

Table 40 - Safety Feedback Instance Numbers

|   Safety Feedback Instance | Kinetix 5700 Drive Motion Safety Category Feedback                                 |                                      |
|----------------------------|------------------------------------------------------------------------------------|--------------------------------------|
|                          1 | Single-axis inverters Motion Safety  Dual-axis inverters Motion Safety 1           | DSL Hiperface                        |
|                          2 | Single-axis inverters Motion Safety  Hiperface Dual-axis inverters Motion Safety 1 | Sin/Cos, Endat Sin/Cos, or           |
|                          3 | Dual-axis inverters (only) Motion Safety 2                                         | DSL Hiperface                        |
|                          4 | Dual-axis inverters (only) Motion Safety 2                                         | Sin/Cos, Endat Sin/Cos, or Hiperface |

Table 41 - Safety Feedback Attributes (Class 0x58)

| Attribute ID Decimal (Hex)   | Attribute Name Attribute Description Values                                                         |                                                                                         |
|------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| 1 (0x1) Velocity Data Type   | Determines the data type of feedback velocity and feedback acceleration and all related attributes. | 1 = REAL (hard-coded)                                                                   |
|                              | 2 (0x2) Feedback Position Actual position of the feedback device.                                   | Feedback Counts Safety data with a safe value defined by Position Safe State Behavior   |
|                              | 3 (0x3) Feedback Velocity Actual velocity of the feedback device.                                   | Feedback Units/s Safety data with a safe value defined by Velocity Safe State Behavior. |
|                              | 4 (0x4) Feedback Acceleration Actual acceleration of the feedback device.                           | Feedback Units/s² Safety data with a safety state of 0.                                 |
|                              | 5 (0x5) Feedback Mode Motion Feedback mode.                                                         | 0 = Not Used (default) 1 = Used                                                         |
|                              | 8 (0x8) Feedback Fault Status of this motion feedback channel.                                      | 0 = No Fault 1 = Faulted                                                                |

Table 41 - Safety Feedback Attributes (Class 0x58) (Continued)

| Attribute ID Decimal (Hex)              | Attribute Name Attribute Description Values                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                         | 9 (0x9) Feedback Fault Reason Determines cause of the fault detected.                                                                                                                                                                  | 0 = Reserved 1 = No Fault 2 = Invalid Configuration 3 = Exceeded Max Speed 4 = Exceeded Max Acceleration 5 = Sin 2 +Cos 2 Error 6 = Quadrature Error 7 = Discrepancy Error 8 = Partner Faulted 9 = Supply Voltage Error 10 = Feedback Signal Noise 11 = Feedback Signal Lost 12 = Feedback Data Loss 13 = Feedback Device Failure 100 = DSL ECN Mismatch 101 = DSL Unexpected UEI 102 = DSL Position Comparison Failure 103 = DSL Position Checksum Failure 104 = DSL Multi-Axis FPGA Failure 105 = DSL Test Message Failure |
|                                         | 10 (0xA) Reset Feedback Fault Resets a motion feedback fault (read/write access). 0 to 1 transition required to reset                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                         | 11 (0xB) Position Safe State Behavior Defines behavior for value reporting when faulted. 2 = Hold Last Value                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                         | 13 (0xD) Velocity Safe State Behavior Defines behavior for value reporting when faulted. 0 = Use Velocity Safe State Value (default)                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                         | 14 (0xE) Velocity Safe State Value Safe Velocity Feedback and Acceleration Feedback value. Default = 0                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 15 (0xF) Feedback Resolution Unit       | Unit of measure for feedback resolution used by Feedback Cycle Resolution attribute.                                                                                                                                                   | Default = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         | 16 (0x10) Feedback Unit Unit of measure for the feedback device. 0 = Rev (default)                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                         | 17 (0x11) Feedback Type Identifies the type of feedback device.                                                                                                                                                                        | 0 = Not Specified (default) 2 = Sine/Cosine 3 = Hiperface 4 = EnDat Sine/Cosine 7 = Hiperface DSL                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 18 (0x12) Feedback Polarity             | Feedback polarity of Normal provides increasing position values when the feedback device is moved in position according to the encoder manufacture specifications. For feedback devices internal to Allen Bradley® motors, the Normal direction is clockwise rotation of the shaft when facing the end of the motor shaft.                                                                                                                                                                                                                                        | 0 = Normal (default) 1 = Inverted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 19 (0x13) Feedback Cycle Resolution     | This is the number of feedback cycles per revolution of the encoder. For a Sin/Cos encoder, this is the number of sinusoidal cycles per revolution.                                                                                    | 0 = Default                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 20 (0x14)  Feedback Cycle interpolation | This value is the number of feedback counts per feedback cycle. This value is always 4 for sin/cos or incremental encoders and 1 for DSL encoders.                                                                                     | Counts/Cycle Default = 0 4 for Feedback Type=2/3/4 Otherwise 1                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 22 (0x16) Velocity Average Time         | A moving average filter is applied to velocity that is provided by the Motion Safety instance of the drive. This parameter specifies the window of time where the average is taken. Feedback velocity is provided as a REAL data type. | 0 = Disable Averaging (default) 1 to 65565 ms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 31 (0x1F) Motion Positive               | Indicates positive motion according to the direction and Standstill Speed attribute.                                                                                                                                                   | 0 = No Positive Motion 1 = Positive Motion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 32 (0x20) Motion Negative               | Indicates negative motion according to the direction and Standstill Speed attribute.                                                                                                                                                   | 0 = No Negative Motion 1 = Negative Motion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                         | 33 (0x21) Standstill Speed Defines the speed below which motion is considered stopped.                                                                                                                                                 | Feedback Units/s Default = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 110 (0x6E) Feedback Valid               | Safety Feedback object is supported, configured, not faulted and is currently producing valid safety feedback data from a connected feedback device.                                                                                   | 0 = Safety Feedback Data Invalid 1 = Safety Feedback Data Valid                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Safe Stop Function Attributes

Safe-stop function attributes provide configuration and status information for safety feedback.

Single-axis drives (inverters) have one safe-stop function instance and dualaxis drives have two safe-stop function instances. Safe-stop function attributes provide status and configuration data. All attributes can be read using explicit messages. Attributes that can be written are indicated in the table. Configuration attributes can be read but cannot be written using an explicit message.

Table 42 - Safe Stop Function Instance Numbers

|    | Safe Stop Instance Kinetix 5700 Drive   | Motion Safety Category   |
|----|-----------------------------------------|--------------------------|
|  1 | Single-axis inverters                   | Motion Safety            |
|  1 | Dual-axis inverters Motion Safety 1     |                          |
|  2 | Dual-axis inverters                     | Motion Safety 2          |

Table 43 - Safe Stop Function Attributes (Class 0x5A)

| Attribute ID Decimal (Hex)           | Attribute Name Attribute Description Values                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      |                                                                                                                             | 10 (0xA) Safety Reset Reset all safety functions. 0 to 1 transition required to reset                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                      | 11 (0xB) Restart Type Selects safety function restart behavior while operating. 1 = Automatic                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 12 (0xC) Cold Start Type             | Selects safety function restart behavior when applying controller power or mode change to Run.                              | 1 = Automatic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 20 (0x14) Safety Feedback Instance   | Instance ID of a Safety Feedback instance to provide position, velocity, and acceleration data used by safe stop functions. | 0 = No feedback (default) 1,2 = 2198-Sxxx-ERS4 1,2,3,4 = 2198-Dxxx-ERS4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                      | 21 (0x15) Safety Feedback Fault Copy of feedback status from the Safety Feedback instance.                                  | 0 = No Fault 1 = Faulted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 22 (0x16) Safety Feedback Fault Type | Condition detected that caused the Feedback Status attribute to fault.                                                      | 0 = Reserved 1 = No Fault 2 = Invalid Configuration 1 3 = Exceeded Max Speed 1 5 = Sin 2 +Cos 2 Error 1 6 = Quadrature Error 1 7 = Discrepancy Error 1 8 = Partner Faulted 1 9 = Supply Voltage Error 1 10 = Feedback Signal Noise 1 11 = Feedback Signal Lost 1 12 = Feedback Data Loss 1 13 = Feedback Device Failure 1 52 = Invalid Configuration 2 53 = Exceeded Max Speed 2 55 = Sin 2 +Cos 2 Error 2 56 = Quadrature Error 2 57 = Discrepancy Error 2 58 = Partner Faulted 2 59 = Supply Voltage Error 2 60 = Feedback Signal Noise 2 61 = Feedback Signal Lost 2 62 = Feedback Data Loss 2 63 = Feedback Device Failure 2 |
|                                      | 30 (0x1E) Safety Function Fault Logical OR of all Fault attributes that reference this instance.                            | 0 = No Fault 1 = Faulted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                      | 31 (0x1F) Safety Stop Fault Logical OR of all Stop Fault attributes in this instance.                                       | 0 = No Fault 1 = Faulted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                      | 32 (0x20) Safety Limit Fault Logical OR of all Limit Fault attributes that reference this instance.                         | 0 = No Fault No Limit Functions Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                      | 33 (0x21) Safety Limit Active Logical OR of all Limit Active attributes that reference this instance.                       | 0 = No Limit No Limit Functions Supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                      | 34 (0x22) Restart Required A stop function has been activated and Restart Type is Manual.                                   | 0 = Restart Not Required 1 = Restart Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Table 43 - Safe Stop Function Attributes (Class 0x5A) (Continued)

| Attribute ID Decimal (Hex)       | Attribute Name Attribute Description Values                                                                                               |                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | 40 (0x28) Safety Stop Status Collection of Safety Stop Status bits:                                                                       | Bit: 0 = Safety Function Fault 1 = Safety Reset 2 = Restart Required 3 = STO Active 4 = Torque Disabled 7 = SS1 Active                                                                                                                                                                                                                                   |
|                                  | 41 (0x29) Safety Stop Faults Collection of Safety Stop Fault bits:                                                                        | Bit: 2 = Feedback Fault 3 = STO Fault 4 = SS1 Fault 5 = SS2 Fault 6 = SOS Fault 7 = SBC Fault 8 = SMT Fault                                                                                                                                                                                                                                              |
| 50 (0x32) Connection Loss Action | Safety Output Connection is lost (or closed) and optional Connection Loss Action is Set to STO (default).                                 | 0 = STO (default) 1 = SS1                                                                                                                                                                                                                                                                                                                                |
| 51 (0x33) Connection Idle Action | Safety Output Connection’s Run/Idle bit transitions from Run to Idle and Optional Connection Idle Action is Set to STO (default).         | 0 = STO (default) 1 = SS1                                                                                                                                                                                                                                                                                                                                |
|                                  | 100 (0x64) Safety IO Status State of MPU inputs                                                                                           | Bit: 0 = PWM Power On (1 On) 1 = PWM Enable A (1 Enable) 2 = Enable A Readback (1 Enabled) 3 = Enable Test A (1 Enabled) 4 = Safety Input A (0 Energized) 8 = Pulse Test Enable (1 Enabled) 9 = PWM Enable B (1 Enable) 10 = Enable B Readback (1 Enabled) 11 = Enable Test B (1 Enabled) 12 = PWM Power Status (0 On) 13 = Safety Input B (0 Energized) |
| 101 (0x65) STO Delay             | Specify delay time from STO Active to Torque Disabled. This delay allows the time for an external brake to engage before torque disabled. | Delay in milliseconds Default = 0                                                                                                                                                                                                                                                                                                                        |
| 110 (0x6E) SBC Ready             | Safe Break Control safety function is supported, configured, and ready for operation.                                                     | 0 = Not Ready SBC Function Not Supported                                                                                                                                                                                                                                                                                                                 |
| 111 (0x6F) SS1 Ready             | Safe Stop 1 safety function is supported, configured, and ready for operation.                                                            | 0 = Not Ready 1 = Ready                                                                                                                                                                                                                                                                                                                                  |
| 112 (0x70) SS2 Ready             | Safe Stop 2 safety function is configured and ready for activation.                                                                       | 0 = Not Ready SS2 Function Not Supported                                                                                                                                                                                                                                                                                                                 |
| 113 (0x71) SOS Ready             | Safe Operating Stop safety function is configured and ready for activation.                                                               | 0 = Not Ready SOS Function Not Supported                                                                                                                                                                                                                                                                                                                 |
| 114 (0x72) SMT Ready             | Safe Motor Temperature safety function is configured and ready for activation.                                                            | 0 = Not Ready SMT Function Not Supported                                                                                                                                                                                                                                                                                                                 |
| 260 (0x104) STO Mode             | Safe torque-off mode.                                                                                                                     | 1 = Used 2 = Permit Torque                                                                                                                                                                                                                                                                                                                               |
| 261 (0x105) STO Output           | Enables or disables energy to the motor that can generate torque (or force in the case of a linear motor).                                | 0 = Disable Torque 1 = Permit Torque Safety data with a safety state of 0.                                                                                                                                                                                                                                                                               |
| 262 (0x106) STO Active           | Output of STO Activation block.                                                                                                           | 0 = Permit Torque 1 = Disable Torque                                                                                                                                                                                                                                                                                                                     |
| 263 (0x107) STO Fault            | Safe Torque-off fault.                                                                                                                    | 0 = No Fault 1 = Faulted                                                                                                                                                                                                                                                                                                                                 |
|                                  | 264 (0x108) STO Fault Type Detailed information about a fault.                                                                            | 1 = No Fault 2 = Invalid Configuration 3 = Circuit Error 4 = Stuck At Low 5 = Stuck At High 6 = Cross Connection 102 = Hardwired STO Input Discrepancy 104 = Hardwired STO Input Active in Network                                                                                                                                                       |

Table 43 - Safe Stop Function Attributes (Class 0x5A) (Continued)

| Attribute ID Decimal (Hex)           | Attribute Name Attribute Description Values                                                                                                  |                                                                                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 265 (0x109) STO Activation           | Bit string showing status of all inputs to the STO Activation block.                                                                         | Bit: 0 = STO Output Active 1 = SS1 Complete 2 = Safety Stop Fault 3 = Safety Limit Fault 4 = Safety Limit Action 5 = Connection Loss 6 = Connection Idle |
|                                      | 266 (0x10A) Torque Disabled Status of Safe Torque-off.                                                                                       | 0 = Torque Permitted 1 = Torque Disabled                                                                                                                 |
| 280 (0x118) SS1 Mode                 | Safe Stop 1 mode.                                                                                                                            | 0 = Not Used 1 = Timed SS1 (default) 2 = Monitored SS1                                                                                                   |
| 281 (0x119) SS1 Request              | Select Safe Stop 1 request.                                                                                                                  | 0 = No Request 1 = Request                                                                                                                               |
| 282 (0x11A) SS1 Active               | Safe Stop 1 function active.                                                                                                                 | 0 = Not Active 1 = Active                                                                                                                                |
| 283 (0x11B) SS1 Fault                | Safe Stop 1 fault.                                                                                                                           | 0 = No Fault 1 = Faulted                                                                                                                                 |
| 284 (0x11C) SS1 Fault Type           | Describes detailed information about the Fault.                                                                                              | 1 = No Fault 2 = Invalid Configuration 3 = Deceleration Rate 4 = Maximum Time 100 = STO Request during SS1 101 = SS1 Request while Feedback not valid    |
|                                      | 285 (0x11D) SS1 Max Stop Time Allowed time to stop.                                                                                          | 0-65535 milliseconds Default = 0                                                                                                                         |
|                                      | 286 (0x11E) SS1 Standstill Speed Defines the speed below which motion is considered stopped.                                                 | Feedback Units / s Default = 0                                                                                                                           |
|                                      | 287 (0x11F) SS1 Stop Monitor Delay Delay before deceleration is monitored.                                                                   | 0-65535 milliseconds Default = 0                                                                                                                         |
|                                      | 288 (0x120) SS1 Decel Ref Rate Minimum rate of deceleration while stopping.                                                                  | Feedback Units / s² 0 = No Decel Check (default)                                                                                                         |
| 289 (0x121) SS1 Activation           | The source of the SS1 activation.                                                                                                            | Bit: 0 = SS1 Request 0 = SS1 Request 1 = Safe Limit Active 2 = Connection Loss 3 = Connection Idle                                                       |
| 290 (0x122) SS1 Decel Ref Tolerance  | Defines the speed tolerance applied to the deceleration ramp check. This attribute is optional in the implementation.                        | Feedback Units/s 2 Default = 0                                                                                                                           |
| 291 (0x123) SS1 Ext Max Stop Time    | Allowed time to stop with extended range to support possibility of long stop times. This attribute is optional in the implementation.        | 0-4294967296 ms Default = 0                                                                                                                              |
| 292 (0x124) SS1 Max Stop Time Source | Selects which Max Stop Time attribute determines the allowed time to stop. Must be supported if optional SS1 Ext Max Stop Time is supported. | 0 = Max Stop Time 1 = Ext Max Stop Time                                                                                                                  |
|                                      | 303 (0x12F) SS2 Fault Safe stop 2 fault.                                                                                                     | 0 = No Fault 1 = Faulted                                                                                                                                 |
|                                      | 304 (0x130) SS2 Fault Type Detailed information about a fault.                                                                               | 1 = No Fault 2 = Invalid Configuration SS2 Function Not Supported                                                                                        |
|                                      | 323 (0x143) SOS Fault Safe Operating Stop fault.                                                                                             | 0 = No Fault 1 = Faulted                                                                                                                                 |
|                                      | 324 (0x144) SOS Fault Type Detailed information about a fault.                                                                               | 1 = No Fault 2 = Invalid Configuration SOS Function Not Supported                                                                                        |
|                                      | 341 (0x155) SMT Fault Safe motor temperature fault.                                                                                          | 0 = No Fault 1 = Faulted                                                                                                                                 |

Table 43 - Safe Stop Function Attributes (Class 0x5A) (Continued)

| Attribute ID Decimal (Hex)   | Attribute Name Attribute Description Values                    |                                                                   |
|------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------|
|                              | 342 (0x156) SMT Fault Type Detailed information about a fault. | 1 = No Fault 2 = Invalid Configuration SMT Function Not Supported |
|                              | 363 (0x16B) SBC Fault Safe brake control fault.                | 0 = No Fault 1 = Faulted                                          |
|                              | 364 (0x16C) SBC Fault Type Detailed information about a fault. | 1 = No Fault 2 = Invalid Configuration SBC Function Not Supported |

## Dual Channel Feedback Attributes

These parameters are set by using the Logix Designer application only when dual-channel feedback is configured. These attributes cannot be individually set by using explicit messaging, but can be read by using a message command.

Table 44 - Dual Channel Feedback Attributes (Class 0x59)

| Attribute ID Decimal (Hex)   |                                   | Attribute Name Attribute Description Values                                                                                                                                                             |                                                                                     |
|------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|                              |                                   | 1 (0x1) Dual Channel Mode Selects the mode for the two channels of the Safety Dual Channel Feedback.                                                                                                    | 0 = Single Feedback 1 = Dual Velocity Check                                         |
| 2 (0x2)                      | Dual Channel Evaluation Status    | Status of the Dual Channel evaluation.                                                                                                                                                                  | 0 = No Discrepancy 1 = Discrepancy Detected                                         |
|                              |                                   | 3 (0x3) Discrepancy Time The time limit at which the input discrepancy becomes an error.                                                                                                                | 0 = No Monitoring (default) 1 to 65535 ms                                           |
|                              | 4 (0x4) Primary Feedback Instance | Instance ID of one of the pair of Safety Feedback instances that forms the Safety Dual Channel Feedback (primary channel).                                                                              | Default = 0, no pairing                                                             |
| 5 (0x5)                      | Secondary Feedback Instance       | Instance ID of the second instance of the dual channel safety feedback pair (secondary channel).                                                                                                        | Default = 0, no pairing                                                             |
|                              | 6 (0x6) Velocity Ratio            | Ratio of velocity from primary channel divided by velocity from secondary channel.                                                                                                                      | Positive REAL value                                                                 |
| 7 (0x7)                      | Velocity Discrepancy Deadband     | Allowed difference for the channel.                                                                                                                                                                     | Default = 0, no Deadband                                                            |
| 8 (0x8)                      | Velocity Discrepancy Measured     | Measured velocity discrepancy.                                                                                                                                                                          | Feedback Units/s                                                                    |
|                              |                                   | 9 (0x9) Velocity Discrepancy Status Status of the Dual Channel evaluation.                                                                                                                              | 0 = No Discrepancy 1 = Discrepancy Detected                                         |
| 110 (0x6E)                   | Discrepancy Checking Active       | Safety Dual Channel Feedback object is supported, configured for dual channel operation, is actively checking primary and secondary feedback data discrepancy, and no discrepancies have been detected. | 0 = Feedback Discrepancy Checking Inactive 1 = Feedback Discrepancy Checking Active |

## Notes:

## Safe Stop 1 (SS1)

Table 45 - SS1 Instruction Checklist

|                  | Test Type Test Description                                                                                                                                                                                                                                | Test Status   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                             |               |
| Normal Operation | Operate the machine at the desired operating system speed.                                                                                                                                                                                                |               |
| Normal Operation | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS1_Name.SpeedLimit •  SS1_Name.DecelerationRamp •  SS1_Name.O1                                                        |               |
| Normal Operation | Initiate SS1 demand.                                                                                                                                                                                                                                      |               |
| Normal Operation | Make sure that the instruction output SS1_Name.01 turns off without generating a fault and that the drive initiates an STO instruction. • Verify that the STO instruction de-energizes the motor for a normal safe condition.                             |               |
| Normal Operation | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status |               |
| Normal Operation | While the system is stopped with the SS1 demand removed, initiate a Reset command of the STO and SS1 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status            |               |

## Safety Function Validation Checklist

Use this appendix to validate your Drive Safety instructions. Each instruction has a checklist with test commands and results to verify for normal operation and abnormal operation scenarios.

| Topic                         |   Page |
|-------------------------------|--------|
| Safe Stop 1 (SS1)             |     93 |
| Safe Stop 2 (SS2)             |     95 |
| Safe Operating Stop (SOS)     |     97 |
| Safely Limited Speed (SLS)    |     99 |
| Safely Limited Position (SLP) |    100 |
| Safe Direction (SDI)          |    101 |
| Safe Feedback Interface (SFX) |    102 |
| Safe Brake Control (SBC)      |    103 |

Use this SS1 instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application. When possible, use immediate operands for instructions to reduce the possibility of systematic errors in your ladder program. Instruction operands must be verified for your safety ladder program.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

Table 45 - SS1 Instruction Checklist (Continued)

|                      | Test Type Test Description                                                                                                                                                                                                                                | Test Status   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|                      | Change the actual motion deceleration rate within the motion task associated with this SS1 function so that it is slower than the calculated speed limit used by the SS1 instruction.                                                                     |               |
|                      | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                             |               |
|                      | Operate machine at the desired operating system speed.                                                                                                                                                                                                    |               |
| Abnormal Operation 1 | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS1_Name.SpeedLimit •  SS1_Name.DecelerationRamp •  SS1_Name.O1                                                        |               |
| Abnormal Operation 1 | Initiate SS1 demand.                                                                                                                                                                                                                                      |               |
| Abnormal Operation 1 | Make sure that the instruction generates a deceleration fault and that the drive initiates an STO instruction. • Verify that the STO instruction de-energizes the motor for a normal safe condition                                                       |               |
| Abnormal Operation 1 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status |               |
| Abnormal Operation 1 | While the system is stopped with the SS1 demand removed, initiate a Reset command of the STO and SS1 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status            |               |
|                      | Change the motion deceleration rate within the motion task associated with this SS1 function so that the stop delay time is exceeded without triggering a deceleration fault.                                                                             |               |
|                      | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                             |               |
|                      | Operate machine at desired operating system speed.                                                                                                                                                                                                        |               |
|                      | Abnormal Operation 2 Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS1_Name.SpeedLimit •  SS1_Name.DecelerationRamp •  SS1_Name.O1                                   |               |
|                      | Initiate SS1 demand.                                                                                                                                                                                                                                      |               |
|                      | Make sure that the instruction generates a maximum time fault and that the drive initiates an STO instruction. • Verify that the STO instruction de-energizes the motor for a normal safe condition                                                       |               |
|                      | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status |               |
|                      | While the system is stopped with the SS1 demand removed, initiate a Reset command of the STO and SS1 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status            |               |

## Safe Stop 2 (SS2)

## Table 46 - SS2 Instruction Checklist

|                  | Test Type Test Description                                                                                                                                                                                                                                                                                                    | Test Status   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                                                                 |               |
| Normal Operation | Operate machine at the desired operating system speed.                                                                                                                                                                                                                                                                        |               |
| Normal Operation | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS2_Name.SpeedLimit •  SS2_Name.DecelerationRamp •  SS2_Name.ActualPosition •  SS2_Name.StandstillSetPoint •  SS2_Name.Output 1                                                            |               |
| Normal Operation | Initiate SS2 demand.                                                                                                                                                                                                                                                                                                          |               |
| Normal Operation | Make sure that while the SS2 instruction is monitoring that the motor decelerates below the SS2_Name.SS2StandstillSpeed setting and then maintains a speed below the SS2_Name.SOSStandstillSpeed (or for position mode, maintains the SS2_Name.StandstillSetpoint without exceeding the SS2_Name.StandstillDeadband setting). |               |
| Normal Operation | While the system is in standstill state and with the sensor subsystems in a safe state, remove the SS2 demand. • Verify proper machine status and safety application program status.                                                                                                                                          |               |
| Normal Operation | Resume normal machine operation. • Verify proper machine status and safety application program status.                                                                                                                                                                                                                        |               |
| Normal Operation | Change the actual motion deceleration rate within the motion task associated with this SS2 function so that it is slower than the calculated speed limit used by the SS2 instruction.                                                                                                                                         |               |
| Normal Operation | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                                                                 |               |
| Normal Operation | Operate machine at the desired operating system speed.                                                                                                                                                                                                                                                                        |               |
| Normal Operation | Abnormal Operation 1 Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS2_Name.SpeedLimit •  SS2_Name.DecelerationRamp •  SS2_Name.ActualPosition •  SS2_Name.StandstillSetPoint •  SS2_Name.Output 1                                       |               |
| Normal Operation | Initiate SS2 demand.                                                                                                                                                                                                                                                                                                          |               |
| Normal Operation | Make sure that the instruction generates a deceleration fault and that the drive initiates an STO instruction. • Verify that the STO instruction de-energizes the motor for a normal safe condition                                                                                                                           |               |
| Normal Operation | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status                                                                     |               |
| Normal Operation | While the system is stopped with the SS1 demand removed, initiate a Reset command of the STO and SS2 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                                                                                |               |

Use this SS2 instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

Table 46 - SS2 Instruction Checklist (Continued)

|                                   | Test Type Test Description                                                                                                                                                                                                                                         | Test Status   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|                                   | Change the motion deceleration rate within the motion task associated with this SS2 function so that the stop delay time is exceeded without triggering a deceleration fault.                                                                                      |               |
|                                   | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                      |               |
|                                   | Operate machine at desired operating system speed.                                                                                                                                                                                                                 |               |
| Abnormal Operation 2              | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS2_Name.SpeedLimit •  SS2_Name.DecelerationRamp •  SS2_Name.ActualPosition •  SS2_Name.StandstillSetPoint •  SS2_Name.Output 1 |               |
|                                   | Initiate SS2 demand.                                                                                                                                                                                                                                               |               |
|                                   | Make sure that the instruction generates a maximum time fault and that the drive initiates an STO instruction. • Verify that the STO instruction de-energizes for a normal safe condition                                                                          |               |
|                                   | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status          |               |
|                                   | While the system is stopped with the SS2 demand removed, initiate a Reset command of the STO and SS2 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                     |               |
|                                   | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                      |               |
|                                   | Operate the machine at maximum (normal) operating system speed.                                                                                                                                                                                                    |               |
|                                   | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS2_Name.SpeedLimit •  SS2_Name.DecelerationRamp •  SS2_Name.ActualPosition •  SS2_Name.StandstillSetPoint                      |               |
| Abnormal Operation 3 (Speed mode) | Initiate SS2 demand.                                                                                                                                                                                                                                               |               |
|                                   | Make sure that while the SS2 instruction is monitoring, that the motor decelerates below the SS2_Name.SS2StandstillSpeed setting and then maintains a speed below the SS2_Name.SOSStandstillSpeed.                                                                 |               |
|                                   | While the system is in the standstill state, initiate a motion command that violates the standstill speed. • Verify that standstill speed fault is generated and STO is initiated • Verify that the STO instruction de-energizes for a normal safe condition       |               |
|                                   | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status          |               |
|                                   | While the system is stopped with the SS2 demand removed, initiate a Reset command of the STO and SS2 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                     |               |

## Table 46 - SS2 Instruction Checklist (Continued)

|                                      | Test Type Test Description                                                                                                                                                                                                                                         | Test Status   |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Abnormal Operation 4 (Position mode) | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                      |               |
| Abnormal Operation 4 (Position mode) | Operate the machine at maximum (normal) operating system speed.                                                                                                                                                                                                    |               |
| Abnormal Operation 4 (Position mode) | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SS2_Name.SpeedLimit •  SS2_Name.DecelerationRamp •  SS2_Name.ActualPosition •  SS2_Name.StandstillSetPoint •  SS2_Name.Output 1 |               |
| Abnormal Operation 4 (Position mode) | Initiate SS2 demand.                                                                                                                                                                                                                                               |               |
| Abnormal Operation 4 (Position mode) | Make sure that while SS2 instruction is monitoring, that the motor maintains the SS2_Name.StandstillSetPoint without exceeding the SS2_Name.StandstillDeadband setting).                                                                                           |               |
| Abnormal Operation 4 (Position mode) | While the system is in the standstill state, initiate a motion command that violates the standstill deadband. • Verify that standstill position fault is generated and STO is initiated • Verify that the STO instruction de-energizes for a normal safe condition |               |
| Abnormal Operation 4 (Position mode) | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status          |               |
| Abnormal Operation 4 (Position mode) | While the system is stopped with the SS2 demand removed, initiate a Reset command of the STO and SS2 instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                     |               |

## Safe Operating Stop (SOS)

## Table 47 - SOS Instruction Checklist

|                  | Test Type Test Description                                                                                                                                                                                                                 | Test Status   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                              |               |
| Normal Operation | Operate machine at the desired operating system speed.                                                                                                                                                                                     |               |
| Normal Operation | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SFX_Name.ActualPosition •  SOS_Name.StandstillSpeed •  SOS_Name.StandstillDeadband •  SOS_Name.Output 1 |               |
| Normal Operation | Initiate SOS demand.                                                                                                                                                                                                                       |               |
| Normal Operation | Make sure that while the SOS instruction maintains a speed below the SOS_Name.StandstillSpeed (or for position mode, maintains position within the SOS_Name.StandstillDeadband setting).                                                   |               |
| Normal Operation | While the system is in standstill state and with the sensor subsystems in a safe state, remove the SOS demand. • Verify proper machine status and safety application program status                                                        |               |
| Normal Operation | Resume normal machine operation. • Verify proper machine status and safety application program status                                                                                                                                      |               |

Use this SOS instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

Table 47 - SOS Instruction Checklist (Continued)

|                                      | Test Type Test Description                                                                                                                                                                                                                                                        | Test Status   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|                                      | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                     |               |
|                                      | Operate machine at the desired operating system speed.                                                                                                                                                                                                                            |               |
|                                      | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SFX_Name.ActualPosition •  SOS_Name.StandstillSpeed •  SOS_Name.StandstillDeadband •  SOS_Name.Output 1                                        |               |
| Abnormal Operation 1 (Speed mode)    | Initiate SOS demand.                                                                                                                                                                                                                                                              |               |
| Abnormal Operation 1 (Speed mode)    | Make sure that the SOS instruction maintains a speed below the SOS_Name.StandstillSpeed .                                                                                                                                                                                         |               |
| Abnormal Operation 1 (Speed mode)    | While the system is in the standstill state, initiate a motion command that violates the SOS_Name.StandstillSpeed. • Verify that the standstill speed fault is generated and that the STO is initiated • Verify that the STO instruction de-energizes for a normal safe condition |               |
| Abnormal Operation 1 (Speed mode)    | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status                         |               |
| Abnormal Operation 1 (Speed mode)    | While the system is stopped with the SOS demand removed, initiate a Reset command of the STO and SOS instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                                    |               |
|                                      | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                     |               |
|                                      | Operate the machine at maximum (normal) operating system speed.                                                                                                                                                                                                                   |               |
|                                      | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualSpeed •  SFX_Name.ActualPosition •  SOS_Name.StandstillSpeed •  SOS_Name.StandstillDeadband •  SOS_Name.Output 1                                        |               |
| Abnormal Operation 2 (Position mode) | Initiate SOS demand.                                                                                                                                                                                                                                                              |               |
| Abnormal Operation 2 (Position mode) | Make sure that the SOS instruction maintains position within the SOS_Name.StandstillDeadband setting.                                                                                                                                                                             |               |
| Abnormal Operation 2 (Position mode) | While the system is in the standstill state, initiate a motion command that violates the SOS_Name.StandstillDeadband. • Verify that standstill position fault is generated and STO is initiated • Verify that the STO instruction de-energizes for a normal safe condition        |               |
| Abnormal Operation 2 (Position mode) | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify that the STO instruction remains de-energized for a normal safe condition • Verify proper machine status and safety application program status                         |               |
| Abnormal Operation 2 (Position mode) | While the system is stopped with the SOS demand removed, initiate a Reset command of the STO and SOS instructions. • Verify that the STO instruction remains de-energized • Verify proper machine status and safety application program status                                    |               |

## Safely Limited Speed (SLS)

Table 48 - SLS Instruction Checklist

|                      | Test Type Test Description                                                                                                                                                                                            | Test Status   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation     | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                         |               |
| Normal Operation     | Operate the machine within the desired speed range.                                                                                                                                                                   |               |
| Normal Operation     | Set up a trend with expected time scale and the following tags to graphically capture this information: SFX_Name.ActualSpeed SLS_Name.SLSLimit SLS_Name.ActiveLimit SLS_Name.Output 1                                 |               |
| Normal Operation     | Initiate SLS demand.                                                                                                                                                                                                  |               |
| Normal Operation     | Verify that the drive achieves the speed below the SLS_Name.ActiveLimit without asserting the SLS_Name.SLSLimit output.                                                                                               |               |
| Normal Operation     | While the system is in SLS monitoring state and with the sensor subsystems in a safe state, remove the SLS demand. • Verify proper machine status and safety application program status                               |               |
| Normal Operation     | Resume normal machine operation. • Verify proper machine status and safety application program status                                                                                                                 |               |
| Abnormal Operation 1 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                         |               |
| Abnormal Operation 1 | Operate the machine within the normal speed range.                                                                                                                                                                    |               |
| Abnormal Operation 1 | Set up a trend with expected time scale and the following tags to graphically capture this information: SFX_Name.ActualSpeed SLS_Name.SLSLimit SLS_Name.ActiveLimit SLS_Name.Output 1                                 |               |
| Abnormal Operation 1 | Initiate SLS demand.                                                                                                                                                                                                  |               |
| Abnormal Operation 1 | Verify that the drive achieves the speed below the SLS_Name.ActiveLimit without asserting the SLS_Name.SLSLimit output.                                                                                               |               |
| Abnormal Operation 1 | While the system is in the SLS monitoring state, initiate a motion command that violates the SLS_Name.ActiveLimit. • Verify that the SLS_Name.SLSLimit output is asserted and the programmed stop action is initiated |               |
| Abnormal Operation 1 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                |               |
| Abnormal Operation 1 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                           |               |

Use this SLS instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application. When possible, use immediate operands for instructions to reduce the possibility of systematic errors in your ladder program. Instruction operands must be verified for your safety ladder program.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Safely Limited Position (SLP) Use this SLP instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application. When possible, use immediate operands for instructions to reduce the possibility of systematic errors in your ladder program. Instruction operands must be verified for your safety ladder program.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Table 49 - SLP Instruction Checklist

|                      | Test Type Test Description                                                                                                                                                                                                                   | Test Status   |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation     | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                |               |
| Normal Operation     | Operate the machine within the desired position range.                                                                                                                                                                                       |               |
| Normal Operation     | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualPosition •  SLP_Name.SLPLimit •  SLP_Name.PositiveTravelLimit •  SLP_Name.NegativeTravelLimit •  SLP_Name.Output 1 |               |
| Normal Operation     | Initiate SLP demand.                                                                                                                                                                                                                         |               |
| Normal Operation     | Verify that the drive achieves and maintains a position between the SLP_Name.PositiveTravelLimit and the SLP_Name.NegativeTravelLimit without asserting the SLP_Name.SLPLimit output.                                                        |               |
| Normal Operation     | While the system is in SLP monitoring state and with the sensor subsystems in a safe state, remove the SLP demand. • Verify proper machine status and safety application program status                                                      |               |
| Normal Operation     | Resume normal machine operation. • Verify proper machine status and safety application program status                                                                                                                                        |               |
| Abnormal Operation 1 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                |               |
| Abnormal Operation 1 | Operate the machine within the desired position range.                                                                                                                                                                                       |               |
| Abnormal Operation 1 | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualPosition •  SLP_Name.SLPLimit •  SLP_Name.PositiveTravelLimit •  SLP_Name.NegativeTravelLimit •  SLP_Name.Output 1 |               |
| Abnormal Operation 1 | Initiate SLP demand.                                                                                                                                                                                                                         |               |
| Abnormal Operation 1 | Verify that the drive achieves and maintains a position between the SLP_Name.PositiveTravelLimit and the SLP_Name.NegativeTravelLimit without asserting the SLP_Name.SLPLimit output.                                                        |               |
| Abnormal Operation 1 | While the system is in the SLP monitoring state, initiate a motion command that violates the SLP_Name.PositiveTravelLimit • Verify that SLP_Name.SLPLimit output is asserted and the programmed stop action is initiated                     |               |
| Abnormal Operation 1 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                                       |               |
| Abnormal Operation 1 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                                  |               |

## Table 49 - SLP Instruction Checklist (Continued)

|                      | Test Type Test Description                                                                                                                                                                                                                   | Test Status   |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Abnormal Operation 2 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                |               |
| Abnormal Operation 2 | Operate the machine within the desired position range.                                                                                                                                                                                       |               |
| Abnormal Operation 2 | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualPosition •  SLP_Name.SLPLimit •  SLP_Name.PositiveTravelLimit •  SLP_Name.NegativeTravelLimit •  SLP_Name.Output 1 |               |
| Abnormal Operation 2 | Initiate SLP demand.                                                                                                                                                                                                                         |               |
| Abnormal Operation 2 | Verify that the drive achieves and maintains a position between the SLP_Name.PositiveTravelLimit and the SLP_Name.NegativeTravelLimit without asserting the SLP_Name.SLPLimit output.                                                        |               |
| Abnormal Operation 2 | While the system is in the SLP monitoring state, initiate a motion command that violates the SLP_Name.NegativeTravelLimit • Verify that SLP_Name.SLPLimit output is asserted and the programmed stop action is initiated                     |               |
| Abnormal Operation 2 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                                       |               |
| Abnormal Operation 2 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                                  |               |

## Safe Direction (SDI)

## Table 50 - SDI Instruction Checklist

|                  | Test Type Test Description                                                                                                                                                                              | Test Status   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Normal Operation | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                           |               |
| Normal Operation | Operate the machine within the desired operating range.                                                                                                                                                 |               |
| Normal Operation | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualPosition •  SDI_Name.SDILimit •  SDI_Name.PositionWindow •  SDI_Name.Output 1 |               |
| Normal Operation | Initiate SDI demand.                                                                                                                                                                                    |               |
| Normal Operation | Verify that motion is in the intended direction and the SDI_Name.SDILimit output is not asserted.                                                                                                       |               |
| Normal Operation | While the system is in SDI monitoring state and with the sensor subsystems in a safe state, remove the SDI demand. • Verify proper machine status and safety application program status                 |               |
| Normal Operation | Resume normal machine operation. • Verify proper machine status and safety application program status                                                                                                   |               |

Use this SDI instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

Table 50 - SDI Instruction Checklist (Continued)

|                      | Test Type Test Description                                                                                                                                                                                                                       | Test Status   |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Abnormal Operation 1 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                    |               |
| Abnormal Operation 1 | Operate the machine within the desired operating range.                                                                                                                                                                                          |               |
| Abnormal Operation 1 | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SFX_Name.ActualPosition •  SDI_Name.SDILimit •  SDI_Name.PositionWindow •  SDI_Name.Output 1                                          |               |
| Abnormal Operation 1 | Initiate SDI demand.                                                                                                                                                                                                                             |               |
| Abnormal Operation 1 | Verify that motion is in the intended direction and the SDI_Name.SDILimit output is not asserted.                                                                                                                                                |               |
| Abnormal Operation 1 | While the system is in the SDI monitoring state, initiate a motion command that violates the SDI_Name.PositionWindow in the unintended direction. • Verify that SDI_Name.SDILimit output is asserted and the programmed stop action is initiated |               |
| Abnormal Operation 1 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                                           |               |
| Abnormal Operation 1 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                                      |               |

## Safe Feedback Interface (SFX)

Table 51 - SFX Instruction Checklist

|                          | Test Type Test Description                                                                                                                                                                                                                                                                              | Test Status   |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|                          | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                                           |               |
|                          | Operate the machine within the normal operating range.                                                                                                                                                                                                                                                  |               |
| Normal Scaling Operation | Set up a trend with the expected time scale and the following tags to graphically compare the motion position and speed from the Main task to the scaled position and speed in the Safety task. •  Axis_Name.ActualPosition •  Axis_Name.ActualSpeed •  SFX_Name.ActualPosition •  SFX_Name.ActualSpeed |               |
| Normal Scaling Operation | Verify that the standard and safety position and speed are correlated as expected.                                                                                                                                                                                                                      |               |
|                          | Initiate a Start command.                                                                                                                                                                                                                                                                               |               |
|                          | Initiate a Homing procedure. • Verify that the Home Position in the SFX instruction is set                                                                                                                                                                                                              |               |
| Normal Homing Operation  | Set up a trend with the expected time scale and the following tags to graphically compare the motion position and speed from the Main task to the scaled position and speed in the Safety task. •  Axis_Name.ActualPosition •  SFX_Name.ActualPosition                                                  |               |
| Normal Homing Operation  | Verify that the standard and safety position are correlated as expected.                                                                                                                                                                                                                                |               |

Use this SFX instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. SFX instruction must be verified within your application. When possible, use immediate operands for instructions to reduce the possibility of systematic errors in your ladder program. Instruction operands must be verified for your safety ladder program.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 51 - SFX Instruction Checklist (Continued)

|                      | Test Type Test Description                                                                                                                                                                                                                                                                              | Test Status   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Abnormal Operation 1 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                                           |               |
| Abnormal Operation 1 | Operate the machine within the normal operating range.                                                                                                                                                                                                                                                  |               |
| Abnormal Operation 1 | Set up a trend with the expected time scale and the following tags to graphically compare the motion position and speed from the Main task to the scaled position and speed in the Safety task. •  Axis_Name.ActualPosition •  Axis_Name.ActualSpeed •  SFX_Name.ActualPosition •  SFX_Name.ActualSpeed |               |
| Abnormal Operation 1 | Verify that the standard and safety position and speed are correlated as expected.                                                                                                                                                                                                                      |               |
| Abnormal Operation 1 | Disconnect the feedback between the motor/encoder and drive.                                                                                                                                                                                                                                            |               |
| Abnormal Operation 1 | Verify the generation of a Fault Type: 100 Feedback Invalid by checking Device_Name.SI.PrimaryFeedbackValid tag.                                                                                                                                                                                        |               |
| Abnormal Operation 1 | Verify the system fault action takes place as configured.                                                                                                                                                                                                                                               |               |
| Abnormal Operation 1 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                                                                                                  |               |
| Abnormal Operation 1 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                                                                                             |               |
| Abnormal Operation 2 | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                                                                                           |               |
| Abnormal Operation 2 | Operate the machine within the normal operating range.                                                                                                                                                                                                                                                  |               |
| Abnormal Operation 2 | Set up a trend with the expected time scale and the following tags to graphically compare the motion position and speed from the Main task to the scaled position and speed in the Safety task. •  Axis_Name.ActualPosition •  Axis_Name.ActualSpeed •  SFX_Name.ActualPosition •  SFX_Name.ActualSpeed |               |
| Abnormal Operation 2 | Verify that the standard and safety position and speed are correlated as expected.                                                                                                                                                                                                                      |               |
| Abnormal Operation 2 | Disconnect the Ethernet cable between the controller and the drive.                                                                                                                                                                                                                                     |               |
| Abnormal Operation 2 | Verify the generation of a Fault Type: 101 Connection Fault by checking the Device_Name.SI.ConnectionFaulted tag.                                                                                                                                                                                       |               |
| Abnormal Operation 2 | Verify the system fault action takes place as configured                                                                                                                                                                                                                                                |               |
| Abnormal Operation 2 | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                                                                                                  |               |
| Abnormal Operation 2 | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                                                                                             |               |

## Safe Brake Control (SBC)

Use this SBC instruction checklist to verify normal operation and the abnormal operation scenarios.

| IMPORTANT   | Perform I/O verification and validation before validating your safety ladder program. When possible, use immediate operands for instructions to reduce the possibility of systematic errors in your ladder program. Instruction operands must be verified for your safety ladder program.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Table 52 - SBC Instruction Checklist

|                    | Test Type Test Description                                                                                                                                                                                                         | Test Status   |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|                    | Verify that the brake feedback is properly wired to the input module as documented.                                                                                                                                                |               |
|                    | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                      |               |
| Normal Operation   | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SBC_Name.BO1 •  SBC_Name.BO2 •  SBC_Name.TOR •  Device_Name.STOOutput                                                   |               |
|                    | Initiate an SBC request and initiate the STO event. • Verify expected coordination of the STO output initiation and the SBC_Name.BO1 and SBC_Name.BO2 outputs • Verify proper machine status and safety application program status |               |
|                    | While the system is stopped, initiate a Start command. • Verify that the system remains de-energized for a normal safe condition • Verify proper machine status and safety application program status                              |               |
|                    | While the system is stopped, initiate a Reset command. • Verify that the system remains de-energized for a normal safe condition • Verify proper machine status and safety application program status                              |               |
|                    | Verify that brake feedback is properly wired to the input module as documented.                                                                                                                                                    |               |
|                    | Initiate a Start command. • Verify that the machine is in a normal machine run condition • Verify proper machine status and safety application program status                                                                      |               |
|                    | Initiate machine function to make sure the brake is released.                                                                                                                                                                      |               |
| Abnormal Operation | Set up a trend with expected time scale and the following tags to graphically capture this information: •  SBC_Name.BO1 •  SBC_Name.BO2 •  SBC_Name.TOR •  Device_Name:STOOutput                                                   |               |
|                    | Remove brake feedback wires from the input module.                                                                                                                                                                                 |               |
|                    | • Verify that the appropriate diagnostic code is generated • Verify that the brake output SBC_Name.BO1 and SBC_Name.BO2 bits clear • Verify the external brake engagement                                                          |               |
|                    | While the system is stopped with the sensor subsystems in a safe state, initiate a Start command. • Verify proper machine status and safety application program status                                                             |               |
|                    | While the system is stopped, initiate a Reset command. • Verify proper machine status and safety application program status                                                                                                        |               |

## 1oo2

## Numerics

definition 6

## A

actions 39

application requirements 31

assembly tags 29

84

85

input output associated axes 34

## attributes

dual channel feedback 91

feedback 86

safe stop

88

axis tags 17

motion connection 81

## C

## category 3

stop category definitions 11

## certification

application requirements PL and SIL 11 TÜV Rheinland 10 , 65

31

user responsibilities 11

## CIP

definition 6

## compatible safety controllers 13

## configure

action 39

associated axes 34

discrepancy checking 47

discrepancy checking example 48

dual feedback example 54

general 33

hardwired 36

module definition 35

motion safety instance 37

networked 36

primary feedback 40

primary feedback example 51 , 59

safety connection 36

safety input 38

safety output 38

scaling 44

scaling example 45 , 46

secondary feedback 44

STO 49

velocity average time 42

velocity resolution 44

controller tags 30

## controller-based

instructions 65

monitoring functions stopping functions 9

9

## D

## decel rate fault 27 discrepancy

checking

47

checking example 48

downloads 32

## drive safety instructions 65

adding instruction 66

example 67

homing 70

pass through data 68

SFX instruction 69

tab 66

## drive-based stopping functions

monitored SS1 9

timed SS1 9

DSL

definition 6

dual

channel feedback attributes 91 feedback example 54

## E

## EN

definition 6

explicit messages 18

## F

## fault

actions 39

codes 77

names 74

faults

76 , 77

safety core 74

SS1 75

SS2, SOS, SBC, SLS, SLP, SDI 75

STO 74

## feedback

attributes 86

types 62

## G

## general 33

GuardLogix controllers 9 , 23

## H

hardwired 36

HFT

definition 6

homing 70

## I

## IEC

definition 6

IEC 60204-1 24

IEC 61508 11 , 23

IEC 61800-5-2 11 , 23

IEC 62061 11 , 23

IGBT

definition 6

input assembly tags 18 , 84

integrated

STO 9

STO mode

STO state reset 78

STO mode operation 29

## ISO

definition 6

ISO 13849-1 23

ISO 13849-1 CAT 3

stop category definitions 11

## L

## Logix Designer

controller tags 30

## M

module definition 35

monitored SS1 9 , 31

definition 6

drive based 24

request removed 28

with fault 27

## motion

and safety connection 16 connection 17 connection axis tags 17 connection tags 81 safety instances 14 , 16 , 37

task 14 , 16

## N

networked 36

## O

out of box state 20

output assembly tags 18 , 85

## P

## pass through

data 17 , 68

PCDC download 32

PES

definition 6

definition 6

proof test interval 11

PFH definition 11

PL

definition 6

PFH

## primary

encoder 16

feedback 40

feedback example 51 , 59

proof test interval 11

## R

## ramp monitor function 25

example 26

reaction time 32

restore hardwired STO mode 20

## S

## safe motion monitoring 12

configuration 13

## safe stop function

assembly tags 29

attributes 88

monitored SS1 (drive based) 24

timed SS1 (drive based) 23

## safe torque-off

STO mode 78

out of box state 20

integrated PFH 11

## safety

controllers 13

core fault 74

feedback 76

feedback faults 76

function 15

input 38

output 38

reaction time 32

supervisor state 19

task 14 , 16

## safety connection 18 , 36

input assembly tags 18

output assembly tags 18

SBC 104

fault 75

validation checklist 104

## scaling 44

example 45 , 46

SFX 70

SDI 101

fault 75

validation checklist 101

## secondary

encoder 16

feedback 44

SFX 15 , 102

instruction 69

scaling

70

validation checklist 102

## SIL rating

definition 6

feedback types 62

monitored SS1 31

timed SS1 31

## SLP 100

fault 75

validation checklist 100

## SLS 99

fault 75 validation checklist 99

SOS 97

fault 75 validation checklist 97

SS1 15 93

, fault 75

validation checklist 93

SS1-r

SS1-t definition 6

SS2 95

fault 75 validation checklist 95

STO 49

fault 74 integrated 9 restore hardwired mode 20 SIL rating 31 state reset 78

## stop

definition 6

category 0 24

category 1 15

## T

## timed

SS1 9 , 31

SS1 (drive based) 23

SS1 definition 6

## timing diagram

decel rate fault 27 monitored SS1 25 request removed 28 timed SS1 24

## troubleshooting 77

## V

validation checklist 93 , 95 , 97 , 99 , 100 , 101 , 102 ,

104

## velocity

average time 42 resolution 44

## W

## website

product downloads 32

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

Allen-Bradley, CompactLogix, ControlLogix, expanding human possibility, GuardLogix, Integrated Architecture, Kinetix, Logix 5000, POINT Guard I/O, Rockwell Automation, Stratix, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

EtherNet/IP, CIP, CIP Safety, and CIP Motion are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIAPACIFIC:RockwellAutomation,Level14,CoreF,Cyberport3,100CyberportRoad,HongKong,Tel:(852）28874788,Fax:(852)25081846 UNITEDKINGD0M:RockwellAutomationLtd.Pitfield,KilnFarmMiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)（1908)838-800,Fax:(44)(1908)261-917