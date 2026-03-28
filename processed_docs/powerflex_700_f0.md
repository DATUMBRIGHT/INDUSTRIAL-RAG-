20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

User Manual

PowerFlex 700 AC Drives – Series A, Frames 0…6

Standard Control Firmware 3.001 and Below

Vector Control Firmware 3.002 and Below

<!-- image -->

## C Drives - Series A, Frames 0...6

andBelow dBelow

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain

this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with

applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment. The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations. WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss. ATTENTION: Identifies information about practices or circumstances that can lead to

personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

Identifies information that is critical for successful application and understanding of the

IMPORTANT

Labels may also be on or inside the equipment to provide specific precautions. product.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or

death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

PowerFlex, DriveExplorer, DriveExecutive, PLC, Force Technology, DPI, and SCANport are either trademarks or registered trademarks of Rockwell Automation, Inc. ControlNet is a trademark of ControlNet International, Ltd. DeviceNet is a trademark of the Open DeviceNet Vendor Association.

20B-UM001.book Page i Thursday, June 20, 2013 1:55 PM

Summary of Changes

The information below summarizes the changes to the PowerFlex 700

User Manual, publication 20B-UM001 since the last release.

Manual Updates

Removed the Installation/Wiring information (Chapter 1), Start Up information

(Chapter 2), dimension, specification and fuse/breaker information (Appendix A). This information can now be found in the Installation Instructions: PowerFlex 700 Adjustable Frequency AC Drive – Frames 0…6, publication 20B-IN0019

–

20B-UM001.book Page ii Thursday, June 20, 2013 1:55 PM

soc-ii

Summary of Changes

Notes:

20B-UM001.book Page i Thursday, June 20, 2013 1:55 PM

Preface

Overview

Table of Contents

Important User Information . . . . . . . . . . . 1-2

Who Should Use this Manual? . . . . . . . . . P-1

What Is Not in this Manual . . . . . . . . . . . . P-1

Additional Resources . . . . . . . . . . . . . . . . P-2

Manual Conventions . . . . . . . . . . . . . . . . . P-2

General Precautions . . . . . . . . . . . . . . . . . P-3

## Catalog Number Explanation . . . . . . . . . . P-5

About Parameters . . . . . . . . . . . . . . . . . . . 1-1

How Parameters are Organized. . . . . . . . . 1-3

Monitor File . . . . . . . . . . . . . . . . . . . . . . 1-12

Motor Control File . . . . . . . . . . . . . . . . . 1-14

Speed Command File . . . . . . . . . . . . . . . 1-21

Dynamic Control File . . . . . . . . . . . . . . . 1-31

Utility File . . . . . . . . . . . . . . . . . . . . . . . . 1-38

Communication File . . . . . . . . . . . . . . . . 1-50

Inputs &amp; Outputs File . . . . . . . . . . . . . . . 1-54

Applications File . . . . . . . . . . . . . . . . . . . 1-60

Parameter Cross Reference – by Name. . 1-61

Parameter Cross Reference – by Number 1-64

Faults and Alarms . . . . . . . . . . . . . . . . . . . 2-1

Drive Status. . . . . . . . . . . . . . . . . . . . . . . . 2-2

Manually Clearing Faults . . . . . . . . . . . . . 2-3

Fault Descriptions . . . . . . . . . . . . . . . . . . . 2-4

Clearing Alarms . . . . . . . . . . . . . . . . . . . . 2-9

Alarm Descriptions . . . . . . . . . . . . . . . . . 2-10

Common Symptoms/Corrective Actions 2-13

Testpoint Codes and Functions . . . . . . . . 2-16

Drive Frame Sizes . . . . . . . . . . . . . . . . . . . A-1

Communication Configurations . . . . . . . . A-1

External and Internal Connections . . . . . . B-1

LCD Display Elements . . . . . . . . . . . . . . . B-2

ALT Functions. . . . . . . . . . . . . . . . . . . . . . B-2

Menu Structure . . . . . . . . . . . . . . . . . . . . . B-3

Viewing and Editing Parameters . . . . . . . . B-5

Linking Parameters (Vector Control Only) B-6

Removing/Installing the HIM . . . . . . . . . . B-8

| Chapter 1  Programming and Parameters      |
|--------------------------------------------|
| Chapter 2  Troubleshooting                 |
| Appendix A  Supplemental Drive Information |
| Appendix B  HIM Overview                   |

20B-UM001.book Page ii Thursday, June 20, 2013 1:55 PM

ii

Table of Contents

Appendix C

Application Notes

External Brake Resistor . . . . . . . . . . . . . . . C-1

Lifting/Torque Proving . . . . . . . . . . . . . . . C-2

Minimum Speed . . . . . . . . . . . . . . . . . . . . C-7

Motor Control Technology . . . . . . . . . . . . C-8

Motor Overload . . . . . . . . . . . . . . . . . . . . C-10

Overspeed . . . . . . . . . . . . . . . . . . . . . . . . C-11

Power Loss Ride Through . . . . . . . . . . . . C-12

Process PI for Standard Control . . . . . . . C-13

Reverse Speed Limit . . . . . . . . . . . . . . . . C-16

Skip Frequency . . . . . . . . . . . . . . . . . . . . C-17

Sleep Wake Mode . . . . . . . . . . . . . . . . . . C-19

Start At PowerUp. . . . . . . . . . . . . . . . . . . C-21

Stop Mode . . . . . . . . . . . . . . . . . . . . . . . . C-22

Voltage Tolerance . . . . . . . . . . . . . . . . . . C-24

| Index   |
|---------|

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

Overview

The purpose of this manual is to provide you with the basic information needed to install, start-up and troubleshoot the PowerFlex 700

Adjustable Frequency AC Drive.

For information on . . . See page . . .

Who Should Use this Manual?

What Is Not in this Manual

Additional Resources

P-1

P-1

P-2

Manual Conventions

P-2

General Precautions P-3 Catalog Number Explanation P-5

Who Should Use this Manual?

This manual is intended for qualified personnel. You must be able to program and operate Adjustable Frequency AC Drive devices. In

addition, you must have an understanding of the parameter settings and

| functions.   |
|--------------|

What Is Not in this Manual

The PowerFlex 700 Series A User Manual provides programming and troubleshooting information for Standard Control and Vector Control drives, Frames 0…6. Drive installation and wiring information is not in this manual, but can be found in the Installation Instructions for your drive:

Frames 0…6 – publication 20B-IN019

Literature is available online at http://www.rockwellautomation.com/

literature.

Preface

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

P-2

Overview

Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

Resource Description

PowerFlex 700 AC Drive Technical Data, publication 20B-TD001

PowerFlex Comm Adapter Manuals, publication

20COMM-UM…

PowerFlex 70 and PowerFlex 700 Reference

| Manual, publication PFLEX-RM001                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 70 Enhanced Control and PowerFlex 700 Vector Control Reference Manual, publication PFLEX-RM004                 |
| Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001                      |
| Safety Guidelines for the Application, Installation and Maintenance of Solid State Control, publication SGI-1.1 control. |
| Product Certifications website, http://ab.com                                                                            |
| You can view or download publications at                                                                                 |
| Rockwell Automation sales representative.                                                                                |
| Manual Conventions                                                                                                       |

This publication provides detailed drive specifications, option specifications and input

protection device ratings.

These publications provide information on configuring, using, and troubleshooting

PowerFlex communication adapters.

These publications provide detailed application specific information for programming and

configuring the PowerFlex 700 drive.

Provides basic information needed to properly wire and ground PWM AC drives.

Provides general guidelines for the application, installation, and maintenance of solid-state

Provides practices for guarding against

Electrostatic damage (ESD)

Provides declarations of conformity, certificates, and other certification details.

http:/www.rockwellautomation.com/literature/. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or

·

In this manual we refer to the PowerFlex 700 Adjustable Frequency

AC Drive as; drive, PowerFlex 700 or PowerFlex 700 Drive.

· To help differentiate parameter names and LCD display text from other text, the following conventions will be used:

–

–

Parameter Names will appear in [brackets].

For example: [DC Bus Voltage].

Display Text will appear in "quotes." For example: "Enabled."

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

·

Overview

P-3

The following words are used throughout the manual to describe an action:

Word Meaning

Can Possible, able to do something

Cannot Not possible, not able to do something

May Permitted, allowed

Must Unavoidable, you must do this

Shall Required and necessary

- Should Recommended Should Not Not recommended

General Precautions

ATTENTION: This drive contains ESD (Electrostatic Discharge)

sensitive parts and assemblies. Static control precautions are required when installing, testing, servicing or repairing this assembly.

| !   |
|-----|

Component damage may result if ESD control procedures are not followed. If you are not familiar with static control procedures,

reference A-B publication 8000-4.5.2, "Guarding Against Electrostatic

Damage" or any other applicable ESD protection handbook.

ATTENTION: An incorrectly applied or installed drive can result in

! component damage or a reduction in product life. Wiring or application errors, such as, undersizing the motor, incorrect or inadequate AC supply, or excessive ambient temperatures may result in malfunction of the system. ! ATTENTION: Only qualified personnel familiar with adjustable frequency AC drives and associated machinery should plan or implement the installation, start-up and subsequent maintenance of the system. Failure to comply may result in personal injury and/or equipment damage. ! ATTENTION: To avoid an electric shock hazard, verify that the voltage on the bus capacitors has discharged before performing any work on the drive. Measure the DC bus voltage at the +DC &amp; –DC

terminals of the Power Terminal Block (refer to Installation Instructions for location). The voltage must be zero. ! ATTENTION: Risk of injury or equipment damage exists. DPI or SCANport host products must not be directly connected together via 1202 cables. Unpredictable behavior can result if two or more devices are connected in this manner.

<!-- image -->

<!-- image -->

<!-- image -->

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

P-4

Overview

ATTENTION: An incorrectly applied or installed bypass system can result in component damage or reduction in product life. The most

common causes are:

·

Wiring AC line to drive output or control terminals.

·

·

Improper bypass or output circuits not approved by Allen-Bradley.

Output circuits which do not connect directly to the motor.

Contact Allen-Bradley for assistance with application or wiring.

ATTENTION: The "adjust freq" portion of the bus regulator function

! is extremely useful for preventing nuisance overvoltage faults resulting from aggressive decelerations, overhauling loads, and eccentric loads. It forces the output frequency to be greater than commanded frequency

- while the drive's bus voltage is increasing towards levels that would
- otherwise cause a fault. However, it can also cause either of the
- following two conditions to occur.

1. Fast positive changes in input voltage (more than a 10% increase within 6 minutes) can cause uncommanded positive speed changes. However an "OverSpeed Limit" fault will occur if the speed reaches [Max Speed] + [Overspeed Limit]. If this condition is unacceptable, action should be taken to 1) limit supply voltages within the specification of the drive and, 2) limit fast positive input voltage changes to less than 10%. Without taking such actions, if this operation is unacceptable, the "adjust freq" portion of the bus

regulator function must be disabled (see parameters 161 and 162).

2. Actual deceleration times can be longer than commanded deceleration times. However, a "Decel Inhibit" fault is generated if the drive stops decelerating altogether. If this condition is unacceptable, the "adjust freq" portion of the bus regulator must be disabled (see parameters 161 and 162). In addition, installing a properly sized dynamic brake resistor will provide equal or better performance in most cases. Important: These faults are not instantaneous. Test results have
2. shown that they can take between 2-12 seconds to occur. ! ATTENTION: Loss of control in suspended load applications can cause personal injury and/or equipment damage. Loads must always be controlled by the drive or a mechanical brake. Parameters 600-611 are designed for lifting/torque proving applications. It is the responsibility of the engineer and/or end user to configure drive parameters, test any

lifting functionality and meet safety requirements in accordance with all applicable codes and standards.

!

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

Catalog Number Explanation

D

C

3

20B

Overview

0

NN

2P1

A

A

Y

N

A

E

P-5

AD

a b c de f gh i j k l m n

a

Drive

## Code Type 20B PowerFlex 700

b

Voltage Rating

e

HIM

Code Operator Interface

0 Blank Cover

3 LCD Display, Full Numeric Keypad

J ♦

K ♦

Remote (Panel Mount), IP66, NEMA/UL

Type 12 Full Numeric LCD HIM

Remote (Panel Mount), IP66, NEMA/UL

Type 12 Prog. Only LCD HIM

f

Documentation

Code Type

No Shipping Package

| A Manual N No Manual   | A Manual N No Manual   |
|------------------------|------------------------|
|                        | (Internal Use Only)    |
|                        | g                      |

<!-- image -->

Brake

Code w/Brake IGBT ‡

<!-- image -->

| N No   | N No                                    | N No   |
|--------|-----------------------------------------|--------|
|        | ‡ Brake IGBT is standard on Frames 0-3, |        |
|        | optional on Frames 4-6.                 |        |
|        | Internal Braking Resistor               |        |

Y

Yes

N No

Not available for Frame 3 drives or larger.

| i        |
|----------|
| Emission |

<!-- image -->

Code CE Filter §

CM Choke

A Yes Yes

<!-- image -->

§ Note: 600V class drives below 77 Amps

(Frames 0-4) are declared to meet the Low

Voltage Directive. It is the responsibility of the user to determine compliance to the EMC

| directive.   | directive.                                      |
|--------------|-------------------------------------------------|
|              | # Only available for 208…240V Frame 0-3 drives. |

<!-- image -->

D 480V AC 3 - 0…6

E 600V AC 3 - 0…6

F 690V AC 3 - 5…6

H 540V DC - N 5…6

J 650V DC - N 5…6

<!-- image -->

| N 325V DC - Y 5…6        | N 325V DC - Y 5…6        |
|--------------------------|--------------------------|
|                          | P 540V DC - Y 5…6        |
|                          | R 650V DC - Y 5…6        |
|                          | T 810V DC - Y 5…6        |
|                          | W 932V DC - Y 5…6        |
|                          | c                        |
| ND Output Rating Example | ND Output Rating Example |

Code Amps kW (Hp)

2P2 2.2 0.37 (0.5)

| 022 22 5.5 (7.5)       | 022 22 5.5 (7.5)   |
|------------------------|--------------------|
| Code Enclosure         |                    |
| A IP20, NEMA/UL Type 1 |                    |

Open/Flange Mount

F ♠

Front: IP00, NEMA/UL Type Open

Back/Heatsink: IP54, NEMA Type 12

<!-- image -->

<!-- image -->

j

Comm Slot

Code Network Type

C ControlNet (Coax)

D DeviceNet

E EtherNet/IP

N None

k

Control &amp; I/O

Code Control I/O Volts

A Standard 24V DC/AC

B Standard 115V AC

C

Vector Δ

24V DC

D

Vector Δ

115V AC

N Standard None

Δ Vector Control Option utilizes DPI Only.

l

Feedback

Code Type

0 None

1 Encoder, 12V/5V

m

Future Use

n

Special Firmware (Frames 0…6 Only)

Code Type

AD ♦

60 Hz Maximum

AE ♦

AX ♦

BA ♦

Cascading Fan/Pump Control

82 Hz Maximum

Pump Off (for pump jack)

♦ Must be used with Vector Control option C or

D (Position k). Positions m-n are only required when custom firmware is supplied.

<!-- image -->

<!-- image -->

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

P-6

Notes:

Overview

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

·

·

Chapter 1

Programming and Parameters

700 parameters. The parameters can be programmed (viewed/edited)

using an LCD HIM (Human Interface Module). As an alternative, programming can also be performed using DriveExplorer™ or

## DriveExecutive™ software and a personal computer. Refer to Appendix B for a brief description of the LCD HIM.

For information on . . . See page . . .

About Parameters

1-1

How Parameters are Organized 1-3 Monitor File 1-12 Motor Control File 1-14 Speed Command File 1-21 Dynamic Control File 1-31 Utility File 1-38

Communication File

|    | Inputs & Outputs File   |
|----|-------------------------|
|    | Applications File       |
|    | ENUM Parameters         |
| •  |                         |

1-50

1-54

1-60

Parameter Cross Reference – by Name

1-62

Parameter Cross Reference – by Number 1-65

About Parameters

To configure a drive to operate in a specific way, drive parameters may have to be set. Three types of parameters exist:

ENUM parameters allow a selection from 2 or more items. The LCD

HIM will display a text message for each item.

Bit Parameters

Bit parameters have individual bits associated with features or conditions. If the bit is 0, the feature is off or the condition is false. If

the bit is 1, the feature is on or the condition is true. Numeric Parameters

These parameters have a single numerical value (i.e. 0.1 Volts).

The example on the following page shows how each parameter type is presented in this manual.

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

1-2

Programming and Parameters

➊ ➌ ➋ ➏ ➍ ➎

File

Group No.

➎

Parameter Name &amp; Description Values

198 [Load Frm Usr Set]

Loads a previously saved set of parameter values from a selected user

set location in drive nonvolatile memory to active drive memory.

<!-- image -->

Default:

Options:

Related

199

0

0

1

2

"Ready"

"Ready"

"User Set 1"

"User Set 2"

3

"User Set 3"

Digital In6
Digital In5
Digital In4
Digital In3
Digital In2
Digital In1

0

0

1=Input Present

0 0 0 0

0

15 14 13 12 11 10 0 9 8 7 6 5 4 3 2 1

3

2

1

1.0

–/+32767.0

0.1

No. – Parameter number. = Parameter value can not be changed until drive is stopped.

= 32 bit parameter in the Standard Control option. All parameters in the Vector Control option are 32 bit.

= Parameter only displayed when [Motor Cntl Sel] is set to "4."

Parameter Name &amp; Description – Parameter name as it appears on an LCD HIM, with a brief

= This parameter is specific to the Standard Control Option.

= This parameter will only be available with the Vector Control option.

= Only available with Vector Control option firmware version 3.xxx &amp; later.

Values – Defines the various operating characteristics of the parameter. Three types exist.

Lists the value assigned at the factory. "Read Only" = no default.

Displays the programming selections available.

Bit Bit: Lists the bit place holder and definition for each bit.

Lists the value assigned at the factory. "Read Only" = no default.

The range (lowest and highest setting) possible for the parameter.

Unit of measure and resolution as shown on the LCD HIM.

Analog inputs can be set for current or voltage with [Anlg In Config], param. 320.

Setting [Speed Units], parameter 79 on Vector Control drives selects Hz or RPM.

Vector

Values that pertain to Vector Control drives only will be indicated by " " or
Vector

Important: When sending values through DPI ports, simply remove the decimal point to arrive at the correct value (i.e. to send "5.00 Hz," use "500").

Related – Lists parameters (if any) that interact with the selected parameter. The symbol " "

indicates that additional parameter information is available in Appendix C.

5

Min/Max:

4

0=Input Not Present x =Reserved

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

Programming and Parameters

How Parameters are Organized

The LCD HIM displays parameters in a File-Group-Parameter or

Numbered List view order. To switch display mode, access the Main

Menu, press ALT, then Sel while cursor is on the parameter selection. In addition, using [Param Access Lvl], the user has the option to display all

Control Options

Two different control options are available for the PowerFlex 700; Standard and Vector. The Standard Control option provides typical Volts per Hertz and Sensorless Vector operation. The Vector Control option

provides the added capability of FVC

Vector control. The cassette determines the type of control you

Standard Control

Option

Vector Control

Option selected, the parameters associated solely with other operations such as

Volts per Hertz or Sensorless Vector will be hidden. Refer to pages 1-4

have available (see diagram). To simplify programming with the Vector Control option, the displayed parameters will change according to the selection made with [Motor Cntl Sel]. For example, if "FVC Vector" is through 1-8 .

File-Group-Parameter Order This simplifies programming by grouping parameters that are used for similar functions. The parameters are organized into files. Each file is divided into groups, and each parameter is an element in a group. By default, the LCD HIM displays parameters by File-Group-Parameter view. Numbered List View

<!-- image -->

All parameters are in numerical order.

1-3

<!-- image -->

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

1-4

Programming and Parameters

Basic Parameter View – Standard Control Option

Parameter 196 [Param Access Lvl] set to option 0 "Basic."

File Group Parameters

Monitor

M

onitor

Metering Output Freq 001

Commanded Freq 002

Output Current 003

DC Bus Voltage 012

## Motor Control Motor Data Motor NP Volts 041

Motor NP FLA 042

Motor NP Hertz 043 Motor Control

Motor NP RPM 044

Motor NP Power 045

Mtr NP Pwr Units 046

Maximum Freq 055

Autotune 061

Speed Ref B Hi 094

Speed Ref A Lo 092

Speed Ref B Lo 095

Decel Time 1 142

Decel Time 2 143

DC Brk Lvl Sel 157

DC Brake Level 158

DC Brake Time 159

Motor OL Hertz 047

TB Man Ref Sel 096

TB Man Ref Hi 097

TB Man Ref Lo 098

S-Curve % 146

Bus Reg Mode A 161

Bus Reg Mode B 162

DB Resistor Type 163

Restart Modes Start At PowerUp 168 Auto Rstrt Tries 174 Auto Rstrt Delay 175

Save To User Set 199

Language 201

Analog In1 Lo 323

Analog In2 Lo 326

Dig Out1 Level 381

Dig Out2 Level 385

|                                 | Torq Attributes Torque Perf Mode 053                                          | Maximum Voltage 054                                                                            |
|---------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Speed Command Speed Command     | Spd Mode & Limits Speed References                                            | Minimum Speed 081 Maximum Speed 082 Speed Ref A Sel 090 Speed Ref B Sel 093 Speed Ref A Hi 091 |
|                                 | Discrete Speeds                                                               | Jog Speed 100 Preset Speed 1-7 101-107                                                         |
| Dynamic Control Dynamic Control | Ramp Rates Accel Time 1 140 Load Limits Current Lmt Sel 147                   | Accel Time 2 141 Current Lmt Val 148                                                           |
|                                 | Stop/Brake Modes                                                              | Stop Mode A 155 Stop Mode B 156                                                                |
| Utility                         | Direction Config Direction Mode 190                                           | Power Loss Power Loss Mode 184 Power Loss Time 185                                             |
| Utility                         | Drive Memory Param Access Lvl 196                                             | Reset To Defalts 197                                                                           |
|                                 | Faults Fault Config 1 238                                                     | Load Frm Usr Set 198                                                                           |
| Inputs & Outputs                | Analog Inputs Anlg In Config 320                                              | Analog In1 Hi 322                                                                              |
| Inputs & Outputs                |                                                                               | Analog In2 Hi 325                                                                              |
|                                 | Analog Outputs Analog Out1 Sel 342                                            | Analog Out1 Hi 343                                                                             |
|                                 |                                                                               | Analog Out1 Lo 344                                                                             |
|                                 | Digital Inputs Digital In1-6 Sel 361-366 Digital Outputs Digital Out1 Sel 380 | Digital Out2 Sel 384                                                                           |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

Programming and Parameters

Basic Parameter View – Vector Control Option

Parameter 196 [Param Access Lvl] set to option 0 "Basic."

File Group Parameters

Monitor

M

onitor

Metering Output Freq 001

Commanded Speed002

Commanded Torque

**

024

DC Bus Voltage 012

## Motor Control Motor Data Motor NP Volts 041

Motor NP FLA 042

Motor NP Hertz 043 Motor Control

Torq Attributes Motor Cntl Sel 053

Motor NP RPM 044

Motor NP Power 045

Mtr NP Pwr Units 046

Autotune Torque

**

066

Inertia Autotune

**

Torque Ref A Sel

Torque Ref A Hi

**

**

067

427

428

Motor Fdbk Type 412 Encoder PPR 413

Minimum Speed 081

Maximum Speed 082

Speed Ref B Hi 094

Speed Ref B Lo 095

TB Man Ref Sel 096

TB Man Ref Hi 097

Jog Speed 2 108

Decel Time 1 142

Decel Time 2 143

DC Brk Lvl Sel 157

DC Brake Level 158

DC Brake Time 159

Motor OL Hertz 047

Motor Poles 049

Torque Ref A Lo

**

429

Pos Torque Limit

**

Neg Torque Limit

**

436

437

Rev Speed Limit

**

454

TB Man Ref Lo 098

Pulse Input Ref 099

S-Curve % 146

Bus Reg Mode A 161

Bus Reg Mode B 162

DB Resistor Type 163

Restart Modes Start At PowerUp 168 Auto Rstrt Tries 174 Auto Rstrt Delay 175

Power Loss Power Loss Mode 184 Power Loss Time 185 Power Loss Level 186

Load Frm Usr Set 198

Save To User Set 199

Diagnostics Start Inhibits 214 Dig In Status 216 Dig Out Status 217

Analog In2 Hi 325

Analog In2 Lo 326

Analog Out1, 2 Lo 344

Analog Out1, 2 Sel 345

Analog Out2 Hi 346

Analog Out1, 2 Lo 347

Digital Outputs Digital Out1-3 Sel 380-388 Dig Out1-3 Level 381-389

These parameters will only be displayed when parameter 053 [Motor Cntl Sel] is set to option "4."

Language 201

|                  |                                                     | Maximum Voltage 054                                                  |                     |
|------------------|-----------------------------------------------------|----------------------------------------------------------------------|---------------------|
|                  | Speed Feedback Spd Mode &                           | Maximum Freq 055 Autotune 061 Speed Units 079 Feedback Select 080    |                     |
| Speed Command    | Speed References                                    | Speed Ref A Sel 090 Speed Ref A Hi 091 Speed Ref A Lo 092            |                     |
| Dynamic          | Discrete Speeds Ramp Rates Accel Time 1 140         | Speed Ref B Sel 093 Jog Speed 1 100 Preset Speed 1-7 101-107         |                     |
| Control          |                                                     | Accel Time 2 141 Load Limits Current Lmt Sel 147 Current Lmt Val 148 |                     |
| Dynamic Control  | Stop/Brake Modes                                    | Stop/Brk Mode A 155                                                  | Stop/Brk Mode A 155 |
|                  |                                                     | Stop/Brk Mode B 156                                                  |                     |
| Utility          | Direction Config Direction Mode 190                 |                                                                      |                     |
| Utility          | Drive Memory Param Access Lvl 196                   | Reset To Defalts 197                                                 |                     |
|                  | Faults Fault Config 1 238 Alarms Alarm Config 1 259 | Analog Inputs Anlg In Config 320                                     |                     |
| Inputs & Outputs |                                                     | Analog In1 Hi 322                                                    |                     |
| Inputs & Outputs |                                                     | Analog In1 Lo 323                                                    |                     |
|                  | Analog Outputs Analog Out1, 2 Sel 342               | Analog Out1 Hi 343                                                   |                     |
|                  | Digital Inputs Digital In1-6 Sel 361-366            |                                                                      |                     |

1-5

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

1-6

Programming and Parameters

Advanced Parameter View – Standard Control Option

Parameter 196 [Param Access Lvl] set to option 1 "Advanced."

File Group Parameters

Monitor

M

onitor

Metering Output Freq 001

Commanded Freq 002

Output Current 003

Torque Current 004

Flux Current 005

Drive Data Rated kW 026

Rated Volts 027

## Motor Control Motor Data Motor Type 040

Motor NP Volts 041 Motor NP FLA 042 Motor Control

Output Voltage 006

Output Power 007

Output Powr Fctr 008

Elapsed MWh 009

Elapsed Run Time 010

Rated Amps 028

Control SW Ver 029

Motor NP RPM 044

Motor NP Power 045

Mtr NP Pwr Units 046

Motor OL Hertz 047

Flux Up Mode 057

Flux Up Time 058

SV Boost Filter 059

Autotune 061

Break Voltage 071

Break Frequency 072

Overspeed Limit 083

Skip Frequency 1 084

Skip Frequency 2 085

Speed Ref B Sel 093

Speed Ref B Hi 094

Speed Ref B Lo 095

Trim Hi 119

Trim Lo 120

Slip RPM Meter 123

PI Integral Time 129

PI Prop Gain 130

PI Lower Limit 131

PI Upper Limit 132

PI Preload 133

Decel Time 1 142

Decel Time 2 143

Drive OL Mode 150

PWM Frequency 151

DC Brake Time 159

Bus Reg Ki 160

Bus Reg Mode A 161

Bus Reg Mode B 162

Auto Rstrt Delay 175

Sleep Wake-Mode 178

Sleep-Wake Ref 179

Wake Level 180

|               |                 |                                                              | Motor NP Hertz 043                                                                         |
|---------------|-----------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------|
|               |                 | Volts per Hertz Start/Acc Boost 069                          | Torq Attributes Torque Perf Mode 053 Maximum Voltage 054 Maximum Freq 055 Compensation 056 |
| Speed Command | Speed Command   | Spd Mode & Limits                                            | Speed Mode 080 Minimum Speed 081 Maximum Speed 082                                         |
|               |                 | Discrete Speeds Speed Trim Trim In Select 117                | Speed Ref A Lo 092 Jog Speed 100 Preset Speed 1-7 101-107                                  |
|               |                 | Slip Comp Slip RPM @ FLA 121 Process PI PI Configuration 124 | Slip Comp Gain 122 PI Control 125                                                          |
| Control       |                 |                                                              | PI Reference Sel 126 PI Setpoint 127 PI Feedback Sel 128                                   |
| Dynamic       | Dynamic Control | Ramp Rates Accel Time 1 140 Load Limits Current Lmt Sel 147  | Accel Time 2 141 Current Lmt Val 148                                                       |
|               |                 | Stop/Brake                                                   | Current Lmt Gain 149                                                                       |
|               |                 | Modes                                                        |                                                                                            |
|               |                 |                                                              | Stop Mode A 155                                                                            |
|               |                 |                                                              | Stop Mode B 156 DC Brake Lvl Sel 157                                                       |
|               |                 |                                                              | DC Brake Level 158                                                                         |
|               |                 |                                                              | Flying Start En 169                                                                        |
|               |                 | Restart Modes Start At PowerUp 168                           |                                                                                            |
|               |                 |                                                              | Flying StartGain 170                                                                       |
|               |                 |                                                              | Auto Rstrt Tries 174                                                                       |
|               |                 | Power Loss Power Loss Mode 184                               |                                                                                            |
|               |                 |                                                              | Power Loss Time 185                                                                        |
|               |                 |                                                              | Power Loss Level 186                                                                       |

MOP Frequency 011

DC Bus Voltage 012

DC Bus Memory 013

Analog In1 Value 016

Analog In2 Value 017

Motor OL Factor 048

IR Voltage Drop 062

Flux Current Ref 063

IXo Voltage Drop 064

Skip Frequency 3 086

Skip Freq Band 087

TB Man Ref Sel 096

TB Man Ref Hi 097

TB Man Ref Lo 098

PI Status 134

PI Ref Meter 135

PI Fdback Meter 136

PI Error Meter 137

PI Output Meter 138

S Curve % 146

DB Resistor Type 163

Bus Reg Kp 164

Bus Reg Kd 165

Wake Time 181

Sleep Level 182

Sleep Time 183

20B-UM001.book Page 7 Thursday, June 20, 2013 1:55 PM

File Group Parameters

Utility

Direction Config Direction Mode 190

Utility

HIM Ref Config Save HIM Ref 192

Man Ref Preload 193

MOP Config Save MOP Ref 194

MOP Rate 195

Load Frm Usr Set 198

Diagnostics Drive Status 1 209

Programming and Parameters

Save To User Set 199

Reset Meters 200

Language 201

Dig Out Status 217

Drive Temp 218

Drive OL Count 219

Motor OL Count 220

Fault Speed 224

Fault Amps 225

Fault Bus Volts 226

Status 1 @ Fault 227

Fault Clear Mode 241

Power Up Marker 242

Alarm1-8 Code 262-269

Drive Ref Rslt 272

Drive Ramp Rslt 273

Fault Clr Mask 283

MOP Mask 284

Local Mask 285

Stop Owner 288

Start Owner 289

Jog Owner 290

Direction Owner 291

Analog In 2 Hi 325

Analog In 1 Lo 323

Analog In 2 Lo 326

Analog Out1 Hi 343

Analog Out1 Lo 344

Dig Out2 Level 385

Dig Out1 OnTime 382

Dig Out2 OnTime 386

|                              | Drive Status 2 210 Drive Alarm 1 211                                                                                                                                                                                                                                      |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              | Drive Alarm 2 212                                                                                                                                                                                                                                                         |
|                              | Speed Ref Source 213 Start Inhibits 214 Last Stop Source 215                                                                                                                                                                                                              |
|                              | Dig In Status 216 Faults Fault Config 1 238                                                                                                                                                                                                                               |
|                              | Fault Clear 240 Alarms Alarm Config 1 259                                                                                                                                                                                                                                 |
| Communication  Communication | Comm Control DPI Baud Rate 270 Drive Logic Rslt 271 Masks & Owners Logic Mask 276 Start Mask 277 Jog Mask 278 Direction Mask 279 Reference Mask 280 Accel Mask 281 Decel Mask 282 Datalinks Data In A1-D2 300-307 Data Out A1-D2 310-317 Analog Inputs Anlg In Config 320 |
| Inputs & Outputs             | Anlg In Sqr Root 321 Analog In 1 Hi 322                                                                                                                                                                                                                                   |
| Inputs & Outputs             | Analog Outputs Anlg Out Config 340 Anlg Out Absolut 341 Analog Out1 Sel 342 Digital Inputs Digital In1-6 Sel 361-366 Digital Outputs Digital Out1 Sel 380                                                                                                                 |
|                              | Dig Out1 Level 381                                                                                                                                                                                                                                                        |
|                              | Digital Out2 Sel 384                                                                                                                                                                                                                                                      |

Voltage Class 202

Drive Checksum 203

Status 2 @ Fault 228

Alarm 1 @ Fault 229

Alarm 2 @ Fault 230

Testpoint 1 Sel 234

Testpoint 1 Data 235

Testpoint 2 Sel 236

Testpoint 2 Data 237

Fault 1-8 Code 243-257

Fault 1-8 Time 244-258

Reference Owner 292

Accel Owner 293

Decel Owner 294

Fault Clr Owner 295

MOP Owner 296

Local Owner 297

Anlg In 1 Loss 324

Anlg In 2 Loss 327

Dig Out1 OffTime 383

Dig Out2 OffTime 387

1-7

<!-- image -->

20B-UM001.book Page 8 Thursday, June 20, 2013 1:55 PM

1-8

Programming and Parameters

Advanced Parameter View – Vector Control Option

Parameter 196 [Param Access Lvl] set to option 1 "Advanced."

File Group Parameters

Monitor

Monitor

Motor Control

Torque Current 004

Flux Current 005

Output Voltage 006

Output Power 007

Output Powr Fctr 008

Elapsed MWh 009

Elapsed Run Time 010

Rated Amps 028

Control SW Ver 029

Motor NP RPM 044

Motor NP Power 045

Mtr NP Pwr Units 046

Motor OL Hertz 047

Flux Current Ref 063

IXo Voltage Drop 064

Autotune Torque

066

**

Inertia Autotune

**

Torque Ref A Sel

**

Torque Ref A Hi

**

Torque Ref A Lo

**

**

**

*

067

427

428

429

430

431

071

Break Frequency

072

*

Fdbk Filter Sel 416

Notch Filter Freq

419

**

**

420

Overspeed Limit 083

Skip Frequency 1

084

*

Skip Frequency 2

085

*

Skip Frequency 3

086

*

Speed Ref B Hi 094

Speed Ref B Lo 095

TB Man Ref Sel 096

MOP Reference 011

DC Bus Voltage 012

DC Bus Memory 013

Analog In1 Value 016

Analog In2 Value 017

Elapsed kWh 014

Motor OL Factor 048

Motor Poles 049

Torque Ref B Hi

432

**

Torque Ref B Lo

**

Torq Ref B Mult

**

Torque Setpoint

**

Torque Setpoint 2

433

434

435

**

Pos Torque Limit

**

Neg Torque Limit

**

Control Status

4383.x

436

437

440

**

Mtr Tor Cur Ref

441

**

Marker Pulse 421

Pulse In Scale 422

Encoder Z Chan 423

Skip Freq Band

087

*

Speed/Torque Mod

088

**

Rev Speed Limit

454

**

TB Man Ref Hi 097

TB Man Ref Lo 098

Pulse Input Ref 099

Jog Speed 1 100 Preset Speed 1-7 101-107 Jog Speed 2 108

Trim Hi 119

Trim Lo 120

*

122 Slip RPM Meter 123

PI Lower Limit 131

PI Output Meter 138

PI Upper Limit 132

PI Preload 133

PI Status 134

PI Ref Meter 135

PI Fdback Meter 136

PI Error Meter 137

**

447

Speed Desired BW

**

449

PI Reference Hi 460

PI Reference Lo 461

PI Feedback Hi 462

PI Feedback Lo 463

PI BW Filter 1392.x

PI Deriv Time 4593.x

Total Inertia

**

450

Speed Loop Meter

**

4513.x

Ramp Rates Accel Time 1, 2 140,141 Decel Time 1, 2 142,143 S Curve % 146

Drive OL Mode 150

PWM Frequency 151

Droop RPM @ FLA152

Regen Power Limit

Current Rate Limit

**

**

153

154

Trim % Setpoint 116

