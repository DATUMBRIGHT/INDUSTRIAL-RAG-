<!-- image -->

## Elevator Panel Solution

Bulletin 150-E

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

|                         | About This Publication . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . 5                      |
|-------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------|
|                         | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . . . . . . . 5                      |
|                         | Additional Resources . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . . 5            |
|                         | European Communities (EC) Directive Compliance . . . . . . . . . . . . . . . . . 6                   |                                      |
|                         | EMC Directive . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . 6            |
|                         | Low Voltage Directive . . . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 6    |
|                         | UL/CSA Elevator Ratings . . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 6      |
|                         | Chapter 1                                                                                            |                                      |
| Introduction            | Component Overview . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 7    |
|                         | Base Controller . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . 8          |
|                         | Fault Contactor. . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . 8          |
|                         | Function Overview . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . . . . . . . . 8                    |
|                         | Starter Selection . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . . . . . . 9          |
|                         | For 6- or 12-Lead Wye-Delta Wound Motors .  . . . . . . . . . . .                                    | . . . . . . . . . 9                  |
|                         | For 3- or 9-Lead Closed Delta-Type Motors . . . . . . . . . . . . . . . . . . . . . . 9              |                                      |
|                         | Chapter 2                                                                                            |                                      |
| Installation and Wiring | Unpacking . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 10                   |
|                         | Mounting . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . . . . . . 10           |
|                         | Dimensions . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . . . . . . . 10         |
|                         | Installation Precautions . . . . . .  . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 12   |
|                         | Motor Branch Protection and Disconnecting Means . . . . . . . . . . . . 12                           |                                      |
|                         | Electrical Noise Suppression. .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 12     |
|                         | Power Factor Correction Capacitors (PFCCs) . . . . . . . . . . . . . . . . . . . 12                  |                                      |
|                         | Terminal Torque Specifications .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 12     |
|                         | Connection Diagrams . . . . . . . .  . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 14   |
|                         | Typical Control Wiring . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . 18           |
|                         | Chapter 3                                                                                            |                                      |
| Programming             | DIP Switch Settings . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . . . . . . . . . . . 20           |
|                         | Motor FLA Requirements . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . 21     |
|                         | Motor Overload Trip Curves . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 22     |
|                         | Input and Output Timing .  . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . . 22 |
|                         | Chapter 4                                                                                            |                                      |
| Troubleshooting         | Introduction. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 23                   |
|                         | Diagnostics Indication . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 23 |
|                         | Troubleshooting Steps. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . 24           |
|                         | Renewal Parts . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . . . . . . . 25         |

|                    | Chapter 5                                                                                                                     |                    |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Specifications     | Electrical . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 26 |                    |
|                    | Mechanical . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 27     |                    |
|                    | Environmental . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . 28 |
|                    | Approximate Dimensions and Shipping Weights . . . . . . . . . . . . . . . . . . 28                                            |                    |
| History of Changes | Appendix A Approximate Dimensions and Shipping Weights . . . . . . . . . . . . . . . . . . 29                                 |                    |

## About This Publication

## Summary of Changes

## Additional Resources

This publication provides detailed instructions that you need to select, install, program, and troubleshoot Bulletin 150-E Elevator Controller Panels.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes. This document has also been reformatted.

|                                                                                                                                                  | Topic Page   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Added Additional Resources section                                                                                                               | 5            |
| Added European Communities (EC) Directive Compliance                                                                                             | 6            |
| Update for series change; fault contactors for Series C updated to Bulletin 100-E contactor options, replacing Bulletins 100-C and 100-D devices | 8,25         |

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                           | Description                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SMC-3, SMC Flex, and SMC-50 Smart Motor Controllers Technical Data, publication 150-TD009                          | Provides specifications and application profiles for the SMC™ Smart Motor Controller product line.                                                                                                                                                                              |
| IEC Contactor Specifications, publication 100-TD013                                                                | Provides specifications for IEC contactors.                                                                                                                                                                                                                                     |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications .                                                          | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

You can view or download publications at rok.auto/literature .

## European Communities (EC) Directive Compliance

If this product has the CE mark, then it is approved for installation within the European Union. It has been designed and tested to meet the following directives.

## EMC Directive

This product is tested to meet the Council Directive 2014/30/EU Electromagnetic Compatibility (EMC) by applying the following standards, in whole or in part, documented in a technical construction file:

EN 60947-4-2 — Product Standard

This product is intended for use in an industrial environment.

## Low Voltage Directive

This product is tested to meet Council Directive 2014/35/EU Low Voltage. This equipment is classified as open equipment and must be mounted in an enclosure during operation to provide safety protection.

## UL/CSA Elevator Ratings

Bulletin 150-C Soft Starters are cULus Listed (Canadian Standards per UL 508 and CSA C22.2 No. 14) as solid-state motor controllers in File E96956. They are also cULus Listed (CAN/CSA B44.1-96) as elevator controllers in UL File E96956.

## Component Overview

## Introduction

This manual provides and overview of the installation, set-up, and typical operation of the Allen-Bradley® hydraulic elevator and escalator starter. This solid- state starter solution is designed to operate 3-phase standard squirrel cage induction motors and can be connected to a 6- or 12-lead Wye-Delta or standard 3- or 9-lead motors. Through the use of line or inside-the-delta control, the solid-state solution can provide ultimate control of the motor. The advantages of a solid-state solution include the following:

- Provides smooth motor starting.
- Reduces current surges on weak electrical systems.
- Reduces starting torque of the motor, which helps to reduce mechanical stress on system components.
- Helps meet both local and regional electrical codes when reduced voltage starting is a requirement.
- Eliminates voltage and current spikes associated with traditional WyeDelta starters.
- Maximizes the life of the motor with reduced electrical strain.
- Reduces general system maintenance requirements for improved uptime.

The starter is made up of two components, the base controller and a fault contactor.

<!-- image -->

Figure 1 - Bulletin 150-E Components

<!-- image -->

## Function Overview

## Base Controller

