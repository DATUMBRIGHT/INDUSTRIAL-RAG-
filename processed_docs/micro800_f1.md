<!-- image -->

## Micro800 Expansion I/O Modules

Catalog Numbers 2085-IQ16, 2085-IQ32T, 2085-OV16, 2085-OB16, 2085-IA8, 2085-IM8, 2085-OA8, 2085-OW8, 2085-OW16, 2085-IF4, 2085-IF8, 2085-OF4, 2085-IRT4, 2085-EP24VDC

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

Preface

## Table of Contents

|                               | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|                               | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5                            |
|                               | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5          |
|                               | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5        |
|                               | Chapter 1                                                                                                                                   |
| Hardware Features             | Micro800 Expansion I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7                  |
|                               | Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8       |
|                               | Chapter 2                                                                                                                                   |
| Discrete and Analog Expansion | Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 |
| I/O Features                  | Discrete Expansion I/O Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                  |
|                               | Discrete Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11           |
|                               | Discrete Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11            |
|                               | Analog Expansion I/O Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                |
|                               | Analog Input and Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                   |
|                               | Analog Data Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                  |
|                               | Valid Range of the Data Formats for 2085-IF4, 2085-IF8,                                                                                     |
|                               | and 2085-OF4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13             |
|                               | Convert Analog Value to Data Format Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13                                  |
|                               | Channel Status Indicator Information for 2085-IF4 and 2085-IF8 . . . . . . . . . . . . . 15                                                 |
|                               | Specialty Module 2085-IRT4 Temperature Input Module . . . . . . . . . . . . . . . . . . . . . . . . . 15                                    |
|                               | Sensor Type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15          |
|                               | Data Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16           |
|                               | Valid Range of the Data Formats for 2085-IRT4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                                    |
|                               | Convert Analog Value to Data Format Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                                  |
|                               | Chapter 3                                                                                                                                   |
| Wiring Connections            | Input/Output Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19        |
|                               | Wiring the 2085-IQ32T Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24                        |
|                               | Expansion I/O Power Supply Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26                    |
|                               | Chapter 4                                                                                                                                   |
| Configure Your Expansion I/O  | Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 |
| Module                        | Add an Expansion I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27         |
|                               | Edit Expansion I/O Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30                 |
|                               | Delete and Replace an Expansion I/O Configuration . . . . . . . . . . . . . . . . . . . . . . . . 36                                        |
|                               | Build, Save, Download a Project with Expansion I/O Configuration . . . . . . . . . . . . . . . . 38                                         |

## Expansion I/O Data Mapping

| Appendix A                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Discrete I/O Data Mapping. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                 |
| Analog I/O Data Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                |
| Specialty I/O Data Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42                         |
| Calibration of Analog Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43                   |
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . . 45 |

## About This Publication

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

## Additional Resources

|                                                                                                                                    | Resource Description                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Micro800 Programmable Controller Family Selection Guide, publication 2080-SG001                                                    | Provides information to help you select the Micro800 controller, plug-ins, expansion I/O, and accessories, based on your requirements.                                                                                                                              |
| Micro800 Programmable Controllers Technical Data, publication 2080-TD001                                                           | Provides detailed specifications for Micro800 controllers, expansion I/O modules, plug-in modules, and accessories.                                                                                                                                                 |
| Micro830, Micro850, and Micro870 Programmable Controllers User Manual, publication 2080-UM002                                      | Describes how to install, configure, use, and troubleshoot your Micro830®, Micro850®, and Micro870® controllers.                                                                                                                                                    |
| Micro800 16-point and 32-point 12/24V Sink/Source Input Modules Installation Instructions, publication 2085-IN001                  | Provides information on mounting and wiring the expansion I/O modules (2085-IQ16, 2085-IQ32T).                                                                                                                                                                      |
| Micro800 Bus Terminator Module Installation Instructions, publication 2085-IN002                                                   | Provides information on mounting and wiring the expansion I/O bus terminator (2085-ECR).                                                                                                                                                                            |
| Micro800 16-point Sink and 16-point Source 12/24V DC Output Modules Installation Instructions, publication 2085-IN003              | Provides information on mounting and wiring the expansion I/O modules (2085-OV16, 2085-OB16).                                                                                                                                                                       |
| Micro800 8-point and 16-point AC/DC Relay Output Modules Installation Instructions, publication 2085-IN004                         | Provides information on mounting and wiring the expansion I/O modules (2085-OW8, 2085-OW16).                                                                                                                                                                        |
| Micro800 8-point Input and 8-point Output AC Modules Installation Instructions, publication 2085-IN005                             | Provides information on mounting and wiring the expansion I/O modules (2085-IA8, 2085-IM8, 2085-OA8).                                                                                                                                                               |
| Micro800 4-channel and 8-channel Analog Voltage/Current Input and Output Modules Installation Instructions, publication 2085-IN006 | Provides information on mounting and wiring the expansion I/O modules (2085-IF4, 2085-IF8, 2085-OF4).                                                                                                                                                               |
| Micro800 4-channel Thermocouple/RTD Input Module Installation Instructions, publication 2085-IN007                                 | Provides information on mounting and wiring the expansion I/O module (2085-IRT4).                                                                                                                                                                                   |
| Micro870 Programmable Controllers 24V DC Expansion Power Supply Installation Instructions, publication 2085-IN008                  | Provides information on mounting and wiring the 24V DC expansion power supply (2085-EP24VDC).                                                                                                                                                                       |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1                   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state |

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use Micro800™ controllers.

This manual is a reference guide for Micro800 expansion I/O modules. It describes the procedures you use to install, wire, and troubleshoot your expansion I/O. This manual:

- Gives you an overview of expansion I/O features and configuration parameter
- Gives you an overview of the Micro800 controller system

You should have a basic understanding of electrical circuitry and familiarity with relay logic. If you do not, obtain the proper training before using this product.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                           | Page   |
|-------------------------------------------------|--------|
| Updated section Wiring the 2085-IQ32T Module 24 |        |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

components.

## Additional Resources (Continued)

|                                                                             | Resource Description                                                                                             |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 | Provides general guidelines for installing a Rockwell Automation industrial system.                              |
| Product Selection and Configuration website, rok.auto/systemtools           | Helps configure complete, valid catalog numbers and build complete quotes based on detailed product information. |
| Product Certifications website, rok.auto/certifications                     | Provides declarations of conformity, certificates, and other certification details.                              |

## Micro800 Expansion I/O Modules

## Hardware Features

<!-- image -->

Micro800 controllers support a range of expansion I/O modules to extend the functionality of the controller.

The different types of expansion I/O modules are listed in Table 1 .

Table 1 - Micro800 Expansion I/O Modules

|                           | Catalog Type Description                                        |
|---------------------------|-----------------------------------------------------------------|
|                           | 2085-IA8 Discrete 8-point, 120V AC input                        |
|                           | 2085-IM8 Discrete 8-point, 240V AC input                        |
|                           | 2085-OA8 Discrete 8-point, 120/240V AC Triac Output             |
|                           | 2085-IQ16 Discrete 16-point, 12/24V Sink/Source Input           |
|                           | 2085-IQ32T Discrete 32-point, 12/24V Sink/Source Input          |
|                           | 2085-OV16 Discrete 16-point, 12/24V DC Sink Transistor Output   |
|                           | 2085-OB16 Discrete 16-point, 12/24V DC Source Transistor Output |
|                           | 2085-OW8 Discrete 8-point, AC/DC Relay Output                   |
|                           | 2085-OW16 Discrete 16-point, AC/DC Relay Output                 |
| 2085-IF4 Analog           | 4-channel, 14-bit isolated(1) voltage/current input             |
| 2085-IF8 Analog           | 8-channel, 14-bit isolated(1) voltage/current input             |
| 2085-OF4 Analog           | 4-channel, 12-bit isolated(1) voltage/current output            |
| 2085-IRT4 Analog          | 4-channel, 16-bit isolated(1) RTD and Thermocouple input module |
| 2085-EP24VDC Power supply | Supplies power for up to four expansion I/O modules(2)          |
|                           | 2085-ECR Terminator 2085 bus terminator                         |

(1) Refers to isolation from field side wiring to controller, not channel-to-channel isolation.

(2) Use only in a Micro870 system with more than four expansion I/O modules.

The bus terminator, 2085-ECR, serves as an end cap and terminates the end of the Serial communication bus. It is required whenever an expansion I/O module is connected to the controller and should be connected to the last expansion I/O module in the system.

<!-- image -->

## Hardware Features

Micro800 expansion I/O modules come as a single-width (90 x 28 x 87 mm, HxWxD) or doublewidth (90 x 46 x 87 mm, HxWxD) form factor. See the Micro800 Programmable Controllers Technical Data, publication 2080-TD001 for information on module dimensions and specifications.

