## PowerFlex 750-Series AC Drives

Catalog Numbers 20F, 20G, 21G

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Original Instructions

<!-- image -->

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

## IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

## New and Updated Information

This manual contains new and updated information.

This table contains the changes made to this revision.

| Topic                                                                              |   Page |
|------------------------------------------------------------------------------------|--------|
| Added information about 270 kW, 400 HP drives to the table of minimum resistances. |    214 |

## Notes:

Preface

| Overview            | Who Should Use This Manual . . .  . . . . . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . 9           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
|                     | What Is Not in This Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                     |                                             |
|                     | Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . . . . . . . . . . 9   |
|                     | Allen-Bradley Drives Technical Support . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                                |                                             |
|                     | Product Certification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11              |                                             |
|                     | Manual Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                |                                             |
|                     | General Precautions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12             |                                             |
|                     | Studio 5000 Environment . . . . . . .  . . . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . . 14            |
|                     | Chapter 1                                                                                                                      |                                             |
| Drive Configuration | Accel/Decel Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16            |                                             |
|                     | Adjustable Voltage . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . 17        |
|                     | Auto Restart . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . . . . 25  |
|                     | Auto/Manual . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . 27        |
|                     | Automatic Device Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34                          |                                             |
|                     | Autotune . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . 35      |
|                     | Auxiliary Power Supply . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 41          |
|                     | Bus Regulation . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . . . . . 41  |
|                     | Configurable Human Interface Module Removal . . . . . . . . . . . . . . . . . . . 52                                           |                                             |
|                     | Droop Feature . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . 53              |
|                     | Duty Rating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53       |                                             |
|                     | Feedback Devices. . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . 54  |
|                     | Flying Start . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . 54                |
|                     | Hand-Off-Auto . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . 64  |
|                     | Masks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 |                                             |
|                     | Owners. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70   |                                             |
|                     | Power Loss . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . 72      |
|                     | Process PID Loop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76            |                                             |
|                     | Reset Parameters to Factory Defaults . . . . . . . . . . . . . . . . .                                                         | . . . . . . . . . . . . . . 88              |
|                     | Sleep/Wake Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90               |                                             |
|                     | Start Permissives . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . . 94  |
|                     | Stop Modes . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . 96      |
|                     | Voltage Class . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . . 104 |
|                     | Chapter 2                                                                                                                      |                                             |
| Feedback and I/O    | Analog Inputs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105         |                                             |
|                     | Analog Outputs . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . 113   |
|                     | Digital Inputs . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . . 119     |
|                     | Digital Outputs . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . 130 |
|                     | PTC Motor Thermistor Input . . .  . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . . . 152           |

## Table of Contents

Chapter 3

| Diagnostics and Protection   | Alarms . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . 155       |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
|                              | Current Limit . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . . 156     |
|                              | DC Bus Voltage/Memory. . . . . . .  . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . . . . . 158               |
|                              | Drive Overload . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . 158           |
|                              | Faults . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . . . 162       |
|                              | Input Phase Loss Detection . . . . .  . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . 166               |
|                              | Motor Overload. . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . 168       |
|                              | Overspeed Limit . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . . 172           |
|                              | Password . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173   |                                                 |
|                              | Real Time Clock . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . . . . . . . 174     |
|                              | Reflected Wave . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . 179           |
|                              | Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185 |                                                 |
|                              | Shear Pin . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . 188                   |
|                              | Slip Compensation . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . 192             |
|                              | Slip Regulator. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . 194         |
|                              | Chapter 4                                                                                                                    |                                                 |
| Motor Control                | Carrier (PWM) Frequency. . . . . .  . . . . . . . . . . . . . . . . . .                                                      | . . . . . . . . . . . . . . . 196               |
|                              | Dynamic Braking. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . 197           |
|                              | Flux Braking . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . 216         |
|                              | Flux Regulator . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . . 218         |
|                              | Flux Up . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . . . . 218       |
|                              | High Resolution Feedback .  . . . . . . . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . 220         |
|                              | Inertia Adaption . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . 221           |
|                              | Inertia Compensation . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 223             |
|                              | Load Observer . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . . 225     |
|                              | Motor Control Modes . . . .  . . . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . . . . . 226         |
|                              | Motor Types. . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . . . . . 235     |
|                              | Notch Filter . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . . . . 244 |
|                              | Regen Power Limit . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . . 247           |
|                              | Speed Reference. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . 251           |
|                              | Speed Regulation. . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . . . . . 260       |
|                              | Torque Reference . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . 262       |
|                              | Speed Torque Position. . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 266             |
|                              | Chapter 5                                                                                                                    |                                                 |
| Drive Features               | Data Logging . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . . . . . 277     |
|                              | Energy Savings . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . . . . . 282     |
|                              | High Speed Trending. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 283             |
|                              | Position Homing. . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . 292       |

Chapter 6

| Integrated Motion on the EtherNet/   | Additional Resources for Integrated Motion on the                                                 |                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------|
| IP Network Applications for          | EtherNet/IP Network Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300 |                                           |
| PowerFlex 755 AC Drives              | Coarse Update Rate . . . .  . . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . 301 |
|                                      | Control Modes for PowerFlex 755 Drives Operating on the                                           |                                           |
|                                      | Integrated Motion on the EtherNet/IP Network . . . . . . . . . . . . . . . . . . 301              |                                           |
|                                      | Drive Nonvolatile (NV) Memory for Permanent Magnet Motor                                          |                                           |
|                                      | Configuration . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . . . 308     |
|                                      | Dual Loop Control. . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . . 309     |
|                                      | Dual-Port EtherNet/IP Option Module (ETAP) . . . . . . . . . . . . . . . . . . 315                |                                           |
|                                      | Hardware Over Travel Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316   |                                           |
|                                      | Integrated Motion on EtherNet/IP Instance to PowerFlex 755 Drive                                  |                                           |
|                                      | Parameter Cross-Reference. . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 317       |
|                                      | Motor Brake Control. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 338       |
|                                      | Network Topologies. . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . 341 |
|                                      | PowerFlex 755 and Kinetix 7000 Drive Overload Rating                                              |                                           |
|                                      | Comparison for Permanent Magnet Motor Operation . . . . . . . . . . . . . 345                     |                                           |
|                                      | PowerFlex 755 Drive Option Module Configuration                                                   |                                           |
|                                      | and Restrictions . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . . . . . 346     |
|                                      | Regenerative/Braking Resistor. . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 347         |
|                                      | Safe Speed Monitor Option Module (20-750-S1) Configuration . . . . 350                            |                                           |
|                                      | Speed Limited Adjustable Torque (SLAT) . . . . . . . . . . . . . . . . . . . . . . . . 353        |                                           |
|                                      | Supported Motors. . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 357     |
|                                      | System Tuning . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . . . 363     |
|                                      | Using an Incremental Encoder with an MPx Motor . . . . . . . . . . . . . . . . 372                |                                           |
|                                      | PowerFlex 755 Integrated Motion on the EtherNet/IP                                                |                                           |
|                                      | Network Block Diagrams . .  . . . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . 375   |

## Notes:

## Who Should Use This Manual

## What Is Not in This Manual

## Additional Resources

## Overview

The purpose of this manual is to provide detailed information including operation, parameter descriptions, and programming.

This manual is intended for qualified personnel. You must be able to program and operate Adjustable Frequency AC Drive devices. In addition, you must have an understanding of the parameter settings and functions.

The purpose of this manual is to provide detailed drive information including operation, parameter descriptions and programming.

The following table lists publications that provide information about PowerFlex 750-Series drives.

| Resource                                                                                           | Description                                                                                                                                                |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 750-Series Drive Installation Instruction, 750- IN001                                    | Provides the basic steps required to install a PowerFlex® 750-Series AC drive.                                                                             |
| PowerFlex 750-Series AC Drives Programming Manual, publication 750-PM001                           | Provides detailed information on: •  I/O, control, and feedback options •  Parameters and programming •  Faults, alarms, and troubleshooting               |
| PowerFlex 750-Series AC Drives Technical Data, publication 750-TD001                               | Provides detailed information on: •  Drive specifications •  Option specifications •  Fuse and circuit breaker ratings                                     |
| PowerFlex 20-HIM-A6 / -C6S HIM (Human Interface Module) User Manual, publication 20HIM-UM001       | Provides detailed information on HIM components, operation, features.                                                                                      |
| PowerFlex 750-Series AC Drives Hardware Service Manual - Frame 8 and Larger, publication 750-TG001 | Provides detailed information on: •  Preventive maintenance •  Component testing •  Hardware replacement procedures                                        |
| PowerFlex 755 Drive Embedded EtherNet/IP Adapter User Manual, publication 750COM-UM001             | These publications provide detailed information on configuring, using, and troubleshooting PowerFlex 750-Series communication option modules and adapters. |
| PowerFlex 750-Series Drive DeviceNet Option Module User Manual, publication 750COM-UM002           | These publications provide detailed information on configuring, using, and troubleshooting PowerFlex 750-Series communication option modules and adapters. |
| PowerFlex 7-Class Network Communication Adapter User Manuals, publications 750COM-UMxxx            | These publications provide detailed information on configuring, using, and troubleshooting PowerFlex 750-Series communication option modules and adapters. |

|                                                                                                                    | Resource Description                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 750-Series Safe Torque Off User Manual, publication 750-UM002                                            | These publications provide detailed information on installation, set up, and operation of the 750-Series safety option modules. |
| Safe Speed Monitor Option Module for PowerFlex 750-Series AC Drives Safety Reference Manual, publication 750-RM001 | These publications provide detailed information on installation, set up, and operation of the 750-Series safety option modules. |
| Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001                | Provides basic information needed to properly wire and ground PWM AC drives.                                                    |
| PowerFlex AC Drives in Common Bus Configurations, publication DRIVES-AT002                                         | Provides basic information needed to properly wire and ground common bus PWM AC drives.                                         |
| Safety Guidelines for the Application, Installation and Maintenance of Solid State Control, publication SGI-1.1    | Provides general guidelines for the application, installation, and maintenance of solid-state control.                          |
| A Global Reference Guide for Reading Schematic Diagrams, publication 100-2.10                                      | Provides a simple cross-reference of common schematic/ wiring diagram symbols used throughout various parts of the world.       |
| Guarding Against Electrostatic Damage, publication 8000- 4.5.2                                                     | Provides practices for guarding against Electrostatic damage (ESD)                                                              |
| Product Certifications website, http://ab.com                                                                      | Provides declarations of conformity, certificates, and other certification details.                                             |

The following publications provide necessary information when applying the Logix Processors.

|                                                                                       | Resource Description                                                                                                                                         |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Logix5000 Controllers Common Procedures, publication 1756-PM001                       | This publication links to a collection of programming manuals that describe how you can use procedures that are common to all Logix5000 controller projects. |
| Logix5000 Controllers General Instructions, publication 1756-RM003                    | Provides a programmer with details about each available instruction for a Logix-based controller.                                                            |
| Logix5000 Controllers Process Control and Drives Instructions, publication 1756-RM006 | Provides a programmer with details about each available instruction for a Logix-based controller.                                                            |

The following publications provide information that is useful when planning and installing communication networks.

|                                                                               | Resource Description                                                                    |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ContolNet Coax Tap Installation Instructions, publication 1786-5.7            | Provides procedures and specifications for the installation of ControlNet coaxial taps. |
| ContolNet Fiber Media Planning and Installation Guide, publication CNET-IN001 | Provides basic information for fiber cable planning and installation.                   |

You can view or download publications at http://www.rockwellautomation.com/literature. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Allen-Bradley Drives Technical Support

## Product Certification

## Manual Conventions

Use one of the following methods to contact Automation and Control Technical Support.

| Online   | Email                                                                   | Telephone   |
|----------|-------------------------------------------------------------------------|-------------|
|          | www.ab.com/support/abdrives support@drives.ra.rockwell.com 262-512-8176 |             |

| Title                                 | Online                                              |
|---------------------------------------|-----------------------------------------------------|
| Rockwell Automation Technical Support | http://support.rockwellautomation.com/knowledgebase |

Product Certifications and Declarations of Conformity are available on the internet at www.rockwellautomation.com/products/certification .

- In this manual we refer to PowerFlex 750-Series Adjustable Frequency AC Drives as: drive, PowerFlex 750, PowerFlex 750 drive or PowerFlex 750 AC drive.
- Specific drives within the PowerFlex 750-Series can be referred to as:
- – PowerFlex 753, PowerFlex 753 drive or PowerFlex 753 AC drive
- – PowerFlex 755, PowerFlex 755 drive or PowerFlex 755 AC drive
- To help differentiate parameter names and LCD display text from other text, the following conventions are used:
- – Parameter Names appear in [brackets] after the Parameter Number. For example: P308 [Direction Mode].
- – Display text appears in "quotes." For example: "Enabled."
- The following words are used throughout the manual to describe an action.

| Word       | Meaning                                |
|------------|----------------------------------------|
| Can        | Possible, able to do something         |
| Cannot     | Not possible, not able to do something |
| May        | Permitted, allowed                     |
| Must       | Unavoidable, you must do this          |
| Shall      | Required and necessary                 |
| Should     | Recommended                            |
| Should Not | Not recommended                        |

## General Precautions

## Qualified Personnel

<!-- image -->

ATTENTION: Only qualified personnel familiar with adjustable frequency AC drives and associated machinery should plan or implement the installation, start-up and subsequent maintenance of the system. Failure to comply may result in personal injury and/or equipment damage.

## Personal Safety

<!-- image -->

ATTENTION: To avoid an electric shock hazard, verify that the voltage on the bus capacitors has discharged completely before servicing. Check the DC bus voltage at the Power Terminal Block by measuring between the +DC and -DC terminals, between the +DC terminal and the chassis, and between the -DC terminal and the chassis. The voltage must be zero for all three measurements.

Hazard of personal injury or equipment damage exists when using bipolar input sources. Noise and drift in sensitive input circuits can cause unpredictable changes in motor speed and direction. Use speed command parameters to help reduce input source sensitivity.

Risk of injury or equipment damage exists. DPI or SCANport™ host products must not be directly connected together via 1202 cables. Unpredictable behavior can result if two or more devices are connected in this manner.

The drive start/stop/enable control circuitry includes solid state components. If hazards due to accidental contact with moving machinery or unintentional flow of liquid, gas or solids exists, an additional hardwired stop circuit may be required to remove the AC line to the drive. An auxiliary braking method may be required.

Hazard of personal injury or equipment damage due to unexpected machine operation exists if the drive is configured to automatically issue a Start or Run command. Do not use these functions without considering applicable local, national and international codes, standards, regulations or industry guidelines.

## Product Safety

<!-- image -->

ATTENTION: An incorrectly applied or installed drive can result in component damage or a reduction in product life. Wiring or application errors such as under sizing the motor, incorrect or inadequate AC supply, or excessive surrounding air temperatures may result in malfunction of the system.

This drive contains ESD (Electrostatic Discharge) sensitive parts and assemblies. Static control precautions are required when installing, testing, servicing or repairing this assembly. Component damage may result if ESD control procedures are not followed. If you are not familiar with static control procedures, reference Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD protection handbook.

Configuring an analog input for 0-20 mA operation and driving it from a voltage source could cause component damage. Verify proper configuration prior to applying input signals.

A contactor or other device that routinely disconnects and reapplies the AC line to the drive to start and stop the motor can cause drive hardware damage. The drive is designed to use control input signals to start and stop the motor. If an input device is used, operation must not exceed one cycle per minute or drive damage will occur.

Drive must not be installed in an area where the ambient atmosphere contains volatile or corrosive gas, vapors or dust. If the drive is not going to be installed for a period of time, it must be stored in an area where it will not be exposed to a corrosive atmosphere.

## Class 1 LED Product

<!-- image -->

ATTENTION: Hazard of permanent eye damage exists when using optical transmission equipment. This product emits intense light and invisible radiation. Do not look into module ports or fiber optic cable connectors.

## Studio 5000 Environment

The Studio 5000™ Engineering and Design Environment combines engineering and design elements into a common environment. The first element in the Studio 5000 environment is the Logix Designer application. The Logix Designer application is the rebranding of RSLogix™ 5000 software and will continue to be the product to program Logix5000™ controllers for discrete, process, batch, motion, safety, and drive-based solutions.

<!-- image -->

The Studio 5000 environment is the foundation for the future of Rockwell Automation® engineering design tools and capabilities. This environment is the one place for design engineers to develop all of the elements of their control system.

## Drive Configuration

| Topic                                       |   Page |
|---------------------------------------------|--------|
| Accel/Decel Time                            |     16 |
| Adjustable Voltage                          |     17 |
| Auto Restart                                |     25 |
| Auto/Manual                                 |     27 |
| Automatic Device Configuration              |     34 |
| Autotune                                    |     35 |
| Auxiliary Power Supply                      |     41 |
| Bus Regulation                              |     41 |
| Configurable Human Interface Module Removal |     52 |
| Droop Feature                               |     53 |
| Duty Rating                                 |     53 |
| Feedback Devices                            |     54 |
| Flying Start                                |     54 |
| Hand-Off-Auto                               |     64 |
| Masks                                       |     67 |
| Owners                                      |     70 |
| Power Loss                                  |     72 |
| Process PID Loop                            |     76 |
| Reset Parameters to Factory Defaults        |     88 |
| Sleep/Wake Mode                             |     90 |
| Start Permissives                           |     94 |
| Stop Modes                                  |     96 |
| Voltage Class                               |    104 |

<!-- image -->

## Accel/Decel Time

You can configure the drive's acceleration time and deceleration time.

## Acceleration Time

P535[Accel Time 1] and P536 [Accel Time 2] set the acceleration rate for all speed changes. Defined as the time to accelerate from 0 to motor nameplate frequency P27 [Motor NP Hertz] or to motor nameplate rated speed P28 [Motor NP RPM]. The setting of Hertz or RPM is programmed in P300 [Speed Units]. Selection between Acceleration Time 1 and Acceleration Time 2 is controlled by a digital input function (see Digin Functions in the PowerFlex 750Series Programming Manual, publication 750-PM001) or by Logic Command (sent over a communication network or DeviceLogix™ software).

Adjustment range is 0.00 to 3600.00 seconds.

## Deceleration Time

P537 [Decel Time 1] and P538 [Decel Time 2] set the deceleration rate for all speed changes. Defined as the time to decelerate from motor nameplate frequency P27 [Motor NP Hertz] or from motor nameplate rated speed P28 [Motor NP RPM] to 0. The setting of Hertz or RPM is programmed in P300 [Speed Units]. Selection between Deceleration Time 1 and Deceleration Time 2 is controlled by a digital input function (see Digin Functions in the PowerFlex 750-Series Programming Manual, publication 750-PM001) or by Logic Command (sent over a communication network or DeviceLogix software).

Adjustment range is 0.00 to 3600.00 seconds.

## Adjustable Voltage

As standard AC drive applications are expanding into new markets, new control methods are required to meet these market demands for electromagnetic applications. Some of these applications, listed below, use non-motor or nonstandard motors that require independent control of load frequency and voltage.

- Vibration welding
- Induction heating
- Power supplies
- Vibratory feeders or conveyors
- Electromagnetic stirring
- Resistive loads

Standard inverter control modes consist of volts per hertz (V/Hz), with boost selections, speed feedback selection, fan, pump, and economize, flux vector (FV), with encoder and encoder less modes. The control of the output voltage/ frequency relationship of the variable frequency inverter must be maintained in the linear and nonlinear (over-modulation) regions. Voltage linearity is achieved by maintaining a constant voltage/frequency ratio over the entire operating region. The variable frequency inverter must deliver an adjustable-frequency alternating voltage whose magnitude is related to the output frequency. As the linear-to-nonlinear transition begins, the control must compensate for the lost voltage and deliver a linear output voltage profile.

In adjustable voltage control mode, the output voltage is controlled independently from the output frequency. The voltage and frequency components have independent references and acceleration/deceleration rates.

The adjustable voltage control mode operation enables separate control of the output voltage and the output frequency for use on applications that are typically non-motor types. The voltage and frequency components have independent references and independent acceleration and deceleration rates. Both the voltage and frequency can be set to any point within their respective range. The following graph illustrates these functional ranges.

<!-- image -->

## Overview

Adjustable voltage control is enabled by setting P35 [Motor Ctrl Mode] to option 9 "Adj VltgMode." This feature provides either three-phase and singlephase output voltage. The default mode is three-phase output voltage and is selected by P1131 [Adj Vltg Config]. In single-phase mode the drive is not designed to operate single phase motors, but rather the output load is considered to have a lagging or unity power factor consisting of resistance and inductance for specially designed motor or non-motor application.

Input reference sources can be configured from P1133 [Adj Vltg Select]. The input source can be scaled and upper when lower limits are applied. A trim source can be selected reference from P1136 [Adj Vltg TrimSel] with the trim voltage added or subtracted from the voltage reference.

The scalar frequency selection and scalar frequency ramp are the same components as used in all other control modes. The exception being the frequency command and ramp are decoupled from the voltage generation for the adjustable voltage control mode to provide an independent frequency ramp. Acceleration and deceleration rates and S Curve are the same as used in all other modes. Upper and lower limits are applied to the value of the output command frequency.

The adjustable voltage control voltage ramp provides an independent voltage ramp decoupled from the scalar frequency ramp and controlled by user selectable acceleration and deceleration ramp times. There is also an adjustable percent S Curve feature.

The current limit function reduces the output voltage when the current limit is exceeded. Minimum and maximum voltage limits are applied so the output voltage is never operated outside that range.

## Adjustable Voltage Control Setup

The following examples of setups for the Adjustable Voltage Control mode are a starting point for configuration. Applications can be unique and require specific parameter settings. These examples are base case only.

Table 1 - Basic Adjustable Voltage Control Parameters

|      | Parameter No. Parameter Name Setting Description   |                                                                                                |
|------|----------------------------------------------------|------------------------------------------------------------------------------------------------|
|   35 |                                                    | Motor Ctrl Mode 9 “Adj VltgMode” Adjustable Voltage feature is used in non-motor applications. |
| 1131 | Adj Vltg Config 1                                  | 1 = 3-Phase Operation, 0 = 1-Phase Operation                                                   |
| 1133 | Adj Vltg Select Preset 1                           |                                                                                                |
| 1134 | Adj Vltg Ref Hi 100                                | Percent                                                                                        |
| 1140 | Adj Vltg AccTime                                   | n Secs Application dependent                                                                   |

|      | Parameter No. Parameter Name Setting Description   |       |                                                                                                                                                                  |
|------|----------------------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1141 | Adj Vltg DecTime                                   |       | n Secs Application dependent                                                                                                                                     |
| 1142 | Adj Vltg Preset1                                   | n VAC | Application dependent                                                                                                                                            |
| 1153 | Dead Time Comp                                     | n %   | Vary from 0% to 100%. Dead Time Comp is best set to 0% when output of the Sine wave Filter is fed into a transformer, to prevent or minimize DC Offset voltages. |

Refer to the PowerFlex 750-Series Programming Manual, publication 750PM001, for parameter descriptions and defaults.

When using sine wave or dv/dt filters, the PWM frequency must match the filter design. The drive's thermal protection changes the PWM frequency if over temperature conditions are detected. Set P420 [Drive OL Mode] to option 1 "Reduce CLmt" and P38 [PWM Frequency] to the filter instructions.

## Additional Parameter Changes

When using adjustable voltage control it is necessary to change additional parameters beyond the feature itself. Use this table to assist in setting these parameters.

Table 2 - Adjustable Voltage Applications Parameter Settings

|    | Parameter No. Parameter Name Setting Description   |                                                                                                                                                                                                                                                   |
|----|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 38 |                                                    | PWM Frequency 2 kHz or 4 kHz Match the setting with filter tuning.                                                                                                                                                                                |
| 40 |                                                    | Mtr Options Cfg Bit 5 = 0 Reflected wave is turned off so that there are no missing pulses in the output voltage waveform and to minimize any offsets that can appear.                                                                            |
| 40 |                                                    | Bit 8 = 1 AsyncPWMLock is on because the filter is tuned to the carrier frequency. The carrier frequency must be fixed, if it changes the filter will not work. Also, set the PWM frequency match filter tuning, either 2 kHz or 4 kHz.           |
| 40 |                                                    | Bit 9 = 1 PWM Freq Lock is on because the filter is tuned to the carrier frequency. The carrier frequency must be fixed, if it changes the filter will not work. Also, set the PWM frequency match filter tuning, either 2 kHz or 4 kHz.          |
| 40 |                                                    | Bit 11 = 0 The “Elect Stab” bit affects angle stability and voltage stability. Angle stability gain is set for 0 so it does not compensate for the current going into the filter’s caps. Voltage stability gain is set for 0 for the same reason. |
| 40 |                                                    | Bit 12 = 0 Transistor diagnostics is turned off because that sequence of turning transistors on and off charges the caps in the filter and can cause an IOC trip.                                                                                 |
| 43 | Flux Up Enable 0                                   | Leave at the “Manual” setting.                                                                                                                                                                                                                    |
| 44 |                                                    | Flux Up Time Default Leave at 0.0000 seconds.                                                                                                                                                                                                     |

|      | Parameter No. Parameter Name Setting Description   |                                                                                                                                 |
|------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|   60 | Start Acc Boost 0                                  | Set if there are DC offset voltages at load transformer input windings.                                                         |
|   61 | Run Boost 0                                        | Set if there are DC offset voltages at load transformer input windings.                                                         |
|   62 | Break Voltage 0                                    | Set if there are DC offset voltages at load transformer input windings.                                                         |
|   63 | Break Frequency 0                                  | Set if there are DC offset voltages at load transformer input windings.                                                         |
|  420 |                                                    | Drive OL Mode 1 “Reduce CLmt” Drive OL mode is set for reduce current limit, and not the PWM frequency as it must remain fixed. |
| 1154 |                                                    | DC Offset Ctrl 1 “Enable” This turns off any offset control programmed in the firmware.                                         |

Modulation mode is default at space vector only because 2-phase modulation will degrade the filter's performance.

| IMPORTANT   | Do not autotune.   |
|-------------|--------------------|

## Application Considerations

Whatever the device the user wants to connect to the drive by using the adjustable voltage feature, that device has some type of rating associated with it. As a minimum it needs to have a current rating and voltage rating. Drive selection is based on those ratings.

## Sizing

First, consider the voltage rating of the drive. Determine what the available line voltage is and select a drive voltage rating to match. Next, select a drive that supplies the current necessary for the device's rating.

## Single Phase Output

Consult Rockwell Automation before configuring a drive for single phase adjustable voltage output. Derating of the drive is necessary because of stress on the DC bus capacitor or the IGBT switching losses. When PWM is applied to a resistor, the current changes state following the voltage. For each PWM voltage pulse the current is pulsing the same way. This rapid change in current is not designed into the IGBT selection for the drive. Therefore, some sort of derating needs to be applied. Somewhere around 67% derating. When in this mode, actual losses must be measured to determine a derating percentage. Adding a reactor in series with the resistor can help by adding inductance and rounding off the corners of the current pulses. Depending on how much inductance is added, the waveform can look like a sine wave.

This is a plot showing output voltage, output current, and DC Bus voltage. Here you can see the current following the voltage in a typical PWM output.

<!-- image -->

This plot enlarges some of the pulses to see the current and its shape.

Notice the tops have an abrupt change to them. Any rounding of the wave form at the top is due to the type of resistor used. The resistors used for this plot are the grid type resistors where the resistor element is coiled along its length, adding a certain amount of inductance. This inductance helps round over the leading edge of the current.

Single Phase - PWM into Resistor - No Reactor

<!-- image -->

-0.005

Below is the same plot with a reactor added in series. These waveform look like a sine wave and that is a function of how much inductance is added. However, the increased voltage drop must be accounted for.

<!-- image -->

Another option is to have a sine wave filter in the circuit. This lets unshielded cable to be used without the worry of PWM generated noise being injected into the facility. The cost of shielded cable versus a sine wave filter, Among other factors, has to be weighed.

When using single phase operation, connect the load to the U and V phases. The W phase is energized but is not used.

Enter your maximum current into the Motor NP Amps parameter. Also use this value in the Current Limit parameter. When started the drive attempts to ramp to the commanded voltage. If current limit is hit, the drive levels off or reduce the voltage to satisfy the current limit.

Notice the DC Bus voltage ripple in two of the plots above. If this ripple is high enough in magnitude, it can cause the drive to trip on an Input Phase Loss fault. This is due to the drive monitoring the bus ripple and if a certain delta between max volts and min volts exists for a certain amount of time, the drive assumes an input phase was lost. This fault can be disabled by setting P462 [InPhase LossActn] to option 0 "Ignore."

## Three Phase Output

If you are driving as resistive load, configure it in a three phase arrangement to avoid using the single phase mode of adjustable voltage. Use a sine wave filter to keep PWM off the resistors. If the resistors are of the ceramic type, it is possible to crack the resistor using PWM.

The following is a plot of voltage and current at the reactor. The output of the drive is sent through a sine wave filter then to the reactor. The shape of the waveform is determined by the amount of capacitance in the sine wave filter.

<!-- image -->

If you wanted to know what voltage you can expect at the three phase reactor, consider an example where the user has four reactors in series. The inductance of each is 1.2mH, 5mH, 5mH and 3mH. First item to calculate is XL for each reactor. . XL = 2  pi  f  H

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Now total it. XL1 + XL2 + XL3 + XL4 = 5.35 ohm.

For a three phase reactor the current is represented by the equation, I V XL =   V XL     3 3

Isolate the voltage. V I XL =    3

The current value can be what the least rating of the reactors are or if the rating are greater than the drive rating, use the drive rating. In this case the drive is rated for 14 amps.

So plug in the numbers. V = = 14 5.35   1.73  1.73 129.8

So 14 amps is realized when the voltage is 129.8 on the output. A drive with a voltage rating of 240V AC could be selected.

Below is a waveform of voltage and current at a resistor. The output of the drive runs through a sine wave filter. Then this is connected to a one to one transformer. This output is then sent to a bridge rectifier giving us pure DC. With the use of a feedback board and the drives PI loop, the voltage at the resistor was steady even if the resistance changed while running.

<!-- image -->

## Other

Setting the frequency acceleration time to zero results in the drive outputting a DC voltage waveform.

If the frequency accel time is set between 0 and 1, this could trigger and anomaly where the drive outputs a frequency not equal to the commanded frequency. The

## Auto Restart

cause of this anomaly is the introduction of the jerk function. This bit needs to be off during this condition.

<!-- image -->

| 40 Mtr Options Cfg   |
|----------------------|

When using single phase operation, connect the load to the U and V phases. The W phase is energized but is not used.

Using a DC output can result in thermal issues. The drive may need to be derated.

## Investigate Possible Derating

Derate drive for sine wave filter.

Motor or drive overload is not affected by adjustable voltage mode.

The Auto Restart feature provides the ability for the drive to automatically perform a fault reset followed by a start attempt without user or application intervention. Provided the drive has been programmed with a 2 wire control scheme and the Run signal is maintained. This enables remote or unattended operation. Only certain faults are allowed to be reset. Faults listed as NonResettable in the programming manual indicate possible drive component malfunction and are not resettable.

Use caution when enabling this feature, because the drive attempts to issue its own start command based on user selected programming.

## Configuration

Setting P348 [Auto Rstrt Tries] to a value greater than zero enables the Auto Restart feature. Setting the number of tries equal to zero disables the feature.

<!-- image -->

ATTENTION: Equipment damage and/or personal injury may result if this parameter is used in an inappropriate application. Do not use this function without considering applicable local, national and international codes, standards, regulations or industry guidelines.

P349 [Auto Rstrt Delay] sets the time, in seconds, between each reset/run attempt.

The auto reset/run feature supports the following status information.

- P936 [Drive Status 2] Bit 1 "AuRstrCntDwn" provides indication that an Auto Restart attempt is presently counting down and the drive attempts to start at the end of the timing event.
- P936 [Drive Status 2] Bit 0 "AutoRstr Act" indicates that the auto restart has been activated.

## Operation

The typical steps performed in an Auto Reset/Run cycle are as follows.

1. The drive is running and an Auto Reset Run fault occurs, thus initiating the fault action of the drive.
2. After the number of seconds in P349 [Auto Rstrt Delay], the drive automatically performs an internal Fault Reset, resetting the faulted condition.
3. The drive then issues an internal Start command to start the drive.
4. If another Auto Reset Run fault occurs, the cycle repeats itself up to the number of attempts set in P348 [Auto Rstrt Tries].
5. If the drive faults repeatedly for more than the number of attempts set in P348 [Auto Rstrt Tries] with less than five minutes between each fault, the Auto Reset/Run is considered unsuccessful and the drive remains in the faulted state.
6. If the drive remains running for five minutes or more because the last reset/run without a fault, or is otherwise stopped or reset, the Auto Reset/ Run is considered successful. The Auto Restart status parameters are reset, and the process repeats if another auto resettable fault occurs.

See Aborting an Auto-Reset/Run Cycle for information on how the Reset/Run cycle can be aborted.

## Beginning an Auto-Reset/Run Cycle

The following conditions must be met when a fault occurs for the drive to begin an Auto Reset/Run cycle:

- The fault type must be Auto Reset Run.
- P348 [Auto Rstrt Tries] setting must be greater than zero.
- The drive must have been running, not jogging, not auto tuning, and not stopping, when the fault occurred. (A DC Brake state is part of a stop sequence and therefore is considered stopping.)

## Auto/Manual

## Aborting an Auto-Reset/Run Cycle

During an Auto Reset/Run cycle the following actions/conditions abort the reset/run attempt process.

- A stop command is issued from any source. (Removal of a 2-wire run-fwd or run-rev command is considered a stop assertion.)
- A fault reset command is issued from any source.
- The enable input signal is removed.
- P348 [Auto Rstrt Tries] is set to zero.
- A Non-Resettable fault occurs.
- Power to the drive is removed.
- The Auto Reset/Run Cycle is exhausted.

After all [Auto Rstrt Tries] have been made and the drive has not successfully restarted and remained running for five minutes or more, the Auto Reset/Run cycle is considered exhausted and therefore unsuccessful. In this case the Auto Reset/Run cycle terminates and an F33 "AuRsts Exhaust" fault is indicated by P953 [Fault Status B] Bit 13 "AuRstExhaust."

The purpose of the Auto/Manual function is to permit temporary override of speed control and/or exclusive ownership of logic (start, run, direction) control. A manual request can come from any port, including HIM, digital input or other input module. However, only one port can own manual control and must release the drive back to auto control before another port can be granted manual control. When in Manual mode, the drive receives its speed reference from the port that requested manual control, unless otherwise directed by the Alternate Manual Reference Select.

The HIM can request Manual control by pressing the Controls key followed by the Manual key. Manual control is released by pressing the Controls key followed by Auto. When the HIM is granted manual control, the drive uses the speed reference in the HIM. If desired, the auto speed reference can be automatically preloaded into the HIM when entering HIM manual control, so that the transition is smooth.

Manual control can also be requested through a digital input. To do this, a digital input has to be set to request Manual control through P172 [DI Manual Ctrl]. Digital Input Manual control requests can be configured to use their own alternative speed reference to control the drive. Digital inputs can also be used in conjunction with Hand-Off-Auto Start to create a three way HOA switch that incorporates Manual mode.

The Safe Speed Monitor Option Module uses Manual mode to control the speed of the drive when entering Safe Limited Speed monitoring.

## Auto/Manual Masks

The port configuration of the Auto/Manual feature is performed through a set of masks. Together, these masks set which ports can control the speed and/or logic control of the drive as well as which ports can request Manual control. The masks are configured by setting a 1 or 0 in the bit number that corresponds to the port (Bit 1 for port 1, Bit 2 for port 2, and so forth). Digital Inputs are always configured through Bit 0, regardless of what port the module physically resides in. If both [Manual Ref Mask] and [Manual Cmd Mask] for a particular port are set to 0, that port is unable to request manual control.

## P324 [Logic Mask]

Logic Mask enables and disables the ports from issuing logic commands (such as start and direction) in any mode. Stop commands from any port are not masked and still stop the drive.

## P325 [Auto Mask]

Auto Mask enables and disables the ports from issuing logic commands (such as start and direction) while in Auto mode. Stop commands from any port are not masked and still stop the drive.

## P326 [Manual Cmd Mask]

Manual Command Mask enables and disables the ports from exclusively controlling logic commands (such as start and direction) while in Manual mode. If a port assumes Manual control, and the corresponding bit for the port in the [Manual Cmd Mask] is set, no other port is able to issue logic commands. Stop commands from any port are not masked and still stops the drive.

## P327 [Manual Ref Mask]

Manual Reference Mask enables and disables the ports from controlling the speed reference while in Manual mode. If a port assumes manual control, and the corresponding bit for the port in the [Manual Ref Mask] is set, the drive is commanded to the speed reference from that port. An alternate speed reference can be commanded using P328 [Alt Man Ref Sel]. If the respective bit for the manual control port is not set, then the drive follows its normal automatic speed reference, even in Manual mode.

## Alternate Manual Reference Select

By default, the speed reference used in Manual mode comes from the port that requested manual control (For example, if a HIM in port 1 requests manual control, the speed reference in Manual mode comes from port 1). If instead it is desired to use an a different speed reference, P328 [Alt Man Ref Sel], can be used. The port selected in the parameter is used for manual reference regardless of which port requested manual control, as long as the port in manual control is allowed to set the manual reference per P327 [Manual Ref Mask]. If P328 [Alt Man Ref Sel] is an analog input, the maximum and minimum speeds can be configured through P329 [Alt Man Ref AnHi] and P330 [Alt Man Ref AnLo].

For analog input between the minimum and maximum, the drive derives the speed from these parameters through linear interpolation.

The P328 [Alt Man Ref Sel] manual reference overrides all other manual speed references, including P563 [DI ManRef Sel].

## HIM Control

Manual Control can be requested through an HIM device attached to port 1, 2, or 3. The proper bits must be set in the masks (P324 [Logic Mask], P326 [Manual Cmd Mask], and P327 [Manual Ref Mask]) for the port that the HIM is attached. To request control through the HIM, press the (Controls) key to display the Control screen.

Press the (Manual) key.

<!-- image -->

Press the (Edit) key to confirm that you want to switch to Manual mode.

<!-- image -->

If the request is accepted, the HIM displays "MAN" in the top right corner. The display does not indicate if the drive is in Manual, but rather if that particular HIM has Manual control. A HIM still displays "AUTO" if it does not have ownership of the Manual mode, even if the drive itself is in Manual mode. To see if the drive is in Manual mode, check P935 [Drive Status 1] Bit 9.

<!-- image -->

When a HIM has Manual control of the drive, the drive uses the speed reference from the HIM unless overridden by P328 [Alt Man Ref Sel]. To change the speed reference on the HIM, navigate to the Status screen and press the middle soft key labeled REF.

<!-- image -->

If the request is not accepted, a message indicates that "Manual Control is not permitted at this time." The most likely causes are that manual control is disabled for the port or that another port currently has manual control. To check which port has manual control, look at P924 [Manual Owner].

<!-- image -->

To release Manual mode from the HIM, press the (Controls) key to display the Control screen.

<!-- image -->

Press the (Edit) key to confirm that you want to switch to Auto mode.

<!-- image -->

## HIM Preload

Before taking a manual control speed reference from a HIM, the drive can preload its current speed into the HIM to provide a smooth transition. Without this feature, the drive immediately transitions to whatever speed was last used in the HIM, before the operator has a chance to make their adjustment. With this feature, the drive maintains its current speed until the operator sets the speed to the desired manual reference.

<!-- image -->

The Auto/Manual HIM Preload is configured through P331 [Manual Preload]. Ports 1, 2, and 3 can be configured to have the speed reference preloaded into the HIM by setting bits 1, 2, and 3 respectively.

## Example Scenario

The drive has a HIM in port 1 and a 24V DC I/O module in port 5. You want to select manual control from a digital input 3 on the I/O module. You want the embedded EtherNet/IP port to be the source for the speed reference in Automatic mode, and the HIM to be the source for the speed reference in Manual mode.

<!-- image -->

## Required Steps

1. Set P172 [DI Manual Ctrl] to Port 5-I/O Module &gt; 1-Dig In Sts &gt; 3 – Input 3.
2. Set P328 [Alt Man Ref Sel] = 871 Port 1 Reference 3. Set P331 [Manual Preload] = 0000 0000 0000 0010, Bit 1 enables the preloading of the speed feedback value to the HIM at port 1 when the HIM is granted manual control.

<!-- image -->

## Digital Input Control

A Digital Input can be configured to request manual control through P172 [DI Manual Ctrl]. When setting up the Auto/Manual masks, digital inputs are configured through Bit 0, regardless of what port the module physically resides in.

A speed reference for Manual mode from a digital input can be set by selecting a port in P328 [Alt Man Ref Sel]. This however causes all manual requests to use that port as a reference, whether the request was from the digital input or from a HIM. A separate manual reference port for use only when the request comes from a digital input can be configured through P563 [DI ManRef Sel]. (To see P564 [DI ManRef AnlgHi], set P301 [Access Level] to 1 "Advanced.") If P328 [Alt Man Ref Sel] is configured, it overrides P563 [DI ManRef Sel] and provides the manual reference.

If P563 [DI ManRef Sel] is an analog input, the maximum and minimum speeds can be configured through P564 [DI ManRef AnlgHi] and P565 [DI ManRef AnlgLo]. For analog input between the minimum and maximum, the drive derives the speed from these parameters through linear interpolation.

## Hand-Off-Auto

The Auto/Manual feature can be used in conjunction with a Hand-Off-Auto Start to create a H-O-A switch that starts the drive and requests manual control at the same time, allowing for a local speed reference to control the drive. See Hand-Off-Auto on page 64 for more details on the Hand-Off-Auto Start feature.

In the circuit below, a speed potentiometer was added to the analog input to provide a speed reference to the drive. When the H-O-A switch is moved from Auto to Hand, the digital input block requests manual control and issues a start command to the drive. If the digital input port receives manual control, the drive accelerates to the reference speed from the analog input. All attempts to change the speed except from the analog input are blocked. If the drive is stopped while in Hand, switch the H-O-A switch to Off and then back to Hand to restart the drive.

If another port has manual control of the drive, but does not have exclusive ownership of the logic commands (due to P326 [Manual Cmd Mask]), turning the switch to Hand causes the drive to begin moving but for the analog input to have no control over the speed.

<!-- image -->

For this circuit, set the following parameters (P301 [Access Level] must be set to 1 "Advanced" to see P563 [DI ManRef Sel]).

| Number Parameter Name Value                       |
|---------------------------------------------------|
| 158 DI Stop Digital Input 0                       |
| 172 DI Manual Ctrl Digital Input 1                |
| 176 DI HOA Start  Digital Input 1                 |
| 324 Logic Mask  xxxxxxxxxxxxxxx1 (Digital In)     |
| 326 Manual Cmd Mask xxxxxxxxxxxxxxx1 (Digital In) |
| 327 Manual Ref Mask xxxxxxxxxxxxxxx1 (Digital In) |
| 563 DI ManRef Sel Anlg In0 Value                  |

The drive requests Manual mode, start, and tracks the reference speed coming from the Analog Input when the H-O-A switches to Hand. (The HIM still reads Auto. This display changes only when the HIM has control of Manual mode).

## Safe Limited Speed

Safe Limited Speed through the PowerFlex Safe Speed Monitor option module uses Manual mode to control the speed of the drive. When Safe Limited Speed monitoring is enabled, the safety module requests manual control of the drive. If the drive does not reach a safe speed, as defined on the option module by P55 [Safe Speed Limit] and within P53 [LimSpd Mon Delay], the drive faults.

While the option module uses the Manual mode, it has no way to provide a speed reference or start the drive. The following parameters must thus be configured.

## P326 [Manual Cmd Mask]

Turn off the bit corresponding to the safety option's port to allow modules installed in other ports to continue to control the drive when it is operating in Manual mode. For example, if the safety option is installed in port 6, then turn off Bit 6 in this parameter.

## P327 [Manual Ref Mask]

Turn on the bit corresponding to the safety option's port to allow the safety option to command the drive to use its Manual Speed Reference when it is operating in Manual mode. For example, if the safety option is installed in port 6, then turn on Bit 6 in this parameter.

## P328 [Alt Man Ref Sel]

Set this parameter to select the desired speed reference when the drive is operating in Manual mode. For example, set this parameter to the value Port 0: Preset Speed 1 to configure the drive to use P571 [Preset Speed 1] as the Manual Speed Reference. In this case, P571 [Preset Speed 1] must be less than P55 [Safe Speed Limit] in the safety option to avoid causing an SLS Speed Fault.

See the Safe Speed Monitor Option Module for PowerFlex 750-Series AC Drives Safety Reference Manual, publication 750-RM001, for more information.

## Automatic Device Configuration

Automatic Device Configuration (ADC) supports the automatic download of configuration data to a Logix controller that has an EtherNet/IP connection to a PowerFlex 755 drive (firmware 4.001 or later) and its associated peripherals ADC is supported in the following:

- RSLogix 5000 software, version 20 or later
- Studio 5000 environment, version 21 or later

Project files (.ACD files) created with this software contain the configuration settings for PowerFlex drives in the project. When the project is downloaded to the controller, the configuration settings are transferred to controller memory. Earlier programming software required a manual process to download configuration settings to the controller.

ADC can also work in tandem with Firmware Supervisor. If Firmware Supervisor is set up and enabled for a drive (Exact Match keying must be used), the drive/ peripheral is automatically upgraded (if necessary) prior to any ADC operation for that port.

Information on Automatic Device Configuration (ADC) can be found in the PowerFlex 755 Embedded EtherNet/IP Adapter User Manual, publication 750COM-UM001, Chapter 4, Configuring the I/O includes the following topics:

- Description of the ADC functionality
- How the Drive Add-On Profiles (AOPs) affect ADC
- Configuring a PowerFlex 755 Drive (firmware 4.001 or later) for ADC
- ADC and Logix Memory
- Storing the Drive's and Peripherals' Firmware in the Logix Controller (Firmware Supervisor)
- Special Considerations When Using a DeviceLogix software Program
- Special Considerations When Using a 20-750-S1 Safe Speed Monitor Module
- Monitoring the ADC Progress
- Examples of potential issues and solutions

## Autotune

The Autotune feature is used to measure motor characteristics. The Autotune feature is made up of several individual tests, each of which is intended to identify one or more motor parameters. These tests require motor nameplate information to be entered into the drive parameters. Although some of the parameter values can be changed manually, measured values of the motor parameters provide the best performance. Each motor control mode requires its own set of tests to be performed. The information obtained from these measurements is stored in the drives non volatile memory for use during operation of the drive. The feature lets these tests to be separated into tests that don't require motor rotation (Static Tune), all tests within the selected control mode (Rotate Tune), or if the control mode requires the Inertia (Inertia Tune).

The Autotune tests are selected through the P70 [Autotune]. The feature provides a manual or automatic method for setting P73 [IR Voltage Drop], P74 [Ixo Voltage Drop] and P75 [Flux Current Ref ]. Valid only when P35 [Motor Ctrl Mode] is set to 1 "Induction SV," 2 "Induct Econ," or 3 "Induction FV."

Other motor control modes such as Permanent Magnet and Interior Permanent magnet, populate other parameters associated with those control modes. See the autotune parameter set below.

## Tests

Four Autotune selections are available in the PowerFlex 755 drive control. All four selections are selected from the Autotune parameter.

## P70 [Autotune]

- 0 = Ready
- 1 = Calculate
- 2 = Static Tune
- 3 = Rotate Tune
- 4 = Inertia Tune

## Ready

Parameter returns to this setting following a Static Tune or Rotate Tune, at which time another start transition is required to operate the drive in Normal mode. It also permits manually setting P73 [IR Voltage Drop], P74 [Ixo Voltage Drop], and P75 [Flux Current Ref ].

## Calculate

When the Autotune parameter is set to Calculate (default), the drive uses motor nameplate data to automatically set P73 [IR Voltage Drop], P74 [Ixo Voltage Drop], P75 [Flux Current Ref ] and P621 [Slip RPM at FLA].

P73 [IR Volt Drop], P87 [PM IR Voltage], P79 [Encdrlss VltComp], P74 [Ixo Voltage Drop], P75 [Flux Current Ref ], P93 [PM Dir Test Cur], and the Slip Frequency parameters are updated based on nameplate parameter values. When a nameplate parameter value is changed, the Autotune parameters are updated based on the new nameplate values.

When using Calculate, updated values come from a lookup table.

## Static Tune

When the Autotune parameter is set to Static, only tests that do not create motor movement are run. A temporary command that initiates a non-rotational motor stator resistance test for the best possible automatic setting of P73 [IR Voltage Drop] in all valid modes and a non-rotational motor leakage inductance test for the best possible automatic setting of P74 [Ixo Voltage Drop] in a Flux Vector (FV) mode. A start command is required following initiation of this setting. Used when motor cannot be rotated.

## Rotate Tune

The actual tests performed when Static and Rotate Tune selections are made, differ for the available motor control modes, Feedback Type and motor type selected. The tests performed are dependent on the settings of P35 [Motor Ctrl Mode], P125 [Pri Vel Fdbk Sel], and P70 [Autotune]. The parameters that are updated are then dependent on the tests run and in some cases calculated values for some parameters are used to update other parameters. Refer to Table 3 .

A temporary command initiates a Static Tune and is then followed by a rotational test for the best possible automatic setting of P75 [Flux Current Ref ]. In Flux Vector (FV) mode, with encoder feedback, a test for the best possible automatic setting of P621 [Slip RPM at FLA] is also run. A start command is required following initiation of this setting.

| IMPORTANT   | If using rotate tune for a Sensorless Vector (SV) mode, uncoupled the motor from the load or results can be invalid. With a Flux Vector (FV) mode, either a coupled or uncoupled load produces valid results. Caution must be used when connecting the load to the motor shaft and then performing an autotune. Rotation during the tune process can exceed machine limits.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 3 - Autotune Value Source

| Control Mode   | Feedback Select                                                   |                                                             | Motor Type                                                   | Autotune Rs Xo Idlt Rslt Id Rsld Slip Encrls Cemf PmOffset   |
|----------------|-------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
|                |                                                                   |                                                             | VF Induction NA Static ON OFF OFF OFF OFF ON OFF OFF OFF OFF |                                                              |
|                |                                                                   | Dynamic ON OFF OFF OFF ON ON OFF OFF OFF OFF                |                                                              |                                                              |
|                |                                                                   | PM NA Static ON OFF OFF OFF OFF OFF OFF OFF OFF OFF         |                                                              |                                                              |
|                |                                                                   | Dynamic ON OFF OFF OFF OFF OFF OFF OFF OFF OFF              |                                                              |                                                              |
|                |                                                                   | Reluctance NA Static ON OFF OFF OFF OFF OFF OFF OFF OFF OFF |                                                              |                                                              |
|                |                                                                   | Dynamic ON OFF OFF OFF ON OFF OFF OFF OFF OFF               |                                                              |                                                              |
|                | FV Induction Encoder Static ON ON ON OFF OFF OFF OFF OFF OFF OFF  |                                                             |                                                              |                                                              |
|                | FV Induction Encoder Static ON ON ON OFF OFF OFF OFF OFF OFF OFF  |                                                             | Dynamic ON ON OFF OFF ON OFF ON OFF OFF OFF                  |                                                              |
|                | Encoderless Static ON ON ON ON OFF OFF OFF OFF OFF OFF            |                                                             |                                                              |                                                              |
|                | Encoderless Static ON ON ON ON OFF OFF OFF OFF OFF OFF            |                                                             |                                                              | Dynamic ON ON ON ON ON ON OFF ON OFF OFF                     |
|                | PM Encoder Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF         |                                                             |                                                              |                                                              |
|                | PM Encoder Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF         | Dynamic ON ON OFF OFF OFF OFF OFF OFF ON ON                 |                                                              |                                                              |
|                | Encoderless Static ON ON OFF OFF OFF OFF OFF OFF OFF OFF          |                                                             |                                                              |                                                              |
|                | Encoderless Static ON ON OFF OFF OFF OFF OFF OFF OFF OFF          | Dynamic ON ON OFF OFF OFF OFF OFF OFF ON OFF                |                                                              |                                                              |
|                | Reluctance Encoder Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF |                                                             |                                                              |                                                              |
|                | Reluctance Encoder Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF | Dynamic OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF             |                                                              |                                                              |
|                | Encoderless Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF        |                                                             |                                                              |                                                              |
|                | Encoderless Static OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF        |                                                             | Dynamic OFF OFF OFF OFF OFF OFF OFF OFF OFF OFF              |                                                              |

## Inertia Tune

The Inertia Autotune selection involves only one test. Several parameters are updated from the test results. Refer to the tables in the Individual Tests section.

A temporary command initiates an inertia test of the motor/load combination. The motor ramps up and down while the drive measures the amount of inertia. This option applies only to FV modes selected in P35 [Motor Ctrl Mode]. Obtain final test results with the load coupled to the motor as long as the rotation won't damage the machine.

## Test Dependencies

When running the flux test, the selected accel rate is used unless it is less than 10 seconds. In this case, 10 seconds is forced. In the case of the Inertia test, a 0.1 second accel rate is used. The selected direction used during normal operation is used for all rotation tests. Also, during any rotate test, the normal speed limits are enforced.

The thermal manager is always being run in the 2 ms loop, which provides protection during all of the Autotune tests.

## Individual Tests

Some of the following tests are executed during an Autotune.

## Resistance Test

This test is a Static test whether Static or Rotate is selected. Used to measure Stator resistance.

## Inductance Tests

This test is a Static test whether Static or Rotate is selected. One test is used for Induction motors and a another is used for PM motors. The result from the Induction test is placed into the Ixo parameter and the PM test is placed into the IXd and IXq parameters.

## Flux Test

This test is a Rotate test that measures the current under a no load condition. The results are used for the flux current. If a Static test is used, the resulting value is from a lookup table.

## Slip Test

This test is a Rotate test that measures the difference between the rotor speed and the stator speed. This measurement is taken during acceleration.

## PM Offset Test

This test can create a small amount of motor movement so it needs to be performed with the Rotate selection. The test reads the encoder position when the drive outputs zero hertz.

## Inertia Test

This test is a stand alone test that is used to measure the system inertia.

The drive sets this value in P76 [Total Inertia] as seconds of inertia. This reflects the time it takes to accelerate the load at 100% torque to base speed. This information can be very useful in determining the total inertia (in lb·ft  ) that is connected to a motor shaft.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we have a formula that isolates the connected inertia.

For the variables, Tacc is the 100% rating of the drive in lb·ft. Let's say I'm using a 10 Hp drive with a 10 Hp motor. We can rearrange the Horsepower formula below to solve for torque in lb·ft.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

And (t) comes from what the drive reports as seconds of inertia after running the inertia tune. Let's say that the drive reported 2.12 seconds of inertia. And now organizing the variables we have

Tacc = 29.42

<!-- formula-not-decoded -->

N = 1785

<!-- formula-not-decoded -->

After these calculations, one can conclude that the connected inertia is equal to 10.76 lb·ft  . Multiplying by 0.04214011 you get 0.453 kg·m  .

What effect can P71 [Autotune Torque] have on these calculations? Regardless of the value entered here, the drive interpolates as if this value was 100%. So the seconds of inertia reported by the drive always reflects 100% torque.

## CEMF Test

This is a Rotate test used to measure a PM motors CEMF.

Autotune Parameters Information about some other Autotune Parameters not covered above.

## Autotune Parameters

## P71 [Autotune Torque]

Typically the default value of 50% is sufficient for most applications. You have the option of increasing this value or decreasing the value.

## P73 [IR Voltage Drop]

The voltage drop due to resistance.

## P74 [Ixo Voltage Drop]

The voltage drop due to Inductance.

## P75 [Flux Current Ref ]

The current necessary to flux up the motor. This value come from a lookup table for Static tunes and is measured during a Rotate tune. Obviously a rotate tune gives more accurate results.

## P76 [Total Inertia]

Reported as seconds of inertia. See description above.

## P77 [Inertia Test Lmt]

A number entered in this parameter limits the inertia tune test to a maximum number of revolutions. If violated, the drive faults on F144 "Autotune Inertia." Also, when a value is entered and the drive determines that the number of revolutions will be exceeded it goes into a decel and stops before the value is exceeded.

## P78 [Encdrlss AngComp] and P79 [Encdrlss VltComp]

These parameters are valid only for Flux Vector motor control mode and open loop. P78 is populated only by a rotate tune. P79 is populated by a Static measurement.

## P80 [PM Cfg]

This configuration parameter enables certain tests to be performed based on the motor connected.

## Permanent Magnet Motors

Parameters P81 through P93 and P120 are all populated by an autotune when the motor selected is permanent magnet. The value for these parameters are determined only by a rotate tune.

## Interior Permanent Magnet Motors

Parameters P1630 through P1647 are all populated by an autotune when the motor selected is interior permanent magnet. The value for these parameters are determined only by a rotate tune.

## Auxiliary Power Supply

## Bus Regulation

The optional Auxiliary Power Supply module, 20-750-APS, is designed to provide power to a single drive's control circuitry in the event incoming supply power to the drive is removed or lost.

When connected to a user supplied 24V DC power source, the communication network functions remain operational and on-line. A DeviceNet program can also continue to run and control any associated input and outputs.

The auxiliary power supply module is designed to power all peripherals, I/O, and connected feedback devices.

Some applications create an intermittent regeneration condition. The following example illustrates such a condition. The application is hide tanning, in which a drum is partially filled with tanning liquid and hides. When the hides are being lifted (on the left), motoring current exists. However, when the hides reach the top and fall onto a paddle, the motor regenerates power back to the drive, creating the potential for an overvoltage fault.

When an AC motor regenerates energy from the load, the drive DC bus voltage increases unless there is another means, of dissipating the energy, such as a dynamic braking chopper/resistor, or the drive takes some corrective action prior to the overvoltage fault value.

<!-- image -->

With bus regulation disabled, the bus voltage can exceed the operating limit and the drive faults to protect itself from excess voltage.

<!-- image -->

With bus regulation enabled, the drive can respond to the increasing voltage by advancing the output frequency until the regeneration is counteracted. This keeps the bus voltage at a regulated level below the trip point.

<!-- image -->

The bus voltage regulator takes precedence over acceleration/deceleration.

Select bus voltage regulation in the Bus Reg mode parameter.

## Operation

Bus voltage regulation begins when the bus voltage exceeds the bus voltage regulation setpoint Vr Vreg g and the switches shown in Figure 1 move to the positions shown.

|                | SW 1 SW 2 SW 3 SW 4 SW 5   |                                      |
|----------------|----------------------------|--------------------------------------|
| Bus Regulation |                            | Limit Bus Reg Open Closed Don’t Care |

Figure 1 - Bus Voltage Regulator, Current Limit, and Frequency Ramp

<!-- image -->

The derivative term senses a rapid rise in the bus voltage and activates the bus regulator prior to actually reaching the bus voltage regulation setpoint Vr Vreg . The derivative term is important because it minimizes overshoot in the bus voltage when bus regulation begins thereby attempting to avoid an overvoltage fault. The integral channel acts as the acceleration or deceleration rate and is fed to the frequency ramp integrator. The proportional term is added directly to the output of the frequency ramp integrator to form the output frequency. The output frequency is then limited to a maximum output frequency.

<!-- image -->

ATTENTION: The "adjust freq" portion of the bus regulator function is extremely useful for preventing nuisance overvoltage faults resulting from aggressive decelerations, overhauling loads, and eccentric loads. It forces the output frequency to be greater than commanded frequency while the drive's bus voltage is increasing towards levels that would otherwise cause a fault. However, it can also cause either of the following two conditions to occur.

1. Fast positive changes in input voltage (more than a 10% increase within 6 minutes) can cause uncommanded positive speed changes. However an "OverSpeed Limit" fault occurs if the speed reaches [Max Speed] + [Overspeed Limit]. If this condition is unacceptable, take action to 1) limit supply voltages within the specification of the drive and, 2) limit fast positive input voltage changes to less than 10%. If this operation is unacceptable and the necessary actions cannot be taken, the "adjust freq" portion of the bus regulator function must be disabled (see parameters 372 and 373).

2. Actual deceleration times can be longer than commanded deceleration times. However, a "Decel Inhibit" fault is generated if the drive stops decelerating altogether. If this condition is unacceptable, the "adjust freq" portion of the bus regulator must be disabled (see parameters 372 and 373). In addition, installing a properly sized dynamic brake resistor provides equal or better performance in most cases. Important: These faults are not instantaneous. Test results have shown that they can take between 2…12 seconds to occur.

## Bus Regulation Modes

The drive can be programmed for one of five different modes to control the DC bus voltage:

- Disabled
- Adjust Frequency
- Dynamic Braking
- Both with Dynamic Braking first
- Both with Adjust Frequency first

P372 [Bus Reg Mode A] is the mode normally used by the drive unless the "DI BusReg Mode B" digital input function is used to switch between modes instantaneously, in which case P373[Bus Reg Mode B] becomes the active bus regulation mode.

The bus voltage regulation setpoint is determined from bus memory (a means to average DC bus over a period of time). The following tables and figure describe the operation.

|     |                          | Voltage Class DC Bus Memory DB On Setpoint DB Off Setpoint   |
|-----|--------------------------|--------------------------------------------------------------|
| 480 | <685V DC 750V DC         | On - 8V DC                                                   |
| 480 | >685V DC Memory + 65V DC | On - 8V DC                                                   |

<!-- image -->

## Option 0 "Disabled"

If [Bus Reg Mode n] is set to 0 "Disabled" The Voltage Regulator is off and the DB transistor is disabled. Energy returning to the DC bus increases the voltage unchecked and trips the drive on over voltage once the voltage threshold is reached.

Figure 2 - PowerFlex 750-Series Bus Regulation – Disabled

<!-- image -->

## Option 1 "Adjust Freq"

If [Bus Reg Mode n] is set to 1 "Adjust Freq" The Bus Voltage Regulator is enabled. The Bus Voltage Regulator setpoint follows "Bus Reg Curve 1" below a DC Bus Memory of 650V DC and follows the "DB Turn On" above a DC Bus Memory of 650V DC (Table 5). For example, with a DC Bus Memory at 684V DC, the adjust frequency setpoint is 750V DC.

Below you can see the DC bus is being regulated as the speed is sacrificed to be sure the drive does not trip on over voltage.

Figure 3 - PowerFlex 750-Series Bus Regulation – Adjust Frequency

<!-- image -->

## Option 2 "Dynamic Brak"

If [Bus Reg Mode n] is set to 2 "Dynamic Brak" The Dynamic Brake Regulator is enabled. In Dynamic Brake mode the Bus Voltage Regulator is turned off. The "DB Turn On" and turn off curves apply. For example, with a DC Bus Memory at 684V DC, the Dynamic Brake Regulator turns on at 750V DC and turns back off at 742V DC. The Dynamic Brake mode can operate differently depending upon the setting of P382 [DB Resistor Type] either External or Internal.

## Internal Resistor

If the drive is set up for an internal resistor, there is a protection scheme built into the firmware such that if it is determined that too much power has been dissipated into the resistor the firmware does not allow the DB transistor to fire any longer. Thus the bus voltage rises and trips on over voltage.

Figure 4 - PowerFlex 750-Series Bus Regulation – Internal Dynamic Brake Resistor

<!-- image -->

## External Resistor

If the drive is set up for an external resistor and the resistor has been sized correctly and the regenerative power limit is set to a value that enables the regenerative power to be fully dissipated, the DB transistor continues to fire throughout the decel time.

Figure 5 - PowerFlex 750-Series Bus Regulation – External Dynamic Brake Resistor

<!-- image -->

The DB current seems as if it is decreasing toward the end of the decel. This is just a result of the sweep time of the oscilloscope and instrumentation. After all, it's not known as "Ohm's Suggestion." The point is evident that the DB transistor is pulsing through the decel.

## Option 3 "Both DB 1st"

If [Bus Reg Mode n] is set to 3 "Both DB 1st" Both regulators are enabled, and the operating point of the Dynamic Brake Regulator is lower than that of the Bus Voltage Regulator. The Bus Voltage Regulator setpoint follows the "DB Turn On" curve. The Dynamic Brake Regulator follows the "DB Turn On" and turn off curves. For example, with a DC Bus Memory between 650 and 685V DC, the Bus Voltage Regulator setpoint is 750V DC and the Dynamic Brake Regulator turns on at 742V DC and back off at 734V DC.

It is possible that the drive can react differently between Flux Vector mode and Sensorless Vector mode. The important thing to remember here is that in SV control, the drive does not use the value entered into P426 [Regen Power Lmt]. If left at default (-50%) and the decel is such that it creates a large amount of regen power, the drive again attempts to protect the resistor.

Consider the plots below.

## Option 4 "Both Frq 1st"

If [Bus Reg Mode n] is set to 4 "Both Frq 1st" Both regulators are enabled, and the operating point of the Bus Voltage Regulator is lower than that of the Dynamic Brake Regulator. The Bus Voltage Regulator setpoint follows the "Bus Reg Curve 2" below a DC Bus Memory of 650V DC and follows the "DB Turn Off " curve above a DC Bus Memory of 650V DC (Table 4). The Dynamic Brake Regulator follows the "DB Turn On" and turn off curves. For example, with a DC Bus Memory at 684V DC, the Bus Voltage Regulator setpoint is 742V DC and the Dynamic Brake Regulator turns on at 750V DC and back off at 742V DC.

Figure 6 shows that upon a stop command the bus voltage rises immediately to a point where the DB transistor turns on briefly bringing the voltage down to a point where the bus regulator can regulate the bus by adjusting the output frequency (speed).

Figure 6 - PowerFlex 750-Series Bus Regulation – Both Adj First

<!-- image -->

## Flux Vector (FV) Control

With the Regen Power Limit left at default, and a decel time of 0.1 seconds, the drive is limiting the amount of power to a point where the resistor could be heating up due to duty cycle considerations. So the drive stops the DB transistor from firing and switches to "Adjust Frequency" to regulate the bus and then enables another DB pulse and then back to adjust frequency and so on until the bus voltage remains below the trigger level.

Figure 7 - PowerFlex 750-Series Bus Regulation – Both DB First FV

<!-- image -->

If the Regen Power Limit is opened up to 100% for instance, the plot will look exactly the same as the Sensorless Vector mode plot show below.

## Sensorless Vector (SV) Control

Because the drive is not limiting the regen power the DB is able to dissipate the power the entire decel time before duty cycle considerations limits the DB capability.

<!-- image -->

Table 4 - Bus Regulation Curves

|     | Voltage Class DC Bus Memory               |                  | Bus Reg Curve 1 Bus Reg Curve 2   |
|-----|-------------------------------------------|------------------|-----------------------------------|
| 480 | < 650V DC                                 | Memory + 100V DC | Curve 1 - 8V DC                   |
| 480 | 650V DC  DC Bus Memory  685V DC 750V DC |                  | Curve 1 - 8V DC                   |
| 480 | > 685V DC                                 | Memory + 65V DC  | Curve 1 - 8V DC                   |

## Level/Gains

The following parameters are Level/Gains related to bus regulation.

## P374 [Bus Reg Lvl Cfg]

Bus Regulation Level Configuration - Selects the reference used to determine the bus voltage regulation level for the bus voltage regulator and the reference used for the dynamic brake.

- "Bus Memory" (0) – References are determined based on P12 [DC Bus Memory].
- "BusReg Level" (1) – References are determined based on the voltage set in P375 [Bus Reg Level].

If coordinated operation of the dynamic brakes of a common bus system is desired, use this selection and set the P375 [Bus Reg Level] to coordinate the brake operation of the common bus drives.

## P375 [Bus Reg Level]

Bus Regulation Level - Sets the turn-on bus voltage level for the bus voltage regulator and the dynamic brake.

Table 5 - Turn On Bus Voltage

|          | P20 [Rated Volts] = Default Turn On Volts = Min/Max Setting =   |              |
|----------|-----------------------------------------------------------------|--------------|
| < 252V   | 375V                                                            | 375V / 389V  |
| 252…503V | 750V                                                            | 750 / 779V   |
| 504…629V | 937V                                                            | 937 / 974V   |
| > 629V   | 1076V                                                           | 1076 / 1118V |

While the following parameters are listed and editable in the drive, they typically do not need to be adjusted in any way. Take care when adjusting because undesired operation can occur in another aspect of motor control.

## P376 [Bus Limit Kp]

Bus Limit Proportional Gain - Enables a progressively faster decel when the drive is behind the programmed decel time by making the bus limiter more responsive. A higher value means the drive tries to decrease decel time.

This parameter is valid only in NON-Flux Vector modes.

## P377 [Bus Limit Kd]

Bus Limit Derivative Gain - Lets you force the bus limit sooner. The higher the value the quicker the bus limit is hit and regulation starts. This can cause regulation below the typical setpoint (750VDC for 460V drive). Too high a value and normal operation of the motor can be affected. (60…60.5 Hz oscillation.)

This parameter is valid only in NON-Flux Vector modes.

## P378 [Bus Limit ACR Ki]

Bus Limit Active Current Regulator Integral Gain - If you find your system makes the regulator unstable or oscillatory, a lower value in this parameter settles out the oscillations.

This parameter is valid only in NON-Flux Vector modes.

## P379 [Bus Limit ACR Kp]

Bus Limit Active Current Regulator Proportional Gain - Determines the responsiveness of the active current and therefore, regenerated power and bus voltage. Raising this value can cause the output frequency (when in bus limit) to become noisy or jittery. Too low a value can cause the bus limit function to malfunction and result in a over voltage fault.

This parameter is valid only in NON-Flux Vector modes.

## P380 [Bus Reg Ki]

Bus Regulator Integral Gain - When regulating the DC bus, the voltage tends to swing above and below the voltage setpoint in what looks like a ringing oscillation. This parameter affects that behavior. A lower the value reduces oscillation.

This parameter is valid only in Flux Vector modes.

## Configurable Human Interface Module Removal

## P381 [Bus Reg Kp]

Bus Regulator Proportional Gain - This determines how fast the bus regulator is activated. The higher the value the faster the drive reacts once the DC voltage setpoint is reached.

This parameter is valid only in Flux Vector modes.

Once again, the likelihood of these parameters needing adjustment is highly unlikely. In fact, some descriptions related to the functionality of these parameters are intentionally left out of this text to eliminate undesired motor operation when they are adjusted unwisely.

With the PowerFlex 750-Series the drives response to a HIM communication loss (removal) is configurable. This feature is available in drives with firmware revision 3.0 or later.

It is used to prevent unintended stopping of the drive by disconnecting the HIM. However, the HIM cannot be the sole source of a Stop command to enable this feature.

The configuration is similar to the communication adapter communication loss selections:

- 0 = Fault
- 1 = Stop
- 2 = Zero Data
- 3 = Hold Last
- 4 = Send Fault Config

The default setting is 0 "Fault."

The HIM can be connected to one 1 of 3 ports per the parameters below. Each port is configured separately:

- P865 [DPI Pt1 Flt Actn] to determine the fault action at port 1.
- P866 [DPI Pt2 Flt Actn] to determine the fault action at port 2.
- P867 [DPI Pt3 Flt Actn] to determine the fault action at port 3.

If "Send Flt Cfg" is to be selected for the fault action, then configure the appropriate parameter below.

- P868 [DPI Pt1 Flt Ref ] to set the speed reference if the HIM at port 1 is disconnected.
- P869 [DPI Pt2 Flt Ref ] to set the speed reference if the HIM at port 2 is disconnected.
- P870 [DPI Pt3 Flt Ref ] to set the speed reference if the HIM at port 3 is disconnected.

A constant value must be entered as the fault speed reference in this instance.

## Droop Feature

## Duty Rating

Droop is used to shed load and is usually used when a soft coupling of two motors is present in an application. The master drive speed regulates and the follower uses droop so it does not oppose the master. The input to the droop block is the commanded motor torque. The output of the droop block reduces the speed reference. P620 [Droop RPM at FLA] sets the amount of speed, in RPM, that the speed reference is reduced when at full load torque. For example, when P620 [Droop RPM at FLA] is set to 50 RPM and the drive is running at 100% rated motor torque, the droop block subtracts 50 RPM from the speed reference.

Applications require different amounts of overload current.

## Normal Duty

Sizing the drive for Normal Duty enables the use of the highest continuous output current rating of the drive and an overload rating of 110% for 60 seconds (every 10 minutes) and 150% for 3 seconds (every minute).

## Heavy Duty

For heavy duty applications, a drive one size larger than is required for the motor is used in the application and therefore provides a larger amount of overload current in comparison to the motor rating. Heavy Duty sizing provides at least 150% for 60 seconds (every 10 minutes) and 180% for 3 seconds (every minute).

## Light Duty

The light duty setting, for a given normal duty rated drive, provides a higher continuous output current but with limited overload capability. When in light duty, the drive provides 110% for 60 seconds (every 10 minutes). The light duty setting is only available on PowerFlex 755 drives, frame 8 and larger.

The overload percentages are with respect to the connected motor rating.

The duty rating is programmed in P306 [Duty Rating]. This parameter is reset to the default setting if a Set Defaults "ALL" is executed. For drives rated under 7.5 kW (10 Hp) the normal duty and heavy duty continuous current ratings are the same, and have the heavy duty overload settings.

When changing the [Duty Rating], review P422 [Current Limit 1] and P423 [Current Limit 2].

Refer to the PowerFlex 750-Series AC Drives Technical Data, publication 750TD001, for continuous and overload current ratings for each catalog number.

## Feedback Devices

## Flying Start

There are three different feedback option modules available for PowerFlex 750Series AC Drives:

- Single Incremental Encoder (20-750-ENC-1)
- Dual Incremental Encoder (20-750-DENC-1)
- Universal Feedback (20-750-UFB-1)

The Dual Incremental Encoder and Universal Feedback modules each support up to two encoders while the Single Incremental Encoder supports one encoder. Multiple feedback option modules can be installed in the drive, however there is a limit of two feedback modules if using Integrated Motion on EtherNet/IP.

For more information on the option modules, including specifications and wiring information, see the PowerFlex 750-Series AC Drives Installation Instructions, publication 750-IN001 .

For more information on encoder feedback options, including connections and compatibility, see Appendix E of the PowerFlex 750-Series Programming Manual, publication 750-PM001 .

The Flying Start feature is used to start into a rotating motor, as quick as possible, and resume normal operation with a minimal impact on load or speed.

When a drive is started in its normal mode it initially applies a frequency of 0 Hz and ramps to the desired frequency. If the drive is started in this mode with the motor already spinning, large currents are generated. An over current trip can result if the current limiter cannot react quickly enough. The likelihood of an over current trip is further increased if there is a residual flux (back emf ) on the spinning motor when the drive starts. Even if the current limiter is fast enough to prevent an over current trip, it can take an unacceptable amount of time for synchronization to occur and for the motor to reach its desired frequency. In addition, larger mechanical stress is placed on the application.

In Flying Start mode, the drive's response to a start command is to synchronize with the motors speed (frequency and phase) and voltage. The motor then accelerates to the commanded frequency. This process prevents an over current trip and significantly reduce the time for the motor to reach its commanded frequency. Because the drive synchronizes with the motor at its rotating speed and ramps to the proper speed, little or no mechanical stress is present.

The Sweep function is currently not in the PowerFlex 750-Series drives frame 8 and larger.

## Configuration

Flying Start can be configured by setting P356 [FlyingStart Mode] to the following:

- 0 "Disabled"
- 1 "Enhanced"
- 2 "Sweep"

## Disabled

Disables the feature.

## Enhanced

An advanced mode that performs the motor reconnect quickly by using the motor's CEMF as a means of detection. This mode is the typical setting for this feature.

## Sweep

The Frequency Sweep mode is used with output sine wave filters. It attempts a reconnect by outputting a frequency starting at P520 [Max Fwd Speed]+ P524 [Overspeed Limit] and decreasing according to a slope that is modified by P359 [FS Speed Reg Ki] until there is a change in the monitored current indicating the speed of the spinning motor has been found. If the motor was not found from the forward sweep, the drive sweeps in the reverse direction from P521 [Max Rev Speed]+ P524 [Overspeed Limit].

## Scope Plots

Flying Start - Sweep Mode

This plot shows a coasting motor. When a start is commanded, the output frequency jumps up to P520 [Max Fwd Speed]+ P524 [Overspeed Limit] at some current. As the sweep frequency decreases the current is monitored. When the sweep frequency matches the frequency of the coasting motor, the current reverses and detection is complete. The motor is accelerated back to commanded speed.

<!-- image -->

## Flying Start - Sweep Slope A

This plot shows when the drive starts to sweep for the spinning motor, the frequency sweep has a certain slope associated with it. By modifying P359 [FS Speed Reg Ki] you can change the slope of this sweep.

Flying Start - Sweep Slope B

<!-- image -->

This plot shows the result of increasing P359 [FS Speed Reg Ki]. The slope is extended.

<!-- image -->

In the two samples shown above, the motor was decelerating. The sweep function and slope manipulation work the same if the motor was spinning at some constant speed.

## Flying Start - Sweep Dip A

This plot shows the effect of modifying P360 [FS Speed Reg Kp]. In this plot a motor is spinning at some constant speed when the drive is issued a start command and the sweep routine is started. Note the current dip when the parameter is set to its lowest value and the drive has determined the frequency of the rotating motor. See the next plot when this parameter set to its highest setting.

Flying Start - Sweep Dip B

<!-- image -->

This plot shows the effect of modifying P360 [FS Speed Reg Kp]. In this plot a motor that is spinning at some constant speed when the drive is issued a start command and the sweep routine is started. Note the current dip when the parameter is set to its highest value and the drive has determined the frequency of

the rotating motor. See the previous plot when this parameter set to its lowest setting.

Flying Start - Sweep Reverse Rotating Motor

<!-- image -->

This plot shows the Sweep mode when the motor is rotating opposite from the commanded frequency. It starts the same as explained above. If it didn't detect the motor's speed as it reaches 3 Hz it begins to sweep in the opposite direction. From here the process continues the same as before.

Flying Start - Enhanced Mode

<!-- image -->

This plot shows a very short time base of the Enhanced mode. If the drive detects the counter EMF of the motor it can instantly re-connect to the motor and accelerate to the commanded speed. If the drive cannot measure the CEMF (this is where the plot picks up) it sends current pulses to the motor in an attempt to excite the motor allowing the drive to detect the speed of the motor. This usually happens only at very low speeds. Once the drive has detected the motor it accelerates to the commanded speed.

<!-- image -->

## Flying Start - Enhanced Mode Reverse

Here is a motor spinning in the opposite direction of the commanded speed. In Enhanced mode the detection takes a very short time and the motor is controlled to zero speed and accelerated to the commanded speed.

<!-- image -->

## P357 [FS Gain]

Sweep mode - The amount of time the detection signal (current) must be below the setpoint. A very short time entered could cause false detections. Too long of a time and detection could be missed.

Enhanced mode - It's the Kp in the current regulator used in the detection process. Used along with P358.

## P358 [FS Ki]

Sweep mode - Integral term in voltage recovery, indirectly connected to time; higher value can shorten recovery time but can cause unstable operation.

Enhanced mode - It's the Ki in the current regulator used in the detection process. Used along with P357.

## P359 [FS Speed Reg Ki]

Sweep mode - The amount of time to sweep the frequency. A short time entered produces a steep slope on the frequency. A higher value (longer time) produces a flatter frequency sweep. Shown above.

Enhanced mode - It's the Ki in the speed regulator used in the detection process. Used along with P358.

## P360 [FS Speed Reg Kp]

Sweep mode - Sets level the current must drop below. A larger value requires less change in current to indicate detection.

Enhanced mode - It's the Kp in the speed regulator used in the detection process. Used along with P357.

## P361 [FS Excitation Ki]

Sweep mode - Integral term used to control the initial output voltage

Enhanced mode - Integral term used in the current regulator, which controls the motor excitation if the detection process deemed it necessary to excite the motor.

## P362 [FS Excitation Kp]

Sweep mode - Proportional term used to control the initial output voltage

Enhanced mode - Proportional term used in the current regulator, which controls the motor excitation if the detection process deemed it necessary to excite the motor.

## P363 [FS Reconnect Dly]

Delay time used between the issued start command and the start of the reconnect function. This is mainly used for power loss situations so the restart doesn't occur too quickly causing possible faults.

## P364 [FS Msrmnt CurLvl]

There are two different measurement methods used when in Enhanced mode. If this parameter is set to zero the second method is cancelled and reconnect is attempted after the first measurement. Any other level change in this parameter could help the second measurement routine. Usually a higher number helps more.

## Cooling Tower Fans Application Example

In some applications, such as large fans, wind or drafts can rotate the fan in the reverse direction when the drive is stopped. If the drive were started in the normal manner, its output begins at zero Hz, acting as a brake to bring the reverse rotating fan to a stop and then accelerating it in the correct direction. This operation can be very hard on the mechanics of the system including fans, belts and other coupling devices.

Draft/wind blows idle fans in reverse direction. Restarting at zero speed and accelerating damages fans and could break belts. Flying start alleviates the problem.

<!-- image -->

There could be occasions when the sweep as well as the CEMF detection fails at low speeds. This is due to the low levels of motor detection signals. It has been discovered that Sweep mode is more successful in these cases than Enhanced mode.

When in Sweep mode the frequency is always swept in the direction of the commanded frequency first.

Motor detection at low speeds can be difficult. Rather than get a false detection, the sweep reverses at 3 Hz.

## Hand-Off-Auto

Many legacy drive installations included a circuit (such as a Hand-Off-Auto switch) that provided 3-wire start and stop signals simultaneously to the drive. PowerFlex 750-Series drives do not start unless there is a full input cycle between the stop and start signals. P176 [DI HOA Start] adds a delay to the start signal, allowing the required time interval between the start and stop signals. This enables the use of a single 3-wire control circuit to start and stop the drive.

## Hand-Off-Auto Start

If P161 [DI Start] and P176 [DI HOA Start] are both configured, a "DigIn Cfg B" alarm results. You cannot use both Digital Input Start and Digital Input Hand-Off-Auto Start at the same time.

Hand-Off-Auto Example

A Motor Control Cabinet has an Hand-Off-Auto switch wired as shown in the figure below.

<!-- image -->

When the switch is turned to Off, the switch is open between the source and Stop (DI:0) and between Stop and Start (DI:1). This causes the drive to be in an asserted stop. When the switch is turned to Auto, the control signal reaches the Stop input but not the Start. The drive can be stopped and started by another location. When the switch is turned to Hand, both the Stop and Start ports are energized.

In order for the drive to start, the Stop signal must be received prior to the Start. With the wiring above, the signals are nearly simultaneous, too fast to be sure that the drive is ready to start. This causes the switch to either be unreliable or not work at all. This can be remedied by adding a time delay to the start signal. By changing Digital Input 1 from DI Start to DI Hand-Off-Auto Start, the drive

automatically adds this time delay and makes sure that the system is ready to start before it receives the command.

<!-- image -->

## Using Hand-Off-Auto with Auto/Manual

To take control of the drive speed when switching from Auto to Hand on the HO-A switch, the Auto/Manual feature can be used. See Auto/Manual on page 27 for more on Auto/Manual Control.

In the circuit below, a speed potentiometer was added to the analog input to provide a speed reference to the drive. When the H-O-A switch is moved from Auto to Hand, the digital input block requests manual control and issues a start command to the drive. If the digital input port receives manual control, the drive accelerates to the reference speed from the analog input. All attempts to change the speed except from the analog input are blocked. If the drive is stopped while in Hand, switch the H-O-A switch to Off and then back to Hand to restart the drive.

If another port has manual control of the drive, but does not have exclusive ownership of the logic commands (due to P326 [Manual Cmd Mask]), turning the switch to Hand causes the drive to begin moving but for the analog input to have no control over the speed.

<!-- image -->

For this circuit, set the following parameters (P301 [Access Level] must be set to 1 "Advanced" to see P563 [DI ManRef Sel]).

|     | Parameter No. Parameter Name Value            |
|-----|-----------------------------------------------|
|     | 158 DI Stop Digital Input 0                   |
| 172 | DI Manual Control Digital Input 1             |
| 176 | DI HOA Start  Digital Input 1                 |
| 324 | Logic Mask  xxxxxxxxxxxxxxx1 (Digital In)     |
| 326 | Manual Cmd Mask xxxxxxxxxxxxxxx1 (Digital In) |
| 327 | Manual Ref Mask xxxxxxxxxxxxxxx1 (Digital In) |
| 563 | DI Manual Reference Select Anlg In0 Value     |

The drive requests Manual mode, starts and tracks the reference speed coming from the Analog Input when the H-O-A switches to Hand. (The HIM still reads Auto. This display changes only when the HIM has control of Manual mode).

## Using Hand-Off-Auto with a Start Relay

The Hand-Off-Auto switch can also be wired to ability to start the drive through a separate start relay.

In the circuit below, the run relay closes the circuit to both the stop and start inputs when the H-O-A switch is in Auto. Using this option, the drive can be started only if the H-O-A switch is in Hand or in Auto and the Run Relay is energized. No network or HIM control of the drive is possible.

<!-- image -->

The above circuit can also be accomplished with a single digital input. Unlike P161 [DI Start], P176 [DI HOA Start] can share the same physical input with P158 [DI Stop]. The circuit can thus become the following.

<!-- image -->

## Masks

To use the H-O-A switch, the run relay and allow for network or HIM control, the circuit can be wired as in the figure below.

<!-- image -->

Here, the stop input is high when the H-O-A switch is in the Hand or Auto position. This eliminates the asserted stop caused when the stop input is low, allowing for the drive to be started from several sources when the H-O-A switch is in the Auto position.

A mask is a parameter that contains one bit for each of the possible ports for the respective PowerFlex 750-Series drive. Each bit acts like a valve for issued commands. Closing the valve (setting a bit value to 0) stops the command from reaching the drive. Opening the valve (setting a bit value to 1) lets the command pass through the mask into the drive.

Table 6 - Mask Parameters and Functions

| Parameter No. Parameter Name Description   |                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 222 Dig In Filt Mask (1)                   | Digital Input Filter Mask. Filters the selected digital input.                                                                                                                                                                                                                                                                            |
| 324                                        | Logic Mask Enables/disables ports to control the logic command (such as start and direction). Does not mask Stop commands.                                                                                                                                                                                                                |
|                                            | 325 Auto Mask Enables/disables ports to control the logic command (such as start and direction), while in Auto mode. Does not mask Stop commands.                                                                                                                                                                                         |
|                                            | 326 Manual Cmd Mask Enables/disables ports to control the logic command (such as start and direction), while in Manual mode. Does not mask Stop commands.                                                                                                                                                                                 |
|                                            | 327 Manual Ref Mask Enables/disables ports to control the speed reference while in Manual mode. When a port is commanding Manual mode, the reference is forced to the commanding port if the respective bit in this parameter is set. If an alternate speed reference source is desired, use P328 [Alt Man Ref Sel] to select the source. |
| 885 Port Mask Act(2)                       | Active status for port communication. Bit 15 “Security” determines if network security is controlling the logic mask instead of this parameter.                                                                                                                                                                                           |
| 886 Logic Mask Act (2)                     | Active status of the logic mask for ports. Bit 15 “Security” determines if network security is controlling the logic mask instead of this parameter.                                                                                                                                                                                      |

| Parameter No. Parameter Name Description   |                                                                                                                                                                                                                                                               |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 887 Write Mask Act(2)                      | Active status of write access for ports. Bit 15 “Security” determines if network security is controlling the write mask instead of this parameter.                                                                                                            |
|                                            | 888 Write Mask Cfg Enables/disables write access (parameters, links, and so forth.) for DPI ports. Changes to this parameter become effective only when power is cycled, the drive is reset or Bit 15 of P887 [Write Mask Actv], transitions from “1” to “0.” |
| 2 Dig In Filt Mask (3)                     | Digital Input Filter Mask. Filters the selected digital input.                                                                                                                                                                                                |

The individual bits for each parameter are as follows.

Table 7 - Mask Parameters with Bit Designations

|        | P222 [Dig In (1)  Filt Mask]  (1)  P324 [Logic Mask] P325 [Auto Mask] P327 [Manual Ref Mask]                                                                          | P326 [Manual Cmd Mask]                                                                               | P885 [Port Mask Act] P886 [Logic Mask Act] P887 [Write Mask Act] P888 [Write Mask Cfg] P2 [Dig In Filt Mask] (4)   |
|--------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Bit 0  |                                                                          | Reserved Digital In Digital In Digital In Digital In Digital In Digital In Reserved Reserved Input 0 |                                                                                                                    |
| Bit 1  |                                                                          |                                                                                                      | Input 1 Port 1 Port 1 Port 1 Port 1 Port 1 Port 1 Port 1 Port 1 Input 1                                            |
| Bit 2  |                                                                          |                                                                                                      | Input 2 Port 2 Port 2 Port 2 Port 2 Port 2 Port 2 Port 2 Port 2 Input 2                                            |
| Bit 3  | Reserved Port 3 Port 3 Port 3 Port 3 Port 3 Port 3 Port 3 Port 3 Input 3 |                                                                                                      |                                                                                                                    |
| Bit 4  | Reserved Port 4 Port 4 Port 4 Port 4 Port 4 Port 4 Port 4 Port 4 Input 4 |                                                                                                      |                                                                                                                    |
| Bit 5  | Reserved Port 5 Port 5 Port 5 Port 5 Port 5 Port 5 Port 5 Port 5 Input 5 |                                                                                                      |                                                                                                                    |
| Bit 6  |                                                                          |                                                                                                      | Reserved Port 6 Port 6 Port 6 Port 6 Port 6 Port 6 Port 6 Port 6 Reserved                                          |
| Bit 7  |                                                                          | Reserved Port 7 Reserved Reserved Reserved Port 7 Reserved Port 7 Port 7 Reserved                    |                                                                                                                    |
| Bit 8  |                                                                          |                                                                                                      | Reserved Port 8 Reserved Reserved Reserved Port 8 Reserved Port 8 Port 8 Reserved                                  |
| Bit 9  |                                                                          | Reserved Port 9 Reserved Reserved Reserved Port 9 Reserved Port 9 Port 9 Reserved                    |                                                                                                                    |
| Bit 10 | Reserved Port 10(2)                                                      | Reserved Reserved Reserved Port 10(2)                                                                | Reserved Port 10(2)  Port 10(2)  Reserved                                                                          |
| Bit 11 | Reserved Port 11(2)                                                      | Reserved Reserved Reserved Port 11(2)                                                                | Reserved Port 11(2)  Port 11(2)  Reserved                                                                          |
| Bit 12 |                                                                          | Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved            |                                                                                                                    |
| Bit 13 | Reserved Port 13(3)  Port 13(3)  Port 13(3)                              | Port 13(3)                                                                                           | Port 13(3)  Port 13(3)  Port 13(3)  Port 13(3)  Reserved                                                           |
| Bit 14 |                                                                          |                                                                                                      | Reserved Port 14 Port 14 Port 14 Port 14 Port 14 Port 14 Port 14 Port 14 Reserved                                  |
| Bit 15 |                                                                          | Reserved Reserved Reserved Reserved Reserved Security Security Security Security Reserved            |                                                                                                                    |

## Example

A PowerFlex 755 drive is controlled via the embedded ethernet (Port 13) remotely by a PLC. Normal operation prevents any type of control from being issued from the remote HIM (Port 2). However, the ability to manually control the drive via the HIM is needed in some cases. To assure these two modes of control, masks are set as follows.

<!-- image -->

This masks out (disables) the remote HIM (Port 2) to control the logic command word (such as start, jog and direction) when the drive is in Auto mode and lets (enables) the HIM to control the logic command word when the drive is in Manual mode.

## Owners

An owner is a parameter that contains one bit for each of the possible port adapters. The bits are set high (value of 1) when its adapter is currently issuing that command, and set low (Value of 0) when its adapter is not issuing that command.

## Parameters and Functions

- P919 [Stop Owner] indicates which port is issuing a valid stop command.
- P920 [Start Owner] indicates which port is issuing a valid start command.
- P921 [ Jog Owner] indicates which port is issuing a valid jog command.
- P922 [Dir Owner] indicates which port has exclusive control of direction command.
- P923 [Clear Flt Owner] indicates which port is currently clearing a fault.
- P924 [Manual Owner] indicates which port has requested manual control of all drive logic and reference functions.
- P925 [Ref Select Owner] indicates which port is issuing a valid reference select.

The bits for each parameter can be broken down as follows.

| Options                                 | ReservedPort 14Port 13 (1 (1)   | ReservedReservedReservedReservedReservedReservedPort 6Port 5Port 4Port 3Port 2Port 1Digital In   |                                           |
|-----------------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------|
| Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |                                 |                                                                                                  |                                           |
|                                         |                                 |                                                                                                  | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |

(1) 755 drives only.

Ownership falls into two categories.

Exclusive: Only one adapter at a time can issue the command and only one bit in the parameter is high.

Non Exclusive: Multiple adapters can simultaneously issue the same command and multiple bits can be high.

Some ownership must be exclusive; that is, only one adapter at a time can issue certain commands and claim ownership of that function. For example, it is not allowable to have one adapter command the drive to run in the forward direction while another adapter is issuing a command to make the drive run in reverse. Direction control ownership is exclusive.

Conversely, any number of adapters can simultaneously issue stop commands. Stop control ownership is not exclusive.

## Ownership Example

The operator presses the HIM Stop button to stop the drive. When the operator attempts to restart the drive by pressing the HIM Start button, the drive does not restart. The operator needs to determine why the drive will not restart. The operator first views the Start Owner to see if the HIM is issuing a valid Start. When the start button on the HIM is pressed, a valid start is being issued as shown below.

<!-- image -->

Because the start command is not maintained causing the drive to run, the operator views the Stop Owner. Note that the status bar on the HIM indicates that a stop has been asserted, but it does not indicate from which port the stop command is originating. Notice that bit 0 is a value of "1," indicating that the Stop device wired to the Digital Input terminal block is open, issuing a Stop command to the drive. Until this device is closed, a permanent Start Inhibit condition exists and the drive will not restart.

<!-- image -->

## Power Loss

The drive contains a sophisticated algorithm to manage initial application of power as well as recovery from a partial power loss event. The drive also has programmable features that can minimize the problems associated with a loss of power in certain applications.

## Terms and Definitions

| Term Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vbus The instantaneous DC bus voltage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Vmem The average DC bus voltage. A measure of the average bus voltage determined by heavily filtering bus voltage. Just after the pre-charge relay is closed during the initial power-up bus pre-charge, bus memory is set equal to bus voltage. Thereafter it is updated by ramping at a very slow rate toward Vbus. The filtered value ramps at 2.4V DC per minute (for a 480VAC drive). An increase in Vmem is blocked during deceleration to prevent a false high value due to the bus being pumped up by regeneration. Any change to Vmem is blocked during inertia ride through.                                                                                                                                                                                                                    |
| Vslew The rate of change of Vmem in volts per minute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Vrecover The threshold for recovery from power loss.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Vtrigger The threshold to detect power loss. The level is adjustable. The default is the value in the PowerFlex 750-Series Bus Level table. If “Pwr Loss Lvl” is selected as an input function AND energized, Vtrigger is set to Vmem minus [Pwr Loss Level]. Vopen is normally 60V DC below Vtrigger (in a 480VAC drive). Both Vopen and Vtrigger are limited to a minimum of Vmin. This is a factor only if [Pwr Loss Level] is set to a large value. Important: When using a value of P451/P454 [Pwr Loss A/B Level] that is larger than default, you must provide a minimum line impedance to limit inrush current when the power line recovers. Provide an input impedance that is equal to or greater than the equivalent of a 5% transformer with a VA rating 5 times the drive’s input VA rating. |
| Vinertia The software regulation reference for Vbus during inertia ride through.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vclose The threshold to close the pre-charge contactor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Vopen The threshold to open the pre-charge contactor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Vmin The minimum value of Vopen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Voff The bus voltage below which the switching power supply falls out of regulation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Table 8 - PowerFlex 750-Series Bus Levels

| Class 200/240V AC 400/480V AC 600/690V AC                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------|
| Vslew 1.2V DC 2.4V DC 3.0V DC                                                                                                       |
| Vrecover Vmem – 30V Vmem – 60V Vmem – 75V                                                                                           |
| Vclose Vmem – 60V Vmem – 120V Vmem – 150V                                                                                           |
| Vtrigger1,2 Vmem – 60V Vmem – 120V Vmem – 150V                                                                                      |
| Vtrigger1,3 Vmem – P451/P454 [Power Loss A/B Level] Vmem – P451/P454 [Power Loss A/B Level] Vmem – P451/P454 [Power Loss A/B Level] |
| Vopen Vmem – P451/P454 [Power Loss A/B Level] Vmem – P451/P454 [Power Loss A/B Level] Vmem – P451/P454 [Power Loss A/B Level]       |
| Vopen4 153V DC 305V DC 382V DC                                                                                                      |
| Vmin 153V DC 305V DC 382V DC                                                                                                        |
| Voff – 200V DC –                                                                                                                    |

In the following diagram, the x-axis across the bottom indicates what the input voltage is into the drive and the y-axis indicates the corresponding DC Bus Voltage. Then the levels of each event are indicated in the graph. For example if I measure at the input of my drive, 450 volts - phase to phase, I find that voltage across the bottom. Now the various voltage levels can be derived according to that voltage level.

<!-- image -->

## Restart after Power Recovery

If a power loss causes the drive to coast, and power recovers, the drive returns to powering the motor if it is in a Run Permit state. The drive is in a Run Permit state if the following is true:

- 3 Wire mode - it is not faulted and if all Enable and Not Stop inputs are energized.
- 2 Wire mode - it is not faulted and if all Enable, Not Stop, and Run inputs are energized.

## Power Loss Modes

The drive is designed to operate at a nominal input voltage. When voltage falls below this nominal value by a significant amount, action can be taken to preserve the bus energy and keep the drive logic alive as long as possible. The drive has three methods of dealing with low bus voltages.

- "Coast" - Disable the drive and allow the motor to coast. (default)
- "Decel" - Decelerate the motor at a rate that regulates the DC bus until the load's kinetic energy can no longer power the drive.
- "Continue" - Allow the drive to power the motor down to 50% of the nominal DC bus voltage. When power loss occurs, P959 [Alarm Status A] Bit 0 turns on if the P449 [Power Loss Actn] is set to 1 "Alarm."

If the P449 [Power Loss Actn] is set to 3 "FltCoastStop," an F3 "Power Loss" fault occurs when the power loss event exceeds P452/455 [Pwr Loss A/B Time].

The drive faults with a F4 "UnderVoltage" fault if the bus voltage falls below Vmin and the P460 [UnderVltg Action] is set to 3 "FltCoastStop."

The pre-charge relay opens if the bus voltage drops below Vopen and closes if the bus voltage rises above Vclose.

If the bus voltage rises above Vrecover for 20 ms, the drive determines the power loss is over. The power loss alarm is cleared.

If the drive is in a Run Permit state, the reconnect algorithm is run to match the speed of the motor. The drive then accelerates at the programmed rate to the set speed.

## Coast

This is the default mode of operation. The drive determines a power loss has occurred if the bus voltage drops below Vtrigger. If the drive is running, the inverter output is disabled and the motor coasts.

<!-- image -->

## Decel

This mode of operation is useful if the mechanical load is high inertia and low friction. By recapturing the mechanical energy, converting it to electrical energy and returning it to the drive, the bus voltage is maintained. As long as there is mechanical energy, the ride through time is extended and the motor remains fully fluxed.

If AC input power is restored, the drive can ramp the motor to the correct speed without the need for reconnecting. The drive determines a power loss has occurred if the bus voltage drops below Vtrigger.

If the drive is running, the inertia ride through function is activated.

The load is decelerated at the correct rate so that the energy absorbed from the mechanical load regulates the DC bus to the value Vinertia.

The inverter output is disabled and the motor coasts if the output frequency drops to zero or if the bus voltage drops below Vopen or if any of the Run Permit inputs are de-energized.

If the drive is still in inertia ride through operation when power returns, the drive immediately accelerates at the programmed rate to the set speed. If the drive is coasting and it is in a Run Permit state, the reconnect algorithm is run to match the speed of the motor. The drive then accelerates at the programmed rate to the set speed.

<!-- image -->

## Continue

This mode provides the maximum power ride through. The input voltage can drop to 50% and the drive is still able to supply drive rated current (not drive rated power) to the motor.

<!-- image -->

<!-- image -->

ATTENTION: To guard against drive damage, a minimum line impedance must be provided to limit inrush current when the power line recovers. Provide an input impedance that is equal to or greater than the equivalent of a 5% transformer with a VA rating 6 times the drive's input VA rating.

Drive damage can occur if proper input impedance is not provided as explained below. If the value for [Power Loss Level] is greater than 18% of [DC Bus Memory], you must provide a minimum line impedance to limit inrush current when the power line recovers. Provide input impedance that is equal to or greater than the equivalent of a 5% transformer with a VA rating 5 times the drives input VA rating.

## Process PID Loop

The internal PID function provides closed loop process control with proportional and integral control action. The function is designed to be used in applications that require simple control of a process without the use of a separate stand-alone loop controller.

The PID function reads a process variable input to the drive and compares it to a desired setpoint stored in the drive. The algorithm then adjusts the output of the PID regulator, changing drive output frequency to attempt zero error between the process variable and the setpoint.

The Process PID can be used to modify the commanded speed or can be used to trim torque. There are two ways the PID Controller can be configured to modify the commanded speed.

- Speed Trim - The PID Output can be added to the master speed reference.
- Exclusive Control - PID can have exclusive control of the commanded speed.

The mode of operation between speed trim, exclusive control, and torque trim is selected in P1079 [PID Output Sel].

## Speed Trim Mode

In this mode, the output of the PID regulator is summed with a master speed reference to control the process. This mode is appropriate when the process needs to be controlled tightly and in a stable manner by adding or subtracting small amounts directly to the output frequency (speed). In the following example, the master speed reference sets the wind/unwind speed and the dancer pot signal is used as a PID Feedback to control the tension in the system. An equilibrium point is programmed as PID Setpoint, and as the tension increases or decreases during winding, the master speed is trimmed to compensate and maintain tension near the equilibrium point.

<!-- image -->

When the PID is disabled the commanded speed is the ramped speed reference.

<!-- image -->

When the PID is enabled the output of the PID Controller is added to the ramped speed reference.

<!-- image -->

## Exclusive Mode

In this mode, the output of PID regulator is the speed reference, and does not "trim" a master speed reference. This mode is appropriate when speed is unimportant and the only thing that matters is satisfying the control loop. In the pumping application example below, the reference or setpoint is the required pressure in the system. The input from the transducer is the PID feedback and changes as the pressure changes. The drive output frequency is then increased or decreased as needed to maintain system pressure regardless of flow changes. With

the drive turning the pump at the required speed, the pressure is maintained in the system.

<!-- image -->

However, when additional valves in the system are opened and the pressure in the system drops, the PID error alters its output frequency to bring the process back into control. When the PID is disabled the commanded speed is the ramped speed reference.

<!-- image -->

When the PID is enabled, the speed reference is disconnected and PID Output has exclusive control of the commanded speed, passing through the linear ramp and S curve.

<!-- image -->

## PID Output Select

Parameter 1079 [PID Output Sel]

- "Not Used" (0) - PID output is not applied to any speed reference.
- "Speed Excl" (1) - PID output is the only reference applied to the speed reference.
- "Speed Trim" (2) - PID output is applied to speed reference as a trim value. (Default)
- "Torque Excl" (3) - PID output is only reference applied to torque reference.
- "Torque Trim" (4) - PID output is applied to torque reference as a trim value.
- "Volt Excl" (5) - PID output is only reference applied to voltage reference.
- "Volt Trim" (6) - PID output is applied to voltage reference as a trim value.

## PID Configuration

Parameter 1065[PI Cfg] is a set of bits that select various modes of operation. The value of this parameter can only be changed while the drive is stopped.

<!-- image -->

## PID Preload

This feature steps the PID Output to a preload value for better dynamic response when the PID Output is enabled. Refer to the diagram below. If PID is not enabled, the PID Integrator can be initialized to the PID Preload Value or the current value of the commanded speed. The operation of Preload is selected in the PID Configuration parameter. By default, Preload Command is off and the PID Load Value is zero, causing a zero to be loaded into the integrator when the PID is disabled. As shown in Diagram A below, when the PID is enabled the PID output starts from zero and regulates to the required level. When PID is enabled with PID Load Value is set to a non-zero value the output begins with a step as shown in Diagram B below. This can result in the PID reaching steady state

sooner, however if the step is too large the drive can go into current limit and extend the acceleration.

<!-- image -->

Preload command can be used when the PID has exclusive control of the commanded speed. With the integrator preset to the commanded speed there is no disturbance in commanded speed when PID is enabled. After PID is enabled the PID output is regulated to the required level.

<!-- image -->

When the PID is configured to have exclusive control of the commanded speed and the drive is in current limit or voltage limit the integrator is preset to the commanded speed so that it knows where to resume when no longer in limit.

## Ramp Ref

The PID Ramp Reference feature is used to provide a smooth transition when the PID is enabled and the PID output is used as a speed trim (not exclusive control). When PID Ramp Reference is selected in the PID Configuration parameter, and PID is disabled, the value used for the PID reference is the PID feedback. This causes the PID error to be zero. Then when the PID is enabled the value used for the PID reference ramps to the selected value for PID reference at the selected acceleration or deceleration rate. After the PID reference reaches the selected value the ramp is bypassed until the PID is disabled and enabled again. Scurve is not available as part of the PID linear ramp.

## Zero Clamp

This feature limits the possible drive action to one direction only. Output from the drive is from zero to maximum frequency forward or zero to maximum frequency reverse. This removes the chance of doing a "plugging" type operation as an attempt to bring the error to zero. This bit is active only in trim mode.

The PID has the option to limit operation so that the output frequency always has the same sign as the master speed reference. The zero clamp option is selected in the PID Configuration parameter. Zero clamp is disabled when PID has exclusive control of speed command.

For example, if master speed reference is +10 Hz and the output of the PID results in a speed adder of –15 Hz, zero clamp limits the output frequency to not become less than zero. Likewise, if master speed reference is –10 Hz and the output of the PID results in a speed adder of +15 Hz, zero clamp limits the output frequency to not become greater than zero.

## Feedback Square Root

This feature uses the square root of the feedback signal as the PID feedback. This is useful in processes that control pressure, because centrifugal fans and pumps vary pressure with the square of speed.

The PID has the option to take the square root of the selected feedback signal. This is used to linearize the feedback when the transducer produces the process variable squared. The result of the square root is normalized back to full scale to provide a consistent range of operation. The option to take the square root is selected in the PID configuration parameter.

<!-- image -->

## Stop Mode

When P370/371 [Stop Mode A/B] is set to 1 "Ramp" and a Stop command is issued to the drive, the PID loop continues to operate during the decel ramp until the PID output becomes more than the master reference. When set to 0 "Coast," the drive disables PID and performs a normal stop. This bit is active in Trim mode only.

## Anti-Wind Up

When P1065 [PID Cfg] Bit 5 "Anti Windup" is set to 1 "Enabled" the PID loop automatically prevents the integrator from creating an excessive error that could cause loop instability. The integrator is automatically controlled without the need for PID Reset or PID Hold inputs.

## Percent Ref

When using Process PID control the output can be selected as percent of the Speed Reference. This works in Speed trim mode only, not in Torque Trim or Exclusive mode.

## Examples

Percent Ref selected, Speed Reference = 43 Hz, PID Output = 10%, Maximum Frequency = 130 Hz. 4.3 Hz is added to the final speed reference.

Percent Ref not selected, Speed Reference = 43 Hz, PID Output = 10%, Maximum Frequency = 130 Hz. 13.0 Hz is added to the final speed reference.

## PID Control

P1066 [PID Control] is a set of bits to dynamically enable and disable the operation of the process PID controller. When this parameter is interactively written to from a network it must be done through a data link so the values are not written to EEprom.

## PID Enable

The PID loop can be enabled/disabled. The Enabled status of the PID loop determines when the PID regulator output is part or all of the commanded speed. The logic evaluated for the PID Enabled status is shown in the following ladder diagram.

The drive must be in Run before the PID Enabled status can turn on. The PID remains disabled when the drive is jogged. The PID is disabled when the drive begins a ramp to stop, except when it is in Trim mode and the Stop mode bit in P1065 [PID Cfg] is enabled.

When a digital input is configured as "PI Enable," the PID Enable bit of P1066 [PID Control] must be turned On for the PID loop to become enabled. If a digital input is not configured as "PI Enable" and the PID Enable bit in [PID Control] is turned On, then the PID loop can become enabled. If the PID Enable bit of [PID Control] is left continuously, then the PID can become enabled as soon as the drive goes into Run. If analog input signal loss is detected, the PID loop is disabled.

<!-- image -->

## PID Hold

The Process PID Controller has the option to hold the integrator at the current value so if some part of the process is in limit the integrator maintains the present value to avoid windup in the integrator. The logic to hold the integrator at the current value is shown in the following ladder diagram. There are three conditions under which Hold turns on.

- If a digital input is configured to provide PID Hold and that digital input is turned on then the PID integrator stops changing. Note that when a digital input is configured to provide PID Hold that takes precedence over the PID control parameter.
- If a digital input is not configured to provide PID Hold and the PID Hold bit in the PID Control parameter is turned on the PID integrator stops changing.
- If the current limit or voltage limit is active then the PID is put into Hold.

<!-- image -->

## PI Reset

This feature holds the output of the integral function at zero. The term "anti windup" is often applied to similar features. It can be used for integrator preloading during transfer and can be used to hold the integrator at zero during "manual mode."

For example a process whose feedback signal is below the reference point, creating error. The drive increases its output frequency in an attempt to bring the process into control. If, however, the increase in drive output does not zero the error, additional increases in output is commanded. When the drive reaches programmed Maximum Frequency, it is possible that a significant amount of integral value has been "built up" (windup). This can cause undesirable and sudden operation if the system were switched to manual operation and back. Resetting the integrator eliminates this windup.

## Invert Error

This feature changes the "sign" of the error, creating a decrease in output for increasing error and an increase in output for decreasing error. An example of this is an HVAC system with thermostat control. In Summer, a rising thermostat reading commands an increase in drive output because cold air is being blown. In Winter, a falling thermostat commands an increase in drive output because warm air is being blown. The PID has the option to change the sign of PID Error. This is used when an increase in feedback needs to cause an increase in output. The option to invert the sign of PID Error is selected in the PID Configuration parameter.

## PID Status

P1089 [PID Status] parameter is a set of bits that indicate the status of the process PID controller.

<!-- image -->

| File   | Group   | No. Display Name Full Name Description Read-WriteData Type   |                                                                                                                                          | Values                                    |
|--------|---------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
|        |         | 1089 PID Status PID Status RO 16-bit Integer                 |                                                                                                                                          |                                           |
|        |         | Status of the Process PI regulator.                          |                                                                                                                                          |                                           |
| APPLICATIONS Process PID        |         | Options                                                      | ReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedPID In LimitPID ResetPID HoldPID Enabled | 0 = Condition False 1 = Condition True    |
|        |         |                                                              |                                                                                                                                          | Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   |
|        |         |                                                              |                                                                                                                                          | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |

## PID Reference and Feedback

The selection of the source for the reference signal is entered in P1067 [PID Ref Sel]. The selection of the source for the feedback signal is selected in P1072 [PID Fdbk Sel]. The reference and feedback have the same limit of possible options.

Options include DPI adapter ports, MOP, preset speeds, analog inputs, pulse input, encoder input and PID setpoint parameter.

The value used for reference is displayed in P1090 [PID Ref Meter] as a read only parameter. The value used for feedback is displayed in P1091 [PID Fdbk Meter] as a read only parameter. These displays are active independent of PID Enabled. Full scale is displayed as ±100.00%.

## PID Reference and Feedback Scaling

The analog PID reference can be limited by using P1068 [PID Ref AnlgHi] and P1069 [PID Ref AnlgLo]. [PID Ref AnlgHi] determines the high value, in percent, for the analog PID reference. [PID Ref AnlgLo] determines the low value, in percent, for the PID reference.

The analog PID feedback can be limited by using P1068 [PID Ref AnlgHi] and P1069 [PID Ref AnlgLo]. [PID Ref AnlgHi] determines the high value, in percent, for the PID feedback. [PID Ref AnlgLo] determines the low value, in percent, for the PID feedback.

## Example

Display P1090 [PID Ref Meter] and P1091 [PID Fdbk Meter] as positive and negative values. Feedback from our dancer comes into Analog Input 2 as a 0-10V DC signal.

- P1067 [PID Ref Sel] = 0 "PI Setpoint"
- P1070 [PID Setpoint] = 50%
- P1072 [PID Fdbk Sel] = 2 "Analog In 2"
- P1068 [PID Ref AnlgHi] = 100%
- P1069 [PID Ref AnlgLo] = –100%
- P1073 [PID Fdbk AnlgHi] = 100%
- P1074 [PID Fdbk AnlgLo] = 0%
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In2 Lo] = 0V

## PI Feedback Scaling

- P675 [Trq Ref A Sel] = "Analog In 1"
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In2 Lo] = 0V
- P1073 [PID Fdbk AnlgHi] = 100%
- P1074 [PID Fdbk AnlgLo] = 0%

Now 5V corresponds to 50% on the PID Feedback, and we try to maintain a PID setpoint of 50% (5V).

## PID Setpoint

This parameter can be used as an internal value for the setpoint or reference for the process. If P1067 [PID Ref Sel] points to this parameter, the value entered here becomes the equilibrium point for the process.

## PID Error

The PID Error is then sent to the Proportional and Integral functions, which are summed together.

PID Error Filter P1084 [PID LP Filter BW] sets up a filter for the PID Error. This is useful in filtering out unwanted signal response, such as noise in the PID loop feedback signal. The filter is a Radians/Second low pass filter.

## PID Gains

Parameters P1086 [PID Prop Gain], P1087 [PID Int Time], and P1088 [PID Deriv Time] determine the response of the PID.

Proportional control (P) adjusts output based on size of the error (larger error = proportionally larger correction). If the error is doubled, then the output of the proportional control is doubled. Conversely, if the error is cut in half then the output of the proportional output is cut in half. With only proportional control there is always an error, so the feedback and the reference are never equal. [PID Prop Gain] is unit less and defaults to 1.00 for unit gain. With [PID Prop Gain] set to 1.00 and PID Error at 1.00% the PID output is 1.00% of maximum frequency.

Integral control (I) adjusts the output based on the duration of the error. (The longer the error is present, the harder it tries to correct). The integral control by itself is a ramp output correction. This type of control gives a smoothing effect to the output and continues to integrate until zero error is achieved. By itself, integral control is slower than many applications require and therefore is combined with proportional control (PI). [PID Int Time] is entered in seconds. If [PID Int Time] is set to 2.0 seconds and PI Error is 100.00% the PI output integrates from 0 to 100.00% in 2.0 seconds.

Derivative Control (D) adjusts the output based on the rate of change of the error and, by itself, tends to be unstable. The faster that the error is changing, the larger change to the output. Derivative control is usually used in torque trim mode and is usually not needed in speed mode.

For example, winders using torque control rely on PD control not PI control. Also, P1084 [PID LP Filter BW] is useful in filtering out unwanted signal response in the PID loop. The filter is a Radians/Second low pass filter.

## PID Lower and Upper Limits/Output Scaling

The output value produced by the PID is displayed as ±100% in P1093 [PID Output Meter].

P1082 [PID Lower Limit] and P1081 [PID Upper Limit] are set as a percentage. In exclusive or speed trim mode, they scale the PID Output to a percentage of P37 [Maximum Freq]. In torque trim mode, they scale the PID Output as a percentage of rated motor torque.

## Reset Parameters to Factory Defaults

## Example

Set the PID lower and Upper limits to ±10% with Maximum Frequency set to 100 Hz. This lets the PID loop adjust the output of the drive ±10 Hz.

P1081 [PID Upper Limit] must always be greater than P1082 [PID Lower Limit].

Once the drive has reached the programmed Lower and Upper PID limits, the integrator stops integrating and no further "windup" is possible.

## PID Output Mult

P1080 [PID Output Mult] enables additional scaling of the PID loop output.

## Example

The application is a velocity controlled winder. As the roll builds up, the output gain can be reduced to allow the dancer signal to be properly reacted to by the PID loop without changing tuning of the PID loop.

## PID Deadband

P1083 [PID Deadband] conditions the PID reference. If the PID reference has undesired rapid changes, the deadband can help smooth out these transitions.

1. Access the Status Screen on the 20-HIM-A6 or 20-HIM-CS6 Human Interface Module.
2. Use the left-right arrow keys to scroll to the port of the device whose parameters you want to set to factory defaults (for example, Port 00 for the Host Drive or the respective port number for the drive's connected peripherals).
3. Press the Folder key next to the green Start key to display its last-viewed folder.
4. Use the left-right arrow keys to scroll to the Memory folder.

<!-- image -->

5. Use the up-down arrow keys to select Set Defaults.
6. Press the Enter (5) key to display the Set Defaults screen.

<!-- image -->

<!-- image -->

For Host Drive

For Connected Peripheral

<!-- image -->

7. Use the up-down arrow keys select the appropriate action.
- Host and Ports (Preferred): Selects the Host device and all ports for a factory default action.
- This Port Only: Selects only this port for a factory default action. (For a description of a selected menu item, press the INFO soft key)
8. Press the Enter (5) key to display the warning pop-up box to reset defaults.

## Host and Ports (preferred) Pop-up Box

<!-- image -->

Press the ENTER soft key to affirm and set most parameters for the Host Drive and port devices to factory defaults. In this case, refer to the Host Drive and port device user manuals for the settings that will NOT be restored—or press the ESC soft key to cancel.

## This Port Only Pop-up Box

<!-- image -->

Press the MOST soft key to set MOST settings for the selected port device to factory defaults. In this case, refer to the Host Drive User Manual for the settings that will NOT be restored. Press the ALL soft key to set ALL settings for the selected port device to factory defaults—or press the ESC soft key to cancel.

A pop-up Fault warning display follows the parameter changes. This can be reset by pressing the clear soft key. And the following confirm pop-up box can be cleared by pressing the enter soft key. Pressing the escape key twice returns the display to the Status screen.

Refer to the PowerFlex 20-HIM-A6/-C6S HIM (Human Interface Module) User Manual, publication 20HIM-UM001, for further information on using the HIM and the resetting of parameters.

## Sleep/Wake Mode

The purpose of the sleep/wake function is to Start (wake) the drive when an SleepWake RefSel signal is greater than or equal to the value in P354 [Wake Level], and Stop (sleep) the drive when an analog signal is less than or equal to the value in P352 [Sleep Level]. Setting P350 [Sleep Wake Mode] to 1 "Direct" enables the sleep/wake function to work as described.

An Invert mode also exists that changes the logic so that an analog value less than or equal to P354 [Wake Level] starts the drive and an SleepWake RefSel signal greater than or equal to P352 [Sleep Level] stops the drive.

Related Sleep/Wake parameters noted below.

| Parameter No. Parameter Name Description   |                                                                                              |
|--------------------------------------------|----------------------------------------------------------------------------------------------|
|                                            | 350 Sleep Wake Mode Enables/disables the Sleep/Wake function.                                |
| 351                                        | SleepWake RefSel Selects the source of the input controlling the sleep/wake function.        |
| 352                                        | Sleep Level Defines the SleepWake RefSel signal level that stops the drive.                  |
| 353                                        | Sleep Time Defines the amount of time at or below 352 [Sleep Level] before a Stop is issued. |
| 354                                        | Wake Level Defines the SleepWake RefSel signal level that starts the drive.                  |
| 355                                        | Wake Time Defines the amount of time at or above 354 [Wake Level] before a Start is issued.  |

## Sleep/Wake Operation

<!-- image -->

## Requirements

In addition to enabling the sleep function with P350 [Sleep Wake Mode], the following conditions must be met:

- A proper value must be programmed for P352 [Sleep Level] and P354 [Wake Level].
- A sleep/wake reference must be selected in P351 [SleepWake RefSel].
- At least one of the following must be programmed (and input closed) in P155 [DI Enable], P158 [DI Stop], P163 [DI Run], P164 [DI Run Forward], or P165 [DI Run Reverse].

## Conditions to Start/Restart

<!-- image -->

ATTENTION: Enabling the sleep/wake function can cause unexpected machine operation during the Wake mode. Equipment damage and/or personal injury can result if this parameter is used in an inappropriate application. Do not use this function without considering the Table 9 below and applicable local, national and international codes, standards, regulations or industry guidelines.

Table 9 - Conditions Required to Start Drive (1)(2)(3)

|                             | Input After Powerup                                 | After a Drive Fault                                   | After a Drive Fault                                                                             | After a Stop Command                                                                                                                                    |
|-----------------------------|-----------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Input After Powerup                                 |                                                       | Reset by HIM or Software “Stop” Reset by HIM, Network/Software, or Digital Input “Clear Faults” | HIM, Network/Software or Digital Input “Stop”                                                                                                           |
| Stop (4)                    | Stop Closed Wake Signal New Start or Run Command(5) | Stop Closed Wake Signal New Start or Run Command(5)   | Stop Closed Wake Signal                                                                         | Stop Closed Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8) New Start or Run Command(5)   |
|                             | Enable Enable Closed Wake Signal                    | Enable Closed Wake Signal New Start or Run Command(5) | Enable Closed Wake Signal                                                                       | Enable Closed Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8) New Start or Run Command(5) |
| Run Run Forward Run Reverse | Run Closed Wake Signal                              | New Run Command(6) Wake Signal                        | Run Closed Wake Signal                                                                          | New Run Command Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8)                           |

For Invert function, refer to the [Anlg Inn LssActn] parameter.

Normal operation requires that P354 [Wake Level] be set greater than P352 [Sleep Level]. However, there are no limits that prevent the parameter settings from crossing, but the drive will not start until such settings are corrected. These levels are programmable while the drive is running. If P352 [Sleep Level] is made greater than P354 [Wake Level] while the drive is running, the drive continues to run as long as the P351 [SleepWake RefSel] signal remains at a level that doesn't trigger the sleep condition. P353 [Sleep Time] is also factored into this as well. Once the drive goes to sleep in this situation, it is not allowed to restart until the level settings are corrected (increase P354 [Wake Level], or decrease P352 [Sleep Level]). If however, the levels are corrected prior to the drive going to sleep, normal Sleep/Wake operation continues.

## Timers

P353 [Sleep Time] P355 [Wake Time]

Timers determine the length of time required for Sleep/Wake levels to produce true functions. These timers start counting when the Sleep/Wake levels are met and count in the opposite direction whenever respective level is not met. If the timer counts all the way to the user specified time, it creates an edge to toggle the Sleep/Wake function to the respective condition (sleep or wake). On powerup, timers are initialized to the state that does not permit a start condition. When the analog signal satisfies the level requirement, the timers start counting.

## Interactive Functions

Separate start commands are also honored (including a digital input start), but only when the sleep timer is not satisfied. Once the sleep timer times out, the sleep function acts as a continuous stop. There are two exceptions that ignore the Sleep/Wake function.

1. When a device is commanding local control, that is HIM in Manual mode or a digital input programmed to P172 [DI Manual Ctrl].
2. When a jog command is being issued.

When a device is commanding local control, the port that is commanding it has exclusive start control (in addition to ref select), essentially overriding the Sleep/ Wake function, and allowing the drive to run in the presence of a sleep situation. This holds true even for the case if digital input is programmed to P172 [DI Manual Ctrl], a digital input start or run is able to override a sleep situation.

## Sleep/Wake Sources

The P351 [SleepWake RefSel] signal source for the sleep/wake function can be any analog input, whether it is being used for another function or not, a DeviceLogix software source (P90 [DLX Real OutSP1] thru P97 [DLX Real OutSP8]), or a valid numeric edit configuration. Configuring the sleep/wake source is done through P351 [SleepWake RefSel].

Also, [Anlg Inn Hi] and [Anlg Inn Lo] parameters have no effect on the function, however, the factory calibrated result, [Anlg Inn Value] parameter, is used. In addition, the absolute value of the calibrated result is used, thus making the function useful for bipolar direction applications.

The analog in loss function, configured by the [Anlg Inn LssActn] parameter, is unaffected and therefore operational with the sleep/wake function, but not tied to the sleep or wake levels and is triggered off the [Anlg Inn Raw Value] parameter.

Refer to the PowerFlex 750-Series Programming Manual, publication 750PM001, for more details.

## Start Permissives

Start permissives are conditions required to permit the drive to start in any mode, such as run, jog, or auto-tune. When all permissive conditions are met, the drive is considered ready to start. The ready condition is confirmed through the ready status in P935 [Drive Status 1].

## Permissive Conditions

- No faults can be active.
- No Type 2 alarms can be active.
- The DI Enable input, if configured, must be closed.
- The DC bus precharge logic must indicate it is a start permissive.
- All Stop inputs must be negated nor any drive functions are issuing a stop.
- No configuration changes (parameters being modified) can be in-progress.
- The drive's safety option module logic must be satisfied.

If a CIP Motion connection is active and if alignment is set to "Not Aligned" then the "CommutNotCfg" bit is high (on). To clear this start inhibit, from the Axis Properties within the Logix Designer application, run a Commutation Test, enter the proper value into the Offset and then set the Alignment to "Controller Offset."

<!-- image -->

If all permissive conditions are met, a valid start, run or jog command starts the drive. The status of all current inhibit conditions are reflected in P933 [Start Inhibits] and the last inhibit conditions are reflected in P934 [Last StrtInhibit] details are shown below.

<!-- image -->

## Stop Modes

Stop Mode A/B can be configured as a method of stopping the drive when a stop command is given. A normal stop command and the run input changing from true to false results in a normal stop command. However, when using TorqueProve, P1100 [Trq Prove Cfg] with Bit 0 enabled, [Stop Mode A/B] must be set to 1 "Ramp."

P392 [Stop Dwell Time] can also be used with a stop command. This can be used to set an adjustable time between detecting zero speed and turning off the drive output.

The PowerFlex 750 series offers several methods for stopping a load. The stop method or mode is defined by parameters 370/371 [Stop Mode A/B] These modes include the following:

- Coast
- Ramp
- Ramp to Hold
- DC Brake
- DC Brake Auto Off
- Current Limit
- Fast Brake

Additionally, P388 [Flux Braking In] can be selected separately (not part of the Stop mode selection) to provide additional braking during a Stop command or when reducing the speed command. For Stop commands, this provides additional braking power during "Ramp" or "Ramp to Hold" selections only. If "Fast Brake" or "DC Brake" is used, "Flux Braking" is active only during speed changes (if enabled).

A "Ramp" selection always provides the fastest stopping time if a method to dissipate the required energy from the DC bus is provided (that is Dynamic Braking resistor, regenerative brake, and so forth.). The PowerFlex Dynamic Braking Selection Guide presented in Appendix A of the Reference Manual, explains Dynamic Braking in detail.

The alternative braking methods to external hardware brake requirements, can be enabled if the stopping time is not as restrictive. Each of these methods dissipates energy in the motor (use care to avoid motor overheating).

## Braking Methods

| Method Use when application Requires Braking Power                                                                                                                                                                                                                                              |                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Coast Power is removed from the motor and it coasts to zero speed                                                                                                                                                                                                                               | None                         |
| Ramp The fastest stopping time or fastest ramp time for speed changes (external brake resistor or regenerative capability required for ramp times faster than the methods below). High duty cycles, frequent stops or speed changes. (The other methods can result in excessive motor heating). | The most                     |
| Ramp to Hold Same as ramp above only when zero speed is reach the drive outputs a DC brake current to be sure the motor shaft doesn't move after it has stopped. This continues until the drive is started again.                                                                               | Same as “Ramp”               |
| DC Brake DC braking is immediately applied (does not follow programmed decel ramp). May have to adjust P397 [DC Brake Kp].                                                                                                                                                                      | Less than Ramp or Fast Brake |
| DCBrkAutoOff Applies DC braking until zero speed is reached or DC brake time is reached, whichever is shorter.                                                                                                                                                                                  | Less than Ramp or Fast Brake |
| Current Lmt Max torque / current applied until zero speed                                                                                                                                                                                                                                       | Big Stuff                    |
| Fast Brake High slip braking for maximum braking performance above base speed. More than DC                                                                                                                                                                                                     | Brake / DC Brake Auto Off    |

## Coast

<!-- image -->

Coast is selected by setting P370/371 [Stop Mode A/B] to 0 "Coast." When in Coast to Stop, the drive acknowledges the Stop command by shutting off the output and releasing control of the motor. The load/motor will coast or free spin until the kinetic energy is dissipated.

- On Stop, the drive output goes immediately to zero (off ).
- No further power is supplied to the motor. The drive has released control.
- The motor coasts for a time that is dependent on the mechanics of the system (Inertia, friction, and so forth).

## DC Brake

<!-- image -->

This method uses DC injection of the motor to Stop and/or hold the load. DC Brake is selected by setting P370/371 [Stop Mode A/B] to 3 "DC Brake." You can also choose the amount of time the braking is applied and the magnitude of the current used for braking with P395 [DC Brake Time] and P394 [DC Brake Level]. This mode of braking generates up to 40% of rated motor torque for braking and is typically used for low inertia loads with infrequent Stop cycles:

- On Stop, 3 phase drive output goes to zero (off ).
- Drive outputs DC voltage on the last used phase to provide the current level programmed in P394 [DC Brake Level]. This voltage causes a stopping brake torque. If the voltage is applied for a time that is longer than the actual possible stopping time, the remaining time is used to attempt to hold the motor at zero speed (decel profile "B" on the diagram above).
- DC voltage to the motor continues for the amount of time programmed in P395 [DC BrakeTime]. Braking ceases after this time expires.
- After the DC Braking ceases, no further power is supplied to the motor. The motor/load may or may not be stopped. The drive has released control of the motor/load (decel profile "A" on the diagram above).
- The motor, if rotating, coasts from its present speed for a time that is dependent on the remaining kinetic energy and the mechanics of the system (inertia, friction, and so forth).
- Excess motor current and/or applied duration, could cause motor damage. Motor voltage can exist long after the Stop command is issued. The right combination of Brake Level and Brake Time must be determined to provide the safest, most efficient stop (decel profile "C" on the diagram above).

<!-- image -->

This method uses drive output reduction to stop the load.

Ramp To Stop is selected by setting parameters 370/371[Stop Mode A/B] to 1 "Ramp." The drive ramps the frequency to zero based on the deceleration time programmed into parameters 537/538 [Decel Time 1/2]. The normal mode of machine operation can utilize [Decel Time 1]. If the machine Stop requires a faster deceleration than desired for normal deceleration, [Decel Time 2] can be activated with a faster rate selected. When in Ramp mode, the drive acknowledges the Stop command by decreasing or ramping the output voltage and frequency to zero in a programmed period (Decel Time), maintaining control of the motor until the drive output reaches zero. The drive output is then shut off. The load/motor follows the decel ramp. Other factors such as bus regulation and current limit can alter the actual decel rate.

Ramp mode can also include a timed hold brake. Once the drive has reached zero output hertz on a Ramp-to-Stop and both parameters 395 [DC Brake Time] and P394 [DC Brake Level] are not zero, the drive applies DC to the motor producing current at the DC Brake Level for the DC Brake Time:

- On Stop, drive output decreases according to the programmed pattern from its present value to zero. The pattern can be linear or squared. The output decreases to zero at the rate determined by the programmed P520 [Max Fwd Speed] or P521 [Max Rev Speed] and the programmed active (Decel Time n).
- The reduction in output can be limited by other drive factors such as bus or current regulation.
- When the output reaches zero the output is shut off.
- The motor, if rotating, coasts from its present speed for a time that is dependent on the mechanics of the system (inertia, friction, and so forth).

## Ramp to Hold

<!-- image -->

This method combines two of the methods above. It uses drive output reduction to stop the Load and DC injection to hold the load at zero speed once it has stopped:

- On Stop, drive output decreases according to the programmed pattern from its present value to zero. The pattern can be linear or squared. The output decreases to zero at the rate determined by the programmed P37 [Maximum Freq] and the programmed active P537/538 [Decel Time 1/2]
- The reduction in output can be limited by other drive factors such as bus or current regulation.
- When the output reaches zero 3 phase drive output goes to zero (off ) and the drive outputs DC voltage on the last used phase to provide the current level programmed in P394 [DC Brake Level]. This voltage causes a holding brake torque.
- DC voltage to the motor continues until a Start command is reissued or the drive is disabled.
- If a Start command is reissued, DC Braking ceases and the drive returns to normal AC operation. If an Enable command is removed, the drive enters a Not Ready state until the enable is restored.

## Fast Brake

<!-- image -->

This method takes advantage of the characteristic of the induction motor whereby frequencies greater than zero (DC braking) can be applied to a spinning motor that provides more braking torque without causing the drive to regenerate:

- On Stop, the drive output decreases based on the motor speed, keeping the motor out of the regen region. This is accomplished by lowering the output frequency below the motor speed where regeneration does not occur. This causes excess energy to be lost in the motor.
- The method uses a PI based bus regulator to regulate the bus voltage to a reference (that is 750V) by automatically decreasing output frequency at the proper rate.
- When the frequency is decreased to a point where the motor no longer causes the bus voltage to increase, the frequency is forced to zero. DC brake is used to complete the stop if the DC Braking Time is non-zero, then the output is shut off.
- Use of the current regulator verifies that over current trips don't occur and allow for an easily adjustable and controllable level of braking torque.
- Use of the bus voltage regulator results in a smooth, continuous control of the frequency and forces the maximum allowable braking torque to be utilized at all times.

## IMPORTANT

For this feature to function properly the active [Bus Reg Mode A/B] must be set to 1 "Adjust Freq" and not be 0 "Disabled."

<!-- image -->

## Block Diagram

<!-- image -->

<!-- image -->

Current Limit stop is not typically set up as the normal Stop mode. Usually the normal stop is programmed at some ramp rate. For the current limit stop a digital input is used for the function. However, you certainly could set the normal stop as CurrentLimit Stop

Current limit stop ramp rate is 0.1 second and is not programmable

## Example

<!-- image -->

In this example the current limit was set high enough to allow the full rating of the drive to be used in the stop sequence.

## Voltage Class

<!-- image -->

In this example the current limit was set at some value such that when the stop was issued the output current was clamped at that setting. Note the decel time is extended.

PowerFlex drives are sometimes referred to by voltage class, which identifies the general input voltage to the drive. P305 [Voltage Class] includes a range of voltages. For example, a 400V class drive has an input voltage range of 380…480V AC. While the hardware remains the same for each class, other variables, such as factory defaults, catalog number, and power unit ratings change. In most cases the voltage of a drive can be reprogrammed to another value within the class by resetting the defaults to something other than factory settings.

P305 [Voltage Class], is required by the drive when parameter downloads occur and is generally not programmed individually. This parameter provides a "Low Voltage" and "High Voltage" setting. The default value is dependent upon the voltage that matches the catalog number (for example 400V or 480V). For example, a drive shipped as 400V (catalog code "C") has a default of "Low Voltage" for P305 [Voltage Class]. A drive shipped as 480V (catalog code "D") has a default of "High Voltage."

When a change is made to P305 [Voltage Class], the continuous current rating of the drive changes by an amount equal to the published difference between catalog numbers. With a change to the current rating, review P422 [Current Limit 1] and P423 [Current Limit 2].

Also note that a Reset to Defaults "All" resets the voltage to the original factory setting.

## Analog Inputs

## Feedback and I/O

| Topic                      |   Page |
|----------------------------|--------|
| Analog Inputs              |    105 |
| Analog Outputs             |    113 |
| Digital Inputs             |    119 |
| Digital Outputs            |    130 |
| PTC Motor Thermistor Input |    152 |

There are two analog inputs per I/O module. Up to four I/O modules can be mounted in the drive ports. See the PowerFlex 750-Series Installation Instructions, publication 750-IN001, for valid ports. Accessing the analog input parameters is done by selecting the port that the module is mounted in, then accessing the Analog Input group of parameters.

<!-- image -->

<!-- image -->

## Analog Input Specifications

<!-- image -->

| Terminal Name                           | Description                                                                                                                                                                                      | Related Param (5)   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Sh Shield                               | Terminating point for wire shields when an EMC plate or conduit box is not installed.                                                                                                            |                     |
| Sh Shield                               | Ptc– Motor PTC (–) Motor protection device (Positive Temperature Coefficient). Temperature Coefficient). on Port X Ptc+ Motor PTC (+)                                                                                                                                                                                                  | 40                  |
|                                         | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 75 on Port X        |
| Ao0+ Analog Out 0 (+)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 75 on Port X        |
| Ao1– Analog Out 1 (–)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 85 on Port X        |
| Ao1+ Analog Out 1 (+)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 85 on Port X        |
| –10V –10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
|                                         | 10VC 10 Volt Common For (–) and (+) 10 Volt references.                                                                                                                                          |                     |
| +10V +10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
| Ai0– Analog Input 0 (–) Isolated        | (3) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance.                                                                                                        | 50, 70 on Port X    |
| Ai0+ Analog Input 0 (+)                 | (3) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance.                                                                                                        | 50, 70 on Port X    |
| Ai1– Analog Input 1 (–)                 | (3) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance.                                                                                                        | 60, 70 on Port X    |
| Ai1+ Analog Input 1 (+)                 | Current mode: 0-20 mA @ 93 ohm input impedance.                                                                                                                                                  | 60, 70 on Port X    |
| 24VC 24 Volt Common (1)                 | Drive supplied logic input power. 200 mA max per I/O module 600 mA max per drive                                                                                                                 |                     |
| +24V +24 Volt DC (1)                    | Drive supplied logic input power. 200 mA max per I/O module 600 mA max per drive                                                                                                                 |                     |
|                                         | Di C Digital Input Common Common for Digital Inputs 0…5                                                                                                                                          |                     |
| Di 0 Digital Input 0  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 1 Digital Input 1  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 2 Digital Input 2  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 3 Digital Input 3  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 4 Digital Input 4  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 5 Digital Input 5  (2)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (4)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |

## Analog Scaling

```
[Anlg Inn Lo] [Anlg Inn Hi]
```

A scaling operation is performed on the value read from an analog input to convert it to units usable for some particular purpose. Control the scaling by setting parameters that associate a low and high analog value (in volts or mA) with a low and high target (in Hz).

## Example 1

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P547 [Spd Ref A AnlgHi] = 60 Hz
- P548 [Spd Ref A AnlgLo] = 0 Hz
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In1 Lo] = 0V

This is the default setting, where 0V represents 0 Hz and 10V represents 60 Hz providing 1024 steps (10 bit analog input resolution) between 0 and 60 Hz.

<!-- image -->

## Example 2

Consider the following setup:

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In1 Lo] = 0V
- P547 [Spd Ref A AnlgHi] = 60 Hz
- P548 [Spd Ref A AnlgLo] = 0 Hz
- P520 [Max Fwd Speed] = 45 Hz
- P522 [Min Fwd Speed] = 15 Hz

This configuration is used when non-default settings are desired for minimum and maximum speeds, but full range (0…10V) scaling from 0…60 Hz is still desired.

<!-- image -->

In this example, a deadband from 0…2.5V and from 7.5…10V is created. Alternatively, the analog input deadband could be eliminated while maintaining the 15 and 45 Hz limits with the following changes:

- P548 [Spd Ref A AnlgLo] = 15 Hz
- P547 [Spd Ref A AnlgHi] = 45 Hz

## Example 3

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P547 [Spd Ref A AnlgHi] = 30 Hz
- P548 [Spd Ref A AnlgLo] = 0 Hz
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In1 Lo] = 0V

This is an application that requires only 30 Hz as a maximum output frequency but is still configured for full 10V input. The result is that the resolution of the input has been doubled, providing 1024 steps between 0 and 30 Hz.

<!-- image -->

## Example 4

- P255 [Anlg In Type], Bit 0 = "1" (Current)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P547 [Spd Ref A AnlgHi] = 60 Hz
- P548 [Spd Ref A AnlgLo] = 0 Hz
- P61 [Anlg In1 Hi] = 20 mA
- P62 [Anlg In1 Lo] = 4 mA

This configuration is referred to as offset. In this case, a 4…20 mA input signal provides 0…60 Hz output, providing a 4 mA offset in the speed command.

<!-- image -->

## Example 5

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P547 [Spd Ref A AnlgHi] = 0 Hz
- P548 [Spd Ref A AnlgLo] = 60 Hz
- P61 [Anlg In1 Hi] = 10V
- P62 [Anlg In1 Lo] = 0V

This configuration is used to invert the operation of the input signal. Here, maximum input (10V) represents 0 Hz and minimum input (0V) represents 60 Hz.

<!-- image -->

## Example 6

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P545 [Spd Ref A Sel] = "Analog In 1"
- P547 [Spd Ref A AnlgHi] = 60 Hz
- P548 [Spd Ref A AnlgLo] = 0 Hz
- P61 [Anlg In1 Hi] = 5V
- P62 [Anlg In1 Lo] = 0V

This configuration is used when the input signal is 0…5V. Here, minimum input (0V) represents 0 Hz and maximum input (5V) represents 60 Hz. This provides full scale operation from a 0…5V source.

<!-- image -->

## Example 7

- P255 [Anlg In Type], Bit 0 = "0" (Voltage)
- P675 [Trq Ref A Sel] = "Analog In 1"
- P677 [Trq Ref A AnlgHi] = 200%
- P678 [Trq Ref A AnlgLo] = 0%

This configuration is used when the input signal is 0…10V. The minimum input of 0V represents a torque reference of 0% and maximum input of 10V represents a torque reference of 200%.

<!-- image -->

## Square Root

The square root function can be applied to each analog input through the use of P256 [Anlg In Sqrt]. Enable the function if the input signal varies with the square of the quantity (for example drive speed) being controlled.

If the mode of the input is bipolar voltage (-10…10V), then the square root function returns 0 for all negative voltages.

The function uses the square root of the analog value as compared to its full scale (for example ) and multiplies it times the full scale of
5V 0.5 or 50% and 0.5 0.707 = = what it controls (for example 60 Hz). 5V 0.5 or 50% and 0.5 0.707 = =

The complete function can be describes as follows:

<!-- formula-not-decoded -->

Setting high and low values to 0V, 10V, 0 Hz, and 60 Hz, the expression reduces to the following:

<!-- formula-not-decoded -->

<!-- image -->

## Analog Input Loss Detection

Signal loss detection can be detected for each analog input. P47 [Anlg In Loss Sts] bits 0, 1, 2 indicate if the signal is lost. Bit 0 indicates that one or both signals are lost. P53 [Anlg In0 LssActn] and P63 [Anlg In1 LssActn] defines what action the drive takes when loss of any analog input signal occurs.

Selects drive action when an analog signal loss is detected. Signal loss is defined as an analog signal less than 1V or 2 mA. The signal loss event ends and normal operation resumes when the input signal level is greater than or equal to 1.5V or 3 mA.

- "Ignore" (0) – No action is taken.
- "Alarm" (1) – Type 1 alarm indicated.
- "Flt Minor" (2) – Minor fault indicated. If running, drive continues to run. Enable with P950 [Minor Flt Cfg]. If not enabled, acts like a major fault.
- "FltCoastStop" (3) – Major fault indicated. Coast to Stop.
- "Flt RampStop" (4) – Major fault indicated. Ramp to Stop.
- "Flt CL Stop" (5) – Major fault indicated. Current Limit Stop.
- "Hold Input" (6) – Holds input at last value.
- "Set Input Lo" (7) – Sets input to P52 [Anlg In0 Lo] or P62 [Anlg In1 Lo].
- "Set Input Hi" (8) – Sets input to P51 [Anlg In0 Hi] or P61 [Anlg In1 Hi].

If the input is in Current mode, 4 mA is the normal minimum usable input value. Any value below 3.2 mA is interpreted by the drive as a signal loss, and a value of 3.8 mA is required on the input for the signal loss condition to end.

If the input is in Unipolar Voltage mode, 2V is the normal minimum usable input value. Any value below 1.6V is interpreted by the drive as a signal loss, and a value of 1.9V is required on the input for the signal loss condition to end. No signal loss detection is possible while an input is in Bipolar Voltage mode. The signal loss condition never occurs even if signal loss detection is enabled.

## Analog Outputs

There are two analog outputs per I/O module. Up to five I/O modules can be mounted in the drive ports. See 750-IN001 for valid ports. Accessing the analog output parameters is done by selecting the port that the module is mounted in then accessing the Analog Output group of parameters.

## Analog Output Specifications

<!-- image -->

| Terminal Name                           | Description                                                                                                                                                                                      | Related Param (4)   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Sh Shield                               | Terminating point for wire shields when an EMC plate or conduit box is not installed.                                                                                                            |                     |
| Sh Shield                               | Ptc– Motor PTC (–) Motor protection device (Positive Temperature Coefficient). Temperature Coefficient). on Port X Ptc+ Motor PTC (+)                                                                                                                                                                                                  | 40                  |
|                                         | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 75 on Port X        |
| Ao0+ Analog Out 0 (+)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 75 on Port X        |
| Ao1– Analog Out 1 (–)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 85 on Port X        |
| Ao1+ Analog Out 1 (+)                   | Ao0– Analog Out 0 (–) Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                          | 85 on Port X        |
| –10V –10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
|                                         | 10VC 10 Volt Common For (–) and (+) 10 Volt references.                                                                                                                                          |                     |
| +10V +10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
| Ai0– Analog Input 0 (–) Isolated        | (2) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. impedance. Ai1– Analog Input 1 (–) 60, 70                                                                                                                                                                                                  | 50, 70 on Port X    |
| Ai0+ Analog Input 0 (+)                 | (2) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. impedance. Ai1– Analog Input 1 (–) 60, 70                                                                                                                                                                                                  | 50, 70 on Port X    |
|                                         | (2) , bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. impedance. Ai1– Analog Input 1 (–) 60, 70                                                                                                                                                                                                  | on Port X           |
| Ai1+ Analog Input 1 (+)                 | Current mode: 0-20 mA @ 93 ohm input impedance.                                                                                                                                                  | on Port X           |
|                                         | 24VC 24 Volt Common Drive supplied logic input power. 200 mA max per I/O module 600 mA max per drive                                                                                             |                     |
| +24V +24 Volt DC                        | 24VC 24 Volt Common Drive supplied logic input power. 200 mA max per I/O module 600 mA max per drive                                                                                             |                     |
|                                         | Di C Digital Input Common Common for Digital Inputs 0…5                                                                                                                                          |                     |
| Di 0 Digital Input 0  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 1 Digital Input 1  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 2 Digital Input 2  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 3 Digital Input 3  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 4 Digital Input 4  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |
| Di 5 Digital Input 5  (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1 on Port X         |

## Analog Output Configuration

Parameters 75 and 85 [Anlg Outn Select] are use to specify the signal used on Analog Outputs 1 and 2, respectively. These parameters can be programmed to the following selections.

| Parameter No. Parameter Name   |
|--------------------------------|
| 1 Output Frequency             |
| 2  Commanded SpdRef            |
| 3 Mtr Vel Fdbk                 |
| 4  Commanded Trq               |
| 5  Torque Cur Fdbk             |
| 6 Flux Cur Fdbk                |
| 7 Output Current               |
| 8 Output Voltage               |
| 9 Output Power                 |
| 11  DC Bus Volts               |

## Scaling

The scaling for the analog output is defined by entering analog output voltages into two parameters, P91 [Anlg Out1 Lo] and P90 [Anlg Out1 Hi]. These two output voltages correspond to the bottom and top of the possible range covered by the quantity being output. Scaling of the analog outputs is accomplished with low and high analog parameter settings that are associated with fixed ranges (see the PowerFlex 750-Series Programming Manual, publication 750-PM001,) for each target function. Additionally, the PowerFlex 755 contains an adjustable scale factor to override the fixed target range. P77 [Anlg Out0 Data] and 82 [Anlg Out0 Val] are described in the following charts.

## Case 1

Case 1: This shows P77 [Anlg Out0 Data] the units are consistent with the selection of P75 [Anlg Out0 Sel]. In this case, the analog out select is set to P3 [Mtr Vel Fdbk] and the units are in rpm. P80 [Anlg Out0 Hi], P81 [Anlg Out0 Lo], P78 [Anlg Out0 DataHi], and P79 [Anlg Out0 DataLo] are all at default. The motor was started and ramped to 1800 rpm. Note that P82 [Anlg Out0 Val] remained zero.

<!-- image -->

- Case 2: Here the P80 [Anlg Out0 Hi] is changed to 9 and P81 [Anlg Out0 Lo] is changed to 1. As the motor ramps up and down, there is no change in the value or scaling of P77 [Anlg Out0 Data]. Note that P82 [Anlg Out0 Val] is still zero.

Case 3: Now P78 [Anlg Out0 DataHi] is changed to 1800 and P79 [Anlg Out0 DataLo] is left at zero. When started P82 [Anlg Out0 Val] starts at 1 and reaches 9 when the motor speed is at maximum.

Case 4: In this section the P80 [Anlg Out0 Hi] and P81 [Anlg Out0 Lo] were reversed in value. Now when the motor ramps up and down P82 [Anlg Out0 Val] is just the opposite. It starts out at 9 and is at 1 at full speed.

Case 2

<!-- image -->

## Case 3

<!-- image -->

## Absolute (Default)

Certain quantities used to drive the analog output are signed, for example the quantity can be both positive and negative. You have the option of having the absolute value (value without sign) of these quantities taken before the scaling occurs. Absolute value is enabled separately for each analog output via the bit enumerated P71 [Analog Out Abs].

## Setpoint

Setpoint is a possible source for an analog output. It can be used to control an analog output from a communication device using a DataLink. Change P75 [Anlg Out0 Sel] to 76 [Anlg Out0 Stpt]. Then map a datalink to P76 and you'll be able to drive the analog output over a network.

<!-- image -->

## Digital Inputs

Physical inputs are programmed to desired digital input functions. These parameters cannot be changed while the drive is running.

## Technical Information

The PowerFlex 753 drive has three digital inputs on its main control board:

- Di 0 – Configured for 115V AC or 24V DC
- – Shared common (Di C) between Di 0ac and Di 0dc terminals
- – TB3 - bottom of the main control board
- Di 1 and Di 2 – Configured for 24V DC
- – Shared common (Di C) for Di 1 and Di 2
- – TB1 - lower front of the main control board

PowerFlex 753 Main Control Board I/O TB1 wiring examples are included in the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001 .

The PowerFlex 755 drive has one digital input on its main control board:

- Di0 – configured for 115V AC or 24V DC
- – Shared common (Di C) between Di 0ac and Di 0dc terminals
- – TB1 - bottom of the main control board

There are also PowerFlex 750-Series option modules that expand the amount of digital inputs that can be used in both the PowerFlex 753 and 755 drives.

20-750-2262C-2R / 20-750-2263C-1R2T

- Six 24V DC input terminals:
- – Labeled as Di 0, Di 1, Di 2, Di 3, Di 4 and Di 5
- – Shared common (Di C)
- – TB1 - front of the option module

## 20-750-2262D-2R

- Six 115V AC input terminals:
- – Labeled as Di 0, Di 1, Di 2, Di 3, Di 4 and Di 5
- – Shared common terminal (Di C)
- – TB1 - front of the option module

PowerFlex 750-Series Option Modules I/O TB1 wiring examples are included in the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001 .

## Configuration

Digital inputs can be programmed to a desired function defined by Parameters 155 to 201 below. These parameters cannot be changed while the drive is running.

|                                                               |                                                         | Number Parameter Name Number Parameter Name Number Parameter Name   |
|---------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------|
| 155 DI Enable                                                 |                                                         | 170 DI Jog 2 Forward 187 DI PwrLoss ModeB                           |
|                                                               | 156 DI Clear Fault 171 DI Jog 2 Reverse 188 DI Pwr Loss |                                                                     |
|                                                               | 157 DI Aux Fault 172 DI Manual Ctrl 189 DI Precharge    |                                                                     |
| 158 DI Stop                                                   | 173 DI Speed Sel 0 190 DI Prchrg Seal                   |                                                                     |
| 159 DI Cur Lmt Stop 174 DI Speed Sel 1 191 DI PID Enable      |                                                         |                                                                     |
|                                                               | 160 DI Coast Stop 175 DI Speed Sel 2 193 DI PID Hold    |                                                                     |
| 161 DI Start                                                  | 176 DI HOA Start 193 DI PID Reset                       |                                                                     |
| 162 DI Fwd Reverse 177 DI MOP Inc 194 DI PID Invert           |                                                         |                                                                     |
| 163 DI Run                                                    |                                                         | 178 DI MOP Dec 195 DI Torque StptA                                  |
| 164 DI Run Forward 179 DI Accel 2                             |                                                         | 196 DI Fwd End Limit                                                |
| 165 DI Run Reverse 180 DI Decel 2                             |                                                         | 197 DI Fwd Dec Limit                                                |
| 166 DI Jog 1                                                  |                                                         | 181 DI SqTqPs Sel 0 198 DI Rev End Limit                            |
| 167 DI Jog 1 Forward 182 DI SqTqPs Sel 1 199 DI Rev Dec Limit |                                                         |                                                                     |
|                                                               |                                                         | 168 DI Jog 1 Reverse 185 DI Stop Mode B 200 DI PHdwr OvrTrvl        |
| 169 DI Jog 2                                                  | 186 DI BusReg Mode B 201 DI NHdwr OvrTrvl               |                                                                     |

Operation for DI Run type parameters can be defined by P150 [Digital In Cfg]:

- "Run Edge" (0) – Control function requires a rising edge (open to close transition) for the drive to run.
- "Run Level" (1) – As long as a separate "Stop" command is not issued, the level alone (no rising edge required) determines whether the drive runs. When set to 1 "Run Level" the absence of a run command is indicated as a stop asserted and P935 [Drive Status 1] Bit 0 is low.

<!-- image -->

ATTENTION: Equipment damage and/or personal injury may result if this parameter is used in an inappropriate application. Do not use this function without considering applicable local, national and international codes, standards, regulations, or industry guidelines.

## Functional Descriptions

## DI Enable

Closing this input lets the drive run when a Start command is issued. If the drive is already running when this input is opened, the drive will coast stop and indicate "not enabled" on the HIM (if present). This is not considered a fault condition, and no fault is generated. If this function is not configured, the drive is considered enabled.

| IMPORTANT   | If the ENABLE (J1) jumper is removed, the Di 0 becomes a hardware enable. For the PowerFlex 753, Di 0 is found on TB3 and for the PowerFlex 755, Di 0 is found on TB1.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

A combination of the hardware enable and a software enable can be utilized; however, the drive will not run if any of the inputs are open.

## DI Clear Fault

The "Clear Fault" digital input function lets an external device reset drive faults through the terminal block. An open to closed transition on this input causes an active fault (if any) to be reset.

## DI Aux Fault

This input function is normally closed and lets external equipment fault the drive. When this input opens, the drive faults on a F2 "Auxiliary Input" fault code. If this input function is not configured, the fault will not occur.

## DI Stop

An open input causes the drive to stop and become "Not Ready." A closed input lets the drive run when given a Start or Run command. If "Start" is configured, then "Stop" must also be configured, otherwise, a digital input configuration alarm occurs.

P370 [Stop Mode A] and P371 [Stop Mode B] dictate the drive's stop action. Refer to Stop Modes on page 96 for more details.

## DI Cur Lmt Stop

With this digital input function, an open input causes the drive to current limit stop. The drive acknowledges the stop command by setting the motor speed reference to zero, causing the drive to bring the motor down to zero speed as fast as the power limits, torque limits, and current limits allow. When the drive output reaches zero, the output transistors are shut off.

## DI Coast Stop

With this digital input function, an open input causes the drive to Coast-to-Stop. The drive acknowledges the stop command by shutting off the output transistors and releasing control of the motor. The load/motor will coast or free spin until the mechanical energy is dissipated.

## DI Start

An open to closed transition while the drive is stopped causes the drive to run in the current direction, unless the "Stop" input function is open. If "Start" is configured, then a "Stop" must also be configured.

## DI Fwd Reverse

This digital input function is one of the ways to provide direction control when the "Start" or "Run" functions (not combined with direction) are used. An open input sets direction to forward. A closed input sets direction to reverse. If state of input changes and drive is running or jogging, the drive changes direction.

## DI Run Forward, DI Run Reverse

These digital input functions cause the drive to run and with a specific direction, as long as the configured input is held closed. Also, these "2-wire" settings prevent any other connected device from starting the drive. An open to closed transition on one input or both inputs while the drive is stopped causes the drive to run unless the "Stop" input function is configured and open.

The table below describes the basic action taken by the drive in response to particular states of these input functions.

| Run Forward Run Reverse Action                                                                               |
|--------------------------------------------------------------------------------------------------------------|
| Open Open Drive stops, terminal block relinquishes direction ownership.                                      |
| Open Closed Drive runs in reverse direction, terminal block takes direction ownership.                       |
| Closed Open Drive runs in forward direction, terminal block takes direction ownership.                       |
| Closed Closed Drive continues to run in current direction, but terminal block maintains direction ownership. |

It is not necessary to program both "Run Forward" and "Run Reverse." These two functions operate with or without each other.

## IMPORTANT

Direction control is an "Exclusive Ownership" function (see Owners). This means that only one control device (terminal block, DPI device, HIM, and so forth) at a time is allowed to control direction at a time. The terminal block must become direction "owner" before it can be used to control direction. If another device is currently the direction owner (as indicated by P922 [Dir Owner]), it is not possible to start the drive or change direction by using the terminal block digital inputs programmed for both Run and Direction control (for example Run/Fwd).

## DI Run

This digital input function is similar to "Run Forward" and "Run Reverse" settings. The only difference being that direction is determined by another input or another device's command (HIM or communication adapter).

## DI Jog 1 Forward, DI Jog 1 Reverse, DI Jog 2 Forward, DI Jog 2 Reverse

Jog is a non-latched command such as Run, but overrides the normal speed reference and uses P556 [ Jog Speed 1] or P557 [ Jog Speed 2] respectively.

An open to closed transition on one input or both inputs while the drive is stopped causes the drive to jog unless the "Stop" input function is configured and

open. The table below describes the actions taken by the drive in response to various states of these input functions.

| Jog Forward Jog Reverse Action                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------|
| Open Open Drive stops if already jogging, but can be started by other means. Terminal block relinquishes direction ownership. |
| Open Closed Drive jogs in reverse direction. Terminal block takes direction ownership.                                        |
| Closed Open Drive jogs in forward direction. Terminal block takes direction ownership.                                        |
| Closed Closed Drive continues to jog in current direction, but terminal block maintains direction ownership.                  |

The drive will not jog while the drive is running or while the "Stop" input is open. Start has precedence.

## DI Jog 1, DI Jog 2

These digital input functions are similar to "Jog Forward" and "Jog Reverse" with the only difference being that direction is determined by another input or another device's command (HIM or communication adapter). In addition, these settings use either P556 [ Jog Speed 1] or P557 [ Jog Speed 2], respectively. In Unipolar mode, the absolute value is used along with a separate direction command. In Bipolar mode, the polarity of P556 [ Jog Speed 1] or P557 [ Jog Speed 2] determines the direction of jog.

## DI Manual Ctrl

The digital input function works in conjunction with the overall Auto/Manual function. When this input is closed, it overrides other speed references, but only if another device (HIM) did not have ownership of the Manual state. If the digital input is successful in gaining manual control, the speed reference comes from P563 [DI ManRef Sel], which can be set to any of the Analog Inputs, Preset Speeds, MOP Reference, or an applicable Port Reference.

Associated with this digital input function, there is the ability to configure the drive to switch smoothly from an automatic (communicated) speed reference to manual speed reference produced by the Human Interface Module (HIM). When the drive is commanded to switch from the automatic (communicated) speed reference to the manual reference via a digital input, it preloads the last value from the speed feedback into the HIM. Then the operator can modify the manual reference on the HIM. This avoids a step change in speed that otherwise occurs from the switch. Use this feature by configuring P328 [Alt Man Ref Sel], P331 [Manual Preload], P172 [DI Manual Ctrl], and P563 [DI ManRef Sel]. This feature requires revision 2.001 of 20-HIM-A6 firmware or later.

## DI Speed Sel 0, 1, and 2

These digital input functions can be used to select the speed reference. The open/ closed state of all the speed select digital input functions combine to select which source is the speed reference.

|    |    | DI Speed Sel 2 DI Speed Sel 1 DI Speed Sel 0 Auto Reference Source (Parameter)   |
|----|----|----------------------------------------------------------------------------------|
|  0 |  0 | 0 Reference A (P545 [Spd Ref A Sel])                                             |
|  0 |  0 | 1 Reference A (P545 [Spd Ref A Sel])                                             |
|  0 |  1 | 0 Reference B (P550 [Spd Ref B Sel])                                             |
|  0 |  1 | 1 Preset Speed 3 (P573 [Preset Speed 3])                                         |
|  1 |  0 | 0 Preset Speed 4 (P574 [Preset Speed 4])                                         |
|  1 |  0 | 1 Preset Speed 5 (P575 [Preset Speed 5])                                         |
|  1 |  1 | 0 Preset Speed 6 (P576 [Preset Speed 6])                                         |
|  1 |  1 | 1 Preset Speed 7 (P577 [Preset Speed 7])                                         |

Refer to Speed Reference on page 251 for more details.

## DI HOA Start

This digital input function provides Hand-Off-Auto control. It functions like a three-wire start signal; with the exception, that it does not require the DI Stop to be high for a full input cycle before the drive looks for a rising edge on DI HOA Start. Use this feature by configuring P176 [DI HOA Start].

## DI MOP Inc, DI MOP Dec

These digital input functions are used to increment and decrement the Motor Operated Potentiometer (MOP) value inside the drive. The MOP is a reference value that can be incremented and decremented by external devices. The MOP value has a configurable preload that is retained through a power cycle. For the drive to use the MOP value as the current speed reference, either P545 [Speed Ref A Sel], P550 [Speed Ref B Sel], or P563 [DI ManRef Sel] must be set to P558 [MOP Reference].

## DI Accel 2, DI Decel 2

These digital input functions toggle between primary and secondary ramp rates. For example, with a digital input programmed to P179 [DI Accel 2], an open digital input follows P535 [Accel Time 1]. A closed digital input follows P536 [Accel Time 2].

## DI SpTqPs Sel 0 and 1

These digital input functions provide the ability to switch between different Speed/Torque/Position modes, (P309 [SpdTrqPsn Mode A], P310 [SpdTrqPsn Mode B], P311 [SpdTrqPsn Mode C], and P312 [SpdTrqPsn Mode D]) from digital input combinations. See Speed Torque Position on page 266 for a complete description of these modes and the digital input combinations that activate each mode.

## DI Stop Mode B

This digital input function selects between two different drive Stop modes. If the input is open, then P370 [Stop Mode A] selects which Stop mode to use. If the input is closed, then P371 [Stop Mode B] selects which Stop mode to use. If this input function is not configured, then P370 [Stop Mode A] always selects which Stop mode to use. See also Stop Modes on page 96 for more details.

## DI BusReg Mode B

This digital input function selects how the drive regulates excess voltage on the DC bus. If the input is open, then P372 [Bus Reg Mode A] selects which bus regulation mode to use. If the input is closed, then P373 [Bus Reg Mode B] selects which bus regulation mode to use. If this input function is not configured, then P372 [Bus Reg Mode A] always selects which bus regulation mode to use. See also Bus Regulation on page 41 for more details.

## DI PwrLoss ModeB

This digital input function selects between two different drive power loss modes. If the input is open, P450 [Pwr Loss Mode A] dictates the drive's action during the Power Loss mode. If the input is closed, P371 [Stop Mode B] dictates the drive's action during the power loss. If this input function is not configured, P450 [Power Loss Mode A] always dictates the drive's action during the power loss. See also Power Loss on page 72 for more details.

## DI Pwr Loss

The drive contains a sophisticated algorithm to manage initial application of power as well as recovery from a partial power loss event. This digital input function is used to force the drive into a power loss condition. If this input is open, the drive's internal algorithm dictates the power loss condition. If the input is closed, the algorithm is overridden and the drive is externally forced into a power lost condition. P449 [Power Loss Actn] configures the drive's response to a power loss time out condition and P452 [Pwr Loss A Time] or P455 [Pwr Loss B Time] set the time that the drive remains in Power Loss mode before a fault occurs. See also Power Loss on page 72 for more details.

## DI Precharge

This digital input function is used to manage disconnection from a common DC bus. If the input is closed, this indicates that the drive is connected to common DC bus and normal precharge handling can occur, and that the drive can run (start permissive). If the physical input is open, this indicates that the drive is disconnected from the common DC bus, and the drive enters the precharge state and initiates a coast stop immediately to prepare for reconnection to the bus. If this input function is not configured, then the drive assumes that it is always connected to the DC bus, and no special precharge handling is done.

## DI Prchrg Seal

This digital input function is used to force a unique fault when an external precharge circuit opens. P323 [Prchrg Err Cfg] dictates the action taken when an external precharge circuit has opened.

## DI PID Enable

If this digital input function is closed, the operation of the Process PID loop is enabled. If this input function is open, the operation of the Process PID loop is disabled.

## DI PID Hold

If this input function is closed, the integrator for the Process PID loop is held at the current value. If this input function is open, the integrator for the Process PID loop is allowed to increase.

## DI PID Reset

If this input function is closed, the integrator for the Process PI loop is reset to 0. If this input function is open, the integrator for the Process PI loop integrates normally.

## DI PID Invert

If this input function is closed, the PI Error is inverted. If this input function is open, the PI Error is not inverted.

## DI Torque StptA

This digital input function is used to force P676 [Trq Ref A Stpt] as the source for Torque Reference A, regardless of the setting in P675 [Trq Ref A Sel]. Used when the drive is in a mode that is commanding torque. Refer to P309 [SpdTrqPsn Mode A], P310 [SpdTrqPsn Mode B], P311 [SpdTrqPsn Mode C], and P312 [SpdTrqPsn Mode D].

## DI Fwd End Limit, DI Rev End Limit

These digital input functions are used to trigger a Forward End Limit and/or a Reverse End Limit. The resulting action depends on whether the drive is operating as a speed, torque or position regulator. The mode of operation is indicated by P935 [Drive Status 1] Bit 21 "Speed Mode," Bit 22 "PositionMode," and Bit 23 "Torque Mode." When the drive is operating as a speed regulator, the resulting action is to execute a "Fast Stop" command. After the drive stops in this case, it only restarts in the opposite direction (if given a new start command). This function is usually used with a limit switch near the point where the drive needs to stop. When the drive is operating as a torque regulator, the resulting action is to execute a "Fast Stop" command. After the drive stops in this case, it restarts and continues operation (if given a new start command). When the drive is operating as a position regulator, the resulting action is to execute a "Fast Stop" command. After the drive stops in this case, it restarts and continues to move towards the position reference (if given a new start command).

## DI Fwd Dec Limit, DI Rev Dec Limit

These digital input functions are used to trigger a Forward Decel Limit and/or a Reverse Decel Limit. The resulting action depends on whether the drive is operating as a speed, torque or position regulator. The mode of operation is indicated by P935 [Drive Status 1] Bit 21 "Speed Mode," Bit 22 "PositionMode" and Bit 23 "Torque Mode." When the drive is operating as a speed regulator, the resulting action is to override the speed reference and decelerate to Preset Speed 1. This function is usually used with a limit switch and initiates the slowing down process prior to encountering the End Limit. When the drive is operating as a torque regulator, the drive ignores this signal and continues operating at its torque reference. When the drive is operating as a position regulator, the drive ignores this signal and continues moving towards its position reference.

## DI PHdwr OvrTrvl, DI NHdwr OvrTrvl

These digital input functions are used to trigger a Positive Hardware Over-travel and/or a Negative Hardware Over-travel. The resulting action is to immediately fault and produce zero torque. After the drive is stopped, the condition needs to be cleared and the fault needs to be reset. The drive restarts (if given a new start command), and continues operation. It follows any speed reference, position reference, or torque reference. The drive's direction is not modified or limited after the restart. This function is usually used with a limit switch in a position beyond the "End Limit," as an extra safety limit to prevent torque from damaging the machine in an over-travel situation.

## Status

For the PowerFlex 753 main control board Digital Inputs (Di) 0, 1, and 2, P220 [Digital In Sts] Bits 0, 1 and 2 represents its respective inputs status. For the PowerFlex 755 main control board Digital Inputs (Di) 0, P220 [Digital In Sts] Bit 0 represents its respective digital input status. For the PowerFlex 750-Series Option Module Digital Inputs (Di) 0, 1, 2, 3, 4, and 5, P1 [Dig In Sts] Bits 0, 1, 2, 3, 4, and 5 represents its respective digital input status. When the bit associated with the digital input is on, depicted by a 1, this means that the drive recognizes that the digital input is on. When the bit associated with the digital input is off, represented by a 0, this means that the drive recognizes that the digital input is off.

## Configuration Conflicts

If you configure the digital inputs so that one or more selections conflict with each other, one of the digital input configuration alarms is asserted. As long as the Digital Input Conflict exists, the drive will not start. These alarms are automatically cleared by the drive as soon as the parameters are changed to remove the conflicts. These are examples of configurations that cause an alarm:

- Configuring both the "Start" input function and the "Run Forward" input function at the same time. "Start" is used only in "3-wire" Start mode, and "Run Forward" is used only in "2-wire" Run mode, therefore, do not configured at the same time.
- Configuring the same toggle input function (for instance "Fwd Reverse") to more than one physical digital input simultaneously.

These alarms, called Type 2 Alarms, are different from other alarms in that it is not possible to start the drive while the alarm is active. It is possible for any of these alarms to occur while the drive is running, because all digital input configuration parameters can be changed only while the drive is stopped. Whenever one or more of these alarms is present, the drive ready status becomes "not ready" and the HIM displays a conflict message. In addition, the drive status light flashes yellow. Refer to the PowerFlex 750-Series Programming Manual, publication 750-PM001, for a complete list of Type 2 Alarms.

## DigIn Cfg B

Digital input conflict. Input functions that cannot exist at the same time have been selected. Correct Digital Input configuration.

## DigIn Cfg C

Digital input conflict. Input functions that cannot be assigned to the same digital input have been selected. Correct Digital Input configuration.

## Block Diagrams

Figure 8 - PowerFlex 753

<!-- image -->

Figure 9 - PowerFlex 755

<!-- image -->

Figure 10 - PowerFlex 750-Series Option Module

<!-- image -->

## Digital Outputs

The PowerFlex 753 has one transistor output and one relay output embedded on its main control board.

The transistor output is on TB1 at the lower front of the main control board.

| Terminal Name Description                | Rating                                          |
|------------------------------------------|-------------------------------------------------|
| T0 Transistor Output 0 Transistor Output | 48V DC, 250 mA maximum load. Open drain output. |

The relay output is on TB2 at the bottom of the main control board.

| Terminal Name Description                                                      | Rating                                  |
|--------------------------------------------------------------------------------|-----------------------------------------|
| R0NC Relay 0 N.C. Output Relay 0 normally closed contact                       | 240V AC, 24V DC, 2A max Resistive Only  |
| R0C Relay 0 Common Output Relay 0 Common                                       |                                         |
| R0NO Relay 0 N.O. Output Relay 0 normally open contact 240V AC, 24V DC, 2A max | General Purpose (Inductive) / Resistive |

Refer to the PowerFlex 750-Series AC Drives Installation Instructions, publication 750-IN001, for PowerFlex 753 Main Control Board I/O wiring examples.

The PowerFlex 755 has no outputs embedded on its Main Control Board.

There are PowerFlex 750-Series Option Modules that expand the amount of digital outputs that can be used in both the PowerFlex 753 and 755 drives.

Catalog numbers 20-750-2262C-2R and 20-750-2262D-2R provide two relay outputs on TB2 at the front of option module.

| Terminal Name Description                                                      | Rating                                  |
|--------------------------------------------------------------------------------|-----------------------------------------|
| R0NC Relay 0 N.C. Output Relay 0 normally closed contact                       | 240V AC, 24V DC, 2A max Resistive Only  |
| R0C Relay 0 Common Output Relay 0 common                                       | 240V AC, 24V DC, 2A max Resistive Only  |
| R0NO Relay 0 N.O. Output Relay 0 normally open contact 240V AC, 24V DC, 2A max | General Purpose (Inductive) / Resistive |
| R1NC Relay 1 N.C. Output Relay 1 normally closed contact                       | 240V AC, 24V DC, 2A max Resistive Only  |
| R1C Relay 1 Common Relay 1 common                                              | 240V AC, 24V DC, 2A max Resistive Only  |
| R1NO Relay 1 N.C. Output Relay 1 normally open contact 240V AC, 24V DC, 2A max | General Purpose (Inductive) / Resistive |

Catalog number 20-750-2263C-1R2T provides one transistor output and two relay outputs on TB2 at the front of option module.

|                                          | Terminal Name Description                                                      | Rating                                                          |
|------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------|
|                                          | R0NC Relay 0 N.C. Output Relay 0 normally closed contact                       | 240V AC, 24V DC, 2A max Resistive Only                          |
| R0C Relay 0 Common Output                | Relay 0 common                                                                 | 240V AC, 24V DC, 2A max Resistive Only                          |
|                                          | R0NO Relay 0 N.O. Output Relay 0 normally open contact 240V AC, 24V DC, 2A max | General Purpose (Inductive) / Resistive                         |
| T0 Transistor Output 0 Transistor Output |                                                                                | 24VDC = 1A max 24VDC = 0.4 Max for U.L. applications. Resistive |
| TC Transistor Output Common              | Transistor Output Common                                                       | 24VDC = 1A max 24VDC = 0.4 Max for U.L. applications. Resistive |
| T1 Transistor Output 1 Transistor Output |                                                                                | 24VDC = 1A max 24VDC = 0.4 Max for U.L. applications. Resistive |

Refer to the PowerFlex 750-Series AC Drives Installation Instructions, publication 750-IN001, for PowerFlex 750-Series Option Module I/O wiring examples.

## Configuration

Each digital output can be programmed to change state based on one of many different conditions. These conditions can fall into different categories.

- Drive status conditions (fault, alarm, and reverse).
- Level conditions (DC bus voltage, current, and frequency)
- Controlled by a digital input.
- Controlled by the network.
- Controlled by DeviceLogix software.

## Drive Status Conditions

For PowerFlex 750-Series drives utilizing an option module, the table below shows an overview of the selectable configurations for the drive's digital output Sel parameters.

| Parameter No. Parameter Name Description   |                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 220(1)                                     | Digital In Sts Status of the digital inputs resident on the main control board (Port 0).                                                                     |
| 227(1)                                     | Dig Out Setpoint Controls Relay or Transistor Outputs when chosen as the source. Can be used to control outputs from a communication device using DataLinks. |
| 233(1)                                     | RO0 Level CmpSts Status of the level compare, and a possible source for a relay or transistor output.                                                        |
|                                            | 720 PTP PsnRefStatus Displays the current operating status of the Point-To-Point Position Planner in the Position Referencing.                               |
| 724                                        | Psn Reg Status Indicates status of position control logic.                                                                                                   |
| 730                                        | Homing Status Indicates status of position control logic.                                                                                                    |
| 933                                        | Start Inhibits Indicates which condition is preventing the drive from starting or running.                                                                   |
| 935                                        | Drive Status 1 Present operating condition of the drive.                                                                                                     |
| 936                                        | Drive Status 2 Present operating condition of the drive.                                                                                                     |
| 937                                        | Condition Sts 1 Status of conditions that can result in the drive taking action (faulting), based on configuration of protective functions.                  |
| 945                                        | At Limit Status Status of dynamic conditions within the drive that are either active or a limit is being applied.                                            |
| 952                                        | Fault Status A Indicates the occurrence of conditions that have been configured as faults. These conditions are from P937 [Condition Sts 1].                 |
| 953                                        | Fault Status B Indicates the occurrence of conditions that have been configured as faults.                                                                   |
| 959                                        | Alarm Status A Indicates the occurrence of conditions that have been configured as alarms. These events are from P937 [Condition Sts 1].                     |
| 960                                        | Alarm Status B Indicates the occurrence of conditions that have been configured as alarms.                                                                   |
| 961                                        | Type 2 Alarms Indicates the occurrence of conditions that have been configured as alarms.                                                                    |
| 1089                                       | PID Status Status of the Process PI regulator.                                                                                                               |
| 1103(2)                                    | Trq Prove Status Displays the status bits for TorqProve.                                                                                                     |
| 1210(2)                                    | Profile Status Indicates status of speed profile/position indexer control logic.                                                                             |
| 1 (3)(4)                                            | Dig In Sts Status of the digital inputs.                                                                                                                     |
| 7 (3)(4)                                            | Dig Out Setpoint Controls Relay or Transistor Outputs when chosen as the source. Can be used to control outputs from a communication device using DataLinks. |
| 13(3)(4)                                   | RO0 Level CmpSts Status of the level compare, and a possible source for a relay or transistor output.                                                        |
| 50(5)                                      | DLX DigOut Sts Provides the individual on/off status of the DLX Logic Command word bits.                                                                     |
| 51(5)                                      | DLX DigOut Sts2 Provides the individual on/off status of the 16 DLX DOPs.                                                                                    |

Refer the PowerFlex 750-Series Programming Manual, publication 750-PM001 , for specific parameter bit level details.

Related PowerFlex 753 selection parameter information is noted below.

|   Parameter No. Parameter Name Description |                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------|
|                                        230 | RO0 Sel Selects the source that energizes the relay output.               |
|                                        240 | TO0 Sel Selects the source that energizes the relay or transistor output. |

Depending on the PowerFlex 750-Series Option Module or Modules installed in the drive, related selection parameter information is noted below.

|   Parameter No. Parameter Name Description |                                                                                      |
|--------------------------------------------|--------------------------------------------------------------------------------------|
|                                         10 | RO0 Sel Selects the source that energizes the relay output.                          |
|                                         20 | RO1 Sel or TO0 Sel Selects the source that energizes the relay or transistor output. |
|                                         30 | TO1 Sel Selects the source that energizes the transistor output.                     |

## Example

Below is an example of a PowerFlex 753 drive's utilizing an embedded digital output Sel parameter being configured such that the output energizes when a fault is present on the drive.

<!-- image -->

## Example

For parameters that are not configurable through the parameter properties' "Value" tab pull-down graphic user interface (GUI), you can utilize the "Numeric Edit" tab to alternatively configure the digital output for a desired function.

Below is an example of a PowerFlex 755 drive utilizing a PowerFlex 750-Series option module's digital output "Sel" parameter being configured such that the output energizes when an alarm is present on one of the drive's inverter section.

You can see below that you cannot select Port 10, Inverter section in the Value tab pull-down GUI.

<!-- image -->

We look through the Port 10, Inverter section parameters and find that P13 [Alarm Status] Bit 0 shows if there is an active alarm on Inverter 1 section.

<!-- image -->

Within the Numeric Edit tab we can configure the digital output for the desired function. See below.

<!-- image -->

For Help, press F1

Once the parameter is configured within the Numeric Edit tab, you can Click OK, or you can go back to the Value tab to see what populates in the pull-down GUI, then Click OK.

<!-- image -->

## Level Conditions

A desired level function needs to be programmed into the "Level Sel" parameter, depending on the output being used. If the value for the specified function (frequency, current, and so forth) is greater than equal to or less than the programmed limit dictated by the "Level" parameter, the output activates or deactivates depending on how the "Sel" parameter is configured.

Notice that the Level Select parameters do not have units. The drive assumes the units and the minimum/maximum values from the selected parameter function. For example, if the "Level Sel" is programmed for P943 [Drive Temp Pct], which indicates operating temperature of the drive power section (heat sink), its units are in percentage of the maximum heat sink temperature with minimum/ maximum values of -200/200 percent.

For the PowerFlex 750-Series drives utilizing an Option Module, the table below shows an overview of the selectable configurations for the drive's Digital Output "Level Sel" parameters.

| Parameter No. Parameter Name Description   |                                                                                                                                           |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|                                            | 1 Output Frequency Output frequency present at terminals T1, T2, and T3 (U, V & W).                                                       |
| 2  Commanded                               | Value of the active Speed/Frequency Reference.                                                                                            |
| 3                                          | Mtr Vel Fdbk Estimated or actual motor speed, with feedback.                                                                              |
| 4                                          | Commanded Trq Final torque reference value after limits and filtering are applied. Percent of motor rated                                 |
| 5                                          | Torque Cur Fdbk Based on the motor, the amount of current that is in phase with the fundamental voltage component.                        |
| 6                                          | Flux Cur Fdbk Amount of current that is out of phase with the fundamental voltage component.                                              |
| 7                                          | Output Current The total output current present at terminals T1, T2, and T3 (U, V & W).                                                   |
| 8                                          | Output Voltage Output voltage present at terminals T1, T2, and T3 (U, V & W).                                                             |
| 9                                          | Output Power Output power present at terminals T1, T2, and T3 (U, V & W).                                                                 |
| 10                                         | Output Powr Fctr Output power factor.                                                                                                     |
| 11                                         | DC Bus Volts DC bus voltage.                                                                                                              |
| 13                                         | Elapsed MWH Accumulated output energy of the drive.                                                                                       |
| 14                                         | Elapsed kWH Accumulated output energy of the drive.                                                                                       |
| 260(1)                                     | Anlg In0 Value Value of the Analog input after filter, square root, and loss action.                                                      |
| 418                                        | Mtr OL Counts Accumulated percentage of motor overload.                                                                                   |
| 419                                        | Mtr OL Trip Time Displays the inverse of the motor overload time.                                                                         |
| 558                                        | MOP Reference Value of the MOP (Motor Operated Potentiometer) Reference to be used as a possible source for P545 and P550.                |
| 707                                        | Load Estimate Displays an estimated load torque value for the drive.                                                                      |
| 940                                        | Drive OL Count Indicates power unit overload (IT) in percentage.                                                                          |
| 943                                        | Drive Temp Pct Indicates operating temperature of the drive power section (heat sink) in percentage of the maximum heat sink temperature. |
| 1090                                       | PID Ref Meter Present value of the PI reference signal.                                                                                   |
| 1091                                       | PID Fdbk Meter Present value of the PI feedback signal.                                                                                   |
| 1092                                       | PID Error Meter Present value of the PI error.                                                                                            |
| 1093                                       | PID Output Meter Present value of the PI output.                                                                                          |
| 1567(2)                                    | FrctnComp Out Displays the torque reference output of the Friction Compensation function.                                                 |
| 50(3)(4)                                   | Anlg In0 Value Value of the Analog input after filter, square root, and loss action.                                                      |
| 60(3)(4)                                   | Anlg In1 Value Value of the Analog input after filter, square root, and loss action.                                                      |
| 90 … 97(5) DLX Real Out SP1 -              | Eight 32-bit Real scratchpad registers for DLX program output use.                                                                        |

## Related PowerFlex 753 drives Level Select parameter information noted below.

|   Parameter No. Parameter Name Description |                                                                                                       |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------|
|                                        230 | RO0 Sel Selects the source that energizes the relay output.                                           |
|                                        231 | RO0 Level Sel Selects the source of the level that is compared.                                       |
|                                        232 | RO0 Level Sets the level compare value.                                                               |
|                                        233 | RO0 Level CmpSts Status of the level compare, and a possible source for a relay or transistor output. |
|                                        240 | TO0 Sel Selects the source that energizes the relay or transistor output.                             |
|                                        241 | TO0 Level Sel Selects the source of the level that is compared.                                       |
|                                        242 | TO0 Level Sets the level compare value.                                                               |
|                                        243 | TO0 Level CmpSts Status of the level compare, and a possible source for the transistor output.        |

Depending on the PowerFlex 750-Series Option Module(s) installed in the drive, related Level Select parameter information noted below.

|    | Parameter No. Parameter Name Description   |                                                                                                       |
|----|--------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 10 |                                            | RO0 Sel Selects the source that energizes the relay output.                                           |
| 11 |                                            | RO0 Level Sel Selects the source of the level that is compared.                                       |
| 12 |                                            | RO0 Level Sets the level compare value.                                                               |
| 13 |                                            | RO0 Level CmpSts Status of the level compare, and a possible source for a relay or transistor output. |
| 20 |                                            | RO1 Sel or TO0 Sel Selects the source that energizes the relay or transistor output.                  |
| 21 | RO1 Level Sel or TO0 Level Sel             | Selects the source of the level that is compared.                                                     |
| 22 | RO1 Level or TO0 Level                     | Sets the level compare value.                                                                         |
| 23 | RO1 Level CmpSts or TO0 Level CmpSts       | Status of the level compare, and a possible source for a relay or transistor output.                  |
| 30 |                                            | TO1 Sel Selects the source that energizes the transistor output.                                      |
| 31 |                                            | TO1 Level Sel Selects the source of the level that is compared.                                       |
| 32 |                                            | TO1 Level Sets the level compare value.                                                               |

## Example

Below is an example of a PowerFlex 753 drive utilizing an embedded digital output Select, Level Select and Level parameters being configured such that the output energizes when the drive's operating temperature of the drive power section (heat sink) in percentage of the maximum heat sink temperature is greater than 50 percent.

<!-- image -->

## Controlled By Digital Input

A digital output can be programmed to be controlled by a digital input. For example, when the input is closed, the output is energized, and when the input is open, the output is de-energized. Note that the output is controlled by the state of the input, even if the input has been assigned a normal drive function (Start, Jog, and so forth).

## Example

In this example, the drive is utilizing a 24V DC, Two Relay Option Module in Port 7. One of the drive's digital input functions, P164 [DI Run Forward] is programmed for Port 7: Digital In Sts.Input 1, with Option Module P10 [RO0 Sel] is programmed for Port 7: Dig In Sts.Input 1 and P20 [RO1 Sel] is programmed for Port 7: Dig In Sts.Input 3.

<!-- image -->

<!-- image -->

As you can see with the picture above, when the Digital Inputs 1 (pink highlight) and 3 (yellow highlight) are true (on) their respective Digital Outputs are true (on) as well.

## Controlled by Network

This configuration is used when it is desired to control the digital outputs over network communication instead of a drive related function. In the case for the PowerFlex 753 embedded digital outputs, P227 [Dig Out Setpoint] is utilized and in the case for the PowerFlex 750-Series Option Module, P7 [Dig Out Setpoint] is utilized. To complete the configuration for control over a network, a datalink must be configured for the respective Digital Output Setpoint parameter.

Related PowerFlex 753 Setpoint parameter information noted below.

<!-- image -->

| File Group   | No. Display Name                                                                                                                                    |                                                                                                                                        |                                         |                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|-------------------------------------------|
|              | Full Name Description                                                                                                                               |                                                                                                                                        |                                         |                                           |
|              | 227  753                                                                                                                                            | Dig Out Setpoint                                                                                                                       |                                         |                                           |
|              | Digital Output Setpoint                                                                                                                             |                                                                                                                                        |                                         |                                           |
|              | Controls Relay or Transistor Outputs when chosen as the source. Can be used to control outputs from a communication device using DataLinks. Options | ReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedTrans Out 0Relay Out 0 |                                         |                                           |
| FEEDBACK & I/O Digital Outputs              |                                                                                                                                                     |                                                                                                                                        |                                         |                                           |
|              |                                                                                                                                                     |                                                                                                                                        |                                         | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |
|              |                                                                                                                                                     |                                                                                                                                        | Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |                                           |

Depending on the PowerFlex 750-Series Option Module(s) installed in the drive, related Setpoint parameter information noted below.

<!-- image -->

|                 | Values                                                                                                                                      | No. Display Name Full Name                                        |                                                                                                                     |                 | Read-WriteData Type   |             |                                                                |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------|-----------------------|-------------|----------------------------------------------------------------|
|                 |                                                                                                                                             | File Group Description 7 Dig Out Setpoint Digital Output Setpoint |                                                                                                                     |                 |                       |             |                                                                |
| I/O             |                                                                                                                                             |                                                                   |                                                                                                                     |                 |                       |             |                                                                |
|                 | Controls Relay or Transistor Outputs when chosen as the source. Can be used to control outputs from a communication device using DataLinks. | Options                                                           | ReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedTrans Out 1 | Trans Out 0 (1) | (2)                   | Relay Out 0 |                                                                |
| Digital Outputs | Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0                                                                                                     |                                                                   |                                                                                                                     |                 |                       |             | 0 = Output De-energized                                        |
|                 |                                                                                                                                             |                                                                   |                                                                                                                     |                 |                       |             | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 1 = Output Energized |
|                 | (1) Bit 1 = “Trans Out 0” for I/O Module model 20-750-2263C-1R2T = “Relay Out 1” for I/O Module models 20-750-2262C-2R and 20-750-2262D-2R  |                                                                   |                                                                                                                     |                 |                       |             |                                                                |

## Example

For this example, our setup includes a PowerFlex 755 utilizing a 20-750-2262C2R 24VDC I/O Option Module and a ControlLogix™ L63 processor. The drive's Option Module, P10 [RO0 Sel] is configured for Port 7: Dig Out Setpoint.Relay Out 0. We are utilizing the Logix Designer application, which includes the Drives Add-On Profiles (AOPs). This gives us the ability to communicate and control the PowerFlex 755 drive over its embedded ethernet port via a datalink P7 [Dig Out Setpoint], Relay Out 0.

Below is a picture of the PowerFlex 755 drive Datalink configuration.

<!-- image -->

Below is a picture of the PowerFlex 755 drive Datalink configuration from DriveExecutive™.&lt;span id="fck\_dom\_range\_temp\_1332343477042\_759" /&gt;

<!-- image -->

Utilizing the Drive Add-On Profiles and a datalink, we can use the created descriptive controller tag (highlighted below) to communicate over a network to control the relay output.

<!-- image -->

The picture below shows the result of controlling the digital output over the network (yellow highlight).

<!-- image -->

## Controlled by DeviceLogix software

DeviceLogix software control technology provides you with the flexibility to customize a drive to more closely match your application needs. DeviceLogix software controls outputs and manages status information locally within the drive allowing you to operate the drive independently or complimentary to supervisory control helping to improve system performance and productivity. You can use the PowerFlex 750-Series DeviceLogix software to read inputs/write outputs and exclusively control the drive.

## Example

In the example below, we are using two real world inputs, such as limit switches being wired into a PowerFlex 750-Series Option Module, and using a DeviceLogix software program to control a digital output.

The picture below shows the DeviceLogix software Digital Input configuration. P33 [DLX DIP 1] is configured for Port 7: Dig In Sts.Input 1 and P35 [DLX DIP 3] is configured for Port 7: Dig In Sts.Input 3. This setup lets us bring in two real world inputs into DeviceLogix software.

<!-- image -->

We then utilize a DeviceLogix software program so that when both Digital Input 1 and Digital Input 3 are true (on), the resultant is the DeviceLogix software Digital Output 1 (DOP 1) turns on.

<!-- image -->

The picture below shows that the Option Module, P10 [RO0 Sel] is configured for DeviceLogix software Port 14: DLX DigOut Sts2.DLX DOPSts1. This links together the DeviceLogix software Digital Output 1 (DOP 1) to the drive's physical output, such that when the DOP 1 is high (on), the drive's Option Module relay output energizes.

<!-- image -->

The picture below shows the status of the DeviceLogix software inputs and outputs via P49 [DLX DigIn Sts] and P51 [DLX DigOut Sts2].

<!-- image -->

The picture below shows the status of the DeviceLogix software inputs and outputs via P1 [Dig In Sts] and P5 [Dig Out Sts].

<!-- image -->

## Invert

There is a logical invert function associated with the PowerFlex 750-Series drive's digital outputs. For the PowerFlex 753, it is configured by P226 [Dig Out Invert], and for the PowerFlex 750-Series Option Module, it is configured by P6 [Dig Out Invert]. This invert function changes the output status bit from a zero, false state, to a one, true state, and vice versa.

This logical invert function requires power to be applied to the drive's control module for the drive's logic to be active. This can be obtained from powering up the drive's control module by either applying power to the drive's input section or from an external 24VDC being wired into the Auxiliary Power Supply Option Module.

PowerFlex 753 Invert parameter information noted below.

<!-- image -->

| File Group   | No. Display Name                     |                |                                           | Values                                                                                                                                 | Read-WriteData Type   |           |                    |
|--------------|--------------------------------------|----------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------|--------------------|
|              | Full Name Description                |                |                                           |                                                                                                                                        |                       |           |                    |
|              | 226  753                             | Dig Out Invert |                                           |                                                                                                                                        | Integer               | RO 16-bit |                    |
|              | Digital Output Invert                |                |                                           |                                                                                                                                        |                       |           |                    |
|              | Inverts the selected digital output. |                |                                           |                                                                                                                                        |                       |           |                    |
| FEEDBACK & I/O Digital Outputs              | Options                              |                |                                           | ReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedTrans Out 0Relay Out 0 |                       |           |                    |
|              |                                      |                |                                           | Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 = Condition False                                                                            |                       |           |                    |
|              |                                      |                |                                           |                                                                                                                                        |                       |           | 1 = Condition True |
|              |                                      |                | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |                                                                                                                                        |                       |           |                    |

Depending on the PowerFlex 750-Series Option Module(s) installed, Invert parameter information noted below.

<!-- image -->

## Example

In this example, the drive is utilizing a 24VDC, two relay Option Module in Port 7 with P10 [RO0 Sel] is programmed for Port 7: Dig In Sts.Input 1. Notice below when the Invert bit for Relay Out 0, when the input status is true (1), the digital output status bit is false (0).

<!-- image -->

## On/Off Time

Each digital output has two user-controlled timers associated with it. The On timer defines the delay time between a False-to-True transition (condition appears) on the output condition and the corresponding change in state of the digital output. The Off timer defines the delay time between a True-to-False transition (condition disappears) on the output condition and the corresponding change in the state of the digital output. Either timer can be disabled by setting the corresponding delay time to zero.

PowerFlex 753 On/Off parameters noted below.

| Parameter No. Parameter Name Description   |                                                                                                                                                                         |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                            | 234 RO0 On Time Sets the “ON Delay” time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay.                   |
| 235                                        | RO0 Off Time Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the relay.               |
| 244                                        | TO0 On Time Sets the “ON Delay” time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay or transistor.         |
| 245                                        | TO0 Off Time Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the relay or transistor. |

Depending on the PowerFlex 750-Series Option Module(s) installed, On/Off parameters noted below.

|    | Parameter No. Parameter Name Description   |                                                                                                                                                                |
|----|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 14 |                                            | RO0 On Time Sets the “ON Delay” time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay.              |
| 15 |                                            | RO0 Off Time Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the relay.      |
| 24 | RO1 On Time or TO0 On Time                 | Sets the “ON Delay” time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay or transistor.            |
| 25 | RO1 Off Time or TO0 Off Time               | Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the relay or transistor.     |
| 34 |                                            | TO1 On Time Sets the “ON Delay” time for the digital outputs. This is the time between the occurrence of a condition and activation of the transistor.         |
| 35 |                                            | TO1 Off Time Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the transistor. |

Whether a particular type of transition (False-to-True or True-to-False) on an output condition results in an energized or de-energized output depends on the output condition. If a transition on an output condition occurs and starts a timer, and the output condition goes back to its original state before the timer runs out, then the timer is aborted and the corresponding digital output does not change state.

## Example

For example, in the diagram below, a digital output is configured for P935 [Drive Status 1], Bit 27 "Cur Limit," the On Time is programmed for two seconds and the Off Time is programmed for 0 seconds.

<!-- image -->

## Status

The [Dig Out Sts] parameter displays the status of the digital outputs and can be used for troubleshooting the digital outputs. When the bit in associated with the digital output is on, this means that the logic in the drive is telling that digital output to turn on. When the bit associated with the digital input is off, this means that the logic in the drive is telling that digital output to turn off.

PowerFlex 753 related Status parameter information noted below.

<!-- image -->

| File   |     | No. Display Name                        |                       |                                                                                                                                        | Values                |                                        | Read-WriteData Type   |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
|--------|-----|-----------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|        |     | Full Name Description                   |                       |                                                                                                                                        |                       |                                        |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
| FEEDBACK & I/O Digital Outputs        | 225 | 753                                     | Dig Out Sts           |                                                                                                                                        |                       |                                        | RO 16-bit             |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
| FEEDBACK & I/O Digital Outputs        | 225 | Digital Output Status                   | Digital Output Status | Digital Output Status                                                                                                                  | Digital Output Status | Digital Output Status                  | Integer               | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status | Digital Output Status |
| FEEDBACK & I/O Digital Outputs        | 225 | Status of the digital outputs.          |                       |                                                                                                                                        |                       |                                        |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
| FEEDBACK & I/O Digital Outputs        | 225 | Options                                 |                       | ReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedReservedTrans Out 0Relay Out 0 |                       | 0 = Condition False 1 = Condition True |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
| FEEDBACK & I/O Digital Outputs        | 225 | Default 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |                       |                                                                                                                                        |                       | 0 = Condition False 1 = Condition True |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |
| FEEDBACK & I/O Digital Outputs        | 225 |                                         |                       | Bit 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                              |                       | 0 = Condition False 1 = Condition True |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |                       |

<!-- image -->

## Block Diagrams

Figure 11 - PowerFlex 753 Drive

<!-- image -->

Figure 12 - PowerFlex 750-Series Option Module

<!-- image -->

## PTC Motor Thermistor Input

A PTC (Positive Temperature Coefficient) sensing device, also known as a motor thermistor, embedded in the motor windings can be monitored by the drive for motor thermal protection. The motor windings are typically equipped with three PTC sensors (one per phase) wired in series as shown in schematic below. The miniaturized sensors have a low resistance below the rated response temperature, and increase their resistance (exponentially) in the rated response temperatures range. The rated response temperature is defined by the PTC sensor. Motors with different thermal insulation classes (Class F or H) are equipped with different PTC sensors, each with its own response temperature such as 120, 130, and 140 Degrees C. Unlike the PT100 or KTY thermistors, which have a linear relation between temperature and resistance, the PTC thermistor is used for a temperature level indication rather than a direct measurement in degrees C.

Figure 13 - PTC characteristic temperature/resistance curve according to IEC-34-11-2

<!-- image -->

## Hardware and Connection

The PTC thermistor leads are connected to the PTC+ and PTC- terminals of either the PowerFlex 753 main control board TB1 or to TB1 of one of the optional I/O cards, catalog numbers 20-750-2262C-2R, 20-750-2263C-1R2T, 20-750-2262D-2R.

PTC thermistors of ATEX certified motors connect to the ATEX option module, 20-750-ATEX, which is mounted onto one of the 11-Series I/O cards, catalog numbers 20-750-1132C-2R, 20-750-1133C-1R2T, 20-750-1132D-2R.

Figure 14 - PTC Connection

<!-- image -->

## Configuration with PTC connected to PowerFlex 753 Main Control Board

Port 0: P250 [PTC Cfg] = 0 "Ignore," 1 "Alarm," 2 "Flt Minor," 3 "FltCoastStop," 4 "Flt RampStop," or 5 "Flt CL Stop"

Status is shown in Port 0: P251 [PTC Sts]

## Configuration with Optional I/O Board

Port X (I/O Module): P40 [PTC Cfg] = 0 "Ignore," 1 "Alarm," 2 "Flt Minor," 3 "Flt CoastStop," 4 "Flt RampStop," or 5 "Flt CL Stop"

Status is shown in Port X (I/O Module): P41 [PTC Sts] and Port X (I/O Module): P42 [PTC Raw Value]

## Configuration with 11-Series I/O module fitted with ATEX Option

Status is shown in Port X (I/O Module): P41 [ATEX Sts] The fault action is not configurable when the ATEX module is used.

## Fault or Alarm Operation

The reaction to an increased PTC resistance depends on the respective PTC configuration, such as alarm or fault. When the ATEX module is used, the result is always fault. When the PTC resistance exceeds 3.2 kOhm a fault or alarm is triggered. The function is reset when the resistance drops below 2.2 kOhm. A short circuit is detected when the resistance value drops below 100 Ohm. If the drive was configured to fault then the fault must be cleared once the PTC function is reset (value is below threshold).

## Alarms

## Diagnostics and Protection

| Topic                      |   Page |
|----------------------------|--------|
| Alarms                     |    155 |
| Current Limit              |    156 |
| DC Bus Voltage/Memory      |    158 |
| Drive Overload             |    158 |
| Faults                     |    162 |
| Input Phase Loss Detection |    166 |
| Motor Overload             |    168 |
| Overspeed Limit            |    172 |
| Password                   |    173 |
| Real Time Clock            |    174 |
| Reflected Wave             |    179 |
| Security                   |    185 |
| Shear Pin                  |    188 |
| Slip Compensation          |    192 |
| Slip Regulator             |    194 |

Alarms are indications of situations that are occurring within the drive or application that are annunciated to the user. These situations can affect the drive operation or application performance. Conditions such as power loss or analog input signal loss can be detected and displayed for drive or operator action.

There are two types of alarms.

- Type 1 Alarms are conditions that do not cause the drive to trip or shut down, but, if the condition persists, it can lead to a drive fault.
- Type 2 Alarms are conditions that are caused by improper programming and prevent the drive from starting until programming is corrected. An example of a Type 2 alarm is when a start function is assigned to a digital input without a stop function also assigned to a digital input.

The Troubleshooting section of the PowerFlex 750-Series Programming Manual, publication 750-PM001, contains a list of drive-specific faults and alarms, their type of fault or alarm, and what action can be configured if applicable.

<!-- image -->

## Current Limit

In a Control Logix program do not set P410 [Motor OL Actn] to 1 "Alarm." There is an anomaly in drives with firmware version 8.001 or earlier that prevents an overload from being asserted in P959 [Alarm Status A] and in P937 [Condition Sts 1] Bit 2 "Motor OL." Neither of these parameters are used under this circumstance to initiate any programmed alarm routine.

Leaving P410 [Motor OL Actn] at one of the fault settings or Flash Updating the drive to a firmware version greater than 8.001 resolves this anomaly. Instructions on Flash Updating drives are provided in drive firmware Release Notes publications.

There are five ways that the drive can protect itself from over current or overload situations.

| Method                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | Hardware Over Current This is a feature that instantly faults the drive if the output current exceeds this value. The value is fixed by hardware and is typically 250% of drive rated amps. The fault code for this feature is F12 “HW OverCurrent.” This feature cannot be defeated or mitigated.                                                                                                                                                                                                                           |
|                                  | Software Over Current This protection mode occurs when peak currents do not reach the hardware over current value and are sustained long enough and high enough to damage certain drive components. If this situation occurs, the drives protection scheme causes an F36 “SW OverCurrent” fault. The point at which this fault occurs is fixed and stored in drive memory.                                                                                                                                                   |
|                                  | Software Current Limit This is a feature that attempts to reduce current by folding back output voltage and frequency if the output current exceeds a programmable value. P422/423 [Current Limit 1/2], selected by P421 [Current Lmt Sel], are programmable up to 150% of drive rating. The reaction to exceeding this value is programmable with Shear Pin fault. Enabling this parameter creates an F61 or F62 “Shear Pin n” fault. Disabling this parameter causes the drive to use fold back to attempt load reduction. |
| Heat Sink Temperature Protection | The drive constantly monitors the heat sink temperature. If the temperature exceeds the drive maximum, a F8 “Heatsink OvrTemp” fault occurs. The value is fixed by hardware at a nominal value of 100 degrees C. This fault is generally not used for over current protection due to the thermal time constant of the heat sink. It is an overload protection.                                                                                                                                                               |
|                                  | Drive Overload Protection Refer to Drive Overload on page 158 .                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Figure 15 - Current Limit Frequency Fold-back Examples

<!-- image -->

## DC Bus Voltage/Memory

## Drive Overload

P11 [DC Bus Volts] is a measurement of the instantaneous value. P12 [DC Bus Memory] is a heavily filtered value or average bus voltage. Just after the precharge relay is closed during initial powerup, bus memory is set equal to bus voltage. Thereafter it is updated to the six-minute average of the instantaneous DC bus voltage.

Bus memory is used as a comparison value to sense a power loss condition. If the drive enters a power loss state, the bus memory is also used for recovery (for example pre-charge control or inertia ride through) upon return of the power source. Update of the bus memory is blocked during deceleration to prevent a false high value caused by a regenerative condition.

The purpose of the drive thermal overload feature is to protect the drive's power module when operation exceeds the design limitations. This feature does not protect the motor, this is handled by the motor overload protection feature (see Motor Overload on page 168).

The drive thermal overload function utilizes two methods to protect the drive. Inverse time protection based on the average output current and a thermal manager that models the temperature of the IGBTs based on measured power module temperature and operating conditions. Each method can reduce the PWM switching frequency or reduce current limit. When rated conditions are exceeded, even after applying one of the measures mentioned above, and the load on the drive is not reduced, a F64 "Drive Overload" fault is generated. The fault detection mechanism cannot be disabled. Only the ability to fold back PWM frequency and current limit can be disabled.

The drive monitors the temperature of the power module based on a measured temperature and a thermal model of the power module. As the temperature rises and P940 [Drive OL Count] increases, the drive can lower the PWM frequency to decrease the switching losses in the power module. If the temperature continues to rise, the drive can reduce current limit to try to decrease the load. This is the factory default response, configurable by P420 [Drive OL Mode], to increasing drive temperature. If the drive temperature becomes critical, P940 [Drive OL Count] = 100%, the drive faults.

If the drive is operated in a low ambient temperature condition the drive can exceed rated levels of current before the monitored temperature becomes critical. To guard against this situation the drive thermal overload also includes an inverse time algorithm. When this scheme detects operation beyond rated limits, current limit can be reduced or a fault can be generated.

## Inverse Time Protection

The following curves show an example of the boundary operations of a 20G1AxC770 drive. The curve is defined by the drive's continuous rating and the respective overload capacities. These are voltage class and duty rating dependant and are configurable by P305 [Voltage Class] and P306 [Duty Rating]. This particular example has six different overload ratings.

- Low Voltage/Normal Duty or High Voltage/Normal Duty
- Low Voltage/Heavy Duty or High Voltage/Heavy Duty
- Low Voltage/Light Duty or High Voltage/Light Duty Light Duty is only available to frame 8 and larger drives.

If the load on the drive exceeds the level of current as shown on one of the curves, the inverse time protection increments the overload counter. Current limit can fold back to 100% of the drive rating when the drive over load count reaches 97.35% until the 10/90 or 5/95 duty cycle has been achieved. For example, 60 seconds at 110% is followed by 9 minutes at 100%, and 3 seconds at 150% is followed by 57 seconds at 100%. With the threshold for where to take action slightly above the rated level the drive only folds back when drive ratings are exceeded. If fold back of current limit is not enabled in P940 [Drive OL Mode], an F64 "Drive Overload" fault occurs when operation exceeds the rated levels.

<!-- image -->

## Normal Duty and Heavy Duty Operation

Applications require different amounts of overload current. Sizing a drive for Normal Duty provides 110% for 60 seconds and 150% for 3 seconds. For a heavy duty application, one larger drive rating than the motor is used and therefore provides a larger amount of overload current in comparison to the motor rating. Heavy duty sizing provides at least 150% for 60 seconds and 180% for 3 seconds. These percentages are with respect to the connected motor rating.

## Thermal Manager

The thermal manager assures that the thermal ratings of the power module are not exceeded. The operation of the thermal manager can be thought of as a function block with the inputs and outputs as shown below.

<!-- image -->

The following is a generalization of the calculations done by the thermal manager. The IGBT junction temperature is calculated based on the measured

drive temperature and a temperature rise that is a function of operating conditions. When the calculated junction temperature reaches a maximum limit, the drive faults. This fault cannot be disabled. This maximum junction temperature is stored on the power board EEPROM along with other information to define the operation of the drive overload function. These values are not user adjustable. In addition to the maximum junction temperature, there are temperature thresholds that select the points at which the PWM frequency begins to fold back, and at which current limit begins to fold back. P960 [Alarm Status B] alarm bits provide status as to when the fold back points are being reached regardless of whether or not the drive is configured to fold back. Bit 6 "PWMFrq Reduc" is the alarm bit for PWM fault and is 10 °C (50 °F) below the fault level. Bit 5 "CurLmt Reduc" is the alarm bit for current limit fold back and is 5 °C (41 °F) below the fault level. The over temperature fault level is reduced when running at output frequencies lower than 5 Hz.

## Configuration

P420 [Drive OL Mode] lets the user select the action to perform with increased current or drive temperature. When this parameter is set to option 0 "Disabled," the drive will not modify the PWM frequency or current limit. When set to 2 "Reduce PWM" the drive only modifies the PWM frequency. This is typically used on hoisting applications. Option 1 "Reduce CLmt" only modifies the current limit. When setting this parameter to 3 "Both-PWM 1st" the drive modifies the PWM frequency first and then the current limit, if necessary, to keep the drive from faulting with a F64 "Drive Overload" or F8 "Heatsink OvrTemp" fault.

## Temperature Display

The drive temperature is measured (NTC on the heat sink) and displayed as percentage of drive thermal capacity in P943 [Drive Temp Pct] and IGBT thermal capacity in P941 [IGBT Temp Pct]. These two parameters are normalized to the thermal capacity of the drive, which is frame dependent, and displays thermal usage in percent of maximum (100% = drive Trip). The heat sink temperature, P944 [Drive Temp C], and IGBT temperature, P942 [IGBT Temp Pct], in degrees C are also provided as test points. These cannot directly be related to a trip point as the maximums are defined as a percent.

## Faults

## Low Speed Operation

When operation is below 5 Hz, the IGBT duty cycle is such that heat builds up more rapidly in the power device. The thermal manager increases the calculated IGBT temperature at low output frequencies and causes corrective action to take place sooner. Consult technical support when prolonged operation at low output frequencies is required so proper drive derating can be applied. Also consider that when a drive is in current limit the output frequency is reduced to try to reduce the load. This works fine for a variable torque load, but for a constant torque load reducing the output frequency does not lower the current (load). Lowering current limit on a constant torque load pushes the drive down to a region where the thermal issue becomes worse. In this situation the thermal manager increases the calculated losses in the power module to track the worst case. So if the thermal manager normally provides 150% for 3 seconds at high speeds, it can only provide 150% for one second before generating a fault at low speeds. Some applications, such as hoisting and lifting, can benefit from the disabling of current limit fold back.

Faults are events or conditions occurring within and/or outside of the drive. These events or conditions by default are considered to be of such significant magnitude that drive operation is discontinued. Faults are annunciated by the STS (Status) indicator on the drive, a HIM, communications network and/or contact outputs.

## Drive Response to Faults

When a fault occurs, the fault condition is latched, requiring the user or application to perform a fault reset to clear the latched condition. The condition that caused the fault determines the user response. If the condition that caused the fault still exists after a fault reset, the drive faults again and the fault condition is latched.

- In response to a fault, the drive takes a predetermined action based on fault type. Drive response to some fault types are user configurable. With nonconfigurable faults the drive output is turned off and a "coast to stop" sequence occurs. The Troubleshooting section of PowerFlex 750-Series Programming Manual, publication 750-PM001, provides details on both types of faults.
- The fault code is entered into the first buffer of the fault queue (see Fault Queue below for rules).
- Additional data on the status of the drive at the time that the fault occurred is recorded. This information is always related to the most recent fault queue entry captured by P951[Last Fault Code]. When another fault occurs, this data is overwritten.

The following data/conditions are captured and latched into non-volatile drive memory.

- P952 [Fault Status A] P953 [Fault Status B] Indicates the occurrence of conditions that have been configured as faults.
- P954 [Status1 at Fault] P955 [Status2 at Fault] Captures operating conditions of the drive at the time of the fault.
- P957 [Fault Amps] Motor amps at the time of the fault.
- P958 [Fault Bus Volts] DC Bus volts at time of the fault.
- P956 [Fault Frequency] Output Hertz at the time of fault.
- P962 [AlarmA at Fault] P963 [AlarmB at Fault] Captures and displays P959/960 [Alarm Status A/B] at the last fault.

## Fault Queue

Faults are also logged into a fault queue such that a history of the most recent fault events is retained. Each recorded event includes a fault code (with associated text) and a fault "time of occurrence." PowerFlex 750-Series drives have a 32 event queue.

The fault queue records the occurrence of each fault event that occurs while no other fault is latched. Each fault queue entry includes a fault code and a time stamp value. New fault events are not logged to the fault queue if a previous fault has already occurred, but has not yet been reset. Only faults that actually trip the drive are logged. No fault that occurs while the drive is already faulted is logged.

The fault queue is a first-in, first-out (FIFO) queue. Fault queue entry 1 is always the most-recent entry (newest). Entry 32 is always the oldest. As a new fault is logged, each existing entry is shifted by one. The previous entry 1 moves to entry 2, previous entry 2 moves to entry 3, and so on. If the queue is full when a fault occurs, the oldest entry is discarded.

The fault queue is saved in nonvolatile storage at power loss and its content retained when power is cycled.

## Fault Code and Time Stamp

The fault code with descriptive text for each entry can be viewed with a HIM. Once the fault code is displayed, pressing the enter key again on the HIM displays the time stamp associated with that fault code. The time stamp is the elapsed time since the fault occurred.

When using one of the available software tools (DriveExecutive, DriveExplorer, Connected Component Workbench, or Logix Designer), the fault code, descriptive text, and time stamp are displayed simultaneously.

## Resetting or Clearing a Fault

A latched fault condition can be cleared by the following methods.

- An off to on transition on a digital input configured as DI Clear Fault.
- Pressing the "CLR" soft key or Stop button on the HIM once a fault has been displayed.
- A DPI peripheral (several ways).
- Performing a reset to factory defaults via parameter write.
- Cycling power to the drive such that the control board goes through a power-up sequence.

Resetting faults clears the faulted status indication. If any fault condition still exists, the fault is re-latched and another entry made in the fault queue.

## Clearing the Fault Queue

Performing a fault reset does not clear the fault queue. This can be done from a menu selection of the HIM or from a DPI command through the communications port.

## Fault Configuration

The drive can be configured such that some conditions do not trip the drive.

The following is a brief list of drive configurable faults. Some of these faults are explained in more detail in their own section of this document.

Accessories such as encoder or I/O cards have additional configurable faults. Refer to the Troubleshooting section of the PowerFlex 750-Series Programming Manual, publication 750-PM001 .

- P409 [Dec Inhibit Actn]
- P410 [Motor OL Actn]
- P435 [Shear Pin 1 Actn]
- P438 [Shear Pin 2 Actn]
- P444 [OutPhaseLossActn]
- P449 [Power Loss Actn]
- P462 [InPhase LossActn]
- P466 [Ground Warn Actn]
- P493 [HSFan EventActn]
- P500 [InFan EventActn]
- P506 [MtrBrngEventActn]
- P510 [MtrLubeEventActn]
- P515 [MchBrgEventActn]
- P519 [MchLubeEventActn]
- P865 [DPI Pt1 Flt Actn]
- P866 [DPI Pt2 Flt Actn]
- P867 [DPI Pt3 Flt Actn]
- P1173 [TorqAlarm TOActn]

## Input Phase Loss Detection

Occasionally, three-phase power sources can fail on one phase while continuing to deliver power between the remaining 2 phases (single-phase). Operating above 50% output under this single-phase condition can damage the drive. If such a condition is likely, we recommend that Input Phase Loss Detection be enabled. The drive can be programmed to turn on an alarm bit or issue a drive fault (minor or major). The drive accomplishes this by interpreting voltage ripple on the DC bus.

## Configuring Input Phase Loss Action

## P462 [InPhase LossActn]

The following bits configure Input Phase Loss action:

- "Ignore" (0) – No action is taken. This can seriously degrade the drive.
- "Alarm" (1) – Type 1 alarm indicated.
- "Flt Minor" (2) – Minor fault indicated. If running, drive continues to run. Enable with P950 [Minor Flt Cfg]. If not enabled, acts like a major fault.
- "FltCoastStop" (3) – Major fault indicated. Coast to Stop.
- "Flt RampStop" (4) – Major fault indicated. Ramp to Stop.
- "Flt CL Stop" (5) – Major fault indicated. Current Limit Stop.

An input phase loss is indicated in P937 [Condition Sts 1] Bit 4 "InPhaseLoss."

<!-- image -->

If a fault action has been selected as a result of an input phase loss, P952 [Fault Status A] Bit 4 "InPhaseLoss" is set.

<!-- image -->

If an alarm action is selected as a result for the input phase loss, P959 [Alarm Status A] Bit 4 "InPhaseLoss" is set.

<!-- image -->

## Motor Overload

## P463 [InPhase Loss Lvl]

Sets the threshold at which the DC bus voltage ripple triggers an F17 "Input Phase Loss" fault. Input phase loss is assumed when the DC bus voltage ripple exceeds the tolerance set by this parameter for a certain time period of time. Setting a larger value permits a higher bus voltage ripple without causing the drive to fault but also results in more heating in the bus capacitors shortening their life or possibly resulting in failure. The default value of 325 is equal to the expected ripple level for a full rated motor running at half load with single phase input. This is just a different way of saying that if you know you are going to run single phase, derate the drive by 50%.

Loading conditions on the motor could also have an effect on this parameter. Particularly shock loads.

The motor overload protection feature uses an IT (inverse time) algorithm to model the temperature of the motor and follows the same curve as a physical class 10 overload device.

<!-- image -->

P26 [Motor NP Amps] is used by the overload feature to establish the 100% level (y axis) shown in the graph above.

Setting P410 [Motor OL Actn] to zero disables the motor thermal overload. For multiple motor applications (more than one motor connected to one drive), separate external overloads for each motor are required, and the drive's motor overload can be disabled.

Operation of the overload is based on three parameters.

- P26 [Motor NP Amps] is the base value for motor protection.
- P413 [Mtr OL Factor] is used to adjust for the service factor of the motor. Within the drive, motor nameplate FLA is multiplied by motor overload factor to select the rated current for the motor thermal overload. This can be used to raise or lower the level of current that causes the motor thermal overload to trip without the need to adjust the motor FLA. For example, if motor nameplate FLA is 10 Amps and motor overload factor is 1.2, then motor thermal overload uses 12 Amps as 100%.

## IMPORTANT

Some motors have a service factor that is only for use with sine wave (non-drive) power. Check with the motor manufacturer to see if the nameplate service factor is valid or must be reduced when operated by a drive.

<!-- image -->

- P414 [Mtr OL Hertz] is used to further protect motors with limited speed ranges. Because many motors do not have sufficient cooling ability at lower speeds, the overload feature can be programmed to increase protection in the lower speed areas. This parameter defines the frequency where derating the motor overload capacity begins. For all settings of overload Hz other than zero, the overload capacity is reduced to 70% when output frequency is zero. During DC injection braking, the motor current can exceed 70% of FLA, but this causes the motor overload to trip sooner than when operating at base speed. At low frequencies, the limiting factor can be the drive overload rather than the motor overload.

<!-- image -->

## Duty Cycle for the Motor Overload

When the motor is cold, this function enables 3 minutes at 150%. When the motor is hot, it enables 1 minute at 150%. A continuous load of 102% is allowed to avoid nuisance faults. The duty cycle of the motor overload is defined as follows. If operating continuous at 100% FLA, and the load increases to 150% FLA for 59 seconds and then returns to 100% FLA, the load must remain at 100% FLA for 20 minutes to reach steady state.

<!-- image -->

The ratio of 1:20 is the same for all durations of 150%. When operating continuous at 100%, if the load increases to 150% for 1 second the load must then return to 100% for 20 seconds before another step to 150%.

|   %FLA |   Cold Trip Time Hot Trip Time |      |
|--------|--------------------------------|------|
|    105 |                           6320 | 5995 |
|    110 |                           1794 | 1500 |
|    115 |                            934 |  667 |
|    120 |                            619 |  375 |
|    125 |                            456 |  240 |
|    130 |                            357 |  167 |
|    135 |                            291 |  122 |
|    140 |                            244 |   94 |
|    145 |                            209 |   94 |
|    150 |                            180 |   60 |
|    155 |                            160 |   50 |
|    160 |                            142 |   42 |
|    165 |                            128 |   36 |
|    170 |                            115 |   31 |
|    175 |                            105 |   27 |
|    180 |                             96 |   23 |
|    185 |                             88 |   21 |
|    190 |                             82 |   19 |
|    195 |                             76 |   17 |
|    200 |                             70 |   15 |

## IMPORTANT

If the application requires high overload current for long durations (for example 150% for 60 seconds), heavy duty sizing (between drive and motor) is required.

## Activating Motor Overload

To turn on Motor Overload protection, configure P410 [Motor OL Actn]. This activates the function. Default setting is 3 "FltCoastStop." The following bits configure P410 [Motor OL Actn].

- "Ignore" (0) – No action is taken.
- "Alarm" (1) – Type 1 alarm indicated.
- "Flt Minor" (2) – Minor fault indicated. If running, drive continues to run. Enable with P950 [Minor Flt Cfg]. If not enabled, acts like a major fault.
- "FltCoastStop" (3) – Major fault indicated. Coast to Stop.
- "Flt RampStop" (4) – Major fault indicated. Ramp to Stop.
- "Flt CL Stop" (5) – Major fault indicated. Current Limit Stop.

## Overspeed Limit

Table 10 - Other Parameters

|   Parameter No. Parameter Name Description |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                        411 | Mtr OL at Pwr Up Motor Overload at Power Up parameter configures the motor overload feature regarding the state of the overload counter at power up. •  “Assume Cold” (0) – P418 [Mtr OL Counts] will be reset to zero the next time the drive is powered up. •  “UseLastValue” (1) – The value of P418 [Mtr OL Counts] will be retained at power down and restored the next time the drive is powered up. •  RealTimeClk (2) – The value of P418 [Mtr OL Counts] begins to decrease at drive power down, reflecting the cooling of the motor, and stops at drive power-up or when zero is reached. This option is only available when the real time clock is active on the drive. |
|                                        412 | Mtr OL Alarm Lvl You can have the drive issue an alarm when the P418 [Mtr OL Counts] reaches a certain level. Enter this value in P412 [Mtr OL Alarm Lvl]. This alarm level is different than, and independent of, the alarm action selected by P410 [Motor OL Actn].                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                        413 | Mtr OL Factor Motor Overload Factor parameter sets the minimum level of current (in percent or P26 [Motor NP Amps]) that causes the motor overload counter to increment. Current levels below this value decrement the overload counter. For example, a service factor of 1.15 implies continuous operation up to 115% of nameplate motor current.                                                                                                                                                                                                                                                                                                                                 |
|                                        414 | Mtr OL Hertz Motor Overload Hertz parameter selects the output frequency below which the motor operating current is derated (more sensitive) to account for the reduced self-cooling capability of typical motors, operating at slower speeds. For motors with extra low speed cooling capacity (for example 10:1 or blower cooled), reduce this setting to take full advantage of the motor being used.                                                                                                                                                                                                                                                                           |
|                                        415 | Mtr OL Reset Lvl Motor Overload Reset Level parameter sets the level that resets a motor overload condition, and lets a fault (if selected as the motor overload action) be manually reset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                        416 | MtrOL Reset Time Motor Overload Reset Time parameter displays the time it takes to restart the drive after a motor overload fault has occurred and the value in P418 [Mtr OL Counts] is less than the P415 [Mtr OL Reset Lvl].                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                        418 | Mtr OL Counts Motor Overload Counts parameter displays the accumulated percentage of motor overload. Continuously operating the motor over 100% of the motor overload setting increases this value to 100% and cause the action selected in P410 [Motor OL Actn] to be taken.                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                        419 | Mtr OL Trip Time Motor Overload Trip Time parameter displays the inverse of the motor overload time, equal to the number of seconds before P418 [Mtr OL Counts] reaches 100%, and the motor overload action is taken.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

An overspeed condition results when the motor speed falls outside of its normal operating range. The forward motor rotation limit is P520 [Max Fwd Speed] + P524 [Overspeed Limit] and the reverse motor rotation limit is P521 [Max Rev Speed] - P524 [Overspeed Limit]. In Flux Vector Control mode or Scalar Control mode with encoder, the motor speed used is a 2msec averaged value of P131 [Active Vel Fdbk]. In Scalar Control mode without an encoder, the overspeed check uses P1 [Output Frequency]. The overspeed condition must exist for at least 16 milliseconds before it causes a fault to occur.

## Password

## CIP Motion

When a PowerFlex 755 drive is running as a CIP Motion drive, then attribute 695 "Motor Overspeed User Limit" specifies the overspeed trip point directly. This attribute has units of percent of motor rated speed. So, if attribute 695 is set to 120% then the overspeed fault occurs at or above 120% rated speed.

## Interior Permanent Magnet

For Interior Permanent Magnet motor control mode, an additional limit is placed on the Speed Limit + Overspeed threshold. This threshold is not allowed to exceed the setting in P1641 [IPM Max Spd] and is a +/- check. P1641 [IPM Max Spd] is set to the speed at which the motor produces the voltage limit of the drive. If the drive faults while the motor is rotating at this speed, the motor produces a voltage at the output of the drive. This voltage could damage the drive if the limit is exceeded. This limit is calculated while performing the rotate portion of the Autotune tests. For example, if P1641 calculated to be 57.82 Hz, then the overspeed limit threshold is set by the Speed Limit + Overspeed Limit parameters and the results are limited to a value of +/- 57.82 Hz.

All parameter configuration settings for the drive and its connected peripherals can be protected from unauthorized access through the keypad by using a password.

When the host drive is password protected, parameter settings for the drive and its connected peripherals can be viewed but not changed until after the existing password value is entered. When attempting to edit a parameter value while logged out, the HIM prompts you for the password before allowing access.

Password protection also applies to the following.

- Drive start-up procedure
- Factory defaults
- User sets
- Copy Cat function

For detailed instructions on enabling and disabling password protection, refer to the PowerFlex 20-HIM-A6 and 20-HIM-C6S HIM (Human Interface Module) User Manual, publication 20HIM-UM001 .

## Real Time Clock

The PowerFlex 755 is equipped with a real-time clock with a battery backup. This enables programming of real time in the drive, and keeping that time even if the drives power is removed. This enables actual timestamps instead of runtime timestamps for faults and events. It is also used in the runtime accumulation of maintenance items such as total run time, number of times fans are running and so forth. If a battery is installed and the time values are set, time is accumulated. Approximate battery life is 4.5 years with drive unpowered, or lifetime if drive is powered.

The real time clock on the drive can be set two different ways. It can either be set from the HIM, or from DriveExecutive/DriveExplorer.

## Setting the Real Time Clock via Drive HIM

1. Access the Status screen.
2. If Port 00 (Host Drive) is not shown above the ESC soft key, use the or key to scroll to Port 00.
3. Press the key to display its last-viewed folder.
4. Use the or key to scroll to PROPERTIES folder.
5. Use the or key to select Set Date and Time.
6. Press the (Enter) key to display its last-viewed folder.
7. Press the EDIT soft key to access the Set Date and Time mode screen, which highlights the present time zone line.
8. To select the time zone (set the drive to the current time zone).
- Press the ZONES soft key to display the Select Time Zone screen.
- Use the or key to select your basic time zone region (for example, Full List).
- Press the (Enter) key to enter your selection.
- Use the or key to select your specific time zone (for example, Chicago), and press the (Enter) key to enter it.
9. To set the date (set the drive to the current date).
- Press the ▲ soft key to select the year in the top line, and use the numeric keys to enter the correct year.

To delete an erroneous date (or time) entry, use the ← soft key. Also, a partial or complete date (or time) value will not update until you press the ► soft key to enter the data. You have to press the ? soft key a second time

to advance to another field or press the ESC soft key to return to the previous screen.

- Press the ► soft key to select the month in the top line, and use the numeric keys to enter the correct month.
- Press the ► soft key to select the day in the top line, and use the numeric keys to enter the correct day.
10. To set the time (set the drive to the current time).
- Press the ► soft key to select the hour in the top line, and use the numeric keys to enter the correct hour.
- Press the ► soft key to select the minutes in the top line, and use the numeric keys to enter the correct minute.
- Press the ► soft key to select the seconds in the top line, and use the numeric keys to enter the correct seconds.
11. Press the ESC soft key to return to the previous screen.

## Setting the Real Time Clock via Drive Software

To set the real time clock using a software package like DriveExecutive or DriveExplorer™ software the procedure is the same.

<!-- image -->

1. First press the at the top center of the application.

<!-- image -->

This dialog box appears.

<!-- image -->

2. Click the Status and Feedback tab.

3. Click Display Alarms/Faults Dialog.

<!-- image -->

A new dialog box appears.

<!-- image -->

4. Click the Device System Time tab.

<!-- image -->

5. If necessary, change the values in the Set Time Zone and Set Device Time dialog boxes.

<!-- image -->

## Installing Battery

To install the battery, first locate the main control board. The location of the main control board is in the far right location of the control POD. The main control board for the PowerFlex 753 and 755 drives are shown below.

Figure 16 - PowerFlex 753 Main Control Board

<!-- image -->

Figure 17 - PowerFlex 755 Main Control Board

<!-- image -->

The battery is installed in pointer position 3. The battery receptacle requires a user-installed CR1220 lithium coin cell battery that provides power to the Real Time Clock. Installing a battery preserves the Real Time Clock setting in the event power to the drive is lost or cycled. Approximate battery life is 4.5 years with drive unpowered, or lifetime if drive is powered. Install the battery with "+" facing out.

## Reflected Wave

## Removing Battery

To remove the battery, simply use a screwdriver to press down on the metal tab going across the battery. Prying the battery out of its holder can result in permanent damage to the main control board.

<!-- image -->

Reflected waves are a phenomenon associated with long cables and fast changes in voltage levels. They were first identified on power transmission lines that are hundreds of miles long. When the power is switched on at one end, the step in voltage travels the length of the transmission line and is reflected back to the switch. The voltage at the far end often surges to twice the initial value of the voltage. Because the voltages involved are quite high, for example 230,000V or more, a surge of 460,000V can result in a damaging arcing fault.

Adjustable speed drives, using IGBT switches that turn on and off within a few nanoseconds, experience the same phenomenon at the AC motor terminals. This can cause motor failures within months or even weeks of commissioning the motor with a drive.

A PWM AC drive provides variable voltage and variable frequency to a motor from a DC bus voltage. It creates the sinusoidally varying voltage to the motor by continually changing the duty cycle of the IGBT switches in a pulse-widthmodulated fashion. Because the motor is largely an inductive load, the current that flows is an integration of the voltage with a lagging phase angle. Figure 18 shows what the drives line-to-line output voltage looks like. The peaks of the output voltage are equal to the value of the DC bus in the drive. Only the widths and polarities change.

Figure 18 - PWM Voltage at the Drive Output Terminals

<!-- image -->

Ideally, the voltage waveform at the motor looks exactly the same as the output of the drive. However, the voltage at the motor has individual on/off pulses that make up the PWM voltage waveform along with a ringing that occurs at every switching transition. This is shown in Figure 19. The peaks of the ringing waveform can easily reach two times the peak of the voltage pulses at the drive (the DC bus voltage). After a short time, the ringing dies away and the motor sees the normal DC bus voltage level. It is this peak level of the ringing voltage that causes motor failure.

Figure 19 - PWM Voltage at the Motor Terminals

<!-- image -->

Shorten the time sweep or magnify these pulses and the ringing effect at the motor terminals can be seen.

<!-- image -->

When the voltage at the motor terminals exceeds the insulation rating of the motor, corona begins to appear. This corona deteriorates the insulation system, eventually leading to a fault to ground. Such a failure is shown below.

<!-- image -->

The level of the DC bus voltage has a direct effect on the peak level of the ringing surge voltage. If the drive operates at 230V AC, the DC bus voltage is about 310V DC and two times peak only reaches 620Vpk. This peak will not damage most motors. However, a 460V AC drive operates at 620V DC bus voltage and 1240Vpk and a 575V AC drive operates at 775V DC and 1550Vpk.

Non-inverter grade motors have insulation systems rated to 1000V and 1200V depending on their construction.

- 1000V motors are assembled without phase paper.
- 1200V motors are assembled with phase paper and slot insulation.

Non-inverter grade motors will fail if operated from a 460V or 575V drive.

There are three ways to eliminate the effects of reflected waves on motors.

1. Match the motor surge impedance to the cable surge impedance.
2. Reduce the dv/dt.

These methods reduce or eliminate reflected wave and surge voltage at the motor.

3. Better insulate the motor so the effects of the surge voltage will not damage the motor.

For inverter applications, NEMA updated the standard MG 1-1998, section 31 regarding motor insulation systems. An inverter duty motor needs to withstand surge voltages that are 3.1 times the rated motor voltage and rise times greater than 0.1 μs. This is 1488V for a 460V motor. to provide better protection, some motor manufacturers have started producing 1600V rated insulation for inverter grade motors. However, even if a motor can withstand 1600V surges, it can still fail if the insulation cannot hold up under rated motor temperatures.

## The Terminator

Is it possible to match the surge impedance of the motor to the cable? There is a device called the terminator that does this, shown in the figure below. It is an RC network at the motor that matches the load surge impedance to the cable. Figure 20 shows the surge voltages when using the terminator. The overshoot is very low, with no ringing to speak of. Due to losses, this device is good for cable lengths up to 600 ft, and for carrier frequencies less than or equal to 4 kHz. However, its key advantage is that this one device works well for any motor in the range from 0.5 to 500hp because it does not have to handle the motor current, being a parallel device.

<!-- image -->

## Line Reactor

What if we go the other way, matching the surge impedance of the cable to the motor? There are several products available that do this. They all consist of the addition of a line reactor at the output of the drive. See the figure below. A 3% line reactor by itself also reduces the dV/dt, but a big disadvantage is that it reduces the voltage available to the motor by 3%. This is useful for cables up to about 600 ft. A better device is what we call a "reflected wave reduction" device where the line reactor is reduced to about 0.2%, and a resistor is placed in parallel with each of the reactors. This reduces the dV/dt and has a voltage drop of only 0.2% instead of 3%. It can be used with cables up to about 1200 ft.

<!-- image -->

A method to reduce just the dV/dt is to use shielded cable between the drive and the motor. The inherent capacitance between the lines and the shield help keep the surge voltage at 1200V up to 600 ft with PWM drives.

## Sine Wave Filter

Instead of matching impedances or reducing the dV/dt of the individual pulses coming from the drive, create a filter that enables the lower fundamental frequencies to pass, and block or absorb the higher frequencies caused by the fast switching IGBTs and the carrier frequency of the PWM waveform? There are two types that are on the market today. One that consists of an LC filter and another that consists of output line reactors along with tuned LC sections.

<!-- image -->

## Waveforms

The waveforms A, B, and C in the figure below describe the different mitigations solutions shown on top of each other.

- A - Unprotected motor
- B - Line Reactor at the Drive
- C - Terminator or RWR

Figure 20 - Waveform Comparison

<!-- image -->

Here are waveforms using a sine wave filter at 30 and 60 Hz. As you can see there are no issues with reflected wave when using a sine wave filter.

<!-- image -->

## Security

The Security feature provides drive access protection.

## Ports

This feature provides write access protection for individual communication ports in the drive. The HIM or communication modules with software tools can be used to change any port to read only.

A password can also be used with the HIM to prevent writing to parameters through the keypad. See Password on page 173 .

The following drive peripherals can be used to control access.

- 20-HIM-A6 or 20-HIM-C6S keypads
- 20-750-n and 20-COMM-n communication options
- 20-COMM-n legacy communication options

Refer to the PowerFlex 750-Series AC Drives Technical Data, publication 750-TD001 for suitability and details.

The following software tools can be used to control access.

- Connected Components Workbench™ (CCW) version 2.0 or later (freeware)
- DriveExplorer version 6.04.99 (freeware)
- DriveExecutive version 5.03 or later

By default, every DPI port in the drive is configured to allow read and write access.

To change the write access on an individual DPI port, change the bit setting of the associated port in P888 [Write Mask Cfg]. Changing the bit value from 1 (read/write) to 0 with a HIM provides read only capability. Using software such as DriveExplorer, DriveExecutive, or CCW can also be used to turn the bit off. Below is an example of using CCW to change port 4 to read only.

<!-- image -->

Any changes to P888 [Write Mask Cfg] will not take effect until one of the following three events occur.

- Power is removed and reapplied.
- A drive reset (not reset to defaults) is performed.
- P887 [Write Mask Act] Bit 15 transitions from 1 to 0.

The status of a port's write access can be verified at P887 [Write Mask Act]. For example, to verify that write access was disabled, P887 [Write Mask Act] Bit 4 "Port 4" equals 0.

<!-- image -->

The port that is being used to make security changes (for example a network adapter connected to Port 5) can only change other ports and not itself to read only. This is to prevent the complete lockout of a drive with no future way to regain write access.

## DPI (Network)

Network Security can only be activated with external software programs that have security capabilities, for example, FactoryTalk® software.

When P885 [Port Mask Act] Bit 15 "Security," P886 [Logic Mask Act] Bit 15 "Security," and P887 [Write Mask Act] Bit 15 "Security" are set to 1 "Read/ Write," Network Security has been enabled by an external program like FactoryTalk and is controlling the logic mask and write mask instead of the parameter. These bits can only be enabled/disabled via the network program.

A port that is being used to communicate to the drive and set the masks or network security can only make changes to other ports and not itself. This is to prevent a complete lockout from a drive.

When the writing capabilities of ports 1, 2, or 3 have been masked, via parameter 888 [Write Mask Cfg] or Network Security, the HIM displays the following message when trying to edit a parameter.

- A6-HIM: Security is enabled. Access Denied
- A3-HIM with Firmware that has Security Functionality: Security Enable. Access Denied
- A3-HIM with Firmware that does not have Security Functionality: Device State has Disabled Function

Software used to interface with the drive also indicates if the writing capabilities have been disabled by P888 [Write Mask Cfg] or Network Security, via the communication port being used.

Below are examples of parameters viewed with drive software via DriveExplorer or CCW when the connected port has been write disabled. The parameter value is grayed out and a lock is displayed.

DriveExplorer

<!-- image -->

Connected Components Workbench

<!-- image -->

Attempting to edit a parameter or clicking on the lock results in one the following screens being displayed when using DriveExecutive or CCW software.

<!-- image -->

## Shear Pin

As a default, the drive folds back when the output current exceeds the current limit level. However, the shear pin feature can be used to instantly fault the drive when output current exceeds a programmed amount. Additionally, the drive can be programmed to ignore this condition during acceleration and deceleration which often requires current that otherwise causes a shear pin fault. Also, the condition can be ignored for a programmable amount of time.

## Activating Shear Pin

To turn on either Shear Pin 1 or Shear Pin 2, configure [Shear Pin n Actn]. This activates the function. Selection between P435 [Shear Pin 1 Actn] and P438 [Shear Pin 2 Actn], cannot be made by a digital input. These parameters can be set over a communication network. The options for each shear pin action are the same. Default for each is 0 "Ignore." The following are the settings for P435 and P438.

- "Ignore" (0) – No action is taken.
- "Alarm" (1) – Type 1 alarm indicated.
- "Flt Minor" (2) – Minor fault indicated. If running, drive continues to run. Enable with P950 [Minor Flt Cfg]. If not enabled, acts like a major fault.
- "FltCoastStop" (3) – Major fault indicated. Coast to Stop.
- "Flt RampStop" (4) – Major fault indicated. Ramp to Stop.
- "Flt CL Stop" (5) – Major fault indicated. Current Limit Stop.

## Ignore During Acceleration

There are situations where a fast acceleration of the motor causes the drive to output current to the motor near or at the current limit value for shear pin and fault the drive while in acceleration. To avoid this condition set P434 [Shear Pin Cfg] Bit 0 "Shear1NoAcc" or Bit 1 "Shear2NoAcc" to 1 to ignore during acceleration.

## Shear Pin Level

A shear pin level must be programmed for the drive to monitor. This level, when exceeded, starts a timer that must expire before performing the [Shear Pin n Actn]. This level is entered into P436 [Shear Pin 1 Level] or P439 [Shear Pin 2 Level]. The units are amps. Default is drive rated amps. Maximum is rated amps multiplied by 1.5.

## Shear Pin Time

If an immediate action is to be taken, set shear pin time to 0. If the shear pin level is to be ignored for a period of time, enter that value into P437 [Shear Pin 1 Time] or P440 [Shear Pin 2 Time].

Generally, some value greater than 0 is entered in shear pin time to eliminate any faults on very short peak current spikes. Thus eliminating nuisance tripping.

## Fault Indication

A unique fault (Shear Pin 1, F61) or (Shear Pin 1, F62) is generated if the function is activated and the condition occurs.

## Application Example

By programming the Shear Pin feature, the drive faults, stopping the excess torque before mechanical damage occurs.

Shear Pin - Gradual Loading

<!-- image -->

<!-- image -->

## Acceleration Fault Anomaly

It is possible for the drive to trip during acceleration on a shear pin fault even when P434 [Shear Pin Cfg] Bits 0 or 1 in are set. This occurs when the accel time is set to something very small. The firmware looks at the internal "at speed" bit to indicate when acceleration is complete. This bit could be set internally faster than what appears the motor is indicating by sight. For example, if the accel time is set to something like 0.5 seconds and P434 Bit 0 is set. The drive will most likely trip on shear pin fault.

There are a couple ways to avoid this.

- Set the accel time longer. This reduces the current requirement.
- Enter a shear pin time longer than the acceleration time.

## Using Both Shear Pin 1 and 2

If your application requires a notification of an impending Shear Pin fault. You can set Shear Pin 1 to give an Alarm at a certain current level, then set Shear Pin 2

to issue the actual fault at a higher current level or a slightly longer Shear Pin time.

<!-- image -->

## Other Points

The Shear Pin feature is not to be taken as a precise current reactionary feature. There can be as much as +/- 5% error in the current feedback signal used to determine shear point levels. Therefore it could be possible that the timer trip point is being set and reset until the entire current reference is above a setpoint.

## Slip Compensation

When slip compensation mode is selected, the drive automatically adds the appropriate amount of output frequency to maintain a consistent motor speed independent of load. During drive commissioning, P621 [Slip RPM at FLA] is set based on entered motor nameplate information. This parameter can be adjusted to provide more or less compensation.

See the motor speed compensation figure below for a comparison of operation with and without slip compensation. This shows that over time, slip compensation corrects for changes in load (curved lines). In contrast, open loop operation shows that no correction is made based on load.

<!-- image -->

Internally, the drive converts the rated slip in RPM to rated slip in frequency. To more accurately determine the rated slip frequency in hertz, an estimate of flux current is necessary. This parameter is either a default value based on motor nameplate data or the autotune value. The drive scales the amount of slip compensation to the motor rated current. The amount of slip frequency added to the frequency command is then scaled by the sensed torque current (indirect measurement of the load) and displayed.

Slip compensation also affects the dynamic speed accuracy (ability to maintain speed during shock loading) as illustrated in the rotor speed response figure below. Initially, the motor is operating at some speed and no load. Some time later, an impact load is applied and the rotor speed decreases as a function of load and inertia. Finally, the impact load is removed and the rotor speed increases momentarily until the slip compensation is reduced based on the applied load.

The responsiveness to an impact load can be adjusted with P622 [Slip Comp BW]. However, too high setting can cause unstable operation and overshoot.

<!-- image -->

## Baking Line Application Example

The diagram below shows a typical application for the slip compensation feature. The PLC controls the frequency reference for all four of the drives. Drive No. 1 and Drive No. 3 control the speed of the belt conveyor. Slip compensation is used to maintain the RPM independent of load changes caused by the cutter or dough feed. By maintaining the required RPM, the baking time remains constant and therefore the end product is consistent.

<!-- image -->

## Slip Regulator

The slip regulator is used to compensate for temperature changes in an induction motor when FOC is used. The slip regulator uses a model of the motor to determine the desired d-axis voltage for a given operating point. A PI regulator is then used to change the drive's slip gain controlling the d-axis motor voltage. This in turn compensates for motor temperature (resistance) changes. The operation of the slip regulator is limited to regions where there is sufficient voltage (feedback or estimate) for the regulator to converge.

As default the slip regulator is enabled.

Do not disable this regulator. If you feel you need to disable this function, consult the factory for verification.

## Motor Control

| Topic                    |   Page |
|--------------------------|--------|
| Carrier (PWM) Frequency  |    196 |
| Dynamic Braking          |    197 |
| Flux Braking             |    216 |
| Flux Regulator           |    218 |
| Flux Up                  |    218 |
| High Resolution Feedback |    220 |
| Inertia Adaption         |    221 |
| Inertia Compensation     |    223 |
| Load Observer            |    225 |
| Motor Control Modes      |    226 |
| Motor Types              |    235 |
| Notch Filter             |    244 |
| Regen Power Limit        |    247 |
| Speed Reference          |    251 |
| Speed Regulation         |    260 |
| Torque Reference         |    262 |
| Speed Torque Position    |    266 |

<!-- image -->

## Carrier (PWM) Frequency

P38 [PWM Frequency] sets the carrier frequency at which the inverter output IGBTs (Insulated Gate Bipolar Transistors) switch. In general, use the lowest possible switching frequency that is acceptable for the particular application. An increased carrier frequency causes less motor heating and lowers the audible noise from the motor. However, it causes the IGBTs to heat up faster than by using the factory default PWM frequency of 4 kHz or 2 kHz depending on drive's the frame size. The higher switching frequency smoothes the current waveform. This reduces vibration in the motor windings and laminations reducing audible noise. This is desirable in applications where motors are installed close to control rooms or in domestic environments. See Figure 21 and note the output current at 2 kHz and 4 kHz. The smoothing of the current waveform continues 12 kHz.

The maximum carrier frequency per frame size and the derating guidelines according to PWM frequency can be found in the PowerFlex 750-Series AC Drives Technical Data, publication 750-TD001 .

Figure 21 - Current at 2 kHz and 4 kHz PWM Frequency

<!-- image -->

Some undesirable effects of higher switching frequencies include higher cable charging currents, higher potential for common mode noise and an increased risk of motor winding insulation breakdown due to the reflected wave phenomenon. Refer to the Wiring and Grounding Guidelines for PWM Drives, publication DRIVES-IN001 for further information. A very large majority of all drive applications will perform adequately at 2 kHz or 4 kHz.

Some applications require a fixed minimum PWM frequency (that is, using a sine wave filter in the output of the drive). In this case, P40 [Mtr Options Cfg] Bit 9 "PWM FreqLock" should be set to prevent the drive from lowering its carrier frequency due to a drive overload condition.

## Dynamic Braking

When an induction motor's rotor is turning slower than the synchronous speed set by the drive's output power; the motor is transforming electrical energy obtained from the drive into mechanical energy available at the drive shaft of the motor. This process is referred to as motoring.

When the rotor is turning faster than the synchronous speed set by the drive's output power, the motor is transforming mechanical energy available at the drive shaft of the motor into electrical energy that can be transferred back into the utility grid. This process is referred to as regeneration.

On most AC PWM drives, the AC power available from the fixed frequency utility grid is first converted into DC power by means of a diode rectifier bridge or controlled SCR bridge, before being inverted into variable frequency AC power. These diode or SCR bridges are very cost effective, but can handle power in only one direction, and that direction is the motoring direction. If the motor is regenerating, the bridge is unable to conduct the necessary negative DC current, and the DC bus voltage increases until the drive trips on a Bus Overvoltage fault.

There are bridge configurations, using either SCRs or Transistors that have the ability to transform DC regenerative electrical energy into fixed frequency utility electrical energy but are expensive. A more cost effective solution is to provide a Transistor Chopper on the DC bus of the AC PWM drive that feeds a power resistor, which transforms the regenerative electrical energy into thermal heat energy, which is dissipated into the local environment.

This process is generally called Dynamic Braking, with the Chopper Transistor and related control and components called the Chopper Module, and the power resistor called the Dynamic Brake Resistor. The entire assembly of Chopper Module with Dynamic Brake Resistor is sometime referred to as the Dynamic Brake Module.

Chopper Modules are designed to be applied in parallel if the current rating is insufficient for the application. One Chopper Module is the designated Master Chopper Module, while any other Modules are the designated Follower Modules. Two lights have been provided on the front of the enclosure to indicate Chopper Module operation – the DC Power light and the Brake On light. The DC Power light is lit when DC power has been applied to the Chopper Module. The Brake On light is lit when the Chopper Module is operating or chopping and is a flickering type of indication.

Update: As of December of 2010, Rockwell Automation no longer has a Chopper Module product as well as a Dynamic Braking Module product. The light configuration stated above was specific to the Rockwell Automation product.

## How it Works

There are two different types of control for dynamic braking, hysteretic control and PWM control. Each used by themselves in a standard stand alone product has no advantage over the other. The preferred control is the PWM method when the application is common DC bus. This advantage is described below.

## Hysteretic Control

The hysteretic method of dynamic braking uses a voltage sensing circuit to monitor the DC bus. As the DC bus voltage increases to the Vdc\_on level the brake IGBT is turned on and is left on until the voltage drops to the Vdc\_off level, which is not so desirable in common DC bus applications—see below. Some PowerFlex drives allow the Vd Vdc\_off f level, [DB Threshold], to be adjusted if the application required it. Setting this level lower makes the dynamic braking more responsive but could lead to excessive DB activation.

<!-- image -->

## PWM Control

This type of control to operate the brake IGBT is similar to the way output voltage to the motor is controlled. As the DC bus voltage increases and hits some predetermined limit the brake IGBT is turned on/off according to a control algorithm switched at 1 kHz. This type of control virtually eliminates bus ripple. The big advantage is when this type of control is in a common bus configuration.

<!-- image -->

<!-- image -->

## Common DC Bus Applications

In a common bus configuration when a dynamic braking resistor is installed on each drive sharing the DC bus, it's possible that the brake IGBT in some drives will not turn on, giving the impression that the drive is not functioning correctly or seeing one drive's brake IGBT failing consistently while the other drives are fine. Looking at the below diagram, it shows the DC bus level for two drives on common bus. The delta between these voltages are exaggerated for clarity. As the voltage increases, the Drive #1 IGBT turns on and decreases the voltage level before Drive #2 sees voltage high enough to be told to turn on. This results in Drive #1 doing all the dynamic braking. Now this situation could be alright as long as the minimum ohmic value for resistance is not violated and the regen event isn't so great that a single resistor can't handle the power. Of course, if there is a large regen event where the voltage continues to rise after Drive #1 has turned on, Drive #2 fires its IGBT when it reaches the voltage limit.

<!-- image -->

Here are two drives with PWM DB control on a common bus. Because one drive turns on at a certain duty cycle the bus voltage is likely to continue to rise guaranteeing that the other drive's IGBT turns on (at a different duty cycle).

<!-- image -->

## How to Select A Chopper Module and Dynamic Brake Resistor

In general, the motor power rating, speed, torque, and details regarding the Regenerative mode of operation is needed to estimate what Chopper Module rating and Dynamic Brake Resistor value to use. A rule of thumb to use is that a Dynamic Brake Module can be specified when regenerative energy is dissipated on an occasional or periodic basis. When a drive is consistently operating in the Regenerative mode of operation, consider utilizing equipment that transforms the electrical energy back to the fixed frequency utility.

The peak regenerative power of the drive must be calculated to determine the maximum Ohmic value of the Dynamic Brake Resistor and to estimate the minimum current rating of the Chopper Module. The Rating of the Chopper Module is chosen from the Brake Chopper Module manual. Once the Chopper Module current rating is known, a minimum Dynamic Brake Resistance value is also known. A range of allowable Dynamic Brake Ohmic values is now known. These values exist from the minimum value set by the Chopper Transistor current rating to a maximum value set by the peak regenerative power developed by the drive to decelerate or satisfy other regenerative applications. If a Dynamic Brake Resistance value less than the minimum imposed by the choice of the Chopper Module is made and applied, damage can occur to the Chopper Transistor. If a Dynamic Brake Resistance value greater than the maximum imposed by the choice of the peak regenerative drive power is made and applied,

the drive can trip off due to transient DC bus overvoltage problems. Once the choice of the approximate Ohmic value of the Dynamic Brake Resistor is made, the wattage rating of the Dynamic Brake Resistor can be made.

The wattage rating of the Dynamic Brake Resistor is estimated by applying the knowledge of the drive motoring and regenerating modes of operation. The average power dissipation of the Regenerative mode must be estimated and the wattage of the Dynamic Brake Resistor chosen to be slightly greater than the average power dissipation of the drive. If the Dynamic Brake Resistor has a large thermodynamic heat capacity, the resistor element is able to absorb a large amount of energy without the temperature of the resistor element exceeding the operational temperature rating. Thermal time constants in the order of 50 seconds and higher satisfy the criteria of large heat capacities for these applications. If a resistor has a small heat capacity, the temperature of the resistor element could exceed the maximum temperature limits during the application of pulse power to the element and could exceed the safe temperature limits of the resistor.

The peak regenerative power can be calculated in English units (Horsepower), in The International System of Units (SI) (Watts), or in the per unit system (pu), which is dimensionless for the most part. In any event, the final number must in Watts of power to estimate Dynamic Brake Ohmic value. Calculations in this page are demonstrated in SI units.

## Speed, Torque, Power Profile

The following figure is a typical dynamic braking application. The top trace represents speed and is designated by the omega symbol. In the profile the motor is accelerated to some speed, it holds that speed for a period of time and is then decelerated. This deceleration is not necessarily to zero speed. The cycle is then repeated.

The middle trace represents motor torque. Torque starts out high as the motor is accelerated then drops down to maintain the commanded speed. Then the torque turns negative as the motor is decelerated. The cycle is then repeated.

The bottom trace represents motor power. Power increases as the motor speed increases. Power decreases some to maintain the commanded speed then goes

negative when deceleration starts. (this point called -Pb is the first value that needs to be calculated). The cycle is then repeated.

<!-- image -->

## Dynamic Braking Module (no longer a Rockwell Automation product)

Figure 22 shows a simplified schematic of a Chopper Module with Dynamic Brake Resistor. The Chopper Module is shown connected to the positive and negative DC bus conductors of an AC PWM Drive. The two series connected Bus Caps are part of the DC bus filter of the AC Drive. The significant power components of the Chopper Module are the protective fusing, the Crowbar SCR, the Chopper Transistor (an IGBT), the Chopper Transistor Voltage Control (hysteretic voltage comparator), and a freewheel diode for the Dynamic Brake Resistor.

The protective fuse is sized to work in conjunction with the Crowbar SCR. Sensing circuitry within the Chopper Transistor Voltage Control determines if abnormal conditions exist within the Chopper Module. One of these abnormal conditions is a shorted Chopper Transistor. If this condition is sensed, the Chopper Transistor Voltage Control fires the Crowbar SCR, shorting the DC

bus, and melting the fuse links. This action isolates the Chopper Module from the DC bus until the problem can be resolved.

The Chopper Transistor is an Isolated Gate Bipolar Transistor (IGBT). There are several transistor ratings that are used in the various Chopper Module ratings. The most important rating is the collector current rating of the Chopper Transistor that helps to determine the minimum Ohmic value used for the Dynamic Brake Resistor. The Chopper Transistor is either ON or OFF, connecting the Dynamic Brake Resistor to the DC bus and dissipating power, or isolating the resistor from the DC bus.

The Chopper Transistor Voltage Control regulates the voltage of the DC bus during regeneration. The average value of DC bus voltage is 375V DC (for 230V AC input), 750V DC (for 460V AC input), and 937.5V DC (for 575V AC input). The voltage dividers reduce the DC bus voltage to a low enough value that is usable in signal circuit isolation and control. The DC bus feedback voltage from the voltage dividers is compared to a reference voltage to actuate the Chopper Transistor.

The Freewheel Diode (FWD) in parallel with the Dynamic Brake Resistor enables any magnetic energy stored in the parasitic inductance of that circuit to be safely dissipated during turn off of the Chopper Transistor.

Figure 22 - Chopper Module Schematic

<!-- image -->

Sizing the Dynamic Brake Module Gather the following information.

1. The nameplate power rating of the motor in watts, kilowatts, or horsepower.
2. The nameplate speed rating of the motor in rpm or rps.

3. The motor inertia and load inertia in kilogram-meters2, or lb·ft 2 .
4. The gear ratio, if a gear is present between the motor and load, GR.
5. Review the Speed, Torque Power profile of the application.

Equations used for calculating Dynamic Braking values use the following variables.

(t) = The motor shaft speed in Radians/second, or Rad s 2N
R 60 = ---------N
RPM

N (t) = The motor shaft speed in Revolutions Per Minute, or RPM

T (t) = The motor shaft torque in Newton-meters, 1.01 lb·ft - 1.355818N·m

P (t) = The motor shaft power in Watts, 1.0HP = 746 Watts

-P b = The motor shaft peak regenerative power in Watts

## Step 1 – Determine the Total Inertia

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kilogram-meters 2 , kg·m  , or pound-feet 2 , lb·ft 2

J m = Motor inertia, kilogram-meters2, kg·m 2 , or pound-feet2, lb·ft 2

GR = The gear ratio for any gear between motor and load, dimentionless

JL = Load inertia, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2 – 1 lb·ft 2 = 0.04214011 kg·m 2

## Step 2 – Calculate the Peak Braking Power

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kg·m 

 = rated angular rotational speed, Rad s 2N 60 = ---------

N = Rated motor speed, RPM

t 3 - t 2 = total time of deceleration from rated speed to 0 speed, in seconds

P b = peak braking power, watts (1.0 HP = 746 Watts)

Compare the peak braking power to that of the rated motor power, if the peak braking power is greater that 1.5 times that of the motor, the deceleration time, (t 3 - t 2 ), needs to be increased so that the drive does not go into current limit. Use 1.5 times because the drive can handle 150% current maximum for 3 seconds.

Peak power can be reduced by the losses of the motor and inverter.

## Step 3 – Calculating the Maximum Dynamic Brake Resistance Value

<!-- formula-not-decoded -->

Vd = The value of DC bus voltage that the chopper module regulates at and is equal to 375V DC, 750V DC, or 937.5V DC

P b = The peak braking power calculated in Step 2

R db1 = The maximum allowable value for the dynamic brake resistor

Choose a Dynamic Brake resistance value that is less than the value calculated in Step 3. If the value is greater than the calculated value, the drive can trip on DC bus overvoltage. Remember to account for resistor tolerances.

Step 4 – Choosing the correct Dynamic Brake Module

|               | Cat. No. Resistance Wattage   |          |
|---------------|-------------------------------|----------|
| 240 Volt      | 240 Volt                      | 240 Volt |
|               | KA005 28 ohms 666 watts       |          |
|               | KA010 13.2 ohms 1650 watts    |          |
| KA050 N/A N/A |                               |          |
| 460 Volt      | 460 Volt                      | 460 Volt |
|               | KB005 108 ohms 1500 watts     |          |
|               | KB010 52.7 ohms 2063 watts    |          |
|               | KB050 10.5 ohms 7000 watts    |          |
| 600 Volt      | 600 Volt                      | 600 Volt |
|               | KC005 108 ohms 1500 watts     |          |
|               | KC010 52.7 ohms 2063 watts    |          |
|               | KC050 15.8 ohms 8000 watts    |          |

In the table above, choose the correct Dynamic Brake Module based upon the resistance value being less than the maximum value of resistance calculated in Step 3. If the Dynamic Brake Resistor value of one Dynamic Brake Module is not sufficiently low, consider using up to three Dynamic Brake Modules in parallel, such that the parallel Dynamic Brake resistance is less than Rdb1 calculated in

Step 3. If the parallel combination of Dynamic Brake Modules becomes too complicated for the application, consider using a Brake Chopper Module with a separately specified Dynamic Brake Resistor.

## Step 5 – Estimate average power

It is assumed that the application exhibits a periodic function of acceleration and deceleration. If (t 3 - t 2 ) = the time in seconds necessary for deceleration from rated speed to 0 speed, and t4 is the time in seconds before the process repeats itself, then the average duty cycle is (t3 - t2)/t4. The power as a function of time is a linearly decreasing function from a value equal to the peak regenerative power to 0 after (t 3 - t 2 ) seconds have elapsed. The average power regenerated over the interval of (t 3 - t 2 ) seconds is Pb/2. The average power in watts regenerated over the period t4 is:

<!-- formula-not-decoded -->

P av v = Average dynamic brake resistor dissipation, in watts t 3 - t 2 = Elapsed time to decelerate from rated speed to 0 speed, in seconds

t 4 = Total cycle time or period of process, in seconds

P b = Peak braking power, in watts

The Dynamic Brake Resistor power rating of the Dynamic Brake Module (singly or two in parallel) that is chosen must be greater than the value calculated in Step 5. If it is not, then a Brake Chopper Module with the suitable Dynamic Brake Resistor must be specified for the application.

## Step 6 – Calculate Percent Average Load

The calculation of AL is the Dynamic Brake Resistor load expressed as a percent. Pdb is the sum of the Dynamic Brake Module dissipation capacity and is obtained from the table in Step 4. This gives a data point for a line to be drawn on the curve in Figure 3. The number calculated for AL must be less than 100%. If AL is greater than 100%, an error was made in a calculation or the wrong Dynamic Brake Module was selected.

<!-- formula-not-decoded -->

AL = Average load in percent of Dynamic Brake Resistor

P av v = Average dynamic brake resistor dissipation calculated in Step 5 (Watts)

P db = Steady state power dissipation capacity of resistors obtained from the table in Step 4 (Watts)

## Step 7 – Calculate Percent Peak Load

The calculation of PL in percent gives the percentage of the instantaneous power dissipated by the Dynamic Brake Resistors relative to the steady state power dissipation capacity of the resistors. This gives a data point to be drawn on the curve of Figure 3. The number calculated for PL commonly falls between 300% and 600% for the Dynamic Brake Modules. A calculated number for PL of less than 100% indicates that the Dynamic Brake Resistor has a higher steady state power dissipation capacity than is necessary.

<!-- formula-not-decoded -->

PL = Peak load in percent of Dynamic Brake Resistor

P av v = Peak braking power calculated in Step 2 (Watts)

P db = Steady state power dissipation capacity of resistors obtained from the table in Step 4 (Watts)

## Step 8 – Plot PL and AL on Curve

Draw a horizontal line equal to the value of AL (Average Load) in percent as calculated in Step 6. This value must be less than 100%. Pick a point on the vertical axis equal to the value of PL (Peak Load) in percent as calculated in Step 7. This value will be greater than 100%. Draw a vertical line at (t3 - t2) seconds such that the line intersects the AL line at right angles. Label the intersection Point 1. Draw a straight line from PL on the vertical axis to Point 1 on the AL line. This line is the power curve described by the motor as it decelerates to minimum speed.

<!-- image -->

If the line you drew lies to the left of the constant temperature power curve of the Dynamic Brake Resistor, then there is no application problem. If any portion of the line lies to the right of the constant temperature power curve of the Dynamic Brake Resistor, then there is an application problem. The application problem is that the Dynamic Brake Resistor is exceeding its rated temperature during the interval that the transient power curve is to the right of the resistor power curve capacity. It is prudent to parallel another Dynamic Brake Module or apply a Brake Chopper Module with a separate Dynamic Brake Resistor.

## Sizing the Chopper and Resistors

## Chopper and Resistors (no longer a Rockwell Automation product)

Sizing the chopper module is the same as the dynamic brake module with a couple of added steps. Because the chopper is separate from the resistors, an additional calculation for current needs to be made. Additionally a calculation for watt-seconds or joules needs to be made for resistor sizing.

## Step 1 – Determine the Total Inertia

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kilogram-meters 2 , kg·m  , or pound-feet 2 , lb·ft 2

J m = motor inertia, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2

GR 2 = the gear ratio for any gear between motor and load, dimensionless

JL = load inertia, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2 (1.0 lb·ft 2 = 0.04214011 kg·m  )

## Step 2 – Calculate the Peak Braking Power

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kg·m 

 = rated angular rotational speed, Rad s 2N 60 = ---------

N = Rated motor speed, RPM

t 3 - t 2 = total time of deceleration from the rated speed to 0 speed, seconds

P b = peak braking power, watts (1.0HP = 746 Watts)

Compare the peak braking power to that of the rated motor power, if the peak braking power is greater that 1.5 times that of the motor, then the deceleration time, (t 3 - t 2 ), needs to be increased so that the drive does not go into current limit. Use 1.5 times because the drive can handle 150% current maximum for 3 seconds.

Peak power can be reduced by the losses of the motor and inverter.

## Step 3 – Calculating the Maximum Dynamic Brake Resistance Value

<!-- formula-not-decoded -->

Vd = The value of DC bus voltage that the chopper module regulates at and is equal to 375V DC, 750V DC, or 937.5V DC

P b = The peak braking power calculated in Step 2

R db1 = The maximum allowable value for the dynamic brake resistor

The choice of the Dynamic Brake resistance value will be less than the value calculated in Step 3. If the value is greater than the calculated value, the drive can trip on DC bus overvoltage. Remember to account for resistor tolerances.

## Step 4 – Choosing the Chopper Module

<!-- formula-not-decoded -->

I dl = The minimum current flowing through the chopper module transistor

Vd = The value of DC bus voltage chosen in Step 3

Rdbl = The value of the dynamic brake resistor calculated in Step 3

The value of I d1 sets the minimum value of current rating for the Chopper Module. When the Chopper Module choice has been made, the current rating of the Module Transistor must be greater than or equal to the calculated value for I d1 . See the table below for rating values.

| Drive Voltage (Volts AC)   | Turn-On Voltage (Volts DC)   | Cat. No. Peak Transistor Current Rating (Amps) Minimum DB Resistor Value (Ohms)   |
|----------------------------|------------------------------|-----------------------------------------------------------------------------------|
|                            | 230 375 WA018 50 9.0         |                                                                                   |
|                            | 230 375 WA018 50 9.0         | WA070 200 2.3                                                                     |
|                            | 230 375 WA018 50 9.0         | WA115 400 1.25                                                                    |
|                            | 460 750 WB009 25 37          |                                                                                   |
|                            | 460 750 WB009 25 37          | WB035 100 9.0                                                                     |
|                            | 460 750 WB009 25 37          | WB110 400 2.5                                                                     |
|                            | 575 935 WC009 25 46          |                                                                                   |
|                            | 575 935 WC009 25 46          | WC035 75 15.5                                                                     |
|                            | 575 935 WC009 25 46          | WC085 400 3.0                                                                     |

## Step 5 – Determine the Minimum Resistance

Each chopper module in the table above has a minimum resistance associated with it. If a resistance lower than the value show in the table is connected to the chopper module, the brake transistor is most likely be damaged.

## Step 6 – Choosing the Dynamic Brake Resistance Value

To avoid damage to this transistor and get the desired braking performance, select a resistor with a resistance between the maximum resistance calculated in Step 3 and the minimum resistance of the selected chopper module.

## Step 7 – Estimating the Minimum Wattage requirements for the Dynamic Brake Resistor

It is assumed that the application exhibits a periodic function of acceleration and deceleration. If (t 3 - t 2 ) = the time in seconds necessary for deceleration from rated speed to 0 speed, and t4 is the time in seconds before the process repeats itself, then the average duty cycle is (t3 - t2)/t4. The power as a function of time is a linearly decreasing function from a value equal to the peak regenerative power to 0 after (t 3 - t 2 ) seconds have elapsed. The average power regenerated over the interval of (t 3 - t 2 ) seconds is Pb/2. The average power in watts regenerated over the period t4 is:

<!-- formula-not-decoded -->

P av v = average dynamic brake resistor dissipation, watts t 3 - t 2 = Elapsed time to decelerate from rated speed to 0 speed, seconds

t 4 = Total cycle time or period of process, seconds

P b = Peak braking power, watts

The Dynamic Brake Resistor power rating in watts that is chosen will be equal to or greater than the value calculated in Step 7.

## Step 8 – Calculate the requires Watt-Seconds (joules) for the resistor

To be sure the resistor's thermal capabilities are not violated, a calculation to determine the amount of energy dissipated into the resistor is made. This determines the amount joules the resistor must be able to absorb.

<!-- formula-not-decoded -->

P ws = Required watt - seconds of the resistor t 3 - t 2 = Elapsed time to decelerate from b speed to 0 speed, seconds

P b = Peak braking power, watts

## Internal Brake IGBT for PowerFlex 755 Drives

## Sizing Resistors for an internal DB IGBT

Sizing resistors for the internal DB IGBT Uses the same formula's as previous, and is very similar to the Chopper Module sizing.

## Step 1 – Determine the Total Inertia

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2

J m = motor inertia, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2

GR = The gear ratio for any gear between motor and load, dimensionless

JL = load inertia, kilogram-meters2, kg·m  , or pound-feet2, lb·ft 2 (1.0 lb·ft 2 = 0.04214011 kg·m  )

## Step 2 – Calculate the Peak Braking Power

<!-- formula-not-decoded -->

JT = Total inertia reflected to the motor shaft, kg·m 

 = rated angular rotational speed, Rad s 2N 60 = ---------

N = Rated motor speed, RPM

t 3 - t 2 = total time of deceleration from the rated speed to 0 speed, seconds

P b = peak braking power, watts (1.0HP = 746 Watts)

Compare the peak braking power to that of the rated motor power, if the peak braking power is greater that 1.5 times that of the motor, then the deceleration time, (t 3 - t 2 ), needs to be increased so that the drive does not go into current limit. Use 1.5 times because the drive can handle 150% current maximum for 3 seconds.

Peak power can be reduced by the losses of the motor and inverter.

## Step 3 – Calculating the Maximum Dynamic Brake Resistance Value

<!-- formula-not-decoded -->

Vd = The value of DC bus voltage that the drive regulates at and is equal to 375V DC, 750V DC, or 937.5V DC depending on input voltage

P b = The peak braking power calculated in Step 2

R db1 = The maximum allowable value for the dynamic brake resistor

The choice of the Dynamic Brake resistance value will be less than the value calculated in Step 3. If the value is greater than the calculated value, the drive can trip on DC bus overvoltage. Remember to account for resistor tolerances.

## Step 4 – Determine the Minimum Resistance

Each drive with an internal DB IGBT has a minimum resistance associated with it. If a resistance lower than the minimum value for a given drive is connected, the brake transistor will likely be damaged. Below is a table of minimum resistances for frame 2 through 7 PowerFlex 750-Series drives.

|    | Frame 400V   |                   | ND kW Catalog Code Min Resistance Max DB Current ND HP Catalog Code Min Resistance Max DB Current   | 480V   |                |                 |
|----|--------------|-------------------|-----------------------------------------------------------------------------------------------------|--------|----------------|-----------------|
|  2 |              | 0.75 C2P1 31.6 25 |                                                                                                     | 1.0    | D2P1 31.6 25   |                 |
|  2 | 1.5          | C3P5 31.6 25      |                                                                                                     | 2.0    | D3P4 31.6 25   |                 |
|  2 | 2.2          | C5P0 31.6 25      |                                                                                                     | 3.0    | D5P0 31.6 25   |                 |
|  2 | 4.0          | C8P7 31.6 25      |                                                                                                     | 5.0    | D8P0 31.6 25   |                 |
|  2 | 5.5          | C011 31.6 25      |                                                                                                     | 7.5    | D011 31.6 25   |                 |
|  2 | 7.5          | C015 31.6 25      |                                                                                                     | 10     | D014 31.6 25   |                 |
|  2 | 11           | C022 22.6 34.9 15 |                                                                                                     |        |                | D022 22.6 34.9  |
|  3 | 15           | C030 31.6 25      |                                                                                                     | 20     | D027 31.6 25   |                 |
|  3 |              | 18.5 C037 31.6 25 |                                                                                                     | 25     | D034 31.6 25   |                 |
|  3 | 22           | C043 16.6 47.6 30 |                                                                                                     |        | D040 16.6 47.6 |                 |
|  4 | 30           | C060 15.8 50      |                                                                                                     | 40     | D052 15.8 50   |                 |
|  4 | 37           | C072 15.8 50      |                                                                                                     | 50     | D065 15.8 50   |                 |
|  5 | 37           | C072 7.9          | 100                                                                                                 | 50     | D065 7.9       | 100             |
|  5 | 45           | C085 7.9          | 100                                                                                                 | 60     | D077 7.9       | 100             |
|  5 | 55           | C104 7.9          | 100                                                                                                 | 75     | D096 7.9       | 100             |
|  6 | 55           | C104 3.3          | 239.4 75                                                                                            |        | D096 3.3       | 239.4           |
|  6 | 75           | C140 3.3          | 239.4 100                                                                                           |        | D125 3.3       | 239.4           |
|  6 | 90           | C170 3.3          | 239.4 125                                                                                           |        | D156 3.3       | 239.4           |
|  6 | 110          | C205 3.3          | 239.4 150                                                                                           |        | D186 3.3       | 239.4           |
|  6 | 132          | C260 3.3          | 239.4 200                                                                                           |        | D248 3.3       | 239.4           |
|  7 | 132          | C260 2.4          | 329                                                                                                 | 200    | D248 2.4       | 329             |
|  7 | 160          | C302 2.4          | 329                                                                                                 | 250    | D302 2.4       | 329             |
|  7 | 200          | C367 2.4          | 329                                                                                                 | 300    | D361 2.4       | 329             |
|  7 | 250          |                   | C456 1.65 478.8 350                                                                                 |        |                | D415 1.65 478.8 |
|  7 | 270          |                   | C477 1.65 478.8 400                                                                                 |        |                | D477 1.65 478.8 |

## Step 5 – Choosing the Dynamic Brake Resistance Value

To avoid damage to this transistor and get the desired braking performance, select a resistor with a resistance between the maximum resistance calculated in Step 3 and the minimum resistance of the drive IGBT.

## Step 6 – Estimating the Minimum Wattage requirements for the Dynamic Brake Resistor

It is assumed that the application exhibits a periodic function of acceleration and deceleration. If (t 3 - t 2 ) = the time in seconds necessary for deceleration from rated speed to 0 speed, and t4 is the time in seconds before the process repeats itself, then the average duty cycle is (t3 - t2)/t4. The power as a function of time is a linearly decreasing function from a value equal to the peak regenerative power to 0 after (t 3 - t 2 ) seconds have elapsed. The average power regenerated over the interval of (t 3 - t 2 ) seconds is Pb/2. The average power in watts regenerated over the period t4 is:

<!-- formula-not-decoded -->

P av v = Average dynamic brake resistor dissipation, in watts t 3 - t 2 = Elapsed time to decelerate from rated speed to 0 speed, in seconds

t 4 = Total cycle time or period of process, in seconds

P b = Peak braking power, in watts

The Dynamic Brake Resistor power rating in watts that is chosen will be equal to or greater than the value calculated in Step 6.

## Step 7 – Calculate the requires Watt-Seconds (joules) for the resistor

To be sure the resistor's thermal capabilities are not violated, a calculation to determine the amount of energy dissipated into the resistor is made. This determines the amount joules the resistor must be able to absorb

<!-- formula-not-decoded -->

P ws = Required watt - seconds of the resistor t 3 - t 2 = Elapsed time to decelerate from b speed to 0 speed, seconds

P b = Peak braking power, watts

## Flux Braking

Flux Braking is an independent feature from the P370/371 [Stop Mode A/B] available in PowerFlex 750-Series drives. When enabled, flux braking is active during the decel ramp of a speed change. Flux braking changes the Volts per Hertz curve ratio outputting a higher voltage, relative to the normal V/Hz curve, to the motor causing over fluxing thus reducing the speed faster than just the decel ramp alone. This feature is not intended for high inertia loads because over fluxing can cause excessive heating in the motor. Very long decel times can build heat.

Flux Braking works in all motor control modes.

Table 11 - Flux Braking Parameters

| Number Parameter Name Min / Max        | Default        |
|----------------------------------------|----------------|
| 388 Flux Braking En Disabled / Enabled | Disabled       |
| 389 Flux Braking Lmt 100.00 / 250.00 % | 125.00         |
| 390 Flux Braking Ki 0.0 / 1000000.0    | 10000.0        |
| 391 Flux Braking Kp 0.0 / 1000000.0    | 0.0 (Disabled) |

## Traces

In all of the following plots the Accel/Decel times are 0.5 s. P372/373 [Bus Reg Mode A/B] is set to option 1 "Adjust Freq." There is a fair amount of inertia connected to the motor shaft. P370/371 [Stop Mode A/B] is set to 1 "Ramp" to stop.

In the plot below the Flux Braking feature is disabled. Note the decel time. Here the bus regulator is controlling the stop time.

Flux Braking - Disabled

<!-- image -->

In the next plot all conditions are the same except the Flux Braking feature is enabled. Note the flux to the motor is increased and the decel time is shorter. Flux Braking - Enabled

<!-- image -->

Finally the same test with the gains set to maximum levels. Slightly faster decel. The use of the gains vary with the connected load.

Flux Braking - Full Gains

<!-- image -->

## Flux Regulator

## Flux Up

The flux regulator is used to control and limit the overall (fundamental) voltage applied to an induction motor when FOC is used. The flux regulator controls field weakening above base speed and maintains voltage margin for a current regulator. A variation of the induction motor flux regulator is used for PM motors for operation above base speed.

As default the flux regulator is enabled. When disabled, the current regulator becomes de-tuned.

Do not disable this regulator. If you feel you need to disable this function, consult the factory for verification.

AC induction motors require flux to be established before controlled torque can be developed. To build flux, voltage is applied. There are two methods to flux the motor.

The first method is Automatic during a normal start. Flux is established as the output voltage and frequency are applied to the motor. While the flux is being established, the unpredictable nature of the developed torque can cause the rotor to oscillate even though acceleration of the load can occur. In the motor, the acceleration profile may not follow the commanded acceleration profile due to the lack of developed torque.

Figure 23 - Accel Profile during Normal Start - No Flux Up

<!-- image -->

The second method is Manual. In this mode, DC current is applied to the motor so that the flux is established before rotation. The flux up time period is based on the level of flux up current and the rotor time constant of the motor. The flux up current is not user adjustable.

Figure 24 - Flux Up Current versus Flux Up Time

<!-- image -->

Once rated flux is reached in the motor, normal operation begins and the desired acceleration profile is achieved.

<!-- image -->

Once rated flux is reached in the motor, normal operation begins and the desired acceleration profile is achieved.

## High Resolution Feedback

## Parameters

| File Group   |                                                                                                                                                                                                                                                                               | No. Display Name Full Name Description   | Values                                       | Read-WriteData Type   |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|----------------------------------------------|-----------------------|
|              | 43 Flux Up Enable Flux Up Enable “Manual” (0) – Flux is established for P44 [Flux Up Time] before initial acceleration. “Automatic” (1) – Flux is established for a calculated time period based on motor nameplate data before acceleration. P44 [Flux Up Time] is not used. | Default: Options:                        | 1 = “Automatic” 0 = “Manual” 1 = “Automatic” | RW 32-bit Integer     |
| MOTOR CONTROL Mtr Ctrl Options              | 44 Flux Up Time Flux Up Time The amount of time the drive will use to try to achieve full motor stator flux. When a Start command is issued, DC current at P26 [Motor NP Amps] level is used to build stator flux before accelerating.                                        | Units: Default: Min/Max:                 | Secs 0.0000 0.0000 / 5.0000                  | RW Real               |

## Applications

This function is usually associated with applications that require extended acceleration times. Out of the box, the drive is set to "Automatic" and attempts to get full motor stator flux based on motor nameplate information. In some cases the loading and ramp curve during acceleration could have an adverse affect on the drive's thermal manager. Some applications include mining conveyors or large centrifuges. This function gives you the ability to manually be sure the motor stator is fully fluxed up before acceleration by manually assigning a flux up time. It can produce a better acceleration at low frequencies without excessive current.

The Universal Feedback option module, PowerFlex 755 drives only, interpolates any sine/cosine signal into 1,048,576 counts per revolution.

The interpolation cannot be changed. It is 1,048,576 counts per revolution regardless of the native cycles per revolution of the sine/cosine. Interpolation is modified to 24 bits when P8 [FB0 Cfg] or P38 [FB1 Cfg] Bit 1 "24-bit Resol" is set.

An acceptable sine/cosine signal is a 1 volt peak-to-peak voltage with a 2.5 volt offset. Most feedback manufactures Sick (SSI), Stegmann (Hiperface), and Heidenhain (En Dat, non en dat) meet this requirement.

## Inertia Adaption

Inertia adaption is used to compensate for lost motion, which occurs when a gear box and/or a springy coupling is present. Lost Motion describes the condition in which an input to a mechanism creates no corresponding displacement at the output. This is most noticeable in systems with large inertia ratios using a gearbox or flexible couplings. The term inertia adaption refers to how this function adapts or changes the dynamic inertia seen by the speed regulator. Inertia adaption can allow an increase in the speed regulator bandwidth, normally limited by the mechanical transmission, by up to four times. This feature is only available on PowerFlex 755 drives. P35 [Motor Ctrl Mode] must be set to vector control and use a motor speed feedback device. Inertia adaption is not enabled by default.

For example, a motor connected to a gearbox is shown.

<!-- image -->

This gearbox can be represented by a spring (K) and gear backlash (BL).

<!-- image -->

When the speed of the motor increases, there is a period of time (represented by Δ x = backlash) before the teeth of the gearbox engage. After that time, there is some twisting (like a spring) in the shaft after the teeth of the gearbox engage. This lost motion causes mechanical instability and limits how high the speed regulator bandwidth can be set without causing instability. Inertia adaption detects the lost motion and a higher speed regulator bandwidth can be achieved without instability.

<!-- image -->

## Configuration

Inertia adaption only works if there is valid inertia value entered in P76 [Total Inertia]. Total inertia is measured during an assisted startup procedure executed from the HIM or software wizard. The inertia tune can be executed manually by setting P70 [Autotune] to option 4 "Inertia Tune" and starting the drive.

<!-- image -->

Activate inertia adaption by setting P704 [InAdp LdObs Mode] to option 1 "InertiaAdapt." Once activated, two filters are automatically updated, P705 [Inertia Adapt BW] and P710 [InertAdptFltrBW], when P636 [Speed Reg BW] is set to a non zero value. Gradually increase P636 [Speed Reg BW] while operating the motor and load. The final speed reg bandwidth exceeds the value before inertia adaption was activated providing the system meets the criteria mentioned below.

When Inertia adaption is activated, disable the two lead-lag filters present in the speed regulator (setting OFF). These filters are in the speed feedback path P637 [SReg FB Fltr Sel] and at the output of the speed regulator P657 [SReg OutFltr Sel]. Both filters are disabled by default.

The Inertia Adaption feature can be used in conjunction with inertia compensation to minimize the acceleration torque required from the Speed Regulator.

Refer to the PowerFlex 750-Series Programming Manual, publication 750PM001, for detailed parameter explanation.

## How does inertia adaption work?

- The inertia adaption algorithm uses a component of acceleration feedback to create a sort of electronic inertia.
- Electronic inertia supplements the inertia lost when the load is suddenly disconnected as through a gearbox or lost motion. In this way the velocity regulator does not see a dramatic change in inertia that is normally associated with load disconnect and potential instability.

## Inertia Compensation

## Where is inertia adaption applied?

- Any system with an inertia ratio greater than 3:1 that is plagued by gear noise or resonance that can't achieve desired performance by ordinary tuning. (Inertia ratio is the ratio of system inertia to motor inertia.)
- Most high performance tracking or electronic line shaft systems.
- Most geared systems requiring higher bandwidths and stiffness.

## What could be a disadvantage when using inertia adaption?

- It can generate a shrill noise with rigid couplings that lack lost motion or sufficient compliance. Do not use inertia adaption in such cases.
- It can produce a low level sound emanating from the motor. This is merely the inertia adaption in action and the sound does not affect performance nor does it harm the motor.

Inertia Compensation is active only in PowerFlex 755 drive and in Flux Vector (FV) motor control modes selected by P35 [Motor Ctrl Mode].

During speed changes, a certain level of torque to respond is required due to load inertia. That level of torque is above the torque used to run at constant speed. Inertia compensation attempts to predict the motor torque required to accelerate and decelerate an inertial load. The Inertia compensation function calculates a feed forward torque signal based on proportional acceleration or deceleration rate of change of speed input and total inertia, also known as the derivative of speed with respect to time. Then that P699 [Inertia Comp Out] signal torque can be fed forward into the torque control, becoming an available input to the P313 [Actv SpTqPs Mode] selector to be summed with P660 [SReg Output] making for smoother accelerations and decelerations, especially with high inertia loads.

<!-- image -->

- Parameter 695 [Inertia CompMode] enables the Inertia Compensation and selects possible velocity reference input sources of motor speed as follows:
- "Disabled" (0) – Inertia compensation function is disabled. P699 [Inertia Comp Out] is zero so the motor torque reference is not affected.

- "Int Ramp Ref " (1) – Inertia compensation is enabled. The function is configured to use the rate of change of P595 [Filtered Spd Ref ]. This is the typical setting that should be used for inertia compensation on a standalone drive.
- "Ext Ramp Ref " (2) – Inertia compensation is enabled. The function is configured to use the rate of change of P700 [Ext Ramped Ref ]. This setting is available for applications that supply a ramped speed reference external to the drive.
- "Spd Rate Ref " (3) – Inertia compensation is enabled. The function is configured to use the P596 [Speed Rate Ref ]. This parameter should contain a value that represents the rate of change of the motor speed reference. This setting is available for applications that supply a ramped speed reference external to the drive.

Parameter 76 [Total Inertia] is calculated during the autotune and is used along with the calculated acceleration or deceleration rate to calculate the torque adder.

Parameter 696 [Inertia Acc Gain] determines the gain for the inertia compensation during acceleration. A gain of 1 results in 100% compensation.

Parameter 697 [Inertia Dec Gain] determines the gain for the inertia compensation during deceleration. A gain of 1 results in 100% compensation.

Parameter 698 [Inertia Comp LPFBW] Inertia Compensation Low Pass Filter Bandwidth. Sets the bandwidth of a low pass filter for the inertia compensation function. The output of this filter supplies P699.

Parameter 699 [Inertia Comp Out] Inertia Compensation Output. Displays the output of the inertia compensation function.

Parameter 700 [Ext Ramped Ref ] External Ramped Reference. This parameter is meant for an external motor speed ramp input signal. This signal will be used by the inertia compensation function when P695 [Inertia CompMode] = 2 "Ext Ramp Ref." This parameter will be entered in units of Hz or RPM, depending on the value of P300 [Speed Units].

Parameter 596 [Speed Rate Ref ] Speed Rate Reference. This parameter is shared by both the Inertia Compensation and Speed Compensation functions.

A value shared by both the Inertia Compensation and Speed Compensation functions (active only in FV motor control modes), typically supplied by an external controller that is also providing a rate limited speed reference. The Speed Rate Reference corresponds to the derivative with respect to time of the speed reference signal. Units of time are in seconds.

For example, if the controller provides a 10 second reference ramp, the controller would also supply a Speed Rate Ref value of 1 pu / 10 sec = 0.1 sec-1 while the reference is accelerating. When the reference is constant, Speed Rate Ref should be zero.

For additional illustration of the control refer to PF755 Control Block Diagrams in the PowerFlex 750-Series Programming Manual, publication 750-PM001 .

## Load Observer

The PowerFlex 755 load observer feature compensates for and greatly reduces load disturbances and gives quicker system response. It minimizes the load torque requirements of the speed regulator. The load observer attempts to determine a load estimate value that matches the load torque present in the simplified load model. This is a simplified motor/load model.

<!-- image -->

From a control point of view, load torque is an input that is just as real as velocity reference, but lacks a parameter. Load torque is unavoidable because it is effectively torque times speed that creates the power to run a load. Considering this load model, the applied torque is the electromagnetic torque generated by the motor control and load torque is clearly shown. M is the combined motor/ load mass (inertia). The applied torque must be greater than the load torque to accelerate the system.

Load torque is not a parameter and thus is not directly accessible, but it can be indirectly measured. Referring to the plant model we can directly measure the applied torque, output velocity and the inertia is generally known or calculated. This leaves load torque as the only unknown value. If we place all three known quantities in a box that we call an observer, load torque can be estimated.

As the output of the load observer is added to the output of the speed regulator the function minimizes the load torque requirement for the output of the speed regulator. Because load observer affects the torque reference and the acceleration feedback is required, this method can only be applied on P35 [Motor Ctrl Mode] Flux Vector control modes with motor feedback device. This feature is available only on PowerFlex 755 drives.

<!-- image -->

## Motor Control Modes

## Configuration

Enable Load Observer by setting P704 [InAdp LdObs Mode] to 2 "LoadObserver." The total inertia value P76 [Total Inertia] is required for this feature. Ideally it is measured during the inertia test as part of the drive startup. The next best approach is to manually enter a reasonably close (calculated) value. In Load Observer mode, P711 [Load Observer BW] is used to set the natural frequency of a low pass filter in radians per second (R/S). Typical values for Load Observer Bandwidth range from 10 to 150 with the higher values being more responsive to disturbances but with increased system noise. There is no nominal best setting, but 40 R/S is a suggested starting point. This selection may not function well in sloppy geared systems. Unlike with Inertia Adaption, there is no automatic parameter setting associated with the Load Observer.

The Load Observer can also be used in conjunction with P695 [Inertia CompMode]. When used together, both the load torque and acceleration torque required from the speed regulator are minimized.

## Where can Load Observer be used?

Load Observer can be used on systems where load disturbances are preventing a further increase in drive performance. The Load Observer can be applied to both periodic load disturbances, such as a piston pump, and random load disturbances. Load observer can be applied on systems that are not suitable for Inertia Adaption. Load Observer cannot be active at the same time as Inertia Adaption.

P35 [Motor Ctrl Mode] selects the output mode of the drive to match the type of motor control to use. The Default selection is a value of 1 = "Induction SV." This parameter is set during any of the assisted start up routines either via the HIM or connected software tool wizard. The parameter settings follow.

- InductionVHz (0) – Induction motor, volts per Hertz control mode. Connected to an induction motor. Used for variable torque applications with improved efficiency energy savings and variable speed constant torque applications such as conveyors. Can also be used in multi-motor or synchronous motor applications.
- Induction SV (1) – Induction motor, sensorless vector control mode. Connected to an induction motor. Used for most constant torque applications. Provides excellent starting, acceleration, and running torque.
- Induct Econ (2) – Induction motor, economize control mode. Used for additional energy savings in constant torque applications that have constant speed reduced load periods.

- Induction FV (3) – Induction motor, flux vector control mode. Connected to an induction motor. Used when high performance precise speed regulation and/or position control closed loop is required. Can also be configured with direct Torque Reference input. Can also be used open loop with less precision.
- PM VHz (4) – Permanent magnet motor, volts per Hertz control mode. Connected to a Surface Permanent Magnet motor (SPM) or Permanent Magnet Synchronous Motor (PMSM). Used for variable torque applications with improved efficiency energy savings and variable speed constant torque applications such as conveyors. Also used in multi-motor or synchronous motor open loop applications.
- PM SV (5) – Permanent magnet motor, sensorless vector control mode. Connected to a Surface Permanent Magnet motor (SPM) or Permanent Magnet Synchronous Motor (PMSM). Used for constant torque applications. Provides excellent starting, acceleration, and running torque.
- PM FV (6) – Permanent magnet motor, flux vector control mode. Connected to a Surface Permanent Magnet motor. Used when high performance precise speed regulation and/or position control closed loop is required. Can also be configured with direct Torque Reference input. Can also be used open loop with less precision.
- SyncRel VHz (7) – Synchronous Reluctance motor, volts per Hertz control mode.

Connected to a Synchronous Reluctance motor. Used for constant torque applications with improved efficiency energy savings and variable speed applications such as conveyors. Used in multi-motor applications.

- SyncRel SV (8) – Synchronous Reluctance motor, sensorless vector control mode.

Connected to a Synchronous Reluctance motor. Used for constant torque applications with improved efficiency energy savings and variable speed applications such as conveyors. Avoid slow speed low inertia applications that cause torque ripple effects.

- Adj VltgMode (9) – Adjustable voltage control mode. Independent Frequency and Voltage regulators; Fixed Frequency and Variable Voltage or Fixed Voltage and Variable Frequency. Typically used for non-motor applications such as resistive and inductive heating elements, vibration welding, power supplies, Electromagnetic stirring of molten metal and some Linear Induction Motor LIM applications.
- IPM FV (10) – Interior permanent magnet motor, flux vector control mode.

Connected to an Interior Permanent Magnet motor. Used when high performance precise speed regulation and/or position control with closed loop feedback is required. Can also be configured with direct Torque Reference input. Can also be used open loop with less precision.

## Volts/Hertz

Volts/Hertz operation creates a fixed relationship between output voltage and output frequency. Volts/Hertz works the same for Permanent Magnet and SyncRel VHz as it does for induction VHz. The relationship can be defined in two ways by setting P65 [VHz Curve] to 0 "Custom V/Hz" or 1 "Fan/Pump."

<!-- image -->

## 0 = "Custom V/Hz"

Custom Volts/Hertz enables a wide variety of patterns using linear segments. The default configuration is a straight line from zero to rated voltage and frequency. This is the same volts/hertz ratio that the motor sees if started across the line. As seen in the diagram below, the volts/hertz ratio can be changed to provide increased torque performance when required by programming five distinct points on the curve.

- P60 [Start Acc Boost] - Used to create additional torque for breakaway from zero speed and acceleration of heavy loads at lower speeds.
- P61 [Run Boost] - Used to create additional running torque at low speeds. The value is typically less than the required acceleration torque. The drive will lower the boost voltage to this level when running at low speeds (not accelerating). This reduces excess motor heating that could be caused if the higher start / accel boost level were used.
- P62 [Break Voltage] and P63 [Break Frequency] - Used to increase the slope of the lower portion of the Volts/Hertz curve, providing additional torque.
- P25 [Motor NP Volts] and P27 [Motor NP Hertz] - Set the upper portion of the curve to match the motor design. Marks the beginning of the constant power region.
- P36 [Maximum Voltage] and P37 [Maximum Frequency] - Slope the portion of the curve used above base speed.

<!-- image -->

## 1 = "Fan/Pump"

When this option is chosen, the relationship is 1/x2. Therefore, at full frequency, full voltage is supplied. At 1/2 rated frequency, 1/4 voltage is applied. This pattern closely matches the torque requirement of a variable torque load (centrifugal fan or pump – load increases as speed increases) and offers the best energy savings for these applications.

<!-- image -->

## Sensorless Vector

Sensorless Vector mode uses a V/Hz core enhanced by excellent current resolution, a slip estimator, a high performance current limiter and the vector algorithms. The basic functions for SV are similar for all three motor types, induction motor, permanent magnet motor, and synchronous reluctance motor, however PM and SyncRel SV do not require Slip Frequency adjustments.

## IM Sensorless Vector

<!-- image -->

## PM and SyncRel Sensorless Vector

<!-- image -->

The algorithms operate on the knowledge that motor current is the vector sum of the torque and flux producing components of current. Values can be entered to identify the motor values or an autotune routine can be run to identify the motor values (see Autotune on page 35). Sensorless vector offers better torque production and a wider speed range than V/Hz. However, it is not appropriate to use when more than one motor is connected to the same drive.

In Sensorless Vector control, the drive commands a specific amount of voltage to develop flux.

<!-- image -->

## Sensorless Vector w/Economizer

Economizer mode consists of the Sensorless Vector control with an additional energy savings function. When steady state speed is achieved, the economizer becomes active and automatically adjusts the drive output voltage based on applied load. By matching output voltage to applied load, the motor efficiency is optimized. Reduced load commands a reduction in motor flux current. The flux current is reduced as long as the total drive output current does not exceed 75% of motor rated current as programmed in P26 [Motor NP Amps]. The flux current is not allowed to be less than 50% of the motor flux current as programmed in P75 [Flux Current Ref ]. During acceleration and deceleration,

the economizer is inactive and Sensorless Vector motor control performs normally.

<!-- image -->

## Flux Vector Control

In Flux Vector mode, the flux and torque producing currents are independently controlled and speed is indirectly controlled by a torque reference. Alternatively, the drive can control torque instead of speed in flux vector mode. In either case, this mode can be operated either with or without feedback and will provide the fastest response to load changes.

Flux Vector control is used with AC squirrel cage induction motors for high performance. Motor data and an autotune is required for correct operation in this mode (refer to Autotune on page 35 for details). In Flux Vector control, the drive takes the speed reference that is specified by the Speed Reference Selection block and compares it to the speed feedback. The speed regulator uses Proportional and Integral gains to adjust the torque reference for the motor. This torque reference attempts to operate the motor at the specified speed. The torque reference is then converted to the torque producing component of the motor current.

This type of speed regulator produces a high bandwidth response to speed command and load changes. Because Flux Vector controls the flux and torque producing currents independently, a torque reference can be sent directly instead of being generated from a speed reference via the Speed Regulator. The independent flux control also enables flux to be reduced in order to run above base motor speed.

## Flux Vector

<!-- image -->

## Permanent Magnet Motor Control

Permanent magnet motor control is selected by setting P35 [Motor Ctrl Mode] to the appropriate choices of motor type. Refer to Appendix D of the PowerFlex 750-Series Programming Manual, publication 750-PM001 for compatible list of Allen-Bradley Servo motors and resolution criteria.

Surface Permanent Magnet (SPM) motor or Permanent Magnet Synchronous Motor (PMSM) is a rotating electrical machine that has the stator phase windings and rotor permanent magnets. The air gap magnetic field is provided by these permanent magnets and hence it remains constant. The conventional DC motor commutates itself with the use of a mechanical commutator whereas SPM/PMSM needs electronic commutation for the direction control of current through the windings. Because the SPM/PMSM motors in effect have their armature coils at the stator, they need to be commutated externally with the help of an external switching circuit. A three phase PWM inverter topology is used for this purpose.

The torque is produced because the interaction of the magnetic fields causes the rotor to rotate. In permanent magnet motors, one of the magnetic fields is created by permanent magnets and the other is created by the stator coils. The maximum torque is produced when the magnetic vector of the rotor is at 90 degrees to the magnetic vector of the stator.

Motor data and an autotune are required for correct operation in this mode. Refer to Autotune on page 35 for details.

## PM Sensorless Vector

<!-- image -->

## PM Flux Vector Control

In flux vector mode, the flux and torque producing currents are independently controlled and speed is indirectly controlled by a torque reference. Alternatively, the drive can also control torque instead of speed in flux vector mode. In either case, this mode can be operated either with or without feedback and will provide the fastest response to load changes.

High Performance and precise control will require encoder feedback. Refer to the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001, for a list of compatible High Resolution Stegmann encoder and Heidenhain encoder feedback on the motor.

High Bandwidth Current Regulator

<!-- image -->

## IPM Flux Vector Control

In IPM Flux Vector mode, the flux and torque producing currents continue to be independently controlled. Speed is indirectly controlled by a torque reference output command from the Speed Regulator. Alternatively, the drive can be configured to control torque instead of speed in flux vector mode. In either case, for precise control, this mode must be operated with encoder feedback in order to provide the fastest response to load changes.

The Iq/Id reference calculation block will produce optimum Iq/Id current reference that will try to establish maximum torque per amp control performance.

## IPM Flux Vector

<!-- image -->

## Motor Types

The following explanation and descriptions of AC motor types are condensed summaries derived from a variety of sources that focus on the history, evolution, and feature benefits of the variety of motor designs. These designs are utilized in all sectors of use and in vast variations of machinery, equipment, and processes.

The types of AC motors described here, powered by fixed utility frequency, are limited to speeds based on the number of poles and winding construction. Variable Frequency Drives (VFDs) broaden practical speed ranges of these motor types by converting utility power and applying appropriately selected VFD electronic control modes specifically matched to these unique motor type designs. Motor control modes set by P35 [Motor Ctrl Mode] are also discussed in Motor Control Modes on page 226 and the PowerFlex 750-Series Programming Manual, publication 750-PM001 .

The following topics are briefly discussed in this section.

- Basics of AC Motor Design
- Induction AC Motors
- Wound-rotor AC Motors
- Multispeed AC Motors
- Synchronous AC Motors
- Permanent Magnet Motor Control
- Synchronous reluctance motors
- AC Linear Electric Motors (LIMs)

## Basics of AC Motor Design

AC motors come in a variety of designs, each with functional purpose and benefits. Asynchronous and synchronous electric motors are the two main categories of AC motors.

The Induction AC motor is a common form of asynchronous motor and is basically an AC transformer with a rotating secondary. The primary winding (stator) is connected to the power source and the shorted secondary (the rotor) carries the induced secondary current. Torque is produced by the action of the rotor (secondary) currents on the air-gap flux. The synchronous motor differs greatly in design and operational characteristics, and is considered a separate class of AC motor.

## AC Induction Motors

P35 [Motor Ctrl Mode] induction motor options.

- 0 = "Induction VHz"
- 1 = "Induction SV"
- 2 = "Induction Econ"
- 3 = "Induction FV"

AC Induction Motors (ACIMs) are the simplest and most rugged electric motor and consist of two basic electrical assemblies: the wound stator and the rotor assembly. The induction AC motor derives its name from currents flowing in the secondary member (rotor) that are induced by alternating currents flowing in the primary member (stator). The combined electromagnetic effects of the stator and rotor currents produce the force to create rotation.

ACIMs typically feature rotors, which consist of a laminated, cylindrical iron core with slots for receiving the conductors. The most common type of rotor has cast-aluminum conductors and short-circuiting end rings. This AC motor "squirrel-cage" rotates when the moving magnetic field induces a current in the shorted conductors. The speed at which the AC motor magnetic field rotates is the synchronous speed of the AC motor and is determined by the number of poles in the stator and the frequency of the power supply: ns = 120f/p, where ns = synchronous speed, f = frequency, and p = the number of poles (that is 120*60 Hz] / 4 = 1800 RPM). To control motor speed other than the fixed utility frequency requires a VFD.

Synchronous speed is the absolute upper limit of AC motor speed. If the AC motor's rotor turns exactly as fast as the rotating magnetic field, then no lines of force are cut by the rotor conductors, and torque is zero. When AC induction motors are running, the rotor always rotates slower than the magnetic field. The AC motor's rotor speed is just slow enough to cause the proper amount of rotor current to flow, so that the resulting torque is sufficient to overcome windage and friction losses, and drive the load. The speed difference between the AC motor's rotor and magnetic field, called slip, is normally referred to as a percentage of synchronous speed: s = 100 (ns - na)/ns, where s = slip, ns = synchronous speed, and na = actual speed. Or it is listed on the nameplate as a base speed (1780 RPM) at rated FLA, frequency, and based on the number of poles.

## Polyphase AC Induction Motors

Polyphase squirrel-cage AC motors are basically constant-speed machines, but some degree of flexibility in operating characteristics results from modifying the rotor slot design. These variations in AC motors produce changes in torque, current, and full-load speed. Evolution and standardization have resulted in four fundamental types of AC motors.

There are five basic NEMA designs for AC motors: A, B, C, D, and F. The speedtorque curves for all five designs are shown on the following graph.

<!-- image -->

AC Motors - Designs A and B are general-purpose AC motors with normal starting torques and currents and low slip. As shown, the characteristics of designs A and B are quite similar. The primary difference between these two designs is that the starting current for design B is limited by NEMA standards, but there is no limitation on the starting current for design A.

AC Motors - Design C have high starting torque with normal starting current and low slip. NEMA design C motor has a higher starting torque than either the A or B designs. This torque is in the vicinity of 225% of full-load torque. Design C AC motors are normally used where breakaway loads are high at starting, but which normally run at rated full load and are not subject to high overload demands after running speed has been reached.

AC Motors - Design D exhibit high slip AC motor starting torque, which is approximately 280% of full-load torque, low starting current, and low full-load speed. Because of the high slip, speed can drop when fluctuating loads are encountered. The high starting torque of the design D motor makes it

particularly suited to handle hard-to-start loads. Another useful characteristic of this motor is the sloping shape of its speed-torque curve. This lets the motor slow down during periods of peak loads, enabling any flywheel energy that has been stored by the load to be released. Typical applications include punch presses and press brakes.

AC Motors - Design F exhibit low starting torque, low starting current, and low slip. These AC motors are built to obtain low locked-rotor current. Both lockedrotor and breakdown torque are low. Normally these AC motors are used where starting torque is low and where high overloads are not imposed after running speed is reached.

In summary, we see that when matching an AC motor to the requirements of a specific load it is important to check the torque requirements of the load and the torque capabilities of the motor in addition to speed and horsepower.

At least three torque values are important:

- Starting torque
- Breakdown torque
- Full-load torque.

## Wound-rotor AC Motors

P35 [Motor Ctrl Mode] induction motor options.

- 0 = "Induction VHz"
- 1 = "Induction SV"
- 3 = "Induction FV"

Squirrel-cage AC motors are relatively inflexible with regard to speed and torque characteristics, but a special wound-rotor AC motor has controllable speed and torque. Application of wound-rotor AC motors is markedly different from squirrel-cage AC motors because of the accessibility of the rotor circuit. AC motor performance characteristics are obtained by inserting different values of resistance in the rotor circuit.

Wound-rotor AC motors are generally started with secondary resistance in the rotor circuit. The AC motor resistance is sequentially reduced to permit the motor to come up to speed. Thus, AC motors can develop substantial torque while limiting locked-rotor current. This secondary AC motor resistance can be designed for continuous service to dissipate heat produced by continuous operation at reduced speed, frequent acceleration, or acceleration with a large inertia load. External resistance gives AC motors a characteristic that results in a large drop in rpm for a fairly small change in load. Reduced AC motor speed is provided down to about 50% rated speed, but efficiency is low.

Retrofitting a Wound-rotor motor with a VFD is possible by eliminating the switching and resistor control infrastructure and shorting the slip rings

connected to the rotor windings. CAUTION! Because wound-rotor motors were not originally designed for use with inverters, the dielectric strength of the motor construction cannot withstand the reflected wave voltages that can get subjected at the motor connections (1.5 to 2.5 times drive's bus voltage). Appropriate mitigation must be considered. General rule of thumb, size the VFD so that it is capable of providing continuous current at 125 to 135% of FLA of the motor, due to elimination of resistors and its design for higher starting torque.

## Multispeed AC Motors

P35 [Motor Ctrl Mode] induction motor options.

- 0 = "Induction VHz"
- 1 = "Induction SV"
- 3 = "Induction FV"

Consequent-pole AC motors are designed for one speed. By physically reconnecting the leads, a 2:1 speed ratio can be obtained. Typical synchronous speeds for 60 Hz AC motors are: 3,600/1,800 rpm (2/4 pole), 1,800/900 rpm (4/8 pole), and 1,200/600 rpm (6/12 pole).

Two-winding AC motors have two separate windings that can be wound for any number of poles so that other speed ratios can be obtained. However, ratios greater than 4:1 are impractical because of AC motor size and weight.

Power output of multispeed AC motors can be proportioned to each different speed. These AC motors are designed with output horsepower capacity in accordance with one of the load characteristics.

When retrofitted with a VFD, the motor is generally wired for the speed range intended to be optimized. Autotuned per representative nameplate information and operated as a single winding single speed induction motor.

## Synchronous AC Motors

P35 [Motor Ctrl Mode] induction motor options.

- 0 = "Induction VHz"

Synchronous AC motors are inherently constant-speed electric motors and they operate in absolute synchronism with line frequency. As with squirrel-cage induction AC motors, speed is determined by the number of pairs of poles and is always a ratio of the line frequency.

Synchronous AC motors are made in sizes ranging from sub-fractional selfexcited units to large-horsepower, direct-current-excited AC motors. In the fractional-horsepower range, synchronous AC motors are used primarily where precise constant speed is required.

In large horsepower sizes applied to industrial loads, synchronous AC motors serve two important functions. First, AC motors provide highly efficient means of converting AC energy to mechanical power. Second, AC motors can operate at leading or unity power factor, thereby providing power-factor correction.

There are two major types of synchronous AC motors: non-excited and directcurrent excited electric motors. Application of a VFD is to vary the desired synchronous speed of the machine.

## Permanent Magnet Motor Control

Permanent magnet motor control is selected by setting P35 [Motor Ctrl Mode] to the appropriate choices of motor type. Refer to the PowerFlex 750-Series Programming Manual, publication 750-PM001, Appendix D for compatible List of Allen-Bradley Servo motors and resolution criteria.

## Surface Permanent Magnet Motor (SPM) or Permanent Magnet Synchronous Motor (PMSM)

P35 [Motor Ctrl Mode] induction motor options.

- 4 = "PM VHz"
- 5 = "PM SV"
- 6 = "PM FV"

SPM or PMSM is a rotating electrical machine that has the stator phase windings and rotor permanent magnets. The air gap magnetic field is provided by these permanent magnets therefore it remains constant.

The conventional DC motor commutates itself with the use of a mechanical commutator whereas SPM / PMSM needs electronic commutation for the direction control of current through the windings. Because the SPM/PMSM motors in effect have their armature coils at the stator, they need to be commutated externally with the help of an external switching circuit. A three phase PWM inverter (VFD) topology is used for this purpose.

The torque is produced because the interaction of the magnetic fields causes the rotor to rotate. In permanent magnet motors, one of the magnetic fields is created by permanent magnets and the other is created by the stator coils. The maximum torque is produced when the magnetic vector of the rotor is at 90 degrees to the magnetic vector of the stator.

Motor data and an autotune are required for correct operation in this mode. Refer to Autotune on page 35 for details on the autotune.

The permanent magnet synchronous motor (PMSM) can be thought of as a cross between an AC induction motor and a brushless DC motor (BLDC). They have

rotor structures similar to BLDC motors which contain permanent magnets. However, their stator structure resembles that of its ACIM cousin, where the windings are constructed in such a way as to produce a sinusoidal flux density in the air gap of the machine. As a result, they perform best when driven by sinusoidal waveforms. However, unlike their ACIM relatives, PMSM motors perform poorly with open-loop scalar V/Hz control, because there is no rotor coil to provide mechanical damping in transient conditions.

Field Oriented Control is the most popular control technique used with PMSMs. As a result, torque ripple can be extremely low, on par with that of ACIMs. PMSM motors provide higher power density for their size compared to ACIMs. This is because with an induction machine, part of the stator current is required to "induce" rotor current in order to produce rotor flux. These additional currents generate heat within the motor. In a PMSM, the rotor flux is already established by the permanent magnets on the rotor.

Most PMSMs utilize permanent magnets which are mounted on the surface of the rotor. This makes the motor appear magnetically "round," and the motor torque is the result of the reactive force between the magnets on the rotor and the electromagnets of the stator. This results in the optimum torque angle being 90 degrees, which is obtained by regulating the d-axis current to zero in a typical FOC application.

## Interior Permanent Magnet Motor

P35 [Motor Ctrl Mode] induction motor options.

- 10 = "IPMn VHz"

Some PMSMs have magnets that are buried inside of the rotor structure. These motors are called Interior Permanent Magnet, or IPM motors. As a result, the radial flux is more concentrated at certain spatial angles than it is at others. This gives rise to an additional torque component called reluctance torque, which is caused by the change of motor inductance along the concentrated and nonconcentrated flux paths.

This causes the optimum Field Oriented Control torque angle to be greater than 90 degrees, which requires regulating the d-axis current to be a fixed negative ratio of the q-axis current. This negative d-axis current also results in field weakening, which reduces the flux density along the d-axis, which in turn partially lowers the core losses. As a result, IPM motors boast even higher power output for a given frame size.

Motor data and an autotune are required for correct operation in this mode. Refer to Autotune on page 35 for details on the autotune.

These motors are becoming increasingly popular as traction motors in hybrid vehicles, as well as variable speed applications for appliances and HVAC. In the servo motor world more and more designs are shifting away from SPM to IPM to

take advantage of inherent advantages. In principle, there are no size limitations to IPM designs and these can be developed from small fractional horsepower to large – hundreds of Hp ratings, creating potential applications that can benefit from variable speed IPM control.

## Synchronous Reluctance Motors

P35 [Motor Ctrl Mode] induction motor options.

- 7 = "SyncRel VHz"
- 8 = "SyncRel SV"

Synchronous reluctance motors have an equal number of stator and rotor poles. The projections on the rotor are arranged to introduce internal flux "barriers," holes which direct the magnetic flux along the so-called direct axis. Typical numbers of poles are 4 and 6. Following example of a 4 pole rotor and 6 pole stator.

As the rotor is operating at synchronous speed and there are no currentconducting parts in the rotor, rotor losses are minimal compared to those of an induction motor, thus potential energy savings in appropriate applications. Once started and rotating at synchronous speed, the motor can operate with sinusoidal voltage. So to start and control speed at frequencies other than utility requires a variable-frequency drive.

## AC Linear Electric Motors LIMs and LSMs

P35 [Motor Ctrl Mode] induction motor options.

- 0 = "Induction VHz"
- 9 = "Adjustable Voltage"

The first linear electric motor was conceived by Wheatstone more than 100 years ago. But large air gaps and low efficiencies prevented linear electric motors from being widely used until recent advances in design and VFD controls.

## Linear Induction Motors (LIMs)

In a LIM, the motor stator creates an Alternating Current (AC) field that induces currents into the reaction plate (moving element), which is typically an aluminum fin or plate. This creates eddy currents in the moving element which react with the moving field in the stator to produce thrust. LIMs typically are kept moving, avoiding holding stationary (equivalent to locked rotor) because of significant heating of the reactor plate.

A linear electric motor in concept has rotary electric motor stator cores, unrolled out over a linear path. The circular stator becomes a linear stator, being defined as a single-sided linear induction electric motor (SLIM). Likewise, if the circular stator is cut into two sections and flattened, the electric motor becomes a doublesided linear induction electric motor (DLIM). The DLIM and SLIM both require a two or three-phase stator (primary) winding and a flat metallic or conductive plate-type armature (secondary) instead of a rotor.

The moving member in a linear induction motor is typically a solid conducting plate or sheet. It does not contain coils or windings. However, a linear electric motor can also be constructed so the primary moves and the secondary remains stationary.

Linear induction motors LIMs are increasingly chosen for material-handling applications and Amusement rides because they are quieter, more reliable, and less expensive than rotary electric motors. And because linear electric motors do not drive gearboxes or rotary-to-linear conversion devices, they can be more efficient.

There are several important differences between linear and rotary electric induction motors that require understanding. Unlike rotary electric motors, the linear motor has a beginning and an end to its travel. First, the moving secondary material enters the primary (stator field) at one end of the electric motor and exits at the opposite end. Induced currents in the secondary material at the entry edge resist air-gap flux buildup. And at the exit edge, the material retards the air-gap flux decay. This results in an uneven air-gap flux distribution which contribute to challenges in sizing VFDs and optimizing set up of control frequency and voltage. VFD control uses either fixed V/Hz, or independently controlled frequency and voltage.

## Linear Synchronous Motors (LSMs)

Linear Synchronous Motors (LSMs) are significantly different than Linear Induction Motors (LIMs) in the way that they produce electromotive forces or motion.

Linear Synchronous Motors (LSMs) are similar in concept with stator cores, arranged along a path for motion, rather than contained in a frame for rotary motion. But the field in a LSM moving secondary element is usually provided by permanent magnets. There are no significant currents induced. Magnets are embedded in the moving element. This does allow for more definitive position control and holding position without excessive heat generation. Generally some sort of position sensor and feedback are necessary to implement control of LSMs via VFD are necessary.

At the time of this writing there has been minimal experience applying VFDs to control Linear Synchronous Motors (LSMs). Only this short description of its construction is included.

## Notch Filter

A notch filter exists in the torque reference loop to reduce mechanical resonance created by a gear train. P687 [Notch Fltr Freq] sets the center frequency for the 2 pole notch filter, and P688 [Notch Fltr Atten] sets the attenuation of the notch filter in the vector control torque reference section. Attenuation is the ratio of the notch filter input signal to its output at the P687 [Notch Fltr Freq]. An attenuation of 30 means that the notch output is 1/30th of the input at the specified frequency.

The notch filter is valid only in Flux Vector Motor Control modes (P35).

Figure 25 - Notch Filter Frequency

<!-- image -->

## Example

A mechanical gear train consists of two masses (the motor and the load) and spring (mechanical coupling between the two loads).

Mechanical Gear Train

<!-- image -->

The resonant frequency is defined by the following equation:

<!-- formula-not-decoded -->

- Jm is the motor inertia (seconds)
- Jload is the load inertia (seconds)
- Kspring is the coupling spring constant (rad2 / sec)

The following graph shows a two mass system with a resonant frequency of 62 radians/second (9.87 Hz). One Hertz is equal to 2p radians/second.

Figure 26 - Resonance

<!-- image -->

The following represents the same mechanical gear train but with [Notch Filter Freq] set to 10.

Figure 27 - 10 Hz Notch

<!-- image -->

To see the effects of the notch filter use test points T65 and T73 in torque control. T65 is before the filter and T73 after. And test point Txx (before) and Txx (after) in position control. See the partial block diagram below.

<!-- image -->

## Regen Power Limit

The P426 [Regen Power Lmt] is programmed as a percentage of the rated power. The mechanical energy that is transformed into electrical power during a deceleration or overhauling load condition is clamped at this level. Without the proper limit, a bus overvoltage can occur. When using the bus regulator [Regen Power Lmt] can be left at factory default, -50%.

When using dynamic braking or a regenerative supply, [Regen Power Lmt] can be set to the most negative limit possible (–800%). When you have dynamic braking or regenerative supply, but want to limit the power to the dynamic brake or regenerative supply, [Regen Power Lmt] you can set a specific level. Values in this parameter are valid only in a Flux Vector mode.

The following series of plots describes the difference between changing Regen Power Limit versus changing the Negative Torque Limit. The beginning part of every plot is identical, this is the acceleration of the motor. Once the stop is commanded and deceleration begins, note the red trace in each. This represents torque current. Because power is proportional to speed, as the speed decreases, the torque current increases allowing more power to be dissipated.

Note the speed feedback in the RPL = -20%, the slower the motor gets the faster it's brought to zero speed and the torque current increases. The higher the value in Regen Power Limit the more power is allow to pass through.

Focus on the torque current (red) trace as you scroll through the plots and note the change in the shape as the regen power limit was increase. Then see how it is clamped at a particular level when Negative Torque Limit is changed.

<!-- image -->

<!-- image -->

RPL = 100%

<!-- image -->

<!-- image -->

NTL = -20%

<!-- image -->

<!-- image -->

NTL = -100%

<!-- image -->

## Speed Reference

The speed reference can come from a variety of sources. Some can be selected through digital inputs or via bit manipulation of the Network Logic Command Word:

- HIM (local or remote)
- Analog Input
- Preset Speed Parameters
- Jog Speed Parameters
- Auxiliary Velocity Feedback
- Network Communication
- Process PID Loop
- MOP Reference
- DeviceLogix software

Figure 28 - PowerFlex 753 Speed Reference Selection Overview

<!-- image -->

Refer to the PowerFlex 750-Series Programming Manual, publication 750PM001, Appendix A for more details on the PowerFlex 753 Control Block Diagrams.

Figure 29 - PowerFlex 755 Speed Reference Selection Overview

<!-- image -->

Refer to the PowerFlex 750-Series Programming Manual, publication 750PM001, Appendix A, for more details on the PowerFlex 755 Control Block Diagrams.

## Network Reference

Speed Reference A is the normal speed reference used. To choose a source for this reference, make a selection in P545 [Spd Ref A Sel]. Also, when the network (Logic Command Word) is used as the speed reference, refer to the following documentation for details of operation:

- PowerFlex 750-Series AC Drives Programming Manual, 750-PM001
- PowerFlex 755 Drive Embedded EtherNet/IP Adapter User Manual, 750COM-UM001
- PowerFlex 20-750-ENETR Dual-port EtherNet/IP Option Module User Manual, 750COM-UM008
- EtherNet/IP Network Configuration User Manual, ENET-UM001

The Reference is a 32-bit REAL (floating point) piece of control data produced by the controller and consumed by the adapter. The Feedback is a 32-bit REAL (floating point) piece of status data produced by the adapter and consumed by the controller.

When using a ControlLogix controller, the 32-bit REAL Reference is always DINT 1 in the output image and the 32-bit REAL Feedback is always:

- DINT 1 in the input image when using the drive Add-On Profile.
- DINT 2 when using the Generic Profile.

For a PLC-5®, SLC™ 500 or MicroLogix™ 1100/1400 controller, the 32-bit REAL Reference word is always words 2 (Least Significant Word) and 3 (Most Significant Word) in the output image and the 32-bit REAL Feedback is always words 2 (Least Significant Word) and 3 (Most Significant Word) in the input image.

When using a drive Add-On Profile, the Reference and Feedback are automatically formatted properly and displayed as a controller tag. When using the Generic Profile, the I/O image is integer-based and the Reference and Feedback are floating point. Because of this, a COP (Copy) instruction or User Defined Data Type (UDDT) is required to correctly write values to the Reference and read values from the Feedback. Refer to the PowerFlex 755 Embedded EtherNet/IP Adapter User Manual or to the PowerFlex 20-750ENETR Dual-port EtherNet/IP Option Module User Manual for ladder logic program examples.

When using the drive Add-On Profile, the controller tags for Reference and Feedback are automatically and properly formatted. This eliminates the need for data conversion using COP (copy) instructions or a UDDT to copy the DINT data into a REAL word.

The Reference and Feedback 32-bit REAL value represents drive speed. The scaling for the speed Reference and Feedback is dependent on drive P300 [Speed Units]. For example, if P300 is set to Hz, a 32-bit REAL Reference value of 30.0 equals a Reference of 30.0 Hz. If P300 is set to RPM, a 32-bit REAL Reference value of 1020.5 equals a Reference of 1020.5 RPM. Note that the commanded maximum speed can never exceed the value of drive P520 [Max Fwd Speed]. Table 12 shows example References and their results for a PowerFlex 755 drive that has its:

- P300 [Speed Units] set to Hz.
- P37 [Maximum Freq] set to 130 Hz.
- P520 [Max Fwd Speed] set to 60 Hz.

When P300 [Speed Units] is set to RPM, the other parameters are also in RPM.

Table 12 - PowerFlex 755 Drive Example Speed Reference/Feedback Scaling

| Network Reference Value Speed Command Value   | (2)     |                       | Output Speed Network Feedback Value   |
|-----------------------------------------------|---------|-----------------------|---------------------------------------|
|                                               |         | 130.0 130 Hz 60 Hz(3) | 60.0                                  |
| 65.0                                          | 65 Hz   | 60 Hz(3)              | 60.0                                  |
| 32.5                                          | 32.5 Hz | 32.5 Hz 32.5          |                                       |
| 0.0                                           | 0 Hz    | 0 Hz                  | 0.0                                   |
| -32.5(1)                                      | 32.5 Hz | 32.5 Hz 32.5          |                                       |

When a network (communication adapter) is selected as the speed reference, a 32-bit word is used as the speed reference. If P308 [Direction Mode], is set to 1 "Bipolar," the most significant bit (MSB) is used for direction control. Otherwise, the MSB is ignored.

## IMPORTANT

When a 20-COMM Carrier (20-750-20COMM) is used to install a 20-COMM adapter on a PowerFlex 750-Series drive, the upper word (Bits 16…31) of the Logic Command Word and Logic Status Word are not accessible. The upper word is only used and accessible on PowerFlex 750-Series communication modules (20-750-*) and the embedded EtherNet/IP on PowerFlex 755 drives.

## Jog

When the drive is not running, pressing the HIM's Jog soft button or a programmed Jog digital input function or by Logic Command (sent over a communication network) causes the drive to jog at a separately programmed jog reference. This jog speed reference value is entered in P556 [ Jog Speed 1] or P557 [ Jog Speed 2].

<!-- image -->

## Scaling of an Analog Speed Reference

Refer to Analog Inputs on page 105 .

## Polarity

The polarity configuration can be selected as unipolar, bipolar, or reverse disabled via P308 [Direction Mode]. When in Unipolar mode, the sign of the speed reference value (and therefore direction of motor rotation) is determined by P879 [Drive Logic Rslt] Bit 4 "Forward" and Bit 5 "Reverse." When in Bipolar mode, the sign of the speed reference value determines the direction of motor rotation. When in Reverse Disable mode, negative speed reference values are rejected and a zero speed value is used in their place.

<!-- image -->

## Trim

The speed reference source, specified in P545 [Spd Ref A Sel] or P550 [Spd Ref B Sel], can be trimmed by variable amount. You have the option to trim the speed reference by a percentage of the reference and/or by a fixed amount and can dictate whether it is a positive or negative value. Refer to the PowerFlex 750Series Trim Block Diagram below.

<!-- image -->

## Example 1

The following example shows the configuration and resultant of the percent trim function:

- P545 [Spd Ref A Sel] = P546 [Spd Ref A Stpt]
- P546 [Spd Ref A Stpt] = 20.00 Hz
- P608 [TrmPct RefA Sel] = P609 [TrmPct RefA Stpt]
- P609 [TrmPct RefA Stpt] = 25%
- P2 [Commanded SpdRef ] = 25.00 Hz

If the speed reference = 20 Hz and if the trim percentage = 25%, the resulting trim is 20 Hz x 25% = 5 Hz, which when added to the speed reference = 25 Hz. As the speed reference changes, the amount of trim also changes because it is a percent of the speed reference. If the trim percentage = -25%, then the resulting trim is 20 Hz x -25% = -5 Hz, the speed reference = 15 Hz.

## Example 2

The following example shows the configuration and resultant of the fixed amount trim function:

- P545 [Spd Ref A Sel] = P546 [Spd Ref A Stpt]
- P546 [Spd Ref A Stpt] = 20.00 Hz
- P600 [Trim Ref A Sel] = P601 [Trim Ref A Stpt]
- P601 [Trim Ref A Stpt] = 10.00 Hz
- P2 [Commanded SpdRef ] = 30.00 Hz

If the speed reference = 20 Hz, and if the trim set point = 10 Hz, the speed reference is 20 Hz + 10 Hz = 30 Hz. If the trim set point = -10 Hz, then the speed reference = 10 Hz.

## Example 3

The following example shows the configuration and resultant of utilizing both the perfect and fixed amount trim function:

- P545 [Spd Ref A Sel] = P546 [Spd Ref A Stpt]
- P546 [Spd Ref A Stpt] = 20.00 Hz
- P608 [TrmPct RefA Sel] = P609 [TrmPct RefA Stpt]
- P609 [TrmPct RefA Stpt] = 25%
- P600 [Trim Ref A Sel] = P601 [Trim Ref A Stpt]
- P601 [Trim Ref A Stpt] = 10.00 Hz
- P2 [Commanded SpdRef ] = 35.00 Hz

If the speed reference = 20 Hz, and if the trim percentage = 25%, that resulting trim is 20 Hz x 25% = 5 Hz, and if the trim set point = 10 Hz, the speed reference is 20 Hz + 5 Hz + 10 Hz = 35 Hz. If the trim percentage = -25% and the trim set point = -10 Hz, then the speed reference = 5 Hz.

## Min/Max Fwd/Rev Speed

Maximum and minimum speed limits are applied to the forward and reverse reference. The minimum speed limits create a band that the drive will not run continuously within, but ramps through. This is due to the forward or reverse minimum speeds, P522 [Min Fwd Speed] and P523 [Min Rev Speed] respectively. If the reference is positive and less than the Min Fwd Speed, it is set to the Min Fwd Speed minimum. If the reference is negative and greater than Min Rev Speed minimum, it is set to the Min Rev Speed minimum. If the minimum is not 0, hysteresis is applied at 0 to prevent bouncing between the Min Fwd Speed and Min Rev Speed minimums. If the reference is greater than the forward or reverse maximum speeds, P520 [Max Fwd Speed] and P521 [Max Rev Speed] respectively, the speed reference is clamped to the their respective maximum limit.

<!-- image -->

## See example below:

- P520 [Max Fwd Speed] = 60 Hz
- P521 [Max Rev Speed] = -60 Hz
- P522 [Min Fwd Speed] = 20 Hz
- P523 [Min Rev Speed] = -20 Hz
- P545 [Spd Ref A Sel] = P546 [Spd Ref A Stpt]

The picture below depicts how the Min/Max Fwd/Rev Speed bands and its influence the drive. The BLUE line depicts the desired speed reference (set point)

and the RED line depicts the drive's commanded speed reference (actual). Notice there are different results, depicted by the grey dotted line, along the graph.

<!-- image -->

## Maximum Frequency

P37 [Maximum Freq] defines the maximum reference frequency. The actual output frequency can be greater as a result of slip compensation and other types of regulation.

## Speed Regulation

A number of parameter are used to control speed regulation.

## Overall Operation for Sensorless Vector Control and Volts per Hertz Control

The drive takes the speed reference and adjusts it using a proportional and integral regulator to compensate for slip and the programmed limits.

## Overall Operation for Flux Vector Control

The drive takes the speed reference that is specified by the speed reference control loop and compares it to the speed feedback. The speed regulator uses proportional and integral gains along with other advanced tuning features to adjust the torque reference that is sent to the motor. The torque reference is used to operate the motor at the specified speed. The regulator is designed for optimal bandwidth for changing speed and load. If an alternate feedback device is used with automatic tachometer switchover, the alternate values of these parameters are used.

## Desired Speed Regulator Bandwidth - P636 [Speed Reg BW]

The Speed Regulator Bandwidth sets the speed loop bandwidth and determines the dynamic behavior of the speed loop. As bandwidth increases, the speed loop becomes more responsive and can track a faster changing speed reference. A change to this parameter causes an automatic update of P645 [Speed Reg Kp], P647 [Speed Reg Ki], and P644 [Spd Err Fltr BW]. To disable the automatic gain and filter update, set this parameter to a value of zero. The configuration settings for Inertia Adaption (PowerFlex 755 only) is automatically selected when this feature is enabled.

The maximum allowable value of this parameter is limited by the ratio of P646 [Spd Reg Max Kp] to P76 [Total Inertia], and the type of speed feedback source in use (encoder versus open loop). For operation following an automatic tach switchover, the bandwidth specified in P648 [Alt Speed Reg BW] is used.

## Total Inertia of Motor and Load - P76 [Total Inertia]

The Total Inertia is the time in seconds for a motor coupled to its load to accelerate from zero to base speed at rated motor torque. This value is calculated during an Inertia Tune, after the motor has ramped up to speed and down and back down to zero speed. Adjusting this parameter causes the drive to calculate and change the speed regulator gains.

## Speed Loop Damping - P653 [Spd Loop Damping]

Sets the damping factor of the vector speed loop's characteristic equation. Damping affects the integral gain when a non-zero bandwidth has been entered. A damping factor of 1.0 is considered critical damping. Lowering the damping produces faster load disturbance rejection, but can cause a more oscillatory response. When the speed regulator bandwidth is zero, gains are set manually and damping factor has no effect.

## Integral Gain - P647 [Speed Reg Ki]

Sets the integral gain of the speed regulator (in FV Motor Control modes). This value is automatically calculated based on the bandwidth setting in P636 [Speed Reg BW], P645 [Speed Reg Kp] and P653 [Spd Loop Damping]. Integral gain can be manually adjusted by setting P636 [Speed Reg BW] to a value of zero. Integral gain has effective scaling of (per unit torque/sec) / (per unit speed).

## Proportional Gain - P645 [Speed Reg Kp]

This value is automatically calculated based on the bandwidth setting in P636 [Speed Reg BW] and P76 [Total Inertia]. The proportional gain can be manually adjusted by setting P636 [Speed Reg BW] to a value of zero. Proportional gain has effective scaling of (per unit torque) / (per unit speed). The maximum allowable value of this parameter is limited by P76 [Total Inertia] and P646 [Spd Reg Max Kp].

## Feed Forward Gain - P643 [SpeedReg AntiBckup]

Controls over-shoot/under-shoot in the step response of the Vector Control mode speed regulator. Over-shoot/under-shoot can be effectively eliminated with a setting of 0.3, which removes backup of the motor shaft when zero speed is reached. This parameter has no affect on the drive's response to load changes. A value of zero disables this feature.

## Servo Lock Gain - P642 [Servo Lock Gain] (PowerFlex 755 only)

Sets the gain of an additional integrator in the Vector Control mode speed regulator. The effect of Servo Lock is to increase stiffness of the speed response to a load disturbance. It behaves like a position regulator with velocity feed forward, but without the pulse accuracy of a true position regulator. Gain is normally set to less than 1/3 speed regulator bandwidth, or for the desired response. A value of zero disables this feature.

## Torque Reference

The Torque Reference is a reference value in percent that represents the rated torque development capability of the motor. During the autotune process, measurements are made to determine the motor equivalent circuit including connected impedance from drive terminals to the motor. Based on entered motor nameplate information and autotune results, the Torque Reference is established as 100% or 1 PU equal to the rated N·m (lb·ft) torque development capability of the motor at Full Load ampere rating within ±5% without encoder feedback, possibly within ±2% with encoder feedback.

True Torque control at the motor shaft can only occur when P35 [Motor Ctrl Mode] is configured for one of the Flux Vector control mode choices. Likewise, Torque Reference parameters are only active when Flux Vector control modes in P35 [Motor Ctrl Mode], options 3 "Induction FV," 6 "PM FV," and 10 "IPM FV."

## Internal Torque Reference Source

The inherent Torque Reference source (default setting in any of the applicable FV Control modes only) is the output from the Speed Regulator parameter, P660 [SReg Output] in percent. As it passes through trimming and limiting functions, it ultimately becomes a commanding torque reference, P690 [Limited Trq Ref ], and an input to and for the inverter Current control to output voltage and frequency to the motor and regulate torque producing vector of current accordingly. Consequently, the motor develops torque as necessary to aid the Speed Regulator to maintain minimal speed error between commanded speed and speed feedback.

Figure 30 - Torque Reference Path

<!-- image -->

There are additional internal Torque Reference sources within the drive such as from a variety of Position Regulator outputs for the motor to develop the corresponding amount of torque necessary to follow a point to point position profile, cam profile, maintain a set position or follow a Motion Planner directed profile.

The torque reference can be trimmed by Friction Compensation, Inertia Adaption, or Load Observer estimator as the application may dictate. Torque Step, an amount of torque reference step change, can be injected to simulate a load disturbance.

## External Torque Reference Source

The Torque Reference can also be established via analog or communication media as a Setpoint reference or brought into the drive externally from a variety of sources including an independent controller or another drive (for load sharing configurations).

When the PowerFlex drive is operated in Torque mode, an alternate source of reference, generally an external signal, is directed to the Torque Control as an active torque reference. Once the scaling is complete on both P675 [Trq Ref A

Sel] and P680 [Trq Ref B Sel], the output can be summed together and along with the output of "Torque Trim," to become P4 [Commanded Trq].

Figure 31 - Torque Control - Reference Scale and Trim

<!-- image -->

For additional and expanded illustration of the Torque Control, refer to the PowerFlex 755 Control Block Diagrams starting on page 375 .

The following are key parameters related to the Torque Reference control illustrated in Figure 30 and Figure 31 .

P313 [Actv SpTqPs Mode] - Active Speed Torque Position Mode Displays the Speed, Torque, Position Mode that is active, based on the dynamic selection of modes A, B, C, and D, per P309…P312 [SpdTrqPsn Mode n], and digital input conditions programmed via P181 [DI SpTqPs Sel 0] and P182 [DI SpTqPs Sel 1]. In some cases, such as operation in the SLAT min/max modes, the final regulation mode may be forced into Speed Regulation. Refer to the Speed, Torque, and Position mode bits in P935 [Drive Status 1] that indicate the active regulation mode of the drive when it is running.

P675 [Trq Ref A Sel] and P680 [Trq Ref B Sel] - Torque Reference A, B Select Selects the source for a torque reference, used when the drive is configured to command torque according to P309…312 [SpdTrqPsn Mode n]. The values of the torque reference sources are added together to provide a single torque reference.

P676 [Trq Ref A Stpt] and P681 [Trq Ref B Stpt] - Torque Reference A, B Setpoint

A digital torque value to be used as a possible source for P675 and P680 respectively.

## P677 [Trq Ref A AnlgHi] and P682 [Trq Ref B AnlgHi] - Torque Reference A, B Analog High

Used only when an analog input is selected as a torque reference according to P676 or P681. Sets the torque value that corresponds to [Anlg Inn Hi] on an I/O module or on the main control (product dependent). This establishes scaling throughout the range.

## P678 [Trq Ref A AnlgLo] and P683 [Trq Ref B AnlgLo] - Torque Reference A, B Analog Low

Used only when an analog input is selected as a torque reference according to P676 [Trq Ref A Stpt] or P681 [Trq Ref B Stpt]. Sets the torque value that corresponds to [Anlg Inn Lo] on an I/O module or on the main control (product dependent). This establishes scaling throughout the range.

## P679 [Trq Ref A Mult] and P684 [Trq Ref B Mult] - Torque Reference A, B Multiplier

A multiplier that is applied to the values referenced by P675 [Trq Ref A Sel] and P680 [Trq Ref B Sel] respectively. A value of 1 leaves the reference unaffected. Negative values invert the reference.

Refer to Speed Torque Position on page 266 for an explanation of Speed Torque Position mode choices for operating in various specific modes utilizing Internal and/or External torque reference sources.

## Speed Torque Position

The PowerFlex 750-Series drives have the ability to have four separate Speed Torque Position modes with the following parameters:

- P309 [SpdTrqPsn Mode A]
- P310 [SpdTrqPsn Mode B]
- P311 [SpdTrqPsn Mode C]
- P312 [SpdTrqPsn Mode D]

Possible selections for the above Speed/Torque/Position parameters are as follows:

- "Zero Torque" (0) – Drive operates as a torque regulator with P685 [Selected Trq Ref ] forced to a constant value of zero torque.
- "Speed Reg" (1) – Drive operates as a speed regulator. P685 [Selected Trq Ref ] comes from P660 [SReg Output] plus P699 [Inertia Comp Out].
- "Torque Ref " (2) – Drive operates as a torque regulator. P685 [Selected Trq Ref ] comes from P4 [Commanded Trq]. Under some conditions such as jogging or performing a ramp to stop operation, the drive automatically bypasses this selection and temporarily switches to Speed Regulation mode.
- "SLAT Min" (3) – Drive operates in "Speed Limited Adjustable Torque – Minimum select" mode. This is a special mode of operation used primarily in web handling applications. The drive typically operates as a torque regulator, provided that the P4 [Commanded Trq] value is algebraically smaller in value than the speed regulator's output. The drive can automatically enter Speed Regulation mode, based on conditions within the speed regulator and the magnitude of the speed regulator's output relative to the torque reference.
- "SLAT Max" (4) – Drive operates in "Speed Limited Adjustable Torque – Maximum select" mode. This is a special mode of operation used primarily in web handling applications. The drive typically operates as a torque regulator, provided that the P4 [Commanded Trq] value is algebraically larger in value than the speed regulator's output. The drive can automatically enter Speed Regulation mode, based on conditions within the speed regulator and the magnitude of the speed regulator's output relative to the torque reference.
- "Sum" (5) – Drive operates as a speed regulator. P685 [Selected Trq Ref ] comes from P660 [SReg Output] plus torque adders summed with P4 [Commanded Trq].
- "Profilier" (6) PowerFlex 755 – Drive uses the Speed Profiler / Position Indexer function. The drive operates as either a speed or position regulator. Mode of operation depends on the configuration of the Step Types in the Profiler/Indexer table.
- "Psn PTP" (7) – Drive operates as a position regulator. P685 [Selected Trq Ref ] has the same source as in Sum mode. The position control is active in Point-to-Point mode and uses its Point-to-Point position reference.

- "Psn Camming" (8) PowerFlex 755 – Drive operates as a position regulator. P685 [Selected Trq Ref ] has the same source as in Sum mode. The position control is active in Position CAM mode and uses its PCAM Planner position and speed reference.
- "Psn PLL" (9) PowerFlex 755 – Drive operates as a position regulator. P685 [Selected Trq Ref ] has the same source as in Sum mode. The position control is active in Position Phase Lock Loop mode and uses its PLL Planner position and speed reference.
- "Psn Direct" (10) – Drive operates as a position regulator. P685 [Selected Trq Ref ] has the same source as in Sum mode. The position control is active in Direct mode and uses its Direct Position Reference.
- "Psn SpdlOrnt" (11) PowerFlex 755 – Drive operates in the Positioning mode to position the load side of a machine to P1582 [SO Setpoint].

These modes selections only apply to the Flux Vector control modes in P35 [Motor Ctrl Mode], options 3 "Induction FV," 6 "PM FV," and 10 "IPM FV." These parameters select between speed regulation, torque regulation, or position regulation operation of the drive. The source of P685 [Selected Trq Ref ] is determined by the selection in these parameters when P181 [DI SpTqPs Sel 0] and P182 [DI SpTqPs Sel 1] have selected "Disabled" or selected bits that are logic low. In P935 [Drive Status 1], three bits are provided that indicate the Regulation mode of the drive when it is running. Bit 21 "Speed Mode" is set when the drive is running with the speed regulator active. Similarly, Bit 22 "PositionMode" and Bit 23 "Torque Mode" indicate when their respective regulation modes are active. Under some conditions, the active Torque mode can be forced into Speed mode regardless of the setting of Speed/Torque/Position. P313 [Actv SpTqPs Mode] indicates this and reflects the mode selection that is in use.

Figure 32 - PowerFlex 755 Firmware Flowchart

<!-- image -->

The following are key parameters related to the Torque Reference control illustrated in Figure 32 .

P313 [Actv SpTqPs Mode] - Active Speed Torque Position Mode Displays the Speed, Torque, Position Mode that is active, based on the dynamic selection of modes A, B, C, and D, per P309…P312 [SpdTrqPsn Mode n], and digital input conditions programmed via P181 [DI SpTqPs Sel 0] and P182 [DI SpTqPs Sel 1]. In some cases, such as operation in the SLAT min/max modes, the final regulation mode may be forced into Speed Regulation. Refer to the Speed, Torque, and Position mode bits in P935 [Drive Status 1] that indicate the active regulation mode of the drive when it is running.

P314 [SLAT Err Stpt] - Speed Limited Adjustable Torque, Error Setpoint Sets the magnitude of P641 [Speed Error] at which the SLAT function will release its Forced Speed Mode signal. This condition must exist for the time specified by P315 [SLAT Dwell Time]. Once released, the drive can operate as a torque regulator, depending on the relative levels of P660 [SReg Output] and P4

[Commanded Trq]. This parameter will be entered in units of Hz or RPM, depending on the value of P300 [Speed Units].

P315 [SLAT Dwell Time] - Speed Limited Adjustable Torque, Dwell Time Sets the time period that P641 [Speed Error] must exceed the P314 [SLAT Err Stpt] magnitude in order to return to min/max torque mode.

P675 [Trq Ref A Sel] and P680 [Trq Ref B Sel] - Torque Reference A, B Select Selects the source for a torque reference, used when the drive is configured to command torque according to P309…312 [SpdTrqPsn Mode n]. The values of the torque reference sources are added together to provide a single torque reference.

## P685 [Selected Trq Ref ] - Selected Torque Reference

Displays the torque value of the selected torque reference (dynamic selection according to P313 [Actv SpTqPs Mode]). This value will be summed with P686 [Torque Step]. The result is then applied to the input of the notch filter located in the Vector torque reference section.

## P686 [Torque Step] - Torque Step

Defines the amount of torque reference step change to simulate a load disturbance, used to test the response. This value is added to the main torque reference P685 [Selected Trq Ref ], and then applied to the input of the notch filter located in the Vector control torque reference section.

## P687 [Notch Fltr Freq] - Notch Filter Frequency

The center frequency for the Notch filter located in the Vector control torque reference section. To disable, set to zero.

## P688 [Notch Fltr Atten] - Notch Filter Attenuation

Sets the attenuation of the notch filter located in the Vector control torque reference section. Attenuation is the ratio of the notch filter input signal to its output at the P687 [Notch Fltr Freq]. An attenuation of 30 means that the notch output is 1/30th of the input at the specified frequency.

<!-- image -->

P689 [Filtered Trq Ref ] - Filtered Torque Reference Displays the output of the notch filter defined by P687 and P688. If P704 [InAdp LdObs Mode] indicates that either the Inertia Adaption or Load Estimate functions are active, then the filtered torque reference will also be modified by these functions.

## P690 [Limited Trq Ref ] - Limited Torque Reference

Displays the torque reference value after filtering (P689), power limits, torque limits, and current limits have been applied. This parameter is the most effective VFD representative Torque Reference value to be monitored for motor load assessment and to be passed on to other drives for load sharing applications involving multiple drives. It represents the percent of the rated torque being developed at the motor shaft.

For additional and expanded illustration of the Torque Control, refer to the PowerFlex 755 Control Block Diagrams starting on page 375 .

## Speed Torque Position Modes

## Zero Torque

Operation in Zero Torque mode enables the motor to be fully fluxed and ready to rotate when a speed command or torque command is given. This mode can be used for a cyclical application where throughput is a high priority. The control logic can select zero torque during the rest portion of a machine cycle instead of stopping the drive. When the cycle start occurs, instead of issuing a start to the drive, a Speed Regulator mode can be selected. The drive immediately accelerates the motor without the need for flux up time.

| IMPORTANT   | Zero Torque can excessively heat the motor if operated in this mode for extended periods of time. A load or flux current is still present when the drive is operating in Zero Torque mode. A motor with an extended speed range or separate cooling methods (blower) can be required.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Speed Regulation

Operating as a speed regulator is the most common and simplest mode to set up. Examples of speed regulated applications are blowers, conveyors, feeders, pumps, saws, and tools. In a speed regulated application, the speed regulator output generates the torque reference. Note that under steady state conditions the speed feedback is steady while the torque reference is a constantly adjusting signal. This is required to maintain the desired speed. In a transient state, the torque reference changes dramatically to compensate for a speed change. A short duration change in speed is the result of increasing or decreasing the load very rapidly.

For the PowerFlex 755 drive, the Inertia Compensation, Inertia Adaption, and the Friction Compensation influence the output of the speed regulator.

## Torque Regulation

A torque regulated application can be described as any process requiring some tension control. An example is a winder or unwinder with material being drawn or pulled with a specific tension required. The process also requires that another

element set the speed. Configuring the drive for torque regulation requires P309 [SpdTrqPsn Mode A] to be set to 2 "Torque Ref." In addition, a reference signal must be linked to the torque reference. For example, when Analog Input 0 is used for the torque reference, P675 [Trq Ref A Sel] needs to be configured for "Anlg In0 Value."

When operating in a Torque mode, the motor current is adjusted to achieve the desired torque. If the material being wound or unwound breaks, the load decreases dramatically and the motor can potentially go into a runaway condition.

## Speed Limited Adjustable Torque (SLAT) Modes

The SLAT minimum and SLAT maximum modes are for applications that require a smooth transition from a torque mode to a speed mode operation and vice versa. When operating in a Torque mode, the motor current is adjusted to achieve the desired torque. For example; web handling, center winders and center unwinders or other mechanical drive train where the drive is normally following a torque reference, but a break, disruption in flow or slippage could occur causing the need to prevent a runaway situation, which is best controlled in speed mode.

Direction of the applied torque and direction of the material movement determine whether SLAT minimum or SLAT maximum mode should be used.

## SLAT Minimum

Choose SLAT minimum mode when material direction and speed reference is considered "Forward" and a positive speed reference value for the Speed Regulator. The Speed Regulator output then creates a positive Torque Reference command value.

Typically configure a positive speed reference value slightly greater than what is equivalent to maintain planned material line speed. This will in turn force the speed regulator into saturation (the speed reference is slightly above the speed feedback) commanding a "more positive" torque reference than what the torque mode torque reference value is. In this scenario the drive would follow the torque reference until there was a breakage or slippage in the application.

When the drive is following a torque reference (torque mode in SLAT minimum mode), either one of two conditions will force the drive into following the speed reference in (speed mode):

- The output of the speed regulator becomes less than the torque reference. The reaction when triggered at the very point that the torque reference value in speed mode is mathematically less than the value in torque mode, generally results in greater velocity overshoot. This is the same condition that would exist in minimum torque /speed mode without SLAT features. The following plot represents the result without using SLAT features.

Figure 33 - Minimum Torque Speed without SLAT

<!-- image -->

Or

- The speed error becomes negative (the speed feedback becomes greater than the speed reference). This would force the control into speed regulator mode, a condition called Forced Speed Mode FSM.

By forcing the drive to enter speed mode FSM, the transition occurs earlier than it would have if the reaction was triggered at the very point that the torque reference value in speed mode is mathematically less than the value in torque mode, generally resulting in less velocity overshoot.

P314 [SLAT Err Stpt] and P315 [SLAT Dwell Time] allow setting some hysteresis for turning off the forced speed mode. They are set to 0 as default so that there is no hysteresis. In SLAT minimum mode, [SLAT Err Stpt] sets how much less the speed feedback should be than the speed reference before turning off the forced speed mode. The SLAT dwell time sets how long the speed error must exceed the SLAT error set point before turning off the forced speed mode.

At the time that the drive switches from torque mode to forced speed mode, the speed regulator output is loaded with the internal motor torque reference to create a smooth transition. In order for the drive to switch from speed mode back to torque mode, forced speed mode (if active) must first be turned off. Forced speed mode will turn off when the speed error is greater than the SLAT error set point for the SLAT dwell time.

With default parameter settings, this will occur when the speed error becomes positive.

When forced speed mode is off, the drive will switch back to Torque mode when the speed regulator output becomes greater than the torque reference.

Empirically setting values P314 [SLAT Err Stpt] and P315 [SLAT Dwell Time] other than default may help create even smoother transitions.

Paper Winder Application Example

<!-- image -->

The drive is set for SLAT Minimum mode, so that the drive normally runs in Torque mode and follows P675 [Trq Ref A Sel]. [Trq Ref A Sel] comes from an external controller and is approximately 60% of motor torque during the snapshot (shown below). The speed reference, also from an external controller, is set just above the speed feedback to saturate the speed regulator while in Torque mode. The following snapshot captures what occurs in the drive during a break in the web.

Figure 34 - SLAT Min to Forced Speed Mode

<!-- image -->

## SLAT Maximum Mode

Choose SLAT Maximum mode when material direction and speed reference is considered "Reverse" and a negative speed reference value for the Speed Regulator. The Speed Regulator output then creates a negative Torque Reference command value.

In SLAT Maximum mode, a speed reference is typically configured to force the speed regulator into saturation (the speed reference is slightly below the speed feedback which is equivalent to maintain planned line speed). In this scenario the drive follows the torque reference until there is breakage or slippage in the application.

In SLAT Maximum mode, the drive switches from Torque mode to Speed mode when either one of the two following conditions occur.

- The output of the speed regulator becomes more than the torque reference. This is the same condition that exists in Maximum Torque/ Speed mode without SLAT features. Or
- The speed error becomes positive (the speed feedback becomes less than the speed reference). This forces the control into speed regulator mode, a condition called Forced Speed Mode (FSM).

By forcing the drive to enter FSM, the transition occurs earlier than it would have if the reaction was triggered at the very point that the torque reference value in speed mode is mathematically more than the value in torque mode, generally resulting in less velocity overshoot.

P314 [SLAT Err Stpt] and P315 [SLAT Dwell Time] allow for setting some hysteresis for turning off the forced speed mode. They are set to 0 as default so that there is no hysteresis. In SLAT maximum mode, [SLAT Err Stpt] sets how much more the speed feedback (algebraically sign sensitive) should be than the speed reference before turning off the forced speed mode. [SLAT Dwell Time] sets how long the speed error must be less than the SLAT error set point before turning off the forced speed mode.

At the time that the drive switches from torque mode to speed mode the speed regulator output is loaded with the value from the torque reference to create a smooth transition.

In order for the drive to switch from speed mode back to torque mode, forced speed mode (if active) must first be turned off. FSM will turn off when the speed error is less than the SLAT error set point for the SLAT dwell time.

With default parameter settings, this will occur when the speed error becomes negative. When forced speed mode is off, the drive will switch back to torque mode when the speed regulator output becomes less than the torque reference.

<!-- image -->

## Sum

Configuring the drive in this mode enables an external torque input to be summed with the torque command generated by the speed regulator. This mode requires both a speed reference and a torque reference to be linked. This mode can be used for applications that have precise speed changes with critical time constraints. If the torque requirement and timing is known for a given speed change, then the external torque input can be used to preload the integrator. The timing of the speed change and the application of an external torque command change must be coordinated for this mode to be useful. The "Sum Spd/Trq" mode will then work as a feed forward to the torque regulator.

## Notes:

## Data Logging

## Drive Features

| Topic               |   Page |
|---------------------|--------|
| Data Logging        |    277 |
| Energy Savings      |    282 |
| High Speed Trending |    283 |
| Position Homing     |    292 |

This wizard logs the values of up to six parameters in a single drive at a specified interval for some period of time, with the minimum sample rate one second. The information is saved as a comma delimited *.csv file for use with Microsoft Excel or any other spreadsheet program. Clicking Next lets you configure the data logger. When data logging is completed, click Finish to close the wizard. If you click Finish before the data logging is completed, only the data collected up to that point is saved in the file. You can cancel the wizard at any time by clicking Cancel or the Close icon. All logged data is lost, and the file is deleted.

## Configuration Example

1. Connect to the drive that you want to trend via DriveExecutive, DriveExplorer, Logix Designer Drive AOPs, or Connected Components Workbench software tool.
2. Click the Show Wizard icon .

<!-- image -->

<!-- image -->

Depending if you click the wand icon or down arrow icon a particular wizard selection dialog box appears. Select the Data Logging Wizard.

<!-- image -->

3. Once the Welcome screen loads, click Next.

<!-- image -->

The data logging wizard can be configured to log up to six parameters at a minimum sample rate of one second for a specified time or number of samples.

<!-- image -->

4. To find a parameter that you want to log, select the Port, and then scroll through the parameter lists, file folders, diagnostic items or use the find function.
5. To add the parameter to the data log list, select the parameter on the leftside list and click the right arrow .

<!-- image -->

That parameter appears in the first available line entry on the right side.

6. To remove a parameter from the data log list, select the parameter on the right side and click the left arrow .

That parameter disappears from that line entry and all subsequent entries are moved up.

In the configuration example below, the data logging wizard is configured to log six drive parameters consisting of Output Frequency, Motor Velocity Feedback, Torque Current Feedback, Output Current, Output Voltage, and DC Bus Voltage parameter values.

<!-- image -->

## 7. Click Next.

This prompt for a save as dialog box that saves the data log information as a comma delimited *.csv file for use with Microsoft Excel or any other spreadsheet program.

<!-- image -->

8. To start the data logging, click Save.

As the data logging begins, a Time Left timer counts down as a blue progress bar moves to the right.

<!-- image -->

When the data logging has finished, a Logging Complete message is displayed.

<!-- image -->

Each column's width is adjustable.

Below is a spreadsheet example of data logged. Use a spreadsheet program to open the *.csv file.

<!-- image -->

## Energy Savings

Setting the motor control mode P35 [Motor Ctrl Mode] to 2 "Induct Econ" or Induction Economizer mode enables additional energy savings within the drive. To be specific, additional energy savings can be realized in constant torque applications that have constant speed reduced load periods.

## Induction Economizer

Induction Economizer mode consists of the sensorless vector control with an additional energy savings function. When steady state speed is achieved, the economizer becomes active and automatically adjusts the drive output voltage based on applied load. By matching output voltage to applied load, the motor efficiency is optimized. Reduced load commands a reduction in motor flux current.

To optimize the performance of the Induction Economizer mode, adjust the following parameters:

- P47 [Econ At Ref Ki] - Integral gain that determines the response of the output voltage when the output frequency is at reference.
- P48 [Econ AccDec Ki] - Integral gain that determines the response of the output voltage when the output frequency is accelerating or decelerating to the reference setpoint.
- P49 [Econ AccDec Kp] - Proportional gain that determines the response of the output voltage when the output frequency is accelerating or decelerating to the reference setpoint.

## High Speed Trending

The high speed trending wizard configures the internal trending of the drive, downloads that trend configuration to the drive, and uploads the trended data from the drive when finished. This information is saved as a comma delimited *.csv file for use with Microsoft Excel or any other spreadsheet program.

The high speed trending can be configured to trend up to eight parameters with 4096 samples for each parameter, at a minimum sample rate of 1.024 milliseconds. It can also be configured to trend up to four parameters with 1024 samples for each parameter, at a minimum sample rate of 256 microseconds. These are defined by the drive. Future drives may offer different options.

The PowerFlex 755 drives have the High Speed Trending functionality. PowerFlex 753 drives do not have the High Speed Trending functionality.

You can run only one wizard at a time.

## Configuration Example

1. Connect to the drive that you want to trend via DriveExecutive, DriveExplorer, Logix Designer Drive AOPs, or Connected Components Workbench software tool.
2. Click the Show Wizard icon .

<!-- image -->

Depending if you click the wand icon or down arrow icon a particular wizard selection dialog box appears.

3. Select the High Speed Trend Wizard.

<!-- image -->

4. Once the Welcome screen loads, Click Next.

<!-- image -->

The Configure Trend window lets you customize the following high speed trend details:

- Trend Mode – dictates number of trend buffers, total number of samples, and the minimum interval sample rate.
- Pre-Trigger samples – dictates number of samples to include in the trend before the trigger.
- Sample Interval – the time interval between trend data samples.
- Trigger Setup – dictates how the data trend is triggered
- a. Comparing two parameters
- b. Comparing a parameter against a constant
- c. A test bit in a parameter

- Trend Buffers – dictates the drive and/or peripheral parameters and diagnostic items that are trended.
5. To configure the Trigger Setup and Trend Buffers, click the Ellipse button

<!-- image -->

<!-- image -->

<!-- image -->

6. Select the parameter that you want to log by selecting the Port, and then scroll through the parameter lists, file folders, diagnostic items or use the find function and click Apply.

<!-- image -->

The best way to remove a parameter selection is to uncheck the check box in the Use column.

<!-- image -->

"Not used" is downloaded instead of the selected parameter. The next time you launch the wizard, that buffer has no parameter set.

In the example below, the trend buffers are configured with five drive parameters consisting of Output Frequency, Motor Velocity Feedback, DC Bus Voltage, Output Current, Output Voltage parameter values. The trend is configured for a total of 4096 samples that include 500 samples before the trigger, at a sample rate of 1.024 ms. The trigger of the high speed trend is the Motor Velocity Feedback greater than zero.

This means the following:

- The drive starts trending.
- When the motor starts rotating forward, the trend starts wrapping up.
- The drive continues trending for about 3.7 seconds to use up the remaining 3596 samples.

- The drive stops trending and is ready for uploading.
7. Click Download once the Download Succeeded message has appeared and the Trend Status is Ready.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

The Trend Status is Running and Download, Upload and Start buttons are unavailable.

<!-- image -->

The trending is in process when you see the Trend Status is in the Finishing state. You can stop the trend at any point in time by clicking Stop. You can then upload all of the data gathered so far.

<!-- image -->

The trending has ended when the Trend Status has changed from Finishing state to the Complete state.

<!-- image -->

<!-- image -->

Click Upload . This prompts a process that uploads the trend data from the drive and saves the information as a comma delimited *.csv file for use with Microsoft Excel or any other spreadsheet program. Upload

<!-- image -->

Click Save to start the upload trend data process.

<!-- image -->

Below is an example of trended data. Use a spreadsheet program to open the *.csv file.

<!-- image -->

Column C here lines up with what is displayed in DriveExplorer or any other drive software tool. Column D shows the value that the drive is using internally. Column D has more accurate data, but you may not have a use for the extra precision. You cannot get the data in column D from any other wizard or software tool.

## Block Diagram

<!-- image -->

## Position Homing

The Homing function is a standalone function of the drive that moves the motor to a home position defined by a switch that is connected to a homing input on a feedback option module, digital input resident on the Main Control Board, or on an I/O option module if there is no feedback module. This function is typically run only once after the drive is powered up or if the drive has become lost. If a universal feedback option module is used, the homing input is part of the general Registration hardware. To perform the homing sequences that require this module, the drive has to configure the Registration function on the module itself.

If a Position Absolute move is made, it is necessary to have performed either a Find Home or a Position Redefine procedure at some time after drive powerup. Until this is done, Bit 19 "Home Not Set" in [Profile Status] remains set, preventing the profile from executing.

The Find Home state is entered from the Initialize Step state when the profile is enabled with the Find Home bit set in the Profile Command parameter. The drive performs a procedure to establish the home position. The procedure consists of a move in Speed mode at the specified Find Home Speed. A digital input is used to sense when the home position limit switch has been traversed. If there is an encoder, the registration logic is used to latch the motor position when the limit switch is reached as the home position. The Find Home function handles three possible cases; Switch and Marker, Switch only, and Marker only.

## Homing Input Selection

## With Feedback Device

Both the universal feedback option modules and the encoder feedback option modules provide a dedicated homing input. The homing input on the feedback module that is selected by P135[Pos Fdbk Sel] is used for homing. If the marker pulse from an encoder is used in the homing function it is also selected by P135[Pos Fdbk Sel].

## Without Feedback Device

If the drive does not have a feedback module and a selection in P135[Psn Fdbk Sel] of "simulator feedback" is made the homing input that the drive uses is selected from any digital inputs residing on an attached I/O module by P734 [DI OL Home Limit]. There is no marker pulse input associated with "open loop" homing.

## Homing Activation

A homing function can be selected by either a digital input or a parameter. The digital input is selected from any digital inputs residing on an attached I/O module by Find Home or Return Home. To select the homing function from a parameter set Bit 0 "Find Home" or Bit 3 "Return Home" of P731 [Homing Control]. The homing sequence can be selected regardless of the mode selected in P313 [Actv SpTqPs Mode]. If the drive has a feedback option module, a vector type control must be selected in P35 [Motor Cntl Mode] parameter. If there is no feedback option module, any type of control can be selected.

When the Find Home function is selected by either a digital input or a parameter, either Bit 1 "Home DI" or Bit 2 "Home Maker" or both must be selected in P731 [Homing Control].

When the Return Home function is selected by either a digital input or a parameter, a selection of Bit 1 "Home DI" or Bit 2 "Home Maker" of P731 [Homing Control] is ignored.

To activate a Homing function, a drive start command is required if the drive is stopped. If a drive is running, the drive must be "At Zero Speed" state when the function is selected.

## Drive Stopped During Activation

If the drive is stopped, a start command to drive is required to activate a homing sequence.

## Drive Started and "At Zero Speed" During Activation

If the drive has already started and "At Zero Speed" the rising edge or toggled bit activates and latches the homing sequence.

## Drive Started and not "At Zero Speed" During Activation

If the drive has already started and not "At Zero Speed" the rising edge is ignored and the homing sequence will not start.

## Homing to Limit Switch with Feedback

Upon activation of homing the drive starts moving in Speed Control mode, and ramp to the speed and direction set in P735 [Find Home Speed] at the rate set in P736 [Find Home Ramp]. When the limit/proximity switch is reached the "Homing Input" is set. The position count is latched and is considered the home position count. The drive then ramps to zero at the rate set in P736 [Find Home Ramp]. The drive then performs a point-to-point position move back to the home position count in speed of 1/10 of P735 [Find Home Speed]. When the motor is "At Position" and "At Zero Speed," the homing sequence is complete.

## NOT Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position and transferring position reference back to its previous source. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity and transferring velocity reference back to its previous source.

## Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position; the drive then transfers position reference back to its previous source once it receives a start command. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity; the drive then transfers velocity reference back to its previous source once it receives a start command.

<!-- image -->

Homing to Marker Pulse with Feedback Upon activation of homing the drive starts moving in Speed Control mode, and ramps to the speed and direction set in P735 [Find Home Speed] at the rate set in P736 [Find Home Ramp]. When the Marker Pulse input is set the position count is latched and is considered the home position count after the marker pulse is reached, the drive then ramps to zero in P736 [Find Home Ramp]. The drive then performs a point-to-point position move back to the home position count in speed of 1/10 of P735 [Find Home Speed]. When the motor is "At Position" and "At Zero Speed," the homing sequence completes.

## NOT Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position and transferring position reference back to its previous source. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity and transferring velocity reference back to its previous source.

## Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position; the drive then transfers position reference back to its previous source once it receives a start command. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running

holding zero velocity; the drive then transfers velocity reference back to its previous source once it receives a start command.

<!-- image -->

## Homing to Switch and Marker Pulse with Feedback

Upon activation of homing the drive starts moving in Speed Control mode, and ramp to the speed and direction set in P735 [Find Home Speed] at the rate set in P736 [Find Home Ramp]. As the motor moves toward the limit/proximity switch, the marker pulse is triggering a register on the feedback module to latch the current position count. When the limit/proximity switch is reached the "Homing Input" is set. The last maker pulse position count that was latched prior to the "Homing Input" being set is considered the home position count. The drive then ramps to zero at the rate set in P736 [Find Home Ramp]. The drive then performs a point-to-point position move back to the home position count in speed of 1/10 of P735 [Find Home Speed]. When the motor is "At Position" and "At Zero Speed", the homing sequence completes.

## NOT Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position, and transferring position reference back to its previous source. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity and transferring velocity reference back to its previous source.

## Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position; the drive then transfers position reference back to its previous source once it receives a start command. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running

holding zero velocity; the drive then transfers velocity reference back to its previous source once it receives a start command.

<!-- image -->

## Find Home DI without Feedback Device

Upon activation of homing the drive starts moving in Speed Control mode, and ramp to the speed and direction set in P735 [Find Home Speed] at the rate set in P736 [Find Home Ramp]. When the limit/proximity switch is reached the "Homing Input" is set.

If P35 [Motor Ctrl Mode] = 3 "Induction FV" P847 [Psn Fdbk] count is latched and is considered the home position count. The drive then ramps to zero at the rate set in P736 [Find Home Ramp]. The drive then performs a point-to-point position move back to the home position count in speed of 1/10 of P735 [Find Home Speed]. When the motor is "At Position" and "At Zero Speed, the homing sequence completes.

## NOT Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position and transferring position reference back to its previous source. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity and transferring velocity reference back to its previous source.

## Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position; the drive then transfers position reference back to its previous source once it receives a start command. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running

holding zero velocity; drive then transfers velocity reference back to its previous source once it receives a start command.

<!-- image -->

## If P35[Motor Ctrl Mode] = 0 "Induction VHz" or 1 "Induction SV"

The drive then ramps to zero at the rate set in P736 [Find Home Ramp].

## If the drive travels passed the proximity switch during decel

The drive reverses direction at a speed of 1/10 of P735 [Find Home Speed]. The drive must then receive a rising edge of the proximity switch followed by a falling edge pulse. Upon receiving the falling edge pulse the drive will decel at the rate set in P736 [Find Home Ramp]. When the motor is "At Zero Speed," the homing sequence completes.

## If the drive remains on proximity switch during decel

The drive reverses direction at a speed of 1/10 of P735 [Find Home Speed]. When the falling edge of the limit/proximity switch is reached the drive will decel at rate set in P736 [Find Home Ramp]. When the motor is "At Zero Speed," the homing sequence completes.

## NOT Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position and transferring position reference back to its previous source. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running holding zero velocity and transferring velocity reference back to its previous source.

## Hold At Home, P731 Bit 7

If a position control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running, holding position; the drive then transfers position reference back to its previous source once it receives a start command. If velocity control type mode is selected in P313 [Actv SpTqPs Mode] the drive continues running

holding zero velocity; drive then transfers velocity reference back to its previous source once it receives a start command.

<!-- image -->

<!-- image -->

## Integrated Motion on the EtherNet/IP Network Applications for PowerFlex 755 AC Drives

| Topic                                                                                                | Page   |
|------------------------------------------------------------------------------------------------------|--------|
| Additional Resources for Integrated Motion on the EtherNet/IP Network Information                    | 300    |
| Coarse Update Rate                                                                                   | 301    |
| Control Modes for PowerFlex 755 Drives Operating on the Integrated Motion on the EtherNet/IP Network | 301    |
| Drive Nonvolatile (NV) Memory for Permanent Magnet Motor Configuration                               | 308    |
| Dual Loop Control                                                                                    | 309    |
| Dual-Port EtherNet/IP Option Module (ETAP)                                                           | 315    |
| Hardware Over Travel Considerations                                                                  | 316    |
| Integrated Motion on EtherNet/IP Instance to PowerFlex 755 Drive Parameter Cross-Reference 317       |        |
| Motor Brake Control                                                                                  | 338    |
| Network Topologies                                                                                   | 341    |
| PowerFlex 755 and Kinetix 7000 Drive Overload Rating Comparison for Permanent Magnet Motor Operation | 345    |
| PowerFlex 755 Drive Option Module Configuration and Restrictions                                     | 346    |
| Regenerative/Braking Resistor                                                                        | 347    |
| Safe Speed Monitor Option Module (20-750-S1) Configuration                                           | 350    |
| Speed Limited Adjustable Torque (SLAT)                                                               | 353    |
| Supported Motors                                                                                     | 357    |
| System Tuning                                                                                        | 363    |
| Using an Incremental Encoder with an MPx Motor                                                       | 372    |
| PowerFlex 755 Integrated Motion on the EtherNet/IP Network Block Diagrams                            | 375    |

## Additional Resources for Integrated Motion on the EtherNet/IP Network Information

These documents contain additional information on the Integrated Motion on the EtherNet/IP Network for PowerFlex 755 AC drive applications.

| Resource                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 750-Series Drive Programming Manual, publication 750-PM001                 | Provides detailed information on: •  I/O, control, and feedback options  •  Parameters and programming  •  Faults, alarms, and troubleshooting                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PowerFlex 750-Series Drive Installation Instructions, publication 750-IN001          | Provides instructions for: •  Mechanical installation •  Connecting incoming power, the motor, and basic I/O                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PowerFlex 750-Series Drive Technical Data, publication 750-TD001                     | Provides detailed information on: •  Drive specifications •  Option specifications •  Fuse and circuit breaker ratings                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Integrated Motion on the Ethernet/IP Network User Manual, publication MOTION-UM003   | Use this manual to configure an Integrated Motion on the Ethernet/IP network application and to start up your motion solution using the ControlLogix™ system.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Logix5000 Controllers Motion Instructions Reference Manual, publication MOTION-RM002 | Provides details about the motion instructions that are available for a Logix5000 controller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Kinetix® Motion Control Selection Guide, publication GMC-SG001                       | This selection guide is meant to help make initial decisions for the motion control products best suited for your system requirements. In addition, there are technical data publications with product specifications and design guide publications with selection information, specific to each drive family, to determine the accessories needed for your application. The design guides also include the recommended motor cables, performance specifications, and torque/ speed (rotary) and force/velocity (linear) curves for each drive and motor/actuator combination. |

You can view or download publications at http:/www.rockwellautomation.com/literature/. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Software Tools

Integrated Architecture Builder can be downloaded at: http://www.rockwellautomation.com/en/e-tools/configuration.html

Motion Analyzer can be downloaded at: http://motion-analyzer.com/

## Coarse Update Rate

## Control Modes for PowerFlex 755 Drives Operating on the Integrated Motion on the EtherNet/IP Network

The position loop for the PowerFlex 755 drive is updated at a rate of 1.024 ms (1024 sec). During each position loop update the drive can either read or write data to the embedded Ethernet port, but cannot do both operations during the same update. Therefore the drive can receive only new updates every other position loop update event. To read new information from the Motion Planner (that is controller), the minimum coarse update rate must be 2.5 ms or greater to be sure that no data packets are lost. If the PowerFlex 755 drive is operated at a coarse update rate of less than 2.5 ms, data packets can be lost (resulting in the drive interpolating between missed updates), and/or the drive can fault if enough data packets are missed consecutively. Rockwell Automation recommends a minimum coarse update rate of 3 ms for the PowerFlex 755 drive.

Integrated Motion on the EtherNet/IP network is a feature available with firmware revision 2.xxx and later for PowerFlex 755 drives. This feature provides a common user experience as with Kinetix 6500 drives when used with Logix controllers, revision 19 and later, on the EtherNet/IP network:

- The same motion profile provides a common configuration experience. The PowerFlex 755 drive uses the Motion Properties/Axis Properties and the same motion attributes as the Kinetix 6500 drive.
- The same motion instructions provide a common programming experience.

Refer to the Integrated Motion on EtherNet/IP appendix in the PowerFlex 750Series Programming Manual, publication 750-PM001, for more information.

## Motion Drive Start (MDS) Instruction

For information regarding the MDS instruction, refer to the Logix5000 Controllers Motion Instructions Reference Manual, publication MOTION-RM002 .

For the PowerFlex 755 drive, the MDS instruction is valid only when the axis configuration is set to one of these control modes:

- Frequency Control
- Velocity Loop
- Torque Loop

The MDS instruction is not valid when the axis configuration is set to Position Loop.

2

## Motion Drive Start Instruction Configuration

The MDS instruction is configured in a similar fashion to most motion instructions, as seen in this example.

<!-- image -->

The MDS instruction is similar to a Motion Axis Jog (MAJ) instruction, however the MDS instruction does not set the acceleration/deceleration rates. The acceleration rate is dynamically set by the ramp attributes configured in a Set System Value (SSV) instruction. See Ramp Attributes on page 304. Note that PF755\_Axis was configured for revolutions. Therefore, the speed units are revs/sec.

## Motion Drive Start (MDS) Sample Code

Start

<!-- image -->

## Increase Speed

The speed is changed by updating the speed reference and then re-executing the MDS instruction.

<!-- image -->

## Decrease Speed

The speed is changed by updating the speed reference and then re-executing the MDS instruction.

<!-- image -->

## Torque Mode

When the axis configuration is in Torque Loop, the Speed attribute within the MDS instruction is not used to command the speed of the drive. The speed is determined by the amount of torque specified in the CommandTorque and/or TorqueTrim attributes.

<!-- image -->

## IMPORTANT

You must command zero torque in the CommandTorque and TorqueTrim attributes before you use the Motion Axis Stop (MAS) instruction to stop a specific motion process on an axis or to stop the axis completely. To use the MAS instruction, you must set Change Decel to No. Otherwise an instruction error can occur. The deceleration rate is set based on the Ramp Deceleration attribute. The Motion Servo Off (MSF) instruction is used to deactivate the drive output for the specified axis and to deactivate the axis' servo loop. If you execute an MSF instruction while the axis is moving, the axis coasts to an uncontrolled stop.

## Ramp Attributes

The MDS instruction is validated if the Integrated Motion on EtherNet/IP drive device supports the following five ramp attributes:

- RampAcceleration
- RampDeceleration
- RampVelocity - Positive
- RampVelocity - Negative
- RampJerk - Control

These ramp attributes are available only when the PowerFlex 755 drive axis configuration is set to Frequency Control or Velocity Loop. These ramp attributes are not available when the axis configuration is set to Torque Loop or Position Loop.

This table provides a cross reference between the PowerFlex 755 Integrated Motion on the EtherNet/IP Network Motion Ramp Attributes and the corresponding drive parameters.

| Ramp Attribute Drive Parameter                               |
|--------------------------------------------------------------|
| RampAcceleration P535 [Accel Time 1]                         |
| RampDeceleration P537 [Decel Time]                           |
| RampVelocity - Positive P520 [Max Fwd Speed]                 |
| RampVelocity - Negative P521 [Max Rev Speed]                 |
| RampJerk - Control P540 [S Curve Accel] P541 [S Curve Decel] |

## Ramp Attribute Sample Code

The Ramp Attributes listed in the previous section are accessible via a Set System Value (SSV) instruction, as shown in this example:

<!-- image -->

## Position Mode, Velocity Mode, and Torque Mode Comparison

The PowerFlex 755 supports the following axis configurations:

- Frequency Control with No Feedback
- Position Loop with Motor Feedback, Dual Feedback or Dual Integral Feedback
- Velocity Loop with Motor Feedback or No Feedback
- Torque Loop with Motor Feedback

The selection options of the axis configuration within the Logix Designer application, Axis Properties, General tab are shown here.

<!-- image -->

When the axis configuration is set to Frequency Control, you can select one of the following control methods that best suits the application:

- Basic Volts/Hertz
- Fan/Pump Volts/Hertz
- Sensorless Vector
- Induction FV

The selection options of the axis configuration within the Logix Designer application Axis Properties, Frequency Control tab are shown here.

<!-- image -->

This table contains the possible axis configurations and corresponding control modes of the PowerFlex 755 drive on the Integrated Motion on the EtherNet/IP Network.

| Axis Configuration                    | P35 [Motor Ctrl Mode] P65 [VHz Curve]   |             |
|---------------------------------------|-----------------------------------------|-------------|
| Frequency Control:                    |                                         |             |
| Basic Volts/Hertz                     | InductionVHz                            | Custom V/Hz |
| Fan/Pump Volts/Hertz                  | InductionVHz                            | Fan/Pump    |
| Sensorless Vector                     | Induction SV                            | Custom V/Hz |
| Sensorless Vector economy Induct Econ |                                         | Custom V/Hz |
| Position Loop                         | Induction FV                            | Custom V/Hz |
| Velocity Loop                         | Induction FV                            | Custom V/Hz |
| Torque Loop                           | Induction FV                            | Custom V/Hz |

## Drive Nonvolatile (NV) Memory for Permanent Magnet Motor Configuration

For more detailed examples on PowerFlex 755 axis configurations, refer to the Axis Configuration Examples for the PowerFlex 755 Drive chapter in the Integrated Motion on the Ethernet/IP Network Configuration and Startup User Manual, publication MOTION-UM003 .

## Frequency Only

For information on the specific Frequency Control details, see the Motion Instructions and Integrated Motion Control Modes appendix in the Logix5000 Controllers Motion Instructions Reference Manual, publication MOTION-RM002 .

A Kinetix drive can automatically read configuration data in a permanent magnet motor/encoder's nonvolatile memory, whereas the motor/encoder configuration data must be manually entered and tuned in a PowerFlex 755 drive when configuring the drive and a permanent magnet motor for operation on the Integrated Motion on the EtherNet/IP Network.

The Drive NV option (shown in the screen example below) lets you start up a PowerFlex 755 drive and permanent magnet motor using the motor/encoder data that is entered and stored in the drive's nonvolatile memory. This is useful for a drive running in standalone mode that is being converted to operation on an Integrated Motion on the EtherNet/IP Network.

Use these settings to configure the drive module:

- Verify that the correct motor/encoder data is present in the drive.
- In the Axis Properties for the drive module, select the Motor category, and from the Data Source pull-down menu, choose Drive NV.
- Verify that the feedback selection in the appropriate drive parameter matches the selection in the Motor Feedback category for the axis.

<!-- image -->

## Dual Loop Control

This section explains how to configure a dual loop feedback application by using Integrated Motion on the EtherNet/IP Network for a PowerFlex 755 drive.

## Dual Loop Application Description

A dual loop control application uses two encoders, one mounted on the motor (typical), and one mounted on the load (as depicted in this block diagram). The two encoders are connected to the PowerFlex 755 drive via separate feedback option modules, one installed in port 5, and another installed in port 4.

<!-- image -->

## Dual Loop Control Configuration

These steps assume that you have created an axis for the PowerFlex 755 drive in the Motion group and added a new PowerFlex 755 drive module in the Logix Designer application. See the Integrated Motion on the EtherNet/IP Network Configuration and Startup User Manual, publication MOTION-UM003, for complete procedures. Follow these steps to configure the dual loop control (encoder) axis.

1. Create a feedback axis in the Motion group for the encoders (Dual\_Loop\_Axis in this example).

2. Open the PowerFlex 755 drive module and click the Associated Axis tab.
3. From the Axis 1 pull-down menu, choose the feedback axis you created (Dual\_Loop\_Axis in this example).
4. From the Motor/Master Feedback Device pull-down menu, choose Port 5 Channel A.
5. From the Load Feedback Device pull-down menu, choose Port 4 Channel A.
6. Click OK.

<!-- image -->

7. Open the Axis Properties for the feedback axis (Dual\_Loop\_Axis).
8. From the Feedback Configuration pull-down menu, choose Dual Feedback to allow the axis object to accept feedback from two sources.
9. Select the Motor Feedback category.
10. From the Type pull-down menu, choose the appropriate motor feedback.
11. In the Cycle Resolution box, type the appropriate value for your device.
12. From the Startup Method pull-down menu, choose the appropriate value for your device.

<!-- image -->

<!-- image -->

13. Select the Load Feedback category.
14. From the Type pull-down menu, choose the appropriate load feedback device.
15. From the Units pull-down menu, choose the appropriate value.
16. In the Cycle Resolution box, type the appropriate value for your device.
17. From the Startup Method pull-down menu, choose the appropriate value for your device.
18. In the Turns box, type the appropriate value for your device.

<!-- image -->

Mrive Parameters

19. Select the Scaling category.
20. From the Load Type pull-down menu, choose the appropriate value for your device.

This example uses a Rotary Transmission.

21. In the Transmission Ratio boxes, type the appropriate values for your device.

This example uses a ratio of 5:1.

22. In the Scaling Units box, type the appropriate value for your device.
23. In the Scaling Position Units box, type the appropriate value for your device.

This example uses 30 position units for every 1.0 load encoder revolution on a rotary axis (for example a dial), that unwinds to zero position after 90 units accumulate.

<!-- image -->

The velocity loop is controlled by the motor encoder feedback. Because a mechanical transmission exists between the motor and load side, the scaling units are potentially different between the two encoders.

24. To verify that the Motor to Load ratio is correct, select the Parameter List category.
25. View the value of the FeedbackUnitRatio parameter. In this example the ratio is 5:1, or 5 motor encoder revolutions to per load encoder revolution.

<!-- image -->

If the velocity loop is not performing well, that is, not following the command and not accelerating or decelerating properly, verify that this ratio is correct.

26. Continue by tuning this axis.

## Dual-Port EtherNet/IP Option Module (ETAP)

The Dual-Port EtherNet/IP option module has two modes of operation, Adapter mode (default) and Tap mode.

## Operation Mode Selection

The Tap mode is intended for use with PowerFlex 755 drives and uses the ENET3 (DEVICE) port as a connection point to transfer Integrated Motion on the EtherNet/IP Network data to the PowerFlex 755 drive's embedded EtherNet/IP adapter. The operation mode is selected by using the Operating Mode jumper ( J4). For more information about setting the Operating Mode jumper, see the PowerFlex 20-750-ENETR Dual-Port EtherNet/IP Option Module User Manual, publication 750COM-UM008 .

## IP Address Assignment

If the PowerFlex 755 drive is connected to a Stratix 6000™ or Stratix 8000 managed Ethernet switch and the drive is set for BOOTP mode, the "dynamic IP address assignment by port" (Stratix 6000) or "DHCP persistence" (Stratix 8000) feature sets the IP address for the drive. For more details, see the Stratix 6000 Ethernet Managed Switch User Manual, publication 1783-UM001, or the Stratix 8000 and Stratix 8300™ Ethernet Managed Switches User Manual, publication 1783-UM003 .

## Option Module Placement

Install the Dual-Port EtherNet/IP option module in Port 4 or 5 of the PowerFlex 755 drive control pod. (When operating in Tap mode, drive Port 6 cannot be used.)

## Hardware Over Travel Considerations

When a PowerFlex 755 drive is configured for Integrated Motion on the EtherNet/IP Network none of the I/O option modules are supported. Therefore, inputs associated with over-travel limits must be wired into controller input modules and then control must be programmed in the Logix Controller.

Operation of this control is accomplished by programming the controller to monitor the over travel limits via digital inputs and setting the desired action when over travel limits are exceeded. Possible actions include (but not limited to), setting an alarm, stopping the motion planner, stopping the drive, or performing a shutdown function.

The sample ladder logic code below depicts a possible solution for performing hardware over travel control (the code is an example only and is not the only solution for monitoring hardware over travel limits). Each individual application determines the requirements for the necessary hardware over travel control. This example monitors digital inputs and issues a motion axis stop if either input goes false and generates an output indicator that could be used to annunciate the stop.

<!-- image -->

## Integrated Motion on EtherNet/IP Instance to PowerFlex 755 Drive Parameter Cross-Reference

This section cross-references the Logix Designer Module Properties and Axis Properties instance to the corresponding PowerFlex 755 drive parameter. See the PowerFlex 755 Standard and Safety Drive Module Optional Attributes appendix in this manual for details on optional attributes and the corresponding control mode functionality supported by a PowerFlex 755 drive module.

## Frequency Control Axis Properties Configuration

General Axis Properties for Frequency Control

<!-- image -->

## Frequency Control Axis Properties

<!-- image -->

Frequency Control Motion Axis Parameters

<!-- image -->

Table 13 - Frequency Control Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |                                                            |
|-------------------------------------------------------------|------------------------------------------------------------|
|                                                             | Break Frequency P63 [Break Frequency]                      |
|                                                             | Break Voltage P62 [Break Voltage]                          |
|                                                             | Current Vector Limit P422 [Current Limit 1]                |
|                                                             | Flux Up Control P43 [Flux Up Enable] – Forced to Automatic |
|                                                             | Flux Up Time P44 [Flux Up Time]                            |
| Frequency Control Method                                    | P65 [VHz Curve]                                            |
| Maximum Frequency                                           | P37 [Maximum Freq]                                         |
| Overtorque Limit                                            | P436 [Shear Pin1 Level]                                    |
| Overtorque Limit Time                                       | P437 [Shear Pin 1 Time]                                    |
| Run Boost                                                   | P61 [Run Boost]                                            |
| Skip Speed 1                                                | P526 [Skip Speed 1]                                        |
| Skip Speed 2                                                | P527 [Skip Speed 2]                                        |
| Skip Speed 3                                                | P528 [Skip Speed 3]                                        |
| Skip Speed Band                                             | P529 [Skip Speed Band]                                     |
| Start Boost                                                 | P60 [Start Acc Boost]                                      |
| Undertorque Limit                                           | P442 [Load Loss Level]                                     |
| Undertorque Limit Time                                      | P443 [Load Loss Time]                                      |
| Velocity Droop                                              | P620 [Droop RPM at FLA]                                    |
| Velocity Limit Negative                                     | P521 [Max Rev Speed]                                       |
| Velocity Limit Positive                                     | P520 [Max Fwd Speed]                                       |

## Velocity Control Axis Properties Configuration

General Axis Properties for Velocity Control

<!-- image -->

Velocity Control Axis Properties

<!-- image -->

## Velocity Control Motion Axis Parameters

<!-- image -->

Table 14 - Velocity Control Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |                                            |
|-------------------------------------------------------------|--------------------------------------------|
| Acceleration Feed Forward Gain P696 [Inertia Acc Gain]      | P697 [Inertia Dec Gain]                    |
|                                                             | SLAT Configuration P309 [SpdTrqPsn Mode A] |
| SLAT Set Point                                              | P314 [SLAT Err Stpt]                       |
| SLAT Time Delay                                             | P315 [SLAT Dwell Time]                     |
| Velocity Droop                                              | P620 [Droop RPM at FLA]                    |
| Velocity Integrator Bandwidth                               | P647 [Speed Reg Ki]                        |
| Velocity Integrator Hold                                    | P635 [Spd Options Ctrl]                    |
| Velocity Integrator Preload                                 | P652 [SReg Trq Preset]                     |
| Velocity Limit Negative                                     | P521 [Max Rev Speed]                       |
| Velocity Limit Positive                                     | P520 [Max Fwd Speed]                       |
| Velocity Loop Bandwidth                                     | P645 [Speed Reg Kp]                        |
| Velocity Low Pass Filter Bandwidth                          | P644 [Spd Err Fltr BW]                     |
| Velocity Negative Feed Forward Gain                         | P643 [SpdReg AntiBckup]                    |
| Velocity Offset                                             | P601 [Trim Ref A Stpt]                     |

## Torque Loop Axis Properties Configuration

General Axis Properties for Torque Loop

<!-- image -->

Torque Loop Axis Properties

<!-- image -->

## Torque Loop Motion Axis Parameters

<!-- image -->

Table 15 - Torque Loop Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |
|-------------------------------------------------------------|
| Flux Up Control P43 [Flux Up Enable] – Forced to Automatic  |
| Flux Up Time P44 [Flux Up Time]                             |
| Overtorque Limit P436 [Shear Pin1 Level]                    |
| Overtorque Limit Time P437 [Shear Pin 1 Time]               |
| Torque Limit Negative P671 [Neg Torque Limit]               |
| Torque Limit Positive P670 [Pos Torque Limit]               |
| Undertorque Limit P442 [Load Loss Level]                    |
| Undertorque Limit Time  P443 [Load Loss Time]               |

## Position Loop Axis Properties Configuration

General Axis Properties for Position Loop

<!-- image -->

Position Loop Axis Properties

<!-- image -->

## Position Loop Motion Axis Parameters

<!-- image -->

Table 16 - Position Loop Instance to Parameter Cross Reference

<!-- image -->

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |                         |
|-------------------------------------------------------------|-------------------------|
| Position Integrator Bandwidth P838 [Psn Reg Ki]             |                         |
| Position Integrator Hold P721 [Position Control]            |                         |
| Position Lead Lag Filter Bandwidth P834 [Psn Out Fltr BW]   |                         |
| Position Lead Lag Filter Gain                               | P833 [Psn Out FltrGain] |
| Position Loop Bandwidth                                     | P839 [Psn Reg Kp]       |
| Position Notch Filter Frequency                             | P830 [PsnNtchFltrFreq]  |
| Velocity Feed Forward Gain                                  | P549 [Spd Ref A Mult]   |

## Induction Motor Data Axis Properties Configuration

## Induction Motor Data Axis Properties

<!-- image -->

Induction Motor Data Motion Axis Parameters

<!-- image -->

Table 17 - Induction Motor Data Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |
|-------------------------------------------------------------|
| Induction Motor Rated Frequency P27 [Motor NP Hertz]        |
| Motor Overload Limit P413 [Mtr OL Factor]                   |
| Motor Rated Continuous Current P26 [Motor NP Amps]          |
| Motor Rated Output Power P30 [Motor NP Power]               |
| Motor Rated Voltage P25 [Motor NP Volts]                    |
| Motor Type  P35 [Motor Cntl Mode]                           |
| Rotary Motor Poles  P31 [Motor Poles]                       |
| Rotary Motor Rated Speed  P28 [Motor NP RPM]                |

## Induction Motor Model Axis Properties Configuration

Induction Motor Model Motion Axis Parameters

<!-- image -->

Table 18 - Induction Motor Model Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter        |
|------------------------------------------------------------------|
| Induction Motor Flux Current P75 [Flux Current Ref]              |
| Induction Motor Rated Slip Speed P621 [Slip RPM at FLA]          |
| Induction Motor Stator Leakage Resistance P74 [Ixo Voltage Drop] |
| Induction Motor Rotor Leakage Resistance  P74 [Ixo Voltage Drop] |
| Induction Motor Stator Resistance  P73 [IR Voltage Drop]         |

## Permanent Magnet Motor Data Axis Properties Configuration

## Permanent Magnet Motor Data Axis Properties

<!-- image -->

Permanent Magnet Motor Data Motion Axis Parameters

<!-- image -->

Table 19 - Permanent Magnet Motor Data Instance to Parameter Cross Reference

<!-- image -->

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |                        |
|-------------------------------------------------------------|------------------------|
| Motor Overload Limit P413 [Mtr OL Factor]                   |                        |
| Motor Rated Continuous Current P26 [Motor NP Amps]          |                        |
| Motor Rated Output Power                                    | P30 [Motor NP Power]   |
| Motor Rated Peak Current                                    | P422 [Current Limit 1] |
| Motor Rated Voltage                                         | P25 [Motor NP Volts]   |
| Motor Type                                                  | P35 [Motor Cntl Mode]  |
| Rotary Motor Poles                                          | P31 [Motor Poles]      |
| Rotary Motor Rated Speed                                    | P28 [Motor NP RPM]     |

Permanent Magnet Motor Model Motion Axis Parameters

<!-- image -->

Table 20 - Permanent Magnet Motor Model Instance to Parameter Cross Reference

<!-- image -->

| Integrated Motion on EtherNet/IP Instance Drive Parameter      |
|----------------------------------------------------------------|
| PM Motor Rotary Voltage Constant P86 [PM CEMF Voltage]         |
| PM Motor Resistance P87 [PM IR Voltage]                        |
| PM Motor Inductance  P88 [PM IXq Voltage] P89 [PM IXd Voltage] |

## Motor Feedback Axis Properties Configuration

## Motor Feedback Axis Properties

<!-- image -->

Motor Feedback Motion Axis Parameters

<!-- image -->

Table 21 - Motor Feedback Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback n Accel Filter Bandwidth P705 [Inertia Adapt BW]                                                                                                      |
| Feedback n Cycle Resolution ENC: P02 [Encoder PPR] DENC: P02 [Encoder 0 PPR] DENC: P12 [Encoder 1 PPR] UFB: P15 [FB0 IncAndSC PPR] UFB: P45 [FB1 IncAndSC PPR] |
| Feedback n Turns UFB: P22 [FB0 SSI Turns] UFB: P52 [FB1 SSI Turns]                                                                                             |
| Feedback n Type UFB: P06 [FB0 Device Sel] UFB: P36 [FB1 Device Sel]                                                                                            |
| Feedback n Velocity Filter Bandwidth P639 [SReg FB Fltr BW]                                                                                                    |
| Feedback n Velocity Filter Taps P126 [Pri Vel FdbkFltr]                                                                                                        |

## Motor Load Feedback Axis Properties Configuration

## Motor Load Feedback Axis Properties

<!-- image -->

## Motor Load Feedback Motion Axis Parameters

<!-- image -->

Table 22 - Motor Load Feedback Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback n Cycle Resolution ENC: P02 [Encoder PPR] DENC: P02 [Encoder 0 PPR] DENC: P12 [Encoder 1 PPR] UFB: P15 [FB0 IncAndSC PPR] UFB: P45 [FB1 IncAndSC PPR] |

## Load Axis Properties Configuration

## Load Axis Properties

<!-- image -->

Load Motion Axis Parameters

<!-- image -->

Table 23 - Load Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Total Inertia P76 [Total Inertia]                                                                                                                                                                                                                                                                                                                  |
| Torque Offset + Torque Trim P686 [Torque Step] •  Torque Offset is summed together with the Torque Trim value, which is sent synchronously to the drive every Coarse Update Period. The Torque Trim value is available for real time “active” torque corrections and the Torque Offset value is available for constant system torque compensation. |

## Load Backlash Axis Properties Configuration

## Load Backlash Axis Properties

<!-- image -->

- Reversal Offset resides in the controller's Motion Planner

## Load Compliance Motion Axis Parameters

<!-- image -->

Table 24 - Load Compliance Instance to Parameter Cross Reference

<!-- image -->

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |
|-------------------------------------------------------------|
| Torque Low Pass Filter Bandwidth P659 [SReg Outfltr BW]     |
| Torque Notch Filter Frequency P687 [Notch Fltr Freq]        |

## Load Observer Axis Properties Configuration

## Load Observer Axis Properties

<!-- image -->

Load Observer Motion Axis Parameters

<!-- image -->

Table 25 - Load Observer Instance to Parameter Cross Reference

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |
|-------------------------------------------------------------|
| Load Observer Bandwidth P711 [Load Observer BW]             |
| Load Observer Configuration P704 [InAdp LdObs Mode]         |
| Load Observer Feedback Gain P706 [InertiaAdaptGain]         |

## Module Properties Power Tab Configuration

<!-- image -->

Table 26 - Power Tab to Parameter Cross Reference

<!-- image -->

| Integrated Motion on EtherNet/IP Instance Drive Parameter   |
|-------------------------------------------------------------|
| Regenerative Power Limit  P426 [Regen Power Lmt]            |
| Bus Regulator Action P372 [Bus Reg Mode A]                  |
| Shunt Regulator Resistor Type  P382 [DB Resistor Type]      |
| External Shunt Resistance P383 [DB Ext Ohms]                |
| External Shunt Power P384 [DB Ext Watts]                    |
| External Shunt Pulse Power P385 [DB ExtPulseWatts]          |

## Motor Brake Control

When a PowerFlex 755 drive is configured for Integrated Motion on the EtherNet/IP Network none of the I/O option modules are supported. Normal means of having the drive control the brake and utilizing drive's I/O are not supported. Motor brake control must be user-configured in the Logix controller. The basic functionality involved is to enable the drive using an MSO instruction, verify that the drive is enabled, and then apply power to disengage the motor brake. The specific motor used and the application often dictates a time delay between when the drive is enabled and the brake is disengaged. A very similar sequence is followed with disabling the drive using an MSF instruction. In this case the brake is engaged, and after a user-configured amount of time, the drive is disabled. Figure 35 depicts this operation.

Figure 35 - Timing Diagram

<!-- image -->

The sample ladder logic code in Figure 36 on page 339 depicts a possible solution for performing brake control (the code is an example only and is not the only solution for performing brake control). Each individual application determines the requirements for the necessary brake control.

Figure 36 - Sample Motor Brake Code

<!-- image -->

Along with normal modes of machine operation it is important to engage the brake in the event of a fault. Fault status can be monitored in the Logix code and the brake can be engaged in the event of a fault. Knowing what the configured Stop Action is helps determine when to engage the brake in the event of a fault. Application considerations can also be factored into this decision. This stop action is configured on the Axis Properties / Actions screen (as shown in this example).

<!-- image -->

## Network Topologies

This topic provides examples of network topologies that can be used when implementing an Integrated Motion on EtherNet/IP Network application by using on of the following programming software applications.

- RSLogix 5000, version 19 and later
- Studio 5000 environment, version 21 and later

## Star Topology

A switch-level star configuration is a traditional Ethernet network layout where devices are connected to a centralized network switch, point-to-point. The star configuration is most effective when the devices are near a central network switch. In a star network topology, all traffic that traverses the network (that is, device-to-device) must pass through the central switch.

<!-- image -->

It is recommended that a managed switch with a transparent and/or boundary clock, plus QoS and IGMP protocol support be used for this Network topology.

Although the ControlLogix is illustrated, the CompactLogix controller could also be used.

## Advantages/Disadvantages

The advantage of a star network is that if a point-to-point connection is lost to an end device, the rest of the network remains operational.

The primary disadvantage of a star topology is that all end devices must typically be connected back to a central location, which increases the amount of cable infrastructure that is required and also increases the number of available ports required by the central switch leading to a higher cost per node solution.

## Linear Topology

In a linear topology, the devices are linked together via a two port embedded switch or through an EtherNet/IP network tap (1783-ETAP), instead of being connected back to a centralized network switch.

<!-- image -->

Either a Dual Port EtherNet/IP Option Module or an EtherNet/IP network tap (1783-ETAP) is required for this network topology (this diagram illustrates an application using the dual port option card). For more information about applying a Dual Port EtherNet/IP Option Module, see the PowerFlex 20-750ENETR Dual-Port EtherNet/IP Option Module User Manual, publication 750COM-UM008 .

Although the ControlLogix controller is illustrated, the CompactLogix controller could also be used.

## Advantages/Disadvantages

The advantages of a linear network include the following:

- The topology simplifies installation by eliminating long cable runs back to a centralized switch.
- The network can be extended over a longer distance because individual cable segments can be up to 100m.

- The network supports up to 50 mixed devices per line.

The primary disadvantage of a linear topology is that a connection loss or link failure disconnects all downstream devices as well. To counter this disadvantage a ring topology could be employed.

## Ring Topology

A ring topology, or device-level ring (DLR), is implemented in a similar fashion to linear topology. However, an extra connection is made from the last device on the line to the first, closing the loop or ring. It is crucial to configure the Ring Supervisor before connecting your linear topology into a ring topology.

<!-- image -->

Either a Dual Port EtherNet/IP Option Module or an Ethernet/IP network tap (1783-ETAP) is required for this network topology (this diagram illustrates an application using ETAPs). For more information about applying a Dual Port EtherNet/IP Option Module, see the PowerFlex 20-750-ENETR Dual-Port EtherNet/IP Option Module User Manual, publication 750COM-UM008 .

Although the ControlLogix is illustrated, the CompactLogix controller could also be used.

## Advantages/Disadvantages

The advantages of a ring network include the following:

- Simple installation
- Resilience to a single point of failure (cable break or device failure)
- Fast recover time from a single point of failure

The primary disadvantage of a ring topology is an additional setup (for example, active ring supervisor) as compared to a linear or star network topology.

## Linear/Star Topology

Network switches can be added to the end of the line, creating a linear/star topology. Ethernet devices that do not have embedded switch technology can be connected in a star topology off of the switch.

<!-- image -->

It is recommended that a managed switch with a transparent and/or boundary clock, plus QoS and IGMP protocol support be used for this Network topology.

Although the ControlLogix controller is illustrated, the CompactLogix controller could also be used.

## PowerFlex 755 and Kinetix 7000 Drive Overload Rating Comparison for Permanent Magnet Motor Operation

## Ring/Star Topology

Network switches can also be connected into a DLR via an Ethernet/IP tap, creating a ring/star topology.

<!-- image -->

It is recommended that a managed switch with a transparent and/or boundary clock, plus QoS and IGMP protocol support be used for this Network topology.

Although the ControlLogix controller is illustrated, the CompactLogix controller could also be used.

The PowerFlex 755 drive can be configured for a normal duty or heavy duty operation. The heavy duty rating has a lower continuous current rating and therefore can produce more current during an overload.

| Duty Rating 0 Hz 100% 110% 150% 180%   |                              |                             |                                                     |
|----------------------------------------|------------------------------|-----------------------------|-----------------------------------------------------|
|                                        |                              |                             | Normal 50% 100% One minute 3 seconds Not applicable |
|                                        | Heavy 65% 75% of normal duty | – One minute of normal duty | 3 seconds of normal duty                            |

The Kinetix 7000 drive overload capability is specific for each power structure. However, the Kinetix 7000 can produce 100% current at 0 Hz.

With permanent magnet motors, the torque is directly proportional to the current. Therefore, the overload ratings of the drive to which the motor is connected provides the torque overload capability of the motor.

## PowerFlex 755 Drive Option Module Configuration and Restrictions

When the PowerFlex 755 drive is configured for an Integrated Motion on the EtherNet/IP Network application, only specific option modules are supported, and in some cases, the port in which the option module is installed in the control pod is restricted.

## IMPORTANT

The PowerFlex 750-Series I/O option modules (20-750-2262C-2R, 20-7502263C-1R2T, 20-750-2262D-2R) must not be used with the Integrated Motion on the EtherNet/IP Network.

| Supported Modules                         | Valid Port Installation Location   |
|-------------------------------------------|------------------------------------|
| Cat. No. Option Module Name               |                                    |
| 20-750-S Safe Torque Off                  | 6                                  |
| 20-750-S1 Safe Speed Monitor              | 6                                  |
| 20-750-ENC Single Incremental Encoder 4…8 |                                    |
| 20-750-DENC Dual Incremental Encoder 4…8  |                                    |
| 20-750-UFB Universal Feedback             | 4…6                                |
| 20-750-APS Auxiliary Power Supply         | 8                                  |
| 20-750-ENETR Dual-Port Ethernet/IP        | 4 and 5                            |

If an unsupported option module is installed, the drive stops responding and the HIM displays "CONFIGURING."

## Safety Option Modules (20-750-S, 20-750-S1)

This restriction and configuration setting must be used when using either of these safety option modules with the Integrated Motion on the EtherNet/IP Network:

- The option modules must be installed in port 6 of the drive control pod only.
- The specific drive module and option catalog number must be selected when adding the drive to the I/O tree in the project. For example, when adding a PowerFlex 755 drive with a Safe Speed Monitor option module, choose 755-EENET-CM-S1.

## Feedback Option Modules (20-750-ENC, 20-750-DENC, and 20-750UFB)

Follow the same installation and configuration instructions provided in the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001 .

## Regenerative/Braking Resistor

## Auxiliary Power Supply Option Module (20-750-APS)

Follow the same installation and configuration instructions provided in the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001 .

## Dual-Port EtherNet/IP Option Module (20-750-ENETR)

Follow the same installation and configuration instructions provided in the PowerFlex 750-Series AC Drives Installation Instructions, publication 750IN001 .

When using a PowerFlex 755 drive with a dynamic brake (shunt regulator) in an Integrated Motion on the Ethernet/IP network the dynamic brake must be set up as part of the I/O connection of the PowerFlex 755 embedded Ethernet/IP module (EENET-CM-xx) properties. Failure to set up the dynamic brake correctly could lead to mechanical damage of the machine. Dynamic brake (shunt) resistor sizing is not covered in this document. For more information on resistor sizing, see the Drives Engineering Handbook, publication DEH-130010 .

## I/O Configuration for a Dynamic Brake (shunt regulator)

Follow these steps to configure a dynamic brake (shunt regulator) for a PowerFlex 755 drive in the Logix Designer application.

1. In the I/O Configuration, double-click the PowerFlex 755-EENET-CMxx x module and select Properties.

<!-- image -->

The Module Properties dialog box appears.

2. Click the Power tab and configure the appropriate boxes according to your application.

<!-- image -->

<!-- image -->

|                               | Regenerative Power Limit The amount of energy that the drive allows during regeneration. If an external regenerative power supply or shunt (dynamic brake) resistor is used, it is recommended that this value be set to -200.0%. Important: If this value is set too low, the ability of the drive to stop a motor is limited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bus Regulator Action          | •  Disabled - This selection disables the drive’s internal DC bus voltage regulation feature. Select this option if there is an external regenerative brake or regenerative line supply connected to the drive DC bus. •  Shunt Regulator - This selection is used when either an external shunt resistor is connected to the drive or the internal IGBT is controlling the power dissipation to the resistor (the type of shunt resistor is selected below). •  Adjustable Frequency - This selection let the drive either change the torque limits or ramp rate of the velocity to control the DC bus voltage. This option is not recommended for positioning applications because it overrides the velocity and the system can overshoot or may not stop. •  Shunt then Adjustable Frequency - This selection lets the Shunt resistor absorb as much energy as it is designed for, then transitions to adjustable frequency control if the limit of the resistor has been reached. •  Adjustable Frequency then Shunt - This selection enables adjustable frequency control of the DC bus. If adjustable frequency control cannot maintain the DC bus within limits, the shunt resistor is activated. |
| Shunt Regulator Resistor Type | Select the type of resistor connected to the drive. Internal resistors include 20-750-DB1-D1 or 20-750-DB1-D2 for frames 1 and 2 drives, respectively. External identifies that a user-selected resistor is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                               | External Shunt When using an external shunt resistor select “Custom.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

|                            | External Shunt Resistance Enter the resistance of the external resistor connected to the drive terminal block connections, BR1 and BR2. Verify that the resistance is equal to or greater than the minimum resistance for the drive capabilities. See “Minimum Dynamic Brake Resistance” in the PowerFlex 750-Series AC Drives Technical Data, publication 750-TD001 .   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                            | External Shunt Power Enter the continuous power dissipation rating (kW) of the external resistor. Failure to specify the correct value can cause the drive to either stop sending energy to the resistor prematurely or overheat the resistor. For example, if an 800 W rated resistor is installed, enter 0.8 in this field.                                            |
| External Shunt Pulse Power | The Watt-Second or Joules rating (kW) of the resistor. This is the amount of energy that the resistor can withstand for one second to reach the maximum temperature. Failure to specify the correct value can cause the drive to either stop sending energy to the resistor prematurely or overheat the resistor.                                                        |

3. Click OK.

## Safe Speed Monitor Option Module (20-750-S1) Configuration

When a PowerFlex 755 drive is configured for Integrated Motion on the EtherNet/IP Network the configuration of the Safe Speed Monitor functions are accomplished via a web page.

## Configuring the Safe Speed Functions

The Safe Speed Monitor module web page differs from the Embedded EtherNet/ IP adapter (port 13) web page that is enabled by setting adapter parameter P52 [Web Enable] to 1 "Enabled." The Safe Speed Monitor module web page is not accessible until the drive has established a network connection to a Logix processor and the Integrated Motion on the EtherNet/IP Network connection has been established. The web page is then accessed by entering the IP address of the drive into a web browser (for example, http://192.168.1.20/). Currently, safety configuration settings cannot be saved in the drive or downloaded to other drives.

<!-- image -->

TIP The Safe Speed Monitor module parameters are not currently part of the Logix platform and therefore, are not overwritten when a drive establishes a Integrated Motion on the EtherNet/IP Network connection. Therefore, it is possible to program the Safe Speed Monitor functions with configuration software (for example, Connected Components Workbench) or a HIM before a network connection is established. This lets you save the safety configuration in the software application or HIM. Configuration of the safety functions can be accomplished in one of the following ways:

- Program the Safe Speed Monitor functions and then download the program that includes the drive parameters to the Logix controller and establish the network connection.
- Inhibit the drive in the Logix I/O tree and program the Safe Speed Monitor functions.
- Disconnect the network cable between the drive and the controller and program the Safe Speed Monitor functions.

## Configuring the Stop Command

While there are different selections when operating the drive and Safe Speed Monitor option module in Standard mode versus the Integrated Motion on the EtherNet/IP Network mode, the equivalent functions operate the same. In the Integrated Motion on the EtherNet/IP Network mode of operation, the Stop Command is programmed in the Actions Category of the Module Properties dialog box. It is important to realize that there is no option to have a ramped stop selected here; only current limit and motor brake options are available. These selections do not ensure that a consistent ramp is implemented each time. If a repeatable ramped stop is desired, then the user can program a Stop Monitor Delay as a part of the Safe Speed Monitor configuration and then monitor the Safe Speed inputs from the controller and issue a ramped stop prior to the safety core issuing the Stop Command signal (as shown in this diagram).

<!-- image -->

(1) This signal is internal between the safety option module and the drive.

(2) The DC\_Out output is shown configured as Power to Release.

## Speed Limited Adjustable Torque (SLAT)

This topic describes how to configure a PowerFlex® 755 AC drive with embedded Ethernet/IP for Speed Limited Adjustable Torque (SLAT) operation using an Integrated Motion on the Ethernet/IP network in Logix Designer application. For more information on SLAT refer to the following publications:

- See Speed Limited Adjustable Torque (SLAT) Min Mode and SLAT Max Mode in the PowerFlex 700S AC Drives with Phase II Control Reference Manual, publication PFLEX-RM003 .
- See Slat Configuration in the Integrated Motion on the Ethernet/IP Network Reference Manual, publication MOTION-RM003 .

## Add a PowerFlex 755 Drive Module to Your Project

See the Integrated Motion on the Ethernet/IP Network Configuration and Startup User Manual, publication MOTION-UM003, for specific instructions on adding a PowerFlex 755 with embedded Ethernet/IP drive module to your project. An example Module Properties dialog box for a PowerFlex 755 with embedded Ethernet/IP is shown here.

<!-- image -->

## Create and Configure an Axis for the PowerFlex 755 Drive

1. See the Integrated Motion on the Ethernet/IP Network Configuration and Startup User Manual, publication MOTION-UM003, for specific instructions on creating and configuring the axis for the PowerFlex 755 drive.

2. In the General dialog, from the Axis Configuration pull-down menu, choose Velocity Loop.
3. Select the Velocity Loop category.

<!-- image -->

The Velocity Loop dialog box appears.

4. Click Parameters.

The Motion Axis Parameters dialog box appears.

<!-- image -->

5. Configure the SLAT parameters. See Slat Configuration in the Integrated Motion on the Ethernet/IP Network Reference Manual, publication MOTION-RM003, for a complete list and descriptions of the SLAT parameters.

<!-- image -->

## Program Commands

When using SLAT with Integrated Motion on the Ethernet/IP network you must start the PowerFlex 755 drive with the MDS instruction as shown below. The Speed reference is sent in the MDS instruction. Also, the torque command is sent to "AxisTag.CommandTorque." To make changes to the speed reference you need to re-trigger the MDS instruction.

<!-- image -->

To use the Motion Axis Stop (MAS) instruction, you must set Change Decel to "No." Otherwise an instruction error occurs. The deceleration rate is set based on the Ramp Deceleration attribute.

To view help for the MDS instructions, right-click MDS in the function block and choose Instruction Help, or select the instruction and press F1. Additionally, see "Speed Limited Adjustable Torque (SLAT) Min Mode and SLAT Max Mode" in the PowerFlex 700S AC Drives with Phase II Control, Reference Manual, publication PFLEX-RM003 .

<!-- image -->

## Changing the Accel/Decel Times for the MDS Instruction

If you are using the MDS instruction, the drive accelerates and decelerates at the planner Max Acceleration and Deceleration values. To set the

"RampAcceleration" and "RampDeceleration" you need to use SSV instructions to change the ramp rates. Below is an example of the SSV instructions:

- Set the RampAcceleration / RampDeceleration attribute to "x" revs/sec 2
- Class Name = Axis
- Instance Name = "Axis Name"
- Attribute Name = RampAcceleration/RampDeceleration
- Source = Tag for value

Example: Velocity (Speed) command is 30 revs/sec and you want to reach that speed from zero in 6.5 seconds. Ramp Acceleration needs to be set to 4.615 revs/ sec 2 .

<!-- image -->

## Supported Motors

The PowerFlex 755 can be used with a variety of both induction and permanent magnet (PM) motors.

## AC Induction Motors

An AC induction motor uses slip between the rotor and the stator to create torque. Some motor manufacturers specify the synchronous speed instead of slip speed on the motor nameplate. For example, a 4 pole, 60 hertz motor has a synchronous speed of 1800 rpm. The drive algorithm cannot use the synchronous speed, it needs the slip rpm. The slip rpm is the rotor speed when the stator is at rated frequency and the motor is at full load. The rotor slips behind the stator to create the torque. For a 4 pole, 60 hertz motor the slip rpm range is 1700…1790 rpm. If the nameplate is showing synchronous speed (in our example 1800 rpm), please contact the motor manufactures to receive the slip rpm.

Some AC motors have two voltage ratings, a high voltage and a low voltage. Follow the motor manufacture's wiring diagram to correctly wire the motor for the proper voltage.

All motor manufactures provide an electrical specification including an electrical model equivalent. If you believe that the PowerFlex drive family is not producing the correct motor torque, please contact the motor manufacturer to receive the electrical specification prior to contacting Rockwell Automation Technical Support.

This list contains the name of manufacturers that produce motors that are recommended for use with PowerFlex 755 drives.

| Manufacturer            | Notes                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Baldor Electric Company | Work well with PowerFlex 755 drives.                                                                                                                                                                                                                                                                                                                                                                             |
| Baumuller               | Work well with PowerFlex 755 drives.                                                                                                                                                                                                                                                                                                                                                                             |
| Elin                    | Work well with PowerFlex 755 drives.                                                                                                                                                                                                                                                                                                                                                                             |
|                         | Electrical Apparatus Company (EAC) Induction motors work well with PowerFlex 755 drives.                                                                                                                                                                                                                                                                                                                         |
| Lenze                   | Some Lenze motors have been stamped with synchronous speed versus slip speed. Please contact Lenze to get the slip speed.                                                                                                                                                                                                                                                                                        |
| Marathon Electric       | Work well with PowerFlex 755 drives. Marathon stamps all pertinent information on their nameplate including electrical model equivalent.                                                                                                                                                                                                                                                                         |
| Reliance                | RPM AC motors are used in industry and work well with PowerFlex 755 drives.                                                                                                                                                                                                                                                                                                                                      |
|                         | Reuland Electric Company, Inc. Work well with PowerFlex 755 drives. Reuland stamps the motor with synchronous speed and then supplies the slip frequency. You must calculate the slip frequency in rpm and then subtract the slip rpm from the synchronous speed to get the slip speed. Before contacting Rockwell Automation Technical Support, please obtain the electrical specification sent with the motor. |
| Rockwell Automation     | 8720 and HPK motors work well with PowerFlex 755 drives. See the appropriate motor manual for the proper nameplate voltage.                                                                                                                                                                                                                                                                                      |
| SEW-EURODRIVE           | SEW-EURODRIVE gear motors are widely used in industry and work well with PowerFlex 755 drives. Some of the older motors were stamped with synchronous speed versus slip speed. Please contact SEWS if the motor is stamped with synchronous speed. If you are using an SEW motor with an integral brake, please verify that the brake is properly suppressed for noise.                                          |

| Manufacturer       | Notes                                                                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| WEG Electric Corp. | WEG motors can have a start winding and a run winding. Always wire the drive to the run winding.                                      |
| Wittenstein        | Work well with PowerFlex 755 drives.                                                                                                  |
|                    | Wound rotor manufacturers Wound Rotors work with PowerFlex 755 drives. You must short the external resistors when using these motors. |

## Permanent Magnet Motors

Most permanent magnet motors are compatible with the PowerFlex 755 drive. You must obtain the motor manufacturer's specification for the motor prior to contacting Rockwell Automation Technical Support.

PowerFlex 755 drives cannot accept a resolver. Therefore, the motors must have either a pulse encoder or absolute feedback device (for example, SSI, Heidenhain, Stegmann/Sick hyperface).

This list contains the name of manufacturers that produce motors that are recommended for use with PowerFlex 755 drives.

| Manufacturer            | Notes                                                                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Baldor Electric Company | Work well with PowerFlex 755 drives. Verify that you are using either the Surface Mount (SM) or Interior Mounted (IPM) motors and select the appropriate control algorithm. |
| KollMorgan              | Work well with PowerFlex 755 drives.                                                                                                                                        |
| Oswald Electric Motors  |                                                                                                                                                                             |
| PowerTec                | Work well with PowerFlex 755 drives, but cannot use resolver feedback.                                                                                                      |
| Rockwell Automation     | MPL, MPM, and RDB motors work well with PowerFlex drives. Use Heidenhain feedback for RDB motors.                                                                           |

## Compatible HPK Motors

The following table contains a list of specifications for Bulletin HPK-Series™ high-power asynchronous motors that are compatible with PowerFlex 750-Series drives. This information is provided to help configure PowerFlex 750-Series drives with the appropriate motor data.

| Cat. No.  Base Speed (N•m) Peak Amps                                                      | KW Volts Amps Hz Torque   | Peak Torque (N•m)   | IM Amps   | R1 R2 X1 X2 Xm   |
|-------------------------------------------------------------------------------------------|---------------------------|---------------------|-----------|------------------|
| HPK-B1307C-MA42AA 1465 17.1 400 34.2 50 112 260 80 15.8 0.181 0.119 0.65 0.704 14.7       |                           |                     |           |                  |
| HPK-B1307C-SA42AA 1465 17.1 400 34.2 50 112 260 80 15.8 0.181 0.119 0.65 0.704 14.7       |                           |                     |           |                  |
| HPK-B1307E-MA42AA 2970 29.8 405 57.5 100 96 165 104 26.1 0.0485 0.0338 0.371 0.423 8.79   |                           |                     |           |                  |
| HPK-B1307E-MB44AA 2970 29.8 405 57.5 100 96 165 104 26.1 0.0485 0.0338 0.371 0.423 8.79   |                           |                     |           |                  |
| HPK-B1307E-MC44AA 2970 29.8 405 57.5 100 96 165 104 26.1 0.0485 0.0338 0.371 0.423 8.79   |                           |                     |           |                  |
| HPK-B1307E-SA42AA 2970 29.8 405 57.5 100 96 165 104 26.1 0.0485 0.0338 0.371 0.423 8.79   |                           |                     |           |                  |
| HPK-B1307E-SB44AA 2970 29.8 405 57.5 100 96 165 104 26.1 0.0485 0.0338 0.371 0.423 8.79   |                           |                     |           |                  |
| HPK-B1308E-MA42AA 2970 33.5 405 64.8 100 115 230 135 28.8 0.037 0.0275 0.296 0.364 7.71   |                           |                     |           |                  |
| HPK-B1308E-MB44AA 2970 33.5 405 64.8 100 115 230 135 28.8 0.037 0.0275 0.296 0.364 7.71   |                           |                     |           |                  |
| HPK-B1308E-SA42AA 2970 33.5 405 64.8 100 115 230 135 28.8 0.037 0.0275 0.296 0.364 7.71   |                           |                     |           |                  |
| HPK-B1308E-SB44AA 2970 33.5 405 64.8 100 115 230 135 28.8 0.037 0.0275 0.296 0.364 7.71   |                           |                     |           |                  |
| HPK-B1609E-MA42AA 2965 48.4 405 88.2 100 156 270 154 31.4 0.0326 0.0227 0.288 0.319 7.23  |                           |                     |           |                  |
| HPK-B1609E-SA42AA 2965 48.4 405 88.2 100 156 270 154 31.4 0.0326 0.0227 0.288 0.319 7.23  |                           |                     |           |                  |
| HPK-B1609E-SB44AA 2965 48.4 405 88.2 100 156 270 154 31.4 0.0326 0.0227 0.288 0.319 7.23  |                           |                     |           |                  |
| HPK-B1609E-X169 2965 48.4 460 88.2 154 156 270 154 154 154 154 154 154 154                |                           |                     |           |                  |
| HPK-B1611E-MA42AA 2975 57 408 105.7 100 183 400 240 47.6 0.0205 0.0152 0.167 0.219 4.82   |                           |                     |           |                  |
| HPK-B1611E-MB44AA 2975 57 408 105.7 100 183 400 240 47.6 0.0205 0.0152 0.167 0.219 4.82   |                           |                     |           |                  |
| HPK-B1611E-SA42AA 2975 57 408 105.7 100 183 400 240 47.6 0.0205 .0.0152 0.167 0.219 4.82  |                           |                     |           |                  |
| HPK-B1613E-MA42AA 2970 73.7 407 135.3 100 237 520 312 54.5 0.0164 0.0127 0.136 0.179 4.21 |                           |                     |           |                  |
| HPK-B1613E-MB44AA 2970 73.7 407 135.3 100 237 520 312 54.5 0.0164 0.0127 0.136 0.179 4.21 |                           |                     |           |                  |
| HPK-B1613E-SA42AA 2970 73.7 407 135.3 100 237 520 312 54.5 0.0164 0.0127 0.136 0.179 4.21 |                           |                     |           |                  |
| HPK-B1613E-SB44AA 2970 73.7 407 135.3 100 237 520 312 54.5 0.0164 0.0127 0.136 0.179 4.21 |                           |                     |           |                  |

| Cat. No. Base Speed (N•m)                                                   | KW Volts Amps Hz Torque   | Peak Torque (N•m)   | Peak Amps IM Amps R1 R2 X1 X2 Xm                                                       |
|-----------------------------------------------------------------------------|---------------------------|---------------------|----------------------------------------------------------------------------------------|
|                                                                             |                           |                     | HPK-B2010E-MA42BA 2985 112 400 216 100 358 35 0.00519 0.00419 0.0626 0.097 2.03        |
|                                                                             |                           |                     | HPK-B2010E-SA42BA 2985 112 400 216 100 358 35 0.00519 0.00419 0.0626 0.097 2.03        |
|                                                                             |                           |                     | HPK-E1308E-MA42AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1308E-MB44AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1308E-MC44AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1308E-SA42AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1308E-SB44AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1308E-SC44AA 2975 33.5 330 80 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92   |
|                                                                             |                           |                     | HPK-E1609E-MA42AA 2965 48.4 405 88.2 100 108 216 160 39 0.0233 0.0176 0.189 0.242 4.92 |
| HPK-E1613E-SA42AA 2975 73.7 400 172 385 237 520 385 385 385 385 385 385 385 |                           |                     |                                                                                        |

## Third-Party Permanent Magnet Motors

The PowerFlex 755 drive can support third-party permanent magnet motors without the need of custom profiles. However, the motor nameplate information sometimes needs to be modified. Rockwell Automation Technical Support requires the following information to assist you in modifying the motor data for use with the drive. Please complete the following tables and email the information to Rockwell Automation Technical Support at: support@drives.ra.rockwell.com .

Table 27 - Permanent Magnet Motor Specifications and Evaluation

| Motor Manufacturer    |                                                   |
|-----------------------|---------------------------------------------------|
| Model Number          |                                                   |
| Feedback Device       |                                                   |
| Type of Feedback      | If resolver, please complete resolver information |
| Feedback Manufacturer |                                                   |
| Feedback Model Number |                                                   |

| Technical Specifications                            |                               |                     |                     |
|-----------------------------------------------------|-------------------------------|---------------------|---------------------|
|                                                     | Item Symbol Value Units Notes |                     |                     |
| Maximum Mechanical Speed n                          | rpm                           |                     |                     |
| Continuous Stall Torque Ms                          |                               | Nm (RMS not 0-peak) | Nm (RMS not 0-peak) |
| Continuous Stall Current A                          |                               | A (RMS not 0-peak)  | A (RMS not 0-peak)  |
| Peak Torque Mj                                      |                               | Nm (RMS not 0-peak) | Nm (RMS not 0-peak) |
| Torque Weight Ratio Tw                              | Nm/Kg                         |                     |                     |
| EMF Constant Ke                                     | Vs/rad                        |                     | Vs/1000rpm          |
| Torque constant Kt                                  | Nm/A                          |                     |                     |
| Reluctance Torque (with respect to Stall Torque) Tr | Nm                            |                     |                     |
| Winding Resistance R                                | Ohms                          |                     | line to line        |
| Winding Inductance L                                | mH                            |                     | line to line        |
| Rotor Inertia J                                     | kg-m2                         |                     |                     |
| Mechanical Time Constant Тm                         | ms                            |                     |                     |
| Electrical Time Constant Тe                         | ms                            |                     |                     |
| Mass M                                              | Kg                            |                     |                     |
| Radial Load Fr                                      | N                             |                     |                     |
| Axial Load Fa                                       | N                             |                     |                     |
| Insulation                                          |                               |                     |                     |
| Protection                                          |                               |                     |                     |

| Motor Nameplate Voltage V   | Volts   |
|-----------------------------|---------|
| Motor Nameplate Power Pwr   | KW      |
| Poles p                     |         |

## Table 28 - Drive Motor Parameter Values

| Parameter                      | Value   | Units   |
|--------------------------------|---------|---------|
| P1: Motor Nameplate volts Vrms |         | Volts   |
| P2: Motor Nameplate Amps       |         | Amps    |
| P3: Motor Nameplate Frequency  |         | HZ      |
| P4: Motor Nameplate RPM        |         | RPM     |
| P5: Motor Name Plate Power     |         | KW      |
| P7: Pole Pairs                 |         |         |
| Zpu                            |         |         |
| IXO Voltage drop               |         | Volts   |
| IR Voltage Droop               |         | Volts   |
| P523 Back Emf                  |         | Volts   |

Provide a Speed Torque profile like in this example.

<!-- image -->

## System Tuning

When using the Integrated Motion on the Ethernet/IP Network connection with the PowerFlex 755 drive, the tuning of the motion system is accomplished via the Logix Designer application. This topic describes the axis hookup tests, motor tests, and autotuning of the motion system required to measure the system inertia. Manual tuning of the axis is also described in this section:

- For additional information on axis attributes and the Control Modes and Methods, see the Integrated Motion on the Ethernet/IP Network Reference Manual, publication MOTION-RM003 .
- For start-up assistance of a Integrated Motion on the EtherNet/IP Network Axis, see the Integrated Motion on the Ethernet/IP Network Configuration and Startup User Manual, publication MOTION-UM003 .

This topic assumes that you have completed all the steps necessary to configure the drive module.

## Axis Hookup Tests

The axis Hookup tests are the first tests to run when autotuning an axis. If you are using a permanent magnet motor in your application, the Commutation test must be run first, as part of the Hookup tests.

<!-- image -->

Motor and Feedback: This test is used to run the motor and verify the correct direction of rotation, and also tests the motor feedback for the proper direction:

- The Test Distance value can be defined to be sure that the system does not rotate too far.
- Click Start to initiate the test. The test completes and prompts you to verify that the motor rotation direction was correct.

- When the test has been completed, click Accept Test Results to save the results.

Motor Feedback: This test is used to test the polarity of the motor feedback:

- Click Start and manually rotate the motor in the positive direction for the distance indicated in the Test Distance box.
- When the test has been completed, click Accept Test Results to save the results.

Commutation: When using a permanent magnet motor, this test must be run first. The Commutation test is used to measure the commutation offset angle for the permanent magnet motor.

- When the test has been completed, click Accept Test Results to save the results.
- Use the resulting Controller Offset value.

Marker: This test is used to check for the marker pulse on an incremental encoder:

- Click Start and manually move the motor until a marker pulse is detected.
- When the marker pulse is detected the test stops. Click Accept Test Results to save the results.

## Motor Analyzer

The Motor Analyzer category offers three choices for calculating or measuring motor electrical data.

<!-- image -->

Dynamic Motor Test: This test is the most accurate test method to determine the motor model parameters. When this test is run the Resistance and Reactance

are measured then the motor is rotated to measure the flux current of the Induction motor. The Rated Slip frequency is also calculated:

- This test is best run with the motor disconnected from the load as the motor spins for some time and there are no travel limits.
- When the test has been completed, click Accept Test Results to save the results.

Static Motor Test: This test is used if the motor cannot rotate freely or is already coupled to the load. When this test is run the Resistance and Reactance are measured then the flux current of the motor is calculated. The Rated Slip frequency is also calculated:

- The motor will not turn during this test.
- When the test has been completed, click Accept Test Results to save the results.

Calculate Model: This method calculates the Resistance, Reactance, and Flux Current of the motor from basic model parameters and the motor parameters data. No measurements are taken when using this calculation:

- Click Start to start the calculation.
- When the test has been completed, click Accept Test Results to save the results.

## Autotune (inertia test)

The Autotune category measures the system inertia and calculates system bandwidth tuning numbers. This table summarizes the application type tuning defaults. An "X" indicates that the system value is selected by default and that the Velocity and Acceleration Feedforward values are set to 100%.

| Application Type                                                          | System Value                                                                  |                               |                                      |                          |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------|--------------------------------------|--------------------------|
|                                                                           | Position Loop Bandwidth Position Integrator Bandwidth Velocity Loop Bandwidth | Velocity Integrator Bandwidth | Integrator Hold Velocity Feedforward | Acceleration Feedforward |
| Custom: (Advanced tuning)                                                 | X X                                                                           |                               |                                      |                          |
| Basic: (Default tuning parameters)                                        | X X                                                                           |                               |                                      |                          |
| Tracking: (Winding/unwinding, flying shear, and web control applications) | X X                                                                           |                               | X X                                  | X                        |
| Point-to-Point: (Pick-and-place, packaging, cut-to length)                                                                           | XXX                                                                           |                               | X                                    |                          |
| Constant Speed: (Conveyors, line shaft, crank)                            | X X                                                                           |                               | X X                                  |                          |

<!-- image -->

Application Type: Specify the type of motion control application to be tuned:

- Custom: This option lets you select the type of gains to use in the system. You can individually select gains to be used with the check boxes that display below Customize Gains to Tune heading.
- Basic: This selection is used for applications where following error and final position is not critical. Basic tuning gains include Position Loop proportional and Velocity Loop proportional.
- Tracking: This selection provides the most aggressive tuning. It is used to keep following error to a minimum and applies to both Velocity Feedforward and Acceleration Feedforward. This tuning selection uses Position Loop proportional, Velocity Loop proportional, and Velocity Loop integral.
- Point to Point: This selection is used for applications that use a move-toposition and do not need to include a following error. Tuning gains for this selection include Position Loop proportional, Position Loop integral, and Velocity Loop proportional.
- Constant Speed: This selection is used for constant speed applications. It is designed to keep velocity error to a minimum. It applies both Velocity Feedforward and uses Position Loop proportional, Velocity Loop proportional and Velocity Loop integral.

Loop Response: The Loop Response attribute is used to determine the responsiveness of the control loops. Specifically, the Loop Response attribute is used to determine the value for the Damping Factor (Z) used in calculating individual gain values:

- High = 0.8
- Medium = 1.0
- Low = 1.5

Load Coupling: The Load Coupling attribute is used to determine how the loop gains are de-rated based on the Load Ratio.

In high performance applications with relatively low Load Ratio values or rigid mechanics, typically Rigid is selected. The gains are not de-rated.

For applications with relatively high Load Ratios and compliant mechanics, Compliant is selected. The autotune algorithm divides the nominal loop bandwidth values by a factor of the Load Ratio + 1.

Measure Inertia using Tune Profile: Check this box to calculate the inertia tuned values as part of the autotune. The Inertia Test results are shown in the Inertia Tuned grid control (bottom right of the dialog box) when the test completes.

When Measure Inertia using Tune Profile is selected as a part of the Autotune test, the PowerFlex 755 drive first jogs or rotates the motor in a single direction to remove any backlash present in the system (as depicted in the chart below). After the backlash has been removed, the "bump" profile is then applied to measure the system inertia (system acceleration). Note that systems with a mechanical restriction or travel limit may not complete the Autotune test.

<!-- image -->

- Motor with Load: Choose this selection to calculate tuning values based on the load inertia. If selected, the load inertia is measured and then applied to the Total Inertia attribute or Total Mass attribute. The Load Ratio is also updated.
- Uncoupled Motor: Choose this selection to calculate tuning values based on the motor inertia. If selected, the motor inertia is measured during the test and is stored in the Rotary Motor Inertia attribute.
- Travel Limit: Enter a value that specifies the maximum distance to travel for the selected tune operation when the system has a limited travel distance. If the tuning test cannot complete within the distance specified the tune fails and faults the axis.
- Speed: Enter a value that specifies the speed of the tune operation. A speed that translates to a minimum of 25% of the motor nameplate RPM is recommended.
- Torque: Enter a value in the range of 0…300 that specifies the torque value to be applied to the tune operation. The default value is 100.
- Direction: Choose the direction of the move for the tune operation. The available values include:
- Forward Unidirectional (default)
- Reverse Unidirectional
- Forward Bi-Directional
- Reverse Bi-Directional

## Run the Autotune

To start the autotune procedure, click Start:

- When the Measure Inertia using Tune Profile check box is selected, the request to start a tune is issued to the controller.
- Any pending edits in this dialog box need to be applied before you start the test. If you have pending edits, a message box appears informing you that pending edits are applied prior to executing the test. Click Yes to apply the pending edits. If you choose No, the test is not be executed.
- Clicking Start issues a Motion Direct command to the controller, which causes any parameters used by the motion direct command to validate before starting the test.
- If the Motion Direct command does not execute due to an error condition, an error message appears and the Test State returns to the Ready state.
- Click Stop to terminate an autotune operation that was started from a source other than Start on this Autotune dialog box. When an Autotune is started from Start on this dialog box, Stop is unavailable.

When the autotune has completed, click Accept Tuned Values to accept the tuning results and before you can change any tuning categories.

## Manual Tune

The Integrated Motion on the Ethernet/IP network axis includes a method for manual tuning the axis gains. Clicking Manual Tune (as indicated in the example here) opens the Manual Tuning window.

<!-- image -->

## Manual Tuning Window

Tuning gains are measured in Hertz in the Integrated Motion on the Ethernet/IP network connection compared to the radians/second in the stand alone drive. 6.283185 Rad/Sec = 1 Hz.

<!-- image -->

The Manual Tuning window contains three sections:

Manual Tuning Section: This section lets you customize the configuration of system tuning. The following two selections can be made:

- System Bandwidth: Changing this value adjusts the Position Loop and Velocity Loop response. The value selected in this field changes the Application Type selection in the Autotune window. Therefore, care must be taken to NOT change this value after the individual gains have been manually configured.
- System Dampening: Changing this value adjusts both the Dampening factor and System Bandwidth values. Lowering the System Dampening factor dramatically increases the System Bandwidth. Care must be taken when changing this value to avoid machine damage. It is recommended that small incremental adjustments be made to the System Dampening while evaluating the overall system response. This value changes the Application Type selection in the Autotune window. Therefore, care must be taken to NOT change this value after the individual gains have been manually configured.

- Position Loop: You can manually adjust the Loop Bandwidth, Integrator Bandwidth, Integrator Hold and Error Tolerance values.
- Velocity Loop: You can manually adjust the Loop Bandwidth, Integrator Bandwidth, Integrator Hold, and Error tolerance (when used as a Velocity Loop) values.

Motion Generator Section: The Motion Generator is a subset of the Motion Direct commands that lets you control the axis motion for tuning.

Additional Tune Section: This section enables adjustment of multiple settings of the axis properties:

- Feedforward Tab: Lets you adjust the Velocity Feedforward percentage and Acceleration Feedforward percentage.
- Compensation Tab: Lets you adjust the System Inertia percentage and Torque Offset percentage.
- Filters Tab: Lets you adjust the Torque Low Pass Filter Bandwidth and Torque Notch Filter Frequency.
- Limits Tab: Lets you adjust the Peak Torque Limit Positive / Negative percentages and Velocity Limit Positive / Negative Units per Second values.
- Planner Tab: Lets you adjust the Maximum Speed, Maximum Acceleration, Maximum Deceleration, Maximum Acceleration Jerk, and Maximum Deceleration Jerk values.

## Using an Incremental Encoder with an MPx Motor

The PowerFlex 755 drive supports incremental encoder feedback when using a Rockwell Automation MPx motor. However, the Motor Device Specification category in the Axis Properties configuration for the Logix Designer application does not currently support MP-Series™ motors with incremental feedback catalog numbers, as shown below. Only MP-Series motors with the suffix –M (Stegmann Multi-turn Absolute), or –S (Single Turn Absolute) motors are supported.

<!-- image -->

To configure a PowerFlex 755 drive with an MPx motor equipped with incremental encoder feedback, the MPx motor must be set up as a third-party motor. Follow these steps to configure an MPx motor with incremental encoder feedback for use with a PowerFlex 755 drive using the Integrated Motion on the EtherNet/IP Network.

1. In the Axis Properties dialog box for the drive, select these options (as shown below):
- From the Data Source pull-down menu, choose Nameplate Datasheet.
- From the Motor Type pull-down menu, choose Rotary Permanent Magnet.
2. You must manually enter the Nameplate / Datasheet – Phase to Phase parameters information. See Appendix D - Permanent Magnet Motors in the PowerFlex 750-Series Programming Manual, publication 750-PM001 , for a list of motor nameplate specification data.

<!-- image -->

TIP If you do not have a Programming Manual readily available, from the Data Source pull-down menu, choose Catalog Number. Then, from the Motor Type pull-down menu, choose the equivalent motor with the -M (Stegmann Multiturn Absolute) device. The Logix Designer application populates the Nameplate / Datasheet – Phase to Phase parameters information with the data that is stored in the database. Record this information for reference. Then, change the Data Source selection to "Nameplate Datasheet." The configuration is transferred to the new selection. The motor data is the same regardless of the selected feedback device.

3. Select the Motor Feedback category.
4. From the Type pull-down menu, choose Digital AqB.
5. Click OK to save your configuration.

<!-- image -->

## PowerFlex 755 Integrated Motion on the EtherNet/IP Network Block Diagrams

The block diagrams in this section highlight the Integrated Motion on the Ethernet/IP Network attributes and path used in PowerFlex 755 drives control. When viewed in electronic format (PDF), or when printed in color, the standard drive control attributes and path appear in blue and the Integrated Motion on the EtherNet/IP Network attributes appear in black and the path appears in black and uses heavier line weights.

Integrated Motion on the Ethernet/IP Network Attributes and Path

<!-- image -->

## Legend and Definitions

Use the following legend and definitions when viewing the diagrams.

Definitions of the Per Unit system:

1.0 PU Position = Distance traveled / 1sec at Base Spd

1.0 PU Speed = Base Speed of the Motor 1.0 PU Torque = Base Torque of the Motor

<!-- image -->

## Block Diagram Table of Contents

| Block Diagram                                                                | Page Block Diagram                                                                                                  | Page   |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------|
| Flux Vector Overview                                                         | 377 Torque Control Overview - Interior Permanent Magnet Motor                                                       | 398    |
| VF (V/Hz), SV Overview                                                       | 378 Torque Control - Reference Scale and Trim 399                                                                   |        |
| Speed / Position Feedback                                                    | 379 Torque Control - Torque                                                                                         | 400    |
|                                                                              | Speed Control - Reference Overview 380 Torque Control - Current, Induction Motor and Surface Permanent Magnet Motor | 401    |
|                                                                              | Speed Control Reference (Sheet 1) 381 Torque Control - Current, Interior Permanent Magnet Motor                     | 402    |
| Speed Control Reference (Sheet 2) 382 Torque Control - Inertia Adaption      |                                                                                                                     | 403    |
|                                                                              | Speed Control Reference (Sheet 3) 383 Torque Control - Load Observer / Estimator 404                                |        |
| Speed Control Reference (Sheet 4) 384 Process Control (Sheet 1)              |                                                                                                                     | 405    |
| Speed Control Reference (Sheet 5) 385 Process Control (Sheet 2)              |                                                                                                                     | 406    |
| Speed Control - Regulator (Flux Vector) 386 MOP Control                      |                                                                                                                     | 407    |
| Position Control - Reference                                                 | 387 Inputs and Outputs - Digital                                                                                    | 408    |
| Position Control - Regulator                                                 | 388 Inputs and Outputs - Analog                                                                                     | 409    |
| Position Control - Aux Functions                                             | 389 11-Series Inputs and Outputs – Digital 410                                                                      |        |
| Position Control - Phase Locked Loop 390                                     | 11-Series Inputs and Outputs – Analog 411                                                                           |        |
| Position Control - Position CAM                                              | 391 11-Series Inputs and Outputs – ATEX 412                                                                         |        |
| Position Control - Profiler/Indexer (Sheet 1) 392 Control Logic              |                                                                                                                     | 413    |
| Position Control - Profiler/Indexer (Sheet 2) / Position Control - Homing    | 393 Inverter Overload IT                                                                                            | 414    |
| Position Control / Aux Functions, Roll Position Indicator                    | 394 Friction Compensation                                                                                           | 415    |
| Position Control – Spindle Orient                                            | 395 Variable Boost Voltage Overview – Function Inputs/Outputs                                                       | 416    |
| Position Control / Aux Functions, Position Oriented Torque Boost             | 396 Diagnostic Tools                                                                                                | 417    |
| Torque Control Overview - Induction Motor and Surface Permanent Magnet Motor | 397 High Speed Trending Wizard                                                                                      | 418    |

## Flux Vector Overview

<!-- image -->

VF (V/Hz), SV Overview

<!-- image -->

## Speed / Position Feedback

<!-- image -->

## Speed Control - Reference Overview

<!-- image -->

## Speed Control Reference (Sheet 1)

<!-- image -->

## Speed Control Reference (Sheet 2)

<!-- image -->

## Speed Control Reference (Sheet 3)

<!-- image -->

## Speed Control Reference (Sheet 4)

<!-- image -->

## Speed Control Reference (Sheet 5)

<!-- image -->

<!-- image -->

## Position Control - Reference

<!-- image -->

## Position Control - Regulator

<!-- image -->

Position Control - Aux Functions

<!-- image -->

## Position Control - Phase Locked Loop

<!-- image -->

## Position Control - Position CAM

<!-- image -->

PF755 Rev\_9.a
Page 15

## Position Control - Profiler/Indexer (Sheet 1)

<!-- image -->

Position Control - Profiler/Indexer (Sheet 2) / Position Control - Homing

<!-- image -->

## Position Control / Aux Functions, Roll Position Indicator

<!-- image -->

## Position Control – Spindle Orient

<!-- image -->

## Position Control / Aux Functions, Position Oriented Torque Boost

<!-- image -->

Torque Control Overview - Induction Motor and Surface Permanent Magnet Motor

<!-- image -->

<!-- image -->

## Torque Control - Reference Scale and Trim

<!-- image -->

Torque Control - Torque

<!-- image -->

<!-- image -->

<!-- image -->

Torque Control - Inertia Adaption

<!-- image -->

PF755 Rev\_9.a
Page 25

Torque Control - Load Observer / Estimator

<!-- image -->

## Process Control (Sheet 1)

<!-- image -->

## Process Control (Sheet 2)

<!-- image -->

MOP Control

<!-- image -->

Inputs and Outputs - Digital

<!-- image -->

Inputs and Outputs - Analog

<!-- image -->

11-Series Inputs and Outputs – Digital

<!-- image -->

## 11-Series Inputs and Outputs – Analog

<!-- image -->

11-Series Inputs and Outputs – ATEX

<!-- image -->

## Control Logic

<!-- image -->

## Inverter Overload IT

<!-- image -->

## Friction Compensation

<!-- image -->

## Variable Boost Voltage Overview – Function Inputs/Outputs

<!-- image -->

<!-- image -->

## High Speed Trending Wizard

<!-- image -->

<!-- image -->

## PowerFlex 755 Standard and Safety Drive Module Optional Attributes

The following table specifies what optional attribute and corresponding control mode functionality is supported by a PowerFlex 755 drive module when using the Logix Designer application.

Y = The attribute/enum/bit is supported

N = The attribute/enum/bit is not supported

R = The attribute is required

## Control Modes

- N = No Control Mode
- F = Frequency Control Mode
- P = Position Control Mode
- V = Velocity Control Mode
- T = Torque Control Mode

For more information on the Control Modes, see Integrated Motion on the Ethernet/IP Network Reference Manual, publication MOTION-RM003 .

The Integrated Motion on the Ethernet/IP Network Reference Manual provides a programmer with details about the Integrated Motion on the Ethernet/IP Network Control Modes, Control Methods, and AXIS\_CIP\_DRIVE Attributes.

Table 29 - Conditional Implementation Key

| Key           | Description                                                                      |
|---------------|----------------------------------------------------------------------------------|
| AOP           | Special device specific semantics needed from AOP                                |
| Co            | Controller only attribute (controller attribute that resides only in controller) |
| C/D           | Yes = The attribute is replicated in the drive                                   |
| CScale        | Motion Scaling Configuration set to Controller Scaling                           |
| Derived       | Implementation rules follow another attribute                                    |
| Dr            | Drive replicated attribute (controller attribute that is replicated in drive)    |
| Drive Scaling | Drive device supports drive scaling functionality                                |
| DScale        | Motion Scaling Configuration set to Drive Scaling                                |
| E21           | EnDat 2.1® (feedback type)                                                       |
| E22           | EnDat 2.2® (feedback type)                                                       |
| E             | Encoder-based control, a feedback device is present                              |
| !E            | Encoderless or sensorless control, a feedback device in not present              |
| HI            | Hiperface® (feedback type)                                                       |

Table 29 - Conditional Implementation Key

| Key          | Description                                                                |
|--------------|----------------------------------------------------------------------------|
|              | IM Rotary or Linear Induction Motor (motor type)                           |
|              | Linear Absolute Feedback Unit - meter; Feedback n Startup Method- absolute |
| Linear Motor | Linear PM motor or Linear Induction motor (motor type)                     |
| LT           | LDT or Linear Displacement Transducer (feedback type)                      |
| NV           | Motor NV or Drive NV (motor data source)                                   |
| O-Bits       | Optional bits associated with bit mapped attribute                         |
| O-Enum       | Optional enumerations associated with attribute                            |
| PM           | Rotary or Linear Permanent Magnet motor (motor type)                       |
|              | Rotary Absolute Feedback Unit - rev; Feedback n Startup Method- absolute   |
| Rotary Motor | Rotary PM motor or Rotary Induction motor (motor type)                     |
|              | SC Sine/Cosine (feedback type)                                             |
| SL           | Stahl SSI (feedback type)                                                  |
| SS           | SSI (feedback type)                                                        |
| TM           | Tamagawa (feedback type)                                                   |
| TP           | Digital Parallel (feedback type)                                           |
| TT           | Digital AqB (feedback type)                                                |

Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                 | N F P V T Conditional Implementation                                                                                                                                                                          |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 19 Set Axis Features                | R R R R R O-Bits 0 = Fine Interpolation (Y) 1 = Registration Auto-rearm (Y) 2 = Alarm Log (Y) 5 = Hookup Test (Y) 6 = Commutation Test (Y) 7 = Motor Test (Y) 8 = Inertia Test (Y) 9 = Sensorless Control (Y) |
| 30 Set Axis Configuration           | R R R R R O-Enum 0 = Feedback Only (N) 1 = Frequency Control (Y) 2 = Position Loop (Y) 3 = Velocity Loop (Y) 4 = Torque Loop (Y)                                                                              |
| 31 Set Feedback Configuration       | R R R R R O-Enum 0 = No Feedback (V/Y)(T/Y) 3 = Load Feedback (PVT/N) 4 = Dual Feedback (P/Y) 8 = Dual Integrator Feedback (P/Y)                                                                              |
| 45 Set Motion Scaling Configuration | R R R R R O-Enum 1 = Drive Scaling (N)                                                                                                                                                                        |
| 1310/251 Set Motor Catalog Number   | - N N N N Dr NV                                                                                                                                                                                               |

## Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                                                       |        | N F P V T Conditional Implementation                                                                                               |
|---------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 1313 Set Motor Data Source - R R R R O-Enum                               |        | 1 = Database (Y) 2 = Drive NV (Y) 3 = Motor NV (N)                                                                                 |
| 1315 Set Motor Type                                                       |        | - R R R R O-Enum 1 = Rotary Permanent Magnet (Y) 2 = Rotary Induction (Y) 3 = Linear Permanent Magnet (N) 4 = Linear Induction (N) |
| 1317 Set Motor Polarity                                                   | - YYYY |                                                                                                                                    |
| 1320 Set Motor Rated Peak Current                                         |        | - N N N N N-IM                                                                                                                     |
| 1321 Set Motor Rated Output Power                                         |        | - Y Y Y Y Y-IM                                                                                                                     |
| 1322 Set Motor Overload Limit                                             | - YYYY |                                                                                                                                    |
| 1323 Set Motor Integral Thermal Switch                                    | - NNNN |                                                                                                                                    |
| 1324 Set Motor Max Winding Temperature - N N N N                          |        |                                                                                                                                    |
| 1325 Set Motor Winding To Ambient Capacitance - N N N N                   |        |                                                                                                                                    |
| 1326 Set Motor Winding To Ambient Resistance - N N N N                    |        |                                                                                                                                    |
| 2310 Set PM Motor Flux Saturation                                         |        | - N N N N PM Motor only                                                                                                            |
| 1339 Set PM Motor Rated Torque                                            |        | - N N N N Rotary PM Motor only                                                                                                     |
| 1340 Set PM Motor Torque Constant                                         |        | - N N N N Rotary PM Motor only                                                                                                     |
| 1342 Set PM Motor Rated Force                                             |        | - N N N N Rotary PM Motor only                                                                                                     |
| 1343 Set PM Motor Force Constant                                          |        | - N N N N Rotary PM Motor only                                                                                                     |
| 1330 Set Rotary Motor Inertia                                             |        | - N Y Y N Rotary Motor only                                                                                                        |
| 1332 Set Rotary Motor Max Speed                                           |        | - N N N N Rotary Motor only                                                                                                        |
| 1333 Set Rotary Motor Damping Coefficient - N N N N Rotary Motor only     |        |                                                                                                                                    |
| 2311 Set Rotary Motor Fan Cooling Speed                                   |        | - N N N N Rotary Motor only                                                                                                        |
| 2312 Set Rotary Motor Fan Cooling Derating - N N N N Rotary Motor only    |        |                                                                                                                                    |
| 1336 Set Linear Motor Mass                                                |        | - N N N N Linear Motor only                                                                                                        |
| 1337 Set Linear Motor Max Speed                                           |        | - N N N N Linear Motor only                                                                                                        |
| 1338 Set Linear Motor Damping Coefficient - N N N N Linear Motor only     |        |                                                                                                                                    |
| 2313 Set Linear Motor Integral Limit Switch - N N N N Linear Motor only   |        |                                                                                                                                    |
| 1349 Set Induction Motor Magnetization Reactance - N N N N Ind Motor only |        |                                                                                                                                    |
| 1350 Set Induction Motor Rotor Resistance - N N N N Ind Motor only        |        |                                                                                                                                    |
| 1352 Set Induction Motor Rated Slip Speed - Y Y Y N Ind Motor only        |        |                                                                                                                                    |
| 1370 Set Load Type                                                        |        | N N N N N DScale                                                                                                                   |
| 1371 Set Transmission Ratio Input                                         |        | N N N N N DScale                                                                                                                   |
| 1372 Set Transmission Ratio Output                                        |        | N N N N N DScale                                                                                                                   |
| 1373 Set Actuator Type                                                    |        | N N N N N DScale                                                                                                                   |
| 1374 Set Actuator Lead                                                    |        | N N N N N DScale                                                                                                                   |
| 1375 Set Actuator Lead Unit                                               |        | N N N N N DScale                                                                                                                   |
| 1376 Set Actuator Diameter                                                |        | N N N N N DScale                                                                                                                   |

Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                                            |              | N F P V T Conditional Implementation                                                |
|----------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------|
| 1377 Set Actuator Diameter Unit N N N N N DScale               |              |                                                                                     |
| 44 Set Feedback Unit Ratio                                     | - - Y N -    |                                                                                     |
| 1401 Get Feedback 1 Serial Number                              | N - N N N    |                                                                                     |
| 1414 Set Feedback 1 Polarity                                   | Y - Y Y Y    |                                                                                     |
| 1415 Set Feedback 1 Startup Method                             |              | R - R R R O-Enum 1= Absolute (Y)                                                    |
| 1420 Set Feedback 1 Data Length                                |              | Y - Y Y Y TP,SS                                                                     |
| 1421 Set Feedback 1 Data Code                                  |              | Y - Y Y Y TP,SS                                                                     |
| 1422 Set Feedback 1 Resolver Transformer Ratio N - N N N RS    |              |                                                                                     |
| 1423 Set Feedback 1 Resolver Excitation Voltage N - N N N RS   |              |                                                                                     |
| 1424 Set Feedback 1 Resolver Excitation Frequency N - N N N RS |              |                                                                                     |
| 1425 Set Feedback 1 Resolver Cable Balance N - N N N RS        |              |                                                                                     |
| 2400 Set Feedback 1 Loss Action                                |              | N - N N N O-Enum 1 = Switch to Sensorless Fdbk (N) 2 = Switch to Redundant Fdbk (N) |
| 2403 Set Feedback 1 Velocity Filter Taps                       | Y - Y Y Y    |                                                                                     |
| 2404 Set Feedback 1 Accel Filter Taps                          | N - N N N    |                                                                                     |
| 1434 Set Feedback 1 Velocity Filter Bandwidth                  | Y - Y Y Y    |                                                                                     |
| 1435 Set Feedback 1 Accel Filter Bandwidth                     | Y - Y Y Y    |                                                                                     |
| 2405 Set Feedback 1 Battery Absolute                           |              | N - N N N TM                                                                        |
| 1451 Get Feedback 2 Serial Number                              | N - N N N    |                                                                                     |
| 1464 Set Feedback 2 Polarity                                   | Y - Y Y Y    |                                                                                     |
| 1465 Set Feedback 2 Startup Method                             |              | R - R R R O-Enum 1 = Absolute (Y)                                                   |
| 1470 Set Feedback 2 Data Length                                |              | Y - Y Y Y TP,SS                                                                     |
| 1471 Set Feedback 2 Data Code                                  |              | Y - Y Y Y TP,SS                                                                     |
| 1472 Set Feedback 2 Resolver Transformer Ratio N - N N N RS    |              |                                                                                     |
| 1473 Set Feedback 2 Resolver Excitation Voltage N - N N N RS   |              |                                                                                     |
| 1474 Set Feedback 2 Resolver Excitation Frequency N - N N N RS |              |                                                                                     |
| 1475 Set Feedback 2 Resolver Cable Balance N - N N N RS        |              |                                                                                     |
| 2450 Set Feedback 2 Loss Action                                |              | N - N N N O-Enum 1 = Switch to Sensorless Fdbk (N) 2 = Switch to Redundant Fdbk (N) |
| 2453 Set Feedback 2 Velocity Filter Taps                       | N - N N N    |                                                                                     |
| 2454 Set Feedback 2 Accel Filter Taps                          | N - N N N    |                                                                                     |
| 1484 Set Feedback 2 Velocity Filter Bandwidth                  | N - N N N    |                                                                                     |
| 1485 Set Feedback 2 Accel Filter Bandwidth                     | N - N N N    |                                                                                     |
| 2455 Set Feedback 2 Battery Absolute                           | N - N N N TM |                                                                                     |
| 365 Get Position Fine Command                                  | - - Y - -    |                                                                                     |
| 366 Get Velocity Fine Command                                  | - - Y Y -    |                                                                                     |
| 367 Get Acceleration Fine Command                              | - - N N N    |                                                                                     |

## Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                         |           | N F P V T Conditional Implementation                                                                                                                 |
|---------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 370 Set Skip Speed 1 - Y - - -              |           |                                                                                                                                                      |
| 371 Set Skip Speed 2                        | - Y - - - |                                                                                                                                                      |
| 372 Set Skip Speed 3                        | - Y - - - |                                                                                                                                                      |
| 373 Set Skip Speed Band                     | - Y - - - |                                                                                                                                                      |
| 374 Set* Ramp Velocity - Positive           |           | - Y - Y - Derived                                                                                                                                    |
| 375 Set* Ramp Velocity - Negative           |           | - Y - Y - Derived                                                                                                                                    |
| 376 Set* Ramp Acceleration                  |           | - Y - Y - Derived                                                                                                                                    |
| 377 Set* Ramp Deceleration                  |           | - Y - Y - Derived                                                                                                                                    |
| 378 Set Ramp Jerk Control                   | - Y - Y - |                                                                                                                                                      |
| 380 Set Flying Start Enable                 | - Y - Y - |                                                                                                                                                      |
| 445 Set Position Error Tolerance Time       | - - Y - - |                                                                                                                                                      |
| 781 Set Position Lead Lag Filter Bandwidth  | - - Y - - |                                                                                                                                                      |
| 782 Set Position Lead Lag Filter Gain       | - - Y - - |                                                                                                                                                      |
| 783 Set Position Notch Filter Frequency     | - - Y - - |                                                                                                                                                      |
| 446 Set Position Integrator Control         |           | - - R - - O-Bits 1: Auto-Preset (N)                                                                                                                  |
| 447 Set Position Integrator Preload         | - - N - - |                                                                                                                                                      |
| 790 Set Velocity Negative Feedforward Gain  | - - Y Y - |                                                                                                                                                      |
| 464/321 Set Velocity Droop                  | - YYY           |                                                                                                                                                      |
| 465 Set Velocity Error Tolerance            | - - N N - |                                                                                                                                                      |
| 466 Set Velocity Error Tolerance Time       | - - N N - |                                                                                                                                                      |
| 467 Set Velocity Integrator Control         |           | - - R R - O-Bits 1: Auto-Preset (N)                                                                                                                  |
| 468 Set Velocity Integrator Preload         | - - Y Y - |                                                                                                                                                      |
| 469 Set Velocity Low Pass Filter Bandwidth  | - - Y Y - |                                                                                                                                                      |
| 470/327 Set Velocity Threshold              | NYYYN     |                                                                                                                                                      |
| 471 Set Velocity Lock Tolerance             | - YYY           |                                                                                                                                                      |
| 473/325 Set Velocity Limit - Positive       | - YYY           |                                                                                                                                                      |
| 474/326 Set Velocity Limit - Negative       | - YYY           |                                                                                                                                                      |
| 833 Set SLAT Configuration                  | - - - Y - |                                                                                                                                                      |
| 834 Set SLAT Set Point                      | - - - Y - |                                                                                                                                                      |
| 835 Set SLAT Time Delay                     | - - - Y - |                                                                                                                                                      |
| 481 Set Acceleration Trim                   | - - N N N |                                                                                                                                                      |
| 482 Get Acceleration Reference              | - - N N N |                                                                                                                                                      |
| 801 Get Load Observer Acceleration Estimate | - - Y Y N |                                                                                                                                                      |
| 802 Get Load Observer Torque Estimate       | - - Y Y N |                                                                                                                                                      |
| 805 Set Load Observer Configuration         |           | - - Y Y N O-Enum 1= Load Observer Only (Y) 2 = Load Observer with Velocity Estimate (N) 3 = Velocity Estimate Only (N) 4 = Acceleration Feedback (Y) |

Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                                |           | N F P V T Conditional Implementation                                         |
|----------------------------------------------------|-----------|------------------------------------------------------------------------------|
| 806 Set Load Observer Bandwidth - - Y Y N          |           |                                                                              |
| 807 Set Load Observer Integrator Bandwidth         | - - N N N |                                                                              |
| 809 Set Load Observer Feedback Gain                | - - Y Y N |                                                                              |
| 485 Set Acceleration Limit                         | - N N N N |                                                                              |
| 486 Set Deceleration Limit                         | - N N N N |                                                                              |
| 496 Set System Inertia                             | - - R R N |                                                                              |
| 825 Set Backlash Compensation Window               | - - N - - |                                                                              |
| 498 Set Friction Compensation Sliding              | - - N N N |                                                                              |
| 499 Set Friction Compensation Static               | - - N N N |                                                                              |
| 500 Set Friction Compensation Viscous              | - - N N N |                                                                              |
| 826/421 Set Friction Compensation Window           | - - N - - |                                                                              |
| 827 Set Torque Lead Lag Filter Bandwidth - - Y Y N |           |                                                                              |
| 828 Set Torque Lead Lag Filter Gain                | - - Y Y N |                                                                              |
| 502 Set Torque Low Pass Filter Bandwidth           | - - N N N |                                                                              |
| 503 Set Torque Notch Filter Frequency              | - - Y Y Y |                                                                              |
| 506 Set Torque Rate Limit                          | - - N N N |                                                                              |
| 507/334 Set Torque Threshold                       | - - N N N |                                                                              |
| 508 Set Overtorque Limit                           | - Y Y Y Y |                                                                              |
| 509 Set Overtorque Limit Time                      | - Y Y Y Y |                                                                              |
| 510 Set Undertorque Limit                          | - Y Y Y Y |                                                                              |
| 511 Set Undertorque Limit Time                     | - Y Y Y Y |                                                                              |
| 521 Get Operative Current Limit                    | - - N N N |                                                                              |
| 522 Get Current Limit Source                       | - - N N N |                                                                              |
| 524 Get Current Reference                          | - - N N N |                                                                              |
| 525 Get Flux Current Reference                     | - - N N N |                                                                              |
| 840 Set Current Disturbance                        | - - N N N |                                                                              |
| 527 Get Current Error                              | - - N N N |                                                                              |
| 528 Get Flux Current Error                         | - - N N N |                                                                              |
| 529 Get Current Feedback                           | - - Y Y Y |                                                                              |
| 530 Get Flux Current Feedback                      | - - Y Y Y |                                                                              |
| 553 Set Current Vector Limit                       | - Y N N N |                                                                              |
| 555 Set Torque Integral Time Constant              | - - N N N |                                                                              |
| 556 Set Flux Loop Bandwidth                        | - - N N N |                                                                              |
| 557 Set Flux Integral Time Constant                | - - N N N |                                                                              |
| 558 Set Flux Up Control                            |           | - Y Y Y Y Ind Motor only O-Enum 1 = Manual Delay (Y) 2 = Automatic Delay (Y) |
| 559 Set Flux Up Time                               |           | - Y Y Y Y Ind Motor only                                                     |

## Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                                               | N F P V T Conditional Implementation                                                                                                                        |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 562 Set Commutation Self-Sensing Current - - N N N PM Motor only  | O-Value = #                                                                                                                                                 |
| 563 Set Commutation Polarity - - N N N PM Motor only              |                                                                                                                                                             |
| 250 Set Feedback Commutation Aligned - - Y Y Y O-Enum             | 2 = Motor Offset (N) 3 = Self-Sense (Y)                                                                                                                     |
| 570 Set Frequency Control Method - R - - - O-Enum                 | 128 = Fan/Pump Volts/Hertz (Y) 129 = Sensorless Vector (Y) 130 = Sensorless Vector Economy (Y)                                                              |
| 600 Get Output Frequency - R Y Y Y                                |                                                                                                                                                             |
| 610 Set Stopping Action - R R R R O-Enum                          | 2 = Ramped Decel Disable (FPV/Y) 3 = Current Decel Hold (PV/N) 4 = Ramped Decel Hold (PV/Y) 128 = DC Injection Brake (IM/Y) 129 = AC Injection Brake (IM/Y) |
| 612 Set Stopping Time Limit - - N N N                             |                                                                                                                                                             |
| 613/354 Set Resistive Brake Contact Delay - N N N N PM Motor only |                                                                                                                                                             |
| 614 Set Mechanical Brake Control - N N N N                        |                                                                                                                                                             |
| 615 Set Mechanical Brake Release Delay - N N N N                  |                                                                                                                                                             |
| 616 Set Mechanical Brake Engage Delay - N N N N                   |                                                                                                                                                             |
| 870 Set DC Injection Brake Current - Y Y Y Y Ind Motor only       |                                                                                                                                                             |
| 872 Set DC Injection Brake Time - Y Y Y Y Ind Motor only          |                                                                                                                                                             |
| 871 Set Flux Braking Enable - Y Y Y Y Ind Motor only              |                                                                                                                                                             |
| 627 Set Power Loss Action - Y Y Y Y O-Enum                        | 2 = Decel Regen (Y)                                                                                                                                         |
| 628 Set Power Loss Threshold - Y Y Y Y                            |                                                                                                                                                             |
| 629 Set Shutdown Action - N N N N O-Enum                          | 1 = Drop DC Bus (N)                                                                                                                                         |
| 630 Set Power Loss Time - Y Y Y Y                                 |                                                                                                                                                             |
| 637 Get Converter Capacity - N N N N                              |                                                                                                                                                             |
| 638/262 Get Bus Regulator Capacity - N N N N                      |                                                                                                                                                             |
| 646 Set Motor Overload Action - N N N N O-Enum                    | 1 = Current Foldback (N)                                                                                                                                    |
| 647 Set Inverter Overload Action - Y Y Y Y O-Enum                 | 1 = Current Foldback (Y) 128 = Reduce PWM Rate (Y) 129 = PWM Foldback (Y)                                                                                   |
| 659 Get CIP Axis Alarms Y Y Y Y Y                                 |                                                                                                                                                             |
| 904 Get CIP Axis Alarms - RA Y Y Y Y Y                            |                                                                                                                                                             |
| 695 Set Motor Overspeed User Limit - Y Y Y Y                      |                                                                                                                                                             |
| 697 Set Motor Thermal Overload User Limit - Y Y Y Y               |                                                                                                                                                             |
| 699 Set Inverter Thermal Overload User Limit - N N N N            |                                                                                                                                                             |

Table 30 - PowerFlex 755 Safety Drive Module Optional Attributes

| ID Access Attribute                         |           | N F P V T Conditional Implementation                           |
|---------------------------------------------|-----------|----------------------------------------------------------------|
| 706 Set Feedback Noise User Limit N N N N N |           |                                                                |
| 707 Set Feedback Signal Loss User Limit     | N N N N N |                                                                |
| 708 Set Feedback Data Loss User Limit       | N N N N N |                                                                |
| 730 Get Digital Inputs                      | - Y Y Y Y |                                                                |
| 731 Set Digital Outputs                     | - N N N N |                                                                |
| 732/267 Get Analog Input 1                  | - N N N N |                                                                |
| 733/268 Get Analog Input 2                  | - N N N N |                                                                |
| 734 Set Analog Output 1                     | - N N N N |                                                                |
| 735 Set Analog Output 2                     | - N N N N |                                                                |
| 750 Set Local Control                       |           | N N N N N O-Enum 1 = Conditionally Allowed (N) 2 = Allowed (N) |
| 980/242 Get Guard Status                    | - Y Y Y Y |                                                                |
| 981/243 Get Guard Faults                    | - Y Y Y Y |                                                                |

## A

## AC induction motors

recommended 357

Accel/Decel 124

Accel/Decel Time 16

Adjustable Voltage 17

Alarms 155

Analog I/O 105

Analog Input

Square Root 111

Analog Inputs 105

Analog Output 114

Analog Outputs 113

Analog Scaling 107

Auto Restart 25

Auto/Manual 27

Autotune 35

Auxiliary Fault 121

Auxiliary Power Supply y 41

auxiliary power supply option module installation and configuration 347

## axis configuration

control modes 307

## B

Braking 216

bulletin HPK-series motors recommended 359

Bus Memory y 158

Bus Regulation 41

Bus Regulation Mode 125

## C

Carrier Frequency y 196

Clear Fault 121

Coarse Update Rate 301

Coast Stop 121

Compensation 192

Configuration Conflicts 127

configure hardware over travel limits 316

incremental encoder feedback with an MPx motor

372

MDS instruction 302

## Configureation

Analog Output 114

Control Mode axis attributes

no control mode 419

position control mode 419

torque control mode 419

velocity control mode 419

control modes axis configuration 307

Integrated Motion on the EtherNet/IP Network 301

Controller, DriveLogix 10

Conventions, Manual 11

Current Limit 156

Current Limit Stop 121

## D

Data Packets lost 301

DC Bus Voltage 158

Decel Time 16

Detection

Input Loss 112

DHCP persistence

IP address assignment 315

## Dig Out Invert

No. 226 – Main Control Board 147

No. 6 – Option Module 147

Dig Out Setpoint

No. 227 – Main Control Board 142

No. 7 – Option Module 142

## Dig Out Sts

No. 225 – Main Control Board 149

No. 5 – Option Module 150

Digital Inputs 119

Digital Outputs 130

Digital Outputs Parameters 142 , 147 , 149

Drive Nonvolatile Memory 308

Drive NV option 308

Drive Overload 158

DriveLogix™ Controller 10

Drives Technical Support 11

dual loop control

309

309

application configuration

Dual-Port EtherNet/IP option module 315

install and configure 347

IP address assignment 315

port assignment 315

## dynamic brake

configure for Integrated Motion on the EtherNet/IP Network 347

Dynamic Braking 197

dynamic IP address assignment by port 315

## E

Enable 121

ETAP. See Dual-Port EtherNet/IP option module

## F

Faults 162

Feedback Devices 54

feedback option modules install and configure 346

Flux Braking 216

Flux Regulator 218

Flux Up 218

Flux Up Enable (No. 43) 220

Flux Up Time (No. 44) 220

Flying Start 54

Forward/Reverse 122

Decel Limit 126

## Forward/Revese

End Limit 126

## frequency control

RSLogix 5000 instance to parameter cross reference 319

## G

## General Precautions 12

## H

Hand-Off-Auto Start 124

## hardware over travel limits

configure for Integrated Motion on the EtherNet/IP Network 316

Human Interface Module Removal 52

## I

## incremental encoder feedback with an MPx motor

configure 372

## induction motor data

RSLogix 5000 instance to parameter cross reference 327

## induction motor model

RSLogix 5000 instance to parameter cross reference 327

Input Loss Detection 112

Input Phase Loss Detection 166

## Inputs

Analog 105

Digital 119

## Integrated Architecture Builder software 300

## Integrated Motion on the EtherNet/IP Network

control logic block diagram 413

control modes

301

diagnostic tools block diagram 417

flux vector overview block diagram 377

friction compensation block diagram 415

high speed trending wizard block diagram

418

inputs and outputs, analog block diagram 409

inputs and outputs, digital block diagram 408

inverter overload IT block diagram 414

MOP control block diagram 407

option modules supported 346

position control, aux functions block diagram 389

position control, homing block diagram 393

position control, phase locked loop block diagram 3 390

position control, position CAM block diagram 391

position control, profiler/indexer (sheet 1) block diagram 392

position control, profiler/indexer (sheet 2) block diagram 393

position control, regulator block diagram 388

position control/aux functions, position oriented torque boost block diagram 396

position control/aux functions, roll position indicator block diagram 394

process control (sheet 1) block diagram 405

process control (sheet 2) block diagram 406

safety option module restrictions 346

speed control reference (sheet 1) block diagram 381

speed control reference (sheet 2) block diagram 382

speed control reference (sheet 3) block diagram 383

speed control reference (sheet 4) block diagram 384

speed control reference (sheet 5) block diagram 385

speed control, reference block diagram 387

speed control, reference overview block diagram 380

speed control, regulator (flux vector) block diagram 386

speed/position feedback block diagram 379

system tuning

363

torque control overview, induction motor and surface permanent magnet motor block diagram 397

torque control overview, interior permanent magnet motor block diagram 398

torque control, current, induction motor and surface permanent magnet motor block diagram 401

torque control, current, interior permanent magnet motor block diagram 402

torque control, inertia adaption block diagram torque control, load observer/estimator block diagram 404

torque control, reference scale and trim block diagram 399

torque control, torque block diagram 400 variable boost voltage overview, function inputs/ outputs block diagram 416

VF (V/Hz), SV overview block diagram 378

## IP address assignment

Dual-Port EtherNet/IP option module 315

403

## J

Jog 123

Jog Forward Jog Reverse

122

## L

## Last StrtInhibit (No. 934) 95

## Linear Topology

Integrated Motion on the EtherNet/IP Network 342

## Linear/Star Topology

Integrated Motion on the EtherNet/IP Network 344 Load

RSLogix 5000 instance to parameter cross reference 334

## Load Compliance

RSLogix 5000 instance to parameter cross reference 335

## Load Observer

RSLogix 5000 instance to parameter cross reference

337

Lost Data Packets 301

## M

Manaual Control 123

Manual Conventions 11

MAS instruction 304

## MDS instruction

configure 301

decrease speed sample code 303

increase speed sample code 303

ramp attributes 304

ramp attributes sample code 305

start sample code 302

torque mode sample code 304

Minimum Coarse Update Rate 301

MOP Increment/Decrement 124

Motion Analyzer software 300

Motion Axis Stop. See MAS instruction

Motion Drive Start. See MDS instruction

Motion Servo Off. See MSF instruction

## Motor Feedback

RSLogix 5000 instance to parameter cross reference 331

## Motor Load Feedback

RSLogix 5000 instance to parameter cross reference 332

Motor Overload 168

Motor Thermistor 152

Motor Types 235

MSF instruction 304

Mtr Options Cfg (No. 40) 25

## N

## Network Topologies

Integrated Motion on the EtherNet/IP Network 341

Nonvolatile Memory y 308

Notch Filter

244

## O

## Option Modules

supported for Integrated Motion on the EtherNet/IP

Network 346

## Outputs

Analog 113 , 114 Digital 130

Overload 158 , 168

Overspeed Limit 172

Owners 70

## P

## Password 173

## Permanent Magnet Motor

evaluation 361

specifications 361

## Permanent Magnet Motor Data 308

RSLogix 5000 instance to parameter cross reference 329

## Permanent Magnet Motor Model

RSLogix 5000 instance to parameter cross reference 329

## Permanent Magnet Motors

recommended 358

PID Cfg (No. 1065) 79

PID Enable 125

PID Hold 126

PID Invert 126

PID Loop 76

PID Reset 126

PID Status (No. 1089) 85

## Port Assignment

Dual-Port EtherNet/IP option module 315

## position loop

RSLogix 5000 instance to parameter cross reference 325

Position Mode

306

Positive/Negative Hardware Over-travel 127

Power Loss

72

,

125

Power Loss Mode 125

Power Tab

RSLogix 5000 instance to parameter cross reference 337

Precautions, General 12

Precharge 125

Process PID Loop 76

Process PID Parameters 79

PTC Motor Thermistor Input 152

PWM Frequency 196

## R

Real Time Clock k 174

Recommended

AC induction motors 357

bulletin HPK-series motors 359

permanent magnet motors 358

Reflected Wave 179

Regen Power Limit 247

Restart, Auto 25

Ring topology

Integrated Motion on the EtherNet/IP Network 343

Ring/star topology

Integrated Motion on the EtherNet/IP Network 345

Run 122

Run Forward/Run Reverse 122

## S

## safety option modules

restrictions for Integrated Motion on the EtherNet/IP Network 346

Scaling, Analog 107

Security 185

Shear Pin 188

shunt regulator configuration for Integrated Motion on the EtherNet/

IP Network 347

## Signal Loss 112

SLAT. See Speed Limited Adjustable Torque

Slip Compensation 192

Slip Regulator 194

Software

Integrated Architecture Builder

Motion Analyzer 300

## Speed Limited Adjustable Torque

configure for Integrated Motion on the EtherNet/IP Network 353

Speed Reference 251

Speed Regulation 260

300

Speed Select 123

Speed Torque Position 266

Speed Torque Position Mode 124

Square Root

Analog Input 111

Star Topology

Integrated Motion on the EtherNet/IP Network 341

Start 122

Start Inhibits (No. 933) 95

Status 127

Stop 121

Stop Mode 124

Support, Product 11

## System Tuning

Integrated Motion on the EtherNet/IP Network 363

## T

## Technical Support 11

Thermistor 152

## Third-party permanent magnet motors

data modifications 361

## Torque

Mode 306

Position 266

Reference 262

## Torque Loop

RSLogix 5000 instance to parameter cross reference 323

torque overload capability 345

Torque Reference 262

Torque Setpoint 126

## V

## Velocity Control

RSLogix 5000 instance to parameter cross reference

321

Velocity Mode

306

## Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products. At http://www.rockwellautomation.com/support you can find technical and application notes, sample code, and links to software service packs. You can also visit our Support Center at https://rockwellautomation.custhelp.com/ for software updates, support chats and forums, technical information, FAQs, and to sign up for product notification updates.

In addition, we offer multiple support programs for installation, configuration, and troubleshooting. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation.com/services/online-phone .

## Installation Assistance

If you experience a problem within the first 24 hours of installation, review the information that is contained in this manual. You can contact Customer Support for initial help in getting your product up and running.

| United States or Canada 1.440.646.3434                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States or Canada Use the Worldwide Locator at http://www.rockwellautomation.com/rockwellautomation/support/overview.page, or contact your local Rockwell Automation representative. |

## New Product Satisfaction Return

Rockwell Automation tests all of its products to help ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

| United States Contact your distributor. You must provide a Customer Support case number (call the phone number above to obtain one) to your distributor to complete the return process.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States Please contact your local Rockwell Automation representative for the return procedure.                                                                              |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/ .

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page .

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400