The base controller is a standard product that uses intelligent features to provide advanced motor control and simple diagnostics. The base controller consists of the elements necessary to control the motor. These elements include:

- a main micro-processor
- current sensing
- built-in adjustable overload
- solid-state power modules, and
- electro-mechanical bypass contacts.

Through the use of simple DIP switch configuration, you can configure the controller for a variety of modes. The default configuration uses the built-in current sensing to limit current to the motor during startup. Once up to speed, the base controller transitions to the run mode by transitioning to internal bypass contactors and changing the state of the auxiliary contact. The internal bypass contactor provides decreased heating during run and removes the SCRs from the circuit.

## Fault Contactor

The fault contactor is controlled through the fault contact of the controller. When control power is applied to the controller, the normally open fault contact closes and applies control power to the coil of the contactor. The fault contact opens, removing power from the fault contactor, and thus disabling the motor during any one of the following events:

- The power is removed from the controller.
- The motor has developed a problem including overloading due to one of the following:
- Mechanical or electrical reasons
- Ground faults or
- Motor short circuits.
- The starter has detected an internal problem such as a shorted SCR or overtemperature condition.

<!-- image -->

150-E Series B devices use Bulletin 100-C or 100-D contactors. Series C devices use Bulletin 100-E contactors. See Table 20 for more information.

The Bulletin 150-E elevator panel provides solution to both advanced motor control and simple diagnostics. Table 1 and Table 2 provide a brief overview of the basic product features.

Table 1 - Motor Control Features

| Function      | Description                                                                                                                                                                                                                                                                                                                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Current Limit | Using internal current sensors, the SMC™ controller regulates the current level that is applied to the motor over the programmed period of time. This type of motor control produces a slow start and ensures that the current does not exceed the programmed level. This is the standard configuration of the device and aligns well with traditional applications. |
| Soft Start    | The voltage is ramped from an initial set point to full voltage over the programmed period of time. This type of motor control produces a smooth start in less time than the current limit setting. However, it does not restrict the current.                                                                                                                       |
| Soft Stop     | The voltage is ramped down from full voltage and applied to the motor over a programmed period of time. The result is a smooth stop.                                                                                                                                                                                                                                 |

## Starter Selection

Table 2 - Diagnostic Features

| Function              | Description                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overload              | Provides protection of the motor for over current conditions. This feature offers a user selectable setting called the trip class, which can be used to accommodate different applications and motor types. When the motor draws more than the nominal value of current for a period of time, the device faults on a motor overload fault.                                                                                                                                                                                                                              |
| Overtemperature       | A built-in self-monitoring method for detecting a SCR overtemperature condition. If the internal temperature exceeds a design threshold, the device faults on a SCR Overtemp fault.                                          |
| Phase Reversal        | You can select the phase relationship of the incoming power. If this phase relationship changes, the device faults, indicating a problem.                                                                                    |
| Phase Loss/ Open Load | When any one of the incoming 3 phases are lost, the controller faults, indicating a phase loss condition has occurred.                                                                                                       |
| Phase Imbalance       | When enabled, detects whether a phase imbalance condition exists and fault the unit. A phase imbalance is defined as a 65% differential between the highest and lowest phase for more than 3 seconds.                        |
| Shorted SCR           | Each time the SMC controller initiates a start, it checks to see if the SCRs are operating correctly. If the controller is unable to properly turn on and off any one of the SCRs, the device faults on a Shorted SCR fault. |

## For 6- or 12-Lead Wye-Delta Wound Motors

The following table lists the catalog numbers that can be used with 6 or 12 lead Wye-Delta motors. For proper operation, the connection should be verified during installation. Chapter 2 includes sample connection diagrams for inside-the-delta connected motors.

Table 3 - Cat. Nos. For Use with 6- or 12-Lead Wye-Delta Motors

| Hp at Nominal Ratings   | Overload Range (1)    | Control Voltage Cat. Nos.   | Control Voltage Cat. Nos.   |
|-------------------------|-----------------------|-----------------------------|-----------------------------|
| 200V 240V 480V 575V     | Overload Range (1)    | 120V                        | 230V                        |
|                         | 10 10 20 30 10.9…32.9 | 150-E32NCE-FC               | 150-E32NCA-FC               |
| 15 15 30 40             | 17…51                 | 150-E51NCE-FC               | 150-E51NCA-FC               |
|                         | 20 20 40 60 21.3…64   | 150-E64NCE-FC               | 150-E64NCA-FC               |
|                         | 20 25 50 60 24.7…74   | 150-E74NCE-FC               | 150-E74NCA-FC               |
|                         | 30 40 75 100 34.7…104 | 150-E104NCE-FC              | 150-E104NCA-FC              |
|                         | 40 50 100 150 49…147  | 150-E147NCE-FC              | 150-E147NCA-FC              |
|                         | 75 75 150 200 59…234  | 150-E234NCE-FC              | 150-E234NCA-FC              |

## For 3- or 9-Lead Closed Delta-Type Motors

The following table lists the catalog numbers that can be used with 3- or 9-lead closed delta type motors. For proper operation, the connection should be verified during installation. Chapter 2 includes sample connection diagrams for line-connected motors.

Table 4 - Cat. Nos. For Use with 6 or 12 Lead Closed Delta-Type Motors

| Hp at Nominal Ratings   | Hp at Nominal Ratings   | Overload Range (1)   | Control Voltage Cat. Nos.   | Control Voltage Cat. Nos.   |
|-------------------------|-------------------------|----------------------|-----------------------------|-----------------------------|
|                         | 200V 240V 480V 575V     | Overload Range (1)   | 120V                        | 230V                        |
|                         | 5 5 10 15               | 6.3…19               | 150-E32NCE-FC               | 150-E32NCA-FC               |
|                         |                         | 7.5 10 20 25 10…30   | 150-E51NCE-FC               | 150-E51NCA-FC               |
|                         |                         | 10 10 25 30 12.3…37  | 150-E64NCE-FC               | 150-E64NCA-FC               |
|                         |                         | 10 15 30 40 14.3…43  | 150-E74NCE-FC               | 150-E74NCA-FC               |
|                         |                         | 15 20 40 50 20…60    | 150-E104NCE-FC              | 150-E104NCA-FC              |
|                         |                         | 25 30 60 75 28.3…85  | 150-E147NCE-FC              | 150-E147NCA-FC              |
|                         |                         | 40 50 100 125 34…135 | 150-E234NCE-FC              | 150-E234NCA-FC              |