Figure 1 - Single-width Expansion I/O

## 2085-OW8 shown

Figure 2 - Double-width Expansion I/O

<!-- image -->

## 2085-OW16 shown

<!-- image -->

Table 2 - Module Description

| Description Description                                           |                                        |
|-------------------------------------------------------------------|----------------------------------------|
| 1 Mounting screw hole/mounting foot 6 Bus connector (male/female) |                                        |
| Removable Terminal Block (RTB)(1)                                 | 2  7 Latch hooks                       |
| 3 RTB hold down screws 8 I/O status LED                           |                                        |
|                                                                   | 4 Cable grip 9 DIN rail mounting latch |
| 5 Module interconnect latch                                       |                                        |

Figure 3 - 2085-IQ32T Hardware Features

<!-- image -->

Table 3 - 2085-IQ32T Hardware Components

| Description Description                                           |                                        |
|-------------------------------------------------------------------|----------------------------------------|
| 1 Mounting screw hole/mounting foot 6 Bus connector (male/female) |                                        |
|                                                                   | 2 Connector 7 Latch hooks              |
| 3 Connector retaining arm 8 I/O status LEDs                       |                                        |
|                                                                   | 4 Cable grip 9 DIN rail mounting latch |
| 5 Module interconnecting latch                                    |                                        |

Figure 4 - 2085-EP24VDC Hardware Features

<!-- image -->

Table 4 - 2085-EP24VDC Hardware Components

|                                                                   | Description Description                |
|-------------------------------------------------------------------|----------------------------------------|
| 1 Mounting screw hole/mounting foot 6 Bus connector (male/female) |                                        |
| 2 Removable Terminal Block (RTB) 7 Latch hooks                    |                                        |
| 3 RTB hold down screws 8 Power status LED                         |                                        |
|                                                                   | 4 Cable grip 9 DIN rail mounting latch |
| 5 Module interconnecting latch                                    |                                        |

## Notes:

## Overview

## Discrete Expansion I/O Features

<!-- image -->

## Discrete and Analog Expansion I/O Features

This section includes a brief description of the different features and configuration parameters for the analog and discrete Micro800 expansion I/O modules.

Micro800 discrete expansion I/O modules are input/output modules that provide On/Off detection and actuation.

## Module Information

The Connected Components Workbench™ programming software makes it easy to configure the modules as most module features can be enabled or disabled through the device configuration portion of the software. You can also use the software to check any expansion I/O module in the system to retrieve:

- Hardware revision information
- Vendor ID
- Module information

Channel Status Indicator Information

The discrete expansion I/O modules have yellow status indicators for each input/output point which indicates the On/Off state of the point.

## Discrete Input

Discrete input modules interface to sensing devices and detect whether they are On or Off. These modules convert AC or DC On/Off signals from user devices to appropriate logic level for use within the processor.

The 2085-IA8, 2085-IM8, 2085-IQ16, and 2085-IQ32T modules update the controller with new data whenever an input point transitions from On to Off and Off to On.

On to Off and Off to On filter times can be adjusted through the Connected Components Workbench software. These filters improve noise immunity within a signal. A larger filter value affects the length of delay times for signals from these modules.

You can select from a series of operational ranges for each channel. The range designates the minimum and maximum signals that are detectable by the module.

## Discrete Output

Output modules may be used to drive a variety of output devices. Typical output devices compatible with the outputs include:

- Motor starters
- Solenoids
- Indicators

Follow these guidelines when designing a system.

- Make sure that the outputs can supply the necessary surge and continuous current for proper operation. See the Micro800 Programmable Controllers Technical Data, publication 2080-TD001 for more information.

## Analog Expansion I/O Features

- Make sure that the surge and continuous current are not exceeded. Damage to the module could result. When sizing output loads, check the documentation that is supplied with the output device for the surge and continuous current needed to operate the device. The Micro800 standard digital outputs are capable of directly driving the Micro800 standard digital inputs.

<!-- image -->

User-configurable options are not available in Connected Components Workbench software for discrete output modules.

## IMPORTANT

On controller minor and major fault, all output channels are de-energized.

This section pertains to the following Micro800 analog expansion I/O modules.

Table 5 - Micro800 Expansion I/O Modules

|                  | Catalog Type Description                                        |
|------------------|-----------------------------------------------------------------|
| 2085-IF4 Analog  | 4-channel, 14-bit isolated(1) voltage/current input             |
| 2085-IF8 Analog  | 8-channel, 14-bit isolated(1) voltage/current input             |
| 2085-OF4 Analog  | 4-channel, 12-bit isolated(1) voltage/current output            |
| 2085-IRT4 Analog | 4-channel, 16-bit isolated(1) RTD and Thermocouple input module |

Analog expansion I/O modules are interface modules that convert analog signals to digital values for inputs and convert digital values to analog signals for outputs. Controllers can then use these signals for control purposes.

## Analog Input and Output

Input/Output Types and Ranges

The 2085-IF4 and 2085-IF8 modules support four and eight input channels, respectively, while the 2085-OF4 supports four output channels. Each of the channels can be configured as current or voltage input/output, with current mode as default configuration.

Table 6 - Input/Output Type/Range for 2085-IF4, 2085-IF8, and 2085-OF4

|          | Module Input/Output Type/Range   |
|----------|----------------------------------|
|          | 2085-IF4 0…20 mA                 |
| 2085-IF8 | 4…20 mA (default) -10…10 V       |
| 2085-OF4 | 0…10 V                           |

To use an input or output as a current or voltage device, you must:

- Wire the input/output connector for the correct input/output type (see Input/Output Wiring on page 19)
- Configure the input/output as current or voltage through Connected Components Workbench software (see Configure Your Expansion I/O Module on page 27)

## Analog Data Formats

This parameter configures each channel to present analog data in any of the following formats:

- Raw/Proportional Data – The value presented to the controller is proportional to the selected input and scaled into the maximum data range allowed by the bit resolution of the A/D converter.

For example, the data value range for a ±10V DC user input is -32,768…+32,767, which covers the full-scale range of -10.5…+10.5V. See Valid Range of the Data Formats for 2085-IF4, 2085-IF8, and 2085-OF4 on page 13 .

- Engineering Units – The module scales the analog input data to the actual current or voltage values for the selected input range. The resolution of the engineering units is 0.001V or 0.001 mA per count.
- Percent Range – The input data is presented as a percentage of the normal operating range.

For example, 0…10V DC equals 0…100%. The amount over and under the normal operating range (the full-scale range) is also supported.

## Valid Range of the Data Formats for 2085-IF4, 2085-IF8, and 2085-OF4

The valid range of each Data Format corresponds to the full range of each Type/Range (or normal range). For example, the full range of 0…20 mA is 0…21 mA.

Table 7 - Valid Range of the 2085-IF4 and 2085-IF8 Data Formats

|                           | Type/Range    | Type/Range                                    | Type/Range    | Type/Range    |
|---------------------------|---------------|-----------------------------------------------|---------------|---------------|
| Data Format               | 0…20 mA(1)    | 4…20 mA(4)  -10…10V(4)  0…10V(4)              |               |               |
| Raw/Proportional Data (2) | -32768…+32767 | -32768…+32767                                 | -32768…+32767 | -32768…+32767 |
| Engineering Units (3)     |               | 0…21000 3200…21000 -10500…+10500 -500…+10500  |               |               |
| Percent Range (4)         |               | 0…10500 -500…+10625 Not supported -500…+10500 |               |               |

Table 8 - Valid Range of the 2085-OF4 Data Formats

|                           | Type/Range    | Type/Range                                | Type/Range    | Type/Range    |
|---------------------------|---------------|-------------------------------------------|---------------|---------------|
| Data Format               | 0…20 mA(1)    | 4…20 mA(4)  -10…10V(4)  0…10V(4)          |               |               |
| Raw/Proportional Data (2) | -32768…+32767 | -32768…+32767                             | -32768…+32767 | -32768…+32767 |
| Engineering Units (3)     |               | 0…21000 3200…21000 -10500…+10500 0…10500  |               |               |
| Percent Range (4)         |               | 0…10500 -500…+10625 Not supported 0…10500 |               |               |

## Convert Analog Value to Data Format Value

The formula for converting an analog value x to a data format value y (or conversely, deriving data format value y to analog value x) is as follows:

Y = ((X - Minimum Value of X Range) * (Range of Y)/(Range of X)) + (Minimum Value of Y Range)

```
Example 1: Find the analog value (Y) of type/range 4…20 mA when the Raw/Proportional Data X is -20000. Given: X = -20000 Minimum value of X Range = -32768 Range of X = 32767 - (-32768) = 65535 Range of Y = 21 - 3.2 = 17.8 Minimum value of Y Range = 3.2
```

