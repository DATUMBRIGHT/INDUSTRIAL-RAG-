<!-- image -->

## Important User Information

Because of the variety of uses for the products described in this publication, those responsible for the application and use of this control equipment must satisfy themselves that all necessary steps have been taken to assure that each application and use meets all performance and safety requirements, including any applicable laws, regulations, codes and standards.

The illustrations, charts, sample programs and layout examples shown in this guide are intended solely for example. Since there are many variables and requirements associated with any particular installation, Allen-Bradley does not assume responsibility or liability (to include intellectual property liability) for actual use based upon the examples shown in this publication.

Allen-Bradley publication SGI–1.1, "Safety Guidelines For The Application, Installation and Maintenance of Solid State Control" (available from your local Allen-Bradley office) describes some important differences between solid-state equipment and electromechanical devices which should be taken into consideration when applying products such as those described in this publication.

Reproduction of the contents of this copyrighted publication, in whole or in part, without written permission of Allen–Bradley Company, Inc. is prohibited.

Throughout this manual we make notes to alert you to possible injury to people or damage to equipment under specific circumstances.

<!-- image -->

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage or economic loss.

Attention helps you:

- Identify a hazard.
- Avoid the hazard.
- Recognize the consequences.

Important: Identifies information that is especially important for successful application and understanding of the product.

Important: We recommend you frequently backup your application programs on appropriate storage medium to avoid possible data loss.

## Summary of Changes

This publication contains new and revised information not included in the previous version.

## New Information

## Addition of DeviceNet Mapping

A new chapter has been added to describe the special mapping for DeviceNet.

## Additional Flex I/O Modules

New series B analog modules are now available for Flex I/O users. These modules are:

- 1794-OE4 series B 4 output analog module
- 1794-IE8 series B 8 input analog module
- 1794-IE4XOE2 series B 4 in/2 out combo analog module

The differences between series A and series B are explained in Appendix B.

## I/O Mapping

I/O mapping for the series B versions of the analog modules has been added.

## Revised Information

This manual has been revised to include separate chapters for remote I/O adapters and DeviceNet adapters. In addition, range selection bits have been revised to include an Off condition.

## Change Bars

The areas in this manual which are different from previous editions are marked with change bars (as shown to the right of this paragraph) to indicate the addition of new or revised information.

| Summary of Changes  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | P1      |
|----------------------------------------------------------------------------------------------------------------------|------|
| New Information  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | P1      |
| Addition of DeviceNet Mapping  . . . . . . . . . . . . . . . . . . . . . . . .                                       | P1      |
| Additional Flex I/O Modules  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | P1      |
| I/O Mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             | P1      |
| Revised Information  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             | P1      |
| Change Bars  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | P1      |
| Using This Manual  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | P-1  |
| Purpose of this Manual  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | P-1  |
| Audience  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        | P-1  |
| Vocabulary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          | P-1  |
| Manual Organization  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | P-1  |
| Conventions  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | P-2  |
| For Additional Information  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | P-2  |
| Overview of FLEX I/O and your Analog Modules  . . . . . . . .                                                        | 1-1  |
| Chapter Objectives  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | 1-1  |
| The FLEX I/O System  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | 1-1  |
| Types of FLEX I/O Modules  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | 1-2  |
| How FLEX I/O Analog Modules Communicate with Programmable Controllers  . . . . . . . . . . . . . . . . . . . . . . . | 1-2  |
| Features of your Analog Modules  . . . . . . . . . . . . . . . . . . . . . . . .                                     | 1-4  |
| Chapter Summary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | 1-4  |
| How to Install Your Analog Module  . . . . . . . . . . . . . . . . . .                                               | 2-1  |
| Chapter Objectives  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | 2-1  |
| Before You Install Your Analog Module  . . . . . . . . . . . . . . . . . . . . .                                     | 2-1  |
| Compliance to European Union Directives  . . . . . . . . . . . . . . . . . .                                         | 2-1  |
| EMC Directive  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | 2-1  |
| Low Voltage Directive  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | 2-2  |
| Power Requirements  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                | 2-2  |
| Installing the Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | 2-4  |
| Mounting the Terminal Base Unit on a DIN Rail  . . . . . . . . . . . . .                                             | 2-4  |
| Panel/Wall Mounting  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                 | 2-5  |
| Mounting the Analog Module on the Terminal Base Unit  . . . . . . .                                                  | 2-7  |
| Connecting Wiring for the Analog Modules  . . . . . . . . . . . . . . . . . .                                        | 2-8  |
| Connecting Wiring using a 1794TB2 or TB3 Terminal Base Unit                                                                                                                      | 2-9  |
| Module Indicators  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | 2-13 |
| Chapter Summary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | 2-13 |

| Module Programming  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | 3-1   |
|---------------------------------------------------------------------------------------------------------------|-------|
| Chapter Objectives  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | 3-1   |
| Block Transfer Programming  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | 3-1   |
| Sample programs for Flex I/O Analog Modules  . . . . . . . . . . . . . . .                                    | 3-2   |
| PLC3 Programming  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 3-2   |
| Figure 3.1 PLC3 Family Sample Program Structure for a 1794IE8 Module                                                                                                               | 3-2   |
| Figure 3.2 PLC3 Family Sample Program Structure for a 1794OE4 Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 3-3   |
| Figure 3.3 PLC3 Family Sample Program Structure for a 1794IE4XOE2 Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 3-3   |
| PLC5 Programming  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 3-4   |
| Figure 3.4 PLC5 Family Sample Program Structure for the 1794IE8  . . . .                                                                                                               | 3-4   |
| Figure 3.5 PLC5 Family Sample Program Structure for the 1794OE4  . . .                                                                                                               | 3-4   |
| Figure 3.6 PLC5 Family Sample Program Structure for the 1794IE4XOE2                                                                                                               | 3-5   |
| PLC2 Programming  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 3-5   |
| Analog Data Format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       | 3-6   |
| Chapter Summary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        | 3-6   |
| Writing Configuration to and Reading Status from Your Module with a Remote I/O Adapter  . . . . . . . . . . . | 4-1   |
| Chapter Objectives  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | 4-1   |
| Configuring Your Analog Module  . . . . . . . . . . . . . . . . . . . . . . . . .                             | 4-1   |
| Range Selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | 4-2   |
| Safe State Value Selection  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         | 4-2   |
| Data Format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | 4-2   |
| Reading Data From Your Module  . . . . . . . . . . . . . . . . . . . . . . . . .                              | 4-2   |
| Mapping Data for the Analog Modules  . . . . . . . . . . . . . . . . . . . . .                                | 4-3   |
| 8 Input Analog Module (Cat. No. 1794IE8 Series B)  . . . . . . . . .                                                                                                               | 4-3   |
| Analog Input Module (1794IE8) Read  . . . . . . . . . . . . . . . . .                                                                                                               | 4-3   |
| Word/Bit Descriptions for the 1794IE8 Analog Input Module Read  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 4-4   |
| Analog Input Module (1794IE8/B) Write Configuration Block  .                                                                                                               | 4-4   |
| Range Selection Bits for the 1794IE8/B Analog Input Module                                                                                                               | 4-5   |
| Word/Bit Descriptions for the 1794IE8/B Analog Input Module Write  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 4-5   |
| 4 Output Analog Module (Cat. No. 1794OE4 Series B)  . . . . . . .                                                                                                               | 4-6   |
| Analog Output Module (1794OE4/B) Read  . . . . . . . . . . . . .                                                                                                               | 4-6   |
| Bit/Word Descriptions for the 1794OE4/B Analog Output Module Read  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | 4-6   |
| Analog Output Module (1794OE4/B) Write Configuration Block                                                                                                               | 4-7   |

| Range Selection Bits for the 1794OE4/B Analog Output Module (Word 5)  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-7   |
|-----------------------------------------------------------------------------------------------|-------|
| Word/Bit Descriptions for the 1794OE4/B Analog Output Module Write  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-7   |
| 4 Input/2 Output Analog Combo Module (Cat. No. 1794IE4XOE2 Series B)  . . . . . . . . . . . . . . . . . . .                                                                                               | 4-9   |
| Analog Combo Module (1794IE4XOE2/B) Read  . . . . . . . . .                                                                                               | 4-9   |
| Word/Bit Descriptions for the 1794IE4XOE2/B Analog Combo Module Read  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-9   |
| Analog Combo Module (1794IE4XOE2/B) Write Configuration Block  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-10  |
| Range Selection Bits for the 1794IE4XOE2/B Analog Combo Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-11  |
| Word/Bit Descriptions for the 1794IE4XOE2/B Analog Combo Module Write  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 4-11  |
| Chapter Summary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | 4-12  |
| How Communication Takes Place and I/O Image . . . . . . . . .                                 |       |
| Table Mapping with the DeviceNet Adapter                                                      | 5-1   |
| Chapter Objectives  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 5-1   |
| About DeviceNet Manager  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | 5-1   |
| Polled I/O Structure  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | 5-1   |
| Adapter Input Status Word  . . . . . . . . . . . . . . . . . . . . . . . . . . .              | 5-2   |
| Mapping Data into the Image Table  . . . . . . . . . . . . . . . . . . . . . . .              | 5-3   |
| 8 Input Analog Module (Cat. No. 1794IE8 Series B) Image Table Mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-3   |
| Analog Input Module (1794IE8/B) Read  . . . . . . . . . . . . . . .                                                                                               | 5-3   |
| Analog Input Module (1794IE8/B) Write  . . . . . . . . . . . . . . . .                                                                                               | 5-4   |
| Range Selection Bits for the 1794IE8/B Analog Input Module                                                                                               | 5-4   |
| Word/Bit Descriptions for the 1794IE8/B Analog Input Module                                                                                               | 5-4   |
| 4 Output Analog Module (1794OE4 Series B) Image Table Mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-6   |
| Analog Output Module (1794OE4/B) Read  . . . . . . . . . . . . .                                                                                               | 5-6   |
| Analog Output Module (1794OE4/B) Write  . . . . . . . . . . . . . .                                                                                               | 5-6   |
| Range Selection Bits for the 1794OE4/B Analog Output Module (Write Word 6)  . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-7   |
| Word/Bit Descriptions for the 1794OE4/B Analog Output Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-7   |
| Analog Combo Module (1794IE4XOE2 Series B)                                                                                               |       |
| Image Table Mapping  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | 5-9   |
| Analog Combo Module (1794IE4XOE2/B) Read  . . . . . . . . .                                                                                               | 5-9   |
| Analog Output Module (1794IE4XOE2/B) Write  . . . . . . . . . .                                                                                               | 5-10  |
| Range Selection Bits for the 1794IE4XOE2 Analog Combo Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-10  |
| Word/Bit Descriptions for the 1794IE4XOE2 Analog Combo Module  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 5-10  |
| Defaults  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 5-12  |

| Specifications  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | A-1   |
|-------------------------------------------------------------------------------------------|-------|
| Differences Between Series A and Series B Analog Modules B-1                              |       |
| Data Table Formats  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | C-1   |
| Two's Complement Binary  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | C-1   |
| Analog Data Format  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | C-2   |
| Scaling Example  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | C-3   |
| Support Services  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | C-1   |
| Technical Support  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | C-1   |
| Engineering and Field Services  . . . . . . . . . . . . . . . . . . . . . . . .           | C-1   |
| Technical Training  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | C-1   |
| Repair and Exchange Services  . . . . . . . . . . . . . . . . . . . . . . . .             | C-1   |

## Purpose of this Manual

## Audience

## Vocabulary

## Manual Organization

## Using This Manual

This manual shows you how to use your FLEX I/O Analog modules with Allen-Bradley programmable controllers. The manual helps you install, program and troubleshoot your modules.

You must be able to program and operate an Allen-Bradley programmable controller to make efficient use of your FLEX I/O modules. In particular, you must know how to program block transfers.

We assume that you know how to do this in this manual. If you do not, refer to the appropriate programming and operations manual before you attempt to program your modules.

In this manual, we refer to:

- – the analog input or analog output module as the "input module" or ''output module"
- – the Programmable Controller as the "controller"

This manual is divided into five chapters. The following chart lists each chapter with its corresponding title and a brief overview of the topics covered in that chapter.

| Chapter   | Title                                                                                | Contents                                                                                                             |
|-----------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1         | Overview of FLEX I/O and Analog modules                                              | Describes FLEX I/O Analog modules, features, and how they function                                                   |
| 2         | How to Install Your Analog Module                                                    | How to install and wire the modules                                                                                  |
| 3         | Module Programming                                                                   | Explains block transfer programming, sample programs                                                                 |
| 4         | Writing Configuration to and Reading Status From with a Remote I/O Adapter           | Explains how to configure your modules and read status information from your modules when using a remote I/O adapter |
| 5         | How Communication Takes Place and I/O Image Table Mapping with the DeviceNet Adapter | Explains how you communicate with your modules, and how the I/O image is mapped when using a DeviceNet adapter       |
| Appendix  | Title                                                                                | Contents                                                                                                             |
| A         | Specifications                                                                       | Specifications for the analog modules                                                                                |
| B         | Differences Between Series A and Series B Analog Modules                             | Lists major differences between series.                                                                              |
| C         | Data Formats                                                                         | Explains 2's complement and left justification of numbers                                                            |

## Conventions

## For Additional Information

We use these conventions in this manual:

| In this manual, we show:                                                       | Like this:   |
|--------------------------------------------------------------------------------|--------------|
| that there is more information about a topic in another chapter in this manual |              |
| that there is more information about the topic in another manual               |              |

<!-- image -->

For additional information on FLEX I/O systems and modules, refer to the following documents:

| Catalog Number   | Voltage   |                                   | Publications              | Publications   |
|------------------|-----------|-----------------------------------|---------------------------|----------------|
|                  |           | Description                       | Installation Instructions | User Manual    |
| 1794             |           | 1794 FLEX I/O Product Data        | 17942.1                           |                |
| 1794ACN                  | 24V dc    | ControlNet Adapter                | 17945.8                           |                |
| 1794ADN                  | 24V dc    | DeviceNet Adapter                 | 17945.14                           | 17946.5.5                |
| 1794ASB                  | 24V dc    | Remote I/O Adapter                | 17945.11                           | 17946.5.3                |
| 1794TB2 1794TB3                  |           | 2wire Terminal Base 3wire Terminal Base                                   | 17945.2                           |                |
| 1794TBN                  |           | Terminal Base Unit                | 17945.16                           |                |
| 1794TBNF                  |           | Fused Terminal Base Unit          | 17945.17                           |                |
| 1794TB3T                  |           | Temperature Terminal Base Unit    | 17945.41                           |                |
| 1794IB16                  | 24V dc    | 16 Input Module                   | 17945.4                           |                |
| 1794OB16                  | 24V dc    | 16 Output Module                  | 17945.3                           |                |
| 1794IB10XOB6                  | 24V dc    | 10 Input/6 Output Module          | 17945.24                           |                |
| 1794IE8                  | 24V dc    | Selectable Analog 8 Input Module  | 17945.6                           |                |
| 1794OE4                  | 24V dc    | Selectable Analog 4 Output Module | 17945.5                           | 17946.5.2                |
| 1794IE4XOE2                  | 24V dc    | 4 Input/2 Output Analog Module    | 17945.15                           |                |
| 1794IR8                  | 24V dc    | 8 RTD Input Analog Module         | 17945.22                           | 17946.5.4                |
| 1794IT8                  | 24V dc    | 8 Thermocouple Input Module       | 17945.21                           | 17946.5.7                |
| 1794IB8S                  | 24V dc    | Sensor Input Module               | 17945.7                           |                |
| 1794IA8                  | 120V ac   | 8 Input Module                    | 17945.9                           |                |
| 1794OA8                  | 120V ac   | Output Module                     | 17945.10                           |                |
| 1794CE1                  |           | Extender Cable                    | 17942.12                           |                |
| 1794NM1                  |           | Mounting Kit                      | 17942.13                           |                |
| 1794PS1                  | 24V dc    | Power Supply                      | 17945.35                           |                |