## Unpacking

## Mounting

## Dimensions

## Installation and Wiring

Before installation, unpack the starter panel from its packaging and perform a complete visual inspection of the panel. Inspect all components for damage related to shipping and handling, including the controller, wiring, and fault contactor. Claims for damage must be made to the carrier as soon as possible after receipt of the shipment.

The small footprint of the starter panel makes it ideal for mounting in the same space previously occupied by legacy solid-state starters and traditional full-voltage starters. The starter panel does not have mounting requirements beyond the basic footprint of the panel.

The product can incorporate a small cooling fan. There are no additional cooling requirements for the product. However, it is good practice to leave at least 6 inches (15.24 cm) of free space above and below the unit for ideal air flow.

<!-- image -->

|    | Note Information                                                                                                                                                                                                                                                                                                                                                                          |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | This screw is intended to secure a prepared bonding conductor (example: a bonding conductor with a crimped-on lug) or a suitable terminal for connection of an unprepared bonding conductor (example: a bonding conductor with a stripped wire end). This screw is not intended for a direct field wiring connection of an unprepared bonding conductor or equipment grounding conductor. |

Figure 2 - Panel Dimensions for 32, 51, and 64 A Elevator Panels

<!-- image -->

Figure 3 - Panel Dimensions for 74, 104, and 147 A Elevator Panels

<!-- image -->

## Note Information

1

This screw is intended to secure a prepared bonding conductor (example: a bonding conductor with a crimped-on lug) or a suitable terminal for connection of an unprepared bonding conductor (example: a bonding conductor with a stripped wire end). This screw is not intended for a direct field wiring connection of an unprepared bonding conductor or equipment grounding conductor.

<!-- image -->

Figure 4 - Panel Dimensions for 234 A Elevator Panels

|    | Note Information                                                                                                                                                                                                                                                                                                                                                                          |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | This screw is intended to secure a prepared bonding conductor (example: a bonding conductor with a crimped-on lug) or a suitable terminal for connection of an unprepared bonding conductor (example: a bonding conductor with a stripped wire end). This screw is not intended for a direct field wiring connection of an unprepared bonding conductor or equipment grounding conductor. |

## Installation Precautions

## Terminal Torque Specifications

The following precautions are provided as guidance for proper installation of this controller. Because this product was designed to be used in a variety of applications, not all precautions mentioned are relevant to your particular application. In all cases, the local codes and standards governing this type of product must be observed.

## Motor Branch Protection and Disconnecting Means

- The controller features motor overload protection. However, it does not have means to protect itself from a short circuit condition. Suitable branch circuit protection and coordination must be provided per the NEC, or the equivalent local electrical code.

## Electrical Noise Suppression

- Electrical noise can be generated from various sources connected to the same power as the controller. Sources of noise include: inductive loads (example: relays and solenoids), large motors, and machinery, variablefrequency drives, and other high-frequency devices (example: welders).
- Electrical noise can enter the product through power and control wiring and cause damage to solid-state components.
- You can mitigate electrical noise using the following methods:
- Proper wiring practices, including grounding, use of shielded cable where appropriate, and separation of power, control, and signaling wires.
- Use surge suppression devices on inductive loads.
- Use isolation transformers for high-frequency generators.

## Power Factor Correction Capacitors (PFCCs)

- PFCCs must always be used on the line side of the controller. Use of PFCCs on the output side of the controller damages the starter.

Table 5 - Torque Specifications

| Controller Size [A]             | Attribute   | Power Terminals             | Power Terminals             | Power Terminals         |
|---------------------------------|-------------|-----------------------------|-----------------------------|-------------------------|
| Controller Size [A]             | Attribute   | Line                        | Load                        | Control                 |
| 32/51/64 Cat. No. 150-E40KD00   | Wire size   | 14…4 AWG 2.5…25 mm 2        | 14…6 AWG 2.5…16 mm 2        | 24…14 AWG 0.2…2.5 mm 2  |
| 32/51/64 Cat. No. 150-E40KD00   | Torque      | 20…25 lb•in 2.3…2.8 N•m     | 20…22.5 lb•in 2.3…2.6 N•m   | 4.4…8 lb•in 0.5…0.9 N•m |
| 74/104/147 Cat. No. 150-E65KD00 | Wire size   | 14…3/0 AWG 2.5…95 mm 2      | 14…1 AWG 2.5…50 mm 2        | 24…14 AWG 0.2…2.5 mm 2  |
| 74/104/147 Cat. No. 150-E65KD00 | Torque      | 100…110 lb•in 11.3…12.4 N•m | 100…110 lb•in 11.3…12.4 N•m | 4.4…8 lb•in 0.5…0.9 N•m |
| 234 Cat. No. 150-E190KD00       | Wire size   | 6…250 MCM 16…120 mm 2       | 6…250 MCM 16…120 mm 2       | 24…14 AWG 0.2…2.5 mm 2  |
| 234 Cat. No. 150-E190KD00       | Torque      | 275 lb•in 31 N•m            | 275 lb•in 31 N•m            | 4.4…8 lb•in 0.5…0.9 N•m |

Table 6 - Fault Contactor Torque