Metering Output Freq 001

Commanded Speed 002

Ramped Speed 022

Speed Reference 023

Commanded Torque

024

**

Speed Feedback 025

Output Current 003

## Drive Data Rated kW 026

Rated Volts 027

Motor Data Motor Type 040

|                             |                                                     | Motor NP Volts 041 Motor NP FLA 042                                                                                                                                    |                            |
|-----------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
|                             | Torq Attributes Motor Cntl Sel 053                  | Motor NP Hertz 043 Maximum Voltage 054 Maximum Freq 055 Compensation 056 Flux Up Mode 057                                                                              |                            |
|                             |                                                     | Flux Up Time 058 SV Boost Filter 059 Autotune 061                                                                                                                      | Torq Ref A Div             |
|                             | Volts per Hertz Start/Acc Boost 069 Run Boost Speed | IR Voltage Drop 062 *  070 Motor Fdbk Type 412                                                                                                                         | Torque Ref B Break Voltage |
| Speed Command Speed Command | Feedback Spd Mode & Limits Speed                    | Encoder PPR 413 Enc Position Fdbk 414 Encoder Speed 415 Speed Units 079 Feedback Select 080 Minimum Speed 081 Maximum Speed 082 Speed Ref A Sel 090 Speed Ref A Hi 091 | Notch Filter K             |
|                             | References                                          | Speed Ref A Lo 092 Speed Ref B Sel 093                                                                                                                                 |                            |
|                             | Discrete Speeds                                     | Speed Trim Trim In Select 117                                                                                                                                          |                            |
|                             | Process PI PI Configuration 124                     | Trim Out Select 118 Slip Comp Slip RPM @ FLA 121 Slip Comp Gain PI Control 125                                                                                         |                            |
|                             |                                                     | PI Reference Sel 126 PI Setpoint 127 PI Feedback Sel 128 PI Integral Time 129                                                                                          |                            |
|                             | Speed Ki Speed Loop                                 | PI Prop Gain 130 **  445                                                                                                                                               | Kf Speed Loop              |
| Dynamic                     | Regulator                                           | Kp Speed Loop **  446                                                                                                                                                  |                            |
| Control                     | Load Limits Current Lmt Sel 147                     | Current Lmt Val 148                                                                                                                                                    |                            |
| Dynamic Control             |                                                     | Current Lmt Gain 149                                                                                                                                                   |                            |

3.x

3.x

20B-UM001.book Page 9 Thursday, June 20, 2013 1:55 PM

File Group Parameters

Dynamic

Stop/Brake

Control continued

Dynamic Control

Modes

Stop/Brk Mode 155,156

DC Brk Lvl Sel 157

DC Brake Level 158

DC Brake Time 159

Restart Modes Start At PowerUp 168

Flying Start En 169

Flying StartGain 170

Power Loss Power Loss Mode 184

Power Loss Time 185

Programming and Parameters

Bus Reg Ki

160

*

Bus Reg Mode 161,162

DB Resistor Type 163

Bus Reg Kp

164

*

Auto Rstrt Delay 175

Sleep-Wake Mode 178

Sleep-Wake Ref 179

Load Loss Level 1873.x

Load Loss Time 1883.x

Shear Pin Time 1893.x

Save To User Set 199

Reset Meters 200

Language 201

Dig Out Status 217

Drive Temp 218

Drive OL Count 219

Motor OL Count 220

Fault Speed 224

Fault Amps 225

Fault Clear Mode 241

Power Up Marker 242

Bus Reg Kd

165

*

Flux Braking 166

DB While Stopped 145

Wake Time 181

Sleep Level 182

Sleep Time 183

Powerup Delay 167

Gnd Warn Level 1773.x

Voltage Class 202

Drive Checksum 203

Fault Bus Volts 226

Status 1,2 @ Fault 227,228

Alarm 1,2 @ Fault 229,230

Testpoint 1,2 Sel 234,236

Testpoint 1,2 Data 235,237

Fault 1-8 Code 243-257

Fault 1-8 Time 244-258

Alarms Alarm Config 1 259 Alarm Clear 261 Alarm1-8 Code 262-269

Scale1, 2 In Lo 478,484

Scale3, 4 In Lo 490,4963.x

Scale1, 2 Out Hi 479,485

Scale3, 4 Out Hi 491,4973.x

Drive Ref Rslt 272

Drive Ramp Rslt 273

MOP Mask 284

Local Mask 285

Stop Owner 288

Start Owner 289

Jog Owner 290

Direction Owner 291

Reference Owner 292

Accel Owner 293

Datalinks Data In A1-D2 300-307 Data Out A1-D2 310-317

Analog In1, 2 Hi 322,325

Analog In1, 2 Lo 323,326

Analog Out1, 2 Hi 343,346

Analog Out1, 2 Lo 344,347

Dig Out OnTime 382,386,390

Dig Out OffTime 383,387,391

Brk Release Time 6043.x

ZeroSpdFloatTime 605

3.x

Float Tolerance 6063.x

Brk Set Time 6073.x

Scale1,2 Out Lo 480,486

Scale3,4 Out Lo 492,4883.x

Scale1,2 Out Val 481,487

Scale3,4 Out Val 493,4993.x

DPI Port Sel 274

DPI Port Value 275

Decel Owner 294

Fault Clr Owner 295

MOP Owner 296

Local Owner 297

DPI Ref Select 2983.x

DPI Fdbk Select 2993.x

Analog In1, 2 Loss 324,327

Anlg Out1,2 Scal 354,355

Anlg1 Out Setpt 377,378

3.x

3.x

Dig Out Setpt 379

3.x

TorqLim SlewRate 608

3.x

BrkSlip Count 609

3.x

Brk Alarm Travel 6103.x

MicroPos Scale% 6113.x

These parameters will only be displayed when parameter 053 [Motor Cntl Sel] is set to option "2 or 3."

These parameters will only be displayed when parameter 053 [Motor Cntl Sel] is set to option "4."

<!-- image -->

|                                    |                                                                                                                               | Power Loss Level 186                                                                                         |                                           |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Utility  Utility                   | Direction Config Direction Mode 190 MOP Config Save MOP Ref 194 MOP Rate 195                                                  | HIM Ref Config Save HIM Ref 192 Man Ref Preload 193                                                          |                                           |
|                                    | Drive Memory Param Access Lvl 196 Diagnostics Drive Status 1, 2 209,210                                                       | Reset To Defalts 197 Load Frm Usr Set 198                                                                    |                                           |
|                                    |                                                                                                                               | Drive Alarm 1, 2 211,212 Speed Ref Source 213                                                                |                                           |
|                                    |                                                                                                                               | Last Stop Source 215 Dig In Status 216                                                                       |                                           |
|                                    | Faults Fault Config 1 238                                                                                                     |                                                                                                              |                                           |
|                                    |                                                                                                                               | Fault Clear 240                                                                                              |                                           |
|                                    | Scaled Blocks Scale1, 2 In Val 476,482                                                                                        | Scale3, 4 In Val 488,4943.x                                                                                  |                                           |
| Communication  Communication       | Comm Control DPI Baud Rate 270 Masks & Owners                                                                                 | Scale1, 2 In Hi 477,483 Scale3, 4 In Hi 489,4953.x Drive Logic Rslt 271 Logic Mask 276 Start Mask 277        |                                           |
|                                    |                                                                                                                               | Jog Mask 278 Direction Mask 279                                                                              |                                           |
|                                    |                                                                                                                               | Reference Mask 280 Accel Mask 281                                                                            |                                           |
|                                    |                                                                                                                               | Decel Mask 282 Fault Clr Mask 283                                                                            |                                           |
| Inputs & Outputs                   | Analog Inputs Anlg In Config 320                                                                                              | Anlg In Sqr Root 321                                                                                         |                                           |
| Applications 3.x  Inputs & Outputs | Digital Inputs Digital In1-6 Sel 361-366 Digital Outputs Digital Out Sel 380,384,388 Torq Proving 3.x  TorqProve Cnfg 600 3.x | Analog Outputs Anlg Out Config 340 Anlg Out Absolut 341 Analog Out1, 2 Sel 342,345 Dig Out Level 381,385,389 |                                           |
| Applications                       |                                                                                                                               | TorqProve Setup 601 3.x 3.x                                                                                  |                                           |
|                                    |                                                                                                                               | Spd Dev Band 602 SpdBand Integrat 603 3.x                                                                    | Spd Dev Band 602 SpdBand Integrat 603 3.x |
|                                    | Firmware 2.001 & later only.                                                                                                  | 3.x  Firmware 3.001 & later only.                                                                            |                                           |

1-9

3.x

<!-- image -->

20B-UM001.book Page 10 Thursday, June 20, 2013 1:55 PM

1-10

Programming and Parameters

Basic Fan/Pump Parameter View(1) – Standard Control Option

Parameter 196 [Param Access Lvl] set to option 3 "Fan/Pump."

File Group Parameters

Monitor

Monitor

Metering Output Freq 001

Commanded Freq 002

Output Current 003

Output Power 007

## Motor Control Motor Data Motor NP Volts 041

Motor NP FLA 042 Motor NP Hertz 043 Motor Control

Torq Attributes Maximum Voltage 054

Elapsed MWh 009

Elapsed Run Time 010

DC Bus Voltage 012

Analog In1 Value 016

Motor NP RPM 044

Motor NP Power 045

Mtr NP Pwr Units 046

Break Voltage 071

Break Frequency 072

Overspeed Limit 083

Skip Frequency 1 084

Skip Freq Band 087

Analog In 1 Lo 323

Anlg In 1 Loss 324

Analog Out1 Hi 343

Analog Out1 Lo 344

Dig Out2 Level 385

(1) Only available on Standard Control drives with firmware version 3.001 or above.

| Speed Command    | Volts per Hertz Start/Acc Boost 069 Run Boost 070 Spd Mode & Limits Speed Mode 080 Minimum Speed 081   |
|------------------|--------------------------------------------------------------------------------------------------------|
| Speed Command    | Speed References Speed Ref A Sel 090 Speed Ref A Hi 091 Speed Ref A Lo 092 Discrete Preset Speed 2 102 |
| Dynamic          | Speeds Ramp Rates Accel Time 1 140                                                                     |
| Control          | Decel Time 1 142 Load Limits Current Lmt Val 148                                                       |
| Dynamic Control  | Stop/Brake Modes Stop Mode A 155                                                                       |
|                  | Restart Modes Start At PowerUp 168                                                                     |
| Utility          | Drive Memory Param Access Lvl 196                                                                      |
|                  | Language 201 Diagnostics Start Inhibits 214                                                            |
|                  | Dig In Status 216 Dig Out Status 217                                                                   |
| Inputs & Outputs | Analog Inputs Anlg In Config 320 Anlg In Sqr Root 321                                                  |
| Inputs & Outputs | Analog In 1 Hi 322 Analog Outputs Anlg Out Config 340 Analog Out1 Sel 342                              |
|                  | Digital Inputs Digital In1-6 Sel 361-366 Digital Outputs Digital Out1 Sel 380                          |
|                  | Digital Out2 Sel 384 Dig Out1 Level 381                                                                |

20B-UM001.book Page 11 Thursday, June 20, 2013 1:55 PM

Programming and Parameters

1-11

Advanced Fan/Pump Parameter View(1) – Standard Control Option

Parameter 196 [Param Access Lvl] set to option 4 "Adv Fan/Pump."

File Group Parameters

Monitor

Monitor

Metering Output Freq 001

Commanded Freq 002

Output Current 003

## Motor Control Motor Data Motor NP Volts 041

Elapsed Run Time 010

DC Bus Voltage 012

Analog In1 Value 016

## Motor NP FLA 042 Motor NP Hertz 043 Motor NP RPM 044

Torq Attributes Torque Perf Mode 053 Motor Control

Maximum Freq 055

Break Voltage 071

Break Frequency 072

Overspeed Limit 083

Skip Frequency 1 084

Skip Frequency 2 085

Speed Ref A Lo 092

Speed Ref B Sel 093

PI Integral Time 129

PI Prop Gain 130

PI Lower Limit 131

PI Upper Limit 132

PI Preload 133

Decel Time 1 142

Decel Time 2 143

Auto Rstrt Delay 175

Sleep Wake-Mode 178

Sleep-Wake Ref 179

Wake Level 180

Drive Memory Param Access Lvl 196 Reset To Defalts 197 Language 201

Dig Out Status 217

Analog In 2 Hi 325

Analog In 1 Lo 323

Analog In 2 Lo 326

Analog Out1 Hi 343

Analog Out1 Lo 344

Dig Out2 Level 385

Dig Out1 OnTime 382

Dig Out2 OnTime 386

(1) Only available on Standard Control drives with firmware version 3.001 or above.

<!-- image -->

|                                   |                                                                                         | Maximum Voltage 054                                                                                              |                                                                                      |
|-----------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Speed Command Speed Command       | Volts per Hertz Start/Acc Boost 069 Spd Mode & Limits Speed                             | Run Boost 070 Speed Mode 080 Minimum Speed 081 Maximum Speed 082 Speed Ref A Sel 090                             | Run Boost 070 Speed Mode 080 Minimum Speed 081 Maximum Speed 082 Speed Ref A Sel 090 |
|                                   | References Discrete Speeds                                                              | Speed Ref A Hi 091 Preset Speed 2-4 102-104                                                                      |                                                                                      |
|                                   | Process PI PI Configuration 124                                                         | PI Control 125                                                                                                   |                                                                                      |
|                                   |                                                                                         | PI Reference Sel 126 PI Setpoint 127                                                                             |                                                                                      |
| Dynamic Control                   | Ramp Rates Accel Time 1 140                                                             | PI Feedback Sel 128 Accel Time 2 141                                                                             |                                                                                      |
| Dynamic Control                   | Stop/Brake                                                                              | Load Limits Current Lmt Val 148 PWM Frequency 151 Stop Mode A 155                                                |                                                                                      |
|                                   | Modes                                                                                   |                                                                                                                  |                                                                                      |
|                                   | Restart Modes Start At PowerUp 168                                                      | Flying Start En 169 Flying StartGain 170 Auto Rstrt Tries 174 Power Loss Power Loss Mode 184 Power Loss Time 185 |                                                                                      |
| Utility                           | Direction Config Direction Mode 190 HIM Ref Config Save HIM Ref 192 Man Ref Preload 193 |                                                                                                                  |                                                                                      |
| Utility                           |                                                                                         |                                                                                                                  |                                                                                      |
|                                   | Diagnostics Start Inhibits 214                                                          | Dig In Status 216                                                                                                |                                                                                      |
| Inputs & Outputs Inputs & Outputs | Analog Inputs Anlg In Config 320                                                        | Anlg In Sqr Root 321 Analog In 1 Hi 322                                                                          |                                                                                      |
|                                   | Analog Outputs Anlg Out Config 340                                                      | Analog Out1 Sel 342                                                                                              |                                                                                      |
|                                   |                                                                                         | Digital Inputs Digital In1-6 Sel 361-366                                                                         |                                                                                      |
|                                   | Digital Outputs Digital Out1 Sel 380                                                    |                                                                                                                  |                                                                                      |
|                                   |                                                                                         | Digital Out2 Sel 384                                                                                             |                                                                                      |
|                                   |                                                                                         | Dig Out1 Level 381                                                                                               |                                                                                      |

Motor NP Power 045

Mtr NP Pwr Units 046

Skip Frequency 3 086

Skip Freq Band 087

Speed Ref B Hi 094

Speed Ref B Lo 095

PI Status 134

PI Ref Meter 135

PI Fdback Meter 136

PI Error Meter 137

PI Output Meter 138

S Curve % 146

Wake Time 181

Sleep Level 182

Sleep Time 183

Anlg In 1 Loss 324

Anlg In 2 Loss 327

Dig Out1 OffTime 383

Dig Out2 OffTime 387

20B-UM001.book Page 12 Thursday, June 20, 2013 1:55 PM

1-12

File

Programming and Parameters

Monitor File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

001 [Output Freq]

Output frequency present at T1, T2 &amp; T3

(U, V &amp; W)

Standard

[Commanded Freq]

Value of the active frequency command.

002

Values

Default:

Min/Max:

Units:

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

| [Commanded Speed] Value of the active Speed/Frequency Vector                                                                            | Default: Units:        |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Reference. Displayed in Hz or RPM, depending on value of [Speed Units]. 003 [Output Current] The total output current present at T1, T2 | Default:               |
| & T3 (U, V & W). 004 [Torque Current]                                                                                                   | Units: Default:        |
| Based on the motor, the amount of current that is in phase with the fundamental voltage component.                                      | Units: Default:        |
|                                                                                                                                         | Units:                 |
| 005 [Flux Current]                                                                                                                      | Default:               |
| Amount of current that is out of phase with the fundamental voltage component.                                                          | Units: Default:        |
| 006 [Output Voltage] Output voltage present at terminals T1,                                                                            | Units: Default:        |
| T2 & T3 (U, V & W).                                                                                                                     | Units: Default: Units: |
| 007 [Output Power] Output power present at T1, T2 & T3 (U,                                                                              | Units: Default: Units: |
| V & W).                                                                                                                                 | Default:               |
| 008 [Output Powr Fctr] Output power factor.                                                                                             | Units:                 |
| 009 [Elapsed MWh] Accumulated output energy of the drive. 32                                                                            | Default:               |
| 010 [Elapsed Run Time]                                                                                                                  | Units: Default: Units: |
| power.                                                                                                                                  | Units: Default: Units: |

Read Only

–/+[Maximum Freq]

0.1 Hz

Read Only

–/+[Maximum Speed]

0.1 Hz

Read Only

–/+[Maximum Speed]

0.1 Hz

0.1 RPM

Read Only

0.0/Drive Rated Amps × 2

0.1 Amps

Read Only

Drive Rating × –2/+2

0.1 Amps

Read Only

Drive Rating × –2/+2

0.1 Amps

Read Only

0.0/Drive Rated Volts

0.1 VAC

Read Only

0.0/Drive Rated kW × 2

0.1 kW

Read Only

0.00/1.00

0.01

Read Only

0.0/214748352.0 MWh

0.1 MWh

Read Only

0.0/214748352.0 Hrs

0.1 Hrs

Related

079

20B-UM001.book Page 13 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

011

See page 1-2 for symbol descriptions

Standard

[MOP Frequency]

Value of the signal at MOP (Motor

Operated Potentiometer).

See description above.

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

Units:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

Read Only

–/+[Maximum Freq]

0.1 Hz

Read Only

–/+[Maximum Speed]

0.1 Hz

0.1 RPM

Read Only

0.0/Based on Drive Rating

0.1 VDC

Read Only

0.0/Based on Drive Rating

0.1 VDC

Read Only

0.0/429496729.5 kWh

0.1 kWh

Read Only

0.000/20.000 mA

–/+10.000V

0.001 mA

0.001 Volt

Read Only

–/+400.0 Hz

–/+24000.0 RPM

0.1 Hz

0.1 RPM

Read Only

–/+400.0 Hz

–/+24000.0 RPM

0.1 Hz

0.1 RPM

Read Only

–/+800.0%

0.1%

Read Only

–/+400.0 Hz

–/+24000.0 RPM

0.1 Hz

0.1 RPM

1-13

Related

079

079

079

053

20B-UM001.book Page 14 Thursday, June 20, 2013 1:55 PM

1-14

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

026 [Rated kW]

32

Drive power rating.

027 [Rated Volts]

The drive input voltage class (208, 240,

400 etc.).

<!-- image -->

| MONITOR Drive Data 028 [Rated Amps]      |                                      | Units: Default:   |
|------|--------------------------------------|-------------------|
|      | The drive rated output current.      | Units: Default:   |
|      | 029 [Control SW Ver]                 |                   |
|      | Main Control Board software version. | Units:            |
|      | Motor Control File                   |                   |
| File | GroupNo.Parameter Name & Description See page 1-2 for symbol descriptions                                      | Values            |

See page 1-2 for symbol descriptions

040 [Motor Type]

Set to match the type of motor connected.

(1) Important: Selecting option 1 or 2

also requires selection of "Custom V/Hz,"

option 2 in parameter 53.

<!-- image -->

Values

Default:

Min/Max:

Units:

Default:

Min/Max:

Min/Max:

Min/Max:

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Read Only

0.00/3000.00 kW

0.01 kW

Read Only

0.0/6553.5 VAC

0.0/65535.0 VAC

0.1 VAC

Read Only

0.0/6553.5 Amps

0.0/65535.0 Amps

Vector

0.1 Amps

Read Only

0.000/256.256

0.000/65535.000

0.001

0

0

1

2

"Induction"

"Induction"

"Synchr Reluc"(1)

"Synchr PM"(1)

Based on Drive Rating

0.0/[Rated Volts]

0.1 VAC

Based on Drive Rating

0.0/[Rated Amps] × 2

0.1 Amps

Based on Drive Cat. No.

5.0/400.0 Hz

0.1 Hz

1750 RPM

1750.0 RPM

Vector

60/2400 RPM

60.0/24000.0 RPM

1 RPM

1.0 RPM

Vector

Vector

Vector

Vector

Related

196

Related

053

047

048

20B-UM001.book Page 15 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

045 [Motor NP Power]

Set to the motor nameplate rated power.

32

046

[Mtr NP Pwr Units]

Programming and Parameters

Values

Default:

Min/Max:

Units:

Default:

Options:

Options:

Min/Max:

Min/Max:

Min/Max:

Options:

Options:

Min/Max:

Standard

<!-- image -->

Based on Drive Rating

0.00/100.00

0.00/1000.00

Vector

0.01 kW/HP

See [Mtr NP Pwr Units]

Drive Rating Based

0

1

0

1

2

"Horsepower"

"kiloWatts"

Drive Rating Based

"Horsepower"

"kiloWatts"

"Convert HP"

3

"Convert kW"

Motor NP Hz/3

0.0/Motor NP Hz

0.1 Hz

1.00

0.20/2.00

0.01

4

2/40

1 Pole

0

"Sensrls Vect"

0

1

2

3

0

0

1

2

3

"Sensrls Vect"

"SV Economize"

"Custom V/Hz"

"Fan/Pmp V/Hz"

"Sensrls Vect"

"Sensrls Vect"

"SV Economize"

"Custom V/Hz"

"Fan/Pmp V/Hz"

4

"FVC Vector"

Drive Rated Volts

Rated Volts x 0.25/Rated

Volts

0.1 VAC

1-15

Related

046

042

220

042

220

20B-UM001.book Page 16 Thursday, June 20, 2013 1:55 PM

1-16

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

055 [Maximum Freq]

Sets the highest frequency the drive will output. Refer to [Overspeed Limit], 083.

056 [Compensation]

Enables/disables correction options.

k
(5)

<!-- image -->

Values

Default:

Min/Max:

Units:

110.0 or 130.0 Hz

5.0/420.0 Hz

0.1 Hz

v
(4)

Enable JerkReflect Wave
 