```
Using the conversion formula: Y = (-20000 - (-32768)) * 17.8/65535 + (3.2) = 6.668 mA Example 2: Find the Raw/Proportional value (Y) of 10 mA (X) for type/range 4…20 mA. Given: X = 10 mA Minimum value of X Range = 3.2 mA (Minimum value of 4…20 mA) Range of X = 21 - 3.2 = 17.8 mA (Range of 4…20 mA) Range of Y = 32767 - (-32768) = 65535 (Range of Raw/Proportional Data) Minimum value of Y Range = -32768 (Minimum value of Raw/Proportional Data) Using the conversion formula:
```

Y = -7732.15 (Decimals are not displayed)

## Input Filter

For the input modules, 2085-IF4 and 2085-IF8, the input filter parameter lets you specify the frequency filter type for each channel. Frequency filter type affects noise rejection, as explained below. Select a frequency filter type considering acceptable noise and response time.

Through the Connected Components Workbench software, you can configure input filter as:

- 50/60Hz Rejection (default)
- No Filter
- 2-point Moving Average
- 4-point Moving Average
- 8-point Moving Average

## Noise Rejection

The input modules use a digital filter that provides noise rejection for the input signals.

The moving average filter reduces the high frequencies and random white noise while keeping an optimal step response. See the Micro800 Programmable Controllers Technical Data, publication 2080-TD001 for minimum and maximum response times.

Normal Mode Rejection is better than 40 dB, while Common Mode Rejection is better than 60 dB @ 50/60 Hz, with the 50/60 Hz rejection filters selected. The modules perform well in the presence of common mode noise as long as the signals applied to the user plus and minus input terminals do not exceed the common mode voltage rating (±10 V) of the modules. Improper earth ground may be a source of common mode noise.

## Process Level Alarms

Process level alarms alert you when the module has exceeded configured high and low limits for each channel (for input modules, it provides additional high-high and low-low alarms). When the channel input or output goes below a low alarm or above a high alarm, a bit is set in the status words. All Alarm Status bits can be read individually or read through the Channel Status Byte.

For the output module, 2085-OF4, it is possible to latch the alarm status bit when the latch configuration is enabled.

You can configure each channel alarm individually.

## Specialty Module 2085-IRT4 Temperature Input Module

## Clamping Limits and Alarm

For the output module, 2085-OF4, clamping limits the output from the analog module to remain within a range configured by the controller, even when the controller commands an output outside that range. This safety feature sets a high clamp and a low clamp. Once clamps are determined for a module, any data received from the controller that exceeds those clamps transitions the output to that limit but not beyond the clamp value. It also sets the alarm status bit when the alarm is enabled. It is also possible to latch the alarm status bit when the latch configuration is enabled.

For example, an application may set the high clamp on a module for 8V and the low clamp for -8V. If a controller sends a value corresponding to 9V to the module, the module only applies 8V to its screw terminals.

You can configure the clamp limit (high/low clamp), the associated alarm, and its latching configuration on a per channel basis.

The following table shows the default values of the High/Low Clamps (in the order of low clamp value followed by the high clamp value) for the respective type/range when they are first enabled. You can change these values (within their full range) according to your application.

Table 9 - Default Range of High Clamp/Low Clamp Values

| Data Format 0…20 mA 4…20 mA -10…+10V 0…10V                                        |                                                        |
|-----------------------------------------------------------------------------------|--------------------------------------------------------|
| Raw/Proportional Data -32768, +29647 -29822, +29086 -31207, +31207 -32768, +29647 |                                                        |
| Engineering Units 0, 20000 4000, 20000 -10000, +10000 0, 10000                    |                                                        |
|                                                                                   | Percent Range 0, 10000 0, 10000 Not supported 0, 10000 |

## Channel Status Indicator Information for 2085-IF4 and 2085-IF8

The 2085-IF4 and 2085-IF8 modules use red LEDs to indicate when certain operating conditions occur on the analog input channels. The behavior for the channel status indicators are described in the following table.

Table 10 - Channel Status Indicator Information for 2085-IF4 and 2085-IF8

| Operating Condition                                                                                                                                                  | Channel Status Indicator   | Status Data                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog input channel is disabled OFF                                                                                                                                 |                            | Analog input status values can be read from Global Variables IO_Xx_ST_yy. Where “x” represents the expansion slot number 1…4, and “yy” represents the status word number 00…02. |
| Analog input channel is enabled and: • No data error is present, or • Closed, or • Not underrange or overrange                                                       | OFF                        | Analog input status values can be read from Global Variables IO_Xx_ST_yy. Where “x” represents the expansion slot number 1…4, and “yy” represents the status word number 00…02. |
| Analog input channel is enabled and data error is present                                                                                                            | RED                        | Analog input status values can be read from Global Variables IO_Xx_ST_yy. Where “x” represents the expansion slot number 1…4, and “yy” represents the status word number 00…02. |
| Analog input channel is enabled and the connection is open                                                                                                           | RED                        | Analog input status values can be read from Global Variables IO_Xx_ST_yy. Where “x” represents the expansion slot number 1…4, and “yy” represents the status word number 00…02. |
| Analog input channel is enabled and either of the underrange or overrange alarms configured is triggered: • Low Alarm • Low Low Alarm • High Alarm • High High Alarm | RED                        | Analog input status values can be read from Global Variables IO_Xx_ST_yy. Where “x” represents the expansion slot number 1…4, and “yy” represents the status word number 00…02. |

The 2085-IRT4 module lets you configure a sensor type for each of four input channels that linearizes analog signal into a temperature value.

## Sensor Type

The following Thermocouple and RTD sensor types are supported by the 2085-IRT4 expansion I/O module.

Table 11 - Supported Thermocouple Types and mV Range

| Sensor Range Range                      |
|-----------------------------------------|
| B 300…1800 °C (572…3272 °F)             |
| C 0…2315 °C (32…4199 °F)                |
| E -270…+1000 °C (-454…+1832 °F)         |
| J -210…+1200 °C (-346…+2192 °F)         |
| K -270…+1372 °C (-454…+2502 °F)         |
| TXK/XK (L) -200…+800 °C (-328…+1472 °F) |
| N -270…+1300 °C (-454…+2372 °F)         |
| R -50…+1768 °C (-58…+3214 °F)           |
| S -50…+1768 °C (-58…+3214 °F)           |
| T -270…+400 °C (-454…+752 °F)           |
| mV 0…100 mV                             |

Table 12 - Supported RTD Types and Ohms Range

| Sensor Range Range                                     |
|--------------------------------------------------------|
| 100 Ω Pt α = 0.00385 Euro -200…+870 °C (-328…+1598 °F) |
| 200 Ω Pt α = 0.00385 Euro -200…+400 °C (-328…+752 °F)  |
| 100 Ω Pt α = 0.003916 U.S -200…+630 °C (-328…+1166 °F) |
| 200 Ω Pt α = 0.003916 U.S. -200…+400 °C (-328…+752 °F) |
| 100 Ω Nickel 618 -60…+250 °C (-76…+482 °F)             |
| 200 Ω Nickel 618 -60…+200 °C (-76…+392 °F)             |
| 120 Ω Nickel 672 -80…+260 °C (-112…+500 °F)            |
| 10 Ω Copper 427 -200…+260 °C (-328…+500 °F)            |
| Ohms 0…500 Ohms                                        |

## Data Format

You can configure the following data formats for channels 0…3 through the Connected Components Workbench software.

- Engineering Units x 1 – If you select engineering units x 1 as the data format for a Thermocouple and RTD input, the module scales input data to the actual temperature values for the selected Thermocouple/RTD type per Thermocouple/RTD standard. It
- Engineering Units x 10 – For a Thermocouple or RTD input, the module scales input data to the actual temperature values for the selected Thermocouple/RTD type per Thermocouple/RTD standard. With this format, the module expresses temperatures in
- Raw/Proportional Data Format – The value presented to the controller is proportional to the selected input and scaled into the maximum data range allowed by the bit resolution of the A/D converter.

For example, the full data value range for a thermocouple type B 300...1800 °C 
° pgpyp
(572…3272 °F) is mapped to -32768…+32767. See Convert Analog Value to Data Format Value on page 17 for the conversion method.

- Percent Range – The input data is presented as a percentage of the normal operating range.

For example, 0…100 mV equals 0…100% or 300…1800 °C (572…3272 °F) equals 0…100% for thermocouple type B sensor. See Convert Analog Value to Data Format Value on page 17 for the conversion method.

## Valid Range of the Data Formats for 2085-IRT4

The following table shows the valid range of the Data Format versus the Data Type/Range for channels 0…3.

Table 13 - Valid Range of the 2085-IRT4 Data Formats