| Controller Size [A]           | Attribute   | Power Terminals       | Power Terminals       | Power Terminals          |
|-------------------------------|-------------|-----------------------|-----------------------|--------------------------|
| Controller Size [A]           | Attribute   | Line                  | Load                  | Control                  |
| 32/51/64 Cat. No. 150-E40KD00 | Wire size   | 10…2 AWG 6…35 mm 2    | 10…2 AWG 6…35 mm 2    | 18…14 AWG 1…2.5 mm 2     |
| 32/51/64 Cat. No. 150-E40KD00 | Torque      | 35 lb•in 4 N•m        | 35 lb•in 4 N•m        | 11 lb•in 1.2 N•m         |
| 74/104 Cat. No. 150-E65KD00   | Wire size   | 10…2 AWG 6…35 mm 2    | 10…2 AWG 6…35 mm 2    | 18…14 AWG 1…2.5 mm 2     |
| 74/104 Cat. No. 150-E65KD00   | Torque      | 35 lb•in 4 N•m        | 35 lb•in 4 N•m        | 11 lb•in 1.2 N•m         |
| 147 Cat. No. 150-E80KD00      | Wire size   | 6…1 AWG 6…70 mm 2     | 6…1 AWG 6…70 mm 2     | 18…14 AWG 1…2.5 mm 2     |
| 147 Cat. No. 150-E80KD00      | Torque      | 53 lb•in 6 N•m        | 53 lb•in 6 N•m        | 11 lb•in 1.2 N•m         |
| 234 Cat. No. 150-E190KD00     | Wire size   | 6…300 MCM 10…150 mm 2 | 6…300 MCM 10…150 mm 2 | 18…14 AWG 1…4 mm 2       |
| 234 Cat. No. 150-E190KD00     | Torque      | 300 lb•in 34 N•m      | 300 lb•in 34 N•m      | 8.9…10.6 lb•in 1…1.2 N•m |

## Connection Diagrams

| 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   | 6 LEAD MOTOR CONNECTIONS   |
|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| STARTER TERMINALS          | T1 T2 T3 T6 T4 T5 JUMPER   |                            |                            |                            |                            |                            |                            |
| MOTOR TERMINALS            | 1 2 3 6 4 5 N/A            |                            |                            |                            |                            |                            |                            |

Figure 5 - Diagram and Power Connections; Motor Wiring—6-lead Delta-connected Motors

<!-- image -->

Figure 6 - Motor Wiring—12-lead Delta-connected Motors

<!-- image -->

| 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   |
|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| STARTER TERMINALS                            |                                              | T1 T2 T3 T6 T4 T5 JUMPER                     |                                              |                                              |                                              |                                              |                                              |
| MOTOR TERMINALS                              | 1&7 2&8 3&9 6&12 4&10 5&11 N/A               |                                              |                                              |                                              |                                              |                                              |                                              |

| 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 12 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| STARTER TERMINALS                             | T1 T2 T3 T6 T4 T5 JUMPER                      |                                               |                                               |                                               |                                               |                                               |                                               |
| MOTOR TERMINALS                               | 1 2 3 12 10 11 4&7 5&8 6&9                    |                                               |                                               |                                               |                                               |                                               |                                               |

<!-- image -->

| 3 LEAD MOTOR CONNECTIONS   | 3 LEAD MOTOR CONNECTIONS   | 3 LEAD MOTOR CONNECTIONS   | 3 LEAD MOTOR CONNECTIONS   | 3 LEAD MOTOR CONNECTIONS   |
|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| STARTER TERMINALS          | T6 T4 T5 JUMPER            |                            |                            |                            |
| MOTOR TERMINALS            | 1 2 3 N/A                  |                            |                            |                            |

Figure 7 - Diagram and Power Connections; Motor Wiring—3-lead Line-connected Motors

<!-- image -->

<!-- image -->

Figure 8 - Motor Wiring—9-lead Line-connected Motors

| 9 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 230V LOW VOLTAGE MOTOR CONNECTIONS   |
|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| STARTER TERMINALS                           |                                             | T6 T4 T5 JUMPER                             |                                             |                                             |
| MOTOR TERMINALS                             | 1, 6, 7 2, 4, 8 3, 5, 9 N/A                 |                                             |                                             |                                             |

<!-- image -->

| 9 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   | 9 LEAD 460V HIGH VOLTAGE MOTOR CONNECTIONS   |
|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| STARTER TERMINALS                            | T6 T4 T5 JUMPER                              |                                              |                                              |                                              |
| MOTOR TERMINALS                              | 1 2 3 4&7 5&8 6&9                            |                                              |                                              |                                              |

## Typical Control Wiring

Figure 9 - Control Wiring for Delta-connected Controllers

<!-- image -->

Figure 10 - Control Wiring for Line-connected Motors

<!-- image -->

Note Information

1 Customer supplied

## DIP Switch Settings

## Programming

Program the 150-E elevator controller with the DIP switches that are located on the front of the controller. The DIP switch settings define all functionality. The following tables define the settings available within the SMC™ controller. The default settings are shaded.

## Table 7 - Start Time

| Setting [seconds] Switch #1 Switch #2 Description   |          |                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2                                                   | OFF      | OFF This defines the time for which the controller ramps or limits current to the motor. The controller can determine when the motor is up-to-speed (UTS), it may transition to bypass before this time expires. If the motor does not reach speed before the time expires, the controller continues under SCR control and does not close the bypass contactor. |
|                                                     | 5 ON OFF | OFF This defines the time for which the controller ramps or limits current to the motor. The controller can determine when the motor is up-to-speed (UTS), it may transition to bypass before this time expires. If the motor does not reach speed before the time expires, the controller continues under SCR control and does not close the bypass contactor. |
| 10                                                  | OFF ON   | OFF This defines the time for which the controller ramps or limits current to the motor. The controller can determine when the motor is up-to-speed (UTS), it may transition to bypass before this time expires. If the motor does not reach speed before the time expires, the controller continues under SCR control and does not close the bypass contactor. |
| 15                                                  | ON ON    | OFF This defines the time for which the controller ramps or limits current to the motor. The controller can determine when the motor is up-to-speed (UTS), it may transition to bypass before this time expires. If the motor does not reach speed before the time expires, the controller continues under SCR control and does not close the bypass contactor. |

## Table 8 - Start Mode