(1
AutoCalc
(
ag
(

k
(1)

c
(2)

EnIxo AutoCXsistor Diag
(
Rev
Adapt

k

Enable JRefIxo AutoCalc
(
stor Diag
(

1

1 1 0 1

1=Enabled

1

0=Disabled x =Reserved

For current limit (except FVC Vector mode).

Standard Control Option Only.

Vector Control Option Only.

Vector firmware 2.003 &amp; later.

Vector firmware 3.001 &amp; later.

Reflect Wave Disables reflected wave overvoltage protection for long cable

Enable Jerk In non-FVC Vector modes, disabling jerk removes a short

S-curve at the start of the accel/decel ramp.

Ixo AutoCalc Not functional – reserved for future enhancements.

Xsistor Diag Disables power transistor power diagnostic tests which run at

Rs Adapt FVC w/Encoder Only - Disabling may improve torque regulation

Mtr Lead Rev Reverses the phase rotation of the applied voltage, effectively

PWM Freq Lock Keeps the PWM frequency from decreasing to 2 kHz at low operating frequencies in FVC Vector mode without encoder.

0

0

"Manual"

"Manual"

1

"Automatic"

0.00 Secs

0.0 Secs

Vector

0.00/5.00 Secs

0.0/5.0 Secs

Vector

0.000/5.000 Secs

0.01 Secs

0.1 Secs

Vector

0.001 Secs

500

0/32767

1

g
(3)

Options:

Min/Max:

Min/Max:

v3

v3

Related

083

053

058

053

058

20B-UM001.book Page 17 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

061 [Autotune]

Provides a manual or automatic method for setting [IR Voltage Drop], [Flux

Vect," "SV Economize" or "FVC Vector."

"Ready" (0) = Parameter returns to this setting following a "Static Tune" or "Rotate

Tune." It also permits manually setting [IR Voltage Drop], [Ixo Voltage Drop] and

"Static Tune" (1) = A temporary command that initiates a non-rotational motor stator resistance test for the best possible automatic setting of [IR Voltage Drop]

in all valid modes and a non-rotational motor leakage inductance test for the best possible automatic setting of [Ixo Voltage Drop] in "FVC Vector" mode. A start

command is required following initiation of this setting. The parameter returns to

"Ready" (0) following the test, at which time another start transition is required to operate the drive in normal mode. Used when motor cannot be rotated.

"Rotate Tune" (2) = A temporary command that initiates a "Static Tune" followed by a rotational test for the best possible automatic setting of [Flux Current Ref]. In

"FVC Vector" mode, with encoder feedback, a test for the best possible automatic setting of [Slip RPM @ FLA] is also run. A start command is required following

initiation of this setting. The parameter returns to "Ready" (0) following the test, at which time another start transition is required to operate the drive in normal

mode. Important: Used when motor is uncoupled from the load. Results may not be valid if a load is coupled to the motor during this procedure.

ATTENTION: Rotation of the motor in an undesired direction can occur during this procedure. To guard against possible injury and/or

equipment damage, it is recommended that the motor be disconnected from the load before proceeding.

"Calculate" (3) = This setting uses motor nameplate data to automatically set [IR

Voltage Drop], [Ixo Voltage Drop], [Flux Current Ref] and [Slip RPM @ FLA].

Based on Drive Rating

0.0/[Motor NP Volts]× 0.25

0.1 VAC

Based on Drive Rating

0.00/[Motor NP FLA]

0.01 Amps

Based on Drive Rating

0.0/230.0, 480.0, 575 VAC

0.1 VAC

<!-- image -->

|                                                                                                                              | [Flux Current Ref].                                                                                                          |                                                                                                                              |          |                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| MOTOR CONTROL Torq Attributes                                                                                                                              | MOTOR CONTROL Torq Attributes                                                                                                                              | MOTOR CONTROL Torq Attributes                                                                                                                              | MOTOR CONTROL Torq Attributes          | MOTOR CONTROL Torq Attributes                                                                                                                              |
| 062 [IR Voltage Drop] Value of voltage drop across the resis tance of the motor stator at rated motor !                                                                                                                              | 062 [IR Voltage Drop] Value of voltage drop across the resis tance of the motor stator at rated motor !                                                                                                                              | 062 [IR Voltage Drop] Value of voltage drop across the resis tance of the motor stator at rated motor !                                                                                                                              | Default: | 062 [IR Voltage Drop] Value of voltage drop across the resis tance of the motor stator at rated motor !                                                                                                                              |
| current. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize” or “FVC Vector.” Units: 063 [Flux Current Ref] | current. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize” or “FVC Vector.” Units: 063 [Flux Current Ref] | current. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize” or “FVC Vector.” Units: 063 [Flux Current Ref] | Default: | current. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize” or “FVC Vector.” Units: 063 [Flux Current Ref] |
| Value of amps for full motor flux. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize or “FVC Vector.” 32   | Value of amps for full motor flux. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize or “FVC Vector.” 32   | Value of amps for full motor flux. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize or “FVC Vector.” 32   | Units:   | Value of amps for full motor flux. Used only when parameter 53 is set to “Sensrls Vect,” “SV Economize or “FVC Vector.” 32   |
|                                                                                                                              |                                                                                                                              | Default:                                                                                                                     |          |                                                                                                                              |
| 064 [Ixo Voltage Drop] set to “Sensrls Vect,” “SV Economize or                                                               |                                                                                                                              | Value of voltage drop across the leakage inductance of the motor at rated motor current. Used only when parameter 53 is      | Units:   |                                                                                                                              |
|                                                                                                                              | “FVC Vector.”                                                                                                                |                                                                                                                              |          |                                                                                                                              |

Programming and Parameters

Values

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

3

0

1

2

3

"Calculate"

"Ready"

"Static Tune"

"Rotate Tune"

"Calculate"

1-17

Related

053

062

053

061

053

061

20B-UM001.book Page 18 Thursday, June 20, 2013 1:55 PM

1-18

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

066

FV

067

Vector

[Autotune Torque]

Specifies motor torque applied to the motor during the flux current and inertia

tests performed during an autotune.

Vector

[Inertia Autotune]

Provides an automatic method of setting

Values

Default:

Min/Max:

Units:

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

50.0%

0.0/150.0%

0.1%

0

0

1

1

24

0

1

2

3-17

18-22

23

24

25-28

"Ready"

"Ready"

"Inertia Tune"

"Torque Setpt"

"Disabled"

"Torque Setpt"

"Torque Stpt1"(2)

"Analog In 1"

"Analog In 2"

"Reserved"

"DPI Port 1-5"(1)

"Reserved"

"Disabled"

"Scale Block1-4"(2)

29

"Torque Stpt2"(2)

100.0%

100.0%

–/+800.0%

0.1%

0.0%

0.0%

–/+800.0%

0.1%

1.0

0.1/3276.7

0.1

1.0

–/+32767.0

0.1

Related

053

053

450

053

053

053

053

053

20B-UM001.book Page 19 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

435

FV

436

See page 1-2 for symbol descriptions

Vector

Vector v3

[Torque Setpoint]

[Torque Setpoint1]

Provides an internal fixed value for

Vector

[Pos Torque Limit]

Programming and Parameters

Values

Default:

Min/Max:

Units:

Default:

Min/Max:

Min/Max:

Min/Max:

0 0 0 0

<!-- image -->

Min/Max:

Min/Max:

Min/Max:

0.0%

–/+800.0%

0.1%

200.0%

0.0/800.0%

0.1%

–200.0%

–800.0/0.0%

0.1%

0.0%

–/+800.0%

0.1%

Read Only

1=Condition True

0=Condition False x =Reserved

1C
RevPhaseMot
EconomizeFluxBrake
DrvVoltLimVltLimStator

0 0 0 0

1=Condition True

0=Condition False x =Reserved

Read Only

–/+32767.0 Amps

0.01 Amps

Based on Drive Rating

0.0/[Motor NP Volts] x 0.25

0.1 VAC

Based on Drive Rating

0.0/[Motor NP Volts] x 0.25

0.1 VAC

1-19

Related

053

053

053

053

053

053

070

053

069

20B-UM001.book Page 20 Thursday, June 20, 2013 1:55 PM

1-20

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

071 [Break Voltage]

Volts per Hertz

Sets the voltage the drive will output at

[Break Frequency]. Refer to parameter

083 [Overspeed Limit].

072 [Break Frequency]

Sets the frequency the drive will output at

Values

Default:

Min/Max:

Units:

Default:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

| 412  Vector                                                                                                                                                                               | [Break Voltage]. Refer to parameter 083. [Motor Fdbk Type]                                                                                                                                                          | Units: Default:                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
|                                                                                                                                                                                           | Selects the encoder type; single channel or quadrature. Options 1 & 3 detect a                                                                                                                                      | Options:                        |
|                                                                                                                                                                                           | loss of encoder signal (when using differential inputs) regardless of the [Feedback Select], param. 080 setting.                                                                                                    |                                 |
|                                                                                                                                                                                           | For FVC Vector mode, use a quadrature encoder only (option 0/1). If a single channel encoder is used (option 2/3) in sensorless vector or V/Hz mode, select                                                         |                                 |
| MOTOR CONTROL  Speed Feedback 413  x motor poles). 414  Displays raw encoder pulse count. For single channel encoders, this count will increase (per rev.) by the amount in Vector Vector | “Reverse Dis” (option 2) in param. 190. [Encoder PPR] Contains the encoder pulses per revolution. For improved operation in FVC Vector mode, PPR should be ≥ (64 [Enc Position Fdbk]                                | Default: Units: Default: Units: |
| 415  Provides a monitoring point that reflects Vector                                                                                                                                     | [Encoder PPR]. For quadrature encoders this count will increase by 4 times the amount defined in [Encoder PPR]. [Encoder Speed]                                                                                     | Default:                        |
| 416  Selects the type of feedback filter desired. “Light” uses a 35/49 radian Vector                                                                                                      | speed as seen from the feedback device. [Fdbk Filter Sel]                                                                                                                                                           | Units: Default: Options:        |
| 419  FV Vector                                                                                                                                                                            | feedback filter. “Heavy” uses a 20/40 radian feedback filter. [Notch Filter Freq] Sets the center frequency for an optional 2-pole notch filter. Filter is applied to the torque command. “0” disables this filter. | Default: Units:                 |

[Motor NP Volts] × 0.25

0.0/[Motor NP Volts]

0.1 VAC

[Motor NP Hz] × 0.25

0.0/[Maximum Freq]

0.1 Hz

0

"Quadrature"

0

1

2

"Quadrature"

"Quad Check"

"Single Chan"

3

"Single Check"

1024 PPR

2/20000 PPR

1 PPR

Read Only

–/+2147483647

1

Read Only

–/+420.0 Hz

–/+25200.0 RPM

0.1 Hz

0.1 RPM

0

"None"

0

1

"None"

"Light"

2

"Heavy"

0.0 Hz

0.0/500.0 Hz

0.1 Hz

Related

053

072

053

071

079

053

20B-UM001.book Page 21 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

420

FV

421

See page 1-2 for symbol descriptions

Vector

[Notch Filter K]

Sets the gain for the 2-pole notch filter.

Latches the raw encoder count at each marker pulse.

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

Units:

Min/Max:

Options:

<!-- image -->

079

See page 1-2 for symbol descriptions

Vector

[Speed Units]

Selects the units to be used for all speed related parameters. Options 0 &amp; 1

indicate status only. Options 2 &amp; 3 will convert/configure the drive for that

selection.

"Convert Hz" (2) - converts all speed

<!-- image -->

Default:

Options:

## SPEED COMMANDSpd Mode &amp; Limits

0.3 Hz

0.1/0.9 Hz

0.1 Hz

Read Only

–/+2147483647

1

64

2/20000

1

0

0

1

2

3

0

0

1

2

3

"Pulse Input"

"Pulse Input"

"Pulse Check"

"Marker Input"

"Marker Check"

"Hz"

"Hz"

"RPM"

"Convert Hz"

"Convert RPM"

1-21

Related

053

Related

20B-UM001.book Page 22 Thursday, June 20, 2013 1:55 PM

1-22

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

080

Standard

[Speed Mode]

Sets the method of speed regulation.

Vector

[Feedback Select]

Selects the source for motor speed

Values

Default:

Options:

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

0

0

1

2

0

0

1

2

3

4

5

"Open Loop"

"Open Loop"

"Slip Comp"

"Process PI"

"Open Loop"

"Open Loop"

"Slip Comp"

"Reserved"

"Encoder"

"Reserved"

"Simulator"

0.0

0.0/[Maximum Speed]

0.1 Hz

0.1 RPM

Vector

50.0 or 60.0 Hz (volt class)

[Motor NP RPM]

5.0/400.0 Hz

75.0/24000.0 RPM

0.1 Hz

0.1 RPM

Vector

10.0 Hz

300.0 RPM

Vector

0.0/20.0 Hz

0.0/600.0 RPM

Vector

0.1 Hz

0.1 RPM

Overspeed

Limit

Max

Speed

Vector

Output

Max

Freq Limit

Freq

Vector

Related

412

152

079

083

092

095

055

079

083

091

094

202

055

079

082

20B-UM001.book Page 23 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

084

See page 1-2 for symbol descriptions

[Skip Frequency 1]

085

086

[Skip Frequency 2]

[Skip Frequency 3]

[Skip Frequency Band] must not equal 0.

087 [Skip Freq Band]

<!-- image -->

Programming and Parameters

Values

Default:

Default:

Default:

Min/Max:

Default:

Min/Max:

Options:

Min/Max:

0.0 Hz

0.0 Hz

0.0 Hz

–/+[Maximum Speed]

0.1 Hz

0.0 Hz

0.0/30.0 Hz

0.1 Hz

1

"Speed Reg"

0

1

2

3

4

5

6

"Zero Torque"

"Speed Reg"

"Torque Reg"

"Min Torq/Spd"

"Max Torq/Spd"

"Sum Torq/Spd"

"Absolute Min"

"Min Torq/Spd" (3) - selects the smallest algebraic value to regulate to when the torque reference and torque generated from the speed regulator are compared.

"Max Torq/Spd" (4) - selects the largest algebraic value when the torque reference and the torque generated from the speed regulator are compared.

"Sum Torq/Spd" (5) - selects the sum of the torque reference and the torque

"Absolute" (6) - selects the smallest absolute algebraic value to regulate to when the torque reference and torque generated from the speed regulator are

0.0 RPM

–[Max Speed]/0.0 Hz

–[Max Speed]/0.0 RPM

0.0 Hz

0.0 RPM

1-23

Related

087

084

085

086

053

20B-UM001.book Page 24 Thursday, June 20, 2013 1:55 PM

1-24

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

090 [Speed Ref A Sel]

Selects the source of the speed reference to the drive unless [Speed Ref

B Sel] or [Preset Speed 1-7] is selected.

(1) See Appendix B for DPI port locations.

<!-- image -->

| 093 [Speed Ref B Sel] See [Speed Ref A Sel] . 094 [Speed Ref B Hi]                                   | 093 [Speed Ref B Sel] See [Speed Ref A Sel] . 094 [Speed Ref B Hi]   |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Scales the upper value of the [Speed Ref B Sel] selection when the source is an 095 [Speed Ref B Lo] | Units: Default:                                                      |
| Scales the lower value of the [Speed Ref B Sel] selection when the source is an                      | Units:                                                               |

Values

Default:

Options:

Min/Max:

Min/Max:

Options:

Min/Max:

Min/Max:

2

1

2

3-6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23-24

25

26

27

"Analog In 2"

"Analog In 1"

"Analog In 2"

"Reserved"

"Pulse In"

"Encoder"

"MOP Level"

"Reserved"

"Preset Spd1"

"Preset Spd2"

"Preset Spd3"

"Preset Spd4"

"Preset Spd5"

"Preset Spd6"

"Preset Spd7"

"DPI Port 1"(1)

"DPI Port 2"(1)

"DPI Port 3"(1)

"DPI Port 4"(1)

"DPI Port 5"(1)

"Reserved"

"Scale Block1"(2)

"Scale Block2"(2)

"Scale Block3"(2)

28

"Scale Block4"(2)

[Maximum Speed]

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

0.0

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

11 "Preset Spd1"

See [Speed Ref A

Sel]

[Maximum Speed]

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

0.0

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

Related

002

091

thru

093

101

thru

107

117

thru

120

192

thru

194

213

272

273

320

361

thru

366

079

082

079

081

See

090

079

093

079

090

093

20B-UM001.book Page 25 Thursday, June 20, 2013 1:55 PM

File

Group No.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

096 [TB Man Ref Sel]

Sets the manual speed reference source when a digital input is configured for

"Auto/Manual."

was selected for any of the following:

- [Trim In Select]

<!-- image -->

Programming and Parameters

Values

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

1

1

2

3-8

"Analog In 1"

"Analog In 1"

"Analog In 2"(1)

"Reserved"

9

"MOP Level"

[Maximum Speed]

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

0.0

–/+[Maximum Speed]

0.1 Hz

0.01 RPM

Vector

Read Only

–/+420.0 Hz

–/+25200.0 RPM

0.1 Hz

0.1 RPM

10.0 Hz

–/+[Maximum Speed]

0.1 Hz

10.0 Hz

300.0 RPM

–/+[Maximum Speed]

0.1 Hz

1 RPM

5.0 Hz/150 RPM

Vector

10.0 Hz/300 RPM

Vector

20.0 Hz/600 RPM

Vector

30.0 Hz/900 RPM

Vector

40.0 Hz/1200 RPM

Vector

50.0 Hz/1500 RPM

Vector

60.0 Hz/1800 RPM

Vector

–/+[Maximum Speed]

0.1 Hz

1 RPM

Vector

10.0 Hz

300.0 RPM

–/+[Maximum Speed]

0.1 Hz

1 RPM

1-25

Related

097

098

079

096

079

096

079

079

090

093

20B-UM001.book Page 26 Thursday, June 20, 2013 1:55 PM

1-26

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

116

Vector v3

[Trim % Setpoint]

Adds or subtracts a percentage of the speed reference or maximum speed.

Dependent on the setting of [Trim Out

Select], parameter 118.

117 [Trim In Select]

Values

Default:

Min/Max:

Units:

Default:

<!-- image -->

Min/Max:

Min/Max:

Min/Max:

0.0%

–/+200.0%

0.1%

2 "Analog In 2"

See [Speed Ref A

Sel]

1
Add or % *
Trim Ref B
Trim Ref A

0

0

1

Min/Max:

Min/Max:

1=Trimmed/%

0=Not Trimmed/Add x =Reserved

60.0 Hz

–/+[Maximum Speed]

0.1 Hz

1 RPM/%

Vector

0.0 Hz

–/+[Maximum Speed]

0.1 Hz

1 RPM/%

Vector

Important: Parameters in the Slip Comp Group are used to enable and tune the

Slip Compensation Regulator. In order to allow the regulator to control drive operation, parameter 080 [Speed Mode] must be set to 1 "Slip Comp".

Based on [Motor NP RPM]

0.0/1200.0 RPM

0.1 RPM

40.0

1.0/100.0

0.1

Read Only

–/+300.0 RPM

0.1 RPM

Related

118

090

093

117

119

120

079

082

117

079

117

061

080

122

123

080

121

122

080

121

122

20B-UM001.book Page 27 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

Programming and Parameters

Values

Important: Parameters in the Process PI Group are used to enable and tune the

PI Loop. In order to allow the PI Loop to control drive operation, program the following:

"Process PI" and parameter 125, bit 0 must be set to "1, Enabled.".

Vector Control Option – Only requires setting parameter 125, bit 0 to "1, Enabled."

1
% of Ref **
Torque Trim *
Anti-Wind Up
Stop Mode
Feedbak Sqrt
Zero Clamp
Ramp Ref
Preload Mode
Invert Error
Excl Mode

0 0 0 0

0

1=Enabled

1

0=Disabled x =Reserved

PI Reset
PI Hold
PI Enable

0

0

1=Enabled

1

Options:

Min/Max:

0=Disabled x =Reserved

"PI Setpoint"

"PI Setpoint"

"Analog In 1"

"Analog In 2"

"Reserved"

"Pulse In"

"Encoder"

"MOP Level"

"Master Ref"

"Preset Spd1-7"

"DPI Port 1-5"

"Reserved"

"Scale Block 1"(1)

"Scale Block 2"(1)

"Scale Block 3"(1)

0

0

1

2

3-6

7

8

9

10

11-17

18-22

23-24

25

26

27

28

"Scale Block 4"(1)

50.00%

–/+100.00% of Maximum

Process Value

0.01%

<!-- image -->

1-27

Related

124

thru

138

080

024

124

thru

138

124

thru

138

20B-UM001.book Page 28 Thursday, June 20, 2013 1:55 PM

1-28

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

128 [PI Feedback Sel]

Selects the source of the PI feedback.

129 [PI Integral Time]

Time required for the integral component to reach 100% of [PI Error Meter]. Not

Values

Default:

Options:

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

Min/Max:

Min/Max:

2 "Analog In 2"

See [PI Reference

Sel]

.

2.00 Secs

0.00/100.00 Secs

0.01 Secs

1.0

0.00/100.00

0.01

–[Maximum Freq]

–100%

Vector

–/+400.0 Hz

–/+800.0%

Vector

0.1 Hz

0.1%

Vector

+[Maximum Freq]

100%

Vector

–/+400.0 Hz

–/+800.0%

Vector

0.1 Hz

0.1%

Vector

0.0 Hz

100.0%

Vector

[PI Lower Limit]/

[PI Upper Limit]

0.1 Hz

0.1%

Vector

Read Only

PI InLimit
PI Reset
PI Hold
PI Enabled

0 0 0 0

1=Condition True

0=Condition False x =Reserved

Read Only

–/+100.0%

0.1%

Read Only

–/+100.0%

0.1%

Related

124

thru

138

124

thru

138

124

thru

138

079

124

thru

138

079

124

thru

138

079

124

thru

138

124

thru

138

124

thru

138

124

thru

138

20B-UM001.book Page 29 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

137 [PI Error Meter]

Present value of the PI error.

Present value of the PI output.

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

Read Only

–/+100.0%

–/+200.0%

0.1%

Read Only

–/+100.0 Hz

–/+100.0%

Vector

–/+800.0%

0.1 Hz

0.1%

Vector

0.0 Radians

0.0/240.0 Radians

0.1 Radians

0.00 Secs

0.00/100.00 Secs

0.01 Secs

100.0%

–/+100.0%

0.1%

–100.0%

–/+100.0%

0.1%

100.0%

–/+100.0%

0.1%

0.0%

–/+100.0%

0.1%

7.0

0.0/4000.0

0.1

v3

v3

1-29

Related

124

thru

138

124

thru

138

137

053

20B-UM001.book Page 30 Thursday, June 20, 2013 1:55 PM

1-30

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

446

FV

Vector

[Kp Speed Loop]

Controls the proportional error gain of the speed regulator. The drive automatically

adjusts [Kp Speed Loop] when a non-zero value is entered for [Speed

Desired BW] or an auto-tune is performed. Typically, manual adjustment

<!-- image -->

Values

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

6.3

0.0/200.0

0.1

0.0

0.0/0.5

0.1

0.0 Radians/Sec

0.0/250.0 Radians/Sec

0.1 Radians/Sec

1.25 Secs

0.10 Secs v3

0.1/600.0 Secs

0.01/600.00

v3

0.1 Secs

0.01 Secs v3

Read Only

–/+800.0%/Hz/RPM

0.1%/Hz/RPM

Related

053

053

053

053

053

121

079

20B-UM001.book Page 31 Thursday, June 20, 2013 1:55 PM

Dynamic Control File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

140

[Accel Time 1]

141

File

Sets the rate of accel for all speed increases.

Max Speed

Accel Time

Accel Rate

<!-- image -->

=

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

Options:

Min/Max:

Min/Max:

Options:

Min/Max:

10.0 Secs

10.0 Secs

0.1/3600.0 Secs

0.0/3600.0 Secs

0.1 Secs

10.0 Secs

10.0 Secs

0.1/3600.0 Secs

0.0/3600.0 Secs

0.1 Secs

0%

0/100%

1%

0

0

1

"Cur Lim Val"

"Cur Lim Val"

"Analog In 1"

2

"Analog In 2"

[Rated Amps] × 1.5

(Equation yields approxi- mate default value.)

Based on Drive Rating

0.1 Amps

250

0/5000

1

3

0

1

2

3

4 kHz

2 kHz

(Frames 4-6, 600/690VAC)

2/10 kHz

2/4/8/10 kHz

"Both–PWM 1st"

"Disabled"

"Reduce CLim"

"Reduce PWM"

"Both–PWM 1st"

v3

v3

1-31

Related

142

143

146

361

140

141

146

361

140

thru

143

146

149

147

149

147

148

219

20B-UM001.book Page 32 Thursday, June 20, 2013 1:55 PM

1-32

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

152

Vector

[Droop RPM @ FLA]

Selects amount of droop that the speed reference is reduced when at full load

torque. Zero disables the droop function.

Important: Selecting "Slip Comp" with parameter 080 in conjunction with

<!-- image -->

Values

Default:

Min/Max:

Units:

Min/Max:

Min/Max:

0.0 RPM

0.0/200.0 RPM

0.1 RPM

–50.0%

–800.0/0.0%

0.1%

400.0%

1.0/800.0%

0.1%

0

0

1

1

0

0

1

2

3

0

0

1

2

"Disabled"

"Disabled"

"Enabled"

"Ramp"

"Coast"

"Coast"

"Ramp"(1)

"Ramp to Hold"(1)

"DC Brake"

"DC Brake Lvl"

"DC Brake Lvl"

"Analog In 1"

"Analog In 2"

Related

053

053

161

162

157

158

159

155

156

158

159

20B-UM001.book Page 33 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

158 [DC Brake Level]

Defines the DC brake current level injected into the motor when "DC Brake"

function is created by a PWM algorithm and may not generate the smooth

ATTENTION: If a hazard of injury due to movement of equipment or material exists, an auxiliary mechanical braking device must be

ATTENTION: This feature should not be used with synchronous or permanent magnet motors. Motors may be demagnetized during

0.0 Secs

0.0/90.0 Secs

0.1 Secs

450

0/5000

1

1

4

0

1

2

3

4

"Adjust Freq"

"Both-Frq 1st"

"Disabled"

"Adjust Freq"

"Dynamic Brak"

"Both-DB 1st"

"Both-Frq 1st"

ATTENTION: The drive does not offer protection for externally mounted brake resistors. A risk of fire exists if external braking

resistors are not protected. External resistor packages must be self-protected from over temperature or the protective circuit shown

in Figure C.1 on page C-1 (or equivalent) must be supplied.

Programming and Parameters

Values

Default:

Min/Max:

Units:

<!-- image -->

Min/Max:

Min/Max:

Options:

[Rated Amps]

0/[Rated Amps] × 1.5

(Equation yields approximate maximum

value.)

0.1 Amps

1-33

Related

155

thru

158

161

162

160

163

20B-UM001.book Page 34 Thursday, June 20, 2013 1:55 PM

1-34

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

163 [DB Resistor Type]

Selects whether the internal or an external DB resistor will be used.

Important: In 0-3 Frame drives, only one

DB resistor can be connected to the drive. Connecting both an internal &amp;

ATTENTION: Equipment damage may result if a drive mounted

(internal) resistor is installed and this parameter is set to "External

Res" or "None." Thermal protection for the internal resistor will be disabled, resulting in possible device damage. Also see

1500

0/10000

1

1000

0/10000

1

0

0

"Disabled"

"Disabled"

1

"Enabled"

0.0 Secs

0.0/30.0 Secs

0.1 Secs

0

"Disabled"

0

1

"Disabled"

"Enabled"

ATTENTION: Equipment damage and/or personal injury may result if this parameter is used in an inappropriate application. Do not use

this function without considering applicable local, national and international codes, standards, regulations or industry guidelines.

<!-- image -->

Values

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

0

2

0

1

2

"Internal Res"

"None"

Vector

"Internal Res"

"External Res"

"None"

Related

161

162

20B-UM001.book Page 35 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

169 [Flying Start En]

Enables/disables the function which reconnects to a spinning motor at actual

using an encoder.

<!-- image -->

Programming and Parameters

Values

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

0

0

1

"Disabled"

"Disabled"

"Enabled"

4000

20/32767

1

0

0/9

1

ATTENTION: Equipment damage and/or personal injury may result if this parameter is used in an inappropriate application. Do Not use

this function without considering applicable local, national and international codes, standards, regulations or industry guidelines.

1.0 Secs

0.5/30.0 Secs

0.1 Secs

1-35

Related

170

169

175

174

20B-UM001.book Page 36 Thursday, June 20, 2013 1:55 PM

1-36

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

178 [Sleep-Wake Mode]

Enables/disables the Sleep/Wake function. Important: When enabled, the

following conditions must be met:

·

·

A proper value must be programmed for [Sleep Level] &amp; [Wake Level].

A speed reference must be selected

ATTENTION: Enabling the Sleep-Wake function can cause unexpected machine operation during the Wake mode. Equipment

damage and/or personal injury can result if this parameter is used in an inappropriate application. Do Not use this function without

considering the information below and in Appendix C. In addition, all applicable local, national &amp; international codes, standards,

regulations or industry guidelines must be considered

After Power-Up After a Drive Fault After a Stop Command

Reset by Clear

Faults (TB) HIM or TB

Stop Closed

Stop Closed

Wake Signal

Enable Closed

Wake Signal

Run Closed

Wake Signal

Direct Mode

Analog Sig. &gt; Sleep Level(6)

Invert Mode

Analog Sig. &lt; Sleep Level(6)
(4)

g gp 
New Start or Run Cmd.(4)

Enable Closed

Direct Mode

Analog Sig. &gt; Sleep Level(6)

Invert Mode

Analog Sig. &lt; Sleep Level(6)
(4)

g gp 
New Start or Run Cmd.(4)

New Run Cmd.(5)

Wake Signal

When power is cycled, if all of the above conditions are present after power is

If all of the above conditions are present when [Sleep-Wake Mode] is

Refer to Reference Control in the Installation Instructions for information on determining the active speed reference. The Sleep/Wake function and the

Vector firmware 3.xxx &amp; later. For Invert function, refer to [Analog In x Loss].

<!-- image -->

Values

Default:

Options:

0

0

1

2

"Disabled"

"Disabled"

"Direct" (Enabled)

"Invert" (Enabled)(7)

Related

20B-UM001.book Page 37 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

179 [Sleep-Wake Ref]

Selects the source of the input controlling the Sleep-Wake function.

Defines the analog input level that will start the drive.

<!-- image -->

| 181 [Wake Time]                                                                                                                                                         | Units: Default:   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Defines the amount of time at or above [Wake Level] before a Start is issued.                                                                                           | Units:            |
| 182 [Sleep Level] Defines the analog input level that will                                                                                                              | Default:          |
| 183 [Sleep Time] Defines the amount of time at or below [Sleep Level] before a Stop is issued.                                                                          | Default:          |
| 177  [Gnd Warn Level] Sets the level at which a ground warning fault will occur. Configure with [Alarm Vector v3                                                        | Default: Units:   |
| 184 [Power Loss Mode] Sets the reaction to a loss of input power. Power loss is recognized when: •  DC bus voltage is ≤ 73% of [DC Bus Memory] and [Power Loss Mode] is | Default:          |
| set to “Coast”. •  DC bus voltage is ≤ 82% of [DC Bus Memory] and [Power Loss Mode] is set to “Decel”.                                                                  |                   |
| 185 [Power Loss Time] Sets the time that the drive will remain in power loss mode before a fault is issued.                                                             | Default: Units:   |

Programming and Parameters

Values

Default:

Options:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Options:

Min/Max:

2

1

2

"Analog In 2"

"Analog In 1"

"Analog In 2"

6.000 mA, 6.000 Volts

[Sleep Level]/20.000 mA

10.000 Volts

0.001 mA

0.001 Volts

1.0 Secs

0.0 Secs

Vector

0.0/30.0 Secs

0.0/1000.0 Secs

Vector

0.1 Secs

5.000 mA, 5.000 Volts

4.000 mA/[Wake Level]

0.000 Volts/[Wake Level]

0.001 mA

0.001 Volts

1.0 Secs

0.0 Secs

Vector

0.0/30.0 Secs

0.0/1000.0 Secs

0.1 Secs

3.0 Amps

1.0/5.0 Amps

0.1 Amps

0

"Coast"

0

1

2

3

"Coast"

"Decel"

"Continue"

"Coast Input"

4

"Decel Input"

0.5 Secs

0.0/60.0 Secs

0.1 Secs

Vector

1-37

Related

181

180

183

182

259

013

185

184

20B-UM001.book Page 38 Thursday, June 20, 2013 1:55 PM

1-38

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

186 [Power Loss Level]

Sets the level at which the [Power Loss

Mode] selection will occur.

Values

Default:

Min/Max:

Units:

Drive Rated Volts

0.0/999.9 VDC

0.1 VDC

The drive can use the percentages referenced in [Power Loss Mode] or a trigger point can be set for line loss detection as follows:

V

trigger

= [DC Bus Memory] – [Power Loss Level]

A digital input (programmed to "29, Pwr Loss Lvl") is used to toggle between

ATTENTION: Drive damage can occur if proper input impedance

If the value for [Power Loss Level] is greater than 18% of [DC Bus

Memory], the user must provide a minimum line impedance to limit inrush current when the power line recovers. The input impedance

should be equal to or greater than the equivalent of a 5%

transformer with a VA rating 5 times the drives input VA rating.

200.0%

0.0/800.0%

0.1%

0.0 Secs

0.0/30.0 Secs

0.1 Secs

0.0 Secs

0.0/30.0 Secs

0.1 Secs

0

"Unipolar"

0

1

2

"Unipolar"

"Bipolar"

"Reverse Dis"

<!-- image -->

|                                                                                                                                                                                               | fixed percentages and the detection level.                                                                                                                                                    |                                                                                                                                                                                               |                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                               | ! is not provided as explained below.                                                                                                                                                         |                                                                                                                                                                                               |                                                                                                                                                                                               |
| DYNAMIC CONTROL Power Loss 187  [Load Loss Level] Sets the percentage of motor nameplate torque at which a load loss alarm will occur. Default: Vector v3                                                                                                                                                                                               | DYNAMIC CONTROL Power Loss 187  [Load Loss Level] Sets the percentage of motor nameplate torque at which a load loss alarm will occur. Default: Vector v3                                                                                                                                                                                               | DYNAMIC CONTROL Power Loss 187  [Load Loss Level] Sets the percentage of motor nameplate torque at which a load loss alarm will occur. Default: Vector v3                                                                                                                                                                                               | DYNAMIC CONTROL Power Loss 187  [Load Loss Level] Sets the percentage of motor nameplate torque at which a load loss alarm will occur. Default: Vector v3                                                                                                                                                                                               |
| Units: 188  [Load Loss Time] Sets the time that current is below the level set in [Load Loss Level] before a fault occurs. Default: Units: 189  [Shear Pin Time] Default: Vector v3 Vector v3 | Units: 188  [Load Loss Time] Sets the time that current is below the level set in [Load Loss Level] before a fault occurs. Default: Units: 189  [Shear Pin Time] Default: Vector v3 Vector v3 | Units: 188  [Load Loss Time] Sets the time that current is below the level set in [Load Loss Level] before a fault occurs. Default: Units: 189  [Shear Pin Time] Default: Vector v3 Vector v3 | Units: 188  [Load Loss Time] Sets the time that current is below the level set in [Load Loss Level] before a fault occurs. Default: Units: 189  [Shear Pin Time] Default: Vector v3 Vector v3 |
|                                                                                                                                                                                               | Sets the time that the drive is at or above current limit before a fault occurs. Zero disables this feature.                                                                                  | Units:                                                                                                                                                                                        |                                                                                                                                                                                               |
|                                                                                                                                                                                               | GroupNo.Parameter Name & Description See page 1-2 for symbol descriptions                                                                                                                                                                                               | Values                                                                                                                                                                                        |                                                                                                                                                                                               |

Direction Config

See page 1-2 for symbol descriptions

190 [Direction Mode]

Selects method for changing direction.

Mode Direction Change

Unipolar Drive Logic

Bipolar Sign of Reference

Reverse Dis Not Changeable

<!-- image -->

Min/Max:

Min/Max:

Min/Max:

Default:

Options:

UTILITY

Related

211

259

187

238

Related

320

thru

327

361

thru

366

20B-UM001.book Page 39 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

192 [Save HIM Ref]

Enables a feature to save the present frequency reference value issued by the

HIM to Drive memory on power loss. Value is restored to the HIM on power up.

1S
At Powr Down

1=Save at Power Down

0=Do Not Save x =Reserved

0

"Disabled"

Options:

0

1

"Disabled"

"Enabled"

Enables/disables the feature that saves the present MOP frequency reference at

1S
Stop
At Powr Down

1=Save at Power Down

0=Do Not Save x =Reserved

1.0 Hz/s

30.0 RPM/s

Vector

0.2/[Maximum Freq]

6.0/[Maximum Freq]

0.1 Hz/s

0.1 RPM/s

Vector

0

"Basic"

0

1

2

3

4

"Basic"

"Advanced"

"Reserved"

"Fan/Pump"(1)

"Adv Fan/Pump"(1)

<!-- image -->

Programming and Parameters

Values

Min/Max:

Options:

Vector

1-39

Related

20B-UM001.book Page 40 Thursday, June 20, 2013 1:55 PM

1-40

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

197 [Reset To Defalts]

Resets parameters to factory defaults except [Language], [Param Access Lvl],

[Voltage Class] &amp; [TorqProve Cnfg]

(params 196, 201, 202 &amp; 600).

·

Option 1 resets parameters to factory defaults based on [Voltage Class].

<!-- image -->

| Options 2 & 3 will reset parameters to factory defaults and set [Voltage   | Options 2 & 3 will reset parameters to factory defaults and set [Voltage                              | Options 2 & 3 will reset parameters to factory defaults and set [Voltage   |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                                                                            | Important: Frames 5 & 6 - the internal                                                                |                                                                            |
| 200 [Reset Meters]                                                         | Resets selected meters to zero.                                                                       | Default:                                                                   |
| 201 [Language]                                                             | Selects the display language when using an LCD HIM. This parameter is not functional with an LED HIM. | Default:                                                                   |
|                                                                            | Options 6, 8 and 9 are “Reserved.”                                                                    |                                                                            |

Values

Default:

Options:

Options:

Options:

Options:

Options:

0

0

1

2

3

0

0

1

2

3

0

0

1

2

3

0

0

1

2

0

0

1

2

3

4

5

7

10

"Ready"

"Ready"

"Factory"

"Low Voltage"

"High Voltage"

"Ready"

"Ready"

"User Set 1"

"User Set 2"

"User Set 3"

"Ready"

"Ready"

"User Set 1"

"User Set 2"

"User Set 3"

"Ready"

"Ready"

"MWh"

"Elapsed Time"

"Not Selected"

"Not Selected"

"English"

"Francais"

"Español"

"Italiano"

"Deutsch"

"Português"

"Nederlands"

Related

041

thru

047

054

055

062

063

069

thru

072

082

148

158

199

198

20B-UM001.book Page 41 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

202 [Voltage Class]

Configures the drive current rating and associates it with the selected voltage

(i.e. 400 or 480V). Normally used when

3 indicate status only. Selecting Option 4

or 5 will covert/configure the drive. Min/

<!-- image -->

Programming and Parameters

Values

Default:

Options: 2

3

4

5

(1)

Based on Drive Cat.

No.

"Low Voltage"

"High Voltage"

"Reserved"(1)

"Convert Lo V"

"Reserved"(1)

"Convert Hi V"

Vector

Vector firmware v3.001 &amp; up.

Read Only

0/65535

1

Read Only

1
mma
Active
Ready

1 0 1 0

1=Condition True

0=Condition False x =Reserved

Description

Port 0 (TB)

Port 1

Port 2

Port 3

Port 4

Port 5

Port 6

No Local

Control

Min/Max:

Vector

1-41

Related

041

thru

047

054

055

062

063

069

thru

072

082

148

158

210

20B-UM001.book Page 42 Thursday, June 20, 2013 1:55 PM

1-42

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

210 [Drive Status 2]

Present operating condition of the drive.

1
nning
Active
Ready

DPI at 500 k
Motor Overld
Bus Freq Reg
Curr Limit
AutoRst Act
AutoRst Ctdn
DB Active *
AutoTuning
DC Braking
Stopping
JoggingRunning
Activ

0

0

0

0

0

0

0

0

0

0

0 0 0 0

0

0 0 0 0

0 0 0 0

<!-- image -->

Read Only

1=Condition True

0=Condition False x =Reserved

Read Only

1=Condition True

0=Condition False x =Reserved

Read Only

1=Condition True

0=Condition False x =Reserved

1C
TrqPrv Cflct *

0

1=Condition True

0=Condition False x =Reserved

Values

Related

209

212

211

20B-UM001.book Page 43 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

213 [Speed Ref Source]

Displays the source of the speed reference to the drive.

<!-- image -->

Programming and Parameters

Values

Default:

Options: 0

1

2

3-6

7

8

9

10

11-17

18

19

20

21

22

23

24

25

26

27

28

Read Only

"PI Output"

"Analog In 1"

"Analog In 2"

"Reserved"

"Pulse In"

"Encoder"

"MOP Level"

"Jog Speed 1"

"Preset Spd1-7"

"DPI Port 1"

"DPI Port 2"

"DPI Port 3"

"DPI Port 4"

"DPI Port 5"

"Reserved"

"Auto Tune"

Vector

"Jog Speed 2"

Vector

"Scale Block 1"(1)

"Scale Block 2"(1)

"Scale Block 3"(1)

29

"Scale Block 4"(1)

Read Only

pe 2 
Fault

0 0 0 0

1=Inhibit True

0=Inhibit False x =Reserved

Read Only

Options: 0

1-5

6

7

8

9

10

11

12

13

"Pwr Removed"

"DPI Port 1-5"

"Reserved"

"Digital In"

"Fault"

"Not Enabled"

"Sleep"

"Jog"

"Autotune"

Vector

"Precharge"

Vector

1-43

Related

090

093

096

101

361

362

363

364

365

366

20B-UM001.book Page 44 Thursday, June 20, 2013 1:55 PM

1-44

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

216 [Dig In Status]

Status of the digital inputs.

Values

Read Only

Digital In6
Digital In5
Digital In4Digital In3
Digital In2
Digital In1

0 0 0 0

1=Input Present

0=Input Not Present x =Reserved

Read Only

O
Digital Out3 *
Digital Out2
Digital Out1

0

1=Output Energized

0=Output De-energized x =Reserved

Read Only

0.0/100.0%

0.1%

Read Only

0.0/100.0%

0.1%

Read Only

0.0/100.0%

0.1%

Read Only

0.0/+[Maximum Freq]

0.1 Hz

Read Only

0.0/+[Maximum Freq]

0.0/+[Maximum Speed]

0.1 Hz

0.1 RPM

Read Only

0.0/[Rated Amps] × 2

0.1 Amps

<!-- image -->

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Related

361

thru

366

380

thru

384

150

047

048

225

thru

230

079

225

thru

230

224

thru

230

20B-UM001.book Page 45 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

226 [Fault Bus Volts]

Captures and displays the DC bus voltage of the drive at the time of the last

fault.

Captures and displays [Drive Status 1] bit pattern at

1
mma
Active
Ready

rm
Decelerating
Accelerating
Actual Dir
Command Dir
Active
Rea

1 0 1 0

Read Only

0.0/Max Bus Volts

0.1 VDC

Read Only

1=Condition True

0=Condition False x =Reserved

Read Only

1
nning
Active
Ready

0 0 0 0

1=Condition True

0=Condition False x =Reserved

Read Only

1=Condition True

0=Condition False x =Reserved

<!-- image -->

Programming and Parameters

Values

Default:

Min/Max:

Units:

0 0 0 0

1-45

Related

224

thru

230

209

224

thru

230

210

224

thru

230

211

224

thru

230

20B-UM001.book Page 46 Thursday, June 20, 2013 1:55 PM

1-46

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

Values

230 [Alarm 2 @ Fault]

Captures and displays [Drive Alarm 2] at the time of the last fault.

1C
Brk Slipped *
PTC Conflict *
TB Ref Cflct
Sleep Config
Ixo Vlt Rang
SpdRef Cflct
FlxAmps Rang
IR Vlts Rang
VHz NegSlope
MaxFrq Cflct
NP Hz CflctMtrTyp Cflct
Bipolr CflctDigIn CflctC
DigIn CflctB
DigIn CflctA

0 0 0 0

Read Only

1=Condition True

0=Condition False x =Reserved

1C
TrqPrv Cflct *

0

1=Condition True

0=Condition False x =Reserved

499

0/65535

1

Read Only

0/4294967295

–/+2147483648

1

1E
Out PhaseLoss *
ShearPNo Acc *
Load Loss *
In PhaseLoss *
Motor Therm *
Decel Inhibt
AutRst Tries
Shear Pin
Motor OverLd
UnderVoltage
Power Loss

1

1 0 x 1

1

* Vector firmware 3.001 &amp; later

0

0

1

2

1=Enabled

0=Disabled x =Reserved

"Ready"

"Ready"

"Clear Faults"

"Clr Flt Que"

<!-- image -->

Min/Max:

Min/Max:

Options:

Vector

Related

212

224

thru

230

20B-UM001.book Page 47 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

241 [Fault Clear Mode]

Enables/disables a fault reset (clear faults) attempt from any source. This

242 [Power Up Marker]

Programming and Parameters

Values

Default:

Options:

Default:

Min/Max:

Min/Max:

Min/Max:

<!-- image -->

1

0

"Enabled"

"Disabled"

1

"Enabled"

Read Only

0.0000/429496.7295 Hr

0.0/429496.7 Hr

Vector

0.0000/214748.3647 Hr

0.0001 Hr

0.1 Hr

Vector

Read Only

0/65535

0

Read Only

0.0000/429496.7295 Hr

0.0000/214748.3647 Hr

0.0001 Hr v3

v3

1-47

Related

244

246

248

250

252

254

256

258

242

20B-UM001.book Page 48 Thursday, June 20, 2013 1:55 PM

1-48

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

259 [Alarm Config 1]

Enables/disables alarm conditions that will initiate an active drive alarm.

Ground Warn *
Load Loss *In Phase Loss *
Motor Therm *Waking
Dece

1E
 Loss 
tor Therm 
Waking
Decel Inhibt
Drv OL Lvl 2Drv OL Lvl 1IntDBRes OHAnlg In Loss
Str At PwrUp
Power Loss
UnderVoltagePrechrg Actv

1 1 1 1

1

1

* Vector firmware 3.001 &amp; later

0

0

1=Enabled

0=Disabled x =Reserved

"Ready"

"Ready"

1

"Clr Alrm Que"

Read Only

0/65535

1

0.0

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

0.0

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

<!-- image -->

Values

Options:

Min/Max:

Min/Max:

Min/Max:

(1)

(1)

Related

262

263

264

265

266

267

268

269

261

20B-UM001.book Page 49 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

478

484

490

496

See page 1-2 for symbol descriptions

Vector

Vector

Vector v3

Vector v3

Value].

(1)

Blocks 3 &amp; 4 only.

<!-- image -->

[Scale1 In Lo]

[Scale2 In Lo]

[Scale3 In Lo]

[Scale4 In Lo]

Programming and Parameters

Values

Default:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

0.0

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

0.0

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

0.0

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

Read Only

–/+32000.0

–/+32767.0 (v2.xxx)

–/+32767.000

v3

0.1

0.001

v3

(1)

(1)

(1)

(1)

1-49

Related

20B-UM001.book Page 50 Thursday, June 20, 2013 1:55 PM

1-50

File

Programming and Parameters

Communication File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

270

Standard

[DPI Data Rate]

Sets the baud rate for attached drive peripherals. When changing this value

the drive must be reset for the change to take affect.

<!-- image -->

Values

Default:

Options:

0

0

"125 kbps"

"125 kbps"

1

"500 kbps"

Default: 1 "500 kbps"

Read Only

1
ar 
Jog
Start
Stop

1 0 1 0

1=Condition True

0=Condition False x =Reserved

Read Only

–/+32767

1

Read Only

–/+32767

1

Min/Max:

Min/Max:

Related

20B-UM001.book Page 51 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

274

275

See page 1-2 for symbol descriptions

Vector

[DPI Port Sel]

Selects which DPI port reference value will appear in [DPI Port Value].

Value of the DPI reference selected in

[DPI Port Sel].

Programming and Parameters

Values

Default:

"DPI Port 1"

Options: 1-5

"DPI Port 1-5"

Read Only

Min/Max:

Units:

<!-- image -->

–/+32767

1

0

0

1

17

0

1

1(1)

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20-23

"Max Freq"

"Max Freq"

"Max Speed"

"Speed Fdbk"

"Output Freq"

"Command Freq"

"Command Spd"

"Output Amps"

"Torque Amps"

"Flux Amps"

"Output Power"

"Output Volts"

"DC Bus Volts"

"PI Reference"(2)

"PI Feedback"

"PI Error"

"PI Output"

"%Motor OL"

"%Drive OL"

"CommandedTrq"

"MtrTrqCurRef"(2)

"Speed Ref"

"Speed Fdbk"

"Pulse In Ref"(2)

"Reserved"

"Scale Block1-4(1)(2)

Determines which adapters can control the drive. If the bit for an adapter is set to

DPI Port 5
DPI Port 4
DPI Port 3
DPI Port 2
DPI Port 1
Digital In

1 1 1 1

1

1

1=Control Permitted

0=Control Masked x =Reserved

See [Logic Mask]

.

1-51

Related

288

thru

297

288

thru

297

20B-UM001.book Page 52 Thursday, June 20, 2013 1:55 PM

1-52

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

278 [Jog Mask]

Controls which adapters can issue jog commands.

279 [Direction Mask]

Controls which adapters can issue forward/reverse direction commands.

<!-- image -->

Values

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

See [Logic Mask]

.

.

.

.

.

.

.

.

Read Only

DPI Port 5
DPI Port 4
DPI Port 3
DPI Port 2
DPI Port 1
Digital In

1=Issuing Command

0=No Command x =Reserved

See [Stop Owner]

See [Stop Owner]

.

.

Related

288

thru

297

288

thru

297

288

thru

297

288

thru

297

288

thru

297

288

thru

297

288

thru

297

288

thru

297

276

thru

285

276

thru

285

276

thru

285

20B-UM001.book Page 53 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

291 [Direction Owner]

Adapter that currently has exclusive control of direction changes.

Adapter that has the exclusive control of the command frequency source

<!-- image -->

| 293 [Accel Owner] Adapter that has exclusive control of                                                                                                                                                                           |          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| selecting [Accel Time 1, 2].                                                                                                                                                                                                      |          |
| Masks & Owners Adapter that has exclusive control of selecting [Decel Time 1, 2]. 295 [Fault Clr Owner]                                                                                                                           |          |
| Adapter that is presently clearing a fault. 296 [MOP Owner]                                                                                                                                                                       |          |
| increases or decreases in MOP command frequency. 297 [Local Owner]                                                                                                                                                                |          |
| COMMUNICATIONS Adapter that has requested exclusive control of all drive logic functions. If an adapter is in local lockout, all other functions (except stop) on all other                                                       |          |
| non-functional. Local control can only be obtained when the drive is not running. 300 [Data In A1] - Link A Word 1                                                                                                                | Default: |
| Parameter number whose value will be written from a communications device data table.                                                                                                                                             | Units:   |
| Datalinks “Disable” the link. Vector Control – Will not be updated until drive is stopped. Refer to your communications option manual for datalink information. 302 303 [Data In B1] - Link B Word 1 [Data In B2] - Link B Word 2 |          |

Programming and Parameters

Values

Min/Max:

See [Stop Owner]

See [Stop Owner]

See [Stop Owner]

See [Stop Owner]

See [Stop Owner]

See [Stop Owner]

See [Stop Owner]

0 (0 = "Disabled")

0/387

0/544

0/611

1

See [Data In A1] - Link A Word 1 [Data

In A2] - Link A Word 2

.

Vector v3

.

.

.

.

.

.

.

1-53

Related

276

thru

285

276

thru

285

140

276

thru

285

142

276

thru

285

276

thru

285

276

thru

285

276

thru

285

20B-UM001.book Page 54 Thursday, June 20, 2013 1:55 PM

1-54

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

304

[Data In C1] - Link C Word 1

305

306

307

[Data In C2] - Link C Word 2

[Data In D1] - Link D Word 1

[Data In D2] - Link D Word 2

Values

See [Data In A1] - Link A Word 1 [Data

In A2] - Link A Word 2

.

See [Data In A1] - Link A Word 1 [Data

In A2] - Link A Word 2

<!-- image -->

| COMMUNICATIONS Datalinks 310 311         | [Data Out A1] - Link A Word 1 [Data Out A2] - Link A Word 2                         | Default:   |
|---------|-------------------------------------------------------------------------------------|------------|
|         | Parameter number whose value will be written to a communications device data table. | Units:     |
| 313 314 | [Data Out B2] - Link B Word 2 [Data Out C1] - Link C Word 1                         |            |
| 316 317 | Inputs & Outputs File [Data Out D1] - Link D Word 1 [Data Out D2] - Link D Word 2   |            |
| File    | GroupNo.Parameter Name & Description See page 1-2 for symbol descriptions  See page 1-2 for symbol descriptions                                                                                     | Values     |
|         | 320 [Anlg In Config] Selects the mode for the analog inputs.                        |            |

.

0 (0 = "Disabled")

Min/Max:

0/387

0/544

0/611

Vector v3

1

See [Data Out A1] - Link A Word 1

[Data Out A2] - Link A Word 2

.

See [Data Out A1] - Link A Word 1

[Data Out A2] - Link A Word 2

.

See [Data Out A1] - Link A Word 1

[Data Out A2] - Link A Word 2

1C
An2 0=V 1=mA
An1 0=V 1=mA

<!-- image -->

0

0

1=Current

1

0=Voltage x =Reserved

1E
Analog In 2
Analog In 1

0

0

1

1=Enable

0=Disable x =Reserved

.

Related

Related

322

325

323

326

20B-UM001.book Page 55 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

322

See page 1-2 for symbol descriptions

[Analog In 1 Hi]

325

[Analog In 2 Hi]

Sets the highest input value to the analog

[Anlg In Config], parameter 320 defines if this input will be –/+10V or 4-20 mA (0-20

<!-- image -->

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

10.000 Volt

10.000 Volt

4.000/20.000mA

0.000/20.000mA

–/+10.000V

0.000/10.000V

0.001 mA

0.001 Volt

0.000 Volt

0.000 Volt

4.000/20.000mA

0.000/20.000mA

–/+10.000V

0.000/10.000V

0.001 mA

0.001 Volt

0

"Disabled"

0

0

1

2

3

4

5

6

"Disabled"

"Disabled"

"Fault"

"Hold Input"

"Set Input Lo"

"Set Input Hi"

"Goto Preset1"

"Hold OutFreq"

1C
Analog Out2 *
Analog Out1

1

1

1

1=Current

0=Voltage x =Reserved

Selects whether the signed value or absolute value of a parameter is used before

1A
Analog Out2 *
Analog Out1

1

1

1

1=Absolute

0=Signed x =Reserved

v3

v3

1-55

Related

091

092

091

092

091

092

20B-UM001.book Page 56 Thursday, June 20, 2013 1:55 PM

1-56

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

342

[Analog Out1 Sel]

345

Vector

[Analog Out2 Sel]

Selects the source of the value that drives the analog output.

[Analog Out1 Lo] Value

Param. 341 = Signed Param. 341 = Absolute [Analog Out1 Hi] Value

+[Maximum Speed]

+[Maximum Speed]

+[Maximum Speed]

200% Rated

200% Rated

200% Rated

200% Rated

120% Rated Input Volts

200% Rated Input Volts

100%

100%

100%

100%

100%

100%

800% Rated

200% Rated

+[Maximum Speed]

+[Maximum Speed]

+[Maximum Speed]

+800%

20.000 mA, 10.000 Volts

4.000/20.000mA

0.000/20.000mA

–/+10.000V

0.001 mA

0.001 Volt

0.000 mA, 0.000 Volts

4.000/20.000mA

0.000/20.000mA

–/+10.000V

0.001 mA

0.001 Volt v3

v3

<!-- image -->

Options

Values

Default:

Options:

0 Hz/RPM

0 Hz/RPM

0 Hz/RPM

0 Hz/RPM

Min/Max:

Min/Max:

0"Output Freq"

See Table

Related

001

002

003

004

005

007

006

012

135

136

137

138

220

219

377

378

340

342

340

342

20B-UM001.book Page 57 Thursday, June 20, 2013 1:55 PM

File

INPUTS &amp; OUTPUTS
Analog Outputs

Group No.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

354

355

See page 1-2 for symbol descriptions

Vector v3

Vector v3

[Anlg Out1 Scale]

[Anlg Out2 Scale]

Sets the high value for the range of

Example: If [Analog Out Sel] =

"Commanded Trq," a value of 150 =

<!-- image -->

Fast Stop When open, the drive will stop with a 0.1 second decel time. (If Torque Proving is being used, float will be ignored at end of ramp and the mechanical brake will be set).

Excl Link Links digital input to a digital output if the output is set to "Input 1-6 Link." This does not

Input 1-6 Link When Digital Output 1 is set to one of these (i.e. Input 3 Link) in conjunction with

Digital Input 3 set to "Excl Link," the Digital Input 3 state (on/off) is echoed in the Digital

## Micro Pos Micropostion input. When closed, the command frequency is set to a percentage speed reference as defined in [MicroPos Scale%], parameter 611.

Param Cntl Parameter controlled analog output allows PLC to control analog outputs through data

Param Cntl Parameter controlled digital output allows PLC to control digital outputs through data

PI Reference Reference for PI block (see Process PI for Standard Control on page C-13).

Precharge En Forces drive into precharge state. Typically controlled by auxiliary contact on the

Pulse In Ref Reference of the pulse input (Z channel of encoder - can be used while A &amp; B

Torque Setpt 1 Selects "Torque Stpt1" for [Torque Ref A Sel] when set, otherwise uses value selected

|                                                                                 | MOP Dec Decrements speed reference as long as input is closed.   |
|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| MOP Inc Increments speed reference as long as input is closed.                  |                                                                  |
| MtrTrqCurRef Torque producing current reference.                                |                                                                  |
| links. Set in [AnlgX Out Setpt], parameters 377-378.                            |                                                                  |
| links. Set in [Dig Out Setpt], parameter 379.                                   |                                                                  |
| disconnect at the DC input to the drive.                                        |                                                                  |
| channels are encoder inputs).                                                   |                                                                  |
| Scale Block 1-4 Output of scale blocks, parameters 354-355.                     |                                                                  |
| Torque Est Calculated percentage of rated motor torque.  in [Torque Ref A Sel]. |                                                                  |

Programming and Parameters

Values

Default:

Min/Max:

Units:

Min/Max:

0.0

[Analog Out1 Sel]

0.01

20.000 mA, 10.000 Volts

0.000/20.000mA

–/+10.000V

0.001 mA

0.001 Volt

Selected Option Definitions – [Analog Outx Sel], [Digital Inx Sel], [Digital Outx Sel]

Option Description Related

380

361

361

380

361

361

361

342

342

380

342

361

342

342

342

361

1-57

Related

20B-UM001.book Page 58 Thursday, June 20, 2013 1:55 PM

1-58

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

361

[Digital In1 Sel]

362

363

364

365

366

Values

Default:

Default:

Default:

Default:

Default:

Default:

Options:

[Digital In2 Sel]

[Digital In3 Sel]

[Digital In4 Sel]

[Digital In5 Sel]

[Digital In6 Sel](11)

Selects the function for the digital inputs.

<!-- image -->

4

5

18

15

16

17

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15-17

18

19

20

21

22

23

24

25

26

27

28

29

30

31-33

34

35

36

37

38

"Stop – CF"

"Start"

"Auto/ Manual"

"Speed Sel 1"

"Speed Sel 2"

"Speed Sel 3"

"Not Used"

"Enable"(8,10)

"Clear Faults"(CF)(4)

"Aux Fault"

"Stop – CF"(10)

"Start"(5, 9)

"Fwd/ Reverse"(5)

"Run"(6, 10)

"Run Forward"(6)

"Run Reverse"(6)

"Jog"(5) "Jog1"(2)

"Jog Forward"(6)

"Jog Reverse"(6)

"Stop Mode B"

"Bus Reg Md B"

"Speed Sel 1-3"(1)

"Auto/ Manual"(7)

"Local"

"Acc2 &amp; Dec2"

"Accel 2"

"Decel 2"

"MOP Inc"(14)

"MOP Dec"(14)

"Excl Link"(14)

"PI Enable"

"PI Hold"

"PI Reset"

"Pwr Loss Lvl"

"Precharge En"(14)

"Spd/Trq Sel1-3"(2,3)

"Jog 2"(2)

"PI Invert"(12)

"Torque Setpt 1"(12,14)

"Micro Pos"(12, 13, 14)

"Fast Stop"(12, 14)

(6) Typical 2-Wire Inputs - Requires that only 2-wire functions are chosen. Including

3-wire selections will cause a type 2 alarm. See Table 2.C for conflicts.

(7) Auto/Manual - Refer to Reference Control in the Installation Instructions for details.

(8) Opening an "Enable" input will cause the motor to coast-to-stop, ignoring any

(9) "Dig In ConflictB" alarm will occur if a "Start" input is programmed without a "Stop" input.

(10) Refer to the Sleep-Wake Mode Attention statement on page 1-36

.

(11) A dedicated hardware enable input is available via a jumper selection. Refer to the

Related

100

156

162

096

141

143

195

194

380

124

20B-UM001.book Page 59 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

379

See page 1-2 for symbol descriptions

Vector v3

[Dig Out Setpt]

Sets the digital output value from a communication device.

Example of [Digital Outx Sel] which should be set to "30, Param Cntl."

O
Net DigOut3
Net DigOut2
Net DigOut1

0

1=Output Energized

0=Output De-energized x =Reserved

1

"Fault"

4

4

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21-26

27

28

29

30

0.0

0.0

0.0/819.2

0.1

"Run"

"Run"

"Fault"(1)

"Alarm"(1)

"Ready"

"Run"

"Forward Run"

"Reverse Run"

"Auto Restart"

"Powerup Run"

"At Speed"(6)

"At Freq"(3)

"At Current"(3)

"At Torque"(3)

"At Temp"(3)

"At Bus Volts"(3)

"At PI Error"(3)

"DC Braking"

"Curr Limit"

"Economize"

"Motor Overld"

"Power Loss"

"Input 1-6 Link"(6)

"PI Enable"(2)

"PI Hold"(2)

"Drive Overload"(2)

"Param Cntl"(4, 6)

<!-- image -->

Programming and Parameters

Values

Options:

Min/Max:

1-59

Related

380

381

385

389

382

386

390

383

002

001

003

004

218

012

137

157

147

053

048

184

379

380

20B-UM001.book Page 60 Thursday, June 20, 2013 1:55 PM

1-60

Programming and Parameters

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

See page 1-2 for symbol descriptions

382

[Dig Out1 OnTime]

386

390

[Dig Out2 OnTime]

Vector

[Dig Out3 OnTime]

Sets the "ON Delay" time for the digital outputs. This is the time between the

occurrence of a condition and activation of the relay.

<!-- image -->

| 383 387 [Dig Out1 OffTime]   | [Dig Out2 OffTime] Vector                                                                                                                                       | Default:   |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| 391                          | [Dig Out3 OffTime] Sets the “OFF Delay” time for the digital outputs. This is the time between the disappearance of a condition and de-activation of the relay. | Units:     |
| Applications File GroupNo.Parameter Name & Description See page 1-2 for symbol descriptions                              | See page 1-2 for symbol descriptions                                                                                                                            | Values     |

600

Vector v3

[TorqProve Cnfg]

Enables/disables torque/brake proving feature. When "Enabled," [Digital Out1 Sel]

becomes the brake control. Note: this value is not changed when parameters are reset to factory defaults (page 1-40).

<!-- image -->

INPUTS &amp; OUTPUTS
Digital Outputs

Values

Default:

Min/Max:

Units:

Min/Max:

x

1

Enable

0

1=Enabled

0=Disabled x =Reserved

Allows control of specific torque proving functions through a communication

Micro Pos
Fast Stop

0

0

1=Enabled

1

0=Disabled x =Reserved

0.00 Secs

0.00 Secs

0.00/600.00 Secs

0.01 Secs

0.00 Secs

0.00 Secs

0.00/600.00 Secs

0.01 Secs

Related

380

380

Related

20B-UM001.book Page 61 Thursday, June 20, 2013 1:55 PM

File

GroupNo.Parameter Name &amp; Description
See page 1-2 for symbol descriptions

602

603

See page 1-2 for symbol descriptions

Vector v3

[Spd Dev Band]

Defines the allowable difference between the commanded frequency and encoder

period of time.

Vector v3

<!-- image -->

| issued when [Spd Dev Band] is outside                                                                                     | Units:          |
|---------------------------------------------------------------------------------------------------------------------------|-----------------|
| [Brk Release Time] Sets the amount of time between Vector v3                                                              | Default:        |
| commanding the brake to release and the start of frequency acceleration.                                                  | Units:          |
| [ZeroSpdFloatTime] is set. Vector v3                                                                                      | Default: Units: |
| Sets the amount of time the drive is below [Float Tolerance] before the brake [Float Tolerance]                           |                 |
| Sets the frequency level where the float timer starts. Vector v3                                                          | Default:        |
| [Brk Set Time]                                                                                                            | Units: Default: |
| Vector v3                                                                                                                 | Units: Default: |
| Defines the amount of delay time                                                                                          | Units: Default: |
| between commanding the brake to be set                                                                                    | Units:          |
| and the start of brake proving. [TorqLim SlewRate] Vector v3                                                              | Default: Units: |
| Sets the number of encoder counts to                                                                                      | Default: Units: |
| define a brake slippage condition. Sets the number of motor shaft revolutions allowed during the brake                    | Units:          |
|                                                                                                                           | Units:          |
| [Brk Alarm Travel] Vector v3                                                                                              | Units:          |
| slippage test. Drive torque is reduced to check for brake slippage. When slippage occurs, the drive allows this number of | Units:          |
| motor shaft revolutions before regaining control.                                                                         | Units:          |
| used when micropositioning has been                                                                                       |                 |
| [MicroPos Scale%] Sets the percent of speed reference to be Vector v3                                                     | Default:        |
|                                                                                                                           | Units:          |
| before this setting will take effect.                                                                                     | Units:          |
| selected. Motor must come to a stop                                                                                       | Units:          |
|                                                                                                                           | Units:          |

[SpdBand Integrat]

Programming and Parameters

Values

Default:

Min/Max:

Default:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

Min/Max:

2.0 Hz

60.0 RPM

0.1/15.0 Hz

3.0/450.0 RPM

0.1 Hz

0.1 RPM

60 mSec

1/200 mSec

1 mSec

0.10 Secs

0.00/10.00 Secs

0.01 Secs

5.0 Secs

0.1/500.0 Secs

0.1 Secs

0.2 Hz

6.0 RPM

0.1/5.0 Hz

3.0/150.0 RPM

0.1 Hz

0.1 RPM

0.10 Secs

0.00/10.00 Secs

0.01 Secs

10.0 Secs

0.5/300.0 Secs

0.1 Secs

250

0/65535

1

1.0 Revs

0.0/1000.0 Revs

0.1 Revs

10.0%

0.1/100.0%

0.1%

1-61

Related

603

602

361

thru

366

20B-UM001.book Page 62 Thursday, June 20, 2013 1:55 PM

1-62

Programming and Parameters

Parameter Cross Reference – by Name

Parameter Name Number Group Page

Accel Mask 281 Masks &amp; Owners

Accel Owner 293 Masks &amp; Owners

Accel Time X 140, 141 Ramp Rates

Alarm Config 1 259 Alarms

Alarm X @ Fault 229, 230 Diagnostics

Alarm X Code 262-269 Alarms

## Analog In X Hi 322, 325 Analog Inputs Analog In X Lo 323, 326 Analog Inputs

Analog In X Loss 324, 327 Analog Inputs

Analog In1 Value 16 Metering

Analog In2 Value 17 Metering

Analog OutX Hi 343, 346 Analog Outputs

Analog OutX Lo 344, 347 Analog Outputs

Analog OutX Sel 342, 345 Analog Outputs

Anlg In Config 320 Analog Inputs

Anlg In Sqr Root 321 Analog Inputs

Anlg Out Absolut 341 Analog Outputs

Anlg Out Config 340 Analog Outputs

Anlg OutX Scale 354, 355 Analog Outputs

Anlg OutX Setpt 377, 378 Analog Outputs

Auto Rstrt Delay 175 Restart Modes

Auto Rstrt Tries 174 Restart Modes

Autotune 61 Torq Attributes

Autotune Torque 66 Torq Attributes

Break Frequency 72 Volts per Hertz

Break Voltage 71 Volts per Hertz

Brk Release Time 604 Torq Proving

Brk Set Time 607 Torq Proving

Brk Alarm Travel 610 Torq Proving

BrkSlip Count 609 Torq Proving

Bus Reg Kd 165 Stop/Brake Modes 1-34

Bus Reg Ki 160 Stop/Brake Modes 1-33

Bus Reg Kp 164 Stop/Brake Modes 1-34

Bus Reg Mode X 161, 162 Stop/Brake Modes 1-33

Commanded Freq 2 Metering

Commanded Speed 2 Metering

Commanded Torque 24 Metering

Compensation 56 Torq Attributes

Control Status 440 Torq Attributes

Control SW Ver 29 Drive Data

Current Lmt Gain 149 Load Limits

Current Lmt Sel 147 Load Limits

Current Lmt Val 148 Load Limits

Current Rate Limit 154 Load Limits

Data In XX 300-307 Datalinks

Data Out XX 310-317 Datalinks

DB Resistor Type 163 Stop/Brake Modes 1-34

DB While Stopped 145 Stop/Brake Modes 1-32

DC Brake Level 158 Stop/Brake Modes 1-33

DC Brake Time 159 Stop/Brake Modes 1-33

DC Brk Lvl Sel 157 Stop/Brake Modes 1-32

DC Bus Memory 13 Metering

DC Bus Voltage 12 Metering

Decel Mask 282 Masks &amp; Owners

1-52

1-53

1-31

1-48

1-48

1-45

1-48

1-55

1-55

1-55

Parameter Name Number Group Page

Decel Owner 294 Masks &amp; Owners

Decel Time X 142, 143 Ramp Rates

Dig In Status 216 Diagnostics

Dig Out Setpt 379 Digital Outputs

Dig Out Status 217 Diagnostics

Dig OutX Level 381, 385,

389

Dig OutX OffTime 383, 387,

391

Dig OutX OnTime 382, 386,

| 1-13      |
|-----------|
| 1-13      |
| 1-56      |
| 1-56      |
| 1-56      |
| 1-54      |
| 1-54      |
| 1-55      |
| 1-57 1-57 |
| 1-35 1-35 |
| 1-17      |
| 1-18      |
| 1-20      |
| 1-20      |
| 1-61      |
| 1-61      |
| 1-61      |
| 1-61      |
| 1-12      |
| 1-12      |
| 1-13      |
| 1-16      |
| 1-19      |
| 1-14      |
| 1-31      |
| 1-31      |
| 1-31      |
| 1-32      |
| 1-53      |
| 1-54      |
| 1-13      |
| 1-13      |
| 1-52      |

Digital Outputs

Digital Outputs

Digital Outputs

390

Digital InX Sel 361-366 Digital Inputs

Digital OutX Sel 380, 384,

Digital Outputs

388

Direction Mask 279 Masks &amp; Owners

Direction Mode 190 Direction Config

Direction Owner 291 Masks &amp; Owners

DPI Baud Rate 270 Comm Control

DPI Data Rate 270 Comm Control

DPI Fdbk Select 299 Comm Control

DPI Port Sel 274 Comm Control

DPI Port Value 275 Comm Control

DPI Ref Select 298 Comm Control

Drive Alarm X 211, 212 Diagnostics

Drive Checksum 203 Drive Memory

Drive Logic Rslt 271 Comm Control

Drive OL Count 219 Diagnostics

Drive OL Mode 150 Load Limits

Drive Ramp Rslt 273 Comm Control

Drive Ref Rslt 272 Comm Control

Drive Status X 209, 210 Diagnostics

Drive Temp 218 Diagnostics

Droop RPM @ FLA 152 Load Limits

Elapsed kWh 014 Metering

Elapsed MWh 9 Metering

Elapsed Run Time 10 Metering

Enc Position Fdbk 414 Speed Feedback

Encoder PPR 413 Speed Feedback

Encoder Speed 415 Speed Feedback

Encoder Z Chan 423 Speed Feedback

Fault 1 Code 243 Faults

Fault 1 Time 244 Faults

Fault 2 Code 245 Faults

Fault 2 Time 246 Faults

Fault 3 Code 247 Faults

Fault 3 Time 248 Faults

Fault 4 Code 249 Faults

Fault 4 Time 250 Faults

Fault 5 Code 251 Faults

Fault 5 Time 252 Faults

Fault 6 Code 253 Faults

Fault 6 Time 254 Faults

Fault 7 Code 255 Faults

Fault 7 Time 256 Faults

Fault 8 Code 257 Faults

Fault 8 Time 258 Faults

1-53

1-31

1-44

1-59

1-44

1-59

1-60

1-60

1-58

1-59

1-52

1-38

1-53

1-50

1-50

1-51

1-51

1-51

1-51

1-42

1-41

1-50

1-44

1-31

1-50

1-50

1-41

1-44

1-32

1-13

1-12

1-12

1-20

1-20

1-20

1-21

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

20B-UM001.book Page 63 Thursday, June 20, 2013 1:55 PM

Parameter Name Number Group Page

Fault Amps 225 Diagnostics

Fault Bus Volts 226 Diagnostics

Fault Clear 240 Faults

Fault Clear Mode 241 Faults

Fault Clr Mask 283 Masks &amp; Owners

Fault Clr Owner 295 Masks &amp; Owners

Fault Config 1 238 Faults

Fault Speed 224 Diagnostics

Fdbk Filter Sel 416 Speed Feedback

1-44

1-45

1-46

1-47

1-52

1-53

1-46

1-44

1-20

1-63

Programming and Parameters

Parameter Name Number Group Page

Motor OL Factor 48 Motor Data

Motor OL Hertz 47 Motor Data

Motor Poles 49 Motor Data

Motor Type 40 Motor Data

Mtr NP Pwr Units 46 Motor Data

Mtr Tor Cur Ref 441 Torq Attributes

Neg Torque Limit 437 Torq Attributes

Notch Filter Freq 419 Speed Feedback

Notch Filter K 420 Speed Feedback

Output Current 3 Metering

Output Freq 1 Metering

Output Power 7 Metering

Output Powr Fctr 8 Metering

1-15

1-15

1-15

1-14

1-15

1-19

1-19

1-20

1-21

1-12

1-12

1-12

1-12

Output Voltage 6 Metering

1-12

Overspeed Limit 83 Spd Mode &amp; Limits 1-22

Param Access Lvl 196 Drive Memory

PI BW Filter 139 Process PI

PI Configuration 124 Process PI

PI Control 125 Process PI

PI Deriv Time 459 Process PI

PI Error Meter 137 Process PI

PI Fdback Meter 136 Process PI

PI Feedback Hi 462 Process PI

PI Feedback Lo 463 Process PI

PI Feedback Sel 128 Process PI

PI Integral Time 129 Process PI

PI Lower Limit 131 Process PI

PI Output Meter 138 Process PI

PI Preload 133 Process PI

PI Prop Gain 130 Process PI

PI Ref Meter 135 Process PI

PI Reference Hi 460 Process PI

PI Reference Lo 461 Process PI

PI Reference Sel 126 Process PI

PI Setpoint 127 Process PI

PI Status 134 Process PI

PI Upper Limit 132 Process PI

Pos Torque Limit 436 Torq Attributes

Power Loss Level 186 Power Loss

Power Loss Mode 184 Power Loss

Power Loss Time 185 Power Loss

Power Up Marker 242 Faults

Powerup Delay 167 Restart Modes

Preset Speed X 101-107 Discrete Speeds

Pulse In Scale 422 Speed Feedback

Pulse Input Ref 99 Speed Reference

PWM Frequency 151 Load Limits

Ramped Speed 22 Metering

Rated Amps 28 Drive Data

Rated kW 26 Drive Data

Rated Volts 27 Drive Data

Reference Mask 280 Masks &amp; Owners

Reference Owner 292 Masks &amp; Owners

Regen Power Limit 153 Load Limits

Reset Meters 200 Drive Memory

Reset To Defalts 197 Drive Memory

Rev Speed Limit 454 Speed Regulator

Run Boost 70 Volts per Hertz

S Curve % 146 Ramp Rates

1-39

1-29

1-27

1-27

1-29

1-29

1-28

1-29

1-29

1-28

1-28

1-28

1-29

1-28

1-28

1-28

1-29

1-29

1-27

1-27

1-28

1-28

1-19

1-38

1-37

1-37

1-47

1-34

1-25

1-21

1-25

1-31

1-13

1-14

1-14

1-14

1-52

1-53

1-32

1-40

1-40

1-23

1-19

1-31

| Feedback Select 80 Spd Mode & Limits 1-22   |      |
|---------------------------------------------|------|
| Float Tolerance 606 Torq Proving            | 1-61 |
| Flux Braking 166 Stop/Brake Modes 1-34      |      |
| Flux Current 5 Metering                     | 1-12 |
| Flux Current Ref 63 Torq Attributes         | 1-17 |
| Flux Up Mode 57 Torq Attributes             | 1-16 |
| Flux Up Time 58 Torq Attributes             | 1-16 |
| Flying Start En 169 Restart Modes           | 1-35 |
| Flying StartGain 170 Restart Modes          | 1-35 |
| Gnd Warn Level 177 Power Loss               | 1-37 |
| Inertia Autotune 67 Torq Attributes         | 1-18 |
| IR Voltage Drop 62 Torq Attributes          | 1-17 |
| Ixo Voltage Drop 64 Torq Attributes         | 1-17 |
| Jog Mask 278 Masks & Owners                 | 1-52 |
| Jog Owner 290 Masks & Owners                | 1-52 |
| Jog Speed 100 Discrete Speeds               | 1-25 |
| Jog Speed 1 100 Discrete Speeds             | 1-25 |
| Jog Speed 2 108 Discrete Speeds             | 1-25 |
| Kf Speed Loop 447 Speed Regulator           | 1-30 |
| Ki Speed Loop 445 Speed Regulator           | 1-29 |
| Kp Speed Loop 446 Speed Regulator           | 1-30 |
| Language 201 Drive Memory                   | 1-40 |
| Last Stop Source 215 Diagnostics            | 1-43 |
| Load Frm Usr Set 198 Drive Memory           | 1-40 |
| Load Loss Level 187 Power Loss              | 1-38 |
| Load Loss Time 188 Power Loss               | 1-38 |
| Local Owner 297 Masks & Owners              | 1-53 |
| Logic Mask 276 Masks & Owners               | 1-51 |
| Man Ref Preload 193 HIM Ref Config          | 1-39 |
| Marker Pulse 421 Speed Feedback             | 1-21 |
| Maximum Freq 55 Torq Attributes             | 1-16 |
| Maximum Speed 82 Spd Mode & Limits 1-22     |      |
| Maximum Voltage 54 Torq Attributes          | 1-15 |
| MicroPos Scale% 611 Torq Proving            | 1-61 |
| Minimum Speed 81 Spd Mode & Limits 1-22     |      |
| MOP Frequency 11 Metering                   | 1-13 |
| MOP Mask 284 Masks & Owners                 | 1-52 |
| MOP Owner 296 Masks & Owners                | 1-53 |
| MOP Rate 195 MOP Config                     | 1-39 |
| MOP Reference 11 Metering                   | 1-13 |
| Motor Cntl Sel 53 Torq Attributes           | 1-15 |
| Motor NP FLA 42 Motor Data                  | 1-14 |
| Motor NP Hertz 43 Motor Data                | 1-14 |
| Motor NP Power 45 Motor Data                | 1-15 |
| Motor NP RPM 44 Motor Data                  | 1-14 |
| Motor NP Volts 41 Motor Data                | 1-14 |
| Motor OL Count 220 Diagnostics              | 1-44 |

20B-UM001.book Page 64 Thursday, June 20, 2013 1:55 PM

1-64

Programming and Parameters

Parameter Name Number Group Page

Save HIM Ref 192 HIM Ref Config

Save MOP Ref 194 MOP Config

Save To User Set 199 Drive Memory

ScaleX In Hi 477-495 Scaled Blocks

ScaleX In Lo 478-496 Scaled Blocks

ScaleX In Value 476-494 Scaled Blocks

ScaleX Out Hi 479-497 Scaled Blocks

ScaleX Out Lo 480-498 Scaled Blocks

ScaleX Out Value 481-499 Scaled Blocks

1-39

1-39

1-40

1-48

1-49

1-48

1-49

1-49

1-49

Shear Pin Time 189 Power Loss

1-38

Skip Freq Band 87 Spd Mode &amp; Limits 1-23

Skip Frequency X 84-86 Spd Mode &amp; Limits 1-23

Sleep Level 182 Restart Modes

Sleep Time 183 Restart Modes

Sleep-Wake Mode 178 Restart Modes

Sleep-Wake Ref 179 Restart Modes

Slip Comp Gain 122 Slip Comp

Slip RPM @ FLA 121 Slip Comp

Slip RPM Meter 123 Slip Comp

Speed Desired BW 449 Speed Regulator

SpdBand Integrat 603 Torq Proving

Spd Dev Band 602 Torq Proving

Parameter Name Number Group Page

Total Inertia 450 Speed Regulator

Trim % Setpoint 116 Speed Trim

Trim Hi 119 Speed Trim

Trim In Select 117 Speed Trim

Trim Lo 120 Speed Trim

Trim Out Select 118 Speed Trim

Voltage Class 202 Drive Memory

Wake Level 180 Restart Modes

Wake Time 181 Restart Modes

ZeroSpdFloatTime 605 Torq Proving

| 1-37   |
|--------|
| 1-37   |
| 1-36   |
| 1-37   |
| 1-26   |
| 1-26   |
| 1-26   |
| 1-30   |
| 1-61   |

Speed Feedback 25 Metering

1-61

1-13

Speed Loop Meter 451 Speed Regulator

1-30

Speed Mode 80 Spd Mode &amp; Limits 1-22

Speed Ref Source 213 Diagnostics

Speed Ref X Hi 91, 94 Speed Reference

Speed Ref X Lo 92, 95 Speed Reference

Speed Ref X Sel 90, 93 Speed Reference

1-43

1-24

1-24

1-24

Speed Reference 23 Metering

1-13

Speed Units 79 Spd Mode &amp; Limits 1-21

Speed/Torque Mod 88 Spd Mode &amp; Limits 1-23

Start At PowerUp 168 Restart Modes

Start Inhibits 214 Diagnostics

Start Mask 277 Masks &amp; Owners

Start Owner 289 Masks &amp; Owners

Start/Acc Boost 69 Volts per Hertz

1-34

1-43

1-51

1-52

1-19

Status X @ Fault 227, 228 Diagnostics

1-45

Stop Mode X 155, 156 Stop/Brake Modes 1-32

Stop Owner 288 Masks &amp; Owners

1-52

Stop/BRK Mode X 155, 156 Stop/Brake Modes 1-32

SV Boost Filter 59 Torq Attributes

TB Man Ref Hi 97 Speed Reference

TB Man Ref Lo 98 Speed Reference

TB Man Ref Sel 96 Speed Reference

Testpoint X Data 235, 237 Diagnostics

Testpoint X Sel 234, 236 Diagnostics

TorqLim SlewRate 608 Torq Proving

TorqProve Cnfg 600 Torq Proving

TorqProve Setup 601 Torq Proving

Torq Ref A Div 430 Torq Attributes

Torque Current 4 Metering

Torque Perf Mode 53 Torq Attributes

Torque Ref B Mult 434 Torq Attributes

Torque Ref X Hi 428, 432 Torq Attributes

Torque Ref X Lo 429, 433 Torq Attributes

Torque Ref X Sel 427, 431 Torq Attributes

Torque Setpoint 435 Torq Attributes

Torque Setpoint2 438 Torq Attributes

1-16

1-25

1-25

1-25

1-46

1-46

1-61

1-60

1-60

1-18

1-12

1-15

1-18

1-18

1-18

1-18

1-19

1-19

1-30

1-26

1-26

1-26

1-26

1-26

1-41

1-37

1-37

1-61

20B-UM001.book Page 65 Thursday, June 20, 2013 1:55 PM

Programming and Parameters

Parameter Cross Reference – by Number

Number Parameter Name Group Page

1 Output Freq Metering

2 Commanded Freq Metering

Commanded Speed Metering

4 Torque Current Metering

5 Flux Current Metering

## 6 Output Voltage Metering 7 Output Power Metering

8 Output Powr Fctr Metering

9 Elapsed MWh Metering

Number Parameter Name Group Page

80 Feedback Select Spd Mode &amp; Limits 1-22

Speed Mode Spd Mode &amp; Limits

81 Minimum Speed Spd Mode &amp; Limits 1-22

82 Maximum Speed Spd Mode &amp; Limits 1-22

83 Overspeed Limit Spd Mode &amp; Limits 1-22

84-86 Skip Frequency X Spd Mode &amp; Limits 1-23

87 Skip Freq Band Spd Mode &amp; Limits 1-23

88 Speed/Torque Mod Spd Mode &amp; Limits 1-23

90, 93 Speed Ref X Sel Speed Reference

91, 94 Speed Ref X Hi Speed Reference

92, 95 Speed Ref X Lo Speed Reference

96 TB Man Ref Sel Speed Reference

97 TB Man Ref Hi Speed Reference

98 TB Man Ref Lo Speed Reference

99 Pulse Input Ref Speed Reference

100 Jog Speed Discrete Speeds

Jog Speed 1 Discrete Speeds

101-107 Preset Speed X Discrete Speeds

108 Jog Speed 2 Discrete Speeds

116 Trim % Setpoint Speed Trim

117 Trim In Select Speed Trim

118 Trim Out Select Speed Trim

119 Trim Hi Speed Trim

120 Trim Lo Speed Trim

121 Slip RPM @ FLA Slip Comp

122 Slip Comp Gain Slip Comp

123 Slip RPM Meter Slip Comp

124 PI Configuration Process PI

125 PI Control Process PI

126 PI Reference Sel Process PI

127 PI Setpoint Process PI

128 PI Feedback Sel Process PI

129 PI Integral Time Process PI

130 PI Prop Gain Process PI

131 PI Lower Limit Process PI

132 PI Upper Limit Process PI

133 PI Preload Process PI

134 PI Status Process PI

135 PI Ref Meter Process PI

136 PI Fdback Meter Process PI

137 PI Error Meter Process PI

138 PI Output Meter Process PI

139 PI BW Filter Process PI

140, 141 Accel Time X Ramp Rates

1-24

1-24

1-24

1-25

1-25

1-25

1-25

1-25

1-25

1-25

1-26

1-26

1-26

1-26

1-26

1-26

1-26

1-26

1-27

1-27

1-27

1-27

1-28

1-28

1-28

1-28

1-28

1-28

1-28

1-28

1-28

1-29

1-29

1-29

1-31

142, 143 Decel Time X Ramp Rates

1-31

145 DB While Stopped Stop/Brake Modes 1-32

146 S Curve % Ramp Rates

147 Current Lmt Sel Load Limits

148 Current Lmt Val Load Limits

149 Current Lmt Gain Load Limits

150 Drive OL Mode Load Limits

151 PWM Frequency Load Limits

152 Droop RPM @ FLA Load Limits

153 Regen Power Limit Load Limits

154 Current Rate Limit Load Limits

1-31

1-31

1-31

1-31

1-31

1-31

1-32

1-32

1-32

1-12

1-12

1-12

1-12

1-12

1-12

1-12

1-12

|                                    | 10 Elapsed Run Time Metering          | 1-12   |
|------------------------------------|---------------------------------------|--------|
|                                    | 11 MOP Frequency Metering             | 1-13   |
|                                    | MOP Reference Metering                |        |
|                                    | 12 DC Bus Voltage Metering            | 1-13   |
|                                    | 014 Elapsed kWh Metering              | 1-13   |
|                                    | 13 DC Bus Memory Metering             | 1-13   |
|                                    | 16 Analog In1 Value Metering          | 1-13   |
|                                    | 17 Analog In2 Value Metering          | 1-13   |
|                                    | 22 Ramped Speed Metering              | 1-13   |
|                                    | 23 Speed Reference Metering           | 1-13   |
|                                    | 24 Commanded Torque Metering          | 1-13   |
|                                    | 25 Speed Feedback Metering            | 1-13   |
|                                    | 26 Rated kW Drive Data                | 1-14   |
|                                    | 27 Rated Volts Drive Data             | 1-14   |
|                                    | 28 Rated Amps Drive Data              | 1-14   |
|                                    | 29 Control SW Ver Drive Data          | 1-14   |
|                                    | 40 Motor Type Motor Data              | 1-14   |
|                                    | 41 Motor NP Volts Motor Data          | 1-14   |
|                                    | 42 Motor NP FLA Motor Data            | 1-14   |
|                                    | 43 Motor NP Hertz Motor Data          | 1-14   |
|                                    | 44 Motor NP RPM Motor Data            | 1-14   |
|                                    | 45 Motor NP Power Motor Data          | 1-15   |
|                                    | 46 Mtr NP Pwr Units Motor Data        | 1-15   |
| 47 Motor OL Hertz Motor Data       |                                       | 1-15   |
| 48 Motor OL Factor Motor Data      |                                       | 1-15   |
|                                    | 49 Motor Poles Motor Data             | 1-15   |
|                                    | 53 Motor Cntl Sel Torq Attributes     | 1-15   |
|                                    | Torque Perf Mode Torq Attributes      |        |
|                                    | 54 Maximum Voltage Torq Attributes    | 1-15   |
|                                    | 55 Maximum Freq Torq Attributes       | 1-16   |
|                                    | 56 Compensation Torq Attributes       | 1-16   |
|                                    | 57 Flux Up Mode Torq Attributes       | 1-16   |
|                                    | 58 Flux Up Time Torq Attributes       | 1-16   |
|                                    | 59 SV Boost Filter Torq Attributes    | 1-16   |
|                                    | 61 Autotune Torq Attributes           | 1-17   |
|                                    | 62 IR Voltage Drop Torq Attributes    | 1-17   |
|                                    | 63 Flux Current Ref Torq Attributes   | 1-17   |
|                                    | 64 Ixo Voltage Drop Torq Attributes   | 1-17   |
| 66 Autotune Torque Torq Attributes |                                       | 1-18   |
|                                    | 67 Inertia Autotune Torq Attributes   | 1-18   |
|                                    | 69 Start/Acc Boost Volts per Hertz    | 1-19   |
|                                    | 70 Run Boost Volts per Hertz          | 1-19   |
|                                    | 71 Break Voltage Volts per Hertz      | 1-20   |
|                                    | 72 Break Frequency Volts per Hertz    | 1-20   |
|                                    | 79 Speed Units Spd Mode & Limits 1-21 |        |

1-65

20B-UM001.book Page 66 Thursday, June 20, 2013 1:55 PM

1-66

Programming and Parameters

Number Parameter Name Group Page

155, 156 Stop Mode X Stop/Brake Modes 1-32

Stop/BRK Mode X Stop/Brake Modes

157 DC Brk Lvl Sel Stop/Brake Modes 1-32

158 DC Brake Level Stop/Brake Modes 1-33

159 DC Brake Time Stop/Brake Modes 1-33

160 Bus Reg Ki Stop/Brake Modes 1-33

161, 162 Bus Reg Mode X Stop/Brake Modes 1-33

163 DB Resistor Type Stop/Brake Modes 1-34

164 Bus Reg Kp Stop/Brake Modes 1-34

165 Bus Reg Kd Stop/Brake Modes 1-34

Number Parameter Name Group Page

234, 236 Testpoint X Sel Diagnostics

235, 237 Testpoint X Data Diagnostics

238 Fault Config 1 Faults

240 Fault Clear Faults

241 Fault Clear Mode Faults

242 Power Up Marker Faults

243 Fault 1 Code Faults

244 Fault 1 Time Faults

245 Fault 2 Code Faults

246 Fault 2 Time Faults

247 Fault 3 Code Faults

248 Fault 3 Time Faults

249 Fault 4 Code Faults

250 Fault 4 Time Faults

251 Fault 5 Code Faults

252 Fault 5 Time Faults

253 Fault 6 Code Faults

254 Fault 6 Time Faults

255 Fault 7 Code Faults

256 Fault 7 Time Faults

257 Fault 8 Code Faults

258 Fault 8 Time Faults

259 Alarm Config 1 Alarms

261 Alarm Clear Alarms

262-269 Alarm X Code Alarms

270 DPI Baud Rate Comm Control

DPI Data Rate Comm Control

271 Drive Logic Rslt Comm Control

272 Drive Ref Rslt Comm Control

273 Drive Ramp Rslt Comm Control

274 DPI Port Sel Comm Control

275 DPI Port Value Comm Control

276 Logic Mask Masks &amp; Owners

277 Start Mask Masks &amp; Owners

278 Jog Mask Masks &amp; Owners

279 Direction Mask Masks &amp; Owners

280 Reference Mask Masks &amp; Owners

281 Accel Mask Masks &amp; Owners

282 Decel Mask Masks &amp; Owners

283 Fault Clr Mask Masks &amp; Owners

284 MOP Mask Masks &amp; Owners

285 Local Mask Masks &amp; Owners

288 Stop Owner Masks &amp; Owners

289 Start Owner Masks &amp; Owners

290 Jog Owner Masks &amp; Owners

291 Direction Owner Masks &amp; Owners

292 Reference Owner Masks &amp; Owners

293 Accel Owner Masks &amp; Owners

294 Decel Owner Masks &amp; Owners

295 Fault Clr Owner Masks &amp; Owners

296 MOP Owner Masks &amp; Owners

297 Local Owner Masks &amp; Owners

298 DPI Ref Select Comm Control

299 DPI Fdbk Select Comm Control

300-307 Data In XX Datalinks

310-317 Data Out XX Datalinks

320 Anlg In Config Analog Inputs

321 Anlg In Sqr Root Analog Inputs

322, 325 Analog In X Hi Analog Inputs

|                                | 166 Flux Braking Stop/Brake Modes 1-34   |      |
|--------------------------------|------------------------------------------|------|
|                                | 167 Powerup Delay Restart Modes          | 1-34 |
|                                | 168 Start At PowerUp Restart Modes       | 1-34 |
|                                | 169 Flying Start En Restart Modes        | 1-35 |
|                                | 170 Flying StartGain Restart Modes       | 1-35 |
|                                | 174 Auto Rstrt Tries Restart Modes       | 1-35 |
|                                | 175 Auto Rstrt Delay Restart Modes       | 1-35 |
|                                | 177 Gnd Warn Level Power Loss            | 1-37 |
|                                | 178 Sleep-Wake Mode Restart Modes        | 1-36 |
|                                | 179 Sleep-Wake Ref Restart Modes         | 1-37 |
|                                | 180 Wake Level Restart Modes             | 1-37 |
|                                | 181 Wake Time Restart Modes              | 1-37 |
|                                | 182 Sleep Level Restart Modes            | 1-37 |
|                                | 183 Sleep Time Restart Modes             | 1-37 |
|                                | 184 Power Loss Mode Power Loss           | 1-37 |
|                                | 185 Power Loss Time Power Loss           | 1-37 |
|                                | 186 Power Loss Level Power Loss          | 1-38 |
|                                | 187 Load Loss Level Power Loss           | 1-38 |
|                                | 188 Load Loss Time Power Loss            | 1-38 |
|                                | 189 Shear Pin Time Power Loss            | 1-38 |
|                                | 190 Direction Mode Direction Config      | 1-38 |
|                                | 192 Save HIM Ref HIM Ref Config          | 1-39 |
|                                | 193 Man Ref Preload HIM Ref Config       | 1-39 |
|                                | 194 Save MOP Ref MOP Config              | 1-39 |
|                                | 195 MOP Rate MOP Config                  | 1-39 |
|                                | 196 Param Access Lvl Drive Memory        | 1-39 |
|                                | 197 Reset To Defalts Drive Memory        | 1-40 |
|                                | 198 Load Frm Usr Set Drive Memory        | 1-40 |
|                                | 200 Reset Meters Drive Memory            | 1-40 |
|                                | 201 Language Drive Memory                | 1-40 |
|                                | 203 Drive Checksum Drive Memory          | 1-41 |
|                                |                                          | 1-41 |
|                                | 209, 210 Drive Status X Diagnostics      |      |
|                                | 213 Speed Ref Source Diagnostics         | 1-43 |
|                                | 214 Start Inhibits Diagnostics           | 1-43 |
|                                |                                          | 1-43 |
|                                | 215 Last Stop Source Diagnostics         |      |
|                                | 217 Dig Out Status Diagnostics           | 1-44 |
|                                | 218 Drive Temp Diagnostics               | 1-44 |
|                                |                                          | 1-44 |
| 220 Motor OL Count Diagnostics | 219 Drive OL Count Diagnostics           | 1-44 |
|                                | 224 Fault Frequency Diagnostics          | 1-44 |
|                                | Fault Speed Diagnostics                  |      |
|                                | 225 Fault Amps Diagnostics               | 1-44 |
|                                | 226 Fault Bus Volts Diagnostics          | 1-45 |
|                                | 227, 228 Status X @ Fault Diagnostics    | 1-45 |
|                                | 229, 230 Alarm X @ Fault Diagnostics     | 1-45 |

1-46

1-46

1-46

1-46

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-47

1-48

1-48

1-48

1-50

1-50

1-50

1-50

1-51

1-51

1-51

1-51

1-52

1-52

1-52

1-52

1-52

1-52

1-52

1-52

1-52

1-52

1-52

1-53

1-53

1-53

1-53

1-53

1-53

1-53

1-51

1-51

1-53

1-54

1-54

1-54

1-55

20B-UM001.book Page 67 Thursday, June 20, 2013 1:55 PM

Number Parameter Name Group Page

323, 326 Analog In X Lo Analog Inputs

324, 327 Analog In X Loss Analog Inputs

340 Anlg Out Config Analog Outputs

341 Anlg Out Absolut Analog Outputs

342, 345 Analog OutX Sel Analog Outputs

343, 346 Analog OutX Hi Analog Outputs

344, 347 Analog OutX Lo Analog Outputs

361-366 Digital InX Sel Digital Inputs

377, 378 Anlg OutX Setpt Analog Outputs

379 Dig Out Setpt Digital Outputs

Digital OutX Sel Digital Outputs

Dig OutX Level Digital Outputs

Dig OutX OnTime Digital Outputs

Dig OutX OffTime Digital Outputs

412 Motor Fdbk Type Speed Feedback

413 Encoder PPR Speed Feedback

414 Enc Position Fdbk Speed Feedback

415 Encoder Speed Speed Feedback

416 Fdbk Filter Sel Speed Feedback

419 Notch Filter Freq Speed Feedback

420 Notch Filter K Speed Feedback

421 Marker Pulse Speed Feedback

422 Pulse In Scale Speed Feedback

423 Encoder Z Chan Speed Feedback

427, 431 Torque Ref X Sel Torq Attributes

428, 432 Torque Ref X Hi Torq Attributes

429, 433 Torque Ref X Lo Torq Attributes

430 Torq Ref A Div Torq Attributes

434 Torque Ref B Mult Torq Attributes

435 Torque Setpoint Torq Attributes

436 Pos Torque Limit Torq Attributes

437 Neg Torque Limit Torq Attributes

438 Torque Setpoint2 Torq Attributes

440 Control Status Torq Attributes

441 Mtr Tor Cur Ref Torq Attributes

445 Ki Speed Loop Speed Regulator

446 Kp Speed Loop Speed Regulator

447 Kf Speed Loop Speed Regulator

449 Speed Desired BW Speed Regulator

450 Total Inertia Speed Regulator

451 Speed Loop Meter Speed Regulator

454 Rev Speed Limit Speed Regulator

459 PI Deriv Time Process PI

460 PI Reference Hi Process PI

461 PI Reference Lo Process PI

462 PI Feedback Hi Process PI

463 PI Feedback Lo Process PI

476-494 ScaleX In Value Scaled Blocks

477-495 ScaleX In Hi Scaled Blocks

478-496 ScaleX In Lo Scaled Blocks

479-497 ScaleX Out Hi Scaled Blocks

480-498 ScaleX Out Lo Scaled Blocks

481-499 ScaleX Out Value Scaled Blocks

600 TorqProve Cnfg Torq Proving

601 TorqProve Setup Torq Proving

<!-- image -->

| 380,          |
|---------------|
| 384, 388      |
| 381,          |
| 385, 389      |
| 382, 386, 390 |
| 383,          |
| 387, 391      |

1-55

1-55

1-55

1-55

1-56

1-56

1-56

1-58

1-57

1-59

1-59

1-59

1-60

1-60

1-20

1-20

1-20

1-20

1-20

1-20

1-21

1-21

1-21

1-21

1-18

1-18

1-18

1-18

1-18

1-19

1-19

1-19

1-19

1-19

1-19

1-29

1-30

1-30

1-30

1-30

1-30

1-23

1-29

1-29

1-29

1-29

1-29

1-48

1-48

1-49

1-49

1-49

1-49

1-60

1-60

Programming and Parameters

1-67

Number Parameter Name Group Page

602 Spd Dev Band Torq Proving

603 SpdBand Integrat Torq Proving

604 Brk Release Time Torq Proving

605 ZeroSpdFloatTime Torq Proving

606 Float Tolerance Torq Proving

607 Brk Set Time Torq Proving

608 TorqLim SlewRate Torq Proving

609 BrkSlip Count Torq Proving

610 Brk Alarm Travel Torq Proving

611 MicroPos Scale% Torq Proving

1-61

1-61

1-61

1-61

1-61

1-61

1-61

1-61

1-61

1-61

20B-UM001.book Page 68 Thursday, June 20, 2013 1:55 PM

1-68

Programming and Parameters

Notes:

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

Troubleshooting

Chapter 4 provides information to guide you in troubleshooting the possible solutions, when applicable) and alarms.

For information on… See page…

Faults and Alarms

Drive Status

Manually Clearing Faults

Fault Descriptions

2-1

2-2

2-4

2-4

Clearing Alarms 2-9 Alarm Descriptions 2-10 Common Symptoms and Corrective Actions 2-13

Testpoint Codes and Functions

Faults and Alarms

A fault is a condition that stops the drive. There are three fault types.

Auto-Reset Run When this type of fault occurs, and [Auto Rstrt Tries] (see page 1-35) is set to a value greater than "0," a

user-configurable timer, [Auto Rstrt Delay] (see page 1-35)

begins. When the timer reaches zero, the drive attempts to automatically reset the fault. If the condition that caused the

fault is no longer present, the fault will be reset and the drive will be restarted.

➁ Non-Resettable This type of fault normally requires drive or motor repair. The cause of the fault must be corrected before the fault can be

cleared. The fault will be reset on power up after repair.

User Configurable These faults can be enabled/disabled to annunciate or ignore

An alarm is a condition that, if left untreated, may stop the drive. There

User Configurable These alarms can be enabled or disabled through

.

| are two alarm types. ➂  a fault condition.              |
|---------------------------------------------------------|
| Type Alarm Description ➀  [Alarm Config 1] on page 1-48 |
| ➁  Non-Configurable These alarms are always enabled.    |

|    | Type Fault Description   |
|----|--------------------------|
| ➀  |                          |

2-16

Chapter 2

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

2-2

Troubleshooting

Drive Status

The condition or state of your drive is constantly monitored. Any changes will be indicated through the LEDs and/or the HIM (if present).

Front Panel LED Indications

Figure 2.1 Typical Drive Status Indicators

POWER

STS

➊

S.M

.

A

.

R

Esc

Exit

Sel

➋ 7 8 9 4 5 6 1 2 3 . 0 +/-Jog Alt Exp Param # Frames 0 &amp; 1

PORT

MOD

NET A

NET B

<!-- image -->

Drive Running

CAUTION

HOT surfaces can cause severe burns

Frames

2 &amp; 3

Green Steady Illuminates when power is applied to the drive.

Green Flashing Drive ready, but not running &amp; no faults are present.

Steady Drive running, no faults are present.

A start inhibit condition exists, the drive cannot be started. Check parameter 214 [Start Inhibits].

An intermittent type 1 alarm condition is occurring.

Check parameter 211 [Drive Alarm 1].

A continuous type 1 alarm condition exists.

Check parameter 211 [Drive Alarm 1].

Flashing Fault has occurred. Check [Fault x Code] or Fault Queue.

Steady A non-resettable fault has occurred.

PORT Green – Status of DPI port internal communications (if present).

MOD Yellow – Status of communications module (when installed).

NET B Red – Status of secondary network (if connected).

<!-- image -->

|    | Drive Running Red                             |
|----|-----------------------------------------------|
|    | See                                           |
|    | page 2-4                                      |
| ➌  |                                               |
|    | NET A Red – Status of network (if connected). |

.

T

.

Lang

Auto / Man

Remove

➌

POWER

STS

S.M.A.R.T

Esc

Alt

.

Exit

Sel

7

4

1

.

Exp

PORT

MOD

NET A

NET B

Lang

8

5

2

0

Auto / Man

9

6

3

+/-

Param #

Remove

Jog

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

Precharge Board LED Indications

Precharge Board LED indicators are found on Frame 5 &amp; 6 drives.

Name Color State Description

Power Green Steady Indicates when precharge board power supply is operational

Alarm Yellow Flashing

[1]

[2]

[3]

[4]

[5]

Number in "[ ]" indicates flashes and associated alarm(1):

Low phase (one phase &lt;80% of line voltage).

Frequency out of range or asymmetry (line sync failed).

Low DC bus voltage (triggers ride-through operation).

[6] Input frequency momentarily out of range (40-65 Hz).

[7]

DC bus short circuit detection active.

Number in "[ ]" indicates flashes and associated fault(2):

An alarm condition automatically resets when the condition no longer exists

A fault indicates a malfunction that must be corrected and can only be reset after cycling power.

The LCD HIM also provides visual notification of a fault or alarm

Display

F-&gt; Faulted Auto

0.0

Hz

— Fault — F 5

Main Menu:
OverVolta

ain Menu:
OverVoltage

iagnostics
Time Since Fault

Diagnostics
Time Since

meter
0000:23:52

Parameter
0000:

F-&gt; Power Loss Auto

0.0

Hz

Main Menu:

Diagnostics

Parameter

Device Select

<!-- image -->

| Fault Red Flashing [2] DC bus short (Udc <2% after 20 ms).                |
|---------------------------------------------------------------------------|
| HIM Indication [4] Line sync failed or low line (Uac <50% Unom). (1)  (2) |
| condition. Condition                                                      |

- Drive is indicating a fault.

The LCD HIM immediately reports the fault condition

by displaying the following.

·

"Faulted" appears in the status line

·

Fault number

· Fault name · Time that has passed since fault occurred

Press Esc to regain HIM control.

<!-- image -->

| Drive is indicating an alarm. The LCD HIM immediately reports the alarm condition by displaying the following. •  Alarm name (Type 2 alarms only) •  Alarm bell graphic   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Troubleshooting

2-3

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

2-4

Troubleshooting

Manually Clearing Faults

Step

1. Press Esc to acknowledge the fault. The fault information will be removed so that you can use the HIM.

2. Address the condition that caused the fault.

The cause must be corrected before the fault can be cleared.

3. After corrective action has been taken, clear the fault by one of these methods.

·

Press Stop

- Cycle drive power · Set parameter 240 [Fault Clear] to "1."

·

<!-- image -->

"Clear Faults" on the HIM Diagnostic menu.

- Table 2.A Fault Types, Descriptions and Actions Fault Descriptions

(1)

No.Type

- Fault
- Analog In Loss 29

➀

➂

<!-- image -->

Description Action

An analog input is configured to fault on signal loss. A signal loss

has occurred.

Configure with [Anlg In 1, 2 Loss]

on page 1-55

.

Anlg Cal Chksum 108 The checksum read from the analog calibration data does not

| Auto Rstrt Tries 33                                   | ➂ Drive unsuccessfully attempted to reset a fault and resume running                                 |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| AutoTune Aborted 80 Autotune function was canceled    | for the programmed number of [Flt RstRun Tries]. Enable/Disable with [Fault Config 1] on page 1-46 . |
| Auxiliary Input 2                                     | by the user or a fault occurred.                                                                     |
| DB Resistance 69 Resistance of the internal DB Vector | Cntl Bd Overtemp 55 The temperature sensor on the Main Control Board detected excessive heat.        |

1. Check parameters.

2. Check for broken/loose connections at inputs.

Replace drive.

Correct the cause of the fault and manually clear.

Restart procedure.

➀ Auxiliary input interlock is open. Check remote wiring.

1. Check Main Control Board fan.

2. Check surrounding air temperature.

3. Verify proper mounting/cooling.

Replace resistor.

Key(s)

Esc

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

(1)

No.Type

Fault

Decel Inhibit 24

Description Action

➂ The drive is not following a commanded deceleration

because it is attempting to limit bus voltage.

<!-- image -->

|                                                                                | Drive OverLoad 64 Drive rating of 110% for 1 minute or 150% for 3 seconds has been exceeded. Excessive Load 79 Motor did not come up to speed in the allotted time during autotune. Encoder Loss 91 Requires differential encoder. One of the 2 encoder channel   |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Encoder Quad Err 90 Both encoder channels changed                              | signals is missing.                                                                                                                                                                                                                                               |
|                                                                                | the fault clear function was performed.                                                                                                                                                                                                                           |
| FluxAmpsRef Rang                                                               | the clear queue function was performed. 78 The value for flux amps determined by the Autotune                                                                                                                                                                     |
| Ground Fault 13                                                                | procedure exceeds the programmed [Motor NP FLA]. ➀ A current path to earth ground                                                                                                                                                                                 |
| greater than 25% of drive rating.                                              | greater than 25% of drive rating.                                                                                                                                                                                                                                 |
| Hardware Fault 93 Hardware enable is disabled (jumpered high) but logic pin is | Hardware Fault 93 Hardware enable is disabled (jumpered high) but logic pin is                                                                                                                                                                                    |
|                                                                                | still low.                                                                                                                                                                                                                                                        |
| Heatsink OvrTemp 8                                                             | ➀ Heatsink temperature exceeds 100% of [Drive Temp].                                                                                                                                                                                                              |

1. Verify input voltage is within drive specified limits.

2. Verify system ground impedance follows proper grounding

techniques.

3. Disable bus regulation and/or add dynamic brake resistor and/or

extend deceleration time. Refer to the Attention statement on page

P-4

Reduce load or extend Accel Time.

Drive Powerup 49 No fault displayed. Used as a Power Up Marker in the Fault Queue indicating that the drive power has been cycled.

1. Uncouple load from motor.

2. Repeat Autotune.

1. Check Wiring.

2. Replace encoder.

1. Check for externally induced noise.

2. Replace encoder.

Faults Cleared 52 No fault displayed. Used as a marker in the Fault Queue indicating that

Flt QueueCleared 51 No fault displayed. Used as a marker in the Fault Queue indicating that

1. Reprogram [Motor NP FLA] with the correct motor nameplate

value.

2. Repeat Autotune.

Check the motor and external wiring to the drive output terminals for a

grounded condition.

1. Check jumper.

2. Replace Main Control Board.

Hardware Fault 130 Gate array load error. 1. Cycle power.

2. Replace Main Control Board.

Hardware Fault 131 Dual port failure. 1. Cycle power.

2. Replace Main Control Board.

1. Verify that maximum ambient temperature has not been

exceeded.

2. Check fan.

3. Check for excess load.

Troubleshooting

2-5

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

2-6

Troubleshooting

(1)

Fault

No.Type

HW OverCurrent 12

Description Action

➀ The drive output current has exceeded the hardware current

limit.

Incompat MCB-PB 106 ➁ Drive rating information stored on the power board is incompatible

with the main control board.

<!-- image -->

|                                                  | with the Main Control Board.                                                                                                                      |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                  | I/O Failure 122 I/O was detected, but failed the powerup sequence. I/O Board is separate in Standard & integral in Vector Control.                |
| Standard                                         | I/O Mismatch 120 I/O board configuration not the same from last time drive was                                                                    |
|                                                  | powered up. Input Phase Loss 17 The DC bus ripple has exceeded a preset level.                                                                    |
|                                                  | IR Volts Range 77 “Calculate” is the autotune default and the value determined by the autotune procedure for IR Drop Volts is not in the range of |
| IXo VoltageRange 87 Voltage calculated for motor |                                                                                                                                                   |
| Load Loss 15 Drive output torque current is      |                                                                                                                                                   |
| Motor Overload 7                                 | ➀ ➂ Internal electronic overload trip. Enable/Disable with [Fault Config 1] on page 1-46 .                                                        |
| NVS I/O Checksum                                 |                                                                                                                                                   |

Check programming. Check for excess load, improper DC boost

setting, DC brake volts set too high or other causes of excess current.

Load compatible version files into drive.

Check connector. Check for induced noise. Replace I/O board or Main

Control Board.

Replace I/O Board (Standard

Control) or Main Control Board

(Vector Control).

Verify configuration.

Check incoming power for a missing phase/blown fuse.

Re-enter motor nameplate data.

1. Check for proper motor sizing.

2. Check for correct programming of

[Motor NP Volts], parameter 41.

3. Additional output impedance may be required.

1. Verify connections between motor and load.

2. Verify level and time requirements.

An excessive motor load exists.

Reduce load so drive output current does not exceed the current set by

[Motor NP FLA].

Motor Thermistor 16 Thermistor output is out of range. 1. Verify that thermistor is connected.

2. Motor is overheated. Reduce load.

109 EEprom checksum error. 1. Cycle power and repeat function.

2. Replace Main Control Board.

NVS I/O Failure 110 EEprom I/O error. 1. Cycle power and repeat function.

2. Replace Main Control Board.

20B-UM001.book Page 7 Thursday, June 20, 2013 1:55 PM

(1)

No.Type

Fault

Description Action

Output PhaseLoss 21 Current in one or more phases has been lost or remains below a

preset level.

Compensation or Bus Regulation have attempted to add an output

<!-- image -->

|                                                                 | [Overspeed Limit].                                                                                      |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| OverVoltage 5                                                   | ➀ DC bus voltage exceeded maximum value.                                                                |
| Parameter Chksum Params Defaulted 48 The drive was commanded to | 100 ➁ The checksum read from the board does not match the checksum calculated.                          |
| Phase V to Grnd 39                                              | Phase U to Grnd 38 A phase to ground fault has been detected between the drive and motor in this phase. |
| Phase W to Grnd 40 Phase UV Short 41 Excessive current has been |                                                                                                         |
| Phase VW Short 42 Phase UW Short 43 Port 1-5 DPI Loss 81-       | detected between these two output terminals. ➁ DPI port stopped communicating.                          |
| 85                                                              | A SCANport device was connected to a drive operating                                                    |
| 85                                                              | DPI devices at 500k baud.                                                                               |
| Port 1-5 Adapter 71- 75                                         | The communications card has a fault.                                                                    |
| Port 1-5 Adapter 71- 75                                         |                                                                                                         |
| Port 1-5 Adapter 71- 75                                         |                                                                                                         |

Check the drive and motor wiring.

Check for phase-to-phase continuity at the motor terminals. Check for

disconnected motor leads.

Remove excessive load or overhauling conditions or increase

[Overspeed Limit].

Monitor the AC line for high line voltage or transient conditions. Bus

overvoltage can also be caused by motor regeneration. Extend the decel

time or install dynamic brake option.

1. Restore defaults.

2. Reload User Set if used.

1. Clear the fault or cycle power to the drive.

2. Program the drive parameters as needed.

1. Check the wiring between the drive and motor.

2. Check motor for grounded phase.

3. Replace drive.

1. Check the motor and drive output terminal wiring for a shorted

condition.

2. Replace drive.

1. If adapter was not intentionally disconnected, check wiring to the

port. Replace wiring, port expander, adapters, Main Control

Board or complete drive as required.

2. Check HIM connection.

3. If an adapter was intentionally disconnected and the [Logic

Mask] bit for that adapter is set to

"1", this fault will occur. To disable this fault, set the [Logic Mask] bit

for the adapter to "0."

1. Check DPI device event queue and corresponding fault

information for the device.

OverSpeed Limit 25

Troubleshooting

2-7

20B-UM001.book Page 8 Thursday, June 20, 2013 1:55 PM

2-8

Troubleshooting

(1)

Fault

No.Type

Power Loss 3

➀

➂

Description Action

DC bus voltage remained below

85% of nominal for longer than

[Power Loss Time]. Enable/

Disable with [Fault Config 1] on page 1-46

.

Power Unit 70 One or more of the output

<!-- image -->

|                                                   | by excessive transistor current or                                                                                                 |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Pwr Brd Chksum1 104 The checksum read from the    | insufficient base drive voltage. Pulse In Loss 92 Z Channel is selected as a pulse input and no signal is present.                 |
| Pwr Brd Chksum2 105 ➁ The checksum read from the  | EEPROM does not match the checksum calculated from the EEPROM data.                                                                |
|                                                   | Replaced MCB-PB 107 ➁ Main Control Board was replaced and parameters were not programmed.                                          |
| Shear Pin 63                                      | ➂ Programmed [Current Lmt Val] has been exceeded. Enable/                                                                          |
| SW OverCurrent 36                                 | ➀ Drive output current has exceeded the 1ms current rating. This rating is greater than the 3                                      |
| TorqPrv Spd Band 20 Difference between [Commanded | second current rating and less than the hardware overcurrent fault level. It is typically 200- 250% of the drive continuous rating |
|                                                   | Speed] and [Encoder Speed] has                                                                                                     |
|                                                   | exceeded the level set in [Spd                                                                                                     |
| Trnsistr OvrTemp 9                                | Dev Band] for a time period greater than [Spd Band Integrat]. ➀ Output transistors have exceeded                                   |

Monitor the incoming AC line for low voltage or line power interruption.

1. Check for damaged output transistors.

2. Replace drive.

1. Check wiring.

2. Replace pulse generator.

Clear the fault or cycle power to the drive.

1. Cycle power to the drive.

2. If problem persists, replace drive.

1. Restore defaults.

2. Reprogram parameters.

Check load requirements and

[Current Lmt Val] setting.

Software Fault 88 Microprocessor handshake error. Replace Main Control Board.

Software Fault 89 Microprocessor handshake error. Replace Main Control Board.

Check for excess load, improper DC

boost setting. DC brake volts set too high.

1. Check wiring between drive and motor.

2. Check release of mechanical brake.

1. Verify that maximum ambient temperature has not been

exceeded.

2. Check fan.

3. Check for excess load.

20B-UM001.book Page 9 Thursday, June 20, 2013 1:55 PM

(1)

No.Type

Fault

UnderVoltage 4

➀

➂

Description Action

DC bus voltage fell below the minimum value of 407V DC at

400/480V input or 204V DC at

200/240V input. Enable/Disable

UserSet1 Chksum 101 ➁ The checksum read from the user

UserSet2 Chksum 102 ➁

set does not match the checksum calculated.

Fault No.(1) Fault No.(1)

Monitor the incoming AC line for low voltage or power interruption.

Re-save user set.

Fault

2 Auxiliary Input 39 Phase V to Grnd 87 IXo VoltageRange

3 Power Loss 40 Phase W to Grnd 88 Software Fault

4 UnderVoltage 41 Phase UV Short 89 Software Fault

5 OverVoltage 42 Phase VW Short 90 Encoder Quad Err

<!-- image -->

| UserSet3 Chksum 103 ➁                       |                                                |
|---------------------------------------------|------------------------------------------------|
| Table 2.B Fault Cross Reference (1)  No.(1) | See page 2-1 for a description of fault types. |

7 Motor Overload 43 Phase UW Short 91 Encoder Loss

8 Heatsink OvrTemp 48 Params Defaulted 92 Pulse In Loss

9 Trnsistr OvrTemp 49 Drive Powerup 93 Hardware Fault

12 HW OverCurrent 51 Flt QueueCleared 100 Parameter Chksum

13 Ground Fault 52 Faults Cleared 101-103 UserSet Chksum

15 Load Loss 55 Cntl Bd Overtemp 104 Pwr Brd Chksum1

16 Motor Thermistor 63 Shear Pin 105 Pwr Brd Chksum2

17 Input Phase Loss 64 Drive OverLoad 106 Incompat MCB-PB

20 TorqPrv Spd Band 69 DB Resistance 107 Replaced MCB-PB

21 Output PhaseLoss 70 Power Unit 108 Anlg Cal Chksum

24 Decel Inhibit 71- 75 Port 1-5 Adapter 120 I/O Mismatch

25 OverSpeed Limit 77 IR Volts Range 121 I/O Comm Loss

29 Analog In Loss 78 FluxAmpsRef Rang 122 I/O Failure

33 Auto Rstrt Tries 79 Excessive Load 130 Hardware Fault

36 SW OverCurrent 80 AutoTune Aborted 131 Hardware Fault

38 Phase U to Grnd 81- 85 Port 1-5 DPI Loss

Fault numbers not listed are reserved for future use.

Clearing Alarms

Alarms are automatically cleared when the condition that caused the alarm is no longer present.

| (1)   |
|-------|

Troubleshooting

2-9

20B-UM001.book Page 10 Thursday, June 20, 2013 1:55 PM

2-10

Alarm

Analog In

Loss

Bipolar

Conflict

Troubleshooting

Alarm Descriptions

Table 2.C Alarm Descriptions and Actions

(1)

No.Type

5

Description

➀ An analog input is configured for "Alarm" on signal loss and signal loss has occurred.

20 ➁ Parameter 190 [Direction Mode] is set to "Bipolar" or "Reverse Dis" and one or more of the following digital input functions is configured: "Fwd/Reverse,"

"Run Forward," "Run Reverse," "Jog Forward" or "Jog Reverse."

Brake Slipped 32 ➁ Encoder movement has exceeded the level in [BrkSlipCount] after the brake

17 ➁ Digital input functions are in conflict. Combinations marked with a " " will

Acc2/Dec2 Accel 2 Decel 2 Jog* Jog Fwd Jog Rev Fwd/Rev

18 ➁ A digital Start input has been configured without a Stop input or other functions are in conflict. Combinations that conflict are marked with a " "

Fwd/

Rev

CF Run Run Fwd Run Rev Jog* Jog Fwd Jog Rev

19 ➁ More than one physical input has been configured to the same input function.

Multiple configurations are not allowed for the following input functions.

Forward/Reverse Run Reverse Bus Regulation Mode B

➀ The calculated IGBT temperature requires a reduction in PWM frequency. If

[Drive OL Mode] is disabled and the load is not reduced, an overload fault will

<!-- image -->

| was set.  Decel Inhibt 10 ➀ Drive is being inhibited from decelerating.  Dig In  ConflictA  cause an alarm.  Dig In  ConflictB  and will cause an alarm.  Dig In  ConflictC  Speed Select 1 Jog Forward Acc2 / Dec2  Speed Select 2 Jog Reverse Accel 2  Speed Select 3 Run Decel 2  Run Forward Stop Mode B  Drive OL  Level 1  8  eventually occur.  * Jog 1 and Jog 2 with Vector Control Option  Acc2 / Dec2  Accel 2  Decel 2  Jog*  Jog Fwd  Jog Rev  Fwd/Rev  * Jog 1 and Jog 2 with Vector Control Option  Start  Stop-  Start  Stop-CF  Run  Run Fwd  Run Rev  Jog*  Jog Fwd  Jog Rev  Fwd/Rev   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

20B-UM001.book Page 11 Thursday, June 20, 2013 1:55 PM

(1)

No.Type

9

Description

➀ The calculated IGBT temperature requires a reduction in Current Limit. If

[Drive OL Mode] is disabled and the load is not reduced, an overload fault will eventually occur.

26 ➁ The calculated or measured Flux Amps value is not within the expected

Alarm

Drive OL

Level 2

FluxAmpsRef

Rang

Ground Warn 15 ➀ Ground current has exceeded the level set in [Gnd Warn Level].

13 ➀ The DC bus ripple has exceeded the level in [Phase Loss Level].

➀ The drive has temporarily disabled the DB regulator because the resistor temperature has exceeded a predetermined value.

25 ➁ The drive auto tuning default is "Calculate" and the value calculated for IR

Drop Volts is not in the range of acceptable values. This alarm should clear when all motor nameplate data is properly entered.

Load Loss 14 Output torque current is below [Load Loss Level] for a time period greater

23 ➁ The sum of [Maximum Speed] and [Overspeed Limit] exceeds [Maximum

Freq]. Raise [Maximum Freq] or lower [Maximum Speed] and/or [Overspeed

Limit] so that the sum is less than or equal to [Maximum Freq].

12 The value at the thermistor terminals has been exceeded.

➁ [Motor Type] has been set to "Synchr Reluc" or "Synchr PM" and one or more

[Torque Perf Mode] = "Sensrls Vect," "SV Economize" or "Fan/Pmp V/Hz."

22 ➁ Fan/pump mode is selected in [Torq Perf Mode] and the ratio of [Motor NP

➁ PTC is enabled for Analog In 1, which is configured as a 0-20 mA current

Sleep Config 29 ➁ Sleep/Wake configuration error. With [Sleep-Wake Mode] = "Direct," possible causes include: drive is stopped and [Wake Level] &lt; [Sleep Level]."Stop=CF,"

"Run," "Run Forward," or "Run Reverse." is not configured in [Digital Inx Sel].

27 ➁ [Speed Ref x Sel] or [PI Reference Sel] is set to "Reserved".

➀ [Start At PowerUp] is enabled. Drive may start at any time within 10 seconds

<!-- image -->

| OvrHeat IR Volts Range                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Ixo Vlt Rang 28 ➁ Motor leakage inductance is out of range.                                                                                        |
| than [Load Loss time].                                                                                                                             |
| Conflict                                                                                                                                           |
| Motor Thermistor Motor Type 21                                                                                                                     |
| Cflct of the following exist:                                                                                                                      |
| •  •  [Flux Up Time] is greater than 0.0 Secs.                                                                                                     |
| •  [Speed Mode] is set to “Slip Comp.” •  [Autotune] = “Static Tune” or “Rotate Tune.” NP Hz Conflict Hertz] to [Maximum Freq] is greater than 26. |
| Power Loss 3  ➀ Drive has sensed a power line loss.                                                                                                |
| Precharge Active 1  ➀ Drive is in the initial DC bus precharge state. PTC Conflict 31  source in [Anlg In Config].                                 |
| Speed Ref                                                                                                                                          |
| Cflct                                                                                                                                              |
| Start At PowerUp 4  of drive powerup.                                                                                                              |

Troubleshooting

2-11

20B-UM001.book Page 12 Thursday, June 20, 2013 1:55 PM

2-12

Troubleshooting

(1)

Alarm

TB Man Ref

Cflct

Vector

No.Type

Description

30 ➁ Occurs when:

·

"Auto/Manual" is selected (default) for [Digital In3 Sel], parameter 363

and

·

[TB Man Ref Sel], parameter 96 has been reprogrammed.

No other use for the selected analog input may be programmed.

Example: If [TB Man Ref Sel] is reprogrammed to "Analog In 2," all of the factory default uses for "Analog In 2" must be reprogramed (such as

Verify/reprogram the parameters that reference an analog input

Reprogram [Digital In3] to another function or "Unused."

49 ➁ When [TorqProve Cnfg] is enabled, [Motor Cntl Sel], [Feedback Select] and

[Motor Fdbk Type] must be properly set (refer to page C-4).

➀ The bus voltage has dropped below a predetermined value.

VHz Neg Slope 24 ➁ [Torq Perf Mode] = "Custom V/Hz" &amp; the V/Hz slope is negative.

Waking 11 ➀ The Wake timer is counting toward a value that will start the drive.

Alarm No.(1) Alarm No.(1) Alarm

1 Precharge Active 13 In Phase Loss 25 IR Volts Range

2 UnderVoltage 14 Load Loss 26 FluxAmpsRef Rang

3 Power Loss 15 Ground Warn 27 Speed Ref Cflct

4 Start At PowerUp 17 Dig In ConflictA 28 Ixo Vlt Rang

<!-- image -->

5 Analog in Loss 18 Dig In ConflictB 29 Sleep Config

6 IntDBRes OvrHeat 19 Dig In ConflictC 30 TB Man Ref Cflct

8 Drive OL Level 1 20 Bipolar Conflict 31 PTC Conflict

9 Drive OL Level 2 21 Motor Type Cflct 32 Brake Slipped

10 Decel Inhibt 22 NP Hz Conflict 49 Torq Prove Cflct

11 Waking 23 MaxFreq Conflict

12 Motor Thermistor 24 VHz Neg Slope

Alarm numbers not listed are reserved for future use.

| (1)   |
|-------|

20B-UM001.book Page 13 Thursday, June 20, 2013 1:55 PM

Troubleshooting

2-13

Common Symptoms and Corrective Actions

Drive does not Start from Start or Run Inputs wired to the terminal block.

Cause(s) Indication Corrective Action

Drive is Faulted Flashing red status light

Clear fault.

·

Press Stop

·

·

·

Cycle power

Set [Fault Clear] to 1 (See page 1-46)

"Clear Faults" on the HIM

Diagnostic menu.

## Incorrect input wiring. Refer to the None Wire inputs correctly and/or install

jumper.

None Program [Digital Inx Sel] for correct inputs. (See page 1-58)

Start or Run programming may be missing.

Program [Digital Inx Sel] to resolve conflicts. (See page 1-58)

Remove multiple selections for the same function.

Install stop button to apply a signal at stop terminal.

None If 2 wire control is required, no action needed.

If 3 wire control is required, program [Digital

Inx Sel] for correct inputs. (See page 1-58)

| Installation Instructions for wiring examples.                                                                                                                                            | Installation Instructions for wiring examples.                                                                                                  | Installation Instructions for wiring examples.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| •                                                                                                                                                                                         | 2 wire control requires Run, Run                                                                                                                |                                                  |
| •  inputs. •  required.                                                                                                                                                                   | Forward, Run Reverse or Jog input. 3 wire control requires Start and Stop Jumper from terminal 25 to 26 is Incorrect digital input programming. |                                                  |
| •  •  2 wire and 3 wire programming may be conflicting. •  Exclusive functions (i.e, direction control) may have multiple inputs configured. •  Stop is factory default and is not wired. | Mutually exclusive choices have been made (i.e., Jog and Jog Forward). Flashing yellow status light and “DigIn CflctB” indication on LCD HIM.   |                                                  |
|                                                                                                                                                                                           | [Drive Status 2] shows type 2 alarm(s).                                                                                                         |                                                  |
| control. HIM Start button is disabled for 2 wire control.                                                                                                                                 | Drive does not Start from HIM. Cause(s) Indication Corrective Action Drive is programmed for 2 wire                                             |                                                  |

Drive does not respond to changes in speed command.

Cause(s) Indication Corrective Action

No value is coming from the source

LCD HIM Status

1. If the source is an analog input, check wiring and use a meter to check for

presence of signal.

2. Check [Commanded Freq] for correct source. (See page 1-12)

| of the command. Line indicates   |
|----------------------------------|
| “At Speed” and output is 0 Hz.   |

20B-UM001.book Page 14 Thursday, June 20, 2013 1:55 PM

2-14

Troubleshooting

Cause(s) Indication Corrective Action

Incorrect reference source has been programmed.

Incorrect Reference source is being selected via remote device or

digital inputs.

| Cause(s) Indication Corrective Action                                                           |
|-------------------------------------------------------------------------------------------------|
| Excess load or short acceleration times force the drive into current limit, slowing or stopping |

Speed command source or value is

## not as expected. Programming is preventing the

None 3. Check [Speed Ref Source] for the source of the speed reference. (See page 1-43)

4. Reprogram [Speed Ref A Sel] for correct source. (See page 1-24)

None 5. Check [Drive Status 1], page 1-41, bits 12

and 13 for unexpected source selections.

6. Check [Dig In Status], page 1-44 to see if inputs are selecting an alternate source.

7. Reprogram digital inputs to correct "Speed

Sel x" option. (See page 1-58)

Motor and/or drive will not accelerate to commanded speed.

Acceleration time is excessive. None Reprogram [Accel Time x]. (See page 1-31)

None Check [Drive Status 2], bit 10 to see if the drive is in Current Limit. (See page 1-42)

Remove excess load or reprogram [Accel Time x].(See page 1-31)

None Check for the proper Speed Command using

Steps 1 through 7 above.

None Check [Maximum Speed] (See page 1-22) and

[Maximum Freq] (See page 1-16) to assure that speed is not limited by programming.

None 1. Correctly enter motor nameplate data.

2. Perform "Static" or "Rotate" Autotune procedure. (Param #061, page 1-17)

| drive output from exceeding limiting                               |
|--------------------------------------------------------------------|
| Motor operation is unstable. Cause(s) Indication Corrective Action |
| Motor data was incorrectly entered or Autotune was not performed.  |

Drive will not reverse motor direction.

Cause(s) Indication Corrective Action

Digital input is not selected for

| reversing control.                                                                                               |
|------------------------------------------------------------------------------------------------------------------|
| Digital input is incorrectly wired. None Check input wiring. Direction mode parameter is incorrectly programmed. |

Motor wiring is improperly phased for reverse.

## A bipolar analog speed command

None Check [Digital Inx Sel], page 1-58. Choose correct input and program for reversing mode.

None Reprogram [Direction Mode], page 1-38 for analog "Bipolar" or digital "Unipolar" control.

None Switch two motor leads.

None 1. Use meter to check that an analog input voltage is present.

2. Check wiring.

Positive voltage commands forward direction.

Negative voltage commands reverse direction.

| absent.   | input is incorrectly wired or signal is   |
|-----------|-------------------------------------------|

20B-UM001.book Page 15 Thursday, June 20, 2013 1:55 PM

Stopping the drive results in a Decel Inhibit fault.

Cause(s) Indication Corrective Action

The bus regulation feature is enabled and is halting deceleration

due to excessive bus voltage.

Excess bus voltage is normally due to excessive regenerated energy or

unstable AC line input voltages.

Internal timer has halted drive

## operation.

1. See Attention statement on page P-4

2. Reprogram parameters 161/162 to eliminate any "Adjust Freq" selection.

3. Disable bus regulation (parameters 161 &amp;

162) and add a dynamic brake.

4. Correct AC input line instability or add an isolation transformer.

5. Reset drive.

Decel Inhibit fault screen.

LCD Status Line indicates

Troubleshooting

.

2-15

20B-UM001.book Page 16 Thursday, June 20, 2013 1:55 PM

2-16

Troubleshooting

Testpoint Codes and Functions

Select testpoint with [Testpoint x Sel], parameters 234/236. Values can be viewed with [Testpoint x Data], parameters 235/237.

Values

Minimum Maximum Default

No.(1)

Description Units

01 DPI Error Status 1 0 255 0

02 Heatsink Temp 0.1 degC –100.0 100.0 0

03 Active Cur Limit 1 0 32767 0

04 Active PWM Freq 1 Hz 2 10 4

05 Life MegaWatt Hr(2) 0.0001 MWh 0 214748.3647 0 06 Life Run Time 0.0001 Hrs 0 214748.3647 0

07 Life Pwr Up Time 0.0001 Hrs 0 214748.3647 0

08 Life Pwr Cycles 1 0 4294967295 0

1 0 4294967295 0

1 0 4294967295 0

11 MCB Life Time 0.0001 Hrs 0 214748.3647 0

12 Raw Analog In 1 1 0 0

13 Raw Analog In 2 1 0 0

16 CS Msg Rx Cnt 1 0 65535 0

17 CS Msg Tx Cnt 1 0 65535 0

18 CS Timeout Cnt 1 0 255 0

19 CS Msg Bad Cnt 1 0 255 0

22 PC Msg Rx Cnt 1 0 65535 0

23 PC Msg Tx Cnt 1 0 65535 0

24-29 PC1-6 Timeout Cnt 1 0 255 0

30 CAN BusOff Cnt 1 0 65535 0

31 No. of Analog Inputs 1 0 x 0

32 Raw Temperature 1 0 65535 0

33 MTO Norm Mtr Amp 0.1 Amps 0 65535 0

34 DTO-Cmd Frequency 1 0 420 0

35 DTO-Cmd Cur Lim 0.1 0 0

36 DTO-Cmd DC Hold 1 0 32767 0

37 Control Bd Temp 0.1 0.0 60.0 0.0

Use the equation below to calculate total Lifetime MegaWatt Hours.

= Total Lifetime MegaWatt Hours

| 09 Life MW-HR Fract(2)                                                                                                       |                   |
|------------------------------------------------------------------------------------------------------------------------------|-------------------|
| 10 MW-HR Frac Unit(2)                                                                                                        |                   |
| (1)  Enter in [Testpoint x Sel].                                                                                             |                   |
| Value of Code 9 Value of Code 9 Vlf Cd10 --------------------------------- × 0.1 ⎝ ⎠ ⎛ ⎞                                                                                                                              |                   |
| Value of Code 10  ---------------------------------  × 0.1  Value of Code 10 --------------------------------- × 0.1 ⎝ ⎠ ⎛ ⎞ | + Value of Code 5 |

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

Frame

## 0

1

Appendix A

Supplemental Drive Information

Communication Configurations

Drive Frame Sizes

Similar PowerFlex 700 drive sizes are grouped into frame sizes to simplify spare parts ordering, dimensioning, etc. A cross reference of

drive catalog numbers and their respective frame size is provided below.

Table A.A AC Input

208/240 400V 480V 600V 690V

ND Hp HD Hp ND kW HD kW ND Hp HD Hp ND Hp HD Hp ND kW HD kW

0.5 0.33 0.37 0.25 0.5 0.33 1 0.5 – –

1 0.75 0.75 0.55 1 0.75 2 1 – –

– – 1.5 0.75 2 1.5 3 2 – – – – 2.2 1.5 3 2 5 3 – – – – 4 2.2 5 3 7.5 5 – –

– – 5.5 4 7.5 5 – – – –

2 1.5 7.5 5.5 10 7.5 10 7.5 – –

3 2 11 7.5 15 10 15 10 – –

53––––––––

7.5 5 – – – – – – – –

10 7.5 15 11 20 15 20 15 – –

– – 18.5 15 25 20 25 20 – –

15 10 22 18.5 30 25 30 25 – –

20 15 30 22 40 30 40 30 – –

– – 37 30 50 40 50 40 – –

25 20 45 37 60 50 60 50 – –

30 25 – – – – – – – –

40 30 55 45 75 60 75 60 45 37.5

50 40 75 55 100 75 100 75 55 45

– – – – – – – – 75 55

– – – – – – – – 90 75

60 50 90 75 125 100 125 100 110 90

75 60 110 90 150 125 150 125 132 110

100 75 132 110 200 150 – – – –

|   2 |
|-----|
|   3 |
|   4 |
|   5 |
|   6 |

A-1

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

A-2

Frame

0

1

Supplemental Drive Information

Table A.B DC Input

325V 540V 650V 810V 932V

ND Hp HD Hp ND kW HD kW ND Hp HD Hp ND Hp HD Hp ND kW HD kW

0.5 0.33 – – 0.5 0.33 1 0.75 – –

1 0.75 – – 1 0.75 2 1.5 – –

– – – – 2 1.5 3 2 – –

––––3253––

– – – – 5 3 7.5 5 – –

– – – – 7.5 5 10 7.5 – –

2 1.5 0.37 0.25 10 7.5 15 10 – –

3 2 0.75 0.55 15 10 – – – –

5 3 1.5 0.75 – – – – – –

7.5 5 2.2 1.5 – – – – – –

– – 4 2.2 – – – – – –

– – 5.5 4 – – – – – –

– – 7.5 5.5 – – – – – –

– – 11 7.5 – – – – – –

10 7.5 15 11 20 15 20 15 – –

– – 18.5 15 25 20 25 20 – –

15 10 22 18.5 30 25 30 25 – –

20 15 30 22 40 30 40 30 – –

– – 37 30 50 40 50 40 – –

25 20 45 37 60 50 60 50 – –

30 25 – – – – – – – –

40 30 55 45 75 60 100 75 45 37.5

50 40 – – 100 75 – – 90 75

60 50 75 55 125 100 150 125 132 110

75 60 90 75 150 125 – – – –

100 75 110 90 – – – – – –

– – 132 110 200 150 – – – –

Typical Programmable Controller Configurations

Important: If block transfers are programmed to continuously write information to the drive, care must be taken to properly

format the block transfer. If attribute 10 is selected for the block transfer, values will be written only to RAM and will

| 2   |                              |
|-----|------------------------------|
| 3   |                              |
| 4   |                              |
| 5   |                              |
| 6   |                              |
|     | Communication Configurations |

not be saved by the drive. This is the preferred attribute for continuous transfers. If attribute 9 is selected, each program

scan will complete a write to the drives non-volatile memory (EEprom). Since the EEprom has a fixed number

of allowed writes, continuous block transfers will quickly damage the EEprom. Do Not assign attribute 9 to continuous block transfers. Refer to the individual communications adapter User Manual for details.

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

Logic Command/Status Words

Figure A.1 Logic Command Word

Logic Bits

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 Command Description x Stop(1)

x Start(1)(2)

0 = Not Stop

1 = Stop

0 = Not Start

1 = Start x Jog 0 = Not Jog

1 = Jog

0 = Not Clear Faults

1 = Clear Faults x Clear

Faults x x Direction 00 = No Command

01 = Forward Command

10 = Reverse Command

11 = Hold Present Direction

0 = No Local Control

1 = Local Control

0 = Not Increment

1 = Increment

Control

Increment x x Accel Rate 00 = No Command

01 = Use Accel Time 1

10 = Use Accel Time 2

11 = Use Present Time x x Decel Rate 00 = No Command

01 = Use Decel Time 1

10 = Use Decel Time 2

11 = Use Present Time

000 = No Command

001 = Ref. 1 (Ref A Select)

010 = Ref. 2 (Ref B Select)

011 = Ref. 3 (Preset 3)

100 = Ref. 4 (Preset 4)

101 = Ref. 5 (Preset 5)

110 = Ref. 6 (Preset 6)

111 = Ref. 7 (Preset 7)

0 = Not Decrement

1 = Decrement

Select(3)

Decrement

A "0 = Not Stop" condition (logic 0) must first be present before a "1 = Start" condition will start the drive. The Start command acts as a momentary Start command. A "1" will start the

This Start will not function if a digital input (parameters 361-366) is programmed for 2-Wire

This Reference Select will not function if a digital input (parameters 361-366) is programmed for "Speed Sel 1, 2 or 3" (option 15, 16 or 17). Note that Reference Selection is "Exclusive

Supplemental Drive Information

<!-- image -->

| x Local                                                                               |
|---------------------------------------------------------------------------------------|
| x MOP                                                                                 |
| x x x Reference                                                                       |
| x MOP                                                                                 |
| drive, but returning to “0” will not stop the drive. (2)  Control (option 7, 8 or 9). |
| Ownership” see [Reference Owner] on page 1-53 .                                       |

A-3

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

A-4

Supplemental Drive Information

Figure A.2 Logic Status Word

Logic Bits

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 Status Description x Ready 0 = Not Ready

1 = Ready x Active 0 = Not Active

1 = Active x Command

Direction

Direction

0 = Reverse

1 = Forward

0 = Reverse

1 = Forward x Accel 0 = Not Accelerating

1 = Accelerating x Decel 0 = Not Decelerating

1 = Decelerating x Alarm 0 = No Alarm

1 = Alarm x Fault 0 = No Fault

1 = Fault x At Speed 0 = Not At Reference

1 = At Reference

000 = Port 0 (TB)

001 = Port 1

010 = Port 2

011 = Port 3

100 = Port 4

101 = Port 5

110 = Reserved

111 = No Local

0000 = Ref A Auto

0001 = Ref B Auto

0010 = Preset 2 Auto

0011 = Preset 3 Auto

0100 = Preset 4 Auto

0101 = Preset 5 Auto

0110 = Preset 6 Auto

0111 = Preset 7 Auto

1000 = Term Blk Manual

1001 = DPI 1 Manual

1010 = DPI 2 Manual

1011 = DPI 3 Manual

1100 = DPI 4 Manual

1101 = DPI 5 Manual

1110 = Reserved

1111 = Jog Ref

<!-- image -->

Control(1)

Source

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

HIM Overview

For information on . . See page . . For information on . . See page . .

External and Internal Connections B-1

LCD Display Elements

ALT Functions

B-2

B-2

Menu Structure

Viewing and Editing

Parameters

Removing/Installing the

HIM

External and Internal Connections

The PowerFlex 700 provides a number of cable connection points

1or or3

➌

<!-- image -->

| (0 Frame shown).   |
|--------------------|

➊

➍

<!-- image -->

B-3

B-5

B-8

!

DANGER

DPI Port 2 Cable connection for handheld and remote options.

DPI Port 3 or 2 Splitter cable connected to DPI Port 2 provides additional port.

DPI Port 5 Cable connection for communications adapter.

2

Appendix B

➋

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

B-2

HIM Overview

LCD Display Elements

Display Description

F-&gt; Power Loss Auto

0.0

Hz

Main Menu:

Diagnostics

## Parameter Device Select

Direction⎥ Drive Status⎥ Alarm⎥ Auto/Man⎥ Information

Commanded or Output Frequency

Programming / Monitoring / Troubleshooting

The top line of the HIM display can be configured with [DPI Fdbk Select], parameter 299

To use an ALT function, press the ALT key, release it, then press the programming key associated with one of the following functions:

<!-- image -->

Table B.A ALT Key Functions

ALT Key and then … Performs this function …

Esc

Sel

S.M.A.R.T. Displays the S.M.A.R.T. screen.

View Allows the selection of how parameters will be viewed or detailed information about a

parameter or component. Lang Displays the language selection screen.

Auto / Man Switches between Auto and Manual Modes.

Remove Allows HIM removal without causing a fault if the

HIM is not the last controlling device and does not have Manual control of the drive.

Exp Allows value to be entered as an exponent

(Not available on PowerFlex 700).

Param # Allows entry of a parameter number for viewing/

<!-- image -->

| ALT   |
|-------|
| .     |
| +/–   |

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

Menu Structure

Figure B.1 HIM Menu Structure

User

Display

Faults

Esc

<!-- image -->

HIM Overview

B-3

Fault Info

Drive Status 1

Drive Status 2

Drive Alarm 1

Drive Alarm 2

Speed Ref Source

Start Inhibits

Last Stop Source

Dig In Status

Dig Out Status

Drive Temp

Drive OL Count

Motor OL Count

FGP: Group

Group 1 Name

Group 2 Name

Group 3 Name

View Fault Queue

Clear Faults

Clr Fault Queue

Reset Device

Basic

Advanced

FGP: Parameter

Parameter Name

Parameter Name

Parameter Name

Value Screen

Device -&gt; HIM

Device &lt;- HIM

Delete HIM Set

Complete Steps:

1. Input Voltage

2. Motor Dat/Ramp

3. Motor Tests

4. Speed Limits

5. Speed Control

6. Strt/Stop/I/O

7. Done/Exit

Make a selection:

Abort

Backup

Resume

Start-Up Menu to move between menu items

to select a menu item to move 1 level back in the menu structure

Press to select how to view parameters
ALT Sel

Esc

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

B-4

HIM Overview

Diagnostics Menu

When a fault trips the drive, use this menu to access detailed data about the drive.

Option Description

Faults View fault queue or fault information, clear faults or reset drive.

Status Info View parameters that display status information about the drive.

Device Version View the firmware version and hardware series of components.

HIM Version View the firmware version and hardware series of the HIM.

Parameter Menu

Refer to Viewing and Editing Parameters on page B-5

.

Use this menu to access parameters in connected peripheral devices.

| Device Select Menu   |
|----------------------|

Memory Storage Menu

Drive data can be saved to, or recalled from, User and HIM sets.

User sets are files stored in permanent nonvolatile drive memory.

HIM sets are files stored in permanent nonvolatile HIM memory.

Option Description

Save data to a HIM set, load data from a HIM set to active drive

HIM Copycat Device -&gt; HIM memory or delete a HIM set.

Device &lt;- HIM

Device User Sets Save data to a User set, load data from a User set to active drive memory or name a User set. Reset To Defaults Restore the drive to its factory-default settings.

Start Up Menu

The HIM and drive have features that you can customize.

| See Installation Instructions.   |
|----------------------------------|
| Option Description               |

Drive Identity Add text to identify the drive.

Change Password Enable/disable or modify the password.

User Dspy Lines Select the display, parameter, scale and text for the User Display.

The User Display is two lines of user-defined data that appears when the HIM is not being used for programming.

User Dspy Time Set the wait time for the User Display or enable/disable it.

User Dspy Video Select Reverse or Normal video for the Frequency and User

Display lines.

Reset User Dspy Return all the options for the User Display to factory default values.

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

or

HIM Overview

B-5

The PowerFlex 700 drive is initially set to Basic Parameter View. To view all parameters, set parameter 196 [Param Access Lvl] to option 1

"Advanced". Parameter 196 is not affected by the Reset to Defaults function.

Viewing and Editing Parameters

LCD HIM Step Key(s) Example Displays 1. In the Main Menu, press the Up Arrow or Down Arrow to scroll to "Parameter." or

## 2. Press Enter. "FGP File" appears on the top

line and the first three files appear below it.

3. Press the Up Arrow or Down Arrow to scroll through the files.

<!-- image -->

FGP: File

Monitor

Motor Control

Speed Reference

FGP: Group

Motor Data

Torq Attributes

Volts per Hertz

FGP: Parameter

Maximum Voltage

Maximum Freq

Compensation

FGP: Par 55

Maximum Freq

60.00 Hz

25 &lt;&gt; 400.00

FGP: Par 55

Maximum Freq

90.00 Hz

25 &lt;&gt; 400.00

If using a HIM with a numeric keypad, press the ALT key and the +/–

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

B-6

HIM Overview

Linking Parameters (Vector Control Option Only)

Most parameter values are entered directly by the user. However, certain parameters can be "linked," so the value of one parameter becomes the

value of another. For Example: the value of an analog input can be linked to [Accel Time 2]. Rather than entering an acceleration time directly (via

HIM), the link allows the value to change by varying the analog signal.

This can provide additional flexibility for advanced applications.

## Each link has 2 components:

·

Source parameter – sender of information.

· Destination parameter – receiver of information. Most parameters can be a source of data for a link, except parameter values that contain an integer representing an ENUM (text choice). These are not allowed, since the integer is not actual data (it represents a value). Table B.B lists the parameters that can be destinations. All links must be established between equal data types (parameter value formatted

in floating point can only source data to a destination parameter value

- that is also floating point).

Establishing A Link

Step Key(s) Example Displays 1. Select a valid destination parameter (see Table B.B) to be linked (refer to page B-5). The parameter value screen will appear. 2. Press Enter to edit the parameter. The cursor will move to the value line.

FGP: Parameter

Accel Time 1

Accel Time 2

Decel Time 1

Min: 0.1 Secs

Max: 3600.0 Secs

Dflt: 10.0 Secs

Present Value

.

.

.

Define Link

Parameter: #141

Accel Time 2

Link:

017

Analog In1 Value

3. Press ALT and then View (Sel). Next, press the Up or Down Arrow to change "Present

Sel

ALT +

<!-- image -->

20B-UM001.book Page 7 Thursday, June 20, 2013 1:55 PM

Table B.B Linkable Parameters

Number Parameter

54 Maximum Voltage

56 Compensation

57 Flux Up Mode

58 Flux Up Time

59 SV Boost Filter

62 IR Voltage Drop

63 Flux Current Ref

69 Start/Acc Boost

70 Run Boost

| 71 Break Voltage                  |
|-----------------------------------|
| 72 Break Frequency                |
| 84 Skip Frequency 1               |
| 85 Skip Frequency 2               |
| 86 Skip Frequency 3               |
| 87 Skip Freq Band                 |
| 91 Speed Ref A Hi                 |
| 92 Speed Ref A Lo                 |
| 94 Speed Ref B Hi                 |
| 95 Speed Ref B Lo                 |
| 97 TB Man Ref Hi                  |
| 98 TB Man Ref Lo                  |
| 100 Jog Speed                     |
| 101 Preset Speed 1                |
| 102 Preset Speed 2                |
| 103 Preset Speed 3                |
| 104 Preset Speed 4                |
| 105 Preset Speed 5                |
| 106 Preset Speed 6                |
| 107 Preset Speed 7                |
| 119 Trim Hi                       |
| 120 Trim Lo                       |
| 121 Slip RPM @ FLA                |
| 122 Slip Comp Gain                |
| 123 Slip RPM Meter                |
| 127 PI Setpoint                   |
| 129 PI Integral Time              |
| 130 PI Prop Gain                  |
| 131 PI Lower Limit                |
| 132 PI Upper Limit                |
| 133 PI Preload                    |
| 140 Accel Time 1                  |
| 141 Accel Time 2 142 Decel Time 1 |
| 143 Decel Time 2                  |
| 146 S-Curve %                     |
| 148 Current Lmt Val               |
| 149 Current Lmt Gain              |
| 151 PWM Frequency                 |
| 158 DC Brake Level                |

Number Parameter

159 DC Brake Time

160 Bus Reg Ki

164 Bus Reg Kp

165 Bus Reg Kd

175 Auto Rstrt Delay

180 Wake Level

181 Wake Time

182 Sleep Level

183 Sleep Time

386 Dig Out2 OnTime

| 185 Power Loss Time                     |
|-----------------------------------------|
| 186 Power Loss Level                    |
| 321 Anlg In Sqr Root                    |
| 322 Analog In1 Hi                       |
| 323 Analog In1 Lo                       |
| 324 Analog In1 Loss                     |
| 325 Analog In2 Hi                       |
| 326 Analog In2 Lo                       |
| 327 Analog In2 Loss                     |
| 343 Analog Out1 Hi                      |
| 344 Analog Out1 Lo                      |
| 346 Analog Out2 Hi                      |
| 347 Analog Out2 Lo                      |
| 381 Dig Out1 Level 382 Dig Out1 OnTime  |
| 383 Dig Out1 OffTime 385 Dig Out2 Level |

387 Dig Out2 OffTime

389 Dig Out3 Level

390 Dig Out3 OnTime

391 Dig Out3 OffTime

416 Fdbk Filter Sel

419 Notch Filter Freq

420 Notch Filter K

428 Torque Ref A Hi

429 Torque Ref A Lo

430 Torq Ref A Div

432 Torque Ref B Hi

433 Torque Ref B Lo

434 Torq Ref B Mult

435 Torque Setpoint

436 Pos Torque Limit

437 Neg Torque Limit

445 Ki Speed Loop

446 Kp Speed Loop

447 Kf Speed Loop

449 Speed Desired BW

450 Total Inertia

454 Rev Speed Limit

460 PI Reference Hi

461 PI Reference Lo

152 Droop RPM @ FLA

153 Regen Power Limit

154 Current Rate Limit

HIM Overview

B-7

Number Parameter

462 PI Feedback Hi

463 PI Feedback Lo

476-494 ScaleX In Value

477-495 ScaleX In Hi

478-496 ScaleX In Lo

479-497 ScaleX Out Hi

480-498 ScaleX Out Lo

602 Spd Dev Band

603 SpdBand Integrat

604 Brk Release Time

605 ZeroSpdFloatTime

606 Float Tolerance

607 Brk Set Time

608 TorqLim SlewRate

609 BrkSlip Count

610 Brk Alarm Travel

611 MicroPos Scale%

20B-UM001.book Page 8 Thursday, June 20, 2013 1:55 PM

B-8

HIM Overview

Removing/Installing the HIM

The HIM can be removed or installed while the drive is powered.

Important: HIM removal is only permissible in Auto mode. If the HIM

is removed while in Manual mode or the HIM is the only remaining control device, a fault will occur.

Key(s)

ALT +

Example Displays

Remove Op Intrfc:

Press Enter to

Disconnect Op Intrfc?

(Port 1 Control)

Step

## To remove the HIM . . .

1. Press ALT and then Enter (Remove). The

Remove HIM confirmation screen appears.

2. Press Enter to confirm that you want to remove the HIM. 3. Remove the HIM from the drive.

<!-- image -->

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

Application Notes

Lifting/Torque Proving

## Minimum Speed

Motor Control Technology

Motor Overload

Overspeed

Power Loss Ride Through

AC Input

C-2

C-7

C-8

C-10

C-11

C-12

R (L1)

S (L2)

T (L3)

Power Off

M

Power Source DB Resistor Thermostat

Appendix C

Control

Reverse Speed Limit

C-16

Skip Frequency

Sleep Wake Mode

Start At PowerUp

Stop Mode

Voltage Tolerance

Power On

M

| External Brake Resistor                      |
|----------------------------------------------|
| Figure C.1 External Brake Resistor Circuitry |
| Three-Phase                                  |

(Input Contactor) M

<!-- image -->

C-17

C-19

C-21

C-22

C-24

<!-- image -->

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

C-2

Application Notes

Lifting/Torque Proving

The lifting/torque proving feature of the PowerFlex 700 is intended for applications where proper coordination between motor control and a

mechanical brake is required. Prior to releasing a mechanical brake, the drive will check motor output phase continuity and verify proper motor

control (torque proving). The drive will also verify that the mechanical brake has control of the load prior to releasing drive control (brake

proving). After the drive sets the brake, motor movement is monitored to ensure the brakes ability to hold the load.

Lifting Application functionality includes: · Torque Proving (includes flux up and last torque measurement). · Brake Proving (includes mode to slowly lower load if brake slips/ fails). · Float Capability · Micro-Positioning · Fast Stop

·

Speed Deviation Fault, Output Phase Loss Fault, Encoder Loss Fault.

The Lifting/Torque Proving feature is only available in Vector firmware

- versions 3.xxx and later. It is intended to operate in the FVC Vector Control mode (see [Motor Cntl Sel], parameter 053) with an encoder.

Motor movement is monitored through the encoder feedback which excludes the other feedback modes from being used.

- ATTENTION: Loss of control in suspended load applications can

cause personal injury and/or equipment damage. Loads must always be

! controlled by the drive or a mechanical brake. Parameters 600-611 are designed for lifting/torque proving applications. It is the responsibility of the engineer and/or end user to configure drive parameters, test any lifting functionality and meet safety requirements in accordance with all applicable codes and standards.

Lifting/Torque Proving Manual Start Up It is possible to use the Assisted Start Up to tune the motor. However, it is recommended that the motor be disconnected from the hoist/crane equipment during the routine. If this is not possible, refer to steps 1 through 12 on the following pages.

<!-- image -->

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

!

2.

Application Notes

C-3

ATTENTION: To guard against personal injury and/or equipment damage caused by unexpected brake release, verify Digital Out 1 brake

connections and/or programming. The default drive configuration energizes the Digital Out 1 relay when power is applied to the drive. If

the brake is connected to this relay, it could be released. If necessary, disconnect the relay output until wiring/programming can be verified.

Initial Static Auto Tune Test

1. Set the following parameters as shown. No. Name Value Notes 380 [Digital Out1 Sel] "9, At Speed" keeps brake engaged during test 041-045 [Motor NP . . .] per nameplate enter motor nameplate data 053 [Motor Cntl Sel] "4, FVC Vector" 080 [Feedback Select] "3, Encoder"

061 [Autotune] "1, Static Tune"

Press the Start key on the HIM. Parameters 062-064 will be updated.

No. Name Value Notes

090 [Digital Out1 Sel] "11, Preset Spd1"

| Motor Rotation/Encoder Direction Test      |
|--------------------------------------------|
| 3.  Set the following parameters as shown. |
| 053 [Motor Cntl Sel] “0, Sensrls Vect”     |
| 080 [Feedback Select] “0, Open Loop”       |

- 238 [Fault Config 1] Bit 8, "In PhaseLoss" = 1

Bit 12, "OutPhaseLoss" = 1

380 [Digital Out1 Sel] "4, Run" releases brake

Important: If the direction of travel is critical at this point, perform short jogs to determine which run direction (RUNFWD

or RUNREV) should be used in the next steps.

Press Start and run the drive in the desired direction. Observe the remove drive power and reverse the two motor leads, or . . .

| 4.                                           |
|----------------------------------------------|
| direction of motor rotation.                 |
| If rotation is not in the desired direction: |
| –                                            |

–

set bit 5 of [Compensation], parameter 56 to "Mtr Lead Rev."

5. With the drive running, observe [Encoder Speed], parameter 415. If the sign of the encoder is not the same as the displayed frequency, remove drive power and reverse encoder leads A and A NOT.

6. With the drive running, verify correct motor rotation and encoder

direction. Set [Motor Fdbk Type], parameter 412 to "1, Quad

- Check." Stop the drive.

<!-- image -->

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

C-4

Application Notes

Rotate AutoTune Test

ATTENTION: In this test the following conditions will occur:

·

·

The motor will be run for 12 seconds at base frequency (60 Hz).

Note that equipment travel during this 12 second interval may exceed equipment limits. However, travel distance can be reduced

by setting [Maximum Speed], parameter 82 to a value less than 45

Hz (i.e. 22.5 Hz = 12 seconds at 30 Hz).

The brake will be released without torque provided by the drive for

15 seconds.

To guard against personal injury and/or equipment damage, this test

7. Set the following parameters as shown. should not be performed if either of the above conditions are considered unacceptable by the user.
2. No. Name Value Notes 053 [Motor Cntl Sel] "4, FVC Vector"

080 [Feedback Select] "3, Encoder"

8. Start the drive and run the motor in the desired direction. Parameters 061 [Autotune] "2, Rotate Tune"

062, 063, 064 &amp; 121 will be updated.

Inertia AutoTune Test

Set [Inertia Autotune], parameter 067 to "1, Inertia Tune."

10. Press Start and run the motor in the direction desired. Parameters

445, 446 and 450 will be updated.

| 9.   |
|------|

11. Set [Speed Desired BW], parameter 449 to desired setting. 12. Set up is complete - check for proper operation.
2. Drive Setup
3. [TorqProve Cnfg], parameter 600 must be set to "Enabled." Once this is

set, a Type 2 alarm will be active until the following three parameter

- settings are entered:
- No. Name Value Notes

053 [Motor Cntl Sel] "4, FVC Vector"

080 [Feedback Select] "3, Encoder"

412 [Motor Fdbk Type] "1, Quad Check"

!

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

Installation/Wiring

When [TorqProve Cnfg] is set to "Enable," the Digital Out 1 relay is used to control the external brake contactor. The normally open (N.O.)

contact, when closed, is intended to energize the contactor. This provides the mechanical brake with voltage, causing the brake to release. Any

Programming [Digital Out1 Sel], parameter 380 will be ignored when

[TorqProve Cnfg] is set to "Enable."

Figure C.2 Typical Torque Proving Configuration

24 25 26 27 28 29 30 31 12 115V AC 13 Brake Set Normally Open = Brake Set

Brake

Contactor

32

Run Fwd

Run Rev

Clear Faults

Float/Micro

Fast Stop

Enable

24V configuration shown

Lifting/Torque Proving Application Programming

The PowerFlex 700 lifting application is mainly influenced by parameters 600 through 611 in the Torque Proving group of the

Application file. Figure C.3 and the paragraphs that follow describe

<!-- image -->

Figure C.3 Torque Proving Flow Diagram

Operator

Run

## Command Commands

Application Notes

Run

Command Released

Run can be initiated anytime

Drive Running [Brk Release Time] Parameter 604 Time

Drive

Actions

Torque

Prove Initiated

Brake

Released

[ZeroSpdFloatTime]

[Brk Set Time]

Parameter 605

Float

Initiated

Brake

Set

All times between Drive Actions are programmable and can be made very small

(i.e. Brake Release Time can be 0.1 seconds)

Parameter 607

<!-- image -->

C-5

Brake

Slip Test

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

C-6

Application Notes

Torque Proving

When the drive receives a start command to begin a lifting operation, the following actions occur:

1.

2.

The drive first performs a transistor diagnostic test to check for phase-to-phase and phase-to-ground shorts. A failure status from

either of these tests will result in a drive fault and the brake relay will

NOT be energized (brake remains set).

The drive will then provide the motor with flux as well as perform a check for current flow through all three motor phases. This ensures

that torque will be delivered to the load when the mechanical brake is released. When torque proving is enabled, open phase loss detection

- is performed regardless of the setting of Bit 12 of [Fault Config 1], parameter 238. 3. If the drive passes all tests, the brake will be released and the drive will take control of the load after the programmed time in [Brk
- Release Time], parameter 604 which is the typical mechanical release time of the brake. Brake Proving When the drive receives a stop command to end a lifting operation, the following actions occur:
1. The brake is commanded closed when the speed of the motor reaches zero.

2.

After the time period programmed in [Brk Set Time], parameter 607, the drive will verify if the brake is capable of holding torque. It will

do this by ramping the torque down at a rate set in [TorqLim

SlewRate], parameter 608. Note that the drive can be started again at any time without waiting for either of the above timers to finish.

3. While the torque is ramping down, the drive will perform a brake slip test. If movement exceeds the limit set in [BrkSlip Count], parameter

609, then an alarm is set and the drive will start a brake slip

- procedure. The drive will allow the motor to travel the distance programmed [Brk Alarm Travel], parameter 610. Another slip test will be performed and will repeat continuously until; A) the load stops slipping, or B) the load reaches the ground. This feature keeps control of the load and returns it to the ground in a controlled manner

in the event of a mechanical brake failure.

20B-UM001.book Page 7 Thursday, June 20, 2013 1:55 PM

Speed Monitoring / Speed Band Limit

This routine is intended to fault the drive if the difference between the speed reference and the encoder feedback is larger than the value set in

[Spd Dev Band], parameter 602 and the drive is NOT making any progress toward the reference. [SpdBand Integrat], parameter 603 sets

the time that the speed difference can be greater than the deviation band before causing a fault and setting the brake.

## Float

Float is defined as the condition when the drive is holding the load at zero hertz while holding off the mechanical brake. The float condition starts when the frequency drops below the speed set in [Float Tolerance], parameter 606. Float will stay active for a period of time set by [ZeroSpdFloatTime], parameter 605. If a digital input (parameters 361-366) is set to "Micro Pos" (also Float) and it is closed, the Float condition will stay active and will disregard the timer. This signal is also

available through a communication device, see [TorqProve Setup], parameter 601. Micro Position Micro Position refers to rescaling of the commanded frequency by a percentage entered in [MicroPos Scale %], parameter 611. This allows for slower operation of a lift which provides an operator with better resolution when positioning a load. Micro Position is activated only when the drive is running at or near zero speed. This can be initiated by a digital input configured as Micro Pos or through a communication

device ([TorqProve Setup]) which is the same digital input which signals the float condition.

Fast Stop Fast Stop is intended to stop the load as fast as possible then set the mechanical brake. The Fast Stop can be initiated from a digital input or through a communication device through [TorqProve Setup]. The difference from a normal stop is that the decel time is forced to be 0.1 seconds. When the Torque Proving function is enabled, the Float time is ignored at the end of the ramp. This feature can be used without enabling the Torque Proving function.

Refer to Reverse Speed Limit on page C-16 Minimum Speed

Application Notes

C-7

20B-UM001.book Page 8 Thursday, June 20, 2013 1:55 PM

C-8

Application Notes

Motor Control Technology

Within the PowerFlex family there are several motor control technologies:

·

Torque Producers

·

·

Torque Controllers

Speed Regulators

Torque Producers

Volts/Hertz This technology follows a specific pattern of voltage and frequency output to the motor, regardless of the motor being used. The shape of the

V/Hz curve can be controlled a limited amount, but once the shape is determined, the drive output is fixed to those values. Given the fixed

values, each motor will react based on its own speed/torque characteristics.

This technology is good for basic centrifugal fan/pump operation and for most multi-motor applications. Torque production is generally good.

Sensorless Vector This technology combines the basic Volts/Hertz concept with known motor parameters such as Rated FLA, HP, Voltage, stator resistance and flux producing current. Knowledge of the individual motor attached to the drive allows the drive to adjust the output pattern to the motor and load conditions. By identifying motor parameters, the drive can maximize the torque produced in the motor and extend the speed range

at which that torque can be produced.

This technology is excellent for applications that require a wider speed range and applications that need maximum possible torque for breakaway, acceleration or overload. Centrifuges, extruders, conveyors and others are candidates. Torque Controllers Vector

This technology differs from the two above, because it actually controls or regulates torque. Rather than allowing the motor and load to actually determine the amount of torque produced, Vector technology allows the drive to regulate the torque to a defined value. By independently identifying and controlling both flux and torque currents in the motor,

true control of torque is achieved. High bandwidth current regulators remain active with or without encoder feedback to produce outstanding

results.

20B-UM001.book Page 9 Thursday, June 20, 2013 1:55 PM

<!-- image -->

Application Notes

C-9

This technology is excellent for those applications where torque control, rather than mere torque production, is key to the success of the process.

These include web handling, demanding extruders and lifting applications such as hoists or material handling.

Vector Control can operate in one of two configurations:

1.

Encoderless

Not to be confused with Sensorless Vector above, Encoderless Vector based on Allen-Bradley's patented Field Oriented Control technology means that a feedback device is not required. Torque control can be achieved across a significant speed range without feedback.

2. Closed Loop (with Encoder)

Vector Control with encoder feedback utilizes Allen-Bradley's Force Technology™. This industry leading technology allows the drive to control torque over the entire speed range, including zero speed. For those applications that require smooth torque regulation at very low speeds or full torque at zero speed, Closed Loop Vector Control is

the answer.

Speed Regulators Any of the PowerFlex drives, regardless of their motor control technology (Volts/Hz, Sensorless Vector or Vector) can be set up to regulate speed. Speed regulation and torque regulation must be separated to understand drive operation. The PowerFlex 70 and PowerFlex 700 with Standard Control can be programmed to regulate speed using the slip compensation feature. Slip

compensation reacts to load changes by adjusting the drive output frequency to maintain motor speed. Torque production operates

independently. This feature produces speed regulation of about 0.5% of base speed over a specified speed range (40:1 for V/Hz and 80:1 for Sensorless Vector). These two drives do not have the capability to extend the speed range or tighten the speed regulation below 0.5% because they do not have connections for a feedback device.

The PowerFlex 700 with the Vector Control option can offer better speed regulation by adding speed feedback. Using a speed feedback device (encoder) tightens speed regulation to 0.001% of base speed and extends the speed range to zero speed.

20B-UM001.book Page 10 Thursday, June 20, 2013 1:55 PM

C-10

Application Notes

Motor Overload

For single motor applications the drive can be programmed to protect the motor from overload conditions. An electronic thermal overload I2T

function emulates a thermal overload relay. This operation is based on three parameters; [Motor NP FLA], [Motor OL Factor] and [Motor OL

Hertz] (parameters 042, 048 and 047, respectively).

[Motor NP FLA] is multiplied by [Motor OL Factor] to allow the user to define the continuous level of current allowed by the motor thermal

overload. [Motor OL Hertz] is used to allow the user to adjust the frequency below which the motor overload is derated. The motor can operate up to 102% of FLA continuously. If the drive had just been activated, it will run at 150% of FLA for 180 seconds. If the motor had been operating at 100% for over 30 minutes, the drive will run at 150% of FLA for 60 seconds. These values assume the drive is

operating above [Motor OL Hertz], and that [Motor OL Factor] is set to 1.00. Operation below 100% current causes the temperature calculation to account for motor cooling.

Motor Overload Curve Trip Time (Sec) Cold Hot 1000 10000 100000

10 100

<!-- image -->

100 125 150 175 200 225 250

Full Load Amps (%)

[Motor OL Hertz] defines the frequency where motor overload capacity derate should begin. The motor overload capacity is reduced when

operating below [Motor OL Hertz]. For all settings of [Motor OL Hertz]

other than zero, the overload capacity is reduced to 70% at an output frequency of zero.

Changing Overload Hz

80

0 10 20 30 40 50 60 70 80 90 100 Continuous Rating 0 20 40 60

% of Base Speed

<!-- image -->

OL Hz = 10

OL Hz = 25

OL Hz = 50

20B-UM001.book Page 11 Thursday, June 20, 2013 1:55 PM

0 10 20 30 40 50 60 70 80 90 100

% of Base Speed

Overspeed Limit is a user programmable value that allows operation at maximum speed, but also provides an "overspeed band" that will allow a

speed regulator such as encoder feedback or slip compensation to

<!-- image -->

increase the output frequency above maximum speed in order to maintain maximum motor speed.

The figure below illustrates a typical Custom V/Hz profile. Minimum

Speed is entered in Hertz and determines the lower speed reference limit during normal operation. Maximum Speed is entered in Hertz and

determines the upper speed reference limit. The two "Speed" parameters only limit the speed reference and not the output frequency. The actual output frequency at maximum speed reference is the sum of the speed reference plus "speed adder" components from functions such as slip compensation.

The Overspeed Limit is entered in Hertz and added to Maximum Speed and the sum of the two (Speed Limit) limit the output frequency. This sum (Speed Limit) must is compared to Maximum Frequency and an alarm is initiated which prevents operation if the Speed Limit exceeds

Maximum Frequency.

Application Notes

C-11

[Motor NP FLA] is multiplied by [Motor OL Factor] to select the rated current for the motor thermal overload. This can be used to raise or lower

the level of current that will cause the motor thermal overload to trip.

The effective overload factor is a combination of [Motor OL Hertz] and

[Motor OL Factor].

Changing Overload Factor

140

120

100

Continuous Rating 0 20 40 60 80

OL % = 1.20

OL % = 1.00

OL % = 0.80

20B-UM001.book Page 12 Thursday, June 20, 2013 1:55 PM

C-12

Application Notes

Maximum

Voltage

Motor NP

Voltage

Allowable Output Frequency Range -

Bus Regulation or Current Limit

Allowable Output Frequency Range - Normal Operation

(lower limit on this range can be 0 depending on the value of Speed Adder)

Allowable Speed Reference Range

Frequency Trim due to Speed

<!-- image -->

Motor NP Hz

Frequency

Overspeed

Limit

Maximum

Speed

Output

Frequency

Limit

When AC input power is lost, energy is being supplied to the motor from the DC bus capacitors. The energy from the capacitors is not being

replaced (via the AC line), thus, the DC bus voltage will fall rapidly. The drive must detect this fall and react according to the way it is

programmed. Two parameters display DC bus voltage:

·

[DC Bus Voltage] - displays the instantaneous value

·

[DC Bus Memory] - displays a 6 minute running average of the voltage. All drive reactions to power loss are based on [DC Bus Memory]. This averages low and high line conditions and sets the drive to react to the average rather than assumed values. For example, a 480V installation

would have a 480V AC line and produce a nominal 648V DC bus. If the

- drive were to react to a fixed voltage for line loss detect, (i.e. 533V DC),

then normal operation would occur for nominal line installations.

- However, if a lower nominal line voltage of 440V AC was used, then nominal DC bus voltage would be only 594V DC. If the drive were to

react to the fixed 533V level (only –10%) for line loss detect, any anomaly might trigger a false line loss detection. Line loss, therefore always uses the 6 minute average for DC bus voltage and detects line loss based on a fixed percentage of that memory. In the same example, the average would be 594V DC instead of 650V DC and the fixed percentage, 27% for "Coast to Stop" and 18% for all others, would allow identical operation regardless of line voltage.

Maximum

Frequency

20B-UM001.book Page 13 Thursday, June 20, 2013 1:55 PM

Application Notes

C-13

The PowerFlex 70 uses only these fixed percentages. The PowerFlex 700

can selectively use the same percentages or the user can set a trigger point for line loss detect. The adjustable trigger level is set using [Power

Loss Level] (see [Power Loss Level] on page 1-38).

Figure C.4 Power Loss Mode = Coast

Bus Voltage

Motor Speed

Power Loss

Output Enable

<!-- image -->

Power Loss

Output Enable

The internal PI function of the PowerFlex 700 provides closed loop process control with proportional and integral control action. The

function is designed for use in applications that require simple control of a process without external control devices. The PI function allows the

<!-- image -->

microprocessor of the drive to follow a single process control loop.

The PI function reads a process variable input to the drive and compares it to a desired setpoint stored in the drive. The algorithm will then adjust

the output of the PI regulator, changing drive output frequency to try and make the process variable equal the setpoint.

Nominal

73%

Nominal

82%

20B-UM001.book Page 14 Thursday, June 20, 2013 1:55 PM

C-14

Application Notes

It can operate as trim mode by summing the PI loop output with a master speed reference.

Slip Adder

Spd Ref

PI Ref

Drive

Running

Process PI

Controller

PI Enabled PI Fbk

Slip

Comp

Open

Loop

Process

PI

Speed Control

Or, it can operate as control mode by supplying the entire speed reference. This method is identified as "exclusive mode"

Slip

Comp

Open

Loop

Process

PI

Speed Control

<!-- image -->

Controller

PI Enabled PI Fbk

The output of the PI loop can be turned on (enabled) or turned off

(disabled). This control allows the user to determine when the PI loop is providing part or all of the commanded speed. The logic for enabling the

<!-- image -->

Drive

Ramping to Stop

Drive

Jogging

[PI Configuration] A Digital Input is Configured to PI Enable Bit 0 Bit 6

Signal Loss

The Configured

Digital Input is Closed

The drive must be running for the PI loop to be enabled. The loop will be disabled when the drive is ramping to a stop (unless "Stop Mode" is

configured in [PI Configuration]), jogging or the signal loss protection

If a digital input has been configured to "PI Enable," two events are required to enable the loop: the digital input must be closed AND bit 0 of

<!-- image -->

Bit 0 of

[PI Control] = 1

(enabled)

Linear Ramp

&amp; S-Curve

+

+

+

+

+

+

Spd Cmd

Spd Cmd

The PI Loop is Enabled

"Enabled" Status

Digital Input is Reflected

in [PI Status]

Bit 0 = 1

20B-UM001.book Page 15 Thursday, June 20, 2013 1:55 PM

100.0

75.0

50.0

25.0

0.0

-25.0

-50.0

-75.0

-100.0

-100.0 -75.0 -50.0 -25.0 0.0 25.0 50.0 75.0 100.0

Normalized Feedback

PI Kp

PI Neg Limit

PI Pos Limit

+

+

PI Error

PI Ki

Spd Cmd

Application Notes

C-15

If no digital input is configured to "PI Enable," then only the Bit 0 = 1

condition must be met. If the bit is permanently set to a "1", then the loop will become enabled as soon as the drive goes into "run".

PI Enabled

PI Output

Spd Cmd PI Pre-load Value = 0 PI Pre-load Value &gt; 0

PI Enabled

<!-- image -->

PI Pre-load Value

PI XS Error

Preload Value

Spd Cmd

PI\_Config

.PreloadCmd

Spd Cmd

Zclamped

Torq Cmd

*

+

*

PI\_Status

.Hold

PI\_Config

.Exclusive

Current Limit or Volt Limit

PI\_Status

.Enabled

+

z

-1

to

PI Output

In Limit

A

20B-UM001.book Page 16 Thursday, June 20, 2013 1:55 PM

C-16

Application Notes

Reverse Speed Limit

Figure C.6 [Rev Speed Limit], parameter 454 set to zero

10V

–10V

10V

Minimum

Speed ≠ 0

[Maximum

Speed]

Reverse

Speed

<!-- image -->

Speed

<!-- image -->

Reverse

Speed

Limit

–10V

Minimum

Speed = 0

Minimum

Speed ≠ 0

–10V

Figure C.7 [Rev Speed Limit], parameter 454 set to a non-zero Value

10V

Maximum

Speed

Forward

Speed

[Maximum

Speed]

Forward

Speed

[Maximum

Speed]

Forward

Speed

20B-UM001.book Page 17 Thursday, June 20, 2013 1:55 PM

Skip Frequency

Figure C.8 Skip Frequency

Frequency

Command

Frequency

Skip + 1/2 Band

Skip Frequency

Skip – 1/2 Band

<!-- image -->

Time

Some machinery may have a resonant operating frequency that must be avoided to minimize the risk of equipment damage. To assure that the

motor cannot continuously operate at one or more of the points, skip frequencies are used. Parameters 084-086, ([Skip Frequency 1-3]) are

The value programmed into the skip frequency parameters sets the center point for an entire "skip band" of frequencies. The width of the band

(range of frequency around the center point) is determined by parameter

87, [Skip Freq Band]. The range is split, half above and half below the skip frequency parameter. If the commanded frequency of the drive is greater than or equal to the skip (center) frequency and less than or equal to the high value of the band (skip plus 1/2 band), the drive will set the output frequency to the

.

high value of the band. See (A) in Figure C.8 . If the commanded frequency is less than the skip (center) frequency and greater than or equal to the low value of the band (skip minus 1/2 band), the drive will set the output frequency to the low value of the band. See (B) in Figure C.8

Acceleration and deceleration are not affected by the skip frequencies. Normal accel/decel will proceed through the band once the commanded frequency is greater than the skip frequency. See (A) &amp; (B) in Figure

C.8. This function affects only continuous operation within the band.

(A)

(B)

Application Notes

(A)

(B)

35 Hz

30 Hz

25 Hz

C-17

20B-UM001.book Page 18 Thursday, June 20, 2013 1:55 PM

C-18

Application Notes

Skip Frequency Examples

The skip frequency will have hysteresis so the output does not

toggle between high and low values.

Three distinct bands can be programmed. If none of the skip

bands touch or overlap, each band has its own high/low limit.

If skip bands overlap or touch, the

center frequency is recalculated

based on the highest and lowest band

values.

If a skip band(s) extend beyond the

max frequency limits, the highest

band value will be clamped at the

max frequency limit. The center

frequency is recalculated based on

the highest and lowest band values.

If the band is outside the limits, the

skip band is inactive.

0 Hz

Skip Frequency 2

0 Hz

Skip Frequency 2

Skip Frequency 1

400 Hz.

0 Hz

Max.Frequency

Skip

400 Hz.

0 Hz

60 Hz. Max.

Frequency

Skip Frequency 1

400 Hz.

Max. Frequency

Skip Frequency 1

Skip Band 1

Skip Band 2

Adjusted

Skip Band w/Recalculated

Skip Frequency

Adjusted

Skip Band w/Recalculated

Skip Frequency

Inactive

Skip Band

20B-UM001.book Page 19 Thursday, June 20, 2013 1:55 PM

Sleep Wake Mode

This function stops (sleep) and starts (wake) the drive based on separately configurable analog input levels rather than discrete start and

stop signals. When enabled in "Direct" mode, the drive will start (wake)

when an analog signal is greater than or equal to the user specified

[Wake Level], and stop the drive when an analog signal is less than or equal to the user specified [Sleep Level]. When Sleep Wake is enabled

for "Invert" mode(1), the drive will start (wake) when an analog signal is less than or equal to the user specified [Wake Level], and stop the drive

when an analog signal is greater than or equal to the user specified

[Sleep Level]. Definitions · Wake - A start command generated when the analog input value remains above [Wake Level] (or below when Invert mode is active) for a time greater than [Wake Time]. · Sleep - A Stop command generated when the analog input value remains below [Sleep Level] (or above when Invert mode is active) for a time greater than [Sleep Time].

·

Speed Reference – The active speed command to the drive as

- selected by drive logic and [Speed Ref x Sel]. · Start Command - A command generated by pressing the Start button on the HIM, closing a digital input programmed for Start, Run, Run
- Forward or Run Reverse. Refer to Figure C.9 .

(1)

Invert mode is only available with Vector firmware 3.xxx and later.

Application Notes

C-19

20B-UM001.book Page 20 Thursday, June 20, 2013 1:55 PM

C-20

Application Notes

Figure C.9 Sleep Wake Mode

Is Sleep-Wake

Working?

No

Have these conditions been met?

1. [Sleep-Wake Ref] must be set to the analog input that will control

"Start/Stop" functions.

2. [Sleep-Wake Mode] must = "1, Direct" (Enable) or "2, Invert (Enable)."

3. [Sleep Level] must be less than [Wake Level] in Direct mode (or greater than [Wake Level] in "Invert" mode).

4. [Speed Ref x Sel] must be set to a speed reference source that will control the drive. If [Sleep-Wake Ref] = [Speed Ref x Sel], the same

5. At least one of the following must be programmed for [Digital Inx Sel]:

Direct

Is Analog Signal Greater than or equal to [Wake Level]?

and for time period greater than or equal to [Wake Time]

Was a Stop Issued?

or Power Cycled?

Yes

Stop or Enable

Issue a Start Command

(HIM, Network or TB)

Consult Factory

<!-- image -->

No

Meet all Conditions!

Close Input

No

Increase Analog Input

Signal and wait for a time period greater than or

equal to [Wake Time].

Consult Factory

No

20B-UM001.book Page 21 Thursday, June 20, 2013 1:55 PM

Start At PowerUp

Standard Control Option

When Start At Powerup in 2 wire control is configured, the drive will start if the start permissive conditions are met within 10 seconds of drive

power being applied. An alarm will be annunciated from application of power until the drive actually starts, indicating the powerup start attempt

is in progress. If the drive has not started within the 10 second interval, the powerup start attempt will be terminated.

Vector Control Option

A powerup delay time of up to 30 seconds can be programmed through [Powerup Delay], parameter 167. After the time expires, the drive will start if all of the start permissive conditions are met. Before that time, restart is not possible.

Start At PowerUp

10 Second Limit Expired? Standard Control Option Yes No

All Start Permissives Met?

Vector Control Option

[Powerup Delay]

Time Expired?

Yes

All Start Permissives Met?

1. No fault conditions present.

2. No Type 2 alarm conditions present.

3. The terminal block programmed enable input is closed.

4. The Stop input (from all sources) is received.

Yes

Is the terminal block Run,

Run Forward or Run Reverse

Input Closed?

Yes

Powerup Start Powerup Start
Powerup Terminated!

<!-- image -->

Application Notes

No

No

Powerup Terminated!

Normal Mode

No

C-21

20B-UM001.book Page 22 Thursday, June 20, 2013 1:55 PM

C-22

Application Notes

Stop Mode

Mode Description

Coast to

Stop

Output Voltage

Output Current

Motor Speed

Stop

Command

This method releases the motor and allows the load to stop by friction.

1. On Stop, the drive output goes immediately to zero (off).

2. No further power is supplied to the motor. The drive has released control.

3. The motor will coast for a time that is dependent on the mechanics of the system

(inertia, friction, etc).

<!-- image -->

Motor Speed

Coast Time is load dependent

DC

Hold Level

- Stop Command DC Hold Time (B) (C) (A)

This method uses DC injection of the motor to Stop and/or hold the load.

1. On Stop, 3 phase drive output goes to zero (off)

2. Drive outputs DC voltage on the last used phase at the level programmed in [DC Brake

Level] Par 158. This voltage causes a "stopping" brake torque. If the voltage is applied for a time that is longer than the actual possible stopping time, the remaining time will

be used to attempt to hold the motor at zero speed.

3. DC voltage to the motor continues for the amount of time programmed in [DC Brake

Time] Par 159. Braking ceases after this time expires.

4. After the DC Braking ceases, no further power is supplied to the motor. The motor may

<!-- image -->

or may not be stopped. The drive has released control.

5. The motor, if rotating, will coast from its present speed for a time that is dependent on the mechanics of the system (inertia, friction, etc).

Time

Time

20B-UM001.book Page 23 Thursday, June 20, 2013 1:55 PM

Mode Description

Ramp to

Stop

Output Voltage

Output Current

Motor Speed

Stop

Command

<!-- image -->

Zero

Command

Speed

This method uses drive output reduction to stop the load.

1. On Stop, drive output will decrease according to the programmed pattern from its present value to zero. The pattern may be linear or squared. The output will decrease

to zero at the rate determined by the programmed [Maximum Freq] and the programmed active [Decel Time x].

2. The reduction in output can be limited by other drive factors such as such as bus or current regulation.

3. When the output reaches zero the output is shut off.

4. The motor, if rotating, will coast from its present speed for a time that is dependent on the mechanics of the system (inertia, friction, etc).

- Ramp to Hold Output Voltage Output Current Motor Speed
- Output Voltage Output Current

Output Current

Output Voltage

DC Hold Time

Time

Application Notes

Output Voltage

Output Current

Motor Speed

DC

Hold Level

- Re-issuing a Start Command Stop Command Zero Command Speed

This method combines two of the methods above. It uses drive output reduction to stop the load and DC injection to hold the load at zero speed once it has stopped.

1. On Stop, drive output will decrease according to the programmed pattern from its present value to zero. The pattern may be linear or squared. The output will decrease

to zero at the rate determined by the programmed [Maximum Freq] and the programmed active [Decel Time x]

2. The reduction in output can be limited by other drive factors such as bus or current

3. When the output reaches zero 3 phase drive output goes to zero (off) and the drive

<!-- image -->

outputs DC voltage on the last used phase at the level programmed in [DC Brake

Level] Par 158. This voltage causes a "holding" brake torque. 4. DC voltage to the motor continues until a Start command is reissued or the drive is

- disabled. 5. If a Start command is reissued, DC Braking ceases and he drive returns to normal AC operation. If an Enable command is removed, the drive enters a "not ready" state until the enable is restored.

Time

C-23

20B-UM001.book Page 24 Thursday, June 20, 2013 1:55 PM

C-24

Application Notes

Voltage Tolerance

Nominal Line

Drive Rating

Voltage

Nominal Motor

Voltage

Drive Full Power

Range

Drive Operating

Range

200-240 200 200* 200-264 180-264

208 208 208-264

240 230 230-264

380-400 380 380* 380-528 342-528

400 400 400-528

480 460 460-528

600 575* 575-660 432-660

600 575* 575-660 475-759

690 690 690-759 475-759

Drive Full Power Range = Nominal Motor Voltage to Drive Rated Voltage +10%.

Rated power is available across the entire Drive Full Power Range.

Drive Operating Range = Lowest (*) Nominal Motor Voltage –10% to Drive Rated Voltage +10%.

Drive Output is linearly derated when Actual Line Voltage is less than

Derated Power Range

Full Power Range

Drive Operating Range

Drive Rated Voltage

Drive Rated Voltage +10%

500-600

(Frames 0-4 Only)

| 500-690 (Frames 5-6 Only)   |                            |                            |
|-----------------------------|----------------------------|----------------------------|
| HP @ Motor (Drive Output)   | HP @ Motor (Drive Output)  | HP @ Motor (Drive Output)  |
| Nominal Motor Voltage -10%  | Nominal Motor Voltage -10% | Nominal Motor Voltage -10% |

Nominal Motor Voltage

Actual Line Voltage (Drive Input)

Calculate the maximum power of a 5 HP, 460V motor connected to a 480V rated drive

Actual Line Voltage / Nominal Motor Voltage = 74.3%

At 342V Actual Line Voltage, the maximum power the 5 HP, 460V motor can produce is

3.7 HP at 44.6 Hz.

<!-- image -->

5 HP

3.7 HP HP @ Motor (Drive Output)

342V

460V

Actual Line Voltage (Drive Input)

<!-- image -->

480V

528V

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

Numerics

32 Bit Parameters

A

Accel Mask

,

Accel Owner

1-52

,

1-53

Accel Time x

,

1-31

Alarm &amp; Fault Types

,

2-1

| Alarm 1 @ Fault ,  1-45                           |
|---------------------------------------------------|
| Alarm 2 @ Fault ,  1-46 Alarm Clear ,  1-48       |
| Alarm Config 1 ,  1-48 Alarm Descriptions ,  2-10 |
| Alarm x Code ,  1-48                              |
| Analog In Loss ,  2-10                            |
| Bipolar Conflict ,  2-10                          |
| Brake Slipped ,  2-10                             |
| Decel Inhibt ,  2-10 2-10                         |
| Dig In Conflict ,  Drive OL Level 2-10            |
| ,  FluxAmpsRef Rang 2-11                          |
| ,  Ground Warn ,  2-11                            |
| In Phase Loss ,  2-11                             |
| IntDBRes OvrHeat ,  2-11                          |
| IR Volts Range ,  2-11                            |
| Ixo Vlt Rang ,  2-11                              |
| Load Loss ,  2-11                                 |
| MaxFreq Conflict ,  2-11 Motor Thermistor 2-11    |
| ,                                                 |
| Motor Type Cflct ,  2-11                          |
| NP Hz Conflict ,  2-11                            |
| Power Loss ,  2-11                                |
| Precharge Active ,  2-11 PTC Conflict 2-11        |
| ,  2-11                                           |
| Sleep Config ,                                    |
| Speed Ref Cflct ,  2-11 Start At PowerUp ,  2-11  |
| ,  Torq Prove Cflct ,  2-12                       |
| TB Man Ref Cflct 2-12                             |
| UnderVoltage ,  2-12 VHz Neg Slope ,  2-12        |
| Alarms, Clearing ,  2-9 ALT Key Functions B-2     |
| ,  ALT Key Functions ,  B-2                       |

,

1-2

Analog In Loss Alarm

Analog In Loss Fault

Analog In x Hi

,

1-55

Analog In x Lo

,

1-55

Analog Inputs Group

,

1-54

Analog Inx Value

,

1-13

Analog Out Scale

,

1-57

Analog Out1 Hi

,

1-56

Analog Out1 Lo

,

Analog Out1 Sel

Analog Out2 Lo

,

1-56

,

1-56

1-56

Analog Out2 Sel

,

1-56

Analog Outputs Group

,

Anlg Cal Chksum Fault

Anlg In Config

,

1-54

Anlg In Loss

,

1-55

Anlg In Sqr Root

,

1-54

Anlg Out Absolut

Anlg Out Config

,

1-55

,

1-55

Anlg Out Setpt

,

1-57

Applications File

,

1-60

Auto Rstrt Delay

,

1-35

Auto Rstrt Tries

,

1-35

Auto Rstrt Tries Fault

,

Auto-Reset/Start

,

2-1

Autotune

,

1-17

AutoTune Aborted Fault

,

2-4

Autotune Torque

,

1-18

Auxiliary Input Fault

,

2-4

B

Bipolar Conflict Alarm

,

2-10

Brake

Dynamic

,

1-33

Brake Slipped Alarm

,

2-10

Break Frequency

,

1-20

Break Voltage

,

1-20

Brk Alarm Travel

,

1-61

Brk Release Time

,

Brk Set Time

,

1-61

1-61

BrkSlip Count

,

1-61

Bus Capacitors, Discharging

Bus Reg Kd

,

1-34

Bus Reg Ki

,

1-33

Bus Reg Kp

,

1-34

Bus Reg Mode A

,

2-4

,

,

2-10

2-4

1-33

,

1-55

2-4

,

Index

P-3

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

Index-2

Bus Reg Mode B

C

Capacitors

Bus, Discharging

,

P-3

Catalog Number Explanation

Clear Fault Owner

,

Clearing Alarms

Clearing Faults

,

1-53

2-9

2-3

| ,  Cntl Bd Overtemp Fault ,  2-4                  |
|---------------------------------------------------|
| Comm Control Group ,  1-50 Commanded Freq ,  1-12 |
| Commanded Speed 1-12                              |
| ,  Commanded Torque 1-13                          |
| ,  Common Symptoms and Corrective                 |
| Action ,  2-13                                    |
| Communication File ,  1-50                        |
| Communications                                    |
| Logic Command Word ,  A-3                         |
| Logic Status Word ,  A-4                          |
| Programmable Controller                           |
| Configurations ,  A-2                             |
| Compensation ,  1-16                              |
| Control Options ,  1-3                            |
| Control Status ,  1-19                            |
| Control SW Ver ,  1-14                            |
| Conventions, Manual ,  P-2                        |
| Copycat ,  B-4                                    |
| Cross Reference, Parameter                        |
| by Name ,  1-61                                   |
| by Number ,  1-64                                 |
| Current Lmt Gain ,  1-31 Current Lmt Sel ,  1-31  |
| Current Lmt Val ,  1-31                           |
| Current Rate Limit ,  1-32                        |
| Data In Ax ,  1-53                                |
| Data Out Ax ,  1-54                               |
| Data, Saving ,  B-4                               |
| Datalinks Group ,  1-53                           |
| DB Resistance Fault ,  2-4                        |
| DB Resistor Type ,  1-34                          |
| DB While Stopped ,  1-32                          |
| DC Brake Level ,  1-33 DC Brake Time ,  1-33      |
| DC Brk Levl Sel ,  1-32                           |
| DC Bus Memory ,  1-13                             |

,

1-33

,

P-5

DC Bus Voltage

,

1-13

Decel Inhibit Fault

,

2-5

Decel Inhibt Alarm

Decel Mask

,

1-52

Decel Owner

,

1-53

Decel Time x

,

1-31

Defaults, Resetting to

,

1-40

Diagnostic Data, Viewing

,

B-4

,

Diagnostics Group

,

1-41

Dig In Conflict Alarm

,

2-10

Dig In Status

,

1-44

Dig Out Setpt

,

1-59

Dig Out Status

,

1-44

Dig Outx Level

,

1-59

Dig Outx OffTime

,

1-60

Dig Outx OnTime

,

1-60

Digital Inputs Group

,

1-58

Digital Inx Sel

,

1-58

Digital Outputs Group

,

1-58

Digital Outx Sel

,

1-59

Direction Config Group

Direction Mask

,

1-52

Direction Mode

,

1-38

Direction Owner

,

1-53

Discrete Speeds Group

DPI Baud Rate

,

1-50

DPI Data Rate

,

1-50

DPI Fdbk Select

1-51

,

DPI Port 1-5 Fault

,

2-7

DPI Port Locations

DPI Port Sel

,

1-51

DPI Port Value

,

1-51

DPI Ref Select

Drive Alarm 1

,

,

1-51

1-42

Drive Alarm 2

,

1-42

Drive Checksum

,

1-41

Drive Data Group

Drive Frame Size

,

1-14

,

A-1

Drive Logic Rslt

,

1-50

Drive Memory Group

,

Drive OL Count

,

1-44

Drive OL Level Alarm

Drive OL Mode

,

1-31

Drive Overload Fault

,

Drive Powerup Fault

,

1-39

2-10

2-5

2-5

Drive Ramp Rslt

,

,

1-50

Drive Ref Rslt

,

1-50

Drive Status 1

,

1-41

Drive Temp

,

1-44

,

B-1

B-4

,

2-10

,

,

1-38

1-25

20B-UM001.book Page 3 Thursday, June 20, 2013 1:55 PM

Index-3

DriveExecutive

,

1-1

DriveExplorer

,

1-1

Droop RPM @ FLA

,

Dynamic Brake

Resistor Selection

1-32

,

Setup

,

1-33

Dynamic Control File

E

| Editing Parameters ,  1-1                         |
|---------------------------------------------------|
| Elapsed kWh 1-13                                  |
| ,  Elapsed MWH 1-12                               |
| ,  Elapsed Run Time 1-12                          |
| ,  Enc Position Fdbk ,  1-20                      |
| Encoder Loss Fault ,  2-5 Encoder PPR ,  1-20 2-5 |
| Encoder Quad Err Fault ,  Encoder Speed ,  1-20   |
| Encoder Z Chan ,  1-21                            |
| ESD, Static Discharge ,  P-3                      |
| Excessive Load Fault ,  2-5                       |
| External Brake Resistor ,  C-1                    |
| Factory Defaults, Resetting to 1-40               |
| ,                                                 |
| 1-39                                              |
| Fan/Pump Parameter Set ,                          |
| Fault & Alarm Types ,  2-1                        |
| Fault 1 Time ,  1-48                              |
| Fault Amps ,  1-44 Fault Bus Volts ,  1-45        |
| Fault Clear ,  1-46 Fault Clear Mode ,  1-47      |
| Fault Clr Mask ,  1-52 ,  1-46                    |
| Fault Config x Fault Descriptions ,  2-4          |
| Fault Frequency ,  1-44                           |
| Fault Queue ,  B-4                                |
| Fault Speed ,  1-44                               |
| Fault x Code ,  1-47                              |
| Analog In Loss ,  2-4                             |
| Anlg Cal Chksum ,  2-4                            |
| Auto Rstrt Tries ,  2-4                           |
| AutoTune Aborted ,  2-4                           |
| Auxiliary Input ,  2-4 Cntl Bd Overtemp 2-4       |
| ,  DB Resistance 2-4                              |
| ,  Decel Inhibit ,  2-5                           |

1-34

,

1-31

DPI Port 1-5

,

2-7

Drive Overload

,

2-5

Drive Powerup

,

2-5

Encoder Loss

,

2-5

Encoder Quad Err

,

2-5

Excessive Load

,

2-5

Faults Cleared

,

2-5

Flt QueueCleared

,

2-5

FluxAmpsRef Rang

,

2-5

Ground Fault

,

2-5

Hardware Fault

,

2-5

Heatsink OvrTemp

,

2-5

HW OverCurrent

,

I/O Comm Loss

,

I/O Failure

,

2-6

I/O Mismatch

,

2-6

Incompat MCB-PB

Input Phase Loss

,

2-6

,

2-6

IR Volts Range

,

2-6

IXo VoltageRange

,

2-6

Load Loss

,

2-6

Motor Overload

,

2-6

Motor Thermistor

,

2-6

NVS I/O Checksum

,

2-6

NVS I/O Failure

,

2-6

Output PhaseLoss

,

2-7

OverSpeed Limit

,

2-7

OverVoltage

2-7

,

Parameter Chksum

,

2-7

Params Defaulted

,

Phase Short

,

2-7

Phase to Grnd

,

2-7

Port 1-5 DPI Loss

,

2-7

Power Loss

,

2-8

Power Unit

,

2-8

Pulse In Loss

,

2-8

Pwr Brd Chksum

,

2-8

Pwr Brd Chksum2

,

2-8

Replaced MCB-PB

,

2-8

Shear Pin

,

2-8

Software

,

2-8

SW OverCurrent

,

2-8

TorqPrv Spd Band

,

2-8

Trnsistr OvrTemp

,

UnderVoltage

,

2-9

UserSet Chksum

,

Faults Cleared Fault

Faults Group

,

1-46

Faults, Clearing

,

2-3

Fdbk Filter Sel

,

1-20

Feedback Select

,

1-22

FGP

,

1-3

File

,

2-8

2-9

2-5

2-7

2-6

2-6

20B-UM001.book Page 4 Thursday, June 20, 2013 1:55 PM

Index-4

Applications

,

1-60

Communication

,

1-50

Dynamic Control

Inputs &amp; Outputs

,

1-31

,

1-54

Monitor

,

1-12

Motor Control

,

1-14

Speed Command

,

1-21

Utility

,

1-38

File-Group-Parameter

Float Tolerance

1-61

,

1-3

| ,  Flt QueueCleared Fault 2-5           |
|-----------------------------------------|
| ,  Flux Braking 1-34                    |
| ,  Flux Current 1-12                    |
| ,                                       |
| Flux Current Ref ,  1-17                |
| Flux Up Mode ,  1-16                    |
| Flux Up Time ,  1-16                    |
| Flux Vector Control Option ,  1-3       |
| FluxAmpsRef Rang Alarm ,  2-11          |
| FluxAmpsRef Rang Fault ,  2-5           |
| Flying Start En ,  1-35                 |
| Flying StartGain ,  1-35                |
| Frame Size, Drive ,  A-1                |
| Functions, ALT Key ,  B-2               |
| General Precautions ,  P-3              |
| Gnd Warn Level 1-37                     |
| ,  Ground Fault 2-5                     |
| ,  Ground Warn Alarm 2-11               |
| ,                                       |
| Alarms 1-48                             |
| ,  Analog Inputs ,  1-54                |
| Comm Control ,  1-50 Datalinks          |
| ,  1-53                                 |
| Diagnostics ,  1-41 Digital Inputs 1-58 |
| ,  Digital Outputs 1-58                 |
| ,  Direction Config 1-38                |
| ,  Discrete Speeds ,  1-25              |
| Drive Data ,  1-14                      |
| Drive Memory ,  1-39                    |
| Faults ,  1-46                          |
| HIM Ref Config ,  1-39                  |
| Load Limits ,  1-31 Masks & Owners 1-51 |
| ,  Metering 1-12                        |
| ,  MOP Config 1-39                      |
| ,  Motor Data 1-14                      |
| ,  Power Loss 1-37                      |
| ,  Process PI ,  1-27                   |

Ramp Rates

,

1-31

Restart Modes

,

1-34

Scaled Blocks

,

1-49

Slip Comp

,

1-26

Spd Mode &amp; Limits

,

1-21

Speed Feedback

,

1-20

Speed References

,

1-24

Speed Regulator

,

Speed Trim

,

1-26

Stop/Brake Modes

,

1-32

Torq Attributes

,

Volts per Hertz

1-15

,

1-19

H

Hardware Fault

,

2-5

Heatsink OvrTemp Fault

,

HIM Menu Structure

HIM Menus

Diagnostics

,

B-4

Memory Storage

,

,

B-4

B-4

Preferences

,

B-4

HIM Ref Config Group

,

1-39

HIM, Removing/Installing

,

B-8

HW OverCurrent Fault

I

I/O Comm Loss Fault

I/O Failure Fault

,

2-6

I/O Mismatch Fault

,

2-6

In Phase Loss Alarm

,

2-11

Incompat MCB-PB Fault

,

2-6

Inertia Autotune

,

1-18

Input Phase Loss Fault

,

2-6

Inputs &amp; Outputs File

,

1-54

IntDBRes OvrHeat Alarm

,

2-11

IR Voltage Drop

,

1-17

IR Volts Range Alarm

,

IR Volts Range Fault

2-11

2-6

Ixo Vlt Rang Alarm

,

,

2-11

Ixo Voltage Drop

,

1-17

IXo VoltageRange Fault

J

Jog Mask

,

Jog Owner

Jog Speed

1-52

,

1-52

,

1-25

,

2-6

,

2-6

1-29

2-5

,

2-6

20B-UM001.book Page 5 Thursday, June 20, 2013 1:55 PM

Index-5

K

Kf Speed Loop

,

Ki Speed Loop

,

Kp Speed Loop

,

L

Language

,

1-40

Last Stop Source

,

1-43

| LCD HIM                                                     |
|-------------------------------------------------------------|
| Menus ,  B-4                                                |
| LEDs ,  2-2                                                 |
| Lifting/Torque Proving ,  C-2 Linear List ,  1-3            |
| Linking Parameters ,  B-6 ,  1-2 ,  1-40                    |
| Load Frm Usr Set                                            |
| Load Limits Group ,  1-31                                   |
| Load Loss Alarm ,  2-11                                     |
| Load Loss Fault ,  2-6                                      |
| Load Loss Level ,  1-38                                     |
| Load Loss Time ,  1-38                                      |
| Local Mask ,  1-52                                          |
| Local Owner ,  1-53                                         |
| Logic Command Word ,  A-3                                   |
| Logic Mask ,  1-51                                          |
| Logic Status Word ,  A-4                                    |
| Man Ref Preload 1-39                                        |
| ,  Manual Conventions P-2                                   |
| ,  Marker Pulse ,  1-21                                     |
| Masks & Owners Group ,  1-51 MaxFreq Conflict Alarm ,  2-11 |
| Maximum Freq ,  1-16                                        |
| Maximum Speed ,  1-22                                       |
| Maximum Voltage ,  1-15                                     |
| Menu Structure, HIM ,  B-4 Metering Group ,  1-12           |
| MicroPos Scale% ,  1-61                                     |
| Minimum Speed ,  1-22 ,  C-7                                |
| MOD LED ,  2-2                                              |
| Monitor File ,  1-12                                        |
| MOP Frequency ,  1-13                                       |
| MOP Mask ,  1-52                                            |
| MOP Owner 1-53                                              |
| ,  MOP Rate 1-39                                            |
| ,  MOP Reference 1-13                                       |
| ,                                                           |

1-30

1-29

1-30

Motor Cntl Sel

,

1-15

Motor Control File

,

1-14

Motor Control Technology

Motor Data Group

,

Motor Fdbk Type

1-14

,

1-20

Motor NP FLA

,

1-14

Motor NP Hertz

,

1-14

Motor NP Power

Motor NP RPM

,

Motor NP Volts

,

,

1-15

1-14

1-14

Motor OL Count

,

1-44

Motor OL Factor

Motor OL Hertz

,

1-15

1-15

Motor Overload

,

C-10

Motor Overload Fault

,

2-6

Motor Poles

,

1-15

Motor Thermistor Alarm

,

2-11

Motor Thermistor Fault

Motor Type

,

1-14

Motor Type Cflct Alarm

,

Mtr NP Pwr Units

,

1-15

Mtr Tor Cur Ref

,

1-19

N

Neg Torque Limit

,

1-19

NET LED

,

2-2

Non-Resettable

,

Notch Filter Freq

2-1

,

1-20

Notch Filter K

,

1-21

NP Hz Conflict Alarm

,

2-11

NVS I/O Checksum Fault

,

2-6

NVS I/O Failure Fault

O

Operator Interface

,

B-5

Output Current

,

1-12

Output Freq

,

1-12

Output PhaseLoss Fault

,

2-7

Output Power

,

1-12

Output Powr Fctr

,

1-12

Output Voltage

,

1-12

Overspeed

,

C-11

Overspeed Limit

,

1-22

OverSpeed Limit Fault

,

OverVoltage Fault

,

2-7

2-6

,

,

2-6

2-11

,

,

2-7

C-8

20B-UM001.book Page 6 Thursday, June 20, 2013 1:55 PM

Index-6

P

Param Access Lvl

,

Parameter

Changing/Editing

1-39

,

B-5

Descriptions

,

1-1

File-Group-Parameter Organization

1-3

Linear List

Viewing

,

,

1-3

B-5

| Parameter Chksum Fault ,  2-7                  |
|------------------------------------------------|
| Parameter Cross Reference 1-61                 |
| by Name ,  by Number ,  1-64                   |
| Parameter Linking B-6                          |
| ,  Parameter View                              |
| Advanced                                       |
| Standard Control 1-6                           |
| ,  Fan/Pump ,  1-11                            |
| Vector Control 1-8                             |
| ,                                              |
| Standard Control 1-4                           |
| ,  Fan/Pump 1-10                               |
| ,  Vector Control 1-5                          |
| ,  Parameters                                  |
| Accel Mask 1-52                                |
| ,  Accel Owner ,  1-53                         |
| Accel Time x ,  1-31                           |
| Alarm 1 @ Fault ,  1-45 Alarm 2 @ Fault 1-46   |
| ,                                              |
| ,  Alarm Config 1 ,  1-48                      |
| Alarm Clear 1-48                               |
| Alarm x Code ,  1-48 Analog In x Hi 1-55       |
| ,                                              |
| Analog In x Lo ,  1-55                         |
| Analog Inx Value ,  1-13 Analog Out Scale 1-57 |
| ,  Analog Out1 Hi 1-56                         |
| ,  Analog Out1 Lo 1-56                         |
| ,  Analog Out1 Sel ,  1-56                     |
| Analog Out2 Hi ,  1-56                         |
| Analog Out2 Lo 1-56                            |
| ,  Analog Out2 Sel 1-56                        |
| ,  Anlg In Config 1-54                         |
| ,  Anlg In Loss 1-55                           |
| ,  Anlg In Sqr Root ,  1-54                    |
| Anlg Out Absolut ,  1-55                       |
| Anlg Out Config ,  1-55                        |
| Anlg Out Setpt ,  1-57                         |
| Auto Rstrt Delay ,  1-35                       |
| Auto Rstrt Tries ,  1-35                       |
| Autotune 1-17                                  |
| ,  Autotune Torque 1-18                        |
| ,                                              |

,

Break Frequency

,

1-20

Break Voltage

,

1-20

Brk Alarm Travel

,

1-61

Brk Release Time

,

Brk Set Time

,

BrkSlip Count

1-61

1-61

,

1-61

Bus Reg Kd

,

Bus Reg Ki

,

1-34

1-33

Bus Reg Kp

,

1-34

Bus Reg Mode A

,

Bus Reg Mode B

,

Clear Fault Owner

1-33

1-33

,

1-53

Commanded Freq

,

1-12

Commanded Speed

,

1-12

Commanded Torque

Compensation

,

1-16

Control Status

,

1-19

Control SW Ver

,

1-14

Current Lmt Gain

,

1-31

Current Lmt Sel

,

1-31

Current Lmt Val

,

1-31

Current Rate Limit

,

1-32

Data In Ax

,

1-53

Data Out Ax

,

1-54

DB Resistor Type

,

DB While Stopped

1-34

,

1-32

DC Brake Level

,

1-33

DC Brake Time

,

DC Brk Levl Sel

,

DC Bus Memory

DC Bus Voltage

1-33

1-32

,

1-13

,

1-13

Decel Mask

,

Decel Owner

Decel Time x

1-52

,

1-53

,

Dig In Status

,

1-31

1-44

Dig Out Setpt

,

1-59

Dig Out Status

,

1-44

Dig Outx Level

,

1-59

Dig Outx OffTime

,

1-60

Dig Outx OnTime

,

1-60

Digital Inx Sel

,

1-58

Digital Outx Sel

,

1-59

Direction Mask

,

Direction Mode

,

Direction Owner

DPI Baud Rate

,

1-52

1-38

,

1-53

1-50

DPI Data Rate

,

1-50

DPI Fdbk Select

,

1-51

DPI Port Sel

,

1-51

DPI Port Value

,

1-51

DPI Ref Select

Drive Alarm 1

,

,

1-51

1-42

Drive Alarm 2

,

1-42

Drive Checksum

,

1-41

,

1-13

20B-UM001.book Page 7 Thursday, June 20, 2013 1:55 PM

Index-7

Drive Logic Rslt

Drive OL Count

,

Drive OL Mode

,

Drive Ramp Rslt

1-50

1-44

1-31

,

1-50

Drive Ref Rslt

,

Drive Status 1

1-50

,

1-41

Drive Temp

,

1-44

Droop RPM @ FLA

Elapsed kWh

,

1-13

Elapsed MWH

,

1-12

| Elapsed Run Time ,  1-12 Enc Position Fdbk ,  1-20 Encoder PPR ,  1-20 Encoder Speed ,  1-20 Encoder Z Chan ,  1-21 Fault 1 Time ,  1-48 Fault Amps ,  1-44 Fault Bus Volts ,  1-45 Fault Clear ,  1-46 Fault Clear Mode ,  1-47 Fault Clr Mask ,  1-52 Fault Config x ,  1-46 Fault Frequency ,  1-44 Fault Speed ,  1-44 Fault x Code ,  1-47 Fdbk Filter Sel ,  1-20 Feedback Select ,  1-22 Float Tolerance ,  1-61 Flux Braking ,  1-34 Flux Current ,  1-12 Flux Current Ref ,  1-17 Flux Up Mode ,  1-16 Flux Up Time ,  1-16 Flying Start En ,  1-35 Flying StartGain ,  1-35 Gnd Warn Level ,  1-37 Inertia Autotune ,  1-18 IR Voltage Drop ,  1-17 Ixo Voltage Drop ,  1-17 Jog Mask ,  1-52 Jog Owner ,  1-52 Jog Speed ,  1-25 Kf Speed Loop ,  1-30   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

,

,

1-32

Marker Pulse

,

1-21

Maximum Freq

,

1-16

Maximum Speed

,

1-22

Maximum Voltage

MicroPos Scale%

Minimum Speed

,

MOP Frequency

,

MOP Mask

,

MOP Owner

1-52

,

1-53

MOP Rate

,

1-39

MOP Reference

,

1-13

Motor Cntl Sel

,

1-15

Motor Fdbk Type

,

1-20

Motor NP FLA

,

1-14

Motor NP Hertz

,

1-14

Motor NP Power

Motor NP RPM

,

Motor NP Volts

,

,

1-15

1-14

1-14

Motor OL Count

,

1-44

Motor OL Factor

Motor OL Hertz

,

1-15

,

1-15

Motor Poles

,

1-15

Motor Type

,

1-14

Mtr NP Pwr Units

,

1-15

Mtr Tor Cur Ref

,

1-19

Neg Torque Limit

,

1-19

Notch Filter Freq

,

1-20

Notch Filter K

,

Output Current

1-21

,

1-12

Output Freq

,

1-12

Output Power

,

1-12

Output Powr Fctr

,

1-12

Output Voltage

,

1-12

Overspeed Limit

,

1-22

Param Access Lvl

PI BW Filter

,

,

1-39

1-29

PI Configuration

,

1-27

PI Control

,

1-27

PI Deriv Time

,

1-29

PI Error Meter

,

1-29

PI Fdback Meter

,

1-28

PI Feedback Hi

,

PI Feedback Lo

,

PI Feedback Sel

PI Integral Time

1-29

1-29

,

1-28

,

1-28

PI Lower Limit

,

1-28

PI Output Meter

,

1-29

PI Preload

,

1-28

PI Prop Gain

,

1-28

PI Ref Meter

,

1-28

PI Reference Hi

,

1-29

PI Reference Lo

,

PI Reference Sel

PI Setpoint

,

1-27

1-29

,

1-27

,

1-15

,

1-61

1-22

1-13

20B-UM001.book Page 8 Thursday, June 20, 2013 1:55 PM

Index-8

PI Status

,

1-28

PI Upper Limit

,

1-28

Pos Torque Limit

,

1-19

Power Loss Level

,

Power Loss Mode

Power Loss Time

1-38

,

1-37

,

1-37

Powerup Delay

,

1-34

PowerUp Marker

,

1-47

Preset Speed x

,

Pulse In Scale

1-25

1-21

| Pulse Input Ref ,  1-25                 |
|-----------------------------------------|
| PWM Frequency ,  1-31                   |
| Ramped Speed ,  1-13                    |
| Rated Amps ,  1-14                      |
| Rated kW ,  1-14                        |
| Rated Volts ,  1-14                     |
| Reference Mask ,  1-52                  |
| Reference Owner ,  1-53                 |
| Regen Power Limit ,  1-32               |
| Reset Meters ,  1-40                    |
| Reset To Defalts ,  1-40                |
| Rev Speed Limit ,  1-23                 |
| Run Boost ,  1-19                       |
| S Curve % ,  1-31                       |
| Save HIM Ref ,  1-39                    |
| Save MOP Ref ,  1-39                    |
| Save To User Set ,  1-40                |
| Scale In Hi ,  1-49                     |
| Scale In Lo ,  1-49                     |
| Scale In Value ,  1-49                  |
| Scale Out Hi ,  1-49                    |
| Scale Out Lo ,  1-49                    |
| ,  1-38                                 |
| Shear Pin Time                          |
| Skip Freq Band ,  1-23 1-23             |
| Skip Frequency x ,  Sleep Level ,  1-37 |
| Sleep Time ,  1-37                      |
| Sleep-Wake Mode ,  1-36                 |
| Sleep-Wake Ref ,  1-37                  |
| Slip Comp Gain ,  1-26                  |
| Slip RPM @ FLA ,  1-26                  |
| Slip RPM Meter ,  1-26                  |
| SpdBand Integrat ,  1-61                |
| Speed Desired BW ,  1-30                |
| Speed Dev Band ,  1-61                  |
| Speed Feedback ,  1-13                  |
| Speed Loop Meter ,  1-30                |
| Speed Mode ,  1-22                      |
| Speed Ref A Hi ,  1-24                  |
| Speed Ref A Lo ,  1-24                  |
| Speed Ref A Sel ,  1-24                 |
| Speed Ref B Hi ,  1-24                  |
| Speed Ref B Lo ,  1-24                  |

,

Speed Ref B Sel

,

1-24

Speed Ref Source

,

1-43

Speed Reference

,

Speed Units

,

1-21

Speed/Torque Mod

,

1-23

Start At PowerUp

,

Start Inhibits

,

1-43

Start Mask

,

1-51

Start Owner

,

1-52

Start/Acc Boost

,

1-19

Status 1 @ Fault

,

1-45

Stop Mode x

,

1-32

Stop Owner

,

1-52

Stop/BRK Mode x

,

1-32

SV Boost Filter

,

TB Man Ref Hi

,

TB Man Ref Lo

,

TB Man Ref Sel

Testpoint 1 Sel

,

Testpoint x Data

1-16

1-25

1-25

,

1-25

1-46

,

1-46

Torq Ref A Div

,

1-18

TorqLim SlewRate

,

1-61

TorqProve Cnfg

,

TorqProve Setup

1-60

,

1-60

Torque Current

,

1-12

Torque Perf Mode

,

1-15

Torque Ref B Mult

,

1-2

Torque Ref x Hi

,

Torque Ref x Lo

,

Torque Ref x Sel

,

1-18

1-18

,

Torque Setpoint

,

Torque Setpoint2

1-18

1-19

,

Total Inertia

,

1-19

1-30

Trim % Setpoint

,

1-26

Trim Hi

,

1-26

Trim In Select

,

1-26

Trim Lo

,

1-26

Trim Out Select

,

1-26

Voltage Class

,

1-41

Wake Level

,

1-37

Wake Time

,

1-37

Zero SpdFloatTime

,

1-61

Params Defaulted Fault

,

2-7

Phase Short Fault

,

2-7

Phase to Grnd Fault

,

2-7

PI BW Filter

,

1-29

PI Configuration

,

1-27

PI Control

,

1-27

PI Deriv Time

,

1-29

PI Error Meter

,

1-29

PI Fdback Meter

,

1-28

PI Feedback Hi

,

1-29

1-34

1-13

1-18

20B-UM001.book Page 9 Thursday, June 20, 2013 1:55 PM

Index-9

PI Feedback Lo

,

PI Feedback Sel

PI Integral Time

,

1-29

1-28

,

1-28

PI Lower Limit

,

1-28

PI Output Meter

,

1-29

PI Preload

,

1-28

PI Prop Gain

,

1-28

PI Ref Meter

,

1-28

PI Reference Hi

,

1-29

PI Reference Lo

,

1-29

PI Reference Sel

PI Setpoint

, 1-27 1-27

PI Status

, 1-28

PI Upper Limit

, Port 1-5 DPI Loss Fault

, 1-28

PORT LED

, 2-2

Ports, DPI Type

, B-1

Pos Torque Limit

, 1-19

, Power Loss Fault 2-8

, Power Loss Alarm 2-11

, Power Loss Group 1-37

, Power Loss Mode 1-37

, Power Loss Level 1-38

, C-12

, Power Unit Fault 2-8

Power Loss Ride Through , Power Loss Time 1-37

,

, Powerup Delay 1-34

PowerUp Marker

,

1-47

Precautions, General

,

P-3

Precharge Active Alarm ,

2-11

Preferences, Setting , B-4

Preset Speed x , 1-25

Process PI

Standard Control , C-13

Process PI Group , 1-27

Programmable Controller

Configurations , A-2

Programming , 1-1

PTC Conflict Alarm , 2-11

Publications, Reference , P-2

Pulse In Loss Fault , 2-8

Pulse In Scale , 1-21

Pulse Input Ref , 1-25

PWM Frequency , 1-31

Pwr Brd Chksum Fault , 2-8

Pwr Brd Chksum2 , 2-8

PWR LED

, 2-2

2-7

R

Ramp Rates Group

,

1-31

Ramped Speed

,

1-13

Rated Amps

,

1-14

Rated kW

,

1-14

Rated Volts

,

1-14

Reference Mask

,

1-52

Reference Material

,

P-2

Reference Owner

,

1-53

Regen Power Limit

,

1-32

Replaced MCB-PB Fault

,

Reset Meters

,

1-40

Reset to Defaults

,

1-40

Restart Modes Group

,

B-4

,

Rev Speed Limit

,

1-23

Reverse Speed Limit

,

C-16

Run Boost

,

1-19

S

S Curve %

,

1-31

Save HIM Ref

,

1-39

Save MOP Ref

,

1-39

Save To User Set

,

1-40

Saving Data

,

B-4

Scale In Hi

,

1-49

Scale In Lo

,

1-49

Scale In Value

,

1-49

Scale Out Hi

,

1-49

Scale Out Lo

,

1-49

Scale Out Value

,

1-49

Scaled Blocks Group

,

Setting Preferences

Shear Pin Fault

,

Shear Pin Time

Skip Freq Band

,

,

,

1-49

B-4

2-8

1-38

1-23

Skip Frequency

,

C-17

Skip Frequency x

,

1-23

Sleep Config Alarm

,

2-11

Sleep Level

,

1-37

Sleep Time

,

1-37

Sleep Wake Mode

Sleep-Wake Mode

,

C-19

,

1-36

Sleep-Wake Ref

,

1-37

Slip Comp Gain

,

Slip Comp Group

Slip RPM @ FLA

Slip RPM Meter

1-26

,

1-26

,

1-26

,

Software Fault

,

1-26

2-8

1-34

2-8

20B-UM001.book Page 10 Thursday, June 20, 2013 1:55 PM

Index-10

Spd Mode &amp; Limits Group

,

1-21

SpdBand Integrat

,

1-61

Speed Command File

,

1-21

Speed Desired BW

1-30

Speed Dev Band

,

,

1-61

Speed Feedback

,

1-13

Speed Feedback Group

,

Speed Loop Meter

,

Speed Mode

,

Testpoint x Data

1-46

Torq Attributes Group

,

Torq Prove Cflct Alarm

Torq Ref A Div

,

1-18

TorqLim SlewRate

,

1-61

TorqProve Cnfg

,

1-60

TorqProve Setup

,

1-60

TorqPrv Spd Band Fault

Torque Current

,

1-12

Torque Perf Mode

,

1-15

Torque Proving

,

C-2

Torque Ref B Mult

,

1-2

Torque Ref x Hi

,

Torque Ref x Lo

,

Torque Ref x Sel

1-18

1-18

,

Torque Setpoint

,

Torque Setpoint2

1-18

1-19

,

Total Inertia

,

1-19

1-30

Trim % Setpoint

,

1-26

Trim Hi

,

1-26

Trim In Select

,

1-26

Trim Lo

,

1-26

Trim Out Select

,

1-26

Trnsistr OvrTemp Fault

Troubleshooting

,

2-1

U

UnderVoltage

Alarm

,

2-12

Fault

,

2-9

User Configurable Alarm

,

2-1

User Sets

,

B-4

UserSet Chksum Fault

Utility File

,

1-38

V

VHz Neg Slope Alarm

,

2-9

2-12

Viewing and Changing Parameters

Voltage Class

,

1-41

Voltage Tolerance

,

C-24

Volts per Hertz Group

,

1-19

W

Wake Level

Wake Time

,

1-37

1-37

,

2-12

Web Sites, see WWW, World Wide Web

,

,

1-22

| Speed Ref A Hi ,  1-24                            |
|---------------------------------------------------|
| Speed Ref A Lo ,  1-24                            |
| Speed Ref A Sel ,  1-24                           |
| Speed Ref B Hi ,  1-24                            |
| Speed Ref B Lo ,  1-24                            |
| Speed Ref B Sel ,  1-24                           |
| Speed Ref Cflct Alarm ,  2-11                     |
| Speed Ref Source ,  1-43                          |
| Speed Reference ,  1-13                           |
| Speed References Group ,  1-24                    |
| Speed Regulator Group ,  1-29                     |
| Speed Trim Group ,  1-26                          |
| Speed Units ,  1-21                               |
| Speed/Torque Mod ,  1-23                          |
| Standard Control Option ,  1-3                    |
| Start At PowerUp ,  1-34 ,  C-21                  |
| Start At PowerUp Alarm ,  2-11                    |
| Start Inhibits ,  1-43                            |
| Start Mask ,  1-51                                |
| Start Owner ,  1-52                               |
| Start/Acc Boost ,  1-19                           |
| Static Discharge, ESD ,  P-3                      |
| Status 1 @ Fault ,  1-45                          |
| Status LEDs ,  2-2                                |
| Stop Mode x ,  1-32                               |
| Stop Owner ,  1-52 Stop/Brake Modes Group ,  1-32 |
| Stop/BRK Mode x ,  1-32                           |
| STS LED ,  2-2                                    |
| SV Boost Filter ,  1-16                           |
| SW OverCurrent Fault ,  2-8                       |
| TB Man Ref Cflct Alarm ,  2-12                    |
| TB Man Ref Hi ,  1-25                             |
| TB Man Ref Lo ,  1-25                             |
| TB Man Ref Sel ,  1-25 ,                          |
| Testpoint 1 Sel ,  1-46 2-16 Waking Alarm         |
| Testpoint Codes and Functions ,                   |

1-30

1-20

1-15

,

2-12

,

,

,

2-8

1-18

2-8

,

B-5

20B-UM001.book Page 11 Thursday, June 20, 2013 1:55 PM

Index-11

WWW, World Wide Web

Z

Zero SpdFloatTime

,

,

1-61

P-1

,

P-2

20B-UM001.book Page 12 Thursday, June 20, 2013 1:55 PM

Index-12

Notes:

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

PowerFlex 700 Parameter Record

Number Parameter Name Setting

40 Motor Type

41 Motor NP Volts

42 Motor NP FLA

43 Motor NP Hertz

44 Motor NP RPM

45 Motor NP Power

46 Mtr NP Pwr Units

## 47 Motor OL Hertz

48 Motor OL Factor

49 Motor Poles

Number Parameter Name Setting

125 PI Control

126 PI Reference Sel

127 PI Setpoint

128 PI Feedback Sel

129 PI Integral Time

130 PI Prop Gain

131 PI Lower Limit

132 PI Upper Limit

133 PI Preload

139 PI BW Filter

140, 141 Accel Time X

142, 143 Decel Time X

145 DB While Stopped

146 S Curve %

147 Current Lmt Sel

148 Current Lmt Val

149 Current Lmt Gain

150 Drive OL Mode

151 PWM Frequency

152 Droop RPM @ FLA

153 Regen Power Limit

154 Current Rate Limit

155, 156 Stop Mode X

Stop/BRK Mode X

157 DC Brk Lvl Sel

158 DC Brake Level

159 DC Brake Time

160 Bus Reg Ki

161, 162 Bus Reg Mode X

163 DB Resistor Type

164 Bus Reg Kp

165 Bus Reg Kd

166 Flux Braking

167 Powerup Delay

168 Start At PowerUp

169 Flying Start En

170 Flying StartGain

174 Auto Rstrt Tries

175 Auto Rstrt Delay

177 Gnd Warn Level

178 Sleep-Wake Mode

179 Sleep-Wake Ref

180 Wake Level

181 Wake Time

182 Sleep Level

183 Sleep Time

184 Power Loss Mode

185 Power Loss Time

186 Power Loss Level

187 Load Loss Level

188 Load Loss Time

189 Shear Pin Time

190 Direction Mode

192 Save HIM Ref

193 Man Ref Preload

| 54 Maximum Voltage   |
|----------------------|
| 88 Speed/Torque Mod  |

1

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

2

Number Parameter Name Setting

194 Save MOP Ref

195 MOP Rate

196 Param Access Lvl

197 Reset To Defalts

198 Load Frm Usr Set

199 Save To User Set

200 Reset Meters

201 Language

202 Voltage Class

234, 236 Testpoint X Sel

238 Fault Config 1

240 Fault Clear

241 Fault Clear Mode

259 Alarm Config 1

261 Alarm Clear

270 DPI Baud Rate

DPI Data Rate

274 DPI Port Sel

276 Logic Mask

277 Start Mask

278 Jog Mask

279 Direction Mask

280 Reference Mask

281 Accel Mask

282 Decel Mask

283 Fault Clr Mask

284 MOP Mask

285 Local Mask

298 DPI Ref Select

299 DPI Fdbk Select

300-307 Data In XX

310-317 Data Out XX

320 Anlg In Config

321 Anlg In Sqr Root

322, 325 Analog In X Hi

323, 326 Analog In X Lo

324, 327 Analog In X Loss

340 Anlg Out Config

341 Anlg Out Absolut

342, 345 Analog OutX Sel

343, 346 Analog OutX Hi

344, 347 Analog OutX Lo

354, 355 Anlg OutX Scale

361-366 Digital InX Sel

377, 378 Anlg OutX Setpt

379 Dig Out Setpt

Digital OutX Sel

Dig OutX Level

Dig OutX OnTime

Dig OutX OffTime

412 Motor Fdbk Type

413 Encoder PPR

416 Fdbk Filter Sel

419 Notch Filter Freq

420 Notch Filter K

422 Pulse In Scale

| 380,  384, 388  381,  385, 389  382,  386, 390  383,  387, 391   |
|------------------------------------------------------------------|

Number Parameter Name Setting

423 Encoder Z Chan

427, 431 Torque Ref X Sel

428, 432 Torque Ref X Hi

429, 433 Torque Ref X Lo

430 Torq Ref A Div

434 Torque Ref B Mult

435 Torque Setpoint

436 Pos Torque Limit

437 Neg Torque Limit

438 Torque Setpoint2

440 Control Status

445 Ki Speed Loop

446 Kp Speed Loop

447 Kf Speed Loop

449 Speed Desired BW

450 Total Inertia

454 Rev Speed Limit

459 PI Deriv Time

460 PI Reference Hi

461 PI Reference Lo

462 PI Feedback Hi

463 PI Feedback Lo

476-494 ScaleX In Value

477-495 ScaleX In Hi

478-496 ScaleX In Lo

479-497 ScaleX Out Hi

480-498 ScaleX Out Lo

600 TorqProve Cnfg

601 TorqProve Setup

602 Spd Dev Band

603 SpdBand Integrat

604 Brk Release Time

605 ZeroSpdFloatTime

606 Float Tolerance

607 Brk Set Time

608 TorqLim SlewRate

609 BrkSlip Count

610 Brk Alarm Travel

611 MicroPos Scale%

20B-UM001.book Page 1 Thursday, June 20, 2013 1:55 PM

20B-UM001.book Page 2 Thursday, June 20, 2013 1:55 PM

Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products.

At http://www.rockwellautomation.com/support, you can find technical manuals, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools. You can also visit

our Knowledgebase at http://www.rockwellautomation.com/knowledgebase for FAQs, technical information, support chat and forums, software updates, and to sign up for product notification updates.

For an additional level of technical phone support for installation, configuration and troubleshooting, we offer TechConnect

SM

support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://

www.rockwellautomation.com/support/

.

Installation Assistance If you experience a problem within the first 24 hours of installation, please review the information that's contained in this manual. You can also contact a special Customer Support number for initial help in getting your product up and running.

United States or Canada 1.440.646.3434 Outside United States or Canada Use the Worldwide Locator at http://www.rockwellautomation.com/rockwellautomation/support/overview.page, or contact your local Rockwell Automation representative.

New Product Satisfaction Return

Rockwell Automation tests all of its products to help ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

Contact your distributor. You must provide a Customer Support case number (call the phone number

Outside United States Please contact your local Rockwell Automation representative for the return procedure.

| United States  above to obtain one) to your distributor to complete the return process.   |
|-------------------------------------------------------------------------------------------|

Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/ .

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400

Publication 20B-UM001H-EN-P - June 2013

Supersedes Publication 20B-UM001G-EN-P - August 2004 Copyright © 2013 Rockwell Automation, Inc. All rights reserved. Printed in the U.S.A.