| Data Format               | Sensor Type – Temperature (10 Thermocouples, 8 RTDs)   | Sensor Type 0…100 mV   | Sensor Type 0…500 ohms   |
|---------------------------|--------------------------------------------------------|------------------------|--------------------------|
| Raw/Proportional Data (1) | -32768…+32767                                          |                        |                          |
| Engineering Units x 1     | Temperature Value(2) (°C/°F)                           | 0…10000(3)             | 0…5000(4)                |
| Engineering Units x 10    | Temperature Value(5) (°C/°F)                           | 0…1000(6)              | 0…500(7)                 |
| Percent Range (8)         | 0…10000                                                |                        |                          |

## Convert Analog Value to Data Format Value

The formula for converting an analog value x to a data format value y, or converting data format value y to analog value x, is as follows:

Y = ((X - Minimum Value of X Range)*(Range of Y)/(Range of X)) + (Minimum Value of Y

```
Range) Example: Find the temperature value (Y) of thermocouple type K when the Raw/Proportional Data X is -20000. Given: X = -20000 (Raw/Proportional Value) Minimum value of X Range = -32768 (Minimum value of Raw/Proportional Data) Range of X = 32767 - (-32768) = 65535 (Range of Raw/Proportional Data)
° gg
Range of Y = 1372 - (-270) = 1642 (Range of Thermocouple K in °C)
° ggp
Minimum value of Y Range = -270 °C (Minimum value of Thermocouple K) Then: Y = (-20000 - (-32768)) * 1642/65535 + (-270 °C) = 49.9 °C
```

Temperature Units

Temperature value can be set to °C (default) or °F.

Open circuit response

This parameter defines the response to be taken by the module during an open circuit.

- Upscale – Sets input to full upper scale value of channel data word. The full-scale value is determined by the selected input type, data format, and scaling.
- Downscale – Sets input to full lower scale value of channel data word. The low scale value is determined by the selected input type, data format, and scaling.
- Hold Last State – Sets input to last input value.
- Zero – Sets input to 0 to force the channel data word to 0.

## Filter Frequency

The 2085-IRT4 module uses a digital filter that provides noise rejection for the input signals. The filter is set by default at 4 Hz. The digital filter provides -3 dB (50% amplitude) attenuation at a filter frequency of 4 Hz.

The -3 dB frequency is the filter cut-off frequency. The cut-off frequency is defined as the point on the frequency response curve where frequency components of the input signal are passed with 3 dB of attenuation. All input frequency components at or below the cut-off frequency are passed by the digital filter with less than 3 dB of attenuation. All frequency components above the cutoff frequency are increasingly attenuated.

The cut-off frequency for each channel is defined by its filter frequency selection and is equal to the filter frequency setting. Choose a filter frequency so that your fastest changing signal is below that of the filter's cut-off frequency. The cut-off frequency should not be confused with the update time. The cut-off frequency relates to how the digital filter attenuates frequency components of the input signal. The update time defines the rate at which an input channel is scanned and its channel data word is updated.

A lower filter frequency provides a better noise rejection, but it also increases the update time. Conversely, a higher filter frequency provides a faster update time, but it decreases the noise rejection and effective resolution.

<!-- image -->

For quickstart instructions on how to add, configure, delete and replace your expansion I/O module, see Configure Your Expansion I/O Module on page 27 .

## Input/Output Wiring

## Wiring Connections

In solid-state control systems, grounding and wire routing helps limit the effects of noise due to electromagnetic interference (EMI).

<!-- image -->

ATTENTION: Do not wire more than 2 conductors on any single terminal.

Basic wiring of devices to the expansion I/O modules are shown as follows.

Figure 5 - 2085-IA8 or 2085-IM8

<!-- image -->

<!-- image -->

Figure 6 - 2085-IQ16

<!-- image -->

Figure 7 - 2085-OA8

<!-- image -->

Figure 8 - 2085-IQ32T

<!-- image -->

See Wiring the 2085-IQ32T Module on page 24 .

## 2085-OB16

Terminal Block 1 Terminal Block 2

<!-- image -->

Figure 10 - 2085-OW8

<!-- image -->

Figure 9 - 2085-OB16 and 2085-OV16

## 2085-OV16

Terminal Block 1 Terminal Block 2

<!-- image -->

Figure 11 - 2085-OW16

<!-- image -->

Terminal Block 1 Terminal Block 2

Figure 12 - 2085-IF4

<!-- image -->

Figure 13 - 2085-IF8

<!-- image -->

Terminal Block 1 Terminal Block 2

Figure 14 - 2085-OF4

<!-- image -->

Figure 15 - 2085-IRT4

Terminal Block 1 Terminal Block 2

<!-- image -->

## Thermistor

<!-- image -->

<!-- image -->

ATTENTION: There is no channel-to-channel isolation for the 2085-IRT4 module. It is recommended to use a non-grounded thermocouple for better noise immunity.

<!-- image -->

## Wiring the 2085-IQ32T Module

Included with your 2085-IQ32T module is a keyed 40-pin female connector and crimp type pins. These components allow you to wire I/O devices to the module using a 40-conductor cable or individual wires.

<!-- image -->

ATTENTION: To comply with UL restrictions, this equipment must be powered from a source compliant with the following: Class 2 or Limited Voltage/Current.

When assembled, align the female connector over the module's male header using the keying slot as a guide. Firmly lock them together with the upper and lower retaining arms.

Figure 17 - Wire the Connector with Available 40-pin Connector

<!-- image -->

## Assemble the Wire Contacts

1. Strip the wire insulation to expose 4 mm (5/32 in.) of wire. Crimp pins can accept 0.14…0.34 mm 2 (26…22 AWG) wire.

<!-- image -->

ATTENTION: Be careful when stripping wires. Wire fragments that fall into the module could cause damage. Once wiring is complete, be sure the module is free of all metal fragments before removing the protective debris strip. Failure to remove the strip before operating can cause overheating.

2. Insert the wire into the crimp pin as far as the wire stop.
3. Crimp the wire barrel around the wire using small needle nose pliers.
4. Crimp the insulation barrel around the wire insulation using small needle nose pliers.
5. Solder wire and wire barrel together using lead-free solder and soldering pencil.
6. Insert the assembled wire contact into the terminal socket. Push the wire contact in until the tang latches. Make sure the tang is properly latched by lightly pulling on the wire.

<!-- image -->

<!-- image -->

<!-- image -->

## Expansion I/O Power Supply Wiring

One 5-pin removable terminal block (RTB) is included with your 2085-EP24VDC module. Use a single external power supply to power both the module and Micro800 controller.

<!-- image -->

<!-- image -->

ATTENTION: To comply with the CE Low Voltage Directive (LVD), this equipment must be powered from a source compliant with the following: Safety Extra Low Voltage (SELV) or Protected Extra Low Voltage (PELV).

## Overview

## Add an Expansion I/O

<!-- image -->

## Configure Your Expansion I/O Module

The following sample project guides you through the step-by-step process of adding, configuring, deleting, and replacing Micro800 expansion I/O modules in Connected Components Workbench software.

<!-- image -->

For more information about using the Connected Components Workbench software, you can refer to the Connected Components Workbench Online Help (it comes with your software).

In this sample project, you need to create a Connected Components Workbench project with a 2080-LC50-24QWB controller. Then, configure four expansion I/O devices (2085-IF4, 2085-IQ32T, 2085-OB16, 2085-IRT4) following the instructions below.

These instructions make use of the drag-and-drop mechanism available in Connected Components Workbench software, which allows the user to easily add, replace, and delete devices through simple drag-and-drop motion.

<!-- image -->

Expansion I/O modules are automatically added to a project when using the "Discover" feature in Connected Components Workbench software.

To add expansion I/O modules to an existing Micro800 controller project, do the following:

1. On the Project organizer pane, right-click Micro850 and choose Open.

<!-- image -->

The Micro850 project page opens in the center pane with a graphical replica of the Micro850 controller on the first tier, Controller properties on the second tier, and an Output box on the last tier.

<!-- image -->

2. On the Device Toolbox pane, found at the rightmost corner of the Connected Components Workbench window, go to the Expansion Modules folder.

<!-- image -->

3. Select and drag 2085-IQ32T to the right of the controller graphic at the center pane. Four blue slots appear to indicate available slots for expansion I/O modules. Drop 2085IQ32T on the first and rightmost slot against the controller.
4. From the Expansion Modules folder on the Device Toolbox pane, drag and drop 2085-IF4 on the second Expansion I/O slot, next to 2085-IQ32T.

<!-- image -->

<!-- image -->

<!-- image -->

To move an expansion I/O device to another slot, simply drag and drop the device to the preferred slot. For step-by-step instructions on how to delete and replace expansion I/O devices, see Delete and Replace an Expansion I/O Configuration on page 36 .

5. From the Expansion Modules folder on the Device Toolbox, drag and drop 2085-OB16 on the third Expansion I/O slot, next to 2085-IF4.
6. From the Expansion Modules folder on the Device Toolbox pane, drag and drop 2085-IRT4 on the fourth Expansion I/O slot, next to 2085-IRT4.

<!-- image -->

You can edit default configuration by following the procedure provided in the next section, Edit Expansion I/O Configuration on page 30 .

## Edit Expansion I/O Configuration

After you have added all four expansion I/O modules, your Connected Components Workbench project should look like this:

<!-- image -->

The Expansion Modules list should appear as shown below. To see device details for each of the expansion I/O you have just added, select General. To see default configuration properties, select Configuration, if available.

<!-- image -->

You can edit default I/O configuration through the Expansion Modules Details box located right below the controller graphic.

IMPORTANT To download configuration to your device, see Build, Save, Download a .

Project with Expansion I/O Configuration on page 38

1. Select the Expansion I/O device you want to configure.
2. Select Configuration. Edit module and channel properties according to your requirements and application.

<!-- image -->

The next sections show you configuration properties for each of the expansion I/O module.

## 2085-IA8 and 2085-IM8

These two AC input modules only have general device details available for the user in Connected Components Workbench software. No configuration properties are available.

<!-- image -->

<!-- image -->

2085-IF4 and 2085-IF8

<!-- image -->

For the analog input modules, 2085-IF4 and 2085-IF8, you can configure properties such as input range, format, filter and alarm limits for each individual channel.

Table 14 - Configuration Parameters for 2085-IF4 and 2085-IF8

| Configuration Property What to do Description   |                                                                                                                                                      |                                                                                                                                   |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Enable channel                                  | Select or deselect the checkbox. The box is selected by default.                                                                                     | Enable or disable a channel through this checkbox. By default, each channel is enabled.                                           |
| Minimum-maximum input range                     | Choose from a range of values: • 0…20 mA • 4…20 mA (default) • -10…+10 V • 0…10 V                                                                    | Defines the input mode for the channel as either voltage or current, with current as default mode.                                |
| Data format                                     | Select from the following options: • Raw/Proportional Data • Engineering Units (default) • Percent Range                                             | See Analog Data Formats on page 12 for detailed information.                                                                      |
| Input filter                                    | Choose from the following values: 50/60Hz Rejection No Filter 2-Point Moving Average 4-Point Moving Average 8-Point Moving Average 50/60Hz Rejection | See Input Filter on page 14 for detailed information.                                                                             |
| High High alarm                                 | Check the checkbox to enable an alarm. By default, High High and Low Low alarms are disabled and High and Low alarms are enabled.                    | Process level alarms alert you when the module has exceeded configured High, High High, Low, and Low Low limits for each channel. |
| High alarm                                      | Check the checkbox to enable an alarm. By default, High High and Low Low alarms are disabled and High and Low alarms are enabled.                    | Process level alarms alert you when the module has exceeded configured High, High High, Low, and Low Low limits for each channel. |
| Low alarm                                       | Check the checkbox to enable an alarm. By default, High High and Low Low alarms are disabled and High and Low alarms are enabled.                    | Process level alarms alert you when the module has exceeded configured High, High High, Low, and Low Low limits for each channel. |
| Low Low alarm                                   | Check the checkbox to enable an alarm. By default, High High and Low Low alarms are disabled and High and Low alarms are enabled.                    | Process level alarms alert you when the module has exceeded configured High, High High, Low, and Low Low limits for each channel. |

2085-IQ16 and 2085-IQ32T

<!-- image -->

For the 16- and 32-channel DC input modules, 2085-IQ16 and 2085-IQ32T respectively, you can configure OFF to ON and ON to OFF ranges.

Table 15 - Configuration Parameters for 2085-IQ16 and 2085-IQ32T

<!-- image -->

| Configuration Property What to do   |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Input —                             |                                                                                                            |
| OFF to ON                           | Choose from the following values: • 8.0 ms • 4.0 ms • 2.0 ms (default) • 1.0 ms • 0.5 ms • 0.1 ms • 0.0 ms |
| ON to OFF                           | Choose from the following values: • 8.0 ms (default) • 4.0 ms • 2.0 ms • 1.0 ms • 0.5 ms • 0.1 ms • 0.0 ms |

2085-OV16, 2085-OB16, 2085-OW16, 2085-OA8, 2085-OW8

The output modules, 2085-OV16, 2085-OB16, 2085-OW16, 2085-OA8, and 2085-OW8, only have device details available to the user in Connected Components Workbench software. There are no user configuration pages for these modules in the Connected Components Workbench software.

<!-- image -->

## 2085-OF4

<!-- image -->

For the analog output module, 2085-OF4, you can configure output unit, minimum to maximum output range, high clamp and low clamp values, and overrange and underrange values.

Table 16 - Configuration Parameters for 2085-OF4

| Configuration Property What to do Description   |                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enable channel                                  | Select or deselect the checkbox. Channel is not enabled by default.                                                                                                                                                                                                                                                                                                                   | Enable or disable a channel through this checkbox. By default, each channel is disabled.                                                                                                                                                                                                                |
| Minimum-maximum output range                    | Choose from a range of values: • 0…20 mA • 4…20 mA (default) • -10…+10 V • 0…10 V                                                                                                                                                                                                                                                                                                     | For more information, see: Input/Output Types and Ranges on page 12 Valid Range of the Data Formats for 2085-IF4, 2085-IF8, and 2085-OF4 on page 13                                                                                                                                                     |
| Data format                                     | Select from the following options: • Raw/Proportional Data • Engineering Units (default) • Percentage Data                                                                                                                                                                                                                                                                            | See Analog Data Formats on page 12 for detailed information.                                                                                                                                                                                                                                            |
| High clamp value                                | Select the checkbox to enable and enter a high clamp value.                                                                                                                                                                                                                                                                                                                           | Sets an appropriate alarm that limits the output from the analog module to remain within a range configured by the controller, even when the controller commands an output outside that range. This safety feature sets a high clamp and a low clamp. Once clamps are determined for a module, any data |
| Low clamp value                                 | Select the checkbox to enable and enter a low clamp value.                                                                                                                                                                                                                                                                                                                            | received from the controller that exceeds those clamps sets an appropriate limit alarm and transitions the output to that limit but not beyond the requested value.                                                                                                                                     |
| Overrange alarm trigger                         | If you enabled and entered a High Clamp value, you can check High Clamp Value as overrange alarm trigger. If you did not enable and entered a High Clamp value, you can check Maximum Output Value as your overrange alarm trigger. If you enabled and entered a Low OverRangeAlarm High Clamp Value Maximum Output Value OverRangeAlarm Trigger High ClampValue Maximum Output Value | The overrange and underrange feature detects when the output module is operating beyond limits set by the output range. The trigger could be set based on clamp values or minimum/maximum output values.                                                                                                |
| Underrange alarm trigger                        | Clamp value, you can check Low Clamp Value to set it as underrange alarm trigger. If you did not enable and entered a Low Clamp value, you can check Minimum Output Value as underrange alarm trigger. UnderRangeAlarmTrigger Low Clamp Value Minimum Output Value UnderRangeAlarmTrigger Low ClampValue Minimum Output Value                                                         | The overrange and underrange feature detects when the output module is operating beyond limits set by the output range. The trigger could be set based on clamp values or minimum/maximum output values.                                                                                                |
| Latch over and under alarm                      | Select to latch.                                                                                                                                                                                                                                                                                                                                                                      | Check the box to latch an alarm in the set position even if the condition that causes the alarm disappears.                                                                                                                                                                                             |
|                                                 |                                                                                                                                                                                                                                                                                                                                                                                       | Restore defaults Select button to restore defaults. Restores default device properties                                                                                                                                                                                                                  |

## 2085-IRT4

<!-- image -->

For the RTD and Thermocouple expansion I/O module, 2085-IRT4, you can configure sensor type, data format, temperature units, and other properties, on each of the four individual channels.

Table 17 - Configuration Parameters for 2085-IRT4

| Configuration Property What to do Description   |                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                 | Enable channel Select the box to enable.                                                                                                                                                                                                                                                                                                                                                                       | This parameter enables the particular channel for operation.                                                                                                                                                                                                                                                                                                                                                                                           |
| Sensor type                                     | Select from the following sensors: • 100 Ω Platinum 385 • 200 Ω Platinum 385 • 100 Ω Platinum 3916 • 200 Ω Platinum 3916 • 100 Ω Nickel 618 • 200 Ω Nickel 618 • 120 Ω Nickel 672 • 100 Ω Copper 427 • 0…500 Ohm • 0…100 mV • Thermocouple B • Thermocouple C • Thermocouple E • Thermocouple J • Thermocouple K • Thermocouple TXK/XK (L) • Thermocouple N • Thermocouple R • Thermocouple S • Thermocouple T | Defines the RTD or Thermocouple sensor type for the channel                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                | Units Set as °C or °F Sets the temperature unit to be used by the channel                                                                                                                                                                                                                                                                                                                                                                              |
| RTD wiring type                                 | Set as any of the following: • 2-wire • 3-wire • 4-wire                                                                                                                                                                                                                                                                                                                                                        | The wiring type for channel x. This parameter is only available when the Sensor Type for the channel is RTD or (0…500 Ω).                                                                                                                                                                                                                                                                                                                              |
| RTD 2-wire cable resistance                     | Replace value from 0.0…500.00 ohms to 0.0…655.35 ohms.                                                                                                                                                                                                                                                                                                                                                         | The specified cable resistance for the 2-wire cable. When the RTD 2-wire cable resistance value is smaller than the input value, it is subtracted from the input value during each read. When the value is greater than the input value, the under-range or open status bit is set (1). To configure the wire resistance, the sensor type must be RTD or (0…500 Ω) and the RTD Wiring Type must be 2-wire. Otherwise, this parameter is not available. |
| Data format                                     | Choose from the following options: • Raw/Proportional Data • Engineering Units*1 • Engineering Units*10 • Percent range                                                                                                                                                                                                                                                                                        | For more information, see: Data Format on page 16 Valid Range of the Data Formats for 2085-IRT4 on page 17                                                                                                                                                                                                                                                                                                                                             |

Table 17 - Configuration Parameters for 2085-IRT4 (Continued)

| Configuration Property What to do Description   |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter update time • 480                        | Set as the following (in msec): • 4 • 8 • 16 • 32 • 40 • 48 • 60 • 101 • 120 • 160 • 200 • 240 • 320 | See Filter Frequency on page 18 . NOTE: Filter update time 4 ms is not available for Thermocouple sensor types B, R, S, E, J, C, K, L, N, or T or 0…10 mV. Filter update time 8 ms is not available for                                                                                                                                                                                                                                                                                                                                                      |
| Filter frequency (-3dB)                         | • Set as the following (in Hz): • 114 • 60 • 30 • 14 • 12 • 9.4 • 8.0 • 4.7 • 4.0 • 3.0 • 2.4 • 2.0  | Thermocouple sensor types B, R, S.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 50/60 Hz noise rejection                        | Set as: • Both (default) • 50 Only • 60 Only • Neither                                               | See Noise Rejection on page 14 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Open circuit response                           | Choose from the following options: • Upscale • Downscale • Hold Last State • Zero                    | Defines the response to be taken during an open circuit, whether to upscale, downscale, hold last state, or zero. Upscale – Sets input to full upper scale value of channel data word. The full-scale value is determined by the selected input type, data format, and scaling. Downscale – Sets input to full lower scale value of channel data word. The low scale value is determined by the selected input type, data format, and scaling. Hold Last State – Sets input to last input value. Zero – Sets input to 0 to force the channel data word to 0. |

## Delete and Replace an Expansion I/O Configuration

Using our example project, let us try to delete 2085-IF4 in slot 2 and 2085-OB16 in slot 3. Then, let us replace the modules with 2085-OW16 and another 2085-IQ32T module in slots 2 and 3, respectively.

## To do this:

1. On the project graphic in the center pane, right-click 2085-IF4 and select Delete.
2. Another message box appears asking you if you want to empty the placeholders to the left to fill the empty slot. Select No.

<!-- image -->

<!-- image -->

After deleting 2085-IF4 from slot 2, the project graphic should look like as follows:

<!-- image -->

3. On the empty slot (slot 2), right-click and select 2085-OW16.
4. Next, replace 2085-OB16 in slot 3 with a 2085-IQ32T device. Right-click 2085-OB16 in slot 3, and choose 2085-IQ32T.

The project graphic and Expansion Modules list should look as follows after the modules are replaced:

<!-- image -->

## Build, Save, Download a Project with Expansion I/O Configuration

<!-- image -->

You can also delete and replace an expansion I/O through the Expansion Modules list. To replace, right-click the expansion I/O module you would like to replace, then select the Expansion I/O module you would like to replace it with, from the list that appears. To delete the Expansion I/O, choose Delete.

<!-- image -->

To learn how to build, save, and download the project to your controller, see the Connected Components Workbench Online Help.

## Discrete I/O Data Mapping

## Expansion I/O Data Mapping

This section includes I/O data mapping for the discrete, analog, and specialty expansion I/O modules.

<!-- image -->

Use the Connected Components Workbench software to see Global Variables.

2085-IQ16 and 2085-IQ32T I/O Data Mapping

Discrete input states can be read from Global Variables \_IO\_Xx\_DI\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…15 for 2085-IQ16 and 00…31 for 2085-IQ32T.

2085-OV16 and 2085-OB16 I/O Data Mapping

Discrete output states can be read from Global Variables \_IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…15.

Discrete output states can be written to Global Variables \_IO\_Xx\_DO\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…15.

2085-IA8 and 2085-IM8 I/O Data Mapping

Discrete input states can be read from Global Variables \_IO\_Xx\_DI\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…07.

2085-OA8 I/O Data Mapping

Discrete output states can be read from Global Variables \_IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…07.

Discrete output states can be written to Global Variables \_IO\_Xx\_DO\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…07.

2085-OW8 and 2085-OW16 I/O Data Mapping

Discrete output states can be read from Global Variables \_IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…07 for 2085-OW8 and 00…15 for 2085-OW16.

Discrete output states can be written to Global Variables \_IO\_Xx\_DO\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the point number 00…07 for 2085-OW8 and 00…15 for 2085-OW16.

<!-- image -->

## Analog I/O Data Mapping

## Table 18 - 2085-IF4(1) Status Data Mapping

| Word R/W 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |                               |                                                                                |                                                                                |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|--------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|                                                  | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved                                                  | Status 0 R PU GF CRC Reserved                                                  | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved |
|                                                  |                               | Status 1 R Reserved HHA1 LLA1 HA1 LA1 DE1 S1 Reserved HHA0 LLA0 HA0 LA0 DE0 S0 | Status 1 R Reserved HHA1 LLA1 HA1 LA1 DE1 S1 Reserved HHA0 LLA0 HA0 LA0 DE0 S0 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|                                                  |                               | Status 2 R Reserved HHA3 LLA3 HA3 LA3 DE3 S3 Reserved HHA2 LLA2 HA2 LA2 DE2 S2 | Status 2 R Reserved HHA3 LLA3 HA3 LA3 DE3 S3 Reserved HHA2 LLA2 HA2 LA2 DE2 S2 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |

## 2085-IF8 I/O Data Mapping

Analog input values are read from Global Variables \_IO\_Xx\_AI\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the channel number 00…07.

Analog input status values can be read from Global Variables IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the status word number 00…04. Individual bits within a status word can be read by appending '.zz' to the Global Variable name, where 'zz' is the bit number 00...15.

## Table 19 - 2085-IF8(1) Status Data Mapping

| Word R/W 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |                                                                                |                                                                                |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|--------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|                                                  |                                                                                | Status 0 R PU GF CRC Reserved                                                  | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved | Status 0 R PU GF CRC Reserved |
|                                                  | Status 1 R Reserved HHA1 LLA1 HA1 LA1 DE1 S1 Reserved HHA0 LLA0 HA0 LA0 DE0 S0 | Status 1 R Reserved HHA1 LLA1 HA1 LA1 DE1 S1 Reserved HHA0 LLA0 HA0 LA0 DE0 S0 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|                                                  | Status 2 R Reserved HHA3 LLA3 HA3 LA3 DE3 S3 Reserved HHA2 LLA2 HA2 LA2 DE2 S2 | Status 2 R Reserved HHA3 LLA3 HA3 LA3 DE3 S3 Reserved HHA2 LLA2 HA2 LA2 DE2 S2 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|                                                  | Status 3 R Reserved HHA5 LLA5 HA5 LA5 DE5 S5 Reserved HHA4 LLA4 HA4 LA4 DE4 S4 | Status 3 R Reserved HHA5 LLA5 HA5 LA5 DE5 S5 Reserved HHA4 LLA4 HA4 LA4 DE4 S4 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|                                                  | Status 4 R Reserved HHA7 LLA7 HA7 LA7 DE7 S7 Reserved HHA6 LLA6 HA6 LA6 DE6 S6 | Status 4 R Reserved HHA7 LLA7 HA7 LA7 DE7 S7 Reserved HHA6 LLA6 HA6 LA6 DE6 S6 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |

Table 20 - Field Descriptions for 2085-IF4 and 2085-IF8 Input Modules

|                      | Field Description                                                                                                                                                   | Field Description   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| CRC error            | This bit is set (1) when there is a CRC error on the data received. It gets cleared when the next good data is received.                                            | CRC                 |
| Data error           | getting any reading for the current sampling. The respective returned Input Data value remains the same as the previous sample.                                     | DE#                 |
| General fault        | This bit is set (1) when any of these faults occur: RAM test failure, ROM test failure, EEPROM failure, and reserved bits. All channel fault bits (S#) are set too. | GF                  |
| High Alarm overrange | These bits are set (1) when the input channel exceeds a preset high limit defined by the configuration selected (UL# is set).                                       | HA#                 |

The following sections provide I/O and status mapping for the following analog expansion I/O modules:

| Catalog Number Description                                      |
|-----------------------------------------------------------------|
| 2085-IF4 4-channel, 14-bit analog voltage/current input module  |
| 2085-IF8 8-channel, 14-bit analog voltage/current input module  |
| 2085-OF4 4-channel, 12-bit analog voltage/current output module |
| 2085-IRT4 4-channel, 16-bit RTD and Thermocouple input module   |

<!-- image -->

Use the Connected Components Workbench software to see Global Variables.

## 2085-IF4 I/O Data Mapping

Analog input values are read from Global Variables \_IO\_Xx\_AI\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the channel number 00…03.

Analog input status values can be read from Global Variables IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the status word number 00…02.

Table 21 - 2085-OF4 Control Data Mapping

| Word   | Bit Position                                                       | Bit Position                          | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   | Bit Position   |
|--------|--------------------------------------------------------------------|---------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Word   |                                                                    | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |                |                |                |                |                |                |                |                |                |                |                |                |                |                |
|        | Control 0 Reserved CE3 CE2 CE1 CE0 UU3 UO3 UU2 UO2 UU1 UO1 UU0 UO0 |                                       |                |                |                |                |                |                |                |                |                |                |                |                |                |                |

## Channel Alarm/Error Unlatch

UUx and UOx are written during run mode to clear any latched underrange and overrange alarms. The alarm is unlatched when the unlatch bit is set (1) and the alarm condition no longer exists. If the alarm condition persists, then the unlatch bit has no effect.

CEx are written during run mode to clear any DAC hardware error bits and re-enable the errordisabled channel x.

You need to keep the unlatch bit set until verification from the appropriate input channel status word says that the alarm status bit has cleared (0), then you need to reset (0) the unlatch bit.

## Status Data

Analog output status can be read from Global Variables IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the status word number 00…06. Individual bits within a status word can be read by appending a '.zz' to the Global Variable name, where 'zz' is the bit number 00...15.

Table 22 - 2085-OF4 Status Data Mapping

| Bit Position                  | Bit Position                                                 | Bit Position                                                         | Bit Position                                                         | Bit Position                                                 | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  | Bit Position                  |
|-------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|                               |                                                              |                                                                      | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                |                                                              |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
| Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value                                | Status 0 Channel 0 Data Value                                        | Status 0 Channel 0 Data Value                                        | Status 0 Channel 0 Data Value                                | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value | Status 0 Channel 0 Data Value |
| Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value                                | Status 1 Channel 1 Data Value                                        | Status 1 Channel 1 Data Value                                        | Status 1 Channel 1 Data Value                                | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value | Status 1 Channel 1 Data Value |
| Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value                                | Status 2 Channel 2 Data Value                                        | Status 2 Channel 2 Data Value                                        | Status 2 Channel 2 Data Value                                | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value | Status 2 Channel 2 Data Value |
| Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value                                | Status 3 Channel 3 Data Value                                        | Status 3 Channel 3 Data Value                                        | Status 3 Channel 3 Data Value                                | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value | Status 3 Channel 3 Data Value |
|                               | Status 4 PU GF CRC Reserved Reserved E3 E2 E1 E0 S3 S2 S1 S0 | Status 4 PU GF CRC Reserved Reserved E3 E2 E1 E0 S3 S2 S1 S0         | Status 4 PU GF CRC Reserved Reserved E3 E2 E1 E0 S3 S2 S1 S0         | Status 4 PU GF CRC Reserved Reserved E3 E2 E1 E0 S3 S2 S1 S0 |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
|                               |                                                              | Status 5 Reserved U3 O3 Reserved U2 O2 Reserved U1 O1 Reserved U0 O0 | Status 5 Reserved U3 O3 Reserved U2 O2 Reserved U1 O1 Reserved U0 O0 |                                                              |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
| Status 6 Reserved             | Status 6 Reserved                                            | Status 6 Reserved                                                    | Status 6 Reserved                                                    | Status 6 Reserved                                            | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             | Status 6 Reserved             |

Table 20 - Field Descriptions for 2085-IF4 and 2085-IF8 Input Modules (Continued)

|                           | Field Description                                                                                                                   | Field Description   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| High High Alarm overrange | These bits are set (1) when the input channel exceeds a preset high high limit defined by the configuration selected (UL# is set).                                                                                                                                     | HHA#                |
| Low Alarm underrange      | These bits are set (1) when the input channel goes below the configured low alarm limit.                                            | LA#                 |
| Low Low Alarm underrange  | These bits are set (1) when the input channel goes below the configured low-low alarm limit.                                        | LLA#                |
| Power up                  | It is set when an unexpected MCU reset occurs in RUN mode. All channel fault bits (S#) are set too. The module stays connected with | PU                  |
| Channel fault             | These bits are set(1) if the corresponding channels are open, have data error or under/overrange.                                   | S#                  |

## 2085-OF4 I/O Data Mapping

Analog output data can be written to Global Variables \_IO\_Xx\_AO\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the channel number 00…03.

Control bit states can be written to Global Variable \_IO\_Xx\_CO\_00.zz, where 'x' represents the expansion slot number 1…4 and 'zz' represents the bit number 00…12.

Table 24 - 2085-IRT4 Status Data Mapping

| Word                                                             |                                       |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |
|------------------------------------------------------------------|---------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Word                                                             | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |
| Status 0 DE3 DE2 DE1 DE0 OC3 OC2 OC1 OC0 R3 R2 R1 R0 S3 S2 S1 S0 |                                       |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |
| Status 1 O3 O2 O1 O0 U3 U2 U1 U0 T3 T2 T1 T0                     |                                       | CJC over                    | CJC under                   | CJC OC CJC DE               |                             |                             |                             |                             |                             |                             |                             |                             |                             |
|                                                                  | Status 2 PU GF CRC Reserved           | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved | Status 2 PU GF CRC Reserved |

Table 25 - Field Descriptions for 2085-IRT4

| Field Description                                                                                                                          | Field Description                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CJC open circuit                                                                                                                           | CJC OC  Indicates that the cold junction sensor is open-circuit. CJC DE bit, when set, indicates the cold junction sensor current readings is not reliable. The previous reading shall be used instead. It indicates internal compensation status if Tx is set. |
| Indicates that the cold junction sensor current readings is not reliable. The previous reading will be used instead. It indicates internal | CJC DE  CJC data error                                                                                                                                                                                                                                          |
| CJC overrange Indicates cold junction sensor overrange (above 75 °C).                                                                      | CJC over                                                                                                                                                                                                                                                        |
|                                                                                                                                            | CJC under  CJC underrange Indicates cold junction sensor is underrange (below -25 °C).                                                                                                                                                                          |
| CRC error                                                                                                                                  | CRC  Indicates there is a CRC error on data receive. All channelfault bits (Sx) are also set. The error is cleared when the next good data is received.                                                                                                         |
| Data error                                                                                                                                 | DEx  Indicates that the current input data is not reliable. The previous input data is sent to the controller instead. Diagnostic status bits are for internal use only.                                                                                        |

Table 23 - Field Descriptions for 2085-OF4 Status Word

|     | Field Description   | Field Description                                                                                                                                                                                                                                                                                    |
|-----|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRC | CRC error           | Indicates there is a CRC error on data receive. All channel fault bits (Sx) are also set. The error is cleared when the next good data is received.                                                                                                                                                  |
| Ex  | Error               | Indicates there is an DAC hardware error, broken wire or high load resistance associated with the channel x, an error code may be displayed on the respective input word (0…3) and the corresponding channel is locked (disabled) until user clears the error by writing the CEx bit in output data. |
| GF  | General fault       | Indicates a fault has occurred, including: RAM test failure, ROM test failure, EEPROM failure, and reserved bits. All channel fault bits (Sx) are also set.                                                                                                                                          |
| Ox  | Overrange flag      | Indicates the controller is attempting to drive the analog output above its normal operating range or above the channel's High Clamp level. However the module continues to convert analog output data to a maximum full range value if clamp levels are not set for the channel.                    |
| PU  | Power up            | Indicates an unexpected MCU reset has occurred in RUN mode. All channel error bits (Ex) and fault bits (Sx) are also set. The module stays connected with no configuration after the reset. PU and channel fault bits are cleared when a good configuration is downloaded.                           |
| Sx  |                     | Channel fault Indicates there is an error associated with the channel x.                                                                                                                                                                                                                             |
| Ux  | Underrange flag     | Indicates the controller is attempting to drive the analog output below its normal operating range or below the channel's Low Clamp level (if clamp limits are set for the channel).                                                                                                                 |

## Specialty I/O Data Mapping

2085-IRT4 I/O Data Mapping

Analog input values can be read from Global Variables \_IO\_Xx\_AI\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the channel number 00…03.

Analog input status can be read from Global Variables IO\_Xx\_ST\_yy, where 'x' represents the expansion slot number 1…4 and 'yy' represents the status word number 00…02. Individual bits within a status word can be read by appending a '.zz' to the Global Variable name, where 'zz' is the bit number 00...15.

## Calibration of Analog Modules

Table 25 - Field Descriptions for 2085-IRT4 (Continued)

|     | Field Description         | Field Description                                                                                                                                                                                                                                                               |
|-----|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GF  | General fault             | Indicates a fault has occurred, including: RAM test failure, ROM test failure, EEPROM failure, and reserved bits. All channel fault bits (Sx) are also set.                                                                                                                     |
| OCx |                           | Open-circuit flag Indicates that an open-circuit condition exists on the channel x.                                                                                                                                                                                             |
| Ox  | Overrange flag            | Indicates the controller is attempting to drive the analog input above its normal operating range or above the channel's High Clamp level. However the module continues to convert analog input data to a maximum full range value if clamp levels are not set for the channel. |
| PU  | Power up                  | Indicates an unexpected MCU reset has occurred in RUN mode. All channel error bits (Ex) and fault bits (Sx) are also set. The module stays connected with no configuration after the reset. PU and channel fault bits are cleared when a good configuration is downloaded.      |
| Rx  | RTD compensation          | Indicates that the RTD compensation of channel x is not working. This is effective for RTD and ohm type only.                                                                                                                                                                   |
| Sx  |                           | Channel fault Indicates there is an error associated with the channel x.                                                                                                                                                                                                        |
| Tx  | Thermocouple compensation | Indicates that the thermocouple compensation of channel x is not working. This is effective for thermocouple type only.                                                                                                                                                         |
| Ux  | Underrange flag           | Indicates that the input of channel x is at the minimum end of its normal operating range. The module automatically resets the bit when the under-range condition is cleared and the data value is within the normal operating range.                                           |

The analog modules are shipped to you calibrated.

## Notes:

## Numerics

2085-ECR 7

2085-EP24VDC 7

wiring 26

2085-IA8 7 , 11

configuration parameters 31

I/O data mapping 39 19

wiring

## 2085-IF4 7 , 12 , 36

configuration parameters 31

I/O data mapping 40

normal mode rejection wiring 22

## 2085-IF4/IF8 parameter

Enable Channel 32

minimum-maximum input range 32

2085-IF8 7 , 12

configuration parameters 31

I/O data mapping 40

wiring 23

2085-IM8 7 , 11

configuration parameters 31

I/O data mapping 39

wiring 19

2085-IQ16 7 , 11 , 32

I/O data mapping 39

wiring 19

2085-IQ32T 7 , 11 , 24 , 32

hardware components wiring 20

wiring option 25

2085-IRT4 7 , 15

35

configuration parameters data format 16 data formats valid range 17 filter frequency 18 open circuit response 17

sensor type 15 , 35

wiring 24

2085-OA8 7 , 33

I/O data mapping 39

wiring 20

2085-OB16 7 , 33

configuration parameters 33 I/O data mapping 39 21

wiring

2085-OF4 7 , 12 , 14 , 15 , 33

configuration parameters 33 , 34 data format 34 I/O data mapping 41 Latch over and under alarm 34 minimum-maximum output range 34 Restore defaults 34

wiring 23

## 2085-OV16 7 , 33

I/O data mapping 39

wiring 21

2085-OW16 7 , 33

configuration parameters 33

I/O data mapping 39 wiring 22

14

9

## 2085-OW8 7 , 33

I/O data mapping 39 21

wiring

## A

alarm status bit 15

alarm status bits 14

analog expansion I/O 12

analog module 15

I/O Type/Range 12

analog to data format conversion 17

analog value to data format value conversion formula 13

average filter 14

## C

channel alarm 14

channel status byte 14

clamp 15

clamping alarm 15

default high/low values 15

limits 15

clamping limits 15

clamps 15

common mode rejection 14

configuration add 27

edit expansion I/O 30

Connected Components Workbench 11 , 12 , 14 ,

16 , 27 , 33

continuous current 12

crimp pin 25

current 12 , 13

## D

data format 15 , 17 , 32 , 35

conversion formula 13 , 17

valid range 13 , 17

valid range for 2085-IRt4 17

data formats 12 , 16

engineering units 13 percent range 13 raw/proportional data 12 valid range for 2085-IF4/IF8 valid range for 2085-OF4 13

## default range

high clamp/low clamp 15

digital filter 14 , 18

discrete input 11

discrete output 11

double-width expansion I/O 8

Downscale 17

13

| E                                                     | O                                                                                |
|-------------------------------------------------------|----------------------------------------------------------------------------------|
| engineering units  13 ,  15                           | open circuit response  36                                                        |
| Engineering Units x 1  16                             | downscale  36                                                                    |
| Engineering Units x 10  16                            | hold last state  36                                                              |
| Expansion I/O  7                                      | upscale  17 ,  36                                                                |
| expansion I/O                                         | operating range  13                                                              |
| analog  12                                            | overrange alarm trigger  34                                                      |
| configuration  27                                     |                                                                                  |
| data mapping  39                                      | P                                                                                |
| discrete  11                                          |                                                                                  |
| discrete input  11 discrete output  11                | Percent Range  16 percent range  13 15                                           |
| hardware features  8                                  | ,                                                                                |
|                                                       | process alarms  14                                                               |
| filter frequency  18                                  |                                                                                  |
| filter frequency (-3dB)  36 filter update time  36    | raw/proportional data  13 ,  15 Raw/Proportional Data Format                     |
|                                                       | 16                                                                               |
| frequency filter  14                                  | resolution  13                                                                   |
|                                                       | RTD sensor types  15 16                                                          |
| H                                                     | RTD types  RTD wiring type  35                                                   |
| hardware features  8                                  |                                                                                  |
| hardware revision  11                                 | S                                                                                |
| 32                                                    | safety feature  15                                                               |
| high alarm  high clamp  15 ,  33 high clamp value  34 | sensor range  16                                                                 |
| high-high alarm  14 ,  32                             | sensor type  17                                                                  |
| Hold Last State  17                                   | single-width expansion I/O  8 solenoids  11                                      |
| I                                                     | status data  41                                                                  |
| indicators  11                                        | status indicator  11 surge  12                                                   |
| input data  13                                        |                                                                                  |
| input filter  14 ,  32 input signals  14              | T thermocouple  16                                                               |
| Input/Output Type/Range 2085-IF4  12                  | Thermocouple and RTD                                                             |
|                                                       | 16 Thermocouple and RTD sensor types  15                                         |
| L                                                     | thermocouple types  16                                                           |
| latch configuration  15                               |                                                                                  |
| low alarm  32                                         | U                                                                                |
| low clamp  15 low clamp value  34                     | UL restrictions Class 2 or Limited Voltage/Current  underrange alarm trigger  34 |
| low limits  14                                        | 24                                                                               |
| low low alarm  32                                     | Units  35                                                                        |
| low-low alarm  14                                     |                                                                                  |
|                                                       | V                                                                                |
|                                                       | 12 ,  13                                                                         |
| M                                                     | voltage                                                                          |
| Micro800 expansion I/O  27 motor starters  11         | W                                                                                |
|                                                       | wiring 2085-IQ32T  24                                                            |
| N noise immunity  11                                  | wiring connections                                                               |
| 14 18 36                                              |                                                                                  |
| ,  ,                                                  |                                                                                  |
|                                                       | 19                                                                               |
| noise rejection                                       |                                                                                  |

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

Allen-Bradley, Connected Components Workbench, expanding human possibility, FactoryTalk, Micro800, Micro830, Micro850, Micro870, Rockwell Automation, and TechConnect are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expanding humanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIA PACIFIC:Rockwell Automation SEA Pte Ltd, 2 Corporation Road, #04-05, Main Lobby,Corporation Place,Singapore 618494,Tel:(65)6510 6608