| Mode Setting Switch #3 Description   |    |
|--------------------------------------|----|
| Current Limit                        | OFF In Current Limit mode, a set level of current is applied to the motor over the start time. In Soft Start mode, the device ramps the torque from the initial ,  level to 100% over the start time. Soft Start ON    |
|                                      | OFF In Current Limit mode, a set level of current is applied to the motor over the start time. In Soft Start mode, the device ramps the torque from the initial ,  level to 100% over the start time. Soft Start ON    |

## Table 9 - Current Limit/Initial Torque Level

| % FLA/ % Torque Switch #4 Switch #5 Description   |    |                                                                                                                                                                                                                                                     |
|---------------------------------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 150%/15% OFF OFF                                  |    | The level indicated by this programming applies an initial level of current or torque to the motor for the start time. For example, if switch #3 is set to OFF, the device performs a current limit start at the level indicated by these switches. |
| 250%/25% ON OFF                                   |    | The level indicated by this programming applies an initial level of current or torque to the motor for the start time. For example, if switch #3 is set to OFF, the device performs a current limit start at the level indicated by these switches. |
| 350%/35%  OFF                                     | ON | The level indicated by this programming applies an initial level of current or torque to the motor for the start time. For example, if switch #3 is set to OFF, the device performs a current limit start at the level indicated by these switches. |
| 450%/65% ON ON                                    |    | The level indicated by this programming applies an initial level of current or torque to the motor for the start time. For example, if switch #3 is set to OFF, the device performs a current limit start at the level indicated by these switches. |

## Table 10 - Soft Stop Time

| Settings [seconds] Switch #6 Switch #7 Description   |                                                                                                                                                                                                                           |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OFF  OFF  OFF                                        | Soft Stop reduces the voltage that is applied to the motor over the programmed period of time. The soft stop is complete when the soft stop timer has expired or the current measured drops below 50% of the FLA setting. |
| 1 x start time ON OFF                                | Soft Stop reduces the voltage that is applied to the motor over the programmed period of time. The soft stop is complete when the soft stop timer has expired or the current measured drops below 50% of the FLA setting. |
| 2 x start time OFF ON                                | Soft Stop reduces the voltage that is applied to the motor over the programmed period of time. The soft stop is complete when the soft stop timer has expired or the current measured drops below 50% of the FLA setting. |
| 3 x start time ON ON                                 | Soft Stop reduces the voltage that is applied to the motor over the programmed period of time. The soft stop is complete when the soft stop timer has expired or the current measured drops below 50% of the FLA setting. |

## Table 11 - Phase Rotation

|                 | Setting Switch #9 Description                                      |
|-----------------|--------------------------------------------------------------------|
| ABC rotation    | OFF This switch defines the allowable phase rotation of the motor. |
| CBA rotation ON | OFF This switch defines the allowable phase rotation of the motor. |

## Table 12 - Phase Imbalance

|             | Setting Switch #10 Description                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------------|
| Enabled     | OFF  The controller can monitor for imbalance between phase currents. You can disable this protection feature. |
| Disabled ON | OFF  The controller can monitor for imbalance between phase currents. You can disable this protection feature. |

<!-- image -->

## Motor FLA Requirements

## Table 13 - Overload Trip Class

|             | Setting Switch #11 Switch #12 Description                                                                                                                                                                   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OFF OFF OFF | The controller incorporates, as standard, electronic overload protection. This motor overload protection is accomplished electronically by using internal current transformers on each of the three phases. |
| 10  ON      | OFF                                                                                                                                                                                                         |
| 15 OFF ON   | The controller incorporates, as standard, electronic overload protection. This motor overload protection is accomplished electronically by using internal current transformers on each of the three phases. |
| 20 ON ON    | The controller incorporates, as standard, electronic overload protection. This motor overload protection is accomplished electronically by using internal current transformers on each of the three phases. |

## Table 14 - Overload Reset

| Setting Switch #13 Description                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Manual OFF In manual reset mode, the fault can only be reset by pushing the ‘Push to Reset’ button on the front of the controller. In auto reset mode, the unit automatically resets when the unit determines the motor has cooled to 75% of its thermal capacity.  Auto  ON |

## Table 15 - Aux #1 Setting

| Setting Switch #14 Description                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Normal OFF The operation defines the operation of the auxiliary contacts. Normal mode means that the contact changes state immediately when a start/run command is given. |
| Up-to-Speed mode means that the contact changes state only when the controller is in bypass. Aux#2, when added, operates opposite of this programming.  Up-to-Speed  ON   |

## Table 16 - Motor Connection Type

| Setting Switch #15 Description                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| In Delta connection mode, the device is designed to control a 6- or 12-lead motor. In line connection mode, the device is designed to control a 3- or 9-lead motor. Line ON |
| In Delta connection mode, the device is designed to control a 6- or 12-lead motor. In line connection mode, the device is designed to control a 3- or 9-lead motor. Line ON |

## Table 17 - Stop Delay

| Setting [seconds] Switch #16 Description   |    |
|--------------------------------------------|----|
| 0.0                                        | OFF When the delay is programmed, the motor continues to run for the programmed period of time after the run command is removed from the pgp controller. 0.75 ON    |
|                                            | OFF When the delay is programmed, the motor continues to run for the programmed period of time after the run command is removed from the pgp controller. 0.75 ON    |

The front of the SMC controller contains a dial that is used for setting the actual FLA of the motor. The label is designed to accommodate motors connected in the line or Delta mode. To determine the proper setting, look at the motor's nameplate and set the dial accordingly. The dial setting can be modified depending on the service factor of the motor.

## Figure 11 - Motor FLA Setting

<!-- image -->

## Motor Overload Trip Curves

The trip class should be set according to the motor's maximum permissible locked rotor time or the general thermal capabilities. Consult the motor manufacturer for recommendations on setting the trip class.

Figure 12 - Trip Class

<!-- image -->

## Input and Output Timing

Figure 13 - Input &amp; Output Timing

## Basic Timing Diagram, No Soft Stop

<!-- image -->

## Introduction

## Diagnostics Indication

Table 18 - LED Fault Indication &amp; Diagnostics