## Chapter Objectives

## The FLEX I/O System

## Overview of FLEX I/O and your Analog Modules

In this chapter, we tell you about:

- what the FLEX I/O system is and what it contains
- types of FLEX I/O analog modules
- how FLEX I/O analog modules communicate with programmable controllers
- the features of your analog modules

FLEX I/O is a small, modular I/O system for distributed applications that performs all of the functions of rack-based I/O. The FLEX I/O system contains the following components shown below:

<!-- image -->

20125

- adapter/power supply – powers the internal logic for as many as eight I/O modules
- terminal base – contains a terminal strip to terminate wiring for two- or three-wire devices
- I/O module – contains the bus interface and circuitry needed to perform specific functions related to your application

## Types of FLEX I/O Modules

We describe the following FLEX I/O Analog modules in this user manual:

| Catalog Number   | Voltage   | Inputs   | Outputs   | Description   |
|------------------|-----------|----------|-----------|---------------|
| 1794IE8                  | 24V dc    | 8        | -         | analog - 8 input, singleended, non-isolated               |
| 1794OE4                  | 24V dc    | -        | 4         | analog - 4 output, singleended, non-isolated               |
| 1794IE4XOE2                  | 24V dc    | 4        | 2         | analog - 4 input, singleended, non-isolated and 2 output, singleended, nonisolated               |

FLEX I/O analog input, output and combination modules are block transfer modules that interface analog signals with any Allen-Bradley programmable controllers that have block transfer capability. Block transfer programming moves input from the module's memory to a designated area in the processor data table, and output data words from a designated area in the processor data table to the module's memory. Block transfer programming also moves configuration words from the processor data table to module memory.

The analog modules have selectable ranges as shown in the table below:

| Voltage     | Current   |
|-------------|-----------|
| 0 to 10V dc | 0 to 20mA |
| +/-10V dc   | 4 to 20mA |

The adapter/power supply transfers data to the module (block transfer write) and from the module (block transfer read) using BTW and BTR instructions in your ladder diagram program. These instructions let the adapter obtain input values and status from the module, and let you send output values and establish the module's mode of operation. Figure 1.1 describes the communication process.

## How FLEX I/O Analog Modules Communicate with Programmable Controllers

Figure 1.1 An Example of Communication Between an Adapter and an Analog Input Module

<!-- image -->

## Features of your Analog Modules

## Chapter Summary

Each module has a unique label identifying its keyswitch position, wiring and module type. A removable label provides space for writing individual designations per your application.

<!-- image -->

In this chapter you learned about the FLEX I/O system and the types of analog modules and how they communicate with programmable controllers.

## Chapter Objectives

## Before You Install Your Analog Module

## Compliance to European Union Directives

## How to Install Your Analog Module

In this chapter, we tell you about:

- how to install your module
- how to set the module keyswitch
- how to wire the terminal base
- the indicators

Before installing your analog module in the I/O chassis:

| You need to:                                                     | As described under:             |
|------------------------------------------------------------------|---------------------------------|
| Calculate the power requirements of all modules in each chassis. | Power Requirements, page 2-2    |
| Position the keyswitch on the terminal base                      | Installing the Module, page 2-4 |

<!-- image -->

ATTENTION: +24V dc power must be applied to your module before operation. If power is not applied, the module position will appear to the adapter as an empty slot in your chassis. If the adapter does not recognize your module after installation is completed, cycle power to the adapter.

If this product has the CE mark it is approved for installation within the European Union and EEA regions. It has been designed and tested to meet the following directives.

## EMC Directive

This product is tested to meet Council Directive 89/336/EEC Electromagnetic Compatibility (EMC) and the following standards, in whole or in part, documented in a technical construction file:

- EN 50081-2EMC – Generic Emission Standard, Part 2 – Industrial Environment
- EN 50082-2EMC – Generic Immunity Standard, Part 2 – Industrial Environment

This product is intended for use in an industrial environment.

## Power Requirements

## Low Voltage Directive

This product is tested to meet Council Directive 73/23/EEC Low Voltage, by applying the safety requirements of EN 61131–2 Programmable Controllers, Part 2 – Equipment Requirements and Tests.

For specific information required by EN 61131-2, see the appropriate sections in this publication, as well as the following Allen-Bradley publications:

- Industrial Automation Wiring and Grounding Guidelines For Noise Immunity, publication 1770-4.1
- Guidelines for Handling Lithium Batteries, publication AG-5.4
- Automation Systems Catalog, publication B111

The wiring of the terminal base unit is determined by the current draw through the terminal base. Make certain that the current draw does not exceed 10A.

<!-- image -->

ATTENTION: Total current draw through the terminal base unit is limited to 10A. Separate power connections may be necessary.

Methods of wiring the terminal base units are shown in the illustration below.

<!-- image -->

ATTENTION: Do not daisy chain power or ground from an analog terminal base unit to any ac or dc discrete module terminal base unit.

Wiring when total current draw is less than 10A

<!-- image -->

Analog module wiring separate from discrete wiring.

<!-- image -->

## Wiring when total current draw is greater than 10A

<!-- image -->

Note: All modules powered by the same power supply must be analog modules for this configuration.

Total current draw through any base unit must not be greater than 10A

## Installing the Module

Installation of the analog module consists of:

- mounting the terminal base unit
- installing the analog module into the terminal base unit
- installing the connecting wiring to the terminal base unit

If you are installing your module into a terminal base unit that is already installed, proceed to "Mounting the Analog Module on the Terminal Base" on page 2–7.

## Mounting the Terminal Base Unit on a DIN Rail

<!-- image -->

ATTENTION: Do not remove or replace a terminal base unit when power is applied. Interruption of the flexbus can result in unintended operation or machine motion.

- 1 . Remove the cover plug (if used) in the male connector of the unit to which you are connecting this terminal base unit.
- 2 . Check to make sure that the 16 pins in the male connector on the adjacent device are straight and in line so that the mating female connector on this terminal base unit will mate correctly .
- 3 . Position the terminal base on the 35 x 7.5mm DIN rail A (A-B pt. no. 199-DR1; 46277-3; EN 50022) at a slight angle with hook B on the left side of the terminal base hooked into the right side of the unit on the left.
- 4 . Make certain that the female flexbus connector C is fully retracted into the base unit.

<!-- image -->

- 5 . Rotate the terminal base onto the DIN rail with the top of the rail hooked under the lip on the rear of the terminal base. Use caution to make sure that the female flexbus connector does not strike any of the pins in the mating male connector. r.
- 6 . Press the terminal base down onto the DIN rail until flush. The locking tab D will snap into position and lock the terminal base to the DIN rail.
- 7 . If the terminal base does not lock in place, use a screwdriver or similar device to move the locking tab down, press the terminal base flush with the DIN rail and release the locking tab to lock the base in place.
- 8 . Gently push the female flexbus connector C into the adjacent terminal base or adapter female connector to complete the flexbus connections.
- 9 . Repeat the above steps to install the next terminal base.

## Panel/Wall Mounting

Installation on a wall or panel consists of:

- laying out the drilling points on the wall or panel
- drilling the pilot holes for the mounting screws
- mounting the adapter mounting plate
- installing the terminal base units and securing them to the wall or panel

If you are installing your module into a terminal base unit that is already installed, proceed to "Mounting the Analog Module on the Terminal Base" on page 2–7.

Use the mounting kit Cat. No. 1794-NM1 for panel/wall mounting.

<!-- image -->

<!-- image -->

To install the mounting plate on a wall or panel:

1. Lay out the required points on the wall/panel as shown in the drilling dimension drawing.

## Drilling Dimensions for Panel/Wall Mounting of FLEX I/O

<!-- image -->

2. Drill the necessary holes for the #6 self-tapping mounting screws.
3. Mount the mounting plate (1) for the adapter module using two #6 self-tapping screws (18 included for mounting up to 8 modules and the adapter).

Important:

Make certain that the mounting plate is properly grounded to the panel. Refer to "Industrial Automation Wiring and Grounding Guidelines," publication 1770-4.1.

4. Hold the adapter (2) at a slight angle and engage the top of the mounting plate in the indention on the rear of the adapter module.
5. Press the adapter down flush with the panel until the locking lever locks.
6. Position the terminal base unit up against the adapter and push the female bus connector into the adapter.
7. Secure to the wall with two #6 self-tapping screws.
8. Repeat for each remaining terminal base unit.

Note: The adapter is capable of addressing eight modules. Do not exceed a maximum of eight terminal base units in your system.

## Mounting the Analog Module on the Terminal Base Unit

1. Rotate the keyswitch (1) on the terminal base unit (2) clockwise to the position required for the specific type of analog module.
2. Make certain the flexbus connector (3) is pushed all the way to the left to connect with the neighboring terminal base/adapter. You cannot install the module unless the connector is fully extended.
3. Make sure that the pins on the bottom of the module are straight so they will align properly with the connector in the terminal base unit.
4. Position the module (4) with its alignment bar (5) aligned with the groove (6) on the terminal base.
5. Press firmly and evenly to seat the module in the terminal base unit. The module is seated when the latching mechanism (7) is locked into the module.
6. Repeat the above steps to install the next module in its terminal base unit.

<!-- image -->

| Analog Module Cat. No.   |   Keyswitch Position |
|--------------------------|----------------------|
| 1794IE8                          |                    3 |
| 1794OE4                          |                    4 |
| 1794IE4XOE2                          |                    5 |

<!-- image -->

ATTENTION: Remove field-side power before removing or inserting the module. This module is designed so you can remove and insert it under backplane power. When you remove or insert a module with field-side power applied, an electrical arc may occur. An electrical arc can cause personal injury or property damage by:

- sending an erroneous signal to your system's field devices causing unintended machine motion

· causing an explosion in a hazardous environment Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance.

Wiring to the analog modules is made through the terminal base unit on which the module mounts.

Refer to the following table for recommended terminal base units that you can use for each module.

| Module   | 1794TB2     | 1794TB3     |
|----------|-----|-----|
| 1794IE8          | Yes | Yes |
| 1794OE4          | Yes | Yes |
| 1794IE4XOE2          | Yes | Yes |

<!-- image -->

<!-- image -->

## &amp;RQQHFWLQJ :LULQJ XVLQJ D 7% RU 7% 7HUPLQDO %DVH 8QLW

-  &amp;RQQHFW WKH LQGLYLGXDO VLJQDO ZLULQJ WR QXPEHUHG WHUPLQDOV RQ WKH ï URZ $ RQ WKH WHUPLQDO EDVH XQLW 8VH %HOGHQ  FDEOH IRU VLJQDO ZLULQJ

<!-- image -->

