## Kinetix 6200 and Kinetix 6500 Safe Torque-off Multi-axis Servo Drives

Catalog Numbers 2094-SE02F-M00-S0, 2094-EN02D-M01-S0

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important User Information

Solid-state equipment has operational characteristics differing from those of electromechanical equipment. Safety Guidelines for the Application, Installation and Maintenance of Solid State Controls (publication SGI-1.1 available from your local Rockwell Automation® sales office or online at http://www.rockwellautomation.com/literature/) describes some important differences between solid-state equipment and hard-wired electromechanical devices. Because of this difference, and also because of the wide variety of uses for solid-state equipment, all persons responsible for applying this equipment must satisfy themselves that each intended application of this equipment is acceptable.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

Identifies information that is critical for successful application and understanding of the product.

Allen-Bradley, Kinetix, RSLogix, TechConnect, Rockwell Automation, and Rockwell Software are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

## New and Updated Information

This manual contains new and updated information.

This revision includes new material for the 2090-K6CK-D44S0 low-profile connector kit and 2090-CS0DSDS-AAxx interface cable for cascading the safe torque-off signals from drive-to-drive.

| Section Topic   |                                                                                            | Page   |
|-----------------|--------------------------------------------------------------------------------------------|--------|
| Chapter 2       | Added a description and connection diagram for the 2090-K6CK-D44S0 connector kit. 16       |        |
| Chapter 3       | Updated Safety Input Wiring diagram to use 24VPWR (IOD-14, IOD-15)                         | 22     |
| Chapter 4       | Updated Cascaded Connections diagram to use 24VPWR (IOD-14, IOD-15)                        | 27     |
| Chapter 4       | Updated 2090-K6CK-D44M wiring examples to use 24VPWR (IOD-14, IOD-15) 28                   |        |
| Chapter 4       | Added 2090-K6CK-D44S0 wiring examples                                                      | 29…30  |
| Chapter 4       | Added Kinetix 6200/6500 cascading safe torque-off cable example                            | 31     |
| Chapter 4       | Added 2090-CS0DSDS-AAxx cable pinout diagram and termination table                         | 31     |
| Appendix A      | Updated General Specifications with value for reset time                                   | 37     |
| Appendix A      | Added footnotes to clarify the effect cascading drives has on reaction time and reset time | 37     |

## Notes:

Preface

|                             | About This Publication. . .                                                                                                                                     | . . . . . . . . . . . . . . . . . . . . 7   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
|                             | . . . . . . . . . . . . . . . . . . . . . .  Who Should Use This Manual . . .                                                                                   |                                             |
|                             | . . . . . . . . . . . . . . . . . .  Terminology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 | . . . . . . . . . . . . . . . . . 7         |
|                             | Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . .                                                                                       | . . . . . . . . . . . . . . . . . . . . . 8 |
|                             | Chapter 1                                                                                                                                                       |                                             |
| Safety Concept              | Introduction. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                                                            | . . . . . . . . . . . . . . . . . . . 9     |
|                             | Safety Certification. . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | . . . . . . . . . . . . . . . . . . . . . 9 |
|                             | Important Safety Considerations  . . . . . . . . . . . . . . . .                                                                                                | . . . . . . . . . . . . . . 10              |
|                             | Safety Category 4 Performance Definition. . . . . . . . . . . . . . . . . . . . . . 10                                                                          |                                             |
|                             | Stop Category 0 Definition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10                                                            |                                             |
|                             | Performance Level and Safety Integrity Level (SIL) CL3 . . . . . . . . . 11                                                                                     |                                             |
|                             | PFD and PFH Definitions . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . . 11          |
|                             | PFD and PFH Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                                                 |                                             |
|                             | Safe State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                                   |                                             |
|                             | Safety Reaction Time. . . .  . . . . . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . . . . . 12    |
|                             | Contact Information If Failure Occurs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                                                               |                                             |
|                             | Automatic Drive Replacement (ADR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                                                                  |                                             |
|                             | Chapter 2                                                                                                                                                       |                                             |
| Installation and Wiring     | Introduction. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                                                              | . . . . . . . . . . . . . . . . . . 13      |
|                             | General Safety Information . . . . .  . . . . . . . . . . . . . . . . . .                                                                                       | . . . . . . . . . . . . . . . . 13          |
|                             | Power Supply Requirements . . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . 14            |
|                             | Wiring the Safety Connections. . .  . . . . . . . . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . 14            |
|                             | Using the 2090-K6CK-D44M Low-profile Connector Kit . . . . . . 14                                                                                               |                                             |
|                             | Using the 2090-K6CK-D44S0 Low-profile Connector Kit . . . . . . 16                                                                                              |                                             |
|                             | Using the Motion-allowed Plug. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                                                                 |                                             |
|                             | Terminal Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                                                   |                                             |
|                             | Chapter 3                                                                                                                                                       |                                             |
| Safe Torque-off I/O Signals | Introduction. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                                                              | . . . . . . . . . . . . . . . . . . 19      |
|                             | Inputs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                                  |                                             |
|                             | Discrepancy Time . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                       | . . . . . . . . . . . . . . . . 20          |
|                             | Reset Input (Reset_In). . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . 23            |
|                             | Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                                    |                                             |
|                             | Safe Stop Output (SS_Out) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                                                              |                                             |
|                             | Safe Stop Reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                                                |                                             |
|                             | Safe Stop Wiring Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26                                                     |                                             |

Chapter 4

| Multi-axis Cascaded Systems         | Introduction . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 27     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
|                                     | Cascaded Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                |                                            |
|                                     | Safe Stop Wiring Examples. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28                 |                                            |
|                                     | 2090-K6CK-D44M Connector Kit Examples. . . . . . . . . . . . . . . . . . . 28                                               |                                            |
|                                     | 2090-K6CK-D44S0 Connector Kit Examples . . . . . . . . . . . . . . . . . . 29                                               |                                            |
|                                     | Chapter 5                                                                                                                   |                                            |
| Troubleshooting the Safe Torque-off | Introduction . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 33     |
| Drive                               | Nonrecoverable Faults . . .  . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . 33   |
|                                     | Fault Recovery . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . . . . . 33 |
|                                     | Input and Output Faults . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . 34         |
|                                     | Fault Codes and Descriptions   . . . . . . . . . . . . . . . . . . .                                                        | . . . . . . . . . . . . . . . . . . 34     |
|                                     | Status Attributes . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . 35             |
|                                     | Guard Status Attributes . . . . . .  . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . 35           |
|                                     | Guard Fault Attributes . . . . . . .  . . . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . . 36           |
|                                     | Appendix A                                                                                                                  |                                            |
| Specifications                      | Introduction . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 37 |                                            |
|                                     | General Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37           |                                            |
|                                     | Certifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38   |                                            |

Index

## About This Publication

## Who Should Use This Manual

## Terminology

Table 1 - Common Safety Terminology

| Abbreviation Full Term   |                                             | Definition                                                                                                                                                                                                               |
|--------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1oo2                     | One out of Two                              | Refers to the behavioral design of a dual-channel safety system.                                                                                                                                                         |
| CAT                      | Category                                    | –                                                                                                                                                                                                                        |
| EN                       | European Norm                               | The official European Standard.                                                                                                                                                                                          |
| ESPE                     | Electro-sensitive Protective Equipment      | An assembly of devices and/or components working together for protective tripping or presence sensing purposes and comprising as a minimum: · a sensing device. · controlling/monitoring devices. · output signal-switching devices (OSSD).                                                                                                                                                                                                                          |
| FMEA                     | Failure Mode and Effects Analysis           | Analysis of potential failure modes to determine the effect upon the system and identify ways to mitigate those effects.                                                                                                 |
| IEC                      | International Electrotechnical Commission – |                                                                                                                                                                                                                          |
| IGBT                     | Insulated Gate Bi-polar Transistors         | Typical power switch used to control main current.                                                                                                                                                                       |
| HFT                      | Hardware Fault Tolerance                    | The HFT equals n, where n+1 faults could cause the loss of the safety function. An HFT of 1 means that 2 faults are required before safety is lost.                                                                      |
| MP                       | Motion Power                                | –                                                                                                                                                                                                                        |
| OSSD                     | Output Signal-switching Device              | The component of the electro-sensitive protective equipment (ESPE) connected to the control system of a machine, which, when the sensing device is actuated during normal operation, responds by going to the OFF-state. |
| PC                       | Personal Computer                           | Computer used to interface with and program your safety system.                                                                                                                                                          |
| PFD                      | Probability of Failure on Demand            | The average probability of a system to fail to perform its design function on demand.                                                                                                                                    |
| PFH                      | Probability of Failure per Hour             | The probability of a system to have a dangerous failure occur per hour.                                                                                                                                                  |
| PL                       | Performance Level                           | ISO 13849-1 safety rating.                                                                                                                                                                                               |
| S0                       | 2094-SE02F-M00-S0                           | Catalog number for Kinetix 6200 drives with Safe Torque-off functionality.                                                                                                                                               |
| S0                       | 2094-EN02D-M01-S0                           | Catalog number for Kinetix 6500 drives with Safe Torque-off functionality.                                                                                                                                               |

This manual explains how the Kinetix® 6200 and Kinetix 6500 drives can be used in Safety Integrity Level (SIL) CL3, Performance Level [PLe], or Category (CAT) 4 applications. It describes the safety requirements, including PFD and PFH values and application verification information, and provides information on configuring and troubleshooting the Kinetix 6200 and Kinetix 6500 drives with safe torque-off functionality.

Use this manual if you are responsible for designing, configuring, or troubleshooting safety applications that use Kinetix 6200 or Kinetix 6500 drives with safe torque-off functionality.

You must have a basic understanding of electrical circuitry and familiarity with Kinetix 6200 and Kinetix 6500 drives. You must also be trained and experienced in the creation, operation, and maintenance of safety systems.

The following table defines common safety terms used in this manual.

Table 1 - Common Safety Terminology (continued)

| Abbreviation Full Term   |                        | Definition                                                                                              |
|--------------------------|------------------------|---------------------------------------------------------------------------------------------------------|
| SFF                      | Safe Failure Fraction  | The sum of safe failures plus the sum of dangerous detected failures divided by the sum of all failures |
| SIL                      | Safety Integrity Level | A measure of a products ability to lower the risk that a dangerous failure could occur.                 |
| SS                       | Safe Stop              | –                                                                                                       |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                        | Description                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002                | Information on installing, configuring, startup, troubleshooting, and applications for your Kinetix 6200 and Kinetix 6500 servo drive system.         |
| Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Safety Reference Manual, publication 2094-RM001             | Information on wiring, troubleshooting, and configuring your Kinetix 6200 and Kinetix 6500 servo drives with the safe speed-monitoring functionality. |
| Kinetix Safe-off Feature Safety Reference Manual, publication GMC-RM002                                         | Information on wiring and troubleshooting your Kinetix 6000 servo drives with the safe-off feature.                                                   |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                           | Information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                |
| EMC Noise Management DVD, publication GMC-SP004                                                                 | Information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                |
| Kinetix Motion Control Selection Guide, publication GMC-SG001                                                   | Specifications, motor/servo-drive system combinations, and accessories for Kinetix motion control products.                                           |
| Safety Guidelines for the Application, Installation and Maintenance of Solid State Control, publication SGI-1.1 | Describes important differences between solid state control and hardwired electromechanical devices.                                                  |

You can view or download publications at:

http://www.rockwellautomation.com/literature. To order paper copies of technical documentation, contact your local Allen-Bradley® distributor or Rockwell Automation sales representative.

## Introduction

## Safety Certification

## Safety Concept

This chapter describes the safety performance level concept and how the Kinetix 6200 and Kinetix 6500 drives can meet the requirements for SIL CL3, CAT 4, or PLe applications.

| Topic                                 |   Page |
|---------------------------------------|--------|
| Safety Certification                  |      9 |
| PFD and PFH Definitions               |     11 |
| PFD and PFH Data                      |     11 |
| Safe State                            |     12 |
| Safety Reaction Time                  |     12 |
| Contact Information If Failure Occurs |     12 |
| Automatic Drive Replacement (ADR)     |     12 |

The Kinetix 6200 and Kinetix 6500 drives are certified for use in safety applications up to and including SIL CL3 according to EN 61800-5-2, EN 61508, and EN 62061, Performance Level PLe and CAT 4 according to ISO 13849-1. Safety requirements are based on the standards current at the time of certification.

The TÜV Rheinland group has approved the Kinetix 6200 and Kinetix 6500 drives for use in safety-related applications where the de-energized state is considered to be the safe state. All of the examples related to I/O included in this manual are based on achieving de-energization as the safe state for typical Machine Safety and Emergency Shutdown (ESD) systems.

<!-- image -->

## Important Safety Considerations

You are responsible for the following:

- The set-up, safety rating, and validation of any sensors or actuators connected to the system
- Completing a system-level risk assessment and reassessing the system any time a change is made
- Certification of the system to the desired safety performance level
- Project management and proof testing
- Access control to the system, including password handling

## IMPORTANT

When applying functional safety, restrict access to qualified, authorized personnel who are trained and experienced.

<!-- image -->

ATTENTION: When designing your system, consider how personnel will exit the machine if the door locks while they are in the machine. Additional safeguarding devices may be required for your specific application.

## Safety Category 4 Performance Definition

The safety-related parts have to be designed with the following considerations to achieve Safety Category 4 according to ISO 13849-1:2006:

- The safety-related parts of machine control systems and/or their protective equipment, as well as their components, must be designed, constructed, selected, assembled, and combined in accordance with relevant standards so that they can withstand expected conditions.
- Basic safety principles must be applied.
- A single fault in any of its parts does not lead to a loss of safety function.
- A single fault is detected at or before the next demand of the safety function, or, if this detection is not possible, then an accumulation of faults must not lead to a loss of the safety function.
- The average diagnostic coverage of the safety-related parts of the control system must be high, including the accumulation of faults.
- The mean time to dangerous failure of each of the redundant channels must be high.
- Measures against common cause failure must be applied.

## Stop Category 0 Definition

Stop Category 0 is achieved with immediate removal of power to the actuator, resulting in an uncontrolled coast to stop. Safe Torque Off accomplishes a Stop Category 0 stop.

## PFD and PFH Definitions

## PFD and PFH Data

## Performance Level and Safety Integrity Level (SIL) CL3

For safety-related control systems, Performance Level (PL), according to ISO 13849-1, and SIL levels, according to EN 61508 and EN 62061, include a rating of the system's ability to perform its safety functions. All of the safety-related components of the control system must be included in both a risk assessment and the determination of the achieved levels.

Refer to the ISO 13849-1, EN 61508, and EN 62061 standards for complete information on requirements for PL and SIL determination.

Safety-related systems can be classified as operating in either a Low Demand mode, or in a High Demand/Continuous mode:

- Low Demand mode: where the frequency of demands for operation made on a safety-related system is no greater than one per year or no greater than twice the proof-test frequency.
- High Demand/Continuous mode: where the frequency of demands for operation made on a safety-related system is greater than once per year or greater than twice the proof test interval.

The SIL value for a low demand safety-related system is directly related to orderof-magnitude ranges of its average probability of failure to satisfactorily perform its safety function on demand or, simply, average probability of failure on demand (PFD). The SIL value for a High Demand/Continuous mode safety-related system is directly related to the probability of a dangerous failure occurring per hour (PFH).

These PFD and PFH calculations are based on the equations from Part 6 of EN 61508 and show worst-case values.

This table provides data for a 20-year proof test interval and demonstrates the worst-case effect of various configuration changes on the data.

Table 2 - PFD and PFH for 20-year Proof Test Interval

| Attribute Value   |
|-------------------|
| PFH [1e-9] 4.09   |
| PFD [1e-4] 3.90   |
| SFF % 99.5        |

## Safe State

## Safety Reaction Time

## Contact Information If Failure Occurs

## Automatic Drive Replacement (ADR)

The Safe State encompasses all operation that occurs outside of the other monitoring and stopping behavior defined as part of the drive. While the drive is in the Safe State, all safety control outputs are in their safe state (de-energized).

When you cycle power, the drive enters the Safe State for self-testing. If the selftests pass, the drive remains in the Safe State until a successful safe stop reset occurs.

If a Safe State fault is detected, the drive goes to the Safe State. This includes faults related to integrity of hardware or firmware.

For more information on faults, refer to Chapter 5 .

The safety reaction time is the amount of time from a safety-related event as input to the system until the system is in the Safe State.

The safety reaction time from an input signal condition that triggers a safe stop, to the initiation of the Safe Stop Type, is 12 ms, max.

## IMPORTANT

For cascaded systems, the reaction time is multiplied by the number of drives in the drive system. For example, drive systems with three cascaded drives (first, middle, and last), have a reaction time of 36 ms, max.

If you experience a failure with any safety-certified device, contact your local Rockwell Automation distributor. With this contact, you can do the following:

- Return the device to Rockwell Automation so the failure is appropriately logged for the catalog number affected and a record is made of the failure.
- Request a failure analysis (if necessary) to determine the probable cause of the failure.

You can replace IAM and AM power modules, and the associated control modules, at any time without any need for configuration or program changes.

## Introduction

## General Safety Information

## Installation and Wiring

This chapter provides details on connecting devices and wiring the 2090-K6CK-D44M and 2090-K6CK-D44S0 low-profile connector kits.

| Topic                         |   Page |
|-------------------------------|--------|
| General Safety Information    |     13 |
| Power Supply Requirements     |     14 |
| Wiring the Safety Connections |     14 |
| Terminal Connections          |     18 |

<!-- image -->

ATTENTION: The drive is intended to be part of the safety-related control system of a machine. Before installation, a risk assessment should be performed to determine whether the specifications of this safety option are suitable for all foreseeable operational and environmental characteristics for the system to which it is to be installed.

Observe all electrical safety regulations stipulated by the appropriate technical authorities.

<!-- image -->

ATTENTION: Make sure that the electrical power supplied to the drive is switched off before making connections.

Refer to the Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002, for more information.

<!-- image -->

## Power Supply Requirements

## Wiring the Safety Connections

The external power supply must conform to the Directive 2006/95/EC Low Voltage, by applying the requirements of EN61131-2 Programmable Controllers, Part 2 - Equipment Requirements and Tests and one of the following:

- EN60950 - SELV (safety extra low voltage)
- EN60204 - PELV (protective extra low voltage)
- IEC 60536 Safety Class III (SELV or PELV)
- UL 508 Limited Voltage Circuit
- 21.6…28.8V DC must be supplied by a power supply that complies with IEC/EN60204 and IEC/EN 61558-1

For planning information, refer to the guidelines in Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

Safety, I/O, and auxiliary feedback connections are made by using the 2090-K6CK-D44M low-profile connector kit. I/O and cascading drive-to-drive safe torque-off connections can be made by using the 2090-K6CK-D44S0 low-profile connector kit. When the safety, I/O, and auxiliary feedback are not required for the application, the motion-allowed plug is used to make the drive operational.

## IMPORTANT

Remove power to the IAM or AM power module before installing either the low-profile connector kit or the motion-allowed plug.

## Using the 2090-K6CK-D44M Low-profile Connector Kit

The 2090-K6CK-D44M connector kit includes one motion-allowed jumper. Remove the jumper to wire the safe torque-off connections. Install the jumper when your application is not using the safe torque-off functionality, but your application requires I/O or auxiliary feedback connections.

## IMPORTANT

You must remove the motion-allowed jumper to wire the safe torque-off connections.

<!-- image -->

Refer to the Kinetix 6200 and Kinetix 6500 Modular Servo Drive User Manual, publication 2094-UM002, for other wiring examples using low-profile connector kits.

## Using the 2090-K6CK-D44S0 Low-profile Connector Kit

The 2090-K6CK-D44S0 connector kit includes two motion-allowed jumpers. Remove the jumpers to wire the safe torque-off connections. Install the jumper when your application is not using the safe torque-off functionality, but your application requires I/O connections.

The 2090-K6CK-D44S0 connector kit lets you cascade the safe torque-off signals from drive-to-drive by using the 2090-CS0DSDS-AAxx interface cable.

## IMPORTANT

You must remove the motion-allowed jumpers to wire the safe torque-off connections.

Figure 2 - Making 2090-K6CK-D44S0 Safety Connections

<!-- image -->

Refer to the Kinetix 6200 and Kinetix 6500 Modular Servo Drive User Manual, publication 2094-UM002, for other wiring examples using low-profile connector kits.

## Using the Motion-allowed Plug

Because the safe torque-off feature of Kinetix 6200 and Kinetix 6500 control modules (catalog numbers 2094-xx02x-M0x-S0) is not configured, the safe torque-off functionality is always operational. If you do not want to use the safe torque-off feature, wiring of the safe stop inputs (SS\_IN\_CH0/1) are still required to operate the drive.

For this reason, the 2094-xx02x-M0x-S0 control modules ship with the motion-allowed plug. The plug inserts into the IOD connector and provides connections designed to defeat the safe torque-off function.

Figure 3 - Motion-allowed Plug Wiring

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SLS_IN_CH3      |              24 |
|              23 | SLS_IN_CH2      |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |
|              15 | 24VCOM          |              15 |
|              14 | 24VPWR          |              14 |

Kinetix 6200 and Kinetix 6500 Safe Torque-off Control Module IOD (44-pin) Connector

If your application does not require any I/O, safety, or auxiliary feedback connections, use the motion-allowed plug supplied with your drive to defeat the safe torque-off functionality.

TIP

Figure 4 - Motion-allowed Plug Installation

<!-- image -->

## Terminal Connections

Prepare wires for termination on the IOD connector with a 5 mm (0.2 in.) strip length. Tighten all terminal screws firmly and recheck them after all connections have been made. Recommended terminal screw torque is 0.4 N·m (3.5 lb·in).

Refer to page 37 for the I/O signal electrical specifications.

Table 3 - IOD Connector Pinouts

| IOD Pin  Description Signal                             |                  |
|---------------------------------------------------------|------------------|
| 0 Chassis ground                                        | Shield           |
| 1  Sine differential input + A differential input +     | AUX_SIN+ AUX_A+  |
| 2  Sine differential input - A differential input -     | AUX_SIN AUX_A-                  |
| 3  Cosine differential input + B differential input +   | AUX_COS+ AUX_B+  |
| 4  Cosine differential input - B differential input -   | AUX_COS AUX_B-                  |
| 5  Data differential input + Index differential input + | AUX_DATA+ AUX_I+ |
| 6  Data differential input - Index differential input - | AUX_DATA AUX_I-                  |
| 7 Clock output +                                        | AUX_CLK+         |
| 8 Clock output -                                        | AUX_CLK-         |
| 9 Encoder 5V power output                               | EPWR_5V          |
| 10 Encoder common                                       | ECOM             |
| 11 Encoder 9V power output                              | EPWR_9V          |
| 12 Reserved                                             | –                |
| 13 Reserved                                             | –                |
| 14 24V power out                                        | 24VPWR  (1)      |
| 15 24V common                                           | 24VCOM (1)       |
| 16 Reserved                                             | –                |
| 17 Safety 24V power input                               | SPWR             |
| 18 Safety 24V common                                    | SCOM             |
| 19 Safe stop input 0                                    | SS_IN_CH0        |
| 20 Safe stop input 1                                    | SS_IN_CH1        |
| 21 Safe stop output 0                                   | SS_OUT_CH0       |
| 22 Safe stop output 1                                   | SS_OUT_CH1       |

| IOD Pin  Description Signal   |             |
|-------------------------------|-------------|
| 23 Safe stop input 2          | SS_IN_CH2   |
| 24 Safe stop input 3          | SS_IN_CH3   |
| 25 Reset reference            | RESET_REF   |
| 26 Reset input                | RESET_IN    |
| 27 Pulse test output 0        | TEST_OUT_0  |
| 28 Pulse test output 1        | TEST_OUT_1  |
| 29 Reserved                   | –           |
| 30 Reserved                   | –           |
| 31 Reserved                   | –           |
| 32 Reserved                   | –           |
| 33 Reserved                   | –           |
| 34 Reserved                   | –           |
| 35 Reserved                   | –           |
| 36 Reserved                   | –           |
| 37 Reserved                   | –           |
| 38 Reserved                   | –           |
| 39 24V power out              | 24VPWR  (2) |
| 40 24V common                 | 24VCOM      |
| 41 Digital input 1            | INPUT1      |
| 42 Digital input 2            | INPUT2      |
| 43 Digital input 3            | INPUT3      |
| 44 Digital input 4            | INPUT4      |

## Introduction

## Inputs

## Safe Torque-off I/O Signals

This chapter describes the safe torque-off input and output signals of the Kinetix 6200 and Kinetix 6500 drives.

| Topic                    |   Page |
|--------------------------|--------|
| Inputs                   |     19 |
| Outputs                  |     23 |
| Safe Stop Wiring Example |     26 |

The Kinetix 6200 and Kinetix 6500 drives have two sets of dual-channel inputs. Each dual-channel input supports the safe stop (SS) function of the drive.

The SS\_IN\_CH0/1 inputs are intended for connection to a non-switching E-stop device (dry contact). It controls the safe-off request initiated by a transition from ON to OFF.

The SS\_IN\_CH2/3 inputs are intended for connection to an OSSD device or as a cascaded input from another safety axis. It controls the safe-off request initiated by a transition from ON to OFF.

The SS\_IN\_CH0/1 inputs are electrically identical and rely on a pair of pulse test outputs, TEST\_OUT\_0 and TEST\_OUT\_1.

## IMPORTANT

Only one pair of dual-channel inputs can be used at the same time.

When both channels are active, if one channel's input terminal transitions from active to inactive and back to active, while the other channel's input terminal remains active, both channels must go inactive at the same time before the evaluated status may return to ON. This condition is called 'cycle inputs required'.

<!-- image -->

<!-- image -->

An Input fault occurs if the inputs are discrepant for longer than one second.

For SS\_IN\_CH0/1, use TEST\_OUT\_0/1 as a reference signal, or a fault occurs.

For more information on I/O faults, refer to Troubleshooting the Safe Torque-off Drive on page 33 .

## Discrepancy Time

The maximum discrepancy time between two inputs is 1.0 second. If both inputs do not change within 1.0 second, an input fault is displayed, the safety circuit is activated, and torque is removed from the motor.

Figure 6 - Discrepancy Time

<!-- image -->

Behavior of reset and safe-off inputs while transitioning from Safe\_Off state to Safe\_Monitor state.

Figure 7 - Reset Behavior

<!-- image -->

## IMPORTANT

When the inactive 'OFF' state of RESET\_IN transitions to the active 'ON' state, following a successful reset, the time to re-enable gate power and gate enable, and set dual-channel safe-off outputs to active 'ON' state will not exceed 20 ms.

## IMPORTANT

## IMPORTANT

If SS\_IN\_CH0/1 are used, then additional debounce filter delay of 36 ms is applied to Ton delay.

After a successful SO Reset, the RSLogix™ 5000 software program must issue an MSF instruction prior to restarting the machine.

Figure 8 - Safety Input Wiring Examples

<!-- image -->

## IMPORTANT

Cross wiring of Test Outputs to Inputs is not allowed. For example, do not connect TEST\_OUT\_0 to Input 1 or TEST\_OUT\_1 to Input 0.

Table 4 - IOD Connector Input Terminals

| Safe Stop Function Signal IOD Pin    |
|--------------------------------------|
| Input 0 = Channel 0 SS_IN_CH0 IOD-19 |
| Input 1 = Channel 1 SS_IN_CH1 IOD-20 |
| Input 2 = Channel 2 SS_IN_CH2 IOD-23 |
| Input 3 = Channel 3 SS_IN_CH2 IOD-24 |

Short-circuits of the input loop to ground or 24V will be detected. For dual-channel inputs, cross loops will also be detected.

## Outputs

## Reset Input (Reset\_In)

The Reset input is for reset and monitoring of the safety circuit. RESET\_REF provides reference voltage for the RESET\_IN input.

For automatic reset option, wire the reset input terminal (IOD-26) to the RESET\_REF terminal, (IOD-25).

Figure 9 - RESET\_IN Terminal Example

<!-- image -->

The drive has safe-stop safety control outputs.

See the specifications in Appendix A to verify your power requirements.

## Safe Stop Output (SS\_Out)

The safe state for this signal is OFF.

These outputs are typically used in multi-axis applications. In multi-axis applications, you can use these outputs to daisy-chain the master drive to a slave.

For SS\_Out to SS\_In\_CH2/3 cascaded signals, the interface is a dual-channel sourcing solid-state safety output connected to a dual-channel safety input. The outputs are pulse-tested.

Figure 10 - SS\_Out to SS\_In Connections for Multi-axis Applications

<!-- image -->

For more information on multi-axis configurations, see Cascaded Configurations starting on page 27 .

Alternately, the first SS\_Out output may be used to signal a programmable logic controller (PLC) that a Safe Stop has been requested.

If the SS\_In is ON (closed) and a successful Safe Stop Reset is performed, the SS\_Out output is turned ON.

If the Safe Stop is initiated or if a Safe Stop is initiated due to a fault, the SS\_Out output is turned OFF.

If an error is detected on either channel of the dual-channel output, a fault occurs, which initiates the Category 0 Stop. The fault is latched until the drive is successfully reset.

For more information on faults, refer to Chapter 5 .

## Safe Stop Reset

Safe torque-off drives provide a Reset Input (RESET\_IN) for resetting the drive after a fault, and for synchronizing restart of several cascading drives. The Reset Input (RESET\_IN) is not safety certified and does not have dual-channel capability. Automatic reset functionality, if needed, can be achieved by hardwiring the RESET\_REF and RESET\_IN terminals together.

The Safe-off Reset (SO Reset) is a reset from the Safe-off State to the active safe monitor state. The reset is successful if the SS\_In input is ON and no faults are present. The SO Reset occurs after the SS\_IN inputs have transitioned to ON and RESET\_IN is ON. After a successful SO Reset, RESET\_IN may transition to the OFF state.

<!-- image -->

ATTENTION: A reset of the Safe Stop function can result in machine operation.

<!-- image -->

ATTENTION: The Safe Stop Reset does not provide safety-related restart according to EN 60204-1. Restart must be performed by external measures if automatic restart could result in a hazardous situation. You are responsible for determining whether automatic restart could pose a hazard.

When an SO Reset is requested, all diagnostic tests that can be performed prior to outputs being energized are performed prior to a successful SO Reset. If a diagnostic test can be performed only when outputs are energized, the test is performed immediately following the SO Reset.

## Faults

If a fault occurs, the SS\_In inputs in use must turn OFF and ON again to reset the GuardResetRequiredStatus bit before a successful SO Reset can occur.

## Safe Stop Wiring Example

This example illustrates safe stop wiring.

Figure 11 - Master, Safe Stop (First or Single Unit)

<!-- image -->

## Introduction

## Cascaded Configurations

## Multi-axis Cascaded Systems

This chapter describes cascaded multi-axis drive operation and provides wiring examples for cascaded multi-axis drive systems.

| Topic                     |   Page |
|---------------------------|--------|
| Cascaded Configurations   |     27 |
| Safe Stop Wiring Examples |     28 |

For cascaded drives, connect the safety switches to the safety inputs (SS\_In) of only the first axis. The inputs are cascaded from one drive to the next by connecting the outputs from the previous drive to the inputs of the next drive.

<!-- image -->

Figure 12 - Cascaded Connections

<!-- image -->

## Safe Stop Wiring Examples

Cascaded configurations can be wired with either the 2090-K6CK-D44M or 2090-K6CK-D44S0 low-profile connector kits. The 2090-K6CK-D44S0 connector is designed specifically for cascading the safe torque-off signals from drive-to-drive.

The examples shown are safe-stop configurations that use a dry-contact safety device.

## 2090-K6CK-D44M Connector Kit Examples

Figure 13 - Cascading Safe Stop Non-OSSD Device Wiring Example

<!-- image -->

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SS_IN_CH3       |              24 |
|              23 | SS_IN_CH2       |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |
|              15 | 24VCOM          |              15 |
|              14 | 24VPWR          |              14 |

<!-- image -->

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SS_IN_CH3       |              24 |
|              23 | SS_IN_CH2       |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |
|              15 | 24VCOM          |              15 |
|              14 | 24VPWR          |              14 |

Figure 14 - Cascading Safe Stop OSSD Device Wiring Example

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SS_IN_CH3       |              24 |
|              23 | SS_IN_CH2       |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |
|              15 | 24VCOM          |              15 |
|              14 | 24VPWR          |              14 |

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SS_IN_CH3       |              24 |
|              23 | SS_IN_CH2       |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |
|              15 | 24VCOM          |              15 |
|              14 | 24VPWR          |              14 |

## 2090-K6CK-D44S0 Connector Kit Examples

The 2090-K6CK-D44S0 connector kit and 2090-CS0DSDS-AAxx safe-off cable are designed specifically for cascading the safe torque-off signals from drive-to-drive.

|   IOD Connector (P5) | IOD Connector (P5)   |   IOD Connector (P5) |
|----------------------|----------------------|----------------------|
|                   28 | TEST_OUT_1           |                   28 |
|                   27 | TEST_OUT_0           |                   27 |
|                   24 | SS_IN_CH3            |                   24 |
|                   23 | SS_IN_CH2            |                   23 |
|                   22 | SS_OUT_CH1           |                   22 |
|                   21 | SS_OUT_CH0           |                   21 |
|                   20 | SS_IN_CH1            |                   20 |
|                   19 | SS_IN_CH0            |                   19 |

|   IOD Connector (P5) | IOD Connector (P5)   |   IOD Connector (P5) |
|----------------------|----------------------|----------------------|
|                   28 | TEST_OUT_1           |                   28 |
|                   27 | TEST_OUT_0           |                   27 |
|                   24 | SS_IN_CH3            |                   24 |
|                   23 | SS_IN_CH2            |                   23 |
|                   22 | SS_OUT_CH1           |                   22 |
|                   21 | SS_OUT_CH0           |                   21 |
|                   20 | SS_IN_CH1            |                   20 |
|                   19 | SS_IN_CH0            |                   19 |

Figure 15 - Cascading Safe Stop Non-OSSD Device Wiring Example

<!-- image -->

|   IOD Connector (P5) | IOD Connector (P5)   |   IOD Connector (P5) |
|----------------------|----------------------|----------------------|
|                   28 | TEST_OUT_1           |                   28 |
|                   27 | TEST_OUT_0           |                   27 |
|                   24 | SS_IN_CH3            |                   24 |
|                   23 | SS_IN_CH2            |                   23 |
|                   22 | SS_OUT_CH1           |                   22 |
|                   21 | SS_OUT_CH0           |                   21 |
|                   20 | SS_IN_CH1            |                   20 |
|                   19 | SS_IN_CH0            |                   19 |

Figure 16 - Cascading Safe Stop OSSD Device Wiring Example

<!-- image -->

|   IOD Connector (P5) | IOD Connector (P5)   |   IOD Connector (P5) |
|----------------------|----------------------|----------------------|
|                   28 | TEST_OUT_1           |                   28 |
|                   27 | TEST_OUT_0           |                   27 |
|                   24 | SS_IN_CH3            |                   24 |
|                   23 | SS_IN_CH2            |                   23 |
|                   22 | SS_OUT_CH1           |                   22 |
|                   21 | SS_OUT_CH0           |                   21 |
|                   20 | SS_IN_CH1            |                   20 |
|                   19 | SS_IN_CH0            |                   19 |

IMPORTANT

|   IOD Connector (P5) | IOD Connector (P5)   |   IOD Connector (P5) |
|----------------------|----------------------|----------------------|
|                   28 | TEST_OUT_1           |                   28 |
|                   27 | TEST_OUT_0           |                   27 |
|                   24 | SS_IN_CH3            |                   24 |
|                   23 | SS_IN_CH2            |                   23 |
|                   22 | SS_OUT_CH1           |                   22 |
|                   21 | SS_OUT_CH0           |                   21 |
|                   20 | SS_IN_CH1            |                   20 |
|                   19 | SS_IN_CH0            |                   19 |

For simplicity, the cables are shown connecting end-to-end with the output cable exiting right. However, all connectors are keyed to exit left as shown in Figure 17 .

In this example, three safe torque-off drives are shown using the Bulletin 2090 low-profile connector kit and cables. The right-angled cable connectors are keyed to exit left as shown. Cables loop back and cascade to the next drive or other cascading device.

Figure 17 - Kinetix 6200/6500 Cascading Safe Torque-off Cable Example

<!-- image -->

Table 5 - Safe Torque-off Cable Catalog Numbers

| Cable Cat. No. Length Description   |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
|                                     | 2090-CS0DSDS-AA02 0.2 m (7.1 in.) Drive-to-drive connections (single-wide IAM or AM power module) |
|                                     | 2090-CS0DSDS-AA03 0.3 m (1.0 ft) Drive-to-drive connections (double-wide IAM or AM power module)  |
|                                     | 2090-CS0DSDS-AA10 1.0 m (3.2 ft) Connect to next 2094 power rail or other safe torque-off device  |

Figure 18 - 2090-CS0DSDS-AAxx Cable Pinout

<!-- image -->

Table 6 - 2090-CS0DSDS-AAxx Cable Terminations

| Cable Termination   | Cable Termination   | 2090-K6CK-D44S0 Pin Description   |
|---------------------|---------------------|-----------------------------------|
|                     | Pins Sockets        |                                   |
|                     | 4 18                | Safety 24V common SCOM            |
|                     | 1 21                | Safe stop output 0 SS_OUT_CH0     |
|                     | 3 22                | Safe stop output 1 SS_OUT_CH1     |
| 4                   | 18                  | Safety 24V common SCOM            |
| 1                   | 23                  | Safe stop input 2 SS_IN_CH2       |
| 3                   | 24                  | Safe stop input 3 SS_IN_CH3       |

## Notes:

## Introduction

## Nonrecoverable Faults

## Fault Recovery

<!-- image -->

## Troubleshooting the Safe Torque-off Drive

This chapter provides troubleshooting tables for diagnosing fault conditions associated with the safe torque-off safety functions.

| Topic                        |   Page |
|------------------------------|--------|
| Nonrecoverable Faults        |     33 |
| Fault Recovery               |     33 |
| Input and Output Faults      |     34 |
| Fault Codes and Descriptions |     34 |
| Status Attributes            |     35 |

In addition to the recoverable faults described in this chapter, the drive also generates nonrecoverable faults when a problem with the drive hardware is detected. These faults are Safe State faults. If a Safe State fault occurs, all safety control outputs are set to their safe state.

To clear a nonrecoverable fault, cycle power. If the nonrecoverable fault persists, the drive may need to be replaced.

If the fault is no longer present, you can clear the fault condition with a successful SO Reset and a Motion Axis Fault Reset (MAFR) via your RSLogix 5000 application program, except in the case of an Internal Hdwr fault or MP Out fault. An Internal Hdwr fault or MP Out fault is cleared at power down.

## Input and Output Faults

## Fault Codes and Descriptions

An input or output fault indication can be caused by several wiring fault conditions during commissioning or normal operation. If an input fault occurs, check for the following:

- One of the channels may have shorted to a 24V DC source.
- One of the channels may have shorted to a GND source.
- Two input channels have shorted together.
- One or both output channels have an overcurrent condition.

An input fault will also occur if only one of the channels in a dual-channel system has changed state after a 1-second discrepancy time interval.

The drive web page can display a fault history queue, which provides a record of the faults detected by the drive. The fault history queue stores the fault codes and timestamps for the last 10 faults that occurred.

Refer to the Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002, for more information on accessing the drive web page.

Table 6 - Safe Torque-off Fault Codes

| Code  Display Text                  | Description                                                                                                                             | Description                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| SAFE FLT 01... INTERNAL HDWR nn (1) | A nonrecoverable microprocessor error has occurred.                                                                                     | A nonrecoverable microprocessor error has occurred.                                                                                     |
| SAFE FLT 03... MP OUT nn (1)        | An MP Output fault occurs if an internal error is detected in the circuit that removes motion producing power from the drive terminals. | An MP Output fault occurs if an internal error is detected in the circuit that removes motion producing power from the drive terminals. |
| SAFE FLT 09... SS IN nn (1)         | I/O Faults (2)                                                                                                                          | An SS_In fault occurs if an error is detected in one of the SS_In dual-channel inputs.                                                  |
| SAFE FLT 10... SS OUT nn (1)        | I/O Faults (2)                                                                                                                          | An SS_Out fault occurs if an error is detected in the SS_Out dual-channel output.                                                       |

## Status Attributes

For diagnostic purposes only, you can view status attributes by accessing the AxisServoDrive.GuardStatus tag (Kinetix 6200 systems) and AxisCIPDrive.GuardStatus tag (Kinetix 6500 systems) in RSLogix 5000 software.

| IMPORTANT   | AxisServoDrive.GuardStatus tags must be selected as a Real-time attribute in order to receive updated attribute values. This is not required for AxisCIPDrive.GuardStatus tags.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Guard Status Attributes

These attributes are stored in the AxisServoDrive.GuardStatus tag (Kinetix 6200 systems) and AxisCIPDrive.GuardStatus tag (Kinetix 6500 systems). Each bit corresponds to a different attribute.

Table 7 - Guard Status Descriptions

| Bit  Display Text Axis 1.     | Description                                                                                                                                                                                                                                           |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 GuardOKStatus               | This bit indicates when there are no faults. It is set (1), when all of the Fault Status bits 1…31 are 0 (no faults). The bit is 0 if any Fault Status bit from 1…31 indicates a fault (1).                                                           |
| 1 RESERVED Reserved.          |                                                                                                                                                                                                                                                       |
| 2  GuardGateDrive OutputSatus | This bit shows the status of the drive’s Motion Power command to the drive. A 1 indicates Motion Power is enabled; a 0 indicates Motion Power is disabled.                                                                                            |
| 3  GuardStopInput Status      | This bit displays the logical value, 1 or 0, evaluated for the dual-channel SS_In input.                                                                                                                                                              |
| 4  GuardStop RequestStatus    | This bit is set to 1 when a safe stop is initiated by either a transition of the SS_In input from ON to OFF or by a Stop Category fault. This bit is reset to 0 when a successful SO Reset occurs and when the Operation mode is set to Disabled (0). |
| 5 RESERVED                    | Reserved.                                                                                                                                                                                                                                             |
| 6 RESERVED                    | Reserved.                                                                                                                                                                                                                                             |
| 7 RESERVED                    | Reserved.                                                                                                                                                                                                                                             |
| 8  GuardStop OutputStatus     | This bit is set to 1 if the dual-channel SS_Out output is being commanded to the ON state. This bit is the commanded value, not a readback value. This bit is set to 0 if the SS_Out output is being commanded to the OFF state.                      |
| 9…22 RESERVED                 | Reserved.                                                                                                                                                                                                                                             |
|                               | 23 GuardResetInputStatus This status bit reflects the state of the Reset_In input. A 1 indicates the Reset_In input is ON; a 0 indicates the Reset_In input is OFF.                                                                                   |
|                               | 24 GuardResetRequiredStatus This bit is set to 1 if an SO Reset is required before Motion Power can be enabled.                                                                                                                                       |
| 25…31 RESERVED                | Reserved.                                                                                                                                                                                                                                             |

Table 8 - Guard Status Bit Values

| Parameter Name Description Bit Values   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Axis 1: Guard Status                    | GuardOKStatus GuardConfigLockedStatus GuardGateDriveOutputSatus GuardStopInputStatus GuardStopRequestStatus GuardStopInProgressStatus GuardStopDecelStatus GuardStopStandstillStatus GuardStopOutputStatus GuardLimitedSpeedInputStatus GuardLimitedSpeedRequestStatus GuardLimitedSpeedMonitorInProgressStatus GuardLimitedSpeedOutputStatus GuardMaxSpeedMonitorInProgressStatus GuardMaxAccelMonitorInProgressStatus GuardDirectionMonitorInProgressStatus GuardDoorControlLockStatus GuardDoorControlOutputStatus GuardDoorMonitorInputStatus GuardDoorMonitorInProgressStatus GuardLockMonitorInputStatus GuardEnablingSwitchInputStatus GuardEnablingSwitchInProgressStatus GuardResetInputStatus GuardResetRequiredStatus GuardStopInputCycleRequiredStatus | 0 = Fault; 1 = OK Reserved 0 = Off; 1 = On 0 = Off; 1 = On 0 = Inactive; 1 = Active Reserved Reserved Reserved 0 = Off; 1 = On Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved Reserved 0 = Off; 1 = On 0 = Off; 1 = On Reserved |

## Guard Fault Attributes

| Parameter Name Description Bit Values   |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Axis 1: Guard Faults Bit-encoded faults | 1 = GuardInternalFault 2 = Reserved 3 = GuardGateDriveFault 4 = Reserved 5 = Reserved 6 = Reserved 7 = Reserved 8 = Reserved 9 = GuardStopInputFault 10 = GuardStopOutputFault 11 = Reserved 12 = Reserved 13 = Reserved 14 = Reserved 15 = Reserved 16 = Reserved 17 = Reserved 18 = Reserved 19 = Reserved 20 = Reserved 21 = Reserved 22 = Reserved 23 = Reserved 24 = Reserved 25 = Reserved 26 = Reserved 27 = Reserved 28 = Reserved |

## Introduction

## General Specifications

## Specifications

This appendix provides product specifications for the safe torque-off safety functions.

| Topic                  |   Page |
|------------------------|--------|
| General Specifications |     37 |
| Certifications         |     38 |

These specifications apply to the safe torque-off safety functions.

| Attribute                          | Value                                                                 |
|------------------------------------|-----------------------------------------------------------------------|
| Standards                          | IEC/EN60204-1, ISO12100, IEC 61508, IEC 61800-5-2                     |
| Safety category                    | Cat. 4 and PLe per EN ISO 13849-1; SIL CL3 per IEC 61508 and EN 62061 |
| Power supply Voltage Current, max  | 21.6…28.8V DC (24V nom), 0.9…1.2 x rated voltage PELV or SELV 0.105 A |
| Power consumption 3 W              |                                                                       |
| SS outputs                         | 24V DC, 20 mA, short-circuit protected                                |
| Pulse outputs                      | 24V DC, 30 mA, short-circuit protected                                |
| SS inputs, max                     | 5 mA per input                                                        |
| Input pulse rejection, max 700 μs  |                                                                       |
| Input ON voltage, min 16.5V        |                                                                       |
| Input OFF voltage, max 5V          |                                                                       |
| Input OFF current, max 2 mA        |                                                                       |
| Safety reaction time, max  (1)     | 12 ms                                                                 |
| Reset_In Input, max 5 mA per input |                                                                       |
| Reset time, max  (2)               | 20 ms                                                                 |
| Conductor size (3)                 | 0.25…0.75 mm 2 (24…18 AWG)                                            |
|                                    | Strip length 5 mm (0.25 in.)                                          |
|                                    | Terminal screw torque 0.22…0.25 N•m (1.9…2.2 lb•in)                   |

<!-- image -->

## Certifications

See the Product Certification link at http://www.ab.com for Declarations of Conformity, Certificates, and other certifications details.

| Agency gy Certification (1)             | Value                                                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us (2) | UL Listed, certified for US and Canada.                                                                                                                                                                                                                                                                                         |
|             | CE European Union 2004/108/EC EMC Directive, compliant with: •  EN 61800-3; categories C2 and C3 •  EN 62061; EM Immunity                                                                                                                                                                                                       |
|             | C-Tick Australian Radiocommunications Act, compliant with: EN 61800-3; categories C2 and C3                                                                                                                                                                                                                                     |
|             | Functional Safety TÜV Certified for Functional Safety: up to SIL CL3, according to EN 61800-5-2, EN 61508, and EN 62061; up to Performance Level PLe and Category 4, according to EN ISO 13849-1; when used as described in this Kinetix 6200 and Kinetix 6500 Safe Torque-off Safety Reference Manual, publication 2094-RM002. |

(1) When product is marked, refer to http://www.ab.com for Declarations of Conformity Certificates.

(2) Underwriters Laboratories Inc. has not evaluated the safe-off, safe torque-off, or safe speed-monitoring options in these products.

## Numerics

2090-K6CK-D44M 14

2090-K6CK-D44S0 16

## A

additional resources 8

ADR 12

automatic drive replacement 12

automatic reset 23 , 25

## C

cascaded configurations 27 cascaded connections 24

Cat 4 7 , 9

performance definition certification 38

Cat 4 7 , 9

ISO 13849-1 9

PLe 7 , 9

SIL CL3 7 , 9

connector kit wiring 14 , 16

cycle inputs 20

## D

discrepancy time 20

documentation additional resources 8

drive replacement 12

## E

emergency shutdown systems 9

EN 61508 11

SIL CL3 certification 9

EN 61508-5-2 38

EN 61800-5-2

SIL CL3 certification 9

EN 62061 11

European Norm definition 7

## F

## failure

contact information 12

## fault codes

input 34 nonrecoverable 33 output 34 recovery 33 Stop Category Faults fault history queue 34

fault recovery 33

34

10

PFH

## G

guard faults 36

guard status 36

## I

input faults 34

inputs 19

ISO 13849-1 9 , 10 , 11 , 38

## M

motion-allowed plug 17

multi-axis configurations 27 wiring 24

## O

output faults 34

outputs 23

## P

PFD

data 11

definition 7 , 11

data 11

definition 7 , 11

pinouts 18

PL 11

definition 7

PLe 7 , 9 , 38

power supply 14

pulse test outputs 19

## R

reaction time 12

recover from fault 33

reset behavior 21

Reset input wiring

Reset\_In input 23

risk assessment 13

## S

## Safe State

definition 12

safety certification, TÜV Rheinland 9 , 38

information 13

power supply 14

reaction time 12

shutdown, EDS 9

## SIL CL3 7 , 9 , 38

certification, user responsibilities 10

single-channel operation 19

SO Reset 25

specifications general 37

SS\_Out output 23

status attributes 35

stop category definition 10

## T

## terminal screws

connections 18

strip length 18

torque 18

## timing diagrams

discrepancy time 20

reset behavior 21

## W

## wiring

connector kit 2090-K6CK-D44M 14 2090-K6CK-D44S0 16 motion-allowed plug 17

multi-axis connections 24

safety input examples 22

## wiring example

Safe Stop mode 26 , 28

## Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products. At http://www.rockwellautomation.com/support, you can find technical manuals, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools. You can also visit our Knowledgebase at http://www.rockwellautomation.com/knowledgebase for FAQs, technical information, support chat and forums, software updates, and to sign up for product notification updates.

For an additional level of technical phone support for installation, configuration, and troubleshooting, we offer TechConnectSM support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation.com/support/ .

## Installation Assistance

If you experience a problem within the first 24 hours of installation, review the information that is contained in this manual. You can contact Customer Support for initial help in getting your product up and running.

| United States or Canada 1.440.646.3434                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States or Canada Use the Worldwide Locator at http://www.rockwellautomation.com/support/americas/phone_en.html, or contact your local Rockwell Automation representative. |

## New Product Satisfaction Return

Rockwell Automation tests all of its products to ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

| United States Contact your distributor. You must provide a Customer Support case number (call the phone number above to obtain one) to your distributor to complete the return process.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States Please contact your local Rockwell Automation representative for the return procedure.                                                                              |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/ .