| Flashes  Fault Type   | Possible Fault Explanations                                                                                                                                                                              | Possible Solutions                                                                                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 Overload            | • Motor overload condition present. • FLA dial adjustment is not matched to motor type.                                                                                                                  | • Check for motor overload condition. • Verify actual motor current does not exceed FLA. • Verify/reset the FLA dial adjustment. • Program/modify the overload setting for load or duty cycle required. |
| 2 Overtemperature     | • Controller ventilation blocked. • Controller duty cycle exceeded. • Cooling fan not working. • Ambient temperature exceeded. • Failed control module. • Over-current condition with Overload disabled. | • Check for proper ventilation. • Verify duty cycle. • Connect or replace cooling fan. • Wait for controller to cool or provide external cooling. • Replace control module.                             |
|                       | 3 Phase Reversal • Incoming supply voltage is not the expected sequence.                                                                                                                                 | • Check power wiring. • Adjust dip switch #9 for desired sequence.                                                                                                                                      |

## Troubleshooting

The following topics are designed to assist in the troubleshooting and maintenance of the SMC™ controller. The items mentioned in this section are not intended to be all-inclusive and it is expected that these items should be used as reference only.

For safety of maintenance personnel as well as others who might be exposed to electrical hazards associated with maintenance activities, follow the local safety related work practices (such as NFPA 70E, Part II in the United States). Maintenance personnel must be trained in the safety practices, procedures, and requirements that pertain to their respective job assignments.

<!-- image -->

SHOCK HAZARD: Hazardous voltage is present in the motor circuit even when the 150-E controller is off. To avoid shock hazard, disconnect the main power before working on the controller, motor, and control devices (such as StartStop push buttons). Procedures that require parts of the equipment to be energized during troubleshooting, testing, etc., must be performed by properly qualified personnel, using appropriate local safety work practices and precautionary measures.

<!-- image -->

ATTENTION: Disconnect the controller from the motor before measuring insulation resistance (IR) of the motor windings. Voltages used for insulation resistance testing can cause SCR failure. Do not make any measurements on the controller with an IR tester (megger).

The LED status indicator on the front of the product provides limited status information regarding the condition of the controller. The conditions are as follows:

- LED Off — No control power or start command given.
- LED On — The device is active with starting, running, or stopping.
- LED Flashes — A fault has been experienced. Refer to table below for additional explanation.

<!-- image -->

## Table 18 - LED Fault Indication &amp; Diagnostics (Continued)

| Flashes  Fault Type      | Possible Fault Explanations                                                        | Possible Solutions                                                                                                                                                                                                                                                                                                     |
|--------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4  Phase Loss/ Open Load | • Missing Supply Phase. • Missing or unable to detect motor connection.            | • Check for open line (open fuse). • Check for incorrect wiring to load. • Verify proper operation of the fault contactor. • Verify connection type to motor (line or Delta). • Ensure product is sized correctly for motor.                                                                                           |
| 5 Phase Imbalance        | • Unbalanced Phase Currents (> 65% differential). • Incoming line voltage problem. | • Check motor current in each phase to verify imbalance. Motor current imbalance can indicate potential motor problem.                                                                                                                                                                                                 |
| 6 Shorted SCR            | • Shorted SCR. • Welded or latched bypass contactor.                               | • Verify connection type (line or Delta) and verify setting. • Perform continuity check across power poles (L1 – T1, L2 – T2, L3 - T3). Measurements should exceed 10 kΩ. For best results, remove line and load motor connections. • Cycle power to device and attempt to restart. If fault persists, replace device. |
|                          | 7 Test • Intended operation. • Reset fault.                                        |                                                                                                                                                                                                                                                                                                                        |
|                          | 12 Check Sum • Internal software corruption. • Replace device.                     |                                                                                                                                                                                                                                                                                                                        |

## Troubleshooting Steps

## Table 19 - Troubleshooting Steps

| Control                                                                                            | Device Status   | Solution                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prestart - no start command given but device is faulted.                                           | LED Flashing    | • Reset fault. • Allow device to cool (overload or SCR over temp). Reset fault. • Cycle power to device.                                                                                                                                                                                                                                                                  |
| Motor fails to start after start command given.                                                    | LED Off         | • Check control power. • Check control circuit connections.                                                                                                                                                                                                                                                                                                               |
|                                                                                                    | LED ON          | • Verify proper operation of fault contactor or isolation devices. • Check connections to the motor. • Verify line power and frequency are within specifications.                                                                                                                                                                                                         |
|                                                                                                    |                 | LED Flashing • See Table 18 for information related to specific fault codes.                                                                                                                                                                                                                                                                                              |
| Motor attempts to start after start command is given, but fails to reach an up-to-speed condition. | LED ON          | • Verify proper operation of the fault contactor or isolation devices. • Verify line power and frequency are within specifications. • Try increasing the initial torque or current limit setting.                                                                                                                                                                         |
|                                                                                                    |                 | LED Flashing • See Table 18 for information related to specific fault codes.                                                                                                                                                                                                                                                                                              |
| Motor stops abruptly and fails to restart.                                                         | LED Off         | • Check for a blown fuse or tripped circuit breaker. • Ensure the control power and start command are present. • Verify proper operation of the fault contactor or isolation devices.                                                                                                                                                                                     |
|                                                                                                    |                 | LED ON • Verify proper operation of the fault contactor or isolation devices.                                                                                                                                                                                                                                                                                             |
|                                                                                                    |                 | LED Flashing • See Table 18 for information related to specific fault codes.                                                                                                                                                                                                                                                                                              |
| Fault contactor fails to close when power is applied.                                              | All Conditions  | • Verify wiring to the coil. The contactor should close when power is applied to the controller. • Verify voltage across the coil (A1 to A2). • Check the resistance of the coil. Replace, if measured open. • Verify internal contact of the controller (terminals 97/98) are properly changing state. Replace the controller if the contact does not operate correctly. |

## Renewal Parts

Table 20 - Renewal Part Cat. Nos.

| Panel                    | Controller                  |                        |                     | Series B Devices                                    | Series C Devices                | Series C Devices   |
|--------------------------|-----------------------------|------------------------|---------------------|-----------------------------------------------------|---------------------------------|--------------------|
|                          |                             |                        |                     | Contactor                                           | Contactor Coil  Contactor       | Contactor Coil     |
| 150-E32NCE-FC 150-E32NCD |                             |                        | (optional) 150-CF64 |                                                     | 100-C37D00 TC473 100-E40KD00 —  |                    |
| 150-E51NCE-FC 150-E51NCD |                             |                        | (optional) 150-CF64 |                                                     | 100-C37D00 TC473 100-E40KD00 —  |                    |
| 150-E64NCE-FC            | 150-E64NCD                  | 150-E64NCD             | (optional) 150-CF64 |                                                     | 100-C37D00 TC473 100-E40KD00 —  |                    |
| 150-E74NCE-FC            | 150-E74NCD                  | 150-E74NCD             | 150-CF147           |                                                     | 100-C43D00 TD473 100-E52KD00    | —                  |
| 150-E104NCE-FC           | 150-E104NCD                 | 150-E104NCD            | 150-CF147           |                                                     | 100-C60D00 TE473 100-E65KD00    | —                  |
| 150-E147NCE-FC           | 150-E147NCD                 | 150-E147NCD            | 150-CF147           |                                                     | 100-C85D00 TE473 100-E80KD00    | —                  |
| 150-E234NCE-FC           | Complete Device 150-E234NCD |                        |                     | 41391-801-03 100-D180ED00 TGE865 100-E190KD11 TG907 |                                 |                    |
| 150-E234NCE-FC           | Control Module 150-ES1BX    |                        |                     | 41391-801-03 100-D180ED00 TGE865 100-E190KD11 TG907 |                                 |                    |
| 150-E234NCE-FC           | Power Pole 150-FPP135C      |                        |                     | 41391-801-03 100-D180ED00 TGE865 100-E190KD11 TG907 |                                 |                    |
| 150-E32NCA-FC            | 150-E32NCD                  | 150-E32NCD             | (optional) 150-CF64 |                                                     | 100-C37KA00 TC858 100-E40KD00 — |                    |
| 150-E51NCA-FC            | 150-E51NCD                  | 150-E51NCD             | (optional) 150-CF64 |                                                     | 100-C37KA00 TC858 100-E40KD00 — |                    |
| 150-E64NCA-FC            | 150-E64NCD                  | 150-E64NCD             | (optional) 150-CF64 |                                                     | 100-C37KA00 TC858 100-E40KD00 — |                    |
| 150-E74NCA-FC            | 150-E74NCD                  | 150-E74NCD             | 150-CF147           |                                                     | 100-C43KA00 TD858 100-E52KD00   | —                  |
| 150-E104NCA-FC           | 150-E104NCD                 | 150-E104NCD            | 150-CF147           |                                                     | 100-C60KA00 TE858 100-E65KD00   | —                  |
| 150-E147NCA-FC           | 150-E147NCD                 | 150-E147NCD            | 150-CF147           |                                                     | 100-C85KA00 TE858 100-E80KD00   | —                  |
| 150-E234NCA-FC           | Complete Device 150-E234NCD |                        |                     | 41391-801-03 100-D180EA00 TGE866 100-E190KD11 TG907 |                                 |                    |
| 150-E234NCA-FC           | Control Module 150-ES1BX    |                        |                     | 41391-801-03 100-D180EA00 TGE866 100-E190KD11 TG907 |                                 |                    |
| 150-E234NCA-FC           |                             | Power Pole 150-FPP135C |                     | 41391-801-03 100-D180EA00 TGE866 100-E190KD11 TG907 |                                 |                    |

## Electrical

## Specifications

Table 21 - Power Circuit

|                                                   | UL/cUL/CSA                                        | IEC                                 |
|---------------------------------------------------|---------------------------------------------------|-------------------------------------|
| Rated Operational Voltage 200…600V AC 200…500V AC | Rated Operational Voltage 200…600V AC 200…500V AC |                                     |
| Rated Insulation Voltage                          | 600V AC                                           | 500V AC                             |
| Di-electric Withstand                             | 2200V AC                                          | 2500V AC                            |
| Repetitive Peak                                   | 200…600V AC: 1600                                 | 500V AC: 1600                       |
| Rated Impulse Voltage                             | 6 kV                                              | 6 kV                                |
| Overvoltage Category                              | III                                               | III                                 |
| Number of Poles                                   | Equipment designed for 3-phase only               | Equipment designed for 3-phase only |
| Operating Frequency                               | 50/60 Hz                                          | 50/60 Hz                            |
|                                                   | 32/52/64                                          | AC-53b: 3.5-15:3585                 |
|                                                   | 74/104/147                                        | AC-53b: 4.5-30:1770                 |
|                                                   | 234                                               | AC-53b: 3.5-30:1770                 |
|                                                   | Line                                              | Delta                               |
|                                                   |                                                   | 32 6.3…19 10.9…32.9                 |
|                                                   | 51 10…30 17…51                                    |                                     |
|                                                   |                                                   | 64 12.3…37 21.3…64                  |
|                                                   |                                                   | 74 14.3…43 24.7…74                  |
|                                                   |                                                   | 104 20…60 34.7…104                  |
|                                                   | 147 28.3…85 49…147                                |                                     |
|                                                   |                                                   | 234 34…135 59…234                   |

|                           |                           | UL/cUL/CSA                                | IEC                               |
|---------------------------|---------------------------|-------------------------------------------|-----------------------------------|
| Rated Operational Voltage | Rated Operational Voltage | 100…120V AC, 200…240V AC 120V AC, 240V AC |                                   |
| Rated Insulation Voltage  | Rated Insulation Voltage  | —                                         | 300V AC                           |
| Di-electric Withstand     | Di-electric Withstand     | —                                         | 3000V                             |
| Rated Impulse Voltage     | Rated Impulse Voltage     | 3 kV                                      | 3 kV                              |
| Operating Frequency       | Operating Frequency       | 50/60 Hz                                  | 50/60 Hz                          |
|                           | 32/52/64                  | 215 mA @ 120V AC 180 mA @ 240V AC         | 215 mA @ 120V AC 180 mA @ 240V AC |
|                           | 74/104/147                | 200 mA @ 120V AC 100 mA @ 240V AC         | 200 mA @ 120V AC 100 mA @ 240V AC |
|                           | 234                       | 200 mA @ 120V AC 120 mA @ 240V AC         | 200 mA @ 120V AC 120 mA @ 240V AC |
|                           | 32/52/64                  | —                                         | —                                 |
|                           | 74/104/147                | —                                         | —                                 |
|                           | 234                       | 20VA                                      | 20VA                              |