$77(17,21 &amp;RQQHFW RQO\ RQH FXUUHQW RU RQH YROWDJH VLJQDO SHU FKDQQHO 'R QRW FRQQHFW ERWK FXUUHQW DQG YROWDJH RQ RQH FKDQQHO

-  &amp;RQQHFW HDFK FKDQQHO FRPPRQ WR ,( ï WKH DVVRFLDWHG WHUPLQDO RQ URZ %  2( ï WKH FRUUHVSRQGLQJ WHUPLQDO RQ WKH VDPH URZ $ ,(;2( ï LQSXWV ï WKH DVVRFLDWHG WHUPLQDO RQ URZ % RXWSXWV ï WKH FRUUHVSRQGLQJ WHUPLQDO RQ WKH VDPH URZ $
-  &amp;RQQHFW 9 GF WR WHUPLQDO  RQ WKH  URZ &amp; DQG 9 FRPPRQ WR WHUPLQDO  RQ WKH ï URZ % 

<!-- image -->

$77(17,21 7R UHGXFH VXVFHSWLELOLW\ WR QRLVH SRZHU DQDORJ PRGXOHV DQG GLVFUHWH PRGXOHV IURP VHSDUDWH SRZHU VXSSOLHV 'R QRW H[FHHG D OHQJWK RI  IW P IRU GF SRZHU FDEOLQJ

<!-- image -->

$77(17,21 5HPRYH ILHOGVLGH SRZHU EHIRUH UHPRYLQJ RU LQVHUWLQJ WKH PRGXOH 7KLV PRGXOH LV GHVLJQHG VR \RX FDQ UHPRYH DQG LQVHUW LW XQGHU EDFNSODQH SRZHU :KHQ \RX UHPRYH RU LQVHUW D PRGXOH ZLWK ILHOGVLGH SRZHU DSSOLHG DQ HOHFWULFDO DUF PD\ RFFXU $Q HOHFWULFDO DUF FDQ FDXVH SHUVRQDO LQMXU\ RU SURSHUW\ GDPDJH E\

-  VHQGLQJ DQ HUURQHRXV VLJQDO WR \RXU V\VWHP·V ILHOG GHYLFHV FDXVLQJ XQLQWHQGHG PDFKLQH PRWLRQ
-  FDXVLQJ DQ H[SORVLRQ LQ D KD]DUGRXV HQYLURQPHQW

5HSHDWHG HOHFWULFDO DUFLQJ FDXVHV H[FHVVLYH ZHDU WR FRQWDFWV RQ ERWK WKH PRGXOH DQG LWV PDWLQJ FRQQHFWRU :RUQ FRQWDFWV PD\ FUHDWH HOHFWULFDO UHVLVWDQFH

7%

<!-- image -->

-  ,I GDLV\ FKDLQLQJ WKH 9 GF SRZHU WR WKH QH[W EDVH XQLW FRQQHFW D MXPSHU IURP WHUPLQDO  RQ WKLV EDVH XQLW WR WHUPLQDO  RQ WKH QH[W EDVH XQLW &amp;RQQHFW WKH 9 GF FRPPRQUHWXUQ IURP WHUPLQDO  RQ WKLV EDVH XQLW WR WHUPLQDO  RQ WKH QH[W EDVH XQLW

<!-- image -->

$77(17,21 9 GF SRZHU PXVW EH DSSOLHG WR \RXU PRGXOH EHIRUH RSHUDWLRQ ,I SRZHU LV QRW DSSOLHG WKH PRGXOH SRVLWLRQ ZLOO DSSHDU WR WKH DGDSWHU DV DQ HPSW\ VORW LQ \RXU FKDVVLV ,I WKH DGDSWHU GRHV QRW UHFRJQL]H \RXU PRGXOH DIWHU LQVWDOODWLRQ LV FRPSOHWHG F\FOH SRZHU WR WKH DGDSWHU

7DEOH $ :LULQJ FRQQHFWLRQV IRU 7% DQG 7% 7HUPLQDO %DVH 8QLWV ZKHQ XVLQJ WKH ,( $QDORJ 0RGXOH

|         |             | /DEHO/DEHO /DEHO/DEHO   | 7% 7%                 | 7% 7%   |
|---------|-------------|-------------------------|-----------------|---|
| &KDQQHO | 6LJQDO 7\SH | 0DUNLQJV                | 6LJQDO 7HUPLQDO | 9 GF &RPPRQ 7HUPLQDO   |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                 |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | &XUUHQW     | ,                       |                  |    |
|          | 9ROWDJH     | 9                       |                  |    |
|          | 9 GF &RPPRQ             |  WKUX                          |  WKUX                  |  WKUX    |
|         | 9 GF SRZHU             | 7% ï  DQG  7% ï  WKUX                          | 7% ï  DQG  7% ï  WKUX                  | 7% ï  DQG  7% ï  WKUX    |

7DEOH % :LULQJ FRQQHFWLRQV IRU 7% DQG 7% 7HUPLQDO %DVH 8QLWV ZKHQ XVLQJ WKH 2( $QDORJ 0RGXOH

| &KDQQHO &KDQQHO  &KDQQHO &KDQQHO   | 7\SH 7\SH  7\SH 7\SH   | /DEHO 0DUNLQJ/DEHO 0DUNLQJ /DEHO 0DUNLQJ/DEHO 0DUNLQJ   | 7% 7% 6LJQDO 7HUPLQDO   |
|------------------------------------|------------------------|---------------------------------------------------------|---|
|                                     | &XUUHQW 6LJQDO         | ,                                                       |    |
|                                     | &XUUHQW &RPPRQ         | 5(7                                                     |    |
|                                     | 9ROWDJH 6LJQDO         | 9                                                       |    |
|                                     | 9ROWDJH &RPPRQ         | 5(7                                                     |     |
|                                     | &XUUHQW 6LJQDO         | ,                                                       |    |
|                                     | &XUUHQW &RPPRQ         | 5(7                                                     |    |
|                                     | 9ROWDJH 6LJQDO         | 9                                                       |    |
|                                     | 9ROWDJH &RPPRQ         | 5(7                                                     |     |
|                                     | &XUUHQW 6LJQDO         | ,                                                       |    |
|                                     | &XUUHQW &RPPRQ         | 5(7                                                     |    |
|                                     | 9ROWDJH 6LJQDO         | 9                                                       |    |
|                                     | 9ROWDJH &RPPRQ         | 5(7                                                     |     |
|                                     | &XUUHQW 6LJQDO         | ,                                                       |    |
|                                     | &XUUHQW &RPPRQ         | 5(7                                                     |    |
|                                     | 9ROWDJH 6LJQDO         | 9                                                       |    |
|                                     | 9ROWDJH &RPPRQ         | 5(7                                                     |     |
|                                     | 9 GF &RPPRQ                        |                                                         |  WKUX    |
|                                     | 9 GF                        |                                                         | 7% ï  DQG  7% ï  WKUX    |

7DEOH &amp; :LULQJ FRQQHFWLRQV IRU 7% DQG 7% 7HUPLQDO %DVH 8QLWV ZKHQ XVLQJ WKH ,(;2( $QDORJ 0RGXOH

|         |                | /DEHO    | 7% 7%                 | 7% 7%        |
|---------|----------------|----------|-----------------|--------|
| &KDQQHO | 6LJQDO 7\SH    | 0DUNLQJV | 6LJQDO 7HUPLQDO | 9 GF &RPPRQ 7HUPLQDO        |
| ,QSXW   | ,QSXW          | ,QSXW    | ,QSXW           | ,QSXW  |
|          | &XUUHQW        | ,        |                  |         |
|          | 9ROWDJH        | 9        |                  |         |
|          | &XUUHQW        | ,        |                  |         |
|          | 9ROWDJH        | 9        |                  |         |
|          | &XUUHQW        | ,        |                  |         |
|          | 9ROWDJH        | 9        |                  |         |
|          | &XUUHQW        | ,        |                  |         |
|          | 9ROWDJH        | 9        |                  |         |
| 2XWSXW  | 2XWSXW         | 2XWSXW   | 2XWSXW          | 2XWSXW |
|         | &XUUHQW 6LJQDO | ,        |                  |        |
|         | &XUUHQW &RPPRQ | 5(7      |                  |        |
|         | 9ROWDJH 6LJQDO | 9        |                  |        |
|         | 9ROWDJH &RPPRQ | 5(7      |                   |        |
|          | &XUUHQW 6LJQDO | ,        |                  |        |
|          | &XUUHQW &RPPRQ | 5(7      |                  |        |
|          | 9ROWDJH 6LJQDO | 9        |                  |        |
|          | 9ROWDJH &RPPRQ | 5(7      |                   |        |
|          | 9 GF &RPPRQ                |          |  WKUX                  |  WKUX         |
|          | 9 GF SRZHU                |          | 7% ï  DQG  7% ï  WKUX                  | 7% ï  DQG  7% ï  WKUX         |

-  7HUPLQDOV    DQG  DUH LQWHUQDOO\ FRQQHFWHG LQ WKH PRGXOH WR 9 GF FRPPRQ

 7HUPLQDOV  WKUX  DUH LQWHUQDOO\ FRQQHFWHG LQ WKH WHUPLQDO EDVH XQLW

<!-- image -->

$77(17,21 7RWDO FXUUHQW GUDZ WKURXJK WKH WHUPLQDO EDVH XQLW LV OLPLWHG WR $ 6HSDUDWH SRZHU FRQQHFWLRQV WR WKH WHUPLQDO EDVH XQLW PD\ EH QHFHVVDU\

## 0RGXOH ,QGLFDWRUV

## &amp;KDSWHU 6XPPDU\

7KH DQDORJ PRGXOHV KDYH RQH VWDWXV LQGLFDWRU WKDW LV RQ ZKHQ SRZHU LV DSSOLHG WR WKH PRGXOH

<!-- image -->

,(;2(

,Q WKLV FKDSWHU \RX OHDUQHG KRZ WR LQVWDOO \RXU LQSXW PRGXOH LQ DQ H[LVWLQJ SURJUDPPDEOH FRQWUROOHU V\VWHP DQG KRZ WR ZLUH WR WKH WHUPLQDO EDVH XQLWV

## Chapter Objectives

## Block Transfer Programming

## Module Programming

In this chapter, we tell you about:

- analog data format
- block transfer programming
- sample programs for the PLC-3 and PLC-5 processors

Your module communicates with the processor through bidirectional block transfers. This is the sequential operation of both read and write block transfer instructions.

A configuration block transfer write (BTW) is initiated when the analog module is first powered up, and subsequently only when the programmer wants to enable or disable features of the module. The configuration BTW sets the bits which enable the programmable features of the module, such as scaling, alarms, ranges, etc. Block transfer reads are performed to retrieve information from the module.

Block transfer read (BTR) programming moves status and data from the module to the processor's data table. The processor user program initiates the request to transfer data from the module to the processor. The transferred words contain module status, channel status and input data from the module.

<!-- image -->

ATTENTION: If the analog module is not powered up before the remote I/O adapter, the adapter will not recognize the module. Make certain that the analog module is installed and powered before or simultaneously with the remote I/O adapter. If the adapter does not establish communication with the module, cycle power to the adapter.

The following sample programs are minimum programs; all rungs and conditioning must be included in your application program. You can disable BTRs, or add interlocks to prevent writes if desired. Do not eliminate any storage bits or interlocks included in the sample programs. If interlocks are removed, the program may not work properly.

Your program should monitor status bits, block transfer read and block transfer write activity.

## Sample programs for Flex I/O Analog Modules

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module if the powerup bit is set.

Thereafter, the program continuously performs read block transfers.

Note: You must create the data file for the block transfers before you enter the block transfer instructions.

The pushbutton allows the user to manually request a block transfer write to configure the module.

The following sample programs show you how to use your analog module efficiently when operating with a programmable controller.

These programs show you how to:

- configure the module
- read data from the module
- update the module's output channels (if used)

These programs illustrate the minimum programming required for communication to take place.

## PLC3 Programming

Block transfer instructions with the PLC-3 processor use one binary file in a data table section for module location and other related data. This is the block transfer control file. The block transfer data file stores data that you want transferred to your module (when programming a block transfer write) or from your module (when programming a block transfer read). The address of the block transfer data files are stored in the block transfer control file.

The same block transfer control file is used for both the read and write instructions for your module. A different block transfer control file is required for every module.

A sample program segment with block transfer instructions is shown in Figure 3.1, and described below.

Figure 3.1 PLC3 Family Sample Program Structure for a 1794IE8 Module

<!-- image -->

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module and send data values.

Thereafter, the program continuously performs read block transfers and write block transfers.

Note: You must create the data file for the block transfers before you enter the block transfer instructions.

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module and send data val ues

Thereafter, the program continuously performs read block transfers and write block transfers.

Note: You must create the data file for the block transfers before you enter the block transfer instructions.

Figure 3.2 PLC3 Family Sample Program Structure for a 1794OE4 Module

<!-- image -->

Figure 3.3 PLC3 Family Sample Program Structure for a 1794IE4XOE2 Module

<!-- image -->

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module if the powerup bit is set.

Thereafter, the program continuously performs read block transfers to configure the module.

The pushbutton allows the user to manually request a block transfer write.

1 Powerup bit included in Series B modules only.

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module and send data val ues.

Thereafter, the program continuously performs read block transfers and write block transfers.

## PLC5 Programming

The PLC-5 program is very similar to the PLC-3 program with the following exceptions:

- block transfer enable bits are used instead of done bits as the conditions on each rung.
- separate block transfer control files are used for the block transfer instructions.

Figure 3.4 PLC5 Family Sample Program Structure for the 1794IE8

<!-- image -->

Figure 3.5 PLC5 Family Sample Program Structure for the 1794OE4

<!-- image -->

## Program Action

At powerup in RUN mode, or when the processor is switched from PROG to RUN, the user program enables a block transfer read. Then it initiates a block transfer write to configure the module and send data values.

Thereafter, the program continuously performs read block transfers and write block transfers.

<!-- image -->

Figure 3.6 PLC5 Family Sample Program Structure for the 1794IE4XOE2

<!-- image -->

## PLC2 Programming

The 1794 analog I/O modules are not recommended for use with PLC-2 family programmable controllers due to the number of digits needed for high resolution. In addition, the data returned from the analog-to-digital converter in the module is 12-bit resolute. This value is left-justified into a 16-bit field, reserving the most significant bit for a sign bit. Refer to Appendix B for more information.

## Analog Data Format

The data returned from the analog-to-digital converter in the module is 12-bit resolute. This value is left-justified into a 16-bit field, reserving the most significant bit for a sign bit.

<!-- image -->

## Chapter Summary

In this chapter, you learned how to program your programmable controller. You were given sample programs for your PLC-3 and PLC-5 family processors.

## Chapter Objectives

## Configuring Your Analog Module

## Writing Configuration to and Reading Status from Your Module with a Remote I/O Adapter

In this chapter, we tell you about:

- configuring your module's features
- entering your data
- reading data from your module
- read block format

Because of the many analog devices available and the wide variety of possible configurations, you must configure your module to conform to the analog device and specific application that you have chosen. The module is configured using a group of data table words that are transferred to the module using a block transfer write instruction.

The software configurable features available are:

- input/output range selection, including full range and bipolar
- safe state operating value (customer selected analog values the module will maintain in the event of a network communication error)

Note: PLC-5 family programmable controllers that use 6200 software programming tools can take advantage of the IOCONFIG utility to configure these modules. IOCONFIG uses menu-based screens for configuration without having to set individual bits in particular locations. Refer to your 6200 software literature for details.

## Range Selection

## Safe State Value Selection

## Data Format

<!-- image -->

## Reading Data From Your Module

Individual input channels are configurable to operate with the following voltage or current ranges:

|                 | Bit Settings     | Bit Settings   |
|-----------------|------------------|----------------|
| Ranges          | Configure Select | Full Range     |
| 0-10V dc/0-20mA | 0                | 1              |
| 4-20mA          | 1                | 0              |
| 10 to +10V dc                 | 1                | 1              |
| Off             | 0                | 0              |

When configured to Off, individual output channels will drive 0V/0mA.

1

<!-- image -->

ATTENTION: If using Series A modules, do not use configure select and full range bit settings of 0. Individual channels revert to 4–20mA with bit selections of all zeroes. This could result in unwanted or incorrect action.

You can select individual channel ranges using the designated words of the write block transfer instruction. Refer to the Bit/Word description for your particular module for word and bit numbers.

You can select the analog values that your output module will maintain in the event of a network communication error. When the multiplex control bits (M) are cleared simultaneously by a communication error, (or by the user), the analog outputs will automatically switch to the values set in the safe state analog words. This allows you to define a safe operating state for controlled devices which depend on the analog output from the module.

The data returned from the analog-to-digital converter in the module is 12-bit resolute. This value is left-justified into a 16-bit field, reserving the most significant bit for a sign bit. The 4–20mA mode scales in the module and uses all 16 bits.

Refer to Appendix C for a table of values for various current and voltage modes, and an example of scaling to engineering terms.

Read programming moves status and data from the module to the processor's data table. The processor's user program initiates the request to transfer data from the input module to the processor.

## Mapping Data for the Analog Modules

The following read and write words and bit/word descriptions describe the information written to and read from the analog modules. Each word is composed of 16 bits.

## 8 Input Analog Module (Cat. No. 1794IE8 Series B)

## Module Image

<!-- image -->

Analog Input Module (1794-IE8) Read

| Word/Dec. Bit   | 15   | 14                     | 13                     | 12                     | 11                     | 10                     | 09                     | 08                     | 07                     | 06                     | 05                     | 04                     | 03                     | 02                     | 01                     | 00                     |
|-----------------|------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| Word/Octal Bit  | 17   | 16  15                 | 14                     | 13                     | 12                     | 11                     | 10                     | 07                     | 06                     | 05                     | 04                     | 03                     | 02                     | 01                     |                        | 00                     |
| Read Word 0     | S    | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 |
| Word 1          | S    | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 |
| Word 2          | S    | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 |
| Word 3          | S    | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 |
| Word 4          | S    | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 |
| Word 5          | S    | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 |
| Word 6          | S    | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 |
| Word 7          | S    | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 |
| Word 8          | PU   | Not used - set to zero | Not used - set to zero | Not used - set to zero | Not used - set to zero | Not used - set to zero | Not used - set to zero | U7                     | U6                     | U5                     | U4                     | U3                     |                        | U2                     | U1                     | U0                     |

Where: S = sign bit (in 2's complement)

U = Underrange bits for 420mA inputs

PU = Power up bit

Word/Bit Descriptions for the 1794-IE8 Analog Input Module Read

| Word                   | Decimal Bit (Octal Bit)   | Definition                                                                                                                                                                                                                                                                                                    |
|------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Word 0Read Word 0 | Bits 00-14 (00-16)        | Channel 0 analog data - 12bit left justified two's complement number; Read Word 0 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Read Word 0                                                                                                                                                                                                                                                                                                               |
| Read Word 0Read Word 0 | Bits 15 (17)              | Channel 0 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 1 Word 1                        | Bits 00-14 (00-16)        | Channel 1 analog data - 12bit left justified two's complement number; Word 1 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 1                                                                                                                                                                                                                                                                                                               |
| Word 1 Word 1                        | Bits 15 (17)              | Channel 1 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 2Word 2           | Bits 00-14 (00-16)        | Channel 2 analog data - 12bit left justified two's complement number; Word 2 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 2                                                                                                                                                                                                                                                                                                               |
| Word 2Word 2           | Bits 15 (17)              | Channel 2 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 3 Word 3                        | Bits 00-14 (00-16)        | Channel 3 analog data - 12bit left justified two's complement number; Word 3 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 3                                                                                                                                                                                                                                                                                                               |
| Word 3 Word 3                        | Bits 15 (17)              | Channel 3 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 4Word 4           | Bits 00-14 (00-16)        | Channel 4 analog data - 12bit left justified two's complement number; Word 4 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 4                                                                                                                                                                                                                                                                                                               |
| Word 4Word 4           | Bits 15 (17)              | Channel 4 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 5 Word 5                        | Bits 00-14 (00-16)        | Channel 5 analog data - 12bit left justified two's complement number; Word 5 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 5                                                                                                                                                                                                                                                                                                               |
| Word 5 Word 5                        | Bits 15 (17)              | Channel 5 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 6Word 6           | Bits 00-14 (00-16)        | Channel 6 analog data - 12bit left justified two's complement number; Word 6 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 6                                                                                                                                                                                                                                                                                                               |
| Word 6Word 6           | Bits 15 (17)              | Channel 6 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 7 Word 7                        | Bits 00-14 (00-16)        | Channel 7 analog data - 12bit left justified two's complement number; Word 7 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 7                                                                                                                                                                                                                                                                                                               |
| Word 7 Word 7                        | Bits 15 (17)              | Channel 7 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 8                 | Bits 00-07                | Underrange bits (U) for individual channels (420mA current input only)- Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on. When set (1), indicates either a broken or open input wire, or input current at or below 4mA.                                                                                                                                                                                                                                                                                                               |
| Word 8                 | Bits 0814 (1016)                           | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Word 8                 | Bit 15 (17)               | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register (write word 0) are 0 (unconfigured state). The configuration register can be cleared by either a reset, or by the user writing all zeroes to it. |

## Analog Input Module (1794-IE8/B) Write Configuration Block

| Word/Dec. Bit   | 15   | 14   | 13   | 12   | 11   | 10   | 09   | 08   | 07   | 06   | 05   | 04   | 03   | 02   | 01   | 00   |
|-----------------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| Word/Octal Bit  | 17   | 16   | 15   | 14   | 13   | 12   | 11   | 10   | 07   | 06   | 05   | 04   | 03   | 02   | 01   | 00   |
| Write Word 0    | C7   | C6   | C5   | C4   | C3   | C2   | C1   | C0   | F7   | F6   | F5   | F4   | F3   | F2   | F1   | F0   |

Where: C = Configure select bit

F = Full range bit

## Range Selection Bits for the 1794-IE8/B Analog Input Module

| Channel No.               | Channel 0   | Channel 0   | Channel 1   | Channel 1   | Channel 2   | Channel 2   | Channel 3   | Channel 3   | Channel 4   | Channel 4   | Channel 5   | Channel 5   | Channel 6   | Channel 6   | Channel 7   | Channel 7   |
|---------------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|                           | F0          | C0          | F1          | C1          | F2          | C2          | F3          | C3          | F4          | C4          | F5          | C5          | F6          | C6          | F7          | C7          |
| Decimal Bits (Octal Bits) | 00          | 08 (10)     | 01          | 09 (11)     | 02          | 10 (12)     | 03          | 11 (13)     | 04          | 12 (14)     | 05          | 13 (15)     | 06          | 14 (16)     | 07          | 15 (17)     |
| 0-10V dc/0-20mA           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           |
| 4-20mA                    | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           |
| 10 to +10V dc                           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           |
| Off1                      | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           |

## Word/Bit Descriptions for the 1794-IE8/B Analog Input Module Write

| Word         | Decimal Bit (Octal Bit)   | Definition                                                                                                                                                                  |
|--------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Write Word 0 | Bits 00-07                | Full range bits (F) for individual channels - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on.                                      |
| Write Word 0 | Bits 08-15 (1017)                           | Configure select bits (C) for individual channels - Bit 08 corresponds to input channel 0, bit 09 corresponds to input channel 1, and so on. Refer to Range Bit Selections. |

## 4 Output Analog Module (Cat. No. 1794OE4 Series B)

<!-- image -->

Analog Output Module (1794-OE4/B) Read

| Word/Dec. Bit   | 15   | 14                  | 13                  | 12                  | 11                  | 10                  | 09                  | 08                  | 07                  | 06                  | 05                  | 04                  | 03   | 02   | 01   | 00   |
|-----------------|------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|------|------|------|------|
| Word/Octal Bit  | 17   | 16                  | 15                  | 14                  | 13                  | 12                  | 11                  | 10                  | 07                  | 06                  | 05                  | 04                  | 03   | 02   | 01   | 00   |
| Read Word 0     | PU   | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | W3   | W2   | W1   | W0   |

PU = Power up bit

Bit/Word Descriptions for the 1794-OE4/B Analog Output Module Read

| Word   | Decimal Bit (Octal Bit)   | Definition                                                                                                                                                                                                                                                                                                    |
|--------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Word 0 Word 0 Word 0 Word 0        | Bits 0003                           | Current outputs only - When set (1), the wire on the output is broken or the load resistance is too high. Bit 00 corresponds to channel 0, bit 01 corresponds to channel 2, and so on.                                                                                                                        |
| Read Word 0 Word 0 Word 0 Word 0        | Bits 0414 (04-16)                           | Not used - set to 0                                                                                                                                                                                                                                                                                           |
| Read Word 0 Word 0 Word 0 Word 0        | Bit 15 (17)               | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register (write word 5) are 0 (unconfigured state). The configuration register can be cleared by either a reset, or by the user writing all zeroes to it. |

## Analog Output Module (1794-OE4/B) Write Configuration Block

| Word/Dec. Bit   | 15                  | 14                           | 13                           | 12                           | 11                           | 10                           | 09                           | 08                           | 07  06                       | 05                           | 04                           | 03                           | 02                           | 01                           | 00                           |
|-----------------|---------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| Word/Octal Bit  | 17                  | 16  15                       | 14                           | 13                           | 12                           | 11                           | 10                           | 07                           | 06                           | 05                           | 04                           | 03                           | 02                           | 01                           | 00                           |
| Write Word 0    | S                   | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      | Analog Data - Channel 0      |
| Word 1          | S                   | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      | Analog Data - Channel 1      |
| Word 2          | S                   | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      | Analog Data - Channel 2      |
| Word 3          | S                   | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      | Analog Data - Channel 3      |
| Word 4          | 0                   | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | M3                           | M2                           | M1                           |                              | M0                           |
| Word 5          | 0                   | Not used - set to 0          | Not used - set to 0          | C3                           | C2                           | C1                           | C0                           |                              | Not used - set to 0          | Not used - set to 0          | F3                           |                              | F2                           | F1                           | F0                           |
| Word 6 thru 9   | Not used - set to 0 | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          |
| Word 10         | S                   | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 | Safe State Value - Channel 0 |
| Word 11         | S                   | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 | Safe State Value - Channel 1 |
| Word 12         | S                   | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 | Safe State Value - Channel 2 |
| Word 13         | S                   | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 | Safe State Value - Channel 3 |

## Range Selection Bits for the 1794-OE4/B Analog Output Module (Word 5)

| Channel No.               | Channel 0   | Channel 0   | Channel 1   | Channel 1   | Channel 2   | Channel 2   | Channel 3   | Channel 3   |
|---------------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|                           | F0          | C0          | F1          | C1          | F2          | C2          | F3          | C3          |
| Decimal Bits (Octal Bits) | 00          | 08 (10)     | 01          | 09 (11)     | 02          | 10 (12)     | 03          | 11 (13)     |
| 4-20mA                    | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           |
| 0-10V dc/0-20mA           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           |
| 10 to +10V dc                           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           |
| Off1                      | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           |

## Word/Bit Descriptions for the 1794-OE4/B Analog Output Module Write

| Word             | Decimal Bit (Octal Bit)   | Definition                      |
|------------------|---------------------------|---------------------------------|
| Write Word 00 00 | Bits 00-14 (00-16)        | Channel 0 analog data - 12bit left justified two's complement number; unused lower bits are zero; 420mA uses all 16 bits.                                 |
| Write Word 00 00 | Bits 15 (17)              | Channel 0 analog data sign bit. |

| Word                      | Decimal Bit (Octal Bit)   | Definition                                                                                                                                     |
|---------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Word 1Word 1              | Bits 00-14 (00-16)        | Channel 1 analog data - 12bit left justified two's complement number; unused Word 1 (00-16)lower bits are zero; 420mA uses all 16 bits. Word 1                                                                                                                                                |
| Word 1Word 1              | Bits 15 (17)              | Channel 1 analog data sign bit.                                                                                                                |
| Word 2 Word 2                           | Bits 00-14 (00-16)        | Channel 2 analog data - 12bit left justified two's complement number; unused Word 2 (00-16)lower bits are zero; 420mA uses all 16 bits. Word 2                                                                                                                                                |
| Word 2 Word 2                           | Bits 15 (17)              | Channel 2 analog data sign bit.                                                                                                                |
| Word 3Word 3              | Bits 00-14 (00-16)        | Channel 3 analog data - 12bit left justified two's complement number; unused Word 3 (00-16)lower bits are zero; 420mA uses all 16 bits. Word 3                                                                                                                                                |
| Word 3Word 3              | Bits 15 (17)              | Channel 3 analog data sign bit.                                                                                                                |
| Word 4                    | Bits 00-03                | Multiplex control bits (M) for individual channels. These bits control the safe state analog outputs. - Bit 00 corresponds to output channel 0, bit 01 corresponds to output channel 1, and so on. 1 = use words 0, 1, 2 or 3 as directed by channel number n 0 = use words 10, 11, 12 or 13 as directed by channel number n When bits 0003 are all cleared (0) simultaneously by a communication error or user choice thru the programmable controller program, word 5 full range and configure select bits are preserved at their last setting.                                                                                                                                                |
| Word 4                    | Bits 0415 (0417)                           | Not used - set to 0.                                                                                                                           |
| Word 5                    | Bits 00-03                | Full range bits (F) for individual channels - Bit 00 corresponds to output channel 0, bit 01 corresponds to output channel 1, and so on.       |
| Word 5                    | Bits 0407                           | Not used - set to 0.                                                                                                                           |
| Word 5                    | Bits 08-11 (1013)                           | Configure select bits (C) for individual channels - Bit 08 corresponds to output channel 0, bit 09 corresponds to output channel 1, and so on. |
| Word 5                    | Bits 1215 (1417)                           | Not used - set to 0.                                                                                                                           |
| Words 6 thru 9            | Bits 00-15 (00-17)        | Not used - set to 0.                                                                                                                           |
| Word 10 Word 10                           | Bits 00-14 (00-16)        | Channel 0 Safe State analog value - 12bit left justified two's complement Word 10 (00-16)number; unused lower bits are zero; 420mA uses all 16 bits. Word 10                                                                                                                                                |
| Word 10 Word 10                           | Bits 15 (17)              | Channel 0 Safe State analog data sign bit.                                                                                                     |
| Word 11Word 11            | Bits 00-14 (00-16)        | Channel 1 Safe State analog value - 12bit left justified two's complement Word 11 (00-16)number; unused lower bits are zero; 420mA uses all 16 bits. Word 11                                                                                                                                                |
| Word 11Word 11            | Bits 15 (17)              | Channel 1 Safe State analog data sign bit.                                                                                                     |
| Word 12 Word 12                           | Bits 00-14 (00-16)        | Channel 2 Safe State analog value - 12bit left justified two's complement Word 12 (00-16)number; unused lower bits are zero; 420mA uses all 16 bits. Word 12                                                                                                                                                |
| Word 12 Word 12                           | Bits 15 (17)              | Channel 2 Safe State analog data sign bit.                                                                                                     |
| Word 13Word  13 Word Word | Bits 00-14 (00-16)        | Channel 3 Safe State analog value - 12bit left justified two's complement 13 (00-16)number; unused lower bits are zero; 420mA uses all 16 bits. 13                                                                                                                                                |
| Word 13Word  13 Word Word | Bits 15 (17)              | Channel 3 Safe State analog data sign bit.                                                                                                     |

## 4 Input/2 Output Analog Combo Module (Cat. No. 1794IE4XOE2 Series B)

Module Image

<!-- image -->

Analog Combo Module (1794-IE4XOE2/B) Read

| Word/Dec. Bit   | 15   | 14                           | 13                           | 12                           | 11                           | 10                           | 09                           | 08                           | 07                           | 06                           | 05                           | 04                           | 03                           | 02                           | 01                           | 00                           |
|-----------------|------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| Word/Octal Bit  | 17   | 16  15                       | 14                           |                              | 13                           | 12                           | 11                           | 10                           | 07                           | 06                           | 05                           | 04                           | 03                           | 02                           | 01                           | 00                           |
| Read Word 0     | S    | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 |
| Word 1          | S    | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 |
| Word 2          | S    | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 |
| Word 3          | S    | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 |
| Word 4          | PU   | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | W1                           | W0                           |                              | U3                           | U2                           | U1                           | U0                           |

W = Diagnostic bits for current output wire broken or load resistance high. (Not used on voltage outputs.)

U = Underrange bits for 420mA inputs

PU = Power up bit

Word/Bit Descriptions for the 1794-IE4XOE2/B Analog Combo Module Read

| Word         | Decimal Bit (Octal Bit)   | Definition                      |
|--------------|---------------------------|---------------------------------|
| Read Word 0 Word 0 Word 0 Word 0              | Bits 00-14 (00-16)        | Channel 0 analog data - 12bit left justified two's complement number; unused lower bits are zero; 420mA uses all 16 bits.                                 |
| Read Word 0 Word 0 Word 0 Word 0              | Bits 15 (17)              | Channel 0 analog data sign bit. |
| Word 1Word 1 | Bits 00-14 (00-16)        | Channel 1 analog data - 12bit left justified two's complement number; Word 1 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 1                                 |
| Word 1Word 1 | Bits 15 (17)              | Channel 1 analog data sign bit. |
| Word 2 Word 2              | Bits 00-14 (00-16)        | Channel 2 analog data - 12bit left justified two's complement number; Word 2 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 2                                 |
| Word 2 Word 2              | Bits 15 (17)              | Channel 2 analog data sign bit. |

| Word                    | Decimal Bit (Octal Bit)   | Definition                                                                                                                                                                                                                                                                                                    |
|-------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Word 3Word 3            | Bits 00-14 (00-16)        | Channel 3 analog data - 12bit left justified two's complement number; Word 3 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 3                                                                                                                                                                                                                                                                                                               |
| Word 3Word 3            | Bits 15 (17)              | Channel 3 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Word 4Word  4 Word Word | Bits 00-03                | Underrange bits (U) for individual channels (420mA current inputs only) - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on. When set (1), indicates either a broken or open input wire, or input current is at or below 4mA.                                                                                                                                                                                                                                                                                                               |
| Word 4Word  4 Word Word | Bits 0405                           | Wire Off bits (W) - Current outputs only - When set (1), the wire on the current output is broken or the load resistance is too high. Bit 00 corresponds 4 to channel 0, bit 01 corresponds to channel 2, and so on. 4                                                                                                                                                                                                                                                                                                               |
| Word 4Word  4 Word Word | Bits 06-14 (06-16)        | Not used                                                                                                                                                                                                                                                                                                      |
| Word 4Word  4 Word Word | Bit 15 (17)               | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register (write word 3) are 0 (unconfigured state). The configuration register can be cleared by either a reset, or by the user writing all zeroes to it. |

## Analog Combo Module (1794-IE4XOE2/B) Write Configuration Block

| Word/Dec. Bit   | 15                  | 14                                  | 13                                  | 12                                  | 11                                  | 10                                  | 09                                  | 08                                  | 07                                  | 06                                  | 05                                  | 04                                  | 03                                  | 02                                  | 01                                  | 00                                  |
|-----------------|---------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| Word/Octal Bit  | 17                  | 16                                  | 15  14                              |                                     | 13                                  | 12                                  | 11                                  | 10                                  | 07                                  | 06                                  | 05                                  | 04                                  | 03                                  | 02                                  | 01                                  | 00                                  |
| Write Word 0    | S                   | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      | Analog Data - Output Channel 0      |
| Word 1          | S                   | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      | Analog Data - Output Channel 1      |
| Word 2          | 0                   | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | M1                                  | M0                                  |
| Word 3          | Not used            | Not used                            | C5                                  | C4                                  | C3                                  | C2                                  | C1                                  | C0                                  | 0                                   | 0                                   | F5                                  | F4                                  | F3                                  | F2                                  | F1                                  | F0                                  |
| Words 4 and 5   | Not used - set to 0 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 | Not used - set to 0                 |
| Word 6          | S                   | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 | Safe State Value - Output Channel 0 |
| Word 7          | S                   | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 | Safe State Value - Output Channel 1 |

Where: M = Multiplex control bits

S = Sign bit (in 2's complement)

C = Configure select bit

F = Full range bit

Range Selection Bits for the 1794-IE4XOE2/B Analog Combo Module

| Channel No.               | Input Channel 0   | Input Channel 0   | Input Channel 1   | Input Channel 1   | Input Channel 2   | Input Channel 2   | Input Channel 3   | Input Channel 3   | Output Channel 0   | Output Channel 0   | Output Channel 1   | Output Channel 1   |
|---------------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|--------------------|--------------------|--------------------|--------------------|
|                           | F0                | C0                | F1                | C1                | F2                | C2                | F3                | C3                | F4                 | C4                 | F5                 | C5                 |
| Decimal Bits (Octal Bits) | 00                | 08 (10)           | 01                | 09 (11)           | 02                | 10 (12)           | 03                | 11 (13)           | 04                 | 12 (14)            | 05                 | 13 (15)            |
| 4-20mA                    | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                  | 1                  | 0                  | 1                  |
| 0-10V dc/0-20mA           | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                  | 0                  | 1                  | 0                  |
| 10 to +10V dc                           | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                  | 1                  | 1                  | 1                  |
| Off1                      | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                  | 0                  | 0                  | 0                  |

Word/Bit Descriptions for the 1794-IE4XOE2/B Analog Combo Module Write

| Word                      | Decimal Bit (Octal Bit)   | Definition                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Write Write Word 0                           | Bits 00-14 (00-16)        | Channel 0 analog data - 12bit left justified two's complement number; unused Write (00-16)lower bits are zero; 420mA uses all 16 bits. Write                                                                                                                                                                                                                                                                                                                                                             |
| Write Write Word 0                           | Bits 15 (17)              | Channel 0 analog data sign bit.                                                                                                                                                                                                                                                                                                                             |
| Word 1Word 1 Word 1Word 1 | Bits 00-14 (00-16)        | Channel 1 analog data - 12bit left justified two's complement number; unused lower bits are zero; 420mA uses all 16 bits.                                                                                                                                                                                                                                                                                                                                                             |
| Word 1Word 1 Word 1Word 1 | Bits 15 (17)              | Channel 1 analog data sign bit.                                                                                                                                                                                                                                                                                                                             |
| Word 2                    | Bits 00-01                | Multiplex control bits (M) for individual channels. These bits control the safe state analog outputs - Bit 00 corresponds to output channel 0, and bit 01 corresponds to output channel 1. 1 = use words 0 and 1 (analog value) as directed by channel number n 0 = use words 6 and 7 (safe state analog value) as directed by channel number n When bits 0001 are all cleared (0) simultaneously by a communication error or user choice thru the programmable controller program, word 3 full range and configure select bits are preserved at their last setting.                                                                                                                                                                                                                                                                                                                                                             |
| Word 2                    | Bits 02-15 (02-17)        | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                        |
| Word 3                    | Bits 00-05                | Full range bits (F) for individual channels - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, bit 02 corresponds to input channel 3, bit 03 corresponds to input channel 3, bit 04 corresponds to output channel 1, and bit 05 corresponds to output channel 2. Refer to Range Bit Selections.                                |
| Word 3                    | Bits 0607                           | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                        |
| Word 3                    | Bits 08-13 (1015)                           | Configure select bits (C) for individual channels - Bit 08 corresponds to input channel 0, bit 09 (11) corresponds to input channel 1, bit 10 (12) corresponds to input channel 2, bit 11 (13) corresponds to input channel 3, bit 12 (14) corresponds to output channel 0, and bit 13 (15) corresponds to output channel 1. Refer to Range Bit Selections. |
| Word 3                    | Bits 1415 (1617)                           | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                        |

| Word                    | Decimal Bit (Octal Bit)   | Definition                                 |
|-------------------------|---------------------------|--------------------------------------------|
| Words 4 and 5           |                           | Not used - set to 0.                       |
| Word 6 Word 6                         | Bits 00-14 (00-16)        | Channel 0 Safe State analog value - 12bit left justified two's complement number; Word 6 (00-16)unused lower bits are zero; 420mA uses all 16 bits. Word 6                                            |
| Word 6 Word 6                         | Bits 15 (17)              | Channel 0 Safe State analog data sign bit. |
| Word 7Word  7 Word Word | Bits 00-14 (00-16)        | Channel 1 Safe State analog value - 12bit left justified two's complement number; 7 (00-16)unused lower bits are zero; 420mA uses all 16 bits. 7                                            |
| Word 7Word  7 Word Word | Bits 15 (17)              | Channel 1 Safe State analog data sign bit. |

## Chapter Summary

In this chapter you learned how to configure your module's features and enter your data.

## Chapter Objectives

## About DeviceNet Manager

<!-- image -->

## Polled I/O Structure

## How Communication Takes Place and I/O Image Table Mapping with the DeviceNet Adapter

In this chapter you will learn about:

- DeviceNet Manager software
- I/O structure
- image table mapping
- factory defaults

DeviceNet Manager is a software tool used to configure your FLEX I/O DeviceNet adapter and its related modules. This software tool can be connected to the adapter via the DeviceNet network.

You must know and understand how DeviceNet Manager works in order to add a device to the network. Refer to the DeviceNet Manager Software User Manual, publication 1787-6.5.3.

Output data is received by the adapter in the order of the installed I/O modules. The Output data for Slot 0 is received first, followed by the Output data for Slot 1, and so on up to slot 7.

The first word of input data sent by the adapter is the Adapter Status Word. This is followed by the input data from each slot, in the order of the installed I/O modules. The Input data from Slot 0 is first after the status word, followed by Input data from Slot 2, and so on up to slot 7.

## DeviceNet Adapter

<!-- image -->

## Adapter Input Status Word

The input status word consists of:

- I/O module fault bits – 1 status bit for each slot
- node address changed – 1 bit
- I/O status – 1 bit

<!-- image -->

The adapter input status word bit descriptions are shown in the following table.

| Bit Description                                                    | Bit        | Explanation                                                                               |
|--------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------|
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 0          | This bit is set (1) when an error is detected in slot position 0.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 1          | This bit is set (1) when an error is detected in slot position 1.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 2          | This bit is set (1) when an error is detected in slot position 2.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 3          | This bit is set (1) when an error is detected in slot position 3.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 4          | This bit is set (1) when an error is detected in slot position 4.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 5          | This bit is set (1) when an error is detected in slot position 5.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 6          | This bit is set (1) when an error is detected in slot position 6.                         |
| I/O Module FaultI/O Module Fault  I/O Module FaultI/O Module Fault | 7          | This bit is set (1) when an error is detected in slot position 7.                         |
| Node Address Changed                                               | 8          | This bit is set (1) when the node address switch setting has been changed since power up. |
| I/O State                                                          | 9          | Bit = 0 - idle Bit = 1 - run                                                              |
| I/O State                                                          | 10 thru 15 | Not used - sent as zeroes.                                                                |

## Possible causes for an I/O Module Fault are:

- transmission errors on the FLEX I/O backplane
- a failed module
- a module removed from its terminal base
- incorrect module inserted in a slot position
- the slot is empty

The node address changed bit is set when the node address switch setting has been changed since power up. The new node address does not take affect until the adapter has been powered down and then powered back up.

## Mapping Data into the Image Table

FLEX I/O analog modules are supported by the DeviceNet adapter . At present, these consist of:

| Module Description             | Catalog Number:   | For image table mapping refer to:   |
|--------------------------------|-------------------|-------------------------------------|
| 8 Input Analog Module          | 1794IE8/B                   | page 5-3                            |
| 4 Output Analog Module         | 1794OE4/B                   | page 5-6                            |
| 4 in/2 out Analog Combo Module | 1794IE4XOE2/B                   | page 5-9                            |

## 8 Input Analog Module (Cat. No. 1794IE8 Series B) Image Table Mapping

<!-- image -->

Analog Input Module (1794-IE8/B) Read

| Decimal Bit   | 15   | 14                     | 13                     | 12                     | 11                     | 10                     | 09                     | 08                     | 07                     | 06                     | 05                     | 04                     | 03                     | 02                     | 01                     | 00                     | Size        |
|---------------|------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|-------------|
| Octal Bit     | 17   | 16                     | 15                     | 14                     | 13                     | 12                     | 11                     | 10                     | 07                     | 06                     | 05                     | 04                     | 03                     | 02                     | 01                     | 00                     | Read Words  |
|               | S    | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Analog Value Channel 0 | Read Word 1 |
|               | S    | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Analog Value Channel 1 | Read Word 2 |
|               | S    | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Analog Value Channel 2 | Read Word 3 |
|               | S    | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Analog Value Channel 3 | Read Word 4 |
|               | S    | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Analog Value Channel 4 | Read Word 5 |
|               | S    | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Analog Value Channel 5 | Read Word 6 |
|               | S    | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Analog Value Channel 6 | Read Word 7 |

| Decimal Bit   | 15   | 14                             | 13                             | 12                             | 11                             | 10                             | 09                             | 08                             | 07                             | 06                     | 05                     | 04                     | 03                     | 02                     | 01                     | 00                     | Size        |
|---------------|------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|-------------|
| Octal Bit     | 17   | 16                             | 15                             | 14                             | 13                             | 12                             | 11                             | 10                             | 07                             | 06                     | 05                     | 04                     | 03  02                 | 01                     |                        | 00                     | Read Words  |
|               | S    | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7         | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Analog Value Channel 7 | Read Word 8 |
|               | PU   | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 | Not used - set to zero  U7  U6 |                        | U5                     | U4                     | U3                     | U2                     | U1                     | U0                     | Read Word 9 |

Where: PU = Power up bit - included in series B modules only .

U = Underrange bits for 420mA inputs

S = sign bit (in 2's complement)

## Analog Input Module (1794-IE8/B) Write

| Decimal Bit         | 15                  | 14                  | 13                  | 12                  | 11                  | 10                  | 09                  | 08                  | 07                  | 06                  | 05                  | 04                  | 03                  | 02                  | 01                  | 00                  | Size                |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| Octal Bit           | 17                  | 16                  | 15                  | 14                  | 13                  | 12                  | 11                  | 10                  | 07                  | 06                  | 05                  | 04                  | 03                  | 02                  | 01                  | 00                  | Write Words         |
|                     | C7                  | C6                  | C5                  | C4                  | C3                  | C2                  | C1                  | C0                  | F7                  | F6                  | F5                  | F4                  | F3                  | F2                  | F1                  | F0                  | Write Word 1        |
| Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Write Word 2 thru 6 |

Where: C = Configure select bit

F = Full range bit

## Range Selection Bits for the 1794-IE8/B Analog Input Module

| Channel No.     | Channel 0   | Channel 0   | Channel 1   | Channel 1   | Channel 2   | Channel 2   | Channel 3   | Channel 3   | Channel 4   | Channel 4   | Channel 5   | Channel 5   | Channel 6   | Channel 6   | Channel 7   | Channel 7   |
|-----------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|                 | F0          | C0          | F1          | C1          | F2          | C2          | F3          | C3          | F4          | C4          | F5          | C5          | F6          | C6          | F7          | C7          |
| Decimal Bit     | 00          | 08          | 01          | 09          | 02          | 10          | 03          | 11          | 04          | 12          | 05          | 13          | 06          | 14          | 07          | 15          |
| 0-10V dc/0-20mA | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           |
| 4-20mA          | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           |
| 10 to +10V dc                 | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           |
| Off1            | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           |

## Word/Bit Descriptions for the 1794-IE8/B Analog Input Module

| Word                   | Decimal Bit   | Definition                      |
|------------------------|---------------|---------------------------------|
| Read Word 1 Read Word 1                        | Bits 00-14    | Channel 0 analog data - 12bit left justified two's complement Read Word 1 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 1                                 |
| Read Word 1 Read Word 1                        | Bits 15       | Channel 0 analog data sign bit. |
| Read Word 2Read Word 2 | Bits 00-14    | Channel 1 analog data - 12bit left justified two's complement Read Word 2 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 2                                 |
| Read Word 2Read Word 2 | Bits 15       | Channel 1 analog data sign bit. |
| Read Word 3 Read Word 3                        | Bits 00-14    | Channel 2 analog data - 12bit left justified two's complement Read Word 3 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 3                                 |
| Read Word 3 Read Word 3                        | Bits 15       | Channel 2 analog data sign bit. |
| Read Word 4Read Word 4 | Bits 00-14    | Channel 3 analog data - 12bit left justified two's complement Read Word 4 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 4                                 |
| Read Word 4Read Word 4 | Bits 15       | Channel 3 analog data sign bit. |

| Word                                              | Decimal Bit   | Definition                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Word 5Read Word 5                            | Bits 00-14    | Channel 4 analog data - 12bit left justified two's complement Read Word 5 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 5                                                                                                                                                                                                                                                                                                               |
| Read Word 5Read Word 5                            | Bits 15       | Channel 4 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Read Word 6 Read Word 6                                                   | Bits 00-14    | Channel 5 analog data - 12bit left justified two's complement Read Word 6 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 6                                                                                                                                                                                                                                                                                                               |
| Read Word 6 Read Word 6                                                   | Bits 15       | Channel 5 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Read Word 7Read Word 7                            | Bits 00-14    | Channel 6 analog data - 12bit left justified two's complement Read Word 7 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 7                                                                                                                                                                                                                                                                                                               |
| Read Word 7Read Word 7                            | Bits 15       | Channel 6 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Read Word 8 Read Word 8                                                   | Bits 00-14    | Channel 7 analog data - 12bit left justified two's complement Read Word 8 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 8                                                                                                                                                                                                                                                                                                               |
| Read Word 8 Read Word 8                                                   | Bits 15       | Channel 7 analog data sign bit.                                                                                                                                                                                                                                                                               |
| Read Word 9                                       | Bits 00-07    | Underrange bits (U) for individual channels (420mA current input only)- Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on. When set (1), indicates either a broken or open input wire, or input current at or below 4mA.                                                                                                                                                                                                                                                                                                               |
| Read Word 9                                       | Bits 0814               | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Read Word 9                                       | Bit 15        | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register (write word 1) are 0 (unconfigured state). The configuration register can be cleared by either a reset, or by the user writing all zeroes to it. |
| Write Word 1Write Word 1 Write Word 1Write Word 1 | Bits 00-07    | Full range bits (F) for individual channels - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on. Refer to range selection above.                                                                                                                                        |
| Write Word 1Write Word 1 Write Word 1Write Word 1 | Bits 08-15    | Configure select bits (C) for individual channels - Bit 08 corresponds to input channel 0, bit 09 corresponds to input channel 1, and so on. Refer to range selection above.                                                                                                                                  |
| Write Word 2                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Write Word 3                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Write Word 4                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Write Word 5                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                          |
| Write Word 6                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                          |

## 4 Output Analog Module (1794OE4 Series B) Image Table Mapping

<!-- image -->

Analog Output Module (1794-OE4/B) Read

| Decimal Bit   | 15                      | 14                      | 13                      | 12                      | 11                      | 10                      | 09                      | 08                      | 07                      | 06                      | 05                      | 04     | 03   | 02   | 01  00   | Size        |
|---------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|--------|------|------|----------|-------------|
| Octal Bit     | 17                      | 16  15                  | 14                      | 13                      |                         | 12                      | 11                      | 10                      | 07                      | 06                      | 05                      | 04  03 | 02   | 01   | 00       | Read Words  |
|               | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | PU  Not used - set to 0 | W3     | W2   | W1   | W0       | Read Word 1 |

Where: PU = Power up bit - included in series B modules only .

W = Diagnostic bits for current output wire broken or load resistance high. (Not used on voltage outputs.)

## Analog Output Module (1794-OE4/B) Write

| Decimal Bit   | 15                  | 14                      | 13                      | 12  11                  | 10                      | 09                      | 08                      | 07                      | 06                      | 05                      | 04                      | 03                      | 02                      | 01                      | 00                      | Size         |
|---------------|---------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|--------------|
| Octal Bit     | 17                  | 16                      | 15  14                  | 13                      | 12                      | 11                      | 10                      | 07                      | 06                      | 05                      | 04  03                  | 02                      | 01                      | 00                      |                         | Read Words   |
|               | S                   | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Analog Data - Channel 0 | Write Word 1 |
|               | S                   | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Analog Data - Channel 1 | Write Word 2 |
|               | S                   | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Analog Data - Channel 2 | Write Word 3 |
|               | S                   | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Analog Data - Channel 3 | Write Word 4 |
|               | Not used - set to 0 | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | Not used - set to 0     | OE3                     | OE2                     | OE1                     |                         | OE0                     | Write Word 5 |
|               | Not used - set to 0 | Not used - set to 0     | Not used - set to 0     | C3                      | C2                      | C1                      | C0                      |                         | Not used - set to 0     | Not used - set to 0     | F3                      |                         | F2                      | F1                      | F0                      | Write Word 6 |

| Decimal Bit         | 15                  | 14                  | 13                  | 12                  | 11                  | 10                  | 09                  | 08                  | 07                  | 06                  | 05                  | 04                  | 03                  | 02                  | 01                  | 00                  | Size                  |
|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|-----------------------|
| Octal Bit  17       |                     | 16  15              | 14                  | 13                  | 12                  |                     | 11                  | 10                  | 07                  | 06                  | 05                  | 04  03              | 02                  | 01                  | 00                  |                     | Read Words            |
| Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Not used - set to 0 | Write Words 7 thru 14 |

## Range Selection Bits for the 1794-OE4/B Analog Output Module (Write Word 6)

| Channel No.     | Channel 0   | Channel 0   | Channel 1   | Channel 1   | Channel 2   | Channel 2   | Channel 3   | Channel 3   |
|-----------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|                 | F0          | C0          | F1          | C1          | F2          | C2          | F3          | C3          |
| Decimal Bit     | 00          | 08          | 01          | 09          | 02          | 10          | 03          | 11          |
| 4-20mA          | 0           | 1           | 0           | 1           | 0           | 1           | 0           | 1           |
| 0-10V dc/0-20mA | 1           | 0           | 1           | 0           | 1           | 0           | 1           | 0           |
| 10 to +10V dc                 | 1           | 1           | 1           | 1           | 1           | 1           | 1           | 1           |
| Off1            | 0           | 0           | 0           | 0           | 0           | 0           | 0           | 0           |

## Word/Bit Descriptions for the 1794-OE4/B Analog Output Module

| Word                     | Decimal Bit   | Definition                                                                                                                                                                                                                                                                                                                |
|--------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Word 1              | Bits 0003               | Current outputs only - When set (1), the wire on the output is broken or the load resistance is too high. Bit 00 corresponds to channel 0, bit 01 corresponds to channel 2, and so on.                                                                                                                                    |
| Read Word 1              | Bits 0414               | Not used - set to 0.                                                                                                                                                                                                                                                                                                      |
| Read Word 1              | Bit 15        | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register (write word 6) are 0 (unconfigured state). The configuration register can be cleared by either of the reset inputs, or by the user writing all zeroes to it. |
| Write Word 1Write Word 1 | Bits 00-14    | Channel 0 analog data - 12bit left justified two's complement Write Word 1 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 1                                                                                                                                                                                                                                                                                                                           |
| Write Word 1Write Word 1 | Bits 15       | Channel 0 analog data sign bit.                                                                                                                                                                                                                                                                                           |
| Write Word 2 Write Word 2                          | Bits 00-14    | Channel 1 analog data - 12bit left justified two's complement Write Word 2 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 2                                                                                                                                                                                                                                                                                                                           |
| Write Word 2 Write Word 2                          | Bits 15       | Channel 1 analog data sign bit.                                                                                                                                                                                                                                                                                           |
| Write Word 3Write Word 3 | Bits 00-14    | Channel 2 analog data - 12bit left justified two's complement Write Word 3 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 3                                                                                                                                                                                                                                                                                                                           |
| Write Word 3Write Word 3 | Bits 15       | Channel 2 analog data sign bit.                                                                                                                                                                                                                                                                                           |
| Write Word 4 Write Word 4                          | Bits 00-14    | Channel 3 analog data - 12bit left justified two's complement Write Word 4 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 4                                                                                                                                                                                                                                                                                                                           |
| Write Word 4 Write Word 4                          | Bits 15       | Channel 3 analog data sign bit.                                                                                                                                                                                                                                                                                           |

| Word                                              | Decimal Bit   | Definition                                                                                                                                                                       |
|---------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Write Word 5                                      | Bits 00-03    | Output Enable bits. Bit 00 corresponds to input 0, bit 01 corresponds to input 1, bit 02 corresponds to input 2, and bit 03 corresponds to input 3. These bits must be set to 1. |
| Write Word 5                                      | Bits 0415               | Not used - set to 0.                                                                                                                                                             |
| Write Word 6Write Word 6 Write Word 6Write Word 6 | Bits 00-03    | Full range bits (F) for individual channels - Bit 00 corresponds to output channel 0, bit 01 corresponds to output channel 1, and so on. Refer to range selection above.         |
| Write Word 6Write Word 6 Write Word 6Write Word 6 | Bits 0407               | Not used - set to 0.                                                                                                                                                             |
| Write Word 6Write Word 6 Write Word 6Write Word 6 | Bits 08-11    | Configure select bits (C) for individual channels - Bit 08 corresponds to output channel 0, bit 09 corresponds to output channel 1, and so on. Refer to range selection above.   |
| Write Word 6Write Word 6 Write Word 6Write Word 6 | Bits 1215               | Not used - set to 0.                                                                                                                                                             |
| Write Word 7                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 8                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 9                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 10                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 11                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 12                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 13                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |
| Write Word 14                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                             |

## Analog Combo Module (1794IE4XOE2 Series B) Image Table Mapping

## Module Image

<!-- image -->

Analog Combo Module (1794-IE4XOE2/B) Read

| Decimal Bit   | 15   | 14                           | 13                           | 12                           | 11                           | 10                           | 09                           | 08                           | 07                           | 06                           | 05                           | 04                           | 03                           | 02                           | 01                           | 00                           | Size        |
|---------------|------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|-------------|
| Octal Bit     | 17   | 16                           | 15                           | 14                           | 13                           | 12                           | 11                           | 10                           | 07                           | 06                           | 05                           | 04                           | 03  02                       |                              | 01                           | 00                           | Read Words  |
|               | S    | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Analog Value Input Channel 0 | Read Word 1 |
|               | S    | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Analog Value Input Channel 1 | Read Word 2 |
|               | S    | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Analog Value Input Channel 2 | Read Word 3 |
|               | S    | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Analog Value Input Channel 3 | Read Word 4 |
|               | PU   | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | Not used - set to 0          | W1                           | W0                           |                              | U3                           | U2                           | U1                           | U0                           | Read Word 5 |

## Analog Output Module (1794-IE4XOE2/B) Write

<!-- image -->

| Decimal Bit   | 15                  | 14                             | 13                             | 12                             | 11                             | 10                             | 09                             | 08                             | 07                             | 06                             | 05                             | 04                             | 03                             | 02                             | 01                             | 00                             | Size                 |
|---------------|---------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|----------------------|
| Octal Bit     | 17                  | 16                             | 15                             | 14                             | 13                             | 12                             | 11                             | 10                             | 07                             | 06                             | 05                             | 04                             | 03                             | 02                             | 01                             | 00                             | Read Words           |
|               | S                   | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Analog Data - Output Channel 0 | Write Word 1         |
|               | S                   | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Analog Data - Output Channel 1 | Write Word 2         |
|               | Not used - set to 0 | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | OE1                            | OE0                            | Write Word 3         |
|               | Not used            | Not used                       | C5                             | C4                             | C3                             | C2                             | C1                             | C0                             | 0                              | 0                              | F5                             | F4                             | F3                             | F2                             | F1                             | F0                             | Write Word 4         |
|               | Not used - set to 0 | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Not used - set to 0            | Write Word 5 thru 10 |

## Range Selection Bits for the 1794-IE4XOE2 Analog Combo Module

| Channel No.     | Input Channel 0   | Input Channel 0   | Input Channel 1   | Input Channel 1   | Input Channel 2   | Input Channel 2   | Input Channel 3   | Input Channel 3   | Output Channel 0   | Output Channel 0   | Output Channel 1   | Output Channel 1   |
|-----------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|--------------------|--------------------|--------------------|--------------------|
|                 | F0                | C0                | F1                | C1                | F2                | C2                | F3                | C3                | F4                 | C4                 | F5                 | C5                 |
| Decimal Bit     | 00                | 08                | 01                | 09                | 02                | 10                | 03                | 11                | 04                 | 12                 | 05                 | 13                 |
| 4-20mA          | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                  | 1                  | 0                  | 1                  |
| 0-10V dc/0-20mA | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                 | 0                 | 1                  | 0                  | 1                  | 0                  |
| 10 to +10V dc                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                 | 1                  | 1                  | 1                  | 1                  |
| Off1            | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                 | 0                  | 0                  | 0                  | 0                  |

## Word/Bit Descriptions for the 1794-IE4XOE2 Analog Combo Module

| Word                   | Decimal Bit   | Definition                      |
|------------------------|---------------|---------------------------------|
| Read Word 1 Read Word 1                        | Bits 00-14    | Channel 0 analog data - 12bit left justified two's complement Read Word 1 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 1                                 |
| Read Word 1 Read Word 1                        | Bits 15       | Channel 0 analog data sign bit. |
| Read Word 2Read Word 2 | Bits 00-14    | Channel 1 analog data - 12bit left justified two's complement Read Word 2 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 2                                 |
| Read Word 2Read Word 2 | Bits 15       | Channel 1 analog data sign bit. |
| Read Word 3 Read Word 3                        | Bits 00-14    | Channel 2 analog data - 12bit left justified two's complement Read Word 3 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 3                                 |
| Read Word 3 Read Word 3                        | Bits 15       | Channel 2 analog data sign bit. |
| Read Word 4Read Word 4 | Bits 00-14    | Channel 3 analog data - 12bit left justified two's complement Read Word 4 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Read Word 4                                 |
| Read Word 4Read Word 4 | Bits 15       | Channel 3 analog data sign bit. |

| Word                                              | Decimal Bit   | Definition                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read Word 5 Read Word 5 Read Word 5 Read Word 5                                                   | Bits 00-03    | Underrange bits (U) for individual channels (420mA current inputs only) - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, and so on.                                                                                                                                                                                                                                                                                                                                                              |
| Read Word 5 Read Word 5 Read Word 5 Read Word 5                                                   | Bits 0405               | Wire Off bits (W) - Current outputs only - When set (1), the wire on the current output is broken or the load resistance is too high. Bit 00 corresponds to channel 0, bit 01 corresponds to channel 2, and so on.                                                                                                                                           |
| Read Word 5 Read Word 5 Read Word 5 Read Word 5                                                   | Bits 06-14    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Read Word 5 Read Word 5 Read Word 5 Read Word 5                                                   | Bit 15        | Power Up bit - included in series B modules only. This bit is always 0 in series A modules. This bit is set to 1 when all bits in the configuration register are 0 (unconfigured state). The configuration register can be cleared by either a reset input, or by the user writing all zeroes to it.                                                         |
| Write Word 1Write Word 1                          | Bits 00-14    | Channel 0 analog data - 12bit left justified two's complement Write Word 1 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 1                                                                                                                                                                                                                                                                                                                                                              |
| Write Word 1Write Word 1                          | Bits 15       | Channel 0 analog data sign bit.                                                                                                                                                                                                                                                                                                                              |
| Write Word 2 Write Word 2                                                   | Bits 00-14    | Channel 1 analog data - 12bit left justified two's complement Write Word 2 Bits 0014  number; unused lower bits are zero; 420mA uses all 16 bits. Write Word 2                                                                                                                                                                                                                                                                                                                                                              |
| Write Word 2 Write Word 2                                                   | Bits 15       | Channel 1 analog data sign bit.                                                                                                                                                                                                                                                                                                                              |
| Write Word 3Write Word 3                          | Bits 00-01    | Output Enable bits. Bit 00 corresponds to output 0, bit 01 Write Word 3 Bits 0001  corresponds to output 1. These bits must be set to 1. Write Word 3                                                                                                                                                                                                                                                                                                                                                              |
| Write Word 3Write Word 3                          | Bits 02-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 4Write Word 4 Write Word 4Write Word 4 | Bits 00-05    | Full range bits (F) for individual channels - Bit 00 corresponds to input channel 0, bit 01 corresponds to input channel 1, bit 02 corresponds to input channel 3, bit 03 corresponds to input channel 3, bit 04 corresponds to output channel 1, and bit 05 corresponds to output channel 2. Refer to range selection above.                                |
| Write Word 4Write Word 4 Write Word 4Write Word 4 | Bits 06-07    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 4Write Word 4 Write Word 4Write Word 4 | Bits 08-13    | Configure select bits (C) for individual channels - Bit 08 corresponds to input channel 0, bit 09 (11) corresponds to input channel 1, bit 10 (12) corresponds to input channel 2, bit 11 (13) corresponds to input channel 3, bit 12 (14) corresponds to output channel 0, and bit 13 (15) corresponds to output channel 1. Refer to range selection above. |
| Write Word 4Write Word 4 Write Word 4Write Word 4 | Bits 14-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 5                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 6                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 7                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 8                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 9                                      | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Write Word 10                                     | Bits 00-15    | Not used - set to 0.                                                                                                                                                                                                                                                                                                                                         |

## Defaults

<!-- image -->

Each I/O module has default values associated with it. At default, each module will generate inputs/status and expect outputs/configuration.

| Module Defaults for:   | Module Defaults for:    | Factory Defaults   | Factory Defaults   | Real Time Size   | Real Time Size   |
|------------------------|-------------------------|--------------------|--------------------|------------------|------------------|
| Catalog Number         | Description             | Input Default      | Output Default     | Input Default    | Output Default   |
| 1794IE8/B                        | 8pt Analog Input                         | 9                  | 6                  | 8                | 0                |
| 1794OE4/B                        | 4pt Analog Output                         | 1                  | 14                 | 0                | 4                |
| 1794IE4XOE2/B                        | 4 in/2 out Analog Combo | 5                  | 10                 | 4                | 2                |

Factory defaults are the values assigned by the adapter when you:

- first power up the system, and
- no previous stored settings have been applied.

For analog modules, the defaults reflect the actual number of input words/output words. For example, for the 8 input analog module, you have 9 input words, and 6 output words.

You can change the I/O data size for a module by reducing the number of words mapped into the adapter module, as shown in real time sizes."

Real time sizes are the settings that provide optimal real time data to the adapter module.

Analog modules have 15 words assigned to them. This is divided into input words/output words. You can reduce the I/O data size to fewer words to increase data transfer over the backplane. For example, an 8 input analog module has 9 words input/6 words output with factory default. You can reduce the input words to 8 by not using the underrange settings set in word 9. Likewise, you can reduce the write words to 0, thus eliminating the configuration setting and unused words.

For information on using DeviceNet Manager software to configure your adapter, refer to the DeviceNet Manager Software User Manual, publication 1787-6.5.3.

## Specifications

| Specifications - 1794IE8/B Analog Input Module                                                                   | Specifications - 1794IE8/B Analog Input Module                                                                   | Specifications - 1794IE8/B Analog Input Module                                                                                                                  |
|-------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Number of Inputs                                                  | Number of Inputs                                                  | 8 singleended, nonisolated                                                                                                                  |
| Module Location                                                   | Module Location                                                   | Cat. No. 1794TB2, TB3 Terminal Base Unit                                                                                                                  |
| Resolution                                                        | Voltage Current                                                   | 12 bits  unipolar; 11 bits plus sign  bipolar 2.56mV/cnt unipolar; 5.13mV/cnt bipolar 5.13µA/cnt                                                                                                                  |
| Data Format                                                       | Data Format                                                       | left justified 16bit 2's complement                                                                                                                  |
| Conversion Type                                                   | Conversion Type                                                   | Successive approximation                                                                                         |
| Conversion Rate                                                   | Conversion Rate                                                   | 256µs all channels                                                                                               |
| Input Current Terminal                                            | Input Current Terminal                                            | 420mA (user configurable) 020mA (user configurable)                                                                                                                  |
| Input Voltage Terminal                                            | Input Voltage Terminal                                            | ±10V (user configurable) 010V (user configurable)                                                                                                                  |
| Normal Mode Rejection Ratio                                       | Voltage Terminal Current Terminal                                 | -3db @ 17Hz; -20db/decade -10.0dB @ 50Hz, -11.4dB @ 60Hz -3db @ 9Hz; -20db/decade -15.3dB @ 50Hz, -16.8dB @ 60Hz |
| Step Response to 63%                                              | Voltage Terminal Current Terminal                                 | 9.4ms 18.2ms                                                                                                     |
| Input Impedance Voltage Terminal Current Terminal                 | Input Impedance Voltage Terminal Current Terminal                 | 100k ohms 238 ohms                                                                                               |
| Input Resistance                                                  | Voltage Terminal Current Terminal                                 | 200k ohms 238 ohms                                                                                               |
| Absolute Accuracy 1 Voltage Terminal Current Terminal             | Absolute Accuracy 1 Voltage Terminal Current Terminal             | 0.29% Full Scale @ 25oC 0.29% Full Scale @ 25oC                                                                  |
| Accuracy Drift with Temperature Voltage Terminal Current Terminal | Accuracy Drift with Temperature Voltage Terminal Current Terminal | 0.00428% Full Scale/oC 0.00407% Full Scale/oC                                                                    |
| Calibration                                                       | Calibration                                                       | None Required                                                                                                    |
| Maximum Overload                                                  | Maximum Overload                                                  | 30V continuous or 32mA continuous, one channel at a time                                                         |
| Isolation Voltage                                                 | Isolation Voltage                                                 | Tested at 850V dc for 1s between user and system No isolation between individual channels                        |
| Indicators                                                        | Indicators                                                        | 1 green power indicator                                                                                          |
| Flexbus Current                                                   | Flexbus Current                                                   | 20mA                                                                                                             |
| Power Dissipation                                                 | Power Dissipation                                                 | 3W maximum @ 31.2V dc                                                                                            |
| Thermal Dissipation                                               | Thermal Dissipation                                               | Maximum 10.2 BTU/hr @ 31.2V dc                                                                                   |
| Keyswitch Position                                                | Keyswitch Position                                                | 3                                                                                                                |
| Specifications continued on next page.                            | Specifications continued on next page.                            |                                                                                                                  |

<!-- image -->

| Specifications - 1794IE8/B Analog Input Module                                                                                                                  | Specifications - 1794IE8/B Analog Input Module                                                            | Specifications - 1794IE8/B Analog Input Module                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| General Specifications                                                                                           | General Specifications                                     | General Specifications                                                                                                           |
| External dc Power                                                                                                | Supply Voltage Voltage Range Supply Current                | 24V dc nominal 19.2 to 31.2V dc (includes 5% ac ripple) 60mA @ 24V dc                                                            |
| Dimensions Inches                                                                                                | (Millimeters)                                              | 1.8H x 3.7W x 2.1D (45.7 x 94.0 x 53.3)                                                                                          |
| Environmental Conditions Operational Temperature Storage Temperature Relative Humidity Shock Operating Vibration | Nonoperating                                                            | 0 to 55oC (32 to 131 o F) -40 to 85oC (-40 to 185 o F) 5 to 95% noncondensing (operating) 5 to 80% noncondensing (nonoperating) 30 g peak acceleration, 11(+1)ms pulse width 50 g peak acceleration, 11(+1)ms pulse width Tested 5 g @ 10-500Hz per IEC 6826                                                                                                                                  |
| Conductors Wire Size                                                                                             | Category                                                   | 12 gauge (4mm 2 ) stranded maximum 3/64 inch (1.2mm) insulation maximum 22                                                       |
| Agency Certification (when product or packaging is marked)                                                       | Agency Certification (when product or packaging is marked) | •  CSA certified •  CSA Class I, Division 2, Groups A, B, C, D certified •  UL listed •  CE marked for all applicable directives |
| Installation Instruction                                                                                         | Installation Instruction                                   | Publication 17945.6                                                                                                                                  |

| Specifications - 1794OE4/B Analog Output Module                                                                   | Specifications - 1794OE4/B Analog Output Module                                                                                           |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Number of Outputs                                                 | 4 singleended, nonisolated                                                                                           |
| Module Location                                                   | Cat. No. 1794TB2, TB3 Terminal Base Unit                                                                                           |
| Resolution Voltage Current                                        | 12 bits plus sign 2.56mV/cnt 5.13µA/cnt                                                   |
| Data Format                                                       | left justified 16bit 2's complement                                                                                           |
| Conversion Type                                                   | Pulse Width Modulation                                                                    |
| Conversion Rate                                                   | 1.024ms maximum all channels                                                              |
| Output Current Terminal                                           | 0mA output until module is configured 420mA user configurable 020mA user configurable                                                                                           |
| Output Voltage Terminal                                           | 0V output until module is configured ±10V user configurable 0-10V user configurable       |
| Step Response to 63% of FS                                        | 24ms                                                                                      |
| Current Load on Voltage Output                                    | 3mA maximum                                                                               |
| Resistive Load on mA Output                                       | 15  750 ohms                                                                                           |
| Absolute Accuracy Voltage Terminal Current Terminal               | 0.133% Full Scale @ 25oC 0.425% Full Scale @ 25oC                                         |
| Accuracy Drift with Temperature Voltage Terminal Current Terminal | 0.0045% Full Scale/oC 0.0069% Full Scale/oC                                               |
| Calibration                                                       | None Required                                                                             |
| Isolation Voltage                                                 | Tested at 850V dc for 1s between user and system No isolation between individual channels |
| Indicators                                                        | 1 green power indicator                                                                   |
| Flexbus Current                                                   | 20mA                                                                                      |
| Power Dissipation                                                 | 4.5W maximum @ 31.2V dc                                                                   |
| Thermal Dissipation                                               | Maximum 15.3 BTU/hr @ 31.2V dc                                                            |
| Keyswitch Position                                                | 4                                                                                         |
| Specifications continued on next page.                            | Specifications continued on next page.                                                    |

| Specifications - 1794OE4/B Analog Output Module                                                                                                                  | Specifications - 1794OE4/B Analog Output Module                                                               | Specifications - 1794OE4/B Analog Output Module                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| General Specifications                                                                                           | General Specifications                                        | General Specifications                                                                                                           |
| External dc Power Supply Voltage Voltage Range Supply Current                                                    | External dc Power Supply Voltage Voltage Range Supply Current | 24V dc nominal 19.2 to 31.2V dc (includes 5% ac ripple) 70mA @ 24V dc (not including outputs)                                    |
| Dimensions Inches                                                                                                | (Millimeters)                                                 | 1.8H x 3.7W x 2.1D (45.7 x 94.0 x 53.3)                                                                                          |
| Environmental Conditions Operational Temperature Storage Temperature Relative Humidity Shock Operating Vibration | Nonoperating                                                               | 0 to 55oC (32 to 131 o F) -40 to 85oC (-40 to 185 o F) 5 to 95% noncondensing (operating) 5 to 80% noncondensing (nonoperating) 30 g peak acceleration, 11(+1)ms pulse width 50 g peak acceleration, 11(+1)ms pulse width Tested 5 g @ 10-500Hz per IEC 6826                                                                                                                                  |
| Conductors Wire Size                                                                                             | Category                                                      | 12 gauge (4mm 2 ) stranded maximum 3/64 inch (1.2mm) insulation maximum 22                                                       |
| Agency Certification (when product or packaging is marked)                                                       | Agency Certification (when product or packaging is marked)    | •  CSA certified •  CSA Class I, Division 2, Groups A, B, C, D certified •  UL listed •  CE marked for all applicable directives |
| Installation Instruction                                                                                         | Installation Instruction                                      | Publication 17945.5                                                                                                                                  |

| Specifications - 1794IE4XOE2/B 4 Input/2 Output Analog Combo Module                                                                   | Specifications - 1794IE4XOE2/B 4 Input/2 Output Analog Combo Module                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Input Specifications                                              | Input Specifications                                                                                             |
| Number of Inputs                                                  | 4 singleended, nonisolated                                                                                                                  |
| Resolution Voltage Current                                        | 12 bits  unipolar; 11 bits plus sign  bipolar 2.56mV/cnt unipolar; 5.13mV/cnt bipolar 5.13µA/cnt                                                                                                                  |
| Data Format                                                       | left justified 16bit 2's complement                                                                                                                  |
| Conversion Type                                                   | Successive approximation                                                                                         |
| Conversion Rate                                                   | 256µs all channels                                                                                               |
| Input Current Terminal                                            | 420mA (user configurable) 020mA (user configurable)                                                                                                                  |
| Input Voltage Terminal                                            | ±10V (user configurable) 010V (user configurable)                                                                                                                  |
| Normal Mode Rejection Ratio Voltage Terminal Current Terminal     | -3db @ 17Hz; -20db/decade -10.0dB @ 50Hz, -11.4dB @ 60Hz -3db @ 9Hz; -20db/decade -15.3dB @ 50Hz, -16.8dB @ 60Hz |
| Step Response to 63% Voltage Terminal Current Terminal            | 9.4ms 18.2ms                                                                                                     |
| Input Impedance Voltage Terminal Current Terminal                 | 100k ohms 238 ohms                                                                                               |
| Input Resistance Voltage Terminal Current Terminal                | 200k ohms 238 ohms                                                                                               |
| Absolute Accuracy 1 Voltage Terminal Current Terminal             | 0.29% Full Scale @ 25oC 0.29% Full Scale @ 25oC                                                                  |
| Accuracy Drift with Temperature Voltage Terminal Current Terminal | 0.00428% Full Scale/oC 0.00407% Full Scale/oC                                                                    |
| Maximum Overload                                                  | 30V continuous or 32mA continuous, one channel at a time                                                         |
| Output Specifications                                             | Output Specifications                                                                                            |
| Number of Outputs                                                 | 2 singleended, nonisolated                                                                                                                  |
| Resolution Voltage Current                                        | 12 bits plus sign 2.56mV/cnt 5.13µA/cnt                                                                          |
| Data Format                                                       | left justified 16bit 2's complement                                                                                                                  |
| Conversion Type                                                   | Pulse Width Modulation                                                                                           |
| Conversion Rate                                                   | 1.024ms maximum all channels                                                                                     |
| Output Current Terminal                                           | 0mA output until module is configured 420mA user configurable 020mA user configurable                                                                                                                  |
| Output Voltage Terminal                                           | 0V output until module is configured ±10V user configurable 0-10V user configurable                              |
| Step Response to 63% of FS                                        | 24ms                                                                                                             |
| Specifications continued on next page.                            | Specifications continued on next page.                                                                           |

| Specifications - 1794IE4XOE2/B 4 Input/2 Output Analog Combo Module                                                                   | Specifications - 1794IE4XOE2/B 4 Input/2 Output Analog Combo Module                                                                                                                                  |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Current Load on Voltage Output                                    | 3mA maximum                                                                                                                      |
| Resistive Load on mA Output                                       | 15  750 ohms                                                                                                                                  |
| Absolute Accuracy 1 Voltage Terminal Current Terminal             | 0.133% Full Scale @ 25oC 0.425% Full Scale @ 25oC                                                                                |
| Accuracy Drift with Temperature Voltage Terminal Current Terminal | 0.0045% Full Scale/oC 0.0069% Full Scale/oC                                                                                      |
| General Specifications                                            | General Specifications                                                                                                           |
| Module Location                                                   | Cat. No. 1794TB2, TB3 Terminal Base Unit                                                                                                                                  |
| Flexbus Current                                                   | 20mA                                                                                                                             |
| Power Dissipation                                                 | 4.0W maximum @ 31.2V dc                                                                                                          |
| Thermal Dissipation                                               | Maximum 13.6 BTU/hr @ 31.2V dc                                                                                                   |
| Keyswitch Position                                                | 5                                                                                                                                |
| Calibration                                                       | None Required                                                                                                                    |
| Indicators                                                        | 1 green power indicator                                                                                                          |
| Isolation Voltage                                                 | Tested at 850V dc for 1s between user and system No isolation between individual channels                                        |
| External dc Power Supply Voltage Voltage Range Supply Current     | 24V dc nominal 19.2 to 31.2V dc (includes 5% ac ripple) 70mA @ 24V dc                                                            |
| Dimensions Inches (Millimeters)                                   | 1.8H x 3.7W x 2.1D (45.7 x 94.0 x 53.3)                                                                                          |
| Environmental Conditions Operational Temperature Storage Temperature Relative Humidity Shock Operating Nonoperating Vibration                                                                   | 0 to 55oC (32 to 131 o F) -40 to 85oC (-40 to 185 o F) 5 to 95% noncondensing (operating) 5 to 80% noncondensing (nonoperating) 30 g peak acceleration, 11(+1)ms pulse width 50 g peak acceleration, 11(+1)ms pulse width Tested 5 g @ 10-500Hz per IEC 6826                                                                                                                                  |
| Conductors Wire Size Category                                     | 12 gauge (4mm 2 ) stranded maximum 3/64 inch (1.2mm) insulation maximum 22                                                       |
| Agency Certification (when product or packaging is marked)        | •  CSA certified •  CSA Class I, Division 2, Groups A, B, C, D certified •  UL listed •  CE marked for all applicable directives |
| Installation Instruction                                          | Publication 17945.15                                                                                                                                  |

- 1 Includes offset, gain, nonlinearity and repeatability error terms.

2 Use this conductor category information for planning conductor routing as described in publication 17704.1, Wiring and Grounding Guidelines for Noise Immunity."

x

## Differences Between Series A and Series B Analog Modules

The following lists major differences between series A and series B analog modules.

| Catalog Number   | Description                                                | Series A                                                                                                                    | Series B                                                                                                                         |
|------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1794IE8, 1794OE4, 1794IE4XOE2                  | Power Up bit in Read Word                                  | None                                                                                                                        | This bit is set when all bits in the configuration register are 0 (unconfigured state).                                          |
| 1794IE8, 1794OE4, 1794IE4XOE2                  | Change to range selection tables                           | No off position available. Module produces either 2V or 4mA, dependent upon the range selected, until module is configured. | Off position now produces 0V or 0mA, dependent upon range selected, until module is configured.                                  |
| Specifications   | Specifications                                             | Specifications                                                                                                              | Specifications                                                                                                                   |
| 1794OE4                  | Output Current Terminal                                    | 4mA output until module is configured 420mA user configurable 020mA user configurable                                                                                                                             | 0mA output until module is configured 420mA user configurable 020mA user configurable                                                                                                                                  |
| 1794OE4                  | Output Voltage Terminal                                    | 2V output until module is configured ±10V user configurable 0-10V user configurable                                         | 0V output until module is configured ±10V user configurable 0-10V user configurable                                              |
| 1794IE4XOE2                  | Output Current Terminal                                    | 4mA output until module is configured 420mA user configurable 020mA user configurable                                                                                                                             | 0mA output until module is configured 420mA user configurable 020mA user configurable                                                                                                                                  |
| 1794IE4XOE2                  | Output Voltage Terminal                                    | 2V output until module is configured ±10V user configurable 0-10V user configurable                                         | 0V output until module is configured ±10V user configurable 0-10V user configurable                                              |
| 1794IE8, 1794OE4, 1794IE4XOE2                  | Agency Certification (when product or packaging is marked) | •  CSA certified •  CSA Class I, Division 2, Groups A, B, C, D certified •  UL listed                                       | •  CSA certified •  CSA Class I, Division 2, Groups A, B, C, D certified •  UL listed •  CE marked for all applicable directives |

<!-- image -->

## Two's Complement Binary

## Data Table Formats

Two's complement binary is used when performing mathematical calculations internal to the processor. To complement a number means to change it to a negative number. For example, the following binary number is equal to decimal 22.

<!-- formula-not-decoded -->

First, the two's complement method places an extra bit (sign bit) in the left–most position, and lets this bit determine whether the number is positive or negative. The number is positive if the sign bit is 0 and negative if the sign bit is 1. Using the complement method:

<!-- formula-not-decoded -->

To get the negative using the two's complement method, you must invert each bit from right to left after the first "1" is detected.

In the above example:

<!-- formula-not-decoded -->

Its two's complement would be:

<!-- formula-not-decoded -->

Note that in the above representation for +22, starting from the right, the first digit is a 0 so it is not inverted; the second digit is a 1 so it is not inverted. All digits after this one are inverted.

If a negative number is given in two's complement, its complement (a positive number) is found in the same way:

<!-- formula-not-decoded -->

0 01110 = +14

All bits from right to left are inverted after the first "1" is detected.

The two's complement of 0 is not found, since no first "1" is ever encountered in the number. The two's complement of 0 then is still 0.

x

<!-- image -->

## Analog Data Format

The data returned from the analog-to-digital converter in the module is 12-bit resolute. This value is left-justified into a 16-bit field, reserving the most significant bit for a sign bit.

<!-- image -->

| Current (mA)  Current (mA)  Current (mA)  Current (mA)       | 4-20mA Mode  4-20mA Mode  4-20mA Mode  4-20mA Mode      | 0-20mA Mode  0-20mA Mode  0-20mA Mode  0-20mA Mode      | Voltage (V) Voltage (V)  Voltage (V) Voltage (V)        | +10 Volt Mode   | +10 Volt Mode   | 0-10 Volt 0 10 Volt M d  Mod 0-10 Volt 0 10 Volt M d  Mode      |
|-------|------|------|--------|-----------------|-----------------|------|
|       |      |      |        | Input           | Output          |      |
|       |      |      | -10.50 | 8000            | 8000            |      |
| 0.00  |      | 0000 | -10.00 | 8620            | 8618            |      |
| 1.00  |      | 0618 | -9.00  | 9250            | 9248            |      |
| 2.00  |      | 0C30 | -8.00  | 9E80            | 9E78            |      |
| 3.00  |      | 1248 | -7.00  | AAB0            | AAA8            |      |
| 4.00  | 0000 | 1860 | -6.00  | B6E0            | B6D8            |      |
| 5.00  | 0787 | 1E78 | -5.00  | C310            | C310            |      |
| 6.00  | 0F0F | 2490 | -4.00  | CF40            | CF40            |      |
| 7.00  | 1696 | 2AA8 | -3.00  | DB70            | DB70            |      |
| 8.00  | 1E1E | 30C0 | -2.00  | E7A0            | E7A0            |      |
| 9.00  | 25A5 | 36D8 | -1.00  | F3D0            | F3D0            |      |
| 10.00 | 2D2D | 3CF0 | 0.00   | 0000            | 0000            | 0000 |
| 11.00 | 34B4 | 4310 | 1.00   | 0C30            | 0C30            | 0C30 |
| 12.00 | 3C3C | 4928 | 2.00   | 1860            | 1860            | 1860 |
| 13.00 | 43C3 | 4F40 | 3.00   | 2490            | 2490            | 2490 |
| 14.00 | 4B4B | 5558 | 4.00   | 30C0            | 30C0            | 30C0 |
| 15.00 | 52D2 | 5B70 | 5.00   | 3CF0            | 3CF0            | 3CF0 |
| 16.00 | 5A5A | 6188 | 6.00   | 4920            | 4928            | 4928 |
| 17.00 | 61E1 | 67A0 | 7.00   | 5550            | 5558            | 5558 |
| 18.00 | 6969 | 6DB8 | 8.00   | 6180            | 6188            | 6188 |
| 19.00 | 70F0 | 73D0 | 9.00   | 6DB0            | 6DB8            | 6DB8 |
| 20.00 | 7878 | 79E8 | 10.00  | 79E0            | 79E8            | 79E8 |
| 21.00 | 7FFF | 7FF8 | 10.50  | 7FF0            | 7FF8            | 7FF8 |

## Scaling Example

To scale your data to a different range:

- SLC 500 – use the scaling instruction.
- PLC-5 – determine a constant (slope) by dividing the desired range by the actual range. Multiply the result by your data, and add or subtract any offset.

## Example:

A 4-20mA input places data at N13:0 (Figure 3.4 on page 3–4), with a range of 0 to 30,840. (30,840 = 7878 hex – see data format on page C–2).

You want the 4-20mA (0 to 30,840) to be 32 to 1000 degrees in the PLC-5. Use the following formula:

Scaled Data (degrees) @ N30:0 = {[(Desired Range)/Actual Range] X Analog Input Data} + Offset

<!-- formula-not-decoded -->

## Example using Compute Instructions

This rung will scale FLEX I/O analog data to a different range. In this example, we want the 420mA input data to represent 32 to 1000 degrees in the PLC5. For this example, N13:0 = 30,840 (7878 in hex). Two compute instructions are needed because of the way the destination value will be rounded if we use an integer location instead of floating point in the first compute instruction. The second compute instruction has a final destination of an integer location.

<!-- image -->

## Symbols

**Empty**, P-1 , P-2 , 1-1 , 1-2 , 2-1 , 3-6 , C-1

## Numbers

| 1794IE4XOE2, specifications, A-5   |
|---|
| 1794IE8, specifications, A-1   |
| 1794OE4, specifications, A-3   |

## A

adapter input status word, 5-1 analog mapping 1794IE8, 5-3 1794IE4XOE2, 5-9 1794OE4, 5-6 analog modules, types, 1-2

## B

| bit/word description                         | bit/word description                         | bit/word description                         | bit/word description                         |
|----------------------------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| 4 output analog module, 1794OE4, 5-7                                              | 4 output analog module, 1794OE4, 5-7                                              | 4 output analog module, 1794OE4, 5-7                                              | 4 output analog module, 1794OE4, 5-7                                              |
| 4 output/4 input module, 4-6                 | 4 output/4 input module, 4-6                 | 4 output/4 input module, 4-6                 | 4 output/4 input module, 4-6                 |
| block transfer, 1794IE8, 5-4                                              | block transfer, 1794IE8, 5-4                                              | block transfer, 1794IE8, 5-4                                              |                                              |
| block transfer read                          | block transfer read                          | block transfer read                          | block transfer read                          |
| 1794IE4XOE2,  4-9                                              | 1794IE4XOE2,  4-9                                              | 1794IE4XOE2,  4-9                                              | 1794IE4XOE2,  4-9                                              |
| 1794IE8/B,                                              | 1794IE8/B,                                              |                                              |                                              |
|                                              | 4-4                                          |                                              |                                              |
| 1794OE4/B, 4-6                                              | 1794OE4/B, 4-6                                              |                                              |                                              |
| block transfer write                         | block transfer write                         | block transfer write                         | block transfer write                         |
| 1794IE4XOE2,  4-11                                              | 1794IE4XOE2,  4-11                                              | 1794IE4XOE2,  4-11                                              | 1794IE4XOE2,  4-11                                              |
| 1794IE8/B,  4-5                                              | 1794IE8/B,  4-5                                              | 1794IE8/B,  4-5                                              | 1794IE8/B,  4-5                                              |
| 1794OE4/B,  4-7                                              | 1794OE4/B,  4-7                                              | 1794OE4/B,  4-7                                              | 1794OE4/B,  4-7                                              |
| block transfer                               | block transfer                               | block transfer                               | block transfer                               |
| read,  1-2                                   | read,  1-2                                   | read,  1-2                                   | read,  1-2                                   |
| write,  1-2 block transfer programming,  3-1 | write,  1-2 block transfer programming,  3-1 | write,  1-2 block transfer programming,  3-1 | write,  1-2 block transfer programming,  3-1 |
| 1794OE4/B,  4-6                                              | 1794OE4/B,  4-6                                              | 1794OE4/B,  4-6                                              | 1794OE4/B,  4-6                                              |
| 1794IE4XOE2,                                              | 4-10                                         |                                              |                                              |
| 1794IE8/B, 4-3                                              | 1794IE8/B, 4-3                                              |                                              |                                              |
| 1794OE4/B, 4-6                                              | 1794OE4/B, 4-6                                              |                                              |                                              |
| configuration block, 4-10                    | configuration block, 4-10                    |                                              |                                              |
| 1794IE8/B,                                              | 4-4                                          |                                              |                                              |
| 1794OE4/B,                                              | 4-7                                          |                                              |                                              |

input range selection, 4-2

| C                                               |                                                 |                                                 |
|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| communication, between module and adapter, 1-3  | communication, between module and adapter, 1-3  | communication, between module and adapter, 1-3  |
| configuration block, block transfer write       | configuration block, block transfer write       | configuration block, block transfer write       |
| 1794IE8/B,  4-4                                                 | 1794IE8/B,  4-4                                                 | 1794IE8/B,  4-4                                                 |
| 1794OE4/B,  4-7 configuring features, 4-1                                                 | 1794OE4/B,  4-7 configuring features, 4-1                                                 | 1794OE4/B,  4-7 configuring features, 4-1                                                 |
| connecting wiring, 2-8                          | connecting wiring, 2-8                          | connecting wiring, 2-8                          |
| 1794IE4XOE2,  2-12                                                 | 1794IE4XOE2,  2-12                                                 | 1794IE4XOE2,  2-12                                                 |
| 1794IE8, 2-10                                                 | 1794IE8, 2-10                                                 | 1794IE8, 2-10                                                 |
| 1794OE4, 2-11                                                 | 1794OE4, 2-11                                                 | 1794OE4, 2-11                                                 |
| 1794TB2, TB3, 2-9                                                 | 1794TB2, TB3, 2-9                                                 | 1794TB2, TB3, 2-9                                                 |
| considerations, pre-installation,               | 2-1                                             |                                                 |
| D                                               | D                                               | D                                               |
| daisy-chaining wiring, 2-3 default values, 5-12 | daisy-chaining wiring, 2-3 default values, 5-12 | daisy-chaining wiring, 2-3 default values, 5-12 |
| description adapter,  1-1                       | description adapter,  1-1                       | description adapter,  1-1                       |
| I/O modules,  1-1                               | I/O modules,  1-1                               | I/O modules,  1-1                               |
| differences, series A and series B,  B-1        | differences, series A and series B,  B-1        | differences, series A and series B,  B-1        |
| DIN rail mounting, 2-4                          | DIN rail mounting, 2-4                          | DIN rail mounting, 2-4                          |
| features                                        | features                                        | features                                        |
| configuring,  4-1                               | configuring,  4-1                               | configuring,  4-1                               |
| of the module,  1-4                             | of the module,  1-4                             | of the module,  1-4                             |
| I                                               | I                                               | I                                               |
| indicators, status,  2-13                       | indicators, status,  2-13                       | indicators, status,  2-13                       |
| input ranges,  4-2                              | input ranges,  4-2                              | input ranges,  4-2                              |
| program selectable,  1-2                        | program selectable,  1-2                        | program selectable,  1-2                        |
| input status word,  5-2                         | input status word,  5-2                         | input status word,  5-2                         |
| K                                               | K                                               | K                                               |
| keyswitch positions, 2-7                        | keyswitch positions, 2-7                        | keyswitch positions, 2-7                        |

## L

leftjustified data, 3-6 , 4-2 , C-2

## M

mapping

1794IE8, 5-3

1794IE4XOE2, 5-9

1794OE4, 5-6

memory map - read

1794IE4XOE2, 5-9

1794IE8, 5-3

1794OE4, 5-6

memory map - write

1794IE4XOE2, 5-10

1794IE8, 5-4

1794OE4, 5-6

module features, 1-4

mounting, on terminal base, 2-7

mounting kit, cat. no. 1794NM1, 2-5

## O

optimal defaults, 5-12

## P

panel/wall mounting, 2-5

PLC-2 programming, 3-5

polled I/O, structure, 5-1

power defaults, 5-12

programming example

PLC-3, 3-2

PLC-5, 3-4

## R

range, selecting, 4-2

range selection

1794IE4XOE2, 4-11 , 5-10

1794IE8, 5-4

1794OE4, 5-7

1794IE8/B, 4-5

1794OE4/B, 4-7

removing and replacing, under power (RIUP), 2-8 , 2-9

## S

safe state, selection of, 4-2

sample program, 3-6

specifications

1794IE4XOE2, A-5

1794IE8, A-1

1794OE4, A-3

status indicators, 2-13

## T

terminal base units, recommended, 2-8 terminology used, for module, P-1

## W

wall/panel mounting, 2-5

wiring

methods of, 2-3

to terminal bases, 2-1

wiring connections

1794IE4XOE2, 2-12

1794IE8, 2-10

1794OE4, 2-11

<!-- image -->

## AllenBradley Publication Problem Report

If you find a problem with our documentation, please complete and return this form.

Pub. Name

FLEX I/O Analog Modules User Manual

Cat. No.

Pub. No. Pub. Date Part No.
17946.5.2 May 1996

Check Problem(s) Type:

Describe Problem(s):

Internal Use Only

- [ ] procedure/step

- [ ] example

- [ ] explanation

- [ ] illustration

- [ ] guideline

- [ ] other

- [ ] definition

- [ ] feature

- [ ] info in manual (accessibility)

- [ ] info not in manual

- [ ] Technical Accuracy

- [ ] text

- [ ] illustration

- [ ] Completeness

What information is missing?

- [ ] Clarity

- [ ] Sequence

What is not in the right order?

What is unclear?

- [ ] Other Comments

Use back for more comments.

Your Name

Location/Phone

Return to: Marketing Communications, AllenBradley Co., 1 AllenBradley Drive, Mayfield Hts., OH 441246118

Phone: (216)6463176

FAX:

(216)6464320

1794IE8, OE4, IE4XOE2

Pub. No. Pub. Date Part No.
, , 
17946.5.2 955122-66 May 1996 Series B

Other Comments

PLEASE FOLD HERE

<!-- image -->

## BUSINESS REPLY MAIL

FIRST-CLASS MAIL PERMIT NO. 18235 CLEVELAND OH

POSTAGE WILL BE PAID BY THE ADDRESSEE

TECHNICAL COMMUNICATION 1 ALLEN BRADLEY DR MAYFIELD HEIGHTS OH 44124-9705

NO POSTAGE NECESSARY IF MAILED IN THE UNITED STATES

<!-- image -->

## Support Services

<!-- image -->

At Allen-Bradley, customer service means experienced representatives at Customer Support Centers in key cities throughout the world for sales service and support. Our value-added services include:

## Technical Support

- SupportPlus programs
- telephone support and 24-hour emergency hotline
- software and documentation updates
- technical subscription services

## Engineering and Field Services

- application engineering assistance
- integration and start-up assistance
- field service
- maintenance support

## Technical Training

- lecture and lab courses
- self-paced computer and video-based training
- job aids and workstations
- training needs analysis

## Repair and Exchange Services

- your only "authorized" source
- current revisions and enhancements
- worldwide exchange inventory
- local support

<!-- image -->

## Worldwide representation.

<!-- image -->

Argentina · Australia · Austria · Bahrain · Belgium · Brazil · Bulgaria · Canada · Chile · China, PRC · Colombia · Costa Rica · Croatia · Cyprus · Czech Republic · Denmark · Ecuador · Egypt · El Salvador · Finland · France · Germany · Greece · Guatemala · Honduras · Hong Kong · Hungary · Iceland · India · Indonesia · Ireland · Israel · Italy · Jamaica · Japan · Jordan · Korea · Kuwait · Lebanon · Malaysia · Mexico · Netherlands · New Zealand · Norway · Pakistan · Peru · Philippines · Poland · Portugal · Puerto Rico · Qatar · Romania · Russia-CIS · Saudi Arabia · Singapore · Slovakia · Slovenia · South Africa, Republic · Spain · Sweden · Switzerland · Taiwan · Thailand · Turkey · United Arab Emirates · United Kingdom · United States · Uruguay · Venezuela · Yugoslavia

AllenBradley Headquarters, 1201 South Second Street, Milwaukee, WI 53204 USA, Tel: (1) 414 3822000 Fax: (1) 414 3824444

Publication 17946.5.2

Publication 17946.5.2 - May 1996 Supersedes Publication 17946.5.2 - February 1995

AllenBradley, a Rockwell Automation Business, has been helping its customers improve productivity and quality for more than 90 years. We design, manufacture and support a broad range of automation products worldwide. They include logic processors, power and motion control devices, operator interfaces, sensors and a variety of software. Rockwell is one of the world's leading technology companies.