Table 22 - Control Circuit

<!-- image -->

## Mechanical

Table 23 - Short-circuit Capabilities

|     | Type 1               | Type 1                     |
|-----|----------------------|----------------------------|
|     | Max Fuse Size & Type | Max Available Fault Rating |
| 32  | 70 A - RK5 5 kA      |                            |
| 32  | 125 A - K5           | 5 kA                       |
| 51  | 125 A - RK5          | 5 kA                       |
| 51  | 200 A - K5           | 10 kA                      |
| 64  | 125 A - RK5          | 5 kA                       |
| 64  | 200 A - K5           | 10 kA                      |
| 74  | 150 A - RK5          | 5 kA                       |
| 74  | 250 A - J            | 10 kA                      |
| 104 | 200 A - RK5          | 5 kA                       |
| 104 | 400 A - J            | 10 kA                      |
| 147 | 250 A - RK5          | 10 kA                      |
| 147 | 400 A - J            | 10 kA                      |
| 234 | 400 A - RK5          | 10 kA                      |
| 234 | 450 A - K5           | 10 kA                      |

## Table 24 - Auxiliary Contacts (Fault &amp; Aux #1)

|                                                           | UL/cUL/CSA                          | IEC                                 |
|-----------------------------------------------------------|-------------------------------------|-------------------------------------|
| Rated Operational Voltage 250V AC/30V DC 250V AC / 30V DC |                                     |                                     |
| Rated Insulation Voltage                                  | 250V                                | 250V AC                             |
| Di-electric Withstand                                     | —                                   | 4 kV                                |
| Rated Impulse Voltage                                     | 1500V AC                            | 2000V AC                            |
| Operating Frequency                                       | 50/60 Hz                            | 50/60 Hz                            |
| Utilization Category                                      | D300                                | AC-15/DC                            |
| Control Circuit Type                                      | Electro-magnetic Relay              | Electro-magnetic Relay              |
| Number of Contacts                                        | 1                                   | 1                                   |
| Contact Type                                              | Normally Open (N.O.)                | Normally Open (N.O.)                |
| Current Type                                              | AC/DC                               | AC/DC                               |
| Rated Operational Current (max)                           | 0.6 A @ 120V AC and 0.3 A @ 240V AC | 0.6 A @ 120V AC and 0.3 A @ 240V AC |
| Conventional Thermal Current (l th )                      | 1 A                                 | 1 A                                 |
| Make/Break VA 432/72                                      |                                     |                                     |

## Table 25 - Mechanical

| Attribute               | Attribute       | Value                                                       |
|-------------------------|-----------------|-------------------------------------------------------------|
| Resistance to Vibration | Operational     | 1.0 G Peak, 0.15 mm (0.006 in) displacement                 |
| Resistance to Vibration |                 | Non-Operational 2.5 G Peak, 0.38 mm (0.015 in) displacement |
| Resistance to Shock     | Operational     | 15 G                                                        |
| Resistance to Shock     | Non-Operational | 5.5 G                                                       |

## Environmental

## Approximate Dimensions and Shipping Weights

Table 26 - Environmental

| Attribute             | Value                                                 |
|-----------------------|-------------------------------------------------------|
| Operating Temperature | 0…50 °C (32…122 °F) Open 0…40 °C (32…104 °F) Enclosed |
| Altitude              | 2000 m (6560 ft)                                      |
| Humidity              | 5…95% (non-condensing)                                |
| Pollution Degree      | 2                                                     |

Dimensions given are in mm (in.). Dimensions are not intended to be used for manufacturing purposes.

Figure 14 - Approximate Dimensions

<!-- image -->

Table 27 - Dimensions &amp; Shipping Weights

| Controller Size [A]   |             | A (Width) B (Height) C (Depth)   |              | D            | E             | 4 x Ø (Hole Diameter)   | Approximate Weight   |
|-----------------------|-------------|----------------------------------|--------------|--------------|---------------|-------------------------|----------------------|
| 32/52/64              | 178 (7.01)  | 144 (5.67)                       | 115.7 (4.56) | 165.1 (6.5)  | 127 (5)       | 5.6 (0.22)              | 4 lbs (2 kg)         |
| 74/104/147            | 240 (9.45)  | 225 (8.86)                       | 147.9 (5.82) | 215 (8.46)   | 205 (8.07)    | 6.6 (0.26)              | 14 lbs (6 kg)        |
| 234                   | 362 (14.25) | 515 (20.28)                      | 216.4 (8.52) | 330.2 (13.0) | 489.5 (19.27) | 8.7 (0.343)             | 51 lbs (23 kg)       |

## History of Changes

This appendix contains the new or updated information for each revision of this publication. These lists include substantive updates only and are not intended to reflect all changes. Translated versions are not always available for each revision.

## 150-UM009D-EN-P, February 2011

| Topic                                                    |
|----------------------------------------------------------|
| Update to European Communities (EC) Directive Compliance |
| Added 100-E contactor options for Series C devices       |
| Updated C234 terminal torque specifications              |

<!-- image -->

## Notes:

## Notes:

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

&amp;

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Allen-Bradley, expanding human possibility, Rockwell Automation, and SMC are trademarks of Rockwell Automation, Inc Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000,Fax:（1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIAPACIFIC:RockwellAutomation,Level14,CoreF,Cyberport3,100CyberportRoad,HongKong,Tel:(852)28874788,Fax:(852)25081846