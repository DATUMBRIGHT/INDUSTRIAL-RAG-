<!-- image -->

## PowerFlex 750-Series Products with TotalFORCE Control

Catalog Numbers 20G, 20J

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

|                             | Preface                                                                                                                                     |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5          |
|                             | Chapter 1                                                                                                                                   |
| Drive Configuration         | Configuring Accel/Decel Time. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7               |
|                             | Automatic Device Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                |
|                             | Precharge Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13           |
|                             | Sleep/Wake Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14        |
|                             | Motor Stop Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18       |
|                             | Start Permissive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28     |
|                             | Low Speed Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30          |
|                             | Power Loss Ride-through . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34              |
|                             | Auxiliary Power Supply. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38          |
|                             | Motor Control Modes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38         |
|                             | Motor Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44  |
|                             | Selecting Velocity Feedback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50              |
|                             | Chapter 2                                                                                                                                   |
| TotalFORCE Control Features | Adaptive Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51     |
|                             | CIP Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 |
|                             | Secondary Motor Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60            |
|                             | Energy Pause Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63            |
|                             | Predictive Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67           |
|                             | Predictive Maintenance CIP Objects. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                    |
|                             | DeviceLogix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86  |
|                             | Emergency Override Function. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                 |
|                             | Reference Motion Planners . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97              |
|                             | Chapter 3                                                                                                                                   |
| Active Front End TotalFORCE | AC Line Commissioning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119             |
| Control                     | Droop Control for Parallel Operation of Bus Supplies. . . . . . . . . . . . . . . . . . . . . . . . . . . 121                               |
|                             | AC Line Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124      |
|                             | Backup Generator Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                    |
|                             | Chapter 4                                                                                                                                   |
| Diagnostics and             | High Speed Trending . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137           |
| Troubleshooting             | Faults and Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143       |
|                             | Input Phase Loss Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147               |
|                             | Chapter 5                                                                                                                                   |
| Application References      | PowerFlex 755T Lifting/Torque Proving. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151                        |
|                             | Anti-Sway Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166            |
|                             | Dynamic Braking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174        |
|                             | Dynamic Bus Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183           |

| Carrier (PWM) Frequency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189                |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog Inputs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191       |
| Analog Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198         |
| Digital Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203     |
| Digital Outputs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213       |
| PTC Motor Thermistor Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                   |
| Index   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . 225 |
| Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227             |

## Summary of Changes

The purpose of this manual is to provide detailed information about configuring PowerFlex® 750-Series products with TotalFORCE® control for common applications.

This manual is intended for qualified personnel. You must be able to program and operate Adjustable Frequency AC Drive devices. In addition, you must have an understanding of the parameter settings and functions.

In this manual we refer to the PowerFlex 750-Series products with TotalFORCE control as:

- PowerFlex 755T products when referring to the group of drives, bus supplies, and common bus inverters listed below.
- PowerFlex 755TL drive when referring to the low harmonic drive product.
- PowerFlex 755TR drive when referring to the regenerative drive product.
- PowerFlex 755TM drive system when referring to regenerative bus supply and common bus inverter products.
- PowerFlex 755TS drive when referring to the six-pulse rectifier standalone AC drive product.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic Page                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------|
| Where an option module cat. no. is listed, the -XT version is also listed if applicable. 10, 12, 154, 157, 158, 164 |
| Corrected parameter number for 10/11:290 [InPhase Loss Lvl]. 149                                                    |
| Updated the Brake Set footnote under the Torque Proving Flow Diagram. 152                                           |

## Notes:

## Configuring Accel/Decel Time

## Drive Configuration

This chapter discusses common configuration topics for PowerFlex® products.

| Topic Page                       |
|----------------------------------|
| Configuring Accel/Decel Time 7   |
| Automatic Device Configuration 9 |
| Precharge Sequence 13            |
| Sleep/Wake Mode 14               |
| Motor Stop Modes 18              |
| Start Permissive 28              |
| Low Speed Operation 30           |
| Power Loss Ride-through 34       |
| Auxiliary Power Supply 38        |
| Motor Control Modes 38           |
| Motor Types 44                   |
| Selecting Velocity Feedback 50   |

You can configure the drive's acceleration time and deceleration time.

## Acceleration Time

Parameters 10/11:1915 [VRef Accel Time 1] and 10/11:1916 [VRef Accel Time 2] set the acceleration ramp that is applied to velocity reference commands. Defined as the time to accelerate from zero to Motor Rated Hz 10/11:402 [Motor NP Hertz] or to Motor Rated RPM 10/ 11:403 [Motor NP RPM]. The setting of Hertz or RPM is programmed in parameter 0:46 [Velocity Units].

A digital input function controls the selection between [VRef Accel Time 1] and [VRef Accel Time 2]. Digital Input Functions are configured through the Feedback &amp; I/O file in Port 0. See the PowerFlex Drives with TotalFORCE® Control Programming Manual, publication 750-PM101 for more information on Digital Input functions. Or, a Logic Command that is sent over a communication network or DeviceLogix™ software can also be used.

This value is used to calculate acceleration and deceleration rates equivalent to LinScurve behavior when 10/11:933 [Ref Time Base] = 0 'Rate'.

This value isn't used when 10/11:933 [Ref Time Base] = 1 'Time'. Instead, 10/11:934 [Ref Accel Time] and 10/11:935 [Ref Decel Time] are applied directly as acceleration and deceleration times. Used only in FVC mode.

Adjustment range is 0.00...3600.00 seconds.

<!-- image -->

## Deceleration Time

Parameter 10/11:1917 [VRef Decel Time 1] and 10/11:1918 [VRef Decel Time 2] set the deceleration ramp time that is applied to velocity reference commands. Defined as the time to decelerate from the Motor Rated Hz 10/11:402 [Motor NP Hertz] or to Motor Rated RPM 10/11:403 [Motor NP RPM]. The setting of Hertz or RPM is programmed in 0:46 [Velocity Units].

A digital input function controls the selection between [VRef Decel Time 1] and [VRef Decel Time 2]. See Digin Functions in the PowerFlex Drives with TotalFORCE Control Programming Manual, publication 750-PM101. Or, a Logic Command that is sent over a communication network or DeviceLogix software can also be used.

This value is used for these stop modes: Ramp, Ramp to Hold, and DecelToHold.

This value is used to calculate acceleration and deceleration rates equivalent to LinScurve behavior when 10/11:933 [Ref Time Base] = 0 'Rate'.

This value isn't used when 10/11:933 [Ref Time Base] = 1 'Time'. Instead, 10/11:934 [Ref Accel Time] and 10/11:935 [Ref Decel Time] are applied directly as acceleration and deceleration times. Used only in FVC mode.

Adjustment range is 0.00...3600.00 seconds.

## Automatic Device Configuration

Automatic Device Configuration (ADC) is a Studio 5000 Logix Designer® application feature that supports the automatic download of drive configuration data. When the RSLogix 5000® software controller establishes an I/O connection with a drive and its associated peripherals, it checks a configuration signature for each port. This check determines if an ADC download is needed. The purpose is to reduce downtime during a field replacement by automatically downloading the configuration rather than manually with a separate tool.

## Compatibility

ADC is available with the following software:

- RSLogix 5000 software, Version 20
- Studio 5000® software, Version 21 and higher
- Drive AOPs, Version 1.xxx and higher for PowerFlex 755T

The latest drive AOPs ship with each release of Studio 5000 Logix Designer and are also available for free download at the Product Compatibility and Download Center (PCDC), rok.auto/pcdc .

To identify the drive AOP version that you are using, open the AOP, click the icon in the upper left corner of the window and select 'About Module Profile'.

<!-- image -->

<!-- image -->

ADC works with all versions of the PowerFlex 755T drives when the Logix I/O connection is made through the built-in EtherNet/IP™ port.

Firmware updates are available for download at the Product Compatibility and Download Center (PCDC), rok.auto/pcdc .

If you do not have the minimum levels of software and hardware, the ADC feature isn't available (ADC icon is missing or appears dimmed). Drive configuration settings are stored inside the ACD project file. With ADC enabled, the Logix controller automatically downloads the configuration settings for a particular drive port if it detects that there's a configuration signature mismatch with a port.

A configuration signature is a globally unique ID number. The Logix controller uses the number to perform a quick compare to determine if a download is needed. If the signatures match, no download is needed. If an option module or entire drive is replaced, the configuration signature for the respective port does not match and a download occurs to the port.

## Activation

To activate the ADC feature, click Device Definition under the Overview tab of the drive.

<!-- image -->

Once in the Device Definition tab, click Automatic Device Configuration. Check the box to Enable Automatic Device Configuration to enable ADC for the drive and all peripheral devices that are identified on the page. When enabled, the configuration data is verified for the connected devices by the controller (configuration owner) when establishing a network I/O connection and, when different, downloaded to the device.

The Enable Automatic Device Configuration is accessible at the Port/Device Level. This allows you to enable/disable ADC for the all or only selected ports/devices. The checkboxes appear unavailable when the global Enable Automatic Device Configuration checkbox is cleared.

ADC can't be configured for some ports/devices, such as a Safe Torque Off option module (20750-S3 and 20-750-S3-XT). The Safety Controller manages the configuration of the Network STO option module.

The column on the right with Fail Drive Connection on Peripheral Error indicates that the controller does not establish a network I/O connection with the drive if an error occurs with this peripheral device.

<!-- image -->

When ADC is enabled, it's visible in the Overview page of the drive:

<!-- image -->

When ADC is enabled, ADC is triggered anytime the Logix controller detects a configuration signature mismatch when establishing an EtherNet/IP network I/O connection.

The use of other configuration tools, such as a HIM or Connected Components Workbench™ software must be minimized and restricted to monitor-only operation. Any configuration changes made by these tools will cause a configuration signature mismatch the next time the Logix controller connects to the device. ADC writes over any configuration changes made by the other tools. Consider using the Write Mask function, drive parameter 0:230 [Write Mask Cfg]. The function stops tools that are connected to ports other than the built-in EtherNet/IP port in a PowerFlex 755T drive from writing to the drive. Any drive configuration changes must be made with the Add-on Profile (AOP).

The use of Explicit Messaging to perform parameter writes in the Logix program must be limited to RAM memory by setting the proper Attribute in the MSG instruction. Any writes to parameter nonvolatile storage (NVS) will clear the configuration signature and cause a mismatch the next time the Logix controller connects to the device. This triggers ADC, which writes over any configuration changes that were previously made.

ADC can execute the first time the Logix controller connects to the drive after ADC has been enabled. The configuration signatures in the controller and drive synchronize, and stops future ADC downloads from occurring unless a configuration change is made or the drive / peripheral is replaced. If a port has configuration parameters that require a reset to become active, ADC will reset the drive after the respective port parameters are downloaded.

When ADC is enabled, it can be activated if the controller is in Run or Program mode. Select 'Inhibit Module' when changes are made to the drive to limit ADC from writing over your changes. 'Inhibit Module' is on the Connection tab in the drive module profile.

Use the Stratix® switches to provide the dynamic IP address assignment by port. This selection removes the need to enter the IP address, subnet mask, and Gateway address manually before connecting a replacement drive to the Ethernet network.

ADC can work in tandem with the Firmware Supervisor. If the Firmware Supervisor is configured and enabled for a drive ('Exact Match' keying must be used), the drive firmware is automatically updated (if necessary) before any ADC operation for that port.

Information on Automatic Device Configuration (ADC) can be found in the PowerFlex 750Series Drives with TotalFORCE Control Built-in EtherNet/IP Adapter User Manual, publication 750COM-UM009, Chapter 3, Configuring the Drive in a Logix System includes the following topics:

- Description of the ADC functionality
- How the Drive Add-on Profiles (AOPs) affect ADC
- Configuring a PowerFlex 755T Drive (firmware 1.xxx or later) for ADC
- ADC and Logix Memory
- Peripheral Changes When Using ADC
- Special Considerations When Using a Safe Speed Monitor Module (20-750-S1 or 20-750S1-XT)
- Special Considerations for Communications and Option Developers Kit Option Cards
- Testing ADC
- Monitoring the ADC Progress
- Programmatically Monitoring Connection Status and the ADC
- Examples of potential issues and solutions
- Best practices

## Precharge Sequence

PowerFlex 755T products use a precharge sequence to control power-up. The precharge sequence starts as soon as the drive detects incoming three-phase power on the input terminals. The sequence ends when the main control board is able to communicate with all necessary peripherals. The following frame-specific sections guide you through the precharge sequence and define what occurs at each step.

## Frames 5 and 6

1. Three-phase power is applied.
2. Incoming three-phase power is stepped down and the main control board is powered.
3. The main control board performs a check before it initiates the precharge sequence.
4. A precharge resistor bank is connected between the AC line and the input of the converter. This resistor bank limits the voltage that is available while the DC bus and LCL filter capacitors begin charging.
5. When the DC bus is 85% of the nominal voltage rating, the AC precharge circuit bypasses the precharge resistor bank. Full line voltage is applied to the input of the converter to complete the precharge sequence.
6. Main control board checks for an 'Ok' status to verify that the precharge sequence was completed successfully and that the drive is ready.

## Frames 7…15

1. Three-phase power is applied.
2. The operator closes the main fuse disconnect (FD1).
3. A step-down transformer limits incoming three-phase power to 240V. Power is applied to the AC precharge board and to the 24V DC network.
4. 24V DC is applied to the control pod and main control board. Fiber-optic communication is established between the main control board and the AC precharge board.
5. The main control board performs a check and sends an 'Ok' status to the AC precharge board to proceed with the precharge sequence.
6. The AC precharge board closes the AC precharge contactor to connect the precharge resistor bank to the DC bus and the LCL filter module.
7. When the DC bus is 85% of nominal voltage rating, the AC precharge circuit closes the AC precharge circuit breaker (CB1). The AC precharge contactor opens to disconnect the precharge resistor bank from the DC bus.
8. The switched mode power supply (SMPS) of the converter and inverter power modules is at 400V DC.
9. The power layer interface (PLI) board, current sense board (CSB), and gate driver are powered by SMPS.
10. The main control board checks communications between AC precharge board, PLI board, CSB board, and gate driver.
11. If the check comes back 'Ok', the precharge is complete and the drive is ready.

## Sleep/Wake Mode

The purpose of the sleep/wake function is to start (wake) the drive when an analog signal level is greater than or equal to the value in parameter 9:94 [Wake Level]. One common application of this function is for efficient control of pumps that use feedback from digital limit sensors to maintain a holding tank between a 'high' and 'low' level. The drive stops (sleeps) when an analog signal level is less than or equal to the value in parameter 9:92 [Sleep Level]. Parameter 9:91 [SleepWake RefSel] selects the source of the analog signal. Set parameter 9:90 [Sleep Wake Mode] to 1 'Direct' to enable the sleep/wake function to work as described.

To function in Invert mode, set parameter 9:90 [Sleep Wake Mode] to 2 'Invert'. The Invert setting changes the logic so that an analog signal level that is less than or equal to parameter 9:94 [Wake Level], the drive starts. The drive stops when an analog signal level is greater than or equal to parameter 9:92 [Sleep Level].

The sleep/wake function is in the Port 9 Process PID primary file.

<!-- image -->

To add Port 9, double-click the drive. Under the Overview tab, click Device Definition:

<!-- image -->

Once you are in Device Definition, go to Dynamic Features and set the Application Set to ProcPID Only to activate Port 9: PID.

<!-- image -->

If you would like to activate DLX, you can activate it under Emb Logic Select: DeviceLogix.

## Sleep/Wake Related Parameters

| Parameter No. Parameter Name Description                                                            |
|-----------------------------------------------------------------------------------------------------|
| 9:90 Sleep Wake Mode Enables/disables the sleep/wake function.                                      |
| 9:91 SleepWake RefSel Selects the source of the input controlling the sleep/wake function.          |
| 9:92 Sleep Level Defines the SleepWake RefSel signal level that stops the drive.                    |
| 9:93 Sleep Time  Defines the amount of time at or below 9:92 [Sleep Level] before a Stop is issued. |
| 9:94 Wake Level Defines the SleepWake RefSel signal level that starts the drive.                    |
| 9:95 Wake Time  Defines the amount of time at or above 9:94 [Wake Level] before a Start is issued.  |

## Sleep/Wake Operation

<!-- image -->

## Conditions to Start/Restart

<!-- image -->

ATTENTION: Enabling the sleep/wake function can cause unexpected machine operation during the Wake mode. Equipment damage and/or personal injury can result if this parameter is used in an inappropriate application. Do not use this function without considering Table 1 and applicable local, national, and international standards, regulations, or industry guidelines.

Table 1 - Conditions Required to Start Drive (1)(2)(3)

|                             | Input After Power-up                                | After a Drive Fault After a Stop Command              | After a Drive Fault After a Stop Command                        |                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Input After Power-up                                | Reset by HIM or Software ‘Stop’                       | Reset by HIM, Network/Software, or Digital Input ‘Clear Faults’ | HIM, Network/Software, or Digital Input ‘Stop’                                                                                                          |
| Stop (4)                    | Stop Closed Wake Signal New Start or Run Command(5) | Stop Closed Wake Signal New Start or Run Command(5)   | Stop Closed Wake Signal                                         | Stop Closed Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8) New Start or Run Command(5)   |
| Enable                      | Enable Closed Wake Signal                           | Enable Closed Wake Signal New Start or Run Command(5) | Enable Closed Wake Signal                                       | Enable Closed Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8) New Start or Run Command(5) |
| Run Run Forward Run Reverse | Run Closed Wake Signal                              | New Run Command(6) Wake Signal                        | Run Closed Wake Signal                                          | New Run Command Direct mode: SleepWake RefSel Signal > Sleep Level (7) Invert mode: SleepWake RefSel Signal < Sleep Level (8)                           |

- (1) When power is cycled, if all conditions are present after power is restored, restart occurs.
- (2) If all conditions are present when [Sleep Wake Mode] is 'enabled,' the drive starts.

(3) The active speed reference. The Sleep/Wake function and the speed reference can be assigned to the same input.

- (4) Can't use 0:110 [DI M CurLmt Stop] or 0:111 [DI M Coast Stop] as the only Stop Input. This configuration causes a Type 2 alarm.

(5) Command must be issued from HIM, terminal block, or network.

(6) Run Command must be cycled.

(7) SleepWake Ref Sel signal does not need to be greater than the wake level.

(8) SleepWake Ref Sel signal does not need to be less than the wake level.

For the Invert function, refer to the [Anlg Inn LssActn] parameter.

Normal operation requires that parameter 9:94 [Wake Level] is set to greater than parameter 9:92 [Sleep Level]. However, there are no limits that help prevent the parameter settings from crossing, but you can't start the drive until those settings are corrected. These levels are programmable while the drive is running. If parameter 9:92 [Sleep Level] is made greater than parameter 9:94 [Wake Level] while the drive is running, the drive continues to run. As long as the parameter 9:91 [SleepWake RefSel] signal remains at a level that doesn't trigger the sleep condition. Parameter 9:93 [Sleep Time] is also factored in. Once the drive goes to sleep in this situation, it isn't allowed to restart until the level settings are corrected (increase parameter 9:94 [Wake Level], or decrease parameter 9:92 [Sleep Level]). If however, the levels are corrected before the drive goes to sleep, normal Sleep/Wake operation continues.

## Timers

Parameter 9:93 [Sleep Time] Parameter 9:95 [Wake Time]

Timers determine the length of time required for Sleep/Wake levels to produce true functions. These timers start counting when the Sleep/Wake levels are met and count in the opposite direction whenever a respective level isn't met. If the timer counts to the user specified time, it creates an edge to toggle the Sleep/Wake function to the respective condition (sleep or wake). On power-up, timers are initialized to the state that does not permit a start condition. When the analog signal satisfies the level requirement, the timers start counting.

## Interactive Functions

Separate start commands are also honored (including a digital input start), but only when the sleep timer isn't satisfied. Once the sleep timer times out, the sleep function acts as a continuous stop. There are two exceptions that ignore the Sleep/Wake function.

1. When a device is commanding local control. For example a HIM in Manual mode or a digital input that is programmed to parameter 0:132 [DI M Manual Ctrl].
2. When a jog command is being issued.

When a device is commanding local control, the port that is commanding it has exclusive start control (and ref select), it overrides the Sleep/Wake function, and it allows the drive to run in the presence of a sleep condition. This configuration holds true even when a digital input is programmed to parameter 0:132 [DI M Manual Ctrl], a digital input start, or run, is able to override a sleep condition.

## Sleep/Wake Sources

The parameter 9:91 [SleepWake RefSel] signal source for the sleep/wake function can be any analog input, whether it's being used for another function or not, a DeviceLogix software source (parameter 9:1120 [DLX Real Out SP1] through 9:1127 [DLX Real Out SP8]), or a valid numeric edit configuration. Configure the sleep/wake source with parameter 9:91 [SleepWake RefSel].

Also, parameters [Anlg Inn Hi] and [Anlg Inn Lo] have no effect on the function, however, the factory calibrated result, parameter [Anlg Inn Value] is used. In addition, the absolute value of the calibrated result is used, which makes the function useful for bipolar direction applications.

Parameter [Anlg Inn LssActn] configures the analog in loss function, which is unaffected and therefore operational with the sleep/wake function, but not tied to the sleep or wake levels and is triggered off the [Anlg Inn Raw Value] parameter.

See the PowerFlex Drives with TotalFORCE Control Programming Manual (firmware revision 10.xxx and later), publication 750-PM101, for more details.

## Motor Stop Modes

Motor Stop Mode A/B can be configured as a method of stopping the drive when a stop command is given. A normal stop command results when the run input changes from true to false. However, when using Torque Prove, parameter 9:50 [Trq Prove Cfg] with bit 0 enabled, parameter 10/11:110/111 [Mtr Stop Mode A/B] must be set to 1 'Ramp'.

Parameter 10/11:145 [Stop Dwell Time] can also be used with a stop command. This option can be used to set an adjustable time between detecting zero speed and turning off the drive output.

## Braking Methods

PowerFlex 755T products offer several methods for stopping a load. Set the stop method or mode with parameters 10/11:110 [Mtr Stop Mode A] and 10/11:111 [Mtr Stop Mode B]. These modes are listed in the following table.

|                  | Method Use When Application Requires Braking Power                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| 0 ‘Coast’        | The motor side inverter immediately stops modulating (stops gating its power devices). Power is removed from the motor and it coasts to zero speed.                                                                                                                                                                                                                                                                                                                                                                                                | None                           |
| 1 ‘Ramp’         | The motor side inverter decelerates the motor, at the rate that is set by the active Decel Time, until it reaches the Zero Speed threshold. It stops modulating (stops gating its power devices) when it reaches the Zero Speed threshold. The fastest stopping time or fastest ramp time for speed changes (external brake resistor or regenerative capability that is required for ramp times faster than the following methods). High duty cycles, frequent stops, or speed changes. (The other methods can result in excessive motor heating). | High                           |
| 2 ‘Current Lmt’  | The motor side inverter decelerates the motor at a rate where the Decel Time is 0.1 seconds. It does not exceed the Current Limit to stop at this rate. It stops modulating (stops gating its power devices) when it reaches the Zero Speed threshold. Max torque/current applied until zero speed.                                                                                                                                                                                                                                                | Maximum                        |
| 3 ‘DecelToHold’  | The motor decelerates using the active Decel Time, until it reaches the Zero Speed threshold. It holds by continuing to modulate with a zero speed (zero frequency) output until there’s a new start command, new run command, or another kind of stop command. This option is intended for use with an encoder and safety module to verify that the drive is holding zero speed.                                                                                                                                                                  | Same as ‘Ramp’                 |
| 4 ‘Ramp to Hold’ | The motor decelerates using the active Decel Time, until it reaches the Zero Speed threshold. It holds by DC braking until there’s a new start command, new run command, or another kind of stop command. Only available with induction motor control modes.                                                                                                                                                                                                                                                                                       | Same as ‘Ramp’ or ‘Fast Brake’ |
| 5 ‘DC Brake’     | The motor side inverter halts output phase rotation and injects DC current on the last used output phase. DC braking is immediately applied (does not follow the programmed decel ramp). Make adjustments with parameter 10/11:154 [DCBrk Cur Reg BW]. Only available with induction motor control modes.                                                                                                                                                                                                                                          | Less than ‘Ramp’               |
| 6 ‘Fast Brake’   | High slip braking for maximum braking performance above base speed. The motor side inverter decreases the output frequency so it’s lower than the motor speed, but not low enough for regeneration to occur. It forces the frequency to zero when the frequency is too low to allow regeneration to cause the DC bus to rise. Only available with induction motor control modes. Important: The Bus Regulation Mode must be Adjust Frequency use this stop mode.                                                                                   | More than ‘DC Brake’           |

Additionally, parameter 10/11:138 [Flux Braking En] can be selected separately (not part of the Stop mode selection) to provide additional braking during a Stop command or when reducing the speed command. For Stop commands, this parameter provides additional braking power during 'Ramp', 'DecelToHold' and 'Ramp to Hold' selections only. If 'Fast Brake' or 'DC Brake' is used, 'Flux Braking' is active only during speed changes when enabled.

A 'Ramp' selection always provides the fastest stopping time. PowerFlex 755TR and PowerFlex 755TM Regenerative Bus Supplies provide regeneration to the AC line. PowerFlex 755TL and PowerFlex 755TM Non-Regenerative Supply can require a method of dissipating regenerative energy from the DC bus such as a dynamic braking resistor or regenerative brake for example. The PowerFlex Dynamic Brake Resistor Calculator application technique, publication PFLEX-AT001, explains dynamic braking in detail.

The alternative braking methods to external hardware brake requirements can be enabled if the stopping time isn't as restrictive. Each of these methods dissipates energy in the motor. Consequently, use care to avoid motor overheating.

## Coast

<!-- image -->

Coast is selected by setting parameter 10/11:110/111 [Mtr Stop Mode A/B] to 0 'Coast'. When in Coast to Stop, the drive acknowledges the Stop command by shutting off the output and releasing control of the motor. The load/motor will coast or free spin until the kinetic energy is dissipated. Available with all motor control modes.

- On Stop, the drive output goes immediately to zero (off).
- No further power is supplied to the motor. The drive has released control.
- The motor coasts for a time that is dependent on the mechanics of the system (Inertia, friction, and so forth).

## Ramp

<!-- image -->

Ramp to Stop is selected by setting parameters 10/11:110/111 [Mtr Stop Mode A/B] to 1 'Ramp'. The drive ramps the frequency to zero based on the deceleration time programmed into parameters 10/11:1917/1918 [VRef Decel Time 1/2]. The normal mode of machine operation can use 10/11:1917 [VRef Decel Time 1]. If the machine Stop requires a faster deceleration than desired for normal deceleration, 10/11:1918 [VRef Decel Time 2] can be activated with a faster rate selected. When in Ramp mode, the drive acknowledges the Stop command by decreasing or ramping the output voltage and frequency to zero in a programmed period (Decel Time), maintaining control of the motor until the drive output reaches zero. The drive output is then shut off. The load/motor follows the decel ramp. Other factors such as bus regulation and current limit can alter the actual decel rate. Available with all motor control modes.

Ramp mode can also include a timed DC hold brake. Once the drive has reached zero output hertz on a Ramp to Stop and both parameter 10/11:153 [DC Brake Time] and parameter 10/11:152 [DC Brake Level] aren't zero, the drive applies DC to the motor that is producing current at the DC Brake Level for the DC Brake Time. Only available with induction motor control modes.

## Current Limit Stop

<!-- image -->

Current limit stop isn't typically set up as the normal Stop mode. Usually the normal stop is programmed at some ramp rate. For the current limit stop, a digital input is used for the function. However, you certainly could set the normal stop as current limit stop. Available with all motor control modes.

Current limit stop ramp rate is 0.1 second and isn't programmable.

<!-- image -->

In this example, the current limit was set high enough to allow the full rating of the drive to be used in the stop sequence.

## Example

<!-- image -->

In this example, the current limit was set at some value such that when the stop was issued the output current was clamped at that setting. The decel time is extended.

## Decel to Hold

<!-- image -->

This method uses drive output reduction to ramp the motor to zero speed and speed regulator output to hold the load at zero speed once it has stopped. This option is intended for use with an encoder and safety module to verify that the drive is holding zero speed. Available with all motor control modes.

- A Stop command initiates motor deceleration using the active Decel Time, until it reaches the Zero Speed threshold.
- It holds by continuing to modulate with a zero speed (zero frequency) output.
- The level of output current depends on the load.
- The hold persists until there's a new start command, new run command, or another kind of stop command.

## Ramp to Hold

<!-- image -->

This method combines two of the stop methods. It uses drive output reduction to ramp the motor to zero speed and DC braking to hold the load at zero speed once it has stopped. Only available with induction motor control modes.

- Stop command initiates ramping the output voltage and frequency to zero in a programmed period (Decel Time), maintaining control of the motor until the drive output reaches zero.
- When the output reaches zero, the three-phase drive output goes to zero (off) and the drive outputs a DC voltage on the last used phase to provide the current level programmed in parameter 10/11:152 [DC Brake Level]. This voltage causes a holding brake torque.
- DC voltage to the motor continues until a Start command is reissued or the drive is disabled.
- If a Start command is reissued, DC Braking ceases and the drive returns to normal AC operation. If an Enable command is removed, the drive enters a Not Ready state until the enable is restored.

## DC Brake

<!-- image -->

This method uses DC injection of the motor to Stop and/or hold the load. DC Brake is selected by setting parameter 10/11:110/111 [Mtr Stop Mode A/B] to 5 'DC Brake'. You can also choose the amount of time the braking is applied and the magnitude of the current used for braking with parameter 10/11:153 [DC Brake Time] and parameter 10/11:152 [DC Brake Level]. This mode of braking generates up to 40% of rated motor torque for braking and is typically used for low inertia loads with infrequent Stop cycles. Only available with induction motor control modes.

- On Stop, three phase drive output goes to zero (off).
- Drive outputs the DC voltage on the last used phase to provide the current level programmed in parameter 10/11:152 [DC Brake Level]. This voltage causes a stopping brake torque. If the voltage is applied for a time that is longer than the actual possible stopping time, the remaining time is used to attempt to hold the motor at zero speed (decel profile 'B' on the diagram).
- DC voltage to the motor continues for the amount of time that is programmed in parameter 10/11:153 [DC BrakeTime]. Braking ceases after this time expires.
- After the DC Braking ceases, no further power is supplied to the motor. The motor/load might not be stopped. The drive has released control of the motor/load (decel profile 'A' on the diagram).
- The motor, if rotating, coasts from its present speed for a time that is dependent on the remaining kinetic energy and the mechanics of the system (inertia, friction, and so forth).
- Excess motor current and/or applied duration, could cause motor damage. Motor voltage can exist long after the Stop command is issued. The right combination of Brake Level and Brake Time must be determined to provide the safest, most efficient stop (decel profile 'C' on the diagram).

## Fast Brake

<!-- image -->

This method takes advantage of the characteristic of the induction motor whereby frequencies greater than zero (DC braking) can be applied to a spinning motor that provides more braking torque without causing the drive to regenerate. Only available with induction motor control modes.

- On Stop, the drive output decreases based on the motor speed, and keeps the motor out of the regen region. This is accomplished by lowering the output frequency below the motor speed where regeneration does not occur. The excess energy is lost in the motor.
- The method uses a PI based bus regulator to regulate the bus voltage by automatically decreasing output frequency at the proper rate.
- When the frequency is decreased to a point where the motor no longer causes the bus voltage to increase, the frequency is forced to zero. DC brake is used to complete the stop if the DC Braking Time is nonzero, then the output is shut off.
- Use of the current regulator verifies that over current trips don't occur and allow for an easily adjustable and controllable level of braking torque.
- Use of the bus voltage regulator results in a smooth, continuous control of the frequency and forces the maximum allowable braking torque to always be utilized.

## IMPORTANT

For this feature to function properly the active [Bus Reg Mode A/B] must be set to 1 'Adjust Freq' and not be 0 'Disabled'.

## Example

<!-- image -->

## Block Diagram

<!-- image -->

## Flux Braking

Flux Braking is an independent feature from the parameter 10/11:110/111 [Mtr Stop Mode A/B] available in PowerFlex 755T products. When enabled, flux braking is active during the decel ramp of a speed change. Flux braking changes the Volts per Hertz curve ratio outputting a higher voltage, relative to the normal V/Hz curve, to the motor causing over fluxing thus reducing the speed faster than just the decel ramp alone. This feature isn't intended for high inertia loads because over fluxing can cause excessive heating in the motor. Long decel times can build heat.

Flux Braking works in all motor control modes. Flux braking only works with induction motors and only during deceleration.

Table 2 - Flux Braking Parameters

| Number Parameter Name Min / Max Default               |
|-------------------------------------------------------|
| 10/11:138 Flux Braking En Disabled / Enabled Disabled |
| 10/11:139 Flux Braking Kp 0.0 / 1000000.0 100.0       |
| 10/11:140 Flux Braking Ki 0.0 / 1000000.0 10000.0     |
| 10/11:141 Flux Braking Lim 100.00 / 250.00% 125.00    |

## Traces

In the following plots, the Accel/Decel times are 0.5 s. Parameter 10/11:116/117 [Bus Reg Mode A/ B] is set to option 1 'Adjust Freq'. There's a fair amount of inertia that is connected to the motor shaft. Parameter 10/11:110/111 [Mtr Stop Mode A/B] is set to 1 'Ramp' to stop.

In the plot below the Flux Braking feature is disabled. Note the decel time. Here the bus regulator is controlling the stop time.

## Flux Braking - Disabled

<!-- image -->

-15

In the next plot, all conditions are the same except the Flux Braking feature is enabled. Note that the flux to the motor is increased and the decel time is shorter.

<!-- image -->

Finally the same test with the gains set to maximum levels. Slightly faster decel. The use of the gains varies with the connected load.

Flux Braking - Full Gains

<!-- image -->

## Start Permissive

Certain status conditions must be met to permit the motor inverter to start in any mode, such as run, jog, or autotune.

PowerFlex 755TL/TR drives and PowerFlex 755TM regenerative bus supplies with active front end converters require that certain conditions must be met to permit line side converter modulation start.

When all permissive conditions are met, the motor inverter and/or line side active converter is considered ready to start. The ready condition is confirmed through the ready status in motor inverter parameters 10/11:354 [Motor Side Sts 1] and 10/11:355 [Motor Side Sts 2] and the line converter parameter 13:225 [Line Side Sts 1].

## Permissive Conditions

- No faults can be active.
- No Type 2 alarms can be active.
- The DI Enable input, if configured, must be closed.
- The DC bus precharge logic must indicate it is a start permissive.
- All Stop inputs must be negated and any drive stop/inhibit functions must not be issuing a stop command.
- No configuration changes (parameters being modified) when a download is in progress.
- The drive's safety option module logic must be satisfied.

PowerFlex 755TL/TR drives and PowerFlex 755TM common bus inverters motor inverter conditions that are inhibiting start are shown in parameter 10/11:351 [M Start Inhibits]. Conditions that prevented the last start command are shown in parameter 10/11:352 [MLastStrtInhibit].

Parameter 10/11:351 - Motor Side Inverter Start Inhibits displays the conditions that are currently inhibiting the motor side inverter from starting.

Bit 0 'Faulted' – System is in a faulted state.

Bit 1 'Alarm' – A Type 2 alarm exists.

Bit 2 'Enable' – An Enable input is open.

Bit 3 'Precharge' – System is in precharge.

Bit 4 'Stop' – The motor side inverter is receiving a stop command.

Bit 5 'Database' – Database is performing a download operation.

Bit 6 'Startup' – The assisted Start routine in the HIM is active and preventing a start.

Bit 7 'RotarySwitch' – Rotary switches on the main control board are set to a combination (888) that prevents start.

Bit 8 'Safety' – A Functional Safety option module is preventing a start.

Bit 9 'Sleep' – Sleep function is issuing a stop.

Bit 10 'Profiler' – Profiler function is issuing a stop.

Bit 11 'CommutNotCfg' – The permanent magnet motor commutation function hasn't been configured for use.

Bit 12 'Ovrd Event' – Inverter start is inhibited due to fault, but converter can continue running.

Bit 13 'Standby' – Indicates that the system is in a low energy (paused) state.

Parameter 10/11:352 - Last Motor Side Inverter Start Inhibits displays the conditions that kept the motor side inverter from starting during the last inhibit.

Bit 0 'Faulted' – System is in a faulted state.

Bit 1 'Alarm' – A Type 2 alarm exists.

Bit 2 'Enable' – An Enable input is open.

Bit 3 'Precharge' – System is in precharge.

Bit 4 'Stop' – The motor side inverter is receiving a stop command.

Bit 5 'Database' – Database is performing a download operation.

Bit 6 'Startup' – The assisted Start routine in the HIM is active and preventing a start.

Bit 7 'RotarySwitch' – Rotary switches on the main control board are set to a combination (888) that prevents start.

Bit 8 'Safety' – A Functional Safety option module is preventing a start.

Bit 9 'Sleep' – The Sleep function is issuing a stop.

Bit 10 'Profiler' – Profiler function is issuing a stop.

Bit 11 'CommutNotCfg' – The permanent magnet motor commutation function hasn't been configured for use.

Bit 12 'Ovrd Event' – Inverter start is inhibited due to fault, but converter can continue running.

Bit 13 'Standby' – Indicates that the system is in a low energy (paused) state.

When the drive receives a new start command, it copies the value from parameter 10/11:351 [M Start Inhibits] into this parameter.

PowerFlex 755TL/TR drives and PowerFlex 755TM regenerative bus supply line converter conditions that are inhibiting modulation start are shown in parameter 13:235 [L Start Inhibits]. Conditions that prevented the last start command are shown in parameter 13:236 [LLastStrtInhibit].

Parameter 13:235 - Line Side Converter Start Inhibits displays the conditions that are inhibiting the line side converter from starting and modulating.

Bit 0 'Faulted' – Indicates that a Fault is present. Faults provide notification of events. They prevent the line side converter from modulating.

Bit 1 'Alarm' – Indicates a Type 2 alarm is present. Type 2 alarms usually indicate a configuration error. They prevent the line side converter from starting and modulating.

Bit 2 'Enable' – Indicates that a digital input is configured for the line side converter Enable function, and it isn't energized (set).

Bit 3 'Precharge' – Indicates that the line side converter is executing a Precharge.

Bit 4 'Stop' – Indicates that the line side converter is receiving a stop command.

Bit 5 'Database' – Indicates that the database is performing a download operation.

Bit 6 'Startup' – Indicates that the assisted Start routine in the HIM is active and preventing a start.

Bit 7 'RotarySwitch' – Indicates that the rotary switches on the main control board are set to a combination that prevents start.

Bit 8 'Standby' – Indicates that the system is in a low energy (paused) state.

Bit 9 'PLL Not Lock' – Indicates that the line side converter phase locked loop isn't synchronized with the AC line.

Bit 11 'DC Bus High' – Indicates that a DC Bus Overvoltage fault has occurred. Bit 12 'Ovrd Event' – Indicates that the line side converter start is inhibited due to fault, but it can continue running.

Parameter 13:236 - Last Line Side Converter Start Inhibits displays the last condition to inhibit the line side converter from starting and modulating.

Bit 0 'Faulted' – Indicates that a Fault was present. Faults provide notification of events. They prevent the line side converter from modulating.

Bit 1 'Alarm' – Indicates that a Type 2 alarm was present. Type 2 alarms usually indicate a configuration error. They prevent the line side converter from starting and modulating.

Bit 2 'Enable' – Indicates that a digital input was configured for the line side converter Enable function, and it wasn't energized (set).

Bit 3 'Precharge' – Indicates that the line side converter was executing a Precharge.

Bit 4 'Stop' – Indicates that the line side converter was receiving a stop command.

Bit 5 'Database' – Indicates that the database was performing a download operation.

Bit 6 'Startup' – Indicates that the assisted Start routine in the HIM was active and prevented a start.

Bit 7 'RotarySwitch' – Indicates that the rotary switches on the main control board were set to a combination that prevented start.

Bit 8 'Standby' – Indicates that the system was in a low energy (paused) state.

Bit 9 'PLL Not Lock' – Indicates that the line side converter phase locked loop wasn't synchronized with AC line.

Bit 11 'DC Bus High' – Indicates that a DC Bus Overvoltage fault had occurred.

Bit 12 'Ovrd Event' – Indicates that the line side converter start was inhibited due to fault, but it could continue running.

## Low Speed Operation

High IGBT junction temperatures can restrict drive capabilities, particularly at low operating frequencies. One strategy to reduce junction temperature is to reduce switching frequency when operating at low commanded frequencies.

Carrier emulation allows for reduced (f/3) switching frequency operation to be implemented with no change to the actual generated carrier frequency. For instance, carrier emulation allows the drive to operate as if the carrier is 1.33 kHz (4 kHz/3) for a 4 kHz carrier or 667 Hz (2 kHz/3) for a 2 kHz carrier.

This feature is available in all motor control modes except in flux vector control for Interior Permanent Magnet motors (IPM FV) in firmware revisions 6 and later.

This feature is active by default in firmware revision 10 and later.

## Operation

The firmware supports a customer selection of the feature that automatically changes the carrier frequency to a low carrier PWM frequency at low induction motor speeds. This change in carrier frequency is necessary to decrease IGBT junction temperature and to decrease the inverter current derating associated with those low speeds.

The firmware also supports customer adjustment of the output frequency threshold at which the low carrier PWM frequency changes back to the user-selected carrier PWM frequency. Some motors can have too much ripple current at the low carrier PWM frequency, and it's necessary to reduce that region of operation by decreasing the output frequency threshold.

For drives and common bus inverters that are configured for an induction motor control mode, the firmware reduces the inverter carrier PWM frequency to one third of the user-selected value to decrease current derating if the following conditions apply.

- Inverter control parameter 10/11:420 [Mtr Ctrl Config] bit 10 'LoPWM FreqEn' is set.
- Inverter output frequency is less than the value of the inverter control parameter PWM Trans Freq.
- Less than 20% of the user-entered motor nameplate frequency.
- Selected carrier PWM frequency is less than or equal to 4 kHz.

## Configuration

To activate the feature, set parameter 10/11:420 [Mtr Ctrl Config] bit 10 'LoPWM FreqEn' to 1.

<!-- image -->

Double-click parameter 10/11:420 [Mtr Ctrl Config] to open the bit configuration window.

<!-- image -->

Use parameter 10/11:429 [PWM Trans Freq] to set the threshold where the function activates.

Review the example where you set parameter 10/11:429 [PWM Trans Freq] to 5 Hz. When the output frequency is above 5 Hz, the function is inactive and the PWM frequency is whatever you selected in parameter 10/11:425 [PWM Frequency]. When the output frequency drops below 5 Hz, the function activates and reduces the PWM frequency to one third of the value in parameter 10/11:425 [PWM Frequency].

<!-- image -->

The following plot that shows the expected operation. The setup for this plot is the drive is commanded to output 5 Hz and the PWM Trans Freq is set to 5 Hz (this setup is only intended to illustrate the feature). So, when the output frequency dithers around the PWM Trans Freq, the feature is activated and deactivated. There's no hysteresis that is involved, and it does not transition based on a set number of PWM cycles. The transition is instant (you can do one actual carrier followed by one emulated followed by one actual, and so forth).

<!-- image -->

## Performance

The performance bandwidth is reduced in the region of lower carrier frequency. The speed regulator gains are automatically reduced to one third. Transferring between modes did not induce transients on the velocity.

## Current Ripple

There's greater current ripple when the carrier frequency is reduced. Consider this thermally if the motor is to be run for long periods in this state.

## Derating

See the PowerFlex 750-Series Products with TotalFORCE Control Technical Data, publication 750-TD100 for derating curves across product ratings. The following derating curve is for low speed operation. The gold trace is for 4 kHz operation. Let us say the drive is programmed to reduce the carrier frequency if the speed of the motor drops below 10 Hz. The derating at 10 Hz is stated as 87%.

<!-- image -->

|      | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed/Load Derating for IP20, UL Type 1 and IP54, UL Type 12   |                         |                                     |
|------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------|-------------------------------------|
|      | LD                                                                                      | LD                                                                                      | ND HD                                                                                   | ND HD                                                                                   |                                                                                         |                                                                                         |                         | 1.33 kHz 2 kHz 4 kHz                |
|      | Hp                                                                                      | Cont. Amps                                                                              | Hp                                                                                      | Cont. Amps                                                                              | Hp                                                                                      | Cont. Amps                                                                              | Hz 1.33 kHz 2 kHz 4 kHz | 1.33 kHz 2 kHz 4 kHz                |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         | 0 79 72 55              | Frequency (Hz) 10 20 30 40 50 60 70 |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         | 2 100 93 73             | Frequency (Hz) 10 20 30 40 50 60 70 |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         | 4 100 100 81            | Frequency (Hz) 10 20 30 40 50 60 70 |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         | 6 100 100 84            | Frequency (Hz) 10 20 30 40 50 60 70 |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         |                                                                                         |                                                                                         | 8 100 100 86            |                                     |
| D617 | 7 500 617                                                                               | 500                                                                                     |                                                                                         |                                                                                         | 600 400 500                                                                             | 10 100 100                                                                              | 87                      |                                     |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         | 600 400 500                                                                             |                                                                                         | 15 100 100 90           |                                     |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         | 600 400 500                                                                             | 20 100 100 92                                                                           |                         |                                     |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         | 600 400 500                                                                             |                                                                                         | 30 100 100 94           |                                     |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         | 600 400 500                                                                             |                                                                                         | 45 100 100 95           |                                     |
| D617 | 7 500 617                                                                               |                                                                                         |                                                                                         |                                                                                         | 600 400 500                                                                             |                                                                                         | 60 100 100 96           |                                     |

When the carrier frequency is reduced at 10 Hz it becomes 1.33 kHz, which is the gold trace in the reduced carrier derating curve. So, the derating goes from 87% to 100% (no derating) when the carrier is lowered (see the following chart where the Load (%) jumps up at 10 Hz). And for this drive rating the speed would have to get below 2 Hz before any derating is required.

<!-- image -->

|      | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   | 480V AC Power Rating Low Speed Derating with Reduced Carrier Frequency for IP20, UL Type 1 and IP54, UL Type 12   |                                 |                                                   |                              |       |
|------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|---------------------------------------------------|------------------------------|-------|
|      | LD                                                                                                                | LD                                                                                                                | ND HD                                                                                                             | ND HD                                                                                                             |                                                                                                                   |                                                                                                                   | Output Freq. PWM Frequency      | Output Freq. PWM Frequency                        | 0.444 kHz 0.666 kHz 1.33 kHz |       |
|      | Hp                                                                                                                | Cont. Amps                                                                                                        | Hp                                                                                                                | Cont. Amps                                                                                                        | Hp                                                                                                                | Cont. Amps                                                                                                        | Hz 0.444 kHz 0.666 kHz 1.33 kHz |                                                   |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 0 91 88 79                      | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 2 100 100 100                   | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 4 100 100 100                   | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 6 100 100 100                   | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 8 100 100 100                   | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   | 500                                                                                                               |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 10 100 100 100                  | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 15 100 100 100 20 100 100 100   | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 30 100 100 100                  | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       |                                 | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              | 14 15 |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 45 100 100 100                  | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |
| D617 | 7 500 617                                                                                                         |                                                                                                                   |                                                                                                                   |                                                                                                                   |                                                                                                                   | 600 400 500                                                                                                       | 60 100 100 100                  | Frequency (Hz) Load (%) 0  2 4 6 8 10 12  0 20 40 |                              |       |

## Power Loss Ride-through

The power loss ride-through feature is an algorithm that is set to take a specific action when power grid disturbances are detected.

## Power Disturbances

Power disturbances are the deviations of input line voltage and frequency from ideal specifications for short periods of time. Voltage and frequency disturbances are a major concern in many industrial applications. Voltage sags, swells, and frequency disturbances cause equipment malfunction and production interruption. Under certain circumstances, the financial loss is severe and can't be tolerated. International committees have established standards such as IEC-61000-4-34, IEC-61000-4-11, and Semi F47. These standards help the food, textile, and electronic industries to avoid wasteful financial loss and provide guidelines help maintain continued system operation during power disturbances.

## Types of Power Disturbances

What Are the main types of power disturbances and why do they occur?

Voltage sags and short time power losses are the most common power disturbances. A voltage sag is a reduction in voltage for a definite period. It can be symmetrical so the reduction in voltage occurs equally on all three phases. It can be asymmetrical, so the reduction does not occur equally on the three phases. Normal operating conditions such as motor starting and/or transformer inrush current can cause most voltage sags. Proper system design helps to avoid or alleviate voltage sags. Short circuit faults also cause voltage sags if they occur close to the main feeder. Voltage sags can also cause phase angle jumps. Phase angle jumps can affect power electronic converters use of phase angle information for their switching.

A power loss of short duration is a special case of voltage sag. The supply voltage and current drop to zero. A current drop can occur when the power utility interrupts the supply of power. The power utility can decide to shed loads when malfunctions and overcurrent conditions occur. Critical loads switched to emergency backup generators can cause a power loss of several seconds.

## Power Loss Ride-through Requirements

To use power loss ride-through with PowerFlex 755T active front end converters, frames 7…15, requires two additional power sources. A 240V AC UPS to keep the main circuit breaker (MCB) closed and 24V DC to keep the fiber-optic communications with peripheral boards alive.

## Functions and Configuration of the Module

What is the power disturbance module?

The power disturbance module is an algorithm that detects the following abnormal conditions: loss of synchronization, voltage sag, high frequency variation, phase loss, and power loss. You can choose one of the following actions to take when the power disturbance module detects an abnormal condition: 'Ignore', 'Alarm', 'Ride Thru', or 'Fault'. You can't choose 'Ignore' for loss of synchronization. The power disturbance module can also be used as a diagnostics tool for evaluating and recording the abnormal conditions.

Loss of Synchronization

The operation of the AFE relies on accurate detection of the line voltage angle. The power disturbance module continuously monitors detection error. It detects the condition if the error exceeds a certain threshold. Wrong connections and transient conditions on the grid cause loss of synchronization. Transient conditions include the following: power interruption, voltage sag, sudden frequency disturbance, and angle jumping. Loss of synchronization is a critical condition. You can choose from the following actions: 'Ride Thru' or 'Fault'.

## Voltage Sag

A voltage sag is the loss or reduction of grid voltage for a short duration. The time can range from a few milliseconds to a few seconds. The power disturbance module monitors the input voltage in real time. It detects a voltage sag condition when the voltage of one or more phase drops by more than 50% of its nominal value. You can choose from the following actions: 'Ignore', 'Alarm', 'Ride Thru', or 'Fault'.

## High Frequency Variation

The operation of the AFE relies on a stable input frequency. The power disturbance module monitors the rate of change of frequency against time. It detects a high frequency variation condition when the frequency change against time exceeds 100 Hertz per second. You can choose from the following actions: 'Ignore', 'Alarm', 'Ride Thru', or 'Fault'.

## Phase Loss

The operation of the AFE relies on a balanced supply. The power disturbance module monitors the current of each incoming phase. It detects a phase loss condition when the current on any of the phases drops too low. You can choose from the following actions: 'Ignore', 'Alarm', 'Ride Thru', or 'Fault'.

## Power Loss

The power disturbance module monitors the root mean square (RMS) values of the input line voltages. It detects a power loss condition when the RMS voltage of the three input phases drops to less than 15% of the nominal value. You can choose from the following actions: 'Ignore', 'Alarm', 'Ride Thru', or 'Fault'.

## Ride Thru Mode

Ride Thru mode is one of the selectable actions available when the power disturbance module detects abnormal conditions. Ride Thru mode temporarily disables PWM gating of the IGBTs in the line side converter. This avoids instability and reduces the probability of fault. It also preserves the energy in the DC bus capacitors. It can support the load for a short time. Because the fly back diodes remain in circuit, the Line Side Converter behaves like a passive diode bridge. Ride Thru disables the voltage and current loops. It also resets the voltage and current integrators.

The flow diagram in Figure 1 illustrates the operation of Ride Thru mode. The Power Disturbance module continuously monitors the incoming voltages and currents and frequency. When it detects an abnormal condition, it follows the Disturbance Action. If the selected Disturbance Action is 'Ride Thru', it disables PWM gating and the control loops. When the abnormal condition clears (voltages, current and frequency return to normal), the control loops and PWM gating resume. If the abnormal condition lasts longer than the time in the Ride Thru Time parameter, the product follows the selection in the Ride Thru Expired Action parameter.

Figure 1 - Flow Diagram for Ride Thru Mode

<!-- image -->

Figure 2 is a set of oscilloscope traces from an actual test. In this test, we've induced a power loss condition. We have set parameters 13:181 [PLL LOS Det Actn] to 0 'Ride Thru', 13:170 [PwrLoss Det Actn] and 13:173 [VltgSag Det Actn] to 2 'Ride Thru' in the Line Side Converter. We've selected 'Coast' for the Ride Thru option in the Motor Side Inverter.

Figure 2 - Power Loss Test

<!-- image -->

Rockwell Automation's patented technology provides fast detection of the voltage sag. Notice that the Line Side Converter is disabled as soon as the condition is detected. When the DC bus voltage falls below the threshold for motor side inverter power loss, the motor begins to coast. Motor speed falls. When the Power Loss condition clears, the line side converter resumes operation. When the DC bus voltage recovers, the motor side inverter starts and accelerates the motor back to speed.

## Ride Thru Mode—PowerFlex 755TL and 755TR Drives

PowerFlex 755TL and TR drives are 'integrated'. This means they have a Line Side Converter and a Motor Side Inverter. These drives use Rockwell Automation Adaptive Bus Reference Ride Thru technology (patent pending). The Line Side Converter is disabled when the abnormal condition is detected. If the Ride Thru option is selected, an additional signal passes from the Line Side Converter to the Motor Side Inverter. When the signal is high, the Motor Side Inverter takes control of the DC bus. The DC bus regulator in the Motor Side Inverter can take energy from the load, if necessary, to keep the DC bus voltage high enough. When the abnormal condition ceases, control passes back to the Line Side Converter.

Figure 3 is a set of oscilloscope traces from an actual test. In this test, we've induced a power loss condition. We have set parameters 13:181 [PLL LOS Det Actn] to 0 'Ride Thru', 13:170 [PwrLoss Det Actn] and 13:173 [VltgSag Det Actn] to 2 'Ride Thru' in the Line Side Converter. We have set parameters 10/11:116 [Bus Reg Mode A] to 1 'Adjust Freq', 10/11:270 [Pwr Loss Actn] to 1 'Alarm', 10/11:271 [Pwr Loss Mode A] to 1 'Decel', 10/11:272 [Pwr Loss A Level] to 50V and 10/11:273 [Pwr Loss A Time] to 60 seconds in the Motor Side Inverter. The duration of the power loss in this test was about ten seconds.

Figure 3 - Ride Thru Test with Integrated Drive

<!-- image -->

The Power Disturbance Module detected the power loss and disabled the Line Side Converter. The Motor Side Inverter took control of the DC bus. It drew energy from the inertia of the load by adjusting the output frequency. The Line Side Converter resumed control when power was restored. Then the Motor Side Inverter accelerated the motor back up to speed.

## Configure The Power Disturbance Module

The best configuration depends on the application and common conditions on the local electrical grid. If the load inertia is high and the application does not tolerate stoppage, 'Ride Thru' might be the best configuration. If the application can tolerate slight disturbances in velocity, 'Ride Thru' might be the best configuration.

In cases where voltage imbalance conditions are common on the grid, it might be best to set parameter 13:181 [PLL LOS Det Actn] to 0 'Ride Thru' and to increase parameter 13:192 [BasicPLL Err Lmt].

In cases where power outages and voltage sags are common on the grid, it might be best to set parameters 13:181 [PLL LOS Det Actn] to 0 'Ride Thru', 13:170 [PwrLoss Det Actn] and 13:173 [VltgSag Det Actn] to 2 'Ride Thru'.

## Auxiliary Power Supply

## Motor Control Modes

Auxiliary power can be used to power the drive's control circuitry in the event the incoming supply is removed or lost. For PowerFlex 755TR, 755TL, and 755TM products, connect a user supplied 24V DC auxiliary power source to the designated terminal block.

For PowerFlex 755TS products, an optional power supply module, 20-750-TAPS-XT, must be used. This power supply module is designed to power all peripherals, I/O, and connected feedback devices. The 20-750-APS power supply module isn't compatible because it does not supply enough power.

When the drive is connected to a user supplied 24V DC power source, the communication network functions remain operational and online. If DeviceLogix is used, the program can also continue to run and control any associated input and outputs.

See the Apply and Remove Power section of the PowerFlex Drives with TotalFORCE Control Programming Manual, publication 750-PM101, for the correct power-up sequence when using auxiliary power.

The PowerFlex 750-Series Products with TotalFORCE support the configuration of two motor control profiles, primary and secondary, which provides application flexibility. Each profile can be configured for any of the motor control modes regardless of how the other profile is configured. The only exception is None (0) which can only be selected for the secondary control profile. See Secondary Motor Control on page 60 for more information on this functionality.

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] select the motor control mode for ports 10 (primary) and 11 (secondary) in the drive. The default selection for 0:65 [Pri MtrCtrl Mode] is 2 'Induction SV' and for 0:67 [Sec MtrCtrl Mode] is 0 'None'. Set these two parameters and cycle power to the drive before performing further commissioning steps.

A change to the motor control mode and power cycle reconfigures which parameters are visible in port 10 (primary) and port 11 (secondary). This helps to reduce configuration time by only showing those parameters that are applicable for the selected motor control mode. The parameter settings follow.

None (0) – This setting is only valid for 0:67 [Sec MtrCtrl Mode]. When set to none, port 11 (secondary) isn't visible. Used when secondary motor control functionality isn't required.

InductionVHz (1) – Induction motor, volts per Hertz control mode. Connected to an induction motor. Commonly used for variable torque applications like centrifugal pumps and fans for improved efficiency and energy savings, or for variable speed constant torque applications such as conveyors. Can also be used for synchronous motor applications. This is the only motor control mode capable of running multiple motors with one drive.

Induction SV (2) – Induction motor, sensorless vector control mode. Connected to an induction motor. Used for most constant torque applications. Provides excellent starting, acceleration, and running torque even at lower speeds.

Induct Econ (3) – Induction motor, economize control mode. Used for additional energy savings in constant torque applications that have constant speed reduced load periods.

Induction FV (4) – Induction motor, flux vector control mode. Connected to an induction motor. Used when high-performance precise speed regulation and/or position control closed loop is required. Can also be configured with direct Torque Reference input. Capable of being used open loop with less precision.

IPM FV (5) – Interior permanent magnet motor, flux vector control mode. Connected to an Interior Permanent Magnet motor. Used when high-performance precise speed regulation and/or position control with closed loop feedback is required. Can also be configured with direct Torque Reference input. Capable of being used open loop with less precision.

SPM FV (6) – Surface permanent magnet motor, flux vector control mode. Connected to a Surface Permanent Magnet motor. Used when high-performance precise speed regulation

and/or position control closed loop is required. Can also be configured with direct Torque Reference input. Capable of being used open loop with less precision.

PM VHz (7) – Permanent magnet motor, volts per Hertz control mode. Connected to a Surface Permanent Magnet motor (SPM) or Permanent Magnet Synchronous Motor (PMSM). Used for variable torque applications with improved efficiency energy savings and variable speed constant torque applications such as conveyors. Also used in multi-motor or synchronous motor open loop applications.

PM SV (8) – Permanent magnet motor, sensorless vector control mode. Connected to a Surface Permanent Magnet motor (SPM) or Permanent Magnet Synchronous Motor (PMSM). Used for constant torque applications. Provides excellent starting, acceleration, and running torque.

SynR VHz (9) – Synchronous Reluctance motor, volts per Hertz control mode. Connected to a Synchronous Reluctance motor. Used for constant torque applications with improved efficiency energy savings and variable speed applications such as conveyors. Can also be used in multi-motor applications.

SynR SV (10) – Synchronous Reluctance motor, sensorless vector control mode. Connected to a Synchronous Reluctance motor. Used for constant torque applications with improved efficiency energy savings and variable speed applications such as conveyors. Avoid slow speed low-inertia applications that cause torque ripple effects.

There are four basic control methods available in the drive. These methods are Volts/Hertz, Sensorless Vector, Economize, and Flux Vector. While the basic operation of each of these methods is the same regardless of the motor type being used, it's important to select the motor control mode for the type of motor being used because the motor data required by the algorithms can vary.

## Volts/Hertz

Volts/Hertz is the simplest form of AC motor control. Volts per Hertz can be used with induction motors (Induction VHz), permanent magnet motors (PM VHz), and synchronous reluctance motors (SyncRel VHz). Volts per Hertz is ideal for variable torque applications like centrifugal pumps and fans. This mode can also be used when running multiple motors on one drive. Volts/Hertz operation creates a fixed relationship between output voltage and output frequency. This is known as a scaler control method because voltage is scaled based on frequency. The relationship can be defined in two ways by setting 10/11:486 [VHz Curve] to 0 'Custom V/Hz' or 1 'Fan/Pump'. Motor autotune tests aren't required in this mode.

Figure 4 - Volts/Hertz

0 = 'Custom V/Hz'

<!-- image -->

Custom Volts/Hertz enables a wide variety of patterns using linear segments. The default configuration produces nearly a straight line from zero to rated voltage and frequency. This is the same volts/hertz ratio that the motor sees if started across the line. As seen in the

diagram below, the volts/hertz ratio can be changed to provide increased torque performance when required by programming five distinct points on the curve.

10/11:480 [Start Acc Boost] - Used to create additional torque for breakaway from zero speed and acceleration of heavy loads at lower speeds.

10/11:481 [Run Boost] - Used to create additional running torque at low speeds. The value is typically less than the required acceleration torque. The drive will lower the boost voltage to this level when running at low speeds (not accelerating). This reduces excess motor heating that could be caused if the higher start/accel boost level were used.

10/11:483 [Break Voltage] and 10/11:484 [Break Frequency] - Used to increase the slope of the lower portion of the Volts/Hertz curve, providing additional torque.

10/11:400 [Motor NP Volts] and 10/11:402 [Motor NP Hertz] - Set the upper portion of the curve to match the motor design. Marks the beginning of the constant power region.

10/11:421 [Maximum Voltage] and 10/11:422 [Maximum Freq] - Slope the portion of the curve used above base speed.

Frequency

<!-- image -->

## 1 = 'Fan/Pump'

When this option is chosen, the basic relationship is % Voltage = % Frequency2 y2 . At rated frequency, full voltage is supplied. At 50% rated frequency, 25% voltage is applied. This parabolic curve closely matches the torque requirement of a variable torque load (centrifugal fan or pump - load increases as speed increases) and offers the best energy savings for these applications by programming three distinct points on the curve.

10/11:481 [Run Boost] - Used to create additional running torque at low speeds. The value is typically less than the required acceleration torque. The Fan/Pump curve does not use 10/ 11:480 [Start Acc Boost] and therefore uses 10/11:480 [Run Boost] regardless of whether the drive is running at speed or accelerating.

10/11:400 [Motor NP Volts] and 10/11:402 [Motor NP Hertz] - Set the upper portion of the curve to match the motor design. Marks the beginning of the constant power region.

10/11:421 [Maximum Voltage] and 10/11:422 [Maximum Frequency] - Slope the portion of the curve used above base speed.

<!-- image -->

## Sensorless Vector

Sensorless Vector mode uses a V/Hz core enhanced by a torque current estimator, a high performance current limiter, and voltage vector algorithms. Sensorless Vector can be used with induction motors (Induction SV), permanent magnet motors (PM SV) and synchronous reluctance motors (SyncRel SV) however, permanent magnet and synchronous reluctance motors do not require slip frequency adjustments. Sensorless Vector is good for constant torque applications that do not require high levels of precision. In this mode, a torque estimator is used to provide a better slip estimate and as an input to the voltage vector algorithms to produce better torque output at low speed. Motor data and motor auto tune tests are required for proper operation in this mode.

Figure 5 - IM Sensorless Vector

<!-- image -->

Figure 6 - PM SyncRel Sensorless Vector

<!-- image -->

The Sensorless Vector algorithms operate on the knowledge that motor current is the vector sum of the torque and flux producing components of current. Values can be entered to identify

the motor values or an autotune routine can be run to identify the motor values. Sensorless vector offers better torque production and a wider speed range than V/Hz. Although Sensorless Vector is still a V/Hz motor control method, it is not appropriate to use when more than one motor is connected to the same drive.

In Sensorless Vector control, the drive commands a specific amount of voltage to develop flux.

(1) During a motor autotune, the drive measures this voltage drop and stores the equivalent resistance in 10/11:512 [u IM Stator Res].

<!-- image -->

## Economize

Economize mode consists of the Sensorless Vector control with an additional energy savings function. Economize can only be used with induction motors (Induction Econ). When steady state speed is achieved, the economizer becomes active and automatically adjusts the drive output voltage based on applied load. By matching output voltage to applied load, the motor efficiency is optimized. As the load is reduced, the drive reduces motor flux current. The flux current is reduced if the total drive output current is less than 75% of motor rated current as programmed in 10/11:401 [Motor NP Amps]. The flux current can only be reduced to 50% of the motor flux current as programmed in 10/11:517[c Flux Cur Ref] or 10/11:518[u Flux Cur Ref]. During acceleration and deceleration, the economizer is inactive and Sensorless Vector motor control performs normally. Motor data and a motor autotune is required for correct operation in this mode.

<!-- image -->

## Flux Vector Control

In Flux Vector mode, the flux and torque producing currents are independently controlled and speed is indirectly controlled by a torque reference. Alternatively, the drive can control torque instead of speed in flux vector mode. In either case, this mode can be operated either with or without feedback and will provide the fastest response to load changes.

Flux Vector control can be used with inductions motors (Induction FV), surface permanent magnet motors (SPM FV) and interior permanent magnet motors (IPM FV). Flux Vector is the highest performance motor control method. Motor data and a motor auto tune is required for

correct operation in this mode. In Flux Vector control, the drive takes the speed reference that is specified by the Speed Reference Selection block and compares it to the speed feedback. The speed regulator uses Proportional and Integral gains to adjust the torque reference for the motor. This torque reference attempts to operate the motor at the specified speed. The torque reference is then converted to the torque producing component of the motor current.

This type of speed regulator produces a high bandwidth response to speed command and load changes. Because Flux Vector controls the flux and torque producing currents independently, a torque reference can be sent directly instead of being generated from a speed reference via the Speed Regulator. The independent flux control also enables flux to be reduced when running above base motor speed.

Figure 7 - Flux Vector—Closed Loop

<!-- image -->

Figure 8 - Flux Vector—Open Loop

<!-- image -->

## Motor Types

The following explanation and descriptions of AC motor types are condensed summaries derived from a variety of sources that focus on the history, evolution, and feature benefits of the variety of motor designs. These designs are utilized in all sectors of use and in vast variations of machinery, equipment, and processes.

The types of AC motors described here, powered by fixed utility frequency, are limited to speeds based on the number of poles and winding construction. Variable Frequency Drives (VFDs) broaden practical speed ranges of these motor types by converting utility power and applying appropriately selected VFD electronic control modes specifically matched to these unique motor type designs.

The PowerFlex 750-Series Products with TotalFORCE Control can store two motor control profiles: primary and secondary. Each profile can be configured independently. For detailed information about how to configure these motor control profiles, see Motor Control Modes on page 38 .

The following topics are briefly discussed in this section.

- Basics of AC Motor Design
- Induction AC Motors
- Wound-rotor AC Motors
- Multispeed AC Motors
- Synchronous AC Motors
- Permanent Magnet Motor Control
- Synchronous reluctance motors

## Basics of AC Motor Design

AC motors come in a variety of designs, each with functional purpose and benefits. Asynchronous and synchronous electric motors are the two main categories of AC motors.

The Induction AC motor is a common form of asynchronous motor and is basically an AC transformer with a rotating secondary. The primary winding (stator) is connected to the power source and the shorted secondary (the rotor) carries the induced secondary current. Torque is produced by the action of the rotor (secondary) currents on the air-gap flux. The synchronous motor differs greatly in design and operational characteristics and is considered a separate class of AC motor.

## Induction Motors

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following induction motor options.

- 1 = 'InductionVHz'
- 2 = 'Induction SV'
- 3 = 'Induct Econ'
- 4 = 'Induction FV'

Induction Motors are the simplest and most rugged electric motor and consist of two basic electrical assemblies: the wound stator and the rotor assembly. The induction AC motor derives its name from currents flowing in the secondary member (rotor) that are induced by alternating currents flowing in the primary member (stator). The combined electromagnetic effects of the stator and rotor currents produce the force to create rotation.

ACIMs typically feature rotors, which consist of a laminated, cylindrical iron core with slots for receiving the conductors. The most common type of rotor has cast-aluminum conductors and short-circuiting end rings. This AC motor "squirrel-cage" rotates when the moving magnetic field induces a current in the shorted conductors. The speed at which the AC motor magnetic field rotates is the synchronous speed of the AC motor and is determined by the number of poles in the stator and the frequency of the power supply: ns = 120f/p, where ns = synchronous

speed, f = frequency, and p = the number of poles (that is 120*60 Hz] / 4 = 1800 RPM). To control motor speed other than the fixed utility frequency requires a variable frequency drive (VFD).

Synchronous speed is the rated speed for the rated torque. If the AC motor's rotor turns exactly as fast as the rotating magnetic field, then no lines of force are cut by the rotor conductors, and torque is zero. When AC induction motors are running, the rotor always rotates slower than the magnetic field. The AC motor's rotor speed is just slow enough to cause the proper amount of rotor current to flow, so that the resulting torque is sufficient to overcome windage and friction losses, and drive the load. The speed difference between the AC motor's rotor and magnetic field, called slip, is normally referred to as a percentage of synchronous speed: s = 100 (ns - na)/ns, where s = slip, ns = synchronous speed, and na = actual speed. Or it is listed on the nameplate as a base speed (1780 RPM) at rated FLA, frequency, and based on the number of poles.

## Polyphase AC Induction Motors

Polyphase squirrel-cage AC motors are basically constant-speed machines, but some degree of flexibility in operating characteristics results from modifying the rotor slot design. These variations in AC motors produce changes in torque, current, and full-load speed. Evolution and standardization have resulted in four fundamental types of AC motors.

There are five basic NEMA designs for AC motors: A, B, C, D, and F. The speed- torque curves for all five designs are shown on the following graph.

Speed - Torque Curves of NEMA A, B, C, D, and F Motors

<!-- image -->

AC Motors - Designs A and B are general-purpose AC motors with normal starting torques and currents and low slip. As shown, the characteristics of designs A and B are quite similar. The primary difference between these two designs is that the starting current for design B is limited by NEMA standards, but there is no limitation on the starting current for design A.

AC Motors - Design C have high starting torque with normal starting current and low slip. NEMA design C motor has a higher starting torque than either the A or B designs. This torque is in the vicinity of 225% of full-load torque. Design C AC motors are normally used where breakaway loads are high at starting, but which normally run at rated full load and are not subject to high overload demands after running speed has been reached.

AC Motors - Design D exhibit high slip AC motor starting torque, which is approximately 280% of full-load torque, low starting current, and low full-load speed. Because of the high slip,

speed can drop when fluctuating loads are encountered. The high starting torque of the design D motor makes it particularly suited to handle hard-to-start loads. Another useful characteristic of this motor is the sloping shape of its speed-torque curve. This lets the motor slow down during periods of peak loads, enabling any flywheel energy that has been stored by the load to be released. Typical applications include punch presses and press brakes.

AC Motors - Design F exhibit low starting torque, low starting current, and low slip. These AC motors are built to obtain low locked-rotor current. Both locked- rotor and breakdown torque are low. Normally these AC motors are used where starting torque is low and where high overloads are not imposed after running speed is reached.

In summary, we see that when matching an AC motor to the requirements of a specific load it is important to check the torque requirements of the load and the torque capabilities of the motor in addition to speed and horsepower.

At least three torque values are important:

- Starting torque
- Breakdown torque
- Full-load torque

## Wound-rotor AC Motors

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following induction motor options.

- 1 = 'InductionVHz'
- 2 = 'Induction SV'
- 4 = 'Induction FV'

Squirrel-cage AC motors are relatively inflexible with regard to speed and torque characteristics, but a special wound-rotor AC motor has controllable speed and torque. Application of wound-rotor AC motors is markedly different from squirrel-cage AC motors because of the accessibility of the rotor circuit. AC motor performance characteristics are obtained by inserting different values of resistance in the rotor circuit.

Wound-rotor AC motors are generally started with secondary resistance in the rotor circuit. The AC motor resistance is sequentially reduced to permit the motor to come up to speed. Thus, AC motors can develop substantial torque while limiting locked-rotor current. This secondary AC motor resistance can be designed for continuous service to dissipate heat produced by continuous operation at reduced speed, frequent acceleration, or acceleration with a large inertia load. External resistance gives AC motors a characteristic that results in a large drop in rpm for a fairly small change in load. Reduced AC motor speed is provided down to about 50% rated speed, but efficiency is low.

Retrofitting a Wound-rotor motor with a VFD is possible by eliminating the switching and resistor control infrastructure and shorting the slip rings connected to the rotor windings.

## IMPORTANT

Because wound-rotor motors were not originally designed for use with inverters, the dielectric strength of the motor construction cannot withstand the reflected wave voltages that can get subjected at the motor connections (1.5 to 2.5 times drive's bus voltage).

Appropriate mitigation must be considered. General rule of thumb, size the VFD so that it can provide continuous current at 125 to 135% of FLA of the motor, due to elimination of resistors and its design for higher starting torque.

## Multi-speed AC Motors

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following induction motor options.

- 1 = 'InductionVHz'
- 2 = 'Induction SV'
- 4 = 'Induction FV'

Consequent-pole AC motors are designed for one speed. By physically reconnecting the leads, a 2:1 speed ratio can be obtained. Typical synchronous speeds for 60 Hz AC motors are: 3,600/ 1,800 rpm (2/4 pole), 1,800/900 rpm (4/8 pole), and 1,200/600 rpm (6/12 pole).

Two-winding AC motors have two separate windings that can be wound for any number of poles so that other speed ratios can be obtained. However, ratios greater than 4:1 are impractical because of AC motor size and weight.

Power output of multispeed AC motors can be proportioned to each different speed. These AC motors are designed with output horsepower capacity in accordance with one of the load characteristics.

When retrofitted with a VFD, the motor is generally wired for the speed range intended to be optimized. Autotuned per representative nameplate information and operated as a single winding single speed induction motor.

## Synchronous AC Motors

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following induction motor options.

- 1 = 'InductionVHz'

Synchronous AC motors are inherently constant-speed electric motors, and they operate in absolute synchronism with line frequency. As with squirrel-cage induction AC motors, speed is determined by the number of pairs of poles and is always a ratio of the line frequency.

Synchronous AC motors are made in sizes ranging from sub-fractional self- excited units to large-horsepower, direct-current-excited AC motors. In the fractional-horsepower range, synchronous AC motors are used primarily where precise constant speed is required.

In large horsepower sizes applied to industrial loads, synchronous AC motors serve two important functions. First, AC motors provide highly efficient means of converting AC energy to mechanical power. Second, AC motors can operate at leading or unity power factor, thereby providing power-factor correction.

There are two major types of synchronous AC motors: non-excited and direct- current excited electric motors. Application of a VFD is to vary the desired synchronous speed of the machine.

## Permanent Magnet Motor Control

Permanent magnet motor control is selected by setting parameter 0:65 [Pri MtrCtrl Mode] and/ or 0:67 [Sec MtrCtrl Mode] to the appropriate choices of motor type.

Motor data and an autotune are required for correct operation in these modes. For detailed information about how to use each of these features, see the PowerFlex 755T Flux Vector Tuning Application Technique, publication 750-AT006 .

## Surface Permanent Magnet Motor (SPM) or Permanent Magnet Synchronous Motor (PMSM)

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following surfacemounted permanent magnet motor options.

- 6 = 'SPM FV'
- 7 = 'PM VHz'
- 8 = 'PM SV'

SPM or PMSM is a rotating electrical machine that has the stator phase windings and rotor permanent magnets. The air gap magnetic field is provided by these permanent magnets therefore it remains constant.

The conventional DC motor commutates itself with the use of a mechanical commutator whereas SPM / PMSM needs electronic commutation for the direction control of current through the windings. Because the SPM/PMSM motors in effect have their armature coils at the stator, they need to be commutated externally with the help of an external switching circuit. A three phase PWM inverter (VFD) topology is used for this purpose.

The torque is produced because the interaction of the magnetic fields causes the rotor to rotate. In permanent magnet motors, one of the magnetic fields is created by permanent magnets and the other is created by the stator coils. The maximum torque is produced when the magnetic vector of the rotor is at 90 degrees to the magnetic vector of the stator.

The permanent magnet synchronous motor (PMSM) can be thought of as a cross between an AC induction motor and a brushless DC motor (BLDC). They have rotor structures similar to BLDC motors which contain permanent magnets. However, their stator structure resembles that of an AC induction motor, where the windings are constructed in such a way as to produce a sinusoidal flux density in the air gap of the machine. As a result, they perform best when driven by sinusoidal waveforms. However, unlike their ACIM relatives, PMSM motors perform poorly with open-loop scalar V/Hz control, because there is no rotor coil to provide mechanical damping in transient conditions.

PMSM motors provide higher power density for their size compared to ACIMs. This is because with an induction machine, part of the stator current is required to "induce" rotor current in order to produce rotor flux. These additional currents generate heat within the motor. In a PMSM, the rotor flux is already established by the permanent magnets on the rotor.

Field Oriented Control is the most popular control technique used with PMSMs. As a result, torque ripple can be extremely low, on par with that of ACIMs. Most PMSMs utilize permanent magnets which are mounted on the surface of the rotor. This makes the motor appear magnetically "round," and the motor torque is the result of the reactive force between the magnets on the rotor and the electromagnets of the stator. This results in the optimum torque angle being 90 degrees, which is obtained by regulating the d-axis current to zero in a typical FOC application.

## Interior Permanent Magnet Motor

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following interior permanent magnet motor option.

- 5 = 'IPM FV'

Some PMSMs have magnets that are buried inside of the rotor structure. These motors are called Interior Permanent Magnet, or IPM motors. As a result, the radial flux is more concentrated at certain spatial angles than it is at others. This gives rise to an additional torque component called reluctance torque, which is caused by the change of motor inductance along the concentrated and non- concentrated flux paths.

This causes the optimum Field Oriented Control torque angle to be greater than 90 degrees, which requires regulating the d-axis current to be a fixed negative ratio of the q-axis current.

This negative d-axis current also results in field weakening, which reduces the flux density along the d-axis, which in turn partially lowers the core losses. As a result, IPM motors boast even higher power output for a given frame size.

These motors are becoming increasingly popular as traction motors in hybrid vehicles, as well as variable speed applications for appliances and HVAC. In the servo motor world, more and more designs are shifting away from SPM to IPM to take advantage of inherent advantages. In principle, there are no size limitations to IPM designs and these can be developed from small fractional horsepower to large – hundreds of Hp ratings, creating potential applications that can benefit from variable speed IPM control.

## Synchronous Reluctance Motors

Parameters 0:65 [Pri MtrCtrl Mode] and 0:67 [Sec MtrCtrl Mode] have the following synchronous reluctance motor option.

- 9 = 'SynR VHz'
- 10 = 'SynR SV'

Synchronous reluctance motors have an equal number of stator and rotor poles. The projections on the rotor are arranged to introduce internal flux "barriers," holes which direct the magnetic flux along the so-called direct axis. Typical numbers of poles are 4 and 6.

As the rotor is operating at synchronous speed and there are no current- conducting parts in the rotor, rotor losses are minimal compared to those of an induction motor, thus potential energy savings in appropriate applications. Once started and rotating at synchronous speed, the motor can operate with sinusoidal voltage. So, to start and control speed at frequencies other than utility requires a variable-frequency drive.

## Selecting Velocity Feedback

The PowerFlex 750-Series Products with TotalFORCE Control support the selection of two feedback sources: primary source and alternate source.

Parameter 10/11:1000 [Pri Vel Fb Sel] selects the port and parameter of the feedback channel to be the primary source of motor velocity feedback. This becomes the source for parameters 10/11:1044 [Motor Vel Fb] and 10/11:1042 [Vel Fb Active].

Parameter 10/11:1006 [Alt Vel Fb Sel] selects the port and parameter of the feedback channel to be the alternate source of motor velocity feedback. This becomes the source for parameters 10/11:1044 [Motor Vel Fb] and 10/11:1042 [Vel Fb Active] when an 'Automatic Switchover' has occurred.

Parameters 10/11:1000 [Pri Vel Fb Sel] and 10/11:1006 [Alt Vel Fb Sel] become available in the Flux Vector (FV) selections of the motor control modes.

## Feedback Modes

The PowerFlex 750-Series Products with TotalFORCE Control provide several feedback modes depending on the selection of the parameter 0:65 [Pri MtrCtrl Mode] (and the parameter 0:67 [Sec MtrCtrl Mode] if this parameter isn't set to 'None'). This parameter is only editable on the Dynamic Features Page.

Possible selections include: 10/11:1048 [Open Loop Fb], 10/11:1050 [Simulator Fb], and any port that contains a feedback module (for example, Encoder). The selection of 'Simulator Fb' is useful for drive operational checkout and test when motor movement is undesired. In simulation mode, gating of the power inverter section of the drive is disabled.

## Automatic Feedback Loss Switchover

The PowerFlex 750-Series Products with TotalFORCE Control are featured with 'Automatic Feedback Loss Switchover' functionality. Parameter 10/11:1019 [Fb Loss Action] selects the mode of the Feedback Loss Switchover function.

Parameter 10/11:1019 [Fb Loss Action] options include:

- 0 = 'Primary Only' – Use primary feedback source exclusively
- 1 = 'Alt Only' – Use alternate feedback source exclusively
- 2 = 'Auto Tach SW' – Switch from primary to alternate upon loss of primary

## Adaptive Control

## TotalFORCE Control Features

This chapter discusses common control topographies used with PowerFlex® products.

| Topic Page                            |
|---------------------------------------|
| Adaptive Control 51                   |
| CIP Security 59                       |
| Secondary Motor Control 60            |
| Energy Pause Function 63              |
| Predictive Maintenance 67             |
| Predictive Maintenance CIP Objects 79 |
| DeviceLogix 86                        |
| Emergency Override Function 94        |
| Reference Motion Planners 97          |

A brief overview of Load Observer, Adaptive Tuning, and Autotune is provided in this section. For detailed information about how to use each of these features, see the PowerFlex 755T Flux Vector Tuning Application Technique, publication 750-AT006 .

## Load Observer

The load observer feature is a control loop inside the drive that estimates the mechanical load on the motor and compensates for it while the drive is running. This feature allows high performance and control loop tuning simplicity similar to that of a mechanically disconnected motor. Its primary function is to:

- Automatically compensate for unknown inertia, compliance, and low frequency resonance
- Automatically compensate for disturbances and changes in inertia
- Force consistent dynamic behavior, which makes the drive easier to tune

## Benefits

You can use load observer with out-of-box control loop gains, where the load is unknown or compliant and thus 10/11:901 [Load Ratio] = 0. You can also use load observer with autotuned control loop gains where 10/11:901 [Load Ratio] &gt; 0. This value can be a known positive value or one that is calculated by performing an autotune procedure.

When load observer is enabled with the recommended out-of-box control loop gains:

- A tuning expert is not needed
- Commissioning time is reduced, especially for high drive count
- Relatively high performance control is provided without tuning
- Changes in inertia, compliance, and low frequency resonances are compensated for automatically
- Periodic retuning to account for machine wear over time is not needed

When load observer is enabled with autotuned control loop gains:

- Load disturbances are compensated for automatically
- Tracking errors, machine vibration, and power consumption are minimized
- Bandwidth and line speeds can be increased
- Tighter control of moving parts reduces wear and saves material costs

<!-- image -->

## Adaptive Tuning

The adaptive tuning feature is an algorithm that continuously monitors and, if necessary, adjusts filter parameters and control loop gains to compensate for unknown and changing load conditions. Adaptive tuning performs the following functions:

- Monitors motor-side resonances
- Automatically adjusts torque loop notch and low pass filter parameters to suppress resonances
- Automatically tunes control loop gains to avoid instability

## Benefits

When you enable adaptive tuning with the recommended out-of-box control loop settings, you do not need a tuning expert. You also gain the following benefits:

- Reduced commissioning time, especially for high drive count
- Automatically suppressed continuously changing resonances
- Periodic identification of resonances and retuning is not needed
- Periodic retuning of filters is not needed
- Minimized tracking errors, machine vibration, and power consumption
- Increased bandwidth and line speeds
- Tighter control of moving parts reduces wear and saves material costs

## Autotune

The Autotune function is used to measure motor characteristics. It is composed of several individual tests, each of which is intended to adjust one or more motor parameters. These tests require you to enter motor nameplate information into the drive parameters. Although you can change some of the parameter values manually, measured values can provide improved performance. Autotuning is often unnecessary when you apply Load Observer with the recommended default settings.

## Position and Velocity Regulators

The PowerFlex 755T utilizes a series form of a Proportional-Integral (PI) controller for the Position Regulator (PReg) and the Velocity Regulator (VReg). The proportional and integral gains are expressed in units of Hz. The proportional gains have been normalized by removing inertia and represent bandwidth which is a readily understood and measurable value. Relating the proportional gains to bandwidth makes the tuning experience more intuitive.

## Figure 9 - Regulator Schemes

<!-- image -->

The recommended method for tuning the position and velocity regulators is adjusting the System Bandwidth parameter 10/11:906 [System BW]. By adjusting the System bandwidth, the proportional and integral gains for the position and velocity regulators are automatically calculated, which eliminates the need to adjust each gain individually. For more information on the Position and Velocity regulators and how to tune them, refer to the PowerFlex 755T Flux Vector Tuning Application Technique, publication 750-AT006 .

Volt Reg C/U Sel Selector:

0- Calculated

1- User Entered

<!-- image -->

## Bus Observer

The bus observer feature is available in the PowerFlex 755TM regenerative bus supplies and the PowerFlex 755TL low harmonic and 755TR regenerative products. Bus observer was added to compensate for unknown capacity changes in the system demand. Enhanced DC bus voltage regulation and repeatability of control loop performance in the presence of unknown AC line conditions are the main goals of the bus observer, rather than command tracking, which allows for lower gain settings. Bus observer performs the following functions:

- Enhances the regulation of the DC bus voltage control.
- Compensates for unknown capacity changes in the system demand.
- Compensates for the external connected capacitance that is less than three times the bus supply.
- Uses current feedback to feed forward the bus voltage regulator.

PowerFlex 755TL/TR drives use power feed forward to enhance the DC bus regulation. The inverter load is fed forward into the converter to improve DC bus voltage regulation.

When the bus observer is not used, higher gain settings are required for a sufficiently robust system. Higher gain settings cause heating of the inductors and capacitor resonance trips. The accuracy of the total bus capacitance that is entered directly affects overall performance.

Example: The bandwidth = 400 Hz with bus observer disabled. However, the bandwidth = 150 Hz with bus observer enabled for equivalent DC bus voltage regulation with lower inductor temperatures.

## Bus Observer Limitations

- If the external capacitance is greater than three times the supply, DC bus regulation can become unstable.
- Do not enter an external capacitance value greater than what is connected or stability can be affected. It is recommended to use the lowest estimated value. Bus observer can compensate for increased line capacitance, but it cannot reduce line capacitance.
- Cannot be enabled or disabled while the converter is active (running).

Figure 10 and Figure 11 show the Bus Observer function.

Figure 10 - Voltage Control (VoltCtrl) Block Diagram

Figure 11 - DC Bus Observer Block Diagram

Total Sys Cap

<!-- image -->

## Feed Forward Power

Feed forward power is a drive function that you can use to improve DC bus voltage regulation in response to changes in the load on the inverter section of the drive.

## Technical Overview

Feed forward power uses the inverter section power demand, parameters 10/11:4 [Output Power] and 13:44 [FF Power Gain], to command the converter side of the drive. This command improves DC bus voltage regulation by letting the DC Bus PI regulator react before the DC Bus voltage sags.

Feed forward power is not used in a PowerFlex 755TM regenerative bus supply because it does not have the inverter control on the same control board.

Figure 12 - Feed Forward Power Block Diagram

<!-- image -->

Table 3 - Feed Forward Power Parameters

<!-- image -->

| Parameter No. Parameter Name Setting Description   |                    |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13:300 PwrFeedFwdConfig                            | 1 = ‘Enabled’      | 0 = ‘Disabled’ The control uses no special method. Feed forward power calculates and compensates for the power demand from the Motor Side Inverter. This sends a signal for power demand from the Motor Side Inverter control to the Line Side Converter control. This is not available with PowerFlex 755TM                                                                                                                 |
| 13:320 BusObs Config                               |                    | 0 = ‘Disabled’ Bus Observer disabled.                                                                                                                                                                                                                                                                                                                                                                                        |
| 13:320 BusObs Config                               | 1 = ‘BusObsOnly    | Bus Observer Only mode. In this mode, the Bus Observer compensates for the unknown capacitance and it only decouples that load. The voltage control loop uses the actual measured DC bus voltage as the feedback signal. The DC bus voltage regulator BW and damping are set based on parameter 13:306 [BusObs Sys BW] and parameter 13:307 [BusObsSysDamping].                                                              |
| 13:320 BusObs Config                               | 2 = ‘BusObsVltEst’ | Bus Observer with voltage estimate mode. In this mode, the Bus Observer compensates for unknown capacitance to decouple that load. In addition, the voltage control uses the estimated DC bus voltage as the feedback signal. Parameter 13:52 [Ext Bus Cap] is not used in this mode. The DC bus voltage regulator BW and damping are set based on parameter 13:306 [BusObs Sys BW] and parameter 13:307 [BusObsSysDamping]. |

## Reference Notch Filters

PowerFlex 755T products include two reference notch filters. There are three instances in which these two filters share a set of common parameters. The instances are located in the Velocity, Position, and Process PI command paths. These reference notch filters help prevent the velocity command from introducing a resonance into the mechanical system or sway into a crane/hoist system.

You can use the reference notch to counter the pendulum effect that is caused by the movement of the trolley or gantry in crane and hoist applications. See Anti-Sway Applications on page 166 information about configuring notch filters for crane/hoist applications.

## Technical Overview

The two notch filters in the velocity reference and position reference paths can be used to notch out command frequencies that can cause resonance or instability in mechanical systems.

Figure 13 and Figure 14 show that the notch filters are located in the reference command of both the position and velocity command paths.

Figure 13 - Position Reference 2 (PRef2) Block Diagram

PRef EGR Out

<!-- image -->

Figure 14 - Velocity Reference – Flux Vector (VRef Vect)

<!-- image -->

Figure 15 - Process PID (Proc1) Block Diagram Block Diagram

<!-- image -->

Table 4 - Notch Filter Parameters

| Parameter No. Parameter Name   | Setting [Min/Max] Description   |                                                                                                                                                                                                                                                                                         |
|--------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:942 Ref NF1 Freq         | 0.00/32767.00 Hz                | Reference Notch Filter Frequency                                                                                                                                                                                                                                                        |
|                                | 0.00/32767.00 Hz                | Enter the center frequency of the first reference q notch filter in units of Hz. 10/11:948 Ref NF2 Freq                                                                                                                                                                                                                                                                                         |
| 10/11:943 Ref NF1 Width        | 0.000/10000.000                 | Reference Notch Filter Width Enter the width of the first reference notch filter around the center frequency.                                                                                                                                                                           |
| 10/11:949 Ref NF2 Width        | 0.000/10000.000                 | This value determines the denominator damping of its second order transfer function. A typical value of 0.4 produces a narrow width and a value of 1.0 produces a wide width.                                                                                                           |
| 10/11:944 Ref NF1 Depth        | 0.000/10000.000                 | Reference Notch Filter Depth Enter the depth of the first reference notch filter at the center frequency. This value determines attenuation level and the numerator damping of its second order transfer                                                                                |
| 10/11:950 Ref NF2 Depth        | 0.000/10000.000                 | function. The minimum depth occurs when this value is the same value as the width, turning off the filter. The maximum depth occurs when this value is zero.                                                                                                                            |
| 10/11:945 Ref NF1 Gain         | -20.00/+20.00                   | Command (Reference) Notch Filter Gain Enter the gain of the first reference notch filter. second order transfer function.                                                                                                                                                               |
| 10/11:951 Ref NF2 Gain         | -20.00/+20.00                   | This value sets the mode of the filter and gain of its For a notch filter, enter a value of 1. For a second order low pass filter, enter a value of 0. For a second order lag-lead filter, enter a value from 0 to 1. For a second order lead-lag filter, enter a value greater than 1. |

## Notch Filters Examples

These graphs show a velocity command before and after the reference notch filter. The command going into the filter is a ramp to 50 rpm in 0.5 seconds and the first notch filter is set to a frequency of 0.5 Hz.

Figure 16 - Velocity Command – Before Reference Notch Filter

<!-- image -->

Figure 17 - Velocity Command – After Reference Notch Filter

<!-- image -->

## CIP Security

PowerFlex 755T products with firmware revision 10.001 or later are CIP Secure Capable with secure hardware devices and code that is embedded into control and communication.

## Overview

CIP Security is an ODVA standardized method of protecting industrial automation control systems (IACS) through EtherNet/IP™ and device authentication, integrity, and confidentiality. As EtherNet/IP becomes a growing standard, evolving these isolated IACS networks towards smart manufacturing, network convergence, and industrial security become a necessity.

CIP Security is configured through FactoryTalk® Policy Manager software.

For more information on how to deploy CIP Security with PowerFlex 755T products and at scale across an industrial automation control system, see the CIP Security with Rockwell Automation Products Application Technique, publication SECURE-AT001 .

## Supported Attributes

PowerFlex 755T products with firmware revision 10.001 or later support these attributes.

|                                    | Property Description                                                                                                                                                                                                                                                         |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Identity and Authentication | Certificate that is based on the X.509 v3 standard is used to provide identity. Pre-shared keys are shared secrets that are shared among trusted entities that are used to provide identity. The TLS protocol facilitates mutual authentication to create trusted endpoints. |
| Data Integrity                     | Keyed-Hash Message Authentication Code (HMAC) is used as a cryptographic method of providing data integrity and message authenticity to EtherNet/IP traffic.                                                                                                                 |
| Data Confidentiality               | Data encryption is used to encode messages or information to help prevent reading or viewing of EtherNet/IP data by unauthorized parties.                                                                                                                                    |

## Secondary Motor Control

Secondary Motor Control functionality is added to PowerFlex 755T drives as modular control profiles in firmware revision 5 and later. The Secondary Motor Control modular control profile is installed in port 11 of the PowerFlex 755T drive. When defining the motor control type to be used with the Secondary Motor Control profile, only parameters for that type of motor control are present in the profile, similar to port 10 Primary Motor Control. When used with the primary motor control profile, you can define different control types, motor types, or motor parameters to increase the flexibility of the PowerFlex 755T drive.

## Secondary Motor Control Configuration

The Secondary Motor Control modular control profile in port 11 is defined in 0:67 [Sec MtrCtrl Mode]. The same motor control types that are available in the primary motor control profile are configurable in the secondary motor control profile. Motor control profiles include Induction VHz, Induction SV, Induction Economizer, Induction FV, IPM FV, and SPM FV. The active motor control type that is configured in the Secondary Motor Control profile port 11 is displayed in 0:68 [Sec MtrCtrl Act].

The motor control type that is defined for the Secondary Motor Control profile determines the parameters that are accessible in port 11. All motor data and application tuning configuration of the Secondary Motor Control profile is done in port 11. You can see the parameter list in the PowerFlex 750-Series Drives with TotalFORCE Control programming manual, publication 750-PM100 .

## Switching Between Motor Control Profiles

The active motor control profile is defined in 0:74 [Motor Ctrl Sel]. There are two methods you can use to change between the primary and secondary motor control profiles.

Logix Configuration

The motor control profile that is actively being used can be changed by writing to 0:74 [Motor Ctrl Sel] either through a datalink or with an explicit message instruction. You can verify that the active motor control profile has changed as expected by doing a readback from the PowerFlex 755T drive by using 0:75 [Mtr Ctrl Sel Act].

Discrete-Wired Digital Input

You can wire a digital input to an I/O option module installed in the PowerFlex 755T drive. The digital input is configured to 0:169 [DI Mtr Ctrl Sel] to switch between the primary and secondary motor control profiles. If the input is open or de-energized, the drive selects the Primary Motor Control profile.

Interaction between Logix and Digital Input

If both methods to control the active motor control profile are being used, the digital input that is configured in 0:169 [DI Mtr Ctrl Sel] takes priority.

## Application Use Cases

Secondary Motor Control profiles can be used for various applications. Applications that require one drive to control two different-sized motors independently, multi-axis storage and retrieval systems, or single motor to multi-motor are several examples that can leverage the two motor control profiles.

## One Drive, Two Independent Motors

You can use the Secondary Motor Control profile to change motor size without the need to reprogram the drive. In this example, one PowerFlex 755T drive is used to control a 100 Hp motor, but can be electrically switched over to a 150 Hp motor. The primary motor control profile is configured with the 100 Hp motor characteristics and tuning requirements. The secondary motor control profile is configured with the 150 Hp motor characteristics and tuning requirements.

The drive is configured to switch between the primary and secondary motor control profiles that are based on which contactor is closed and electrically connected to the specified motor.

Figure 18 - One Drive, Two Independent Motors

<!-- image -->

One Drive, Two Motor Control Types

You can use secondary motor control when one PowerFlex 755T drive is used to switch from two different motor control types. For this example, the PowerFlex 755T drive is configured to switch between controlling an induction motor and an SPM permanent magnet motor. Induction Flux Vector is configured in the Primary Motor Control profile, and SPM Motor Flux Vector is configured in the Secondary Motor Control profile.

The drive is configured to switch between the primary and secondary motor control profiles that are based on which contactor is closed and electrically connected to the specified motor.

Figure 19 - One Drive, Two Motor Control Types

<!-- image -->

One Drive, One Motor, and Multi-Motor Control

You can use secondary motor control when one PowerFlex 755T drive is used to switch from controlling one motor to controlling a multi-motor system. For this example, the PowerFlex 755T drive is configured to switch between controlling one motor in induction flux vector mode and controlling a multi-motor system in induction VHz mode. Induction Flux Vector is configured in the Primary Motor Control profile, and Induction VHz is configured in the Secondary Motor Control profile.

The drive is configured to switch between the primary and secondary motor control profiles that are based on which contactor is closed and electrically connected to the specified motor.

Figure 20 - One Drive, One Motor, Multi-Motor

<!-- image -->

## Energy Pause Function

The Energy Pause function sends the drive or bus supply to and from a low-energy state on command. This function saves energy, reduces wear on parts, and reduces fan noise.

## Components that save energy:

- LCL filter and line side converter heatsink fans
- Balancing resistors
- Power module power supplies
- LCL filter module inductors

For frames 5 and 6 of the PowerFlex 755TR/TL/TM and all frame sizes of the PowerFlex 755TS, an external input contactor can be controlled to disconnect the drive from the AC line when in energy pause mode.

For frames 7…15 of the PowerFlex 755 TR/TL drives, the line side converters are disconnected from the AC line and the fans are in a low-energy state when in energy pause mode.

Table 5 - Total Energy Savings—PowerFlex 755TR/TL/TM Products

| Common Bus Inverters [kW]                                             | Common Bus Inverters [kW]   |
|-----------------------------------------------------------------------|-----------------------------|
| Frame Drives [kW] Bus Supplies [kW]  IP21, UL Type 1 IP54, UL Type 12 |                             |
| 5 0.4 — — —                                                           |                             |
| 6 0.6 0.6 — —                                                         |                             |
| 7 1.4 1.1 — —                                                         |                             |
| 8 1.3 1.1 0.3 0.7                                                     |                             |
| 9 2.2 1.8 0.6 1.0                                                     |                             |
| 10 3.5 2.5 0.9 1.6                                                    |                             |
| 11 4.5 3.7 1.2 2.0                                                    |                             |
| 12 5.8 4.8 1.4 2.6                                                    |                             |
| 13 7.1 5.9 1.7 3.3                                                    |                             |
| 14 8.9 7.3 2.2 3.7                                                    |                             |
| 15 11.5 9.6 2.6 5.0                                                   |                             |

## System Requirements

The Energy Pause function is available in PowerFlex 755TL low harmonic drives, 755TR regenerative drives, 755TM common bus inverters, and 755TS drives.

- Firmware revision 3 or later is installed for PowerFlex 755TL low harmonic drives, 755TR regenerative drives, and 755TM bus supplies.
- Firmware revision 10 or later is installed for PowerFlex 755TM common bus inverters.
- Firmware revision 11 or later is installed for PowerFlex 755TS drives
- A customer-supplied 24V DC auxiliary power source is connected. See Auxiliary Power Supply on page 38 for more information on using an auxiliary power supply.

## Monitor Status with Energy Pause

Three machine states govern the energy pause function: Owned, Paused, and Resuming. These states are a subset of the states that are required to support the CIP Energy Power Management object. The names come from that object.

Monitor the status of the state machine with parameter 0:59 [Energy Status].

<!-- image -->

## Owned State

After powerup and when AC precharge is complete, the function moves to the Owned state. The Owned state is the traditional operating state. The line side converter is energized and can modulate. The motor side inverter is energized and can modulate.

In the Owned state, the function waits for an Energy Pause command. If it receives one, it moves to the Paused state. An Energy Pause command is ignored if the line side converter and the motor side inverter are modulating.

For the PowerFlex 755TL low harmonic drives, 755TR regenerative drives, and 755TM bus supplies you must set parameter 0:63 [LS Start Mode] to 2 'Conv Logic' to use energy pause. PowerFlex 755TM common bus inverters and 755TS drives do not have this parameter.

## Paused State

In the Paused state, the product disconnects three-phase power from the LCL filter module and line side converter. In frames 7...15, it disconnects three-phase power by opening the precharge circuit breaker (MCB). It also lowers the speed of the heatsink fans in the LCL filter and power modules.

Frame 5…6 drives do not have internal precharge circuit breakers. A digital output controls a contactor that disconnects the whole product from three-phase power.

To operate the contactor pilot coil, the contactor is wired to a digital output on an I/O option module.

In this state, the function clears faults that naturally occur as a result of the three-phase power being disconnected.

In the Paused state, the product waits for an Energy Resume command. If it receives one, it moves to the Resuming state. For frame 5…7 drives the HMI indicates a drive status of 'in precharge'.

## Resuming State

The Resuming state moves the product from the Paused state back to the Owned state. It reconnects three-phase power and then performs the AC precharge.

In this state, the Energy Pause function clears faults that occur as a result of the three-phase power being disconnected.

The function moves to the Owned state when AC precharge is complete.

## Activate Energy Pause

You can activate the Energy Pause function by setting a bit in the controller, or by using a discrete-wired digital input. The product must be stopped before an energy pause request can be sent. If a converter or inverter is modulating, the drive ignores the request to enter energy pause mode and remains in the Owned state. The product must detect a rising edge of the energy pause command after the converter and inverter have been stopped.

## Logic Command

For PowerFlex 755TM bus supplies, 755TM common bus inverters, and 755TS drives:

- Program the Logix project to set bit 21 'Energy Pause' of the logic command word to request an Energy Pause command. For more information on the logic command word, see the Logic Command and Logic Status tabs in the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101 .
- Program the project to clear the bit to request an Energy Resume command.

## For PowerFlex 755TL/TR drives:

- Set parameter 0:63 [LS Start Mode] to 2 'ConvLogic'
- Set an output datalink to parameter 0:64 [LS Manual Ctrl]
- Program the Logix project to set parameter 0:64 [LS Manual Ctrl] bit 21 'Energy Pause]'of word to request an Energy Pause command.
- Program the project to clear the bit to request an Energy Resume command.

## Discrete-wired Digital Input

Use parameter 0:135 [DI Energy Pause] to select a digital input on an I/O option card in one of the option slots. Wire the input to circuitry that closes or energizes to create an Energy Pause command, and opens or de-energizes to create an Energy Resume command.

Discrete-wired Digital Output—PowerFlex 755TS All Frames and 755TR/TL/TM Frames 5 and 6

The Energy Pause function sets parameter 0:59 [Energy Status] bit 16 'Cls Ext Cont' to close an external contactor to connect the line side converter to three-phase power.

Example: Connect a digital output function that energizes to close an external contactor.

- Set I/O card parameter nn:10 [RO0 Sel] to 59.16. This value is the address of parameter 0:59 [Energy Status] bit 16.
- Connect the relay output to the contactor to energize the coil that closes the contactor.
- The energy function clears this bit 16 in the Paused state. Bit 16 is set in the Resuming and Owned states.

Interaction Between Logic Command and Digital Input

Parameter 0:267 [EnergyPauseOwner] indicates which ports are issuing valid energy pause commands. By default, bit 15 = 1, which is the embedded Ethernet port.

When both methods (logic command and digital input) are used, an OR function of the two signals determines the Energy Pause request. An Energy Pause request results if either signal detects the request. A Resume request results if both signals are cleared.

Table 6 - Energy Pause Request Results

| Logic Command Bit 21 ‘Energy Pause’ DI Energy Pause Digital Input Request Result   |
|------------------------------------------------------------------------------------|
| 0 (cleared) 0 (open or de-energized) Resume Command                                |
| 0 (cleared) 1 (closed or energized) Energy Pause Command                           |
| 1 (set) 0 (open or de-energized) Energy Pause Command                              |
| 1 (set) 1 (closed or energized) Energy Pause Command                               |

## Energy Pause on Common Bus Systems

When using Energy Pause on a common bus system, pause and resume commands must be coordinated between the bus supply and common bus inverters. To pause a common bus system:

- Stop all devices (not modulating)
- Send pause command to common bus inverters
- Wait for all devices to report they are in the Paused state
- Send pause command to the bus supply
- Bus supply reports it is in the Paused state

A resume command for a common bus system must be done in the reverse order that is used for pause. To resume a common bus system:

- Send resume command to the bus supply
- Wait for the bus supply to report it is in the Owned state
- Send resume command to the common bus inverters
- Common bus inverters report they are in the Owned state
- Devices are ready to start

## Predictive Maintenance

The overall goal of the predictive maintenance function is to enable regular maintenance of drives, motors, and machines.

The predictive maintenance function monitors the lifespan of various components that are used in PowerFlex 755T products that are running firmware revision 6.xxx or earlier. The function uses prior usage patterns to calculate the component lifespan. For firmware revisions 10.xxx and later, see Predictive Maintenance CIP Objects on page 79 .

The predictive maintenance function allows you to set the event action and event levels. The event level changes how much of the total life of a component is consumed before the predictive maintenance function notifies you to replace the component.

The predictive maintenance function can monitor the following components:

- Insulated-gate bipolar transistors (IGBTs)
- Fans and blowers
- DC bus capacitors
- Circuit breaker
- LCL capacitors
- Filters (airflow health)

The predictive maintenance function calculates the remaining life of components. The calculation is based on the following application factors:

- Temperature
- Air quality
- Airflow
- Voltage
- Runtime
- Cycles
- Drive size

In each of the predictive maintenance functions, there are several parameters that are used to configure levels, actions, inputs, and outputs. The following sections describe those functions and parameters. The following descriptions are the same for all parameters. For example, Event Level functions are the same for all parameters, in that it determines when the event that it is monitoring occurs based on percentage of life used.

## Setting the Event Levels and Event Actions

There is an event level and event action for each type of predictive maintenance function. The event level and event action parameters are in port 0, because it is logical for all events of the same type to occur at the same level. For example, it is logical for all heatsink fan events to happen at the same level. Heatsink fans are in the line side converter and the motor side inverter.

## Event Level

The event level determines when the event occurs. The level is expressed in percent of life used.

The event occurs when the component has used up this amount of predicted life. The default is 80%. If you leave it at the default setting, the event occurs when 80% of the component life is used. If you change a level to 50%, the event occurs when half of the component life is used.

You can change these values to almost any level. Select a level that is appropriate for your application and drive section. If the drive section is critical or the application cannot tolerate unplanned downtime, you can use lower event level values.

## Event Action

The event action determines what happens when the event occurs. There are two choices: Ignore and Alarm. If you select alarm, the event triggers an alarm. Alarms are notifications and do not interrupt product operation. The alarm number and alarm text appear on the HIM and in any connected software. They are also recorded in the alarm queue.

You could choose Ignore if you wanted to use another means to track remaining life and create a notification. One possible option is to use your own logic in a controller to monitor elapsed life and remaining life parameters, and then create a notification on a Human Machine Interface screen.

## Monitor Elapsed Life and Remaining Life

There is an elapsed life and a remaining life parameter for each component that is covered by predictive maintenance.

## Elapsed Life

The values of these parameters represent the accumulated damage that the components experience.

The unit of measure is unique for each type of component.

- Hours for fans, bus capacitors, and filter capacitors.
- Cycles for relay contacts, IGBTs, precharge contactors, switches, and breakers.

The values reflect the runtime on the components and the running conditions. For example, elapsed life values for fans increment faster when the temperature is higher and the fan speed is higher. Elapsed life values for IGBTs increment faster when temperature, load, and carrier frequency are higher. Elapsed life values for bus capacitors increment faster when temperature, load, and DC bus ripple are higher.

## Remaining Life

The value of this parameter represents a prediction of how much life is remaining in the component. Changes you make to the event level for each predictive maintenance function directly affect this value.

The unit of measure for these parameters is always hours, regardless of the component type. Measuring time in hours helps you schedule replacement during planned downtime.

Predicted values are based on the rate of change of accumulated damage. For example, remaining life values for fans are lower when recent temperature and speed are higher. Remaining life values for IGBTs are lower when recent temperature, load, and carrier frequency are higher. Remaining life values for bus capacitors are lower when recent temperature, load, and DC bus ripple are higher.

These predicted values are similar to the 'fuel range' displayed on many automotive dashboards. The value is high, for a given amount of fuel, when you are cruising efficiently on the highway. It is low, for the same amount, if you are stuck in 'stop and go' city traffic.

## Predictive Maintenance Function Details — Firmware Revisions 6 and Earlier

This section describes the details of the predictive maintenance functions of PowerFlex 755T products that use firmware revisions 1 through 6 only.

IGBT Modules

Table 7 - Event Level and Event Action Parameters

|                                                 | Parameter No. Parameter Name Units Definition                                                                                                             |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0:566 IGBT Event Level %                        | Enter a value to determine when a Predictive Maintenance IGBT event in the power modules takes place. The event notifies you to replace the power module. |
| 0:567 IGBT Event Actn  0 = ‘Ignore’ 1 = ‘Alarm’ | Select the action taken when the Predictive Maintenance IGBT event in the power modules takes place.                                                      |

Output Parameters (Port 12 and 14)

Remaining Lifetime and Elapsed Lifetime: The calculation uses Event Level and the record of operating conditions from the past 30 days. These conditions include component data, temperature, load (current), and runtime. Positive values indicate the estimated number of hours until the event occurs. These values count down.

Negative values indicate the number of hours that have passed since the event occurred. The precision of this parameter is limited to the eight most significant digits. The three least significant digits are rounded. For example, an internal value of 18760230188 is represented in this parameter as 18760230000.

Table 8 - Output Parameters

|        |                                                                                                                                                                 | Units Definition Parameters                                                      |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Hours  | Displays the remaining life for the IGBTs in the line side power module. IGBTs in power module L0 IGBTs in power module L1 … IGBTs in power module L9           | 14:140 [L0IGBT RemainLif] 14:240 [L1IGBT RemainLif] … 14:1040 [L9IGBT RemainLif] |
| Hours  | Displays the unprocessed elapsed life of the IGBTs in the line side power module. IGBTs in power module L0 IGBTs in power module L1 … IGBTs in power module L9  | 14:139 [L0IGBT ElpsdLife] 14:239 [L1IGBT ElpsdLife] … 14:1039 [L9IGBT ElpsdLife] |
| Cycles | Displays the unprocessed elapsed life of the IGBTs in the motor side power module. IGBTs in power module M0 IGBTs in power module M1 … IGBTs in power module M9 | 12:139 [M0IGBT ElpsdLife] 12:239 [M1IGBT ElpsdLife] … 12:1039 [M9IGBT ElpsdLife] |

## Fan or Blower

The following fans have the proposed fan life model implemented:

- Heatsink fan (Power module and LCL filter module blower)
- Control pod fan
- Power bay roof fan: IP54 only (frame 8…12)
- Input bay roof fan: Input bay (frame 8…9) and Control bay (frame 8…12)
- Door fan: Input bay (frame 10…12), Entry wire bay (frame 8…12), and Exit wire bay (frame 8…12)

The firmware calculates by averaging the measured ambient temperature parameters from the power modules in the motor side inverter and the line side converter.

## Table 9 - Input Parameters

<!-- image -->

|                                                                                          | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                            | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                            | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                     |                                                                                                                      |                                                                                                                      |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                              |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| °C Temperature Module M0 = 12:131 [M0 Meas Amb Tmp] Module M1 = 12:231 [M1 Meas Amb Tmp] | °C Temperature Module M0 = 12:131 [M0 Meas Amb Tmp] Module M1 = 12:231 [M1 Meas Amb Tmp]                                    | °C Temperature Module M0 = 12:131 [M0 Meas Amb Tmp] Module M1 = 12:231 [M1 Meas Amb Tmp]                                    | °C Temperature Module M0 = 12:131 [M0 Meas Amb Tmp] Module M1 = 12:231 [M1 Meas Amb Tmp]                             | Module L0 = 14:131 [L0 Meas Amb Tmp] Module L1 = 14:231 [L1 Meas Amb Tmp] … Module L9 = 14:1031 [L9 Meas Amb Tmp]    | Module L0 = 14:131 [L0 Meas Amb Tmp] Module L1 = 14:231 [L1 Meas Amb Tmp] … Module L9 = 14:1031 [L9 Meas Amb Tmp]    | Module L0 = 14:131 [L0 Meas Amb Tmp] Module L1 = 14:231 [L1 Meas Amb Tmp] … Module L9 = 14:1031 [L9 Meas Amb Tmp]                           | Module L0 = 14:131 [L0 Meas Amb Tmp] Module L1 = 14:231 [L1 Meas Amb Tmp] … Module L9 = 14:1031 [L9 Meas Amb Tmp]                           | Module LCL0 = 14:1241 [F0 Meas Amb Tmp] Module LCL1 = 14:1441 [F2 Meas Amb Tmp] … Modlue LCL5 = 14:2141 [F9 Meas Amb Tmp]                   | Module LCL0 = 14:1241 [F0 Meas Amb Tmp] Module LCL1 = 14:1441 [F2 Meas Amb Tmp] … Modlue LCL5 = 14:2141 [F9 Meas Amb Tmp]                   | Module LCL0 = 14:1241 [F0 Meas Amb Tmp] Module LCL1 = 14:1441 [F2 Meas Amb Tmp] … Modlue LCL5 = 14:2141 [F9 Meas Amb Tmp]    |
|                                                                                          |                                                                                                                             |                                                                                                                             | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                           | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                           |                                                                                                                      |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                              |
|                                                                                          | °C Temperature 0:25 [Ctrl Pod Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] | °C Temperature 0:25 [Ctrl Pod Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] 0:503 [Meas Amb Temp] |                                                                                                                      |                                                                                                                      |                                                                                                                      |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                              |
|                                                                                          |                                                                                                                             |                                                                                                                             |                                                                                                                      |                                                                                                                      |                                                                                                                      |                                                                                                                                             |                                                                                                                                             | Units Definition Heatsink Fans Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                    | Units Definition Heatsink Fans Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                    |                                                                                                                              |
| % Event Level                                                                            | 0:562 [HSFan EventLevel]                                                                                                    | 0:514 [PodFan Event Lvl]                                                                                                    | 0:514 [PodFan Event Lvl]                                                                                             | 0:534 [PwrRfFanEventLvl]                                                                                             | 0:534 [PwrRfFanEventLvl]                                                                                             | 0:524 [In Fan EventLvl]                                                                                                                     | 0:524 [In Fan EventLvl]                                                                                                                     | 0:554 [CtrlFanEventLvl]                                                                                                                     | 0:554 [CtrlFanEventLvl]                                                                                                                     | 0:544 [WrgFanEventLvl]                                                                                                       |
| 1 or 0 Event Action                                                                      | 0:563 [HSFan EventActn]                                                                                                     | 0:515 [PodFan EventActn]                                                                                                    | 0:515 [PodFan EventActn]                                                                                             | 0:535 [PwrRfFanEvntActn]                                                                                             | 0:535 [PwrRfFanEvntActn]                                                                                             | 0:525 [In FanEventActn]                                                                                                                     | 0:525 [In FanEventActn]                                                                                                                     | 0:555 [CtrlFanEvntActn]                                                                                                                     | 0:555 [CtrlFanEvntActn]                                                                                                                     | 0:545 [WrgFanEvntActn]                                                                                                       |
|                                                                                          |                                                                                                                             |                                                                                                                             |                                                                                                                      | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                     | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                     | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                                            | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                                            |                                                                                                                                             |                                                                                                                                             |                                                                                                                              |
| Hours  Remaining Life                                                                    | Module M0 = 12:136 [M0HSFanRemainLif] Module M1 = 12:236 [M1HSFanRemainLif] … Module M9 = 12:1036 [M9HSFanRemainLif]        | Module M0 = 12:136 [M0HSFanRemainLif] Module M1 = 12:236 [M1HSFanRemainLif] … Module M9 = 12:1036 [M9HSFanRemainLif]        | Module M0 = 12:136 [M0HSFanRemainLif] Module M1 = 12:236 [M1HSFanRemainLif] … Module M9 = 12:1036 [M9HSFanRemainLif] | Module L0 = 14:136 [L0HSFanRemainLif] Module L1 = 14:236 [L0HSFanRemainLif] … Module L9 = 14:1036 [L0HSFanRemainLif] | Module L0 = 14:136 [L0HSFanRemainLif] Module L1 = 14:236 [L0HSFanRemainLif] … Module L9 = 14:1036 [L0HSFanRemainLif] | Module L0 = 14:136 [L0HSFanRemainLif] Module L1 = 14:236 [L0HSFanRemainLif] … Module L9 = 14:1036 [L0HSFanRemainLif]                        | Module L0 = 14:136 [L0HSFanRemainLif] Module L1 = 14:236 [L0HSFanRemainLif] … Module L9 = 14:1036 [L0HSFanRemainLif]                        | Module LCL0 = 14:1246 [F0HSFanRemainLif] Module LCL1 = 14:1446 [F2HSFanRemainLif] … Module LCL5 = 14:2146 [F9HSFanRemainLif]                | Module LCL0 = 14:1246 [F0HSFanRemainLif] Module LCL1 = 14:1446 [F2HSFanRemainLif] … Module LCL5 = 14:2146 [F9HSFanRemainLif]                | Module LCL0 = 14:1246 [F0HSFanRemainLif] Module LCL1 = 14:1446 [F2HSFanRemainLif] … Module LCL5 = 14:2146 [F9HSFanRemainLif] |
|                                                                                          |                                                                                                                             |                                                                                                                             |                                                                                                                      |                                                                                                                      |                                                                                                                      |                                                                                                                                             | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  |                                                                                                                                             |                                                                                                                              |
| Hours  Remaining Life                                                                    | 0:513 [PodFan RemainLif]                                                                                                    | 0:513 [PodFan RemainLif]                                                                                                    | 0:533 [PwrRfFanRem Life]                                                                                             | 0:533 [PwrRfFanRem Life]                                                                                             | 0:523 [In FanRemainLif]                                                                                              | 0:523 [In FanRemainLif]                                                                                                                     | 0:553 [CtrlFanRem Life]                                                                                                                     | 0:553 [CtrlFanRem Life]                                                                                                                     | 0:543 [WrgFanRem Life]                                                                                                                      | 0:543 [WrgFanRem Life]                                                                                                       |
|                                                                                          | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                            | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                            | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                     |                                                                                                                      |                                                                                                                      |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                                             |                                                                                                                              |
| Hours Elapsed Life                                                                       | Module M0 = 12:135 [M0HSFanElpsdLife] Module M1 = 12:235[M1HSFanElpsdLife] … Module M9 = 12:1035 [M9HSFanElpsdLife]         | Module M0 = 12:135 [M0HSFanElpsdLife] Module M1 = 12:235[M1HSFanElpsdLife] … Module M9 = 12:1035 [M9HSFanElpsdLife]         | Module M0 = 12:135 [M0HSFanElpsdLife] Module M1 = 12:235[M1HSFanElpsdLife] … Module M9 = 12:1035 [M9HSFanElpsdLife]  | Module L0 = 14:135 [L0HSFanElpsdLife] Module L1 = 14:235 [L1HSFanElpsdLife] … Module L9 = 14:1035 [L9HSFanElpsdLife] | Module L0 = 14:135 [L0HSFanElpsdLife] Module L1 = 14:235 [L1HSFanElpsdLife] … Module L9 = 14:1035 [L9HSFanElpsdLife] | Module L0 = 14:135 [L0HSFanElpsdLife] Module L1 = 14:235 [L1HSFanElpsdLife] … Module L9 = 14:1035 [L9HSFanElpsdLife]                        | Module LCL0 = 14:1245 [F0HSFanElpsdLife] Module LCL1 = 14:1445 [F2HSFanElpsdLife] … Module LCL5 = 14:2145 [F9HSFanElpsdLife]                | Module LCL0 = 14:1245 [F0HSFanElpsdLife] Module LCL1 = 14:1445 [F2HSFanElpsdLife] … Module LCL5 = 14:2145 [F9HSFanElpsdLife]                | Module LCL0 = 14:1245 [F0HSFanElpsdLife] Module LCL1 = 14:1445 [F2HSFanElpsdLife] … Module LCL5 = 14:2145 [F9HSFanElpsdLife]                |                                                                                                                              |
|                                                                                          |                                                                                                                             |                                                                                                                             |                                                                                                                      |                                                                                                                      |                                                                                                                      | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  | Units Definition Control Pod Power Bay Roof Input Bay Fan Control Bay Roof Wiring Bay Fans                                                  |                                                                                                                              |
|                                                                                          |                                                                                                                             |                                                                                                                             |                                                                                                                      |                                                                                                                      |                                                                                                                      | Hours Elapsed Life 0:512 [PodFan ElpsdLife] 0:532 [PwrRfFanElpsdLif] 0:522 [In FanElpsdLife] 0:552 [CtrlFanElpsdLif] 0:542 [WrgFanElpsdLif] | Hours Elapsed Life 0:512 [PodFan ElpsdLife] 0:532 [PwrRfFanElpsdLif] 0:522 [In FanElpsdLife] 0:552 [CtrlFanElpsdLif] 0:542 [WrgFanElpsdLif] | Hours Elapsed Life 0:512 [PodFan ElpsdLife] 0:532 [PwrRfFanElpsdLif] 0:522 [In FanElpsdLife] 0:552 [CtrlFanElpsdLif] 0:542 [WrgFanElpsdLif] | Hours Elapsed Life 0:512 [PodFan ElpsdLife] 0:532 [PwrRfFanElpsdLif] 0:522 [In FanElpsdLife] 0:552 [CtrlFanElpsdLif] 0:542 [WrgFanElpsdLif] |                                                                                                                              |

## DC Bus Capacitors

To help support planned maintenance schedules, predictive parameters issue an alarm when it is time to replace bus capacitors.

Table 12 - Input Parameters

|                | Units Definition Motor Side Power Module Fans Line Side Power Module Fans LCL Filter Module Fans                  |                                                                                                                   |                                                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| °C Temperature | Module M0 = 12:131 [M0 Meas Amb Tmp] Module M1 = 12:231 [M1 Meas Amb Tmp] … Module M9 = 12:1031 [M9 Meas Amb Tmp] | Module L0 = 14:131 [L0 Meas Amb Tmp] Module L1 = 14:231 [L1 Meas Amb Tmp] … Module L9 = 14:1031 [L9 Meas Amb Tmp] | Module LCL0 = 14:1241 [F0 Meas Amb Tmp] Module LCL1 = 14:1441 [F2 Meas Amb Tmp] … Module LCL5 = 14:2141 [F9 Meas Amb Tmp] |

Table 13 - Event Level and Event Action Parameters

| Units Definition Heatsink Fans               |
|----------------------------------------------|
| % Event Level 0:570 [Bus Cap EventLvl]       |
| 1 or 0 Event Action 0:571 [BusCap EventActn] |

Table 15 - Input Parameters

|                | Units Definition Motor Side Power Module Fans Line Side Power Module Fans Motor Side Heatsink Line Side Heatsink   |                                                                                              |                                                                                                 |                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| °C Temperature | M0 = 12:131 [M0 Meas Amb Tmp] M1 = 12:231 [M1 Meas Amb Tmp] … M9 = 12:1031 [M9 Meas Amb Tmp]                       | L0 = 14:131 [L0 Meas Amb Tmp] L1 = 14:231 [L1 Meas Amb Tmp] … L9 = 14:1031 [L9 Meas Amb Tmp] | M0 = 12:118 [M0 HeatsinkTempV] M1 = 12:218 [M1 HeatsinkTempV] … M9 = 12:1018 [M9 HeatsinkTempV] | L0 = 14:118 [L0 HeatsinkTempS] L1 = 14:218 [L1 HeatsinkTempS] … L9 = 14:1018 [L9 HeatsinkTempS] |

Table 16 - Output Parameters

| Units Definition High Temperature Rise Low Temperature Rise         |
|---------------------------------------------------------------------|
| 1 or 0 Event Action 0:590 [Hi TR EventActn] 0:591 [Lo TR EventActn] |

## Circuit Breakers

Circuit breakers generally have a fixed number of cycles available. This number varies based on whether the breaker disconnect operation occurs under electrical load.

Table 17 - Event Level and Event Action Parameters

| Units Definition AC Precharge Main Circuit Breaker AC Precharge Contactor DC Precharge Molded Case Switch   |                                                                                       |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|                                                                                                             | % Event Level 0:578 [MCB LifeEvntLvl] 0:582 [PCC LifeEvntLvl] 0:574 [MCS Event Level] |
| 1 or 0 Event Action 0:579 [MCB LifeEvntActn] 0:583 [PCC LifeEvntActn] 0:575 [MCS Event Action]              |                                                                                       |

## Table 14 - Output Parameters

|                       | Units Definition Motor Side Power Module Line Side Power Module                                                      |                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Hours  Remaining Life | Module M0 = 12:143 [M0BusCapRmngLife] Module M1 = 12:243 [M1BusCapRmngLife] … Module M9 = 12:1043 [M9BusCapRmngLife] | Module L0 = 14:143 [L0BusCapRmngLife] Module L1 = 14:243 [L1BusCapRmngLife] … Module L9 = 14:1043 [L9BusCapRmngLife] |
| Hours Elapsed Life    | Module M0 = 12:142 [M0BusCapElpsdLif] Module M1 = 12:242 [M1BusCapRmngLife] … Module M9 = 12:1042 [M9BusCapRmngLife] | Module L0 = 14:142 [L0BusCapElpsdLif] Module L1 = 14:242 [L1BusCapElpsdLif] … Module L9 = 14:1042 [L9BusCapElpsdLif] |

## Airflow Health

The goal of the predictive maintenance function is to be able to assess the health of the airflow system with the ability to detect abnormal conditions that are based on deviations from an expected temperature rise.

The following warnings are generated by comparing the actual temperature rise with the upper and lower expected temperature rise limits.

- High Temperature Rise warning
- Low Temperature Rise warning

Several conditions can cause a high temperature rise warning, including:

- Blocked air filter
- Mismatch of air filter and IP class of drive
- Internal recirculation caused by damaged or missing baffles or gaskets
- Debris in the IGBT airflow path
- Excessive pre-heating of air
- Missing LCL filter or power module covers
- Roof fan failures

Several conditions can cause a low temperature rise warning, including:

- Missing air filter
- Mismatch of air filter and IP class of drive

## Table 18 - Output Parameters

|                       | Units Definition AC Precharge Main Circuit Breaker AC Precharge Contactor DC Precharge Molded Case Switch   |                                                       |                                                                                                                      |
|-----------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Hours  Remaining Life | 14:1143 [ACP0 MCB RmngLif] 14:1153 [ACP1 MCB RmngLif]                                                       | 14:1146 [ACP0 PCC RmngLif] 14:1156 [ACP1 PCC RmngLif] | Module M0 = 12:146 [DCP0MCS Rem Life] Module M1 = 12:246 [DCP1MCS Rem Life] … Module M9 = 12:1046 [DCP9MCS Rem Life] |
| Cycles Elapsed Life   | 14:1142 [ACP0 MCBElpsdLif] 14:1152 [ACP1 MCBElpsdLif]                                                       | 14:1145 [ACP0 PCCElpsdLif] 14:1155 [ACP1 PCCElpsdLif] | Module M0 = 12:145 [DCP0MCS ElpsdLif] Module M1 = 12:245 [DCP1MCS ElpsdLif] … Module M9 = 12:1045 [DCP9MCS ElpsdLif] |

## LCL Capacitors

The calculation of line capacitor life is simplified. The only operating parameter is ambient temperature.

## Table 19 - Input Parameters

| Units Definition Motor Side Power Module Fans                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| °C Ambient Temperature Module LCL0 = 14:1241 [F0 Meas Amb Tmp] Module LCL1 = 14:1441 [F2 Meas Amb Tmp] … Module LCL5 = 14:2141 [F9 Meas Amb Tmp] |
| % Event Level 0:586 [LCL Cap EventLvl]                                                                                                           |
| 1 or 0 Event Action 0:587 [LCLCap EventActn]                                                                                                     |

Table 20 - Output Parameters

|                      | Units Definition DC Precharge Molded Case Switch                                                                          |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|
| Hours Remaining Life | Module LCL0 = 14:1250 [F0 Cap RmngLife] Module LCL1 = 14:1450 [F2 Cap RmngLife] … Module LCL5 = 14:2150 [F9 Cap RmngLife] |
| Hours Elapsed Life   | Module LCL0 = 14:1249 [F0 Cap ElpsdLif] Module LCL1 = 14:1449 [F2 Cap ElpsdLif] … Module LCL5 = 14:2149 [F9 Cap ElpsdLif] |

## Resetting the Meters After Component Replacement

Rockwell Automation has made the following components field replaceable: all types of fans, DC bus capacitors, LCL filter capacitors, main circuit breakers in AC precharge, precharge contactors in AC precharge, and molded case switches in DC precharge.

| IMPORTANT   | Do not perform a reset while the product is in an Energy Pause paused state. See Energy Pause Function on page 63 for details.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|

## General Instructions

Reset the Elapsed Life and Remaining Life parameters for a component after proper replacement. Follow this general procedure to reset the parameters.

1. Go to port 0 and open parameter 0:504 [PredMain Rst En]. Set the bit for the area that contains the new component.

2. Go to the port and area that contains the parameters that are related to the new component.
3. Find the parameter for Predictive Maintenance Reset in that area. Then select the component type that you just replaced.
4. Return to parameter 0:504 [PredMain Rst En] in port 0. Then clear the bit you set in step 1 .

<!-- image -->

## Reset Examples

This section provides instructions about how to reset Predictive Maintenance function parameters after you replace a component.

M0 Power Module Heatsink Fan Example

Follow these steps to reset the Elapsed Life and Remaining Life parameters for the heatsink fan in the M0 power module in the motor side inverter.

1. Go to port 0 and open parameter 0:504 [PredMain Rst En]. Set bit 10 'M0'.
2. Go to the Predictive Main group in the M0 Power Module file in port 12.
3. Find parameter 12:130 [M0PredMaintReset]. Then select 1 'M HSFan Life' in the dropdown menu.

<!-- image -->

<!-- image -->

Parameter 12:130 [M0PredMaintReset] returns to 0 'Ready' after the reset is performed.

4. Return to parameter 0:504 [PredMain Rst En] in port 0. Then clear bit 10 'M0'.

<!-- image -->

## Control Pod Fan Example

Follow these steps to reset the Elapsed Life and Remaining Life parameters for the pods on the control pod.

1. Go to port 0 and open parameter 0:504 [PredMain Rst En]. Set bit 0 'Port 0'.
2. Stay in port 0, and go to parameter 0:505 [Pred Maint Reset]. Then select 1 'PodFan Life'.

<!-- image -->

<!-- image -->

Parameter 0:505 [Pred Maint Reset] returns to 0 'Ready' after the reset is performed.

3. Return to parameter 0:504 [PredMain Rst En] in port 0. Then clear bit 0 'Port 0'.

<!-- image -->

## Configuration Examples

This section provides instructions for configuring the Predictive Maintenance Event Level and Event Action.

Heatsink Fan Example

Go to the Predictive Maintenance group in the Protection file of port 0.

Go to parameter 0:562 [HSFan EventLevel]. Change the value to 70%.

<!-- image -->

Now all heatsink fan events occur when 70% of the fan life is consumed. The heatsink fan events affect the fans in the M0 motor side inverter power module, the L0 line side converter power module, and the F0 LCL filter.

Go to parameter 0:563 [HSFan EventActn]. The value is set to 'Alarm' with an internal value of 1.

<!-- image -->

When this parameter is set to alarm, a heatsink fan event results in a numbered alarm with text to indicate which heatsink fan is affected.

## IGBT Example

Go to the Predictive Maintenance group in the Protection file of port 0.

Go to parameter 0:566 [IGBT Event Level]. Change the value to 60%.

<!-- image -->

Now all IGBT events occur when 60% of the IGBT life is consumed. The IGBT events affect IGBTs in the M0 Motor Side Inverter power module and the L0 Line Side Converter power module.

Go to parameter 0:567 [IGBT Event Actn]. The value is set to 'Alarm' with an internal value of 1.

<!-- image -->

When set to alarm, an IGBT event results in a numbered alarm with text to indicate which power module is affected.

## Control Pod Fan Example

Go to the Predictive Maintenance group in the Protection file of port 0.

Go to parameter 0:514 [PodFan EventLevel]. Change the value to 70%.

<!-- image -->

Now the control pod fan event occurs when 70% of the fan life is consumed.

Go to parameter 0:515 [PodFan EventActn]. The value is set to 'Alarm' with an internal value of 1.

<!-- image -->

When set to alarm, a Control Pod Fan event results in a numbered alarm with text.

## Monitoring Examples

This section provides instructions for monitoring the Elapsed Life and Remaining Life.

M0 Power Module Heatsink Fan Example

Follow these steps to view the Elapsed Life and Remaining Life parameters for the heatsink fan in the M0 power module in the motor side inverter.

1. In the programming tool, go to the port 12 parameters.

<!-- image -->

n

2. Go to the Predictive Main group in the M0 Power Module file.

<!-- image -->

This group lists all of the parameters that are related to predictive maintenance on the M0 power module.

3. Double-click parameters 12:135 [M0HSFanElpsdLife] and 12:136 [M0HSFanRemainLif]. The value for the parameter you selected appears.

## L0 Power Module Bus Capacitor Example

Follow these steps to view the Elapsed Life and Remaining Life parameters for the bus capacitors in the L0 power module in the line side converter.

1. In the programming tool, go to the port 14 parameters.
2. Go to the Predictive Main group in the L0 Power Module file.

<!-- image -->

<!-- image -->

This group lists all of the parameters that are related to Predictive Maintenance on the L0 Power Module.

3. Double-click parameters 14:142 [L0BusCapElpsdLife] and 14:143 [L0BusCapRmngLife]. The value for the parameter you selected appears.

## Predictive Maintenance CIP Objects

This section describes the details of the Predictive Maintenance using CIP Objects for PowerFlex 755T and 755TS products that are running firmware revision 10.xxx and later. The names and function of the Predictive Maintenance CIP Objects are the same as the Predictive Maintenance Parameters, the difference is in how the data is collected. CIP Objects are like parameters in that they're locations where data is stored but the communication route or mapping for these locations are different. To access CIP Objects, explicit messaging is required. Configuring these message instructions requires the Class, Service, Instance, and Attribute for each Predictive Maintenance data location. The PowerFlex 755T Predictive Maintenance CIP objects are classified into three levels: Predictive Maintenance Environmental, Predictive Maintenance Component Group, and Predictive Maintenance Component Levels.

The predictive maintenance feature uses the mathematical physics of failure models to predict more accurately (based on actual operating conditions) when to perform maintenance on a product component, thus saving cost over routine (fixed) time-based preventative maintenance. Predictive maintenance information also allows customers to help prevent the occurrence of downtime due to unexpected failures by alerting them in advance when maintenance is required to avoid a failure.

The Predictive Maintenance Objects are a set of CIP objects that provide a way to organize and characterize product components and their associated predictive maintenance data. These CIP objects are designed to be applicable to a range of products from simple devices with a single component to large multi-frame products with dozens of components of different types, which provide a rich set of data for customer predictive maintenance purposes. Figure 21 shows an hierarchical device example of the relationship between the predictive maintenance CIP objects within a product.

Figure 21 - Predictive Maintenance Object Hierarchy

<!-- image -->

The Predictive Maintenance Environmental Conditions Object, class 413 (hex), provides a configuration interface. Use this interface to identify the environment in which products are installed and operating. The attribute values that are provided by this object allow for the adjustment and appropriate derating that is associated with the environment to be introduced into the predictive maintenance algorithms (physics of failure models) which calculate the life of the components in a product. Some algorithms use this additional environmental information in their implementation and some do not. If no predictive maintenance algorithms require environmental information in a product, this object does not have to be implemented.

Table 21 - Class 413—Environmental Conditions

| Class: hex (dec)   |                                                 |           |    | Name Instance Attribute Attribute Name   | Data Classif. Access Rule   | Data Type      | Description                                                                                                                                                                                                                                                                                                                               | Settings/Values  (1)                                                                                                                     |
|--------------------|-------------------------------------------------|-----------|----|------------------------------------------|-----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product |    | 1 Enclosure Rating — Set USINT           |                             |                | Selects the ingress protection (IP) rating for the standalone product. Enclosure rating does not refer to any additional protective cabinet where the product is installed.                                                                                                                                                               | 0 = IP00, NEMA/UL Open Type 1 = IP21, NEMA/UL Type 1 2…3 = Reserved 4 = IP54, NEMA/UL Type 12 5 = IP65, NEMA/UL Type 4X 6…255 = Reserved |
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product | 2  | Airborne Contaminants Severity Level     |                             | — Set USINT    | Selects the severity level of airborne contaminants in the environment to which the product is exposed. ‘G1’ (0) – Severity level is mild. ‘G2’ (1) – Severity level is moderate. ‘G3’ (2) – Severity level is harsh. ‘GX’ (3) – Severity level is severe. ‘GX+’ (4) – Severity level is extreme (Rockwell extension to ANSI/ ISA-71.04). | 0 = G1 1 = G2 2 = G3 3 = GX 4 = GX+ 5…255 = Reserved                                                                                     |
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product | 3  | Supported Enclosure Ratings              | — Get                       | STRUCT OF      | Selects a limited list of supported ingress protection ratings that can be set in the Enclosure Rating attribute.                                                                                                                                                                                                                         | 0 = False (Not supported) 1 = True                                                                                                       |
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product | 3  | No. of Supported Enclosure Ratings       |                             | — Get USINT    | Selects the number of supported enclosure ratings enumeration values to be included in the list.                                                                                                                                                                                                                                          | —                                                                                                                                        |
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product | 3  | Supported Enclosure Ratings List         | — Get                       | ARRAY of USINT | The array of listed enclosure ratings enumeration values supported by the product. Valid enumeration values are listed in attribute 1 to be included in the list. The length of array entries is limited by the data type of USINT or a maximum value of 255.                                                                             | —                                                                                                                                        |
| 0x413 (1043)       | Predictive Maintenance Environmental Conditions | 1=Product | 4  | Reset Required Status                    |                             | — Get BOOL     | Selects if the device requires a type 0 reset service or a power cycle, to apply configuration changes to any of the settable instance attributes.                                                                                                                                                                                        | 0 = Off 1 = On                                                                                                                           |

(1) The Settings/Values in this column are instances.

The CIP objects in this class require a power cycle or device reset is for the configured changes to take effect.

The Predictive Maintenance Component Object, class 0x414 (hex), provides a way to indicate predictive maintenance data and status for an individual physical component in a product. The information can then be communicated to users through various human interfaces to provide the necessary insight for maintaining the product in their facility. Additionally, this object allows predictive maintenance data to be reset after a component maintenance action (service or replacement) is performed. Multiple instances of this object can be required to represent the various physical components with predictive maintenance information in a product.

Table 22 - Class 414—Predictive Maintenance Component

| Class: hex (dec)   |                                  |    |    | Name Instance Attribute Attribute Name   | Data Classif. Access Rule   | Data Type     | Description                                                                                                                                                                                                                                                                                                                                                                     | Settings/Values  (1)                                                                                                                                                                      |
|--------------------|----------------------------------|----|----|------------------------------------------|-----------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x414 (1044)       | Predictive Maintenance Component | —  |    | 1 Component Type Constant Get UINT       |                             |               | Select the type of physical component this instance represents. The type of physical component determines the type of predictive maintenance algorithm used to calculate component life. Additionally, components of the same type are often grouped together using the Predictive Maintenance Component Group object (0x0415). component has exceeded its expected total life. | Groups 0x0000…0x0800  (2)                                                                                                                                                                 |
| 0x414 (1044)       |                                  |    | 2  | Predicted Remaining Life                 | Accumul ator                | Get DINT      | Displays the amount of predicted remaining life of the component. Remaining Life Units (for example, hours) to anticipated failure.                                                                                                                                                                                                                                             | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    | 3  | Predicted Remaining Life Units           | Constant Get UINT           |               | Indicates the units used to define the Remaining Life of the component. Hours are the preferred units, but counts may be more appropriate for simple components. For example, Counts could indicate the number of cycles between operating and non-operating states.                                                                                                            | 0x1001 = General/Count 0x1104 = Time/Hour                                                                                                                                                 |
| 0x414 (1044)       |                                  |    |    | 4 Elapsed Life                           | Accumul ator                | Get UDINT     | Displays the life, in hours or counts, that the component has been in operation.                                                                                                                                                                                                                                                                                                | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    | 5  | Elapsed Life Units                       | Constant Get UINT           |               | Indicates the units used to define the elapsed life of the component. Counts could indicate the number of cycles between operating and non-operating states.                                                                                                                                                                                                                    | 0x1001 = General/Count 0x1104 = Time/Hour                                                                                                                                                 |
| 0x414 (1044)       |                                  |    | 6  | Consumed Life Percentage                 | Accumul ator                | Get REAL      | Percentage of the total life of the component that has been used. Displays the consumed life of the component as a percentage of its total life. A value of 0% indicates a component has never been in operation. A value of 100% indicates the component has been in operation for its expected total life. Values greater than 100% are possible and indicate that the        | %                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    | 7  | Remaining Life Below Threshold           | Status Get BOOL             |               | Indicates whether the remaining life of the component has fallen below a user configured threshold level. The threshold level is configured in the Predictive Maintenance Component Group object (0x0415). The Remaining Life Threshold attribute from the group instance along with the Remaining Life attribute from this instance determine the state of this flag.          | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    |    | 8 Operating Status Get BOOL              |                             |               | Indicates whether the associated physical component is operating or is actively running.                                                                                                                                                                                                                                                                                        | 0 = Not operating or not in operational state. 1 = Operating or in operational state. The component remaining life is decreasing at a rate based on the predictive maintenance algorithm. |
| 0x414 (1044)       |                                  |    |    | 9 Reset Count                            | Accumul ator                | Get UDINT     | Indicates the number of times the component has had its predictive maintenance data reset via the Reset service.                                                                                                                                                                                                                                                                | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    |    | 10 Identity Instance Constant Get UINT   |                             |               | Instance number of the Identity object instance that represents the device containing the physical or serviceable component (device where the physical component is located).                                                                                                                                                                                                   | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    | 11 | Component Number Reference               | Constant Get UINT           |               | Differentiates between components when multiple components are associated with one Identity instance.                                                                                                                                                                                                                                                                           | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    |    | 12 Location Constant Get                 |                             | SHORT_ STRING | Identifies the location of the component within a product, device, or subsystem.                                                                                                                                                                                                                                                                                                | —                                                                                                                                                                                         |
| 0x414 (1044)       |                                  |    | 13 | Replacement Catalog Number               | Constant Get                | SHORT_ STRING | If a component is replaceable or serviceable, this is the catalog number of the part that can be ordered to replace or service it.                                                                                                                                                                                                                                              | —                                                                                                                                                                                         |

(1) The Settings/Values in this column are instances.

(2) Instances for Component Type attribute are found in the respective tab in the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101 .

The Predictive Maintenance Component Group Object, class 0x415 (hex), is one object in a set of predictive maintenance CIP objects that provide a way to organize and characterize product components and their associated predictive maintenance data. These CIP objects are applicable to a range of products from simple devices with one component to large multiframe products with dozens of components of different types, which provide a rich set of data for customer predictive maintenance purposes. Figure 21 shows a hierarchical device example of the relationship between the predictive maintenance CIP objects within a product.

Table 23 - Class 415—Predictive Maintenance Component Group

| Class: hex (dec)   |                                        |    |    | Name Instance Attribute Attribute Name   | Data Classif. Access Rule   | Data Type     | Description                                                                                                                                                                                                                                                                                                                                                                | Settings/Values  (1)                      |
|--------------------|----------------------------------------|----|----|------------------------------------------|-----------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 1  | Component Group Type                     |                             |               | Constant Get UINT Specifies the type of components in the component group. Groups 0x0000…0x0800                                                                                                                                                                                                                                                                            |                                           |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 2  | Number Of Components                     | Constant Get USINT          |               | Number of components (Predictive Maintenance Component object instances) included in this component group instance.                                                                                                                                                                                                                                                        | —                                         |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 3  | Component Instance List                  | Constant Get                | ARRAY of UINT | This attribute defines the list of Predictive Maintenance Components to be monitored within this Predictive Maintenance Component Group.                                                                                                                                                                                                                                   | —                                         |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  |    |                                          |                             |               | 4 Enabled Constant Set BOOL Enable or disable the component group.                                                                                                                                                                                                                                                                                                         | 0 = Disabled 1 = Enabled (Default)        |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 5  | Remaining Life Threshold                 | Config. Set UDINT           |               | Select a remaining life level below which components in this group report a predictive maintenance event. The units applied to this attribute are determined though the Remaining Life Threshold Units attribute.                                                                                                                                                          | —                                         |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 6  | Remaining Life Threshold Action          | Config. Set USINT           |               | Select the action that components in this group take when their remaining life falls below the configured threshold. ‘Ignore’ (0) – The device behavior ignores exceeding the Remaining Life Threshold specified level. ‘Event’ (1) – The device behavior produces an event to indicate that the Remaining Life Threshold has been exceeded, which could trigger an alarm. | 0 = Ignore 1 = Event                      |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 7  | Remaining Life Threshold Units           | Constant Get UINT           |               | Indicates the engineering units being used for the Remaining Life Threshold attribute.                                                                                                                                                                                                                                                                                     | 0x1001 = General/Count 0x1104 = Time/Hour |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 8  | User Maintenance Maximum Life            | Config. Set UDINT           |               | Specifies a user defined Maximum life for all components in the group.                                                                                                                                                                                                                                                                                                     | —                                         |
| 0x415 (1045)       | Predictive Maintenance Component Group | —  | 9  | User Maintenance Maximum Life Units      | Constant Get UINT           |               | Indicates the engineering units being used for the User Maintenance Maximum Life attribute.                                                                                                                                                                                                                                                                                | 0x1001 = General/Count 0x1104 = Time/Hour |

(1) The Settings/Values in this column are instances.

For detailed information and a complete list of the Predictive Maintenance CIP Objects, see the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101 .

## CCW/AOP Predictive Maintenance Example

When connected to a drive via Connected Components Workbench software (CCW) or Logix Designer application, select Predictive Maintenance. A page opens up that shows the Predictive Maintenance items in the drive. Pull-down menus allow for filtering to show Predictive Maintenance items by location or component type. Choose an environmental setting of Mild, Harsh, Severe, or Extreme to select which derate the Predictive Maintenance items use. The Notification setting section allows you to set thresholds and actions for each Predictive Maintenance item. See the following figures.

Figure 22 - Main Predictive Maintenance Screen

<!-- image -->

Figure 23 - Select Location of Predictive Maintenance Object

<!-- image -->

Figure 24 - Select the Component Type

<!-- image -->

Figure 25 - Set the Enclosure Type

<!-- image -->

Figure 26 - Set the Environmental Contaminants Level

<!-- image -->

Figure 27 - Set Notifications, Enable/Disable, Remaining Life Threshold, Remaining Life Action

<!-- image -->

## CIP Messaging Example

Explicit (CIP) messaging can be used to read or write Predictive Maintenance items. See the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101 for detailed information and a complete list of the Predictive Maintenance CIP Objects. The example uses a PowerFlex 755TS frame 2. Heatsink Fan Remaining Life is read using explicit messaging from a Logix processor. Currently, the Heatsink Fan Remaining life is shown as being 682,699 Hours from the graphical user interface.

Figure 28 - CIP Explicit Message

<!-- image -->

Use the Pred Maint Objects tab in the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101, to select the class and attribute: Class 0x414 Component Objects, Attribute 2 Remaining Life.

Figure 29 - Select Class and Attribute

<!-- image -->

The instance is gathered from the respective component tab. In this case the heatsink fan is listed in the Fan Group tab. Instance = 1 Heatsink Fan.

Figure 30 - Select the Instance

<!-- image -->

Create a message instruction in Logix. Message Type = CIP Generic, Service Type = Get Attribute Single, Instance = 1, Class = 414, Attribute = 2. Create a tag for the destination element tag based on the Data Type as listed in the reference tables = DINT.

Figure 31 - Create a MSG Instruction

<!-- image -->

Execute the MSG instruction and capture the desired value as shown below the value captured matches the value the graphical user interface displayed. The value captured is 682699.

## DeviceLogix

Figure 32 - Captured Value

<!-- image -->

PowerFlex 755T products (firmware revision 4 or later) have embedded DeviceLogix™ (DLX) capability that provides built-in control capacity for local application and supplementary supervisory control. DeviceLogix functionality enhances productivity for standalone applications or complimentary operation to a controller. DeviceLogix functionality is configured using either function block or ladder logic programming.

Figure 33 - Function Block Programming

<!-- image -->

Figure 34 - Ladder Logic Programming

<!-- image -->

Some examples of DeviceLogix functionality are:

- Controls Logic Command bits and Speed Reference
- Monitors Logic Status bits and Speed Feedback
- Reads inputs
- Writes outputs
- Reads and writes to parameters

DeviceLogix functionality supports the most frequently used instructions in the industry to build a logic program, including: Logical, Move, Timer, Counter, Compare, and Math. You can configure up to 500 instruction blocks to support application requirements.

DeviceLogix functionality also supports custom instructions that encapsulate logic you develop with the built-in instruction set. This feature is called a Macro instruction, with which you can design application instructions for the target device.

## Tag Binding in PowerFlex 755T Products

DeviceLogix functionality includes tag binding. This tag-mapping capability allows you to create tags for any parameter in the drive that is needed for programming. This new feature provides a consistent programming experience in the DeviceLogix function for PowerFlex 755T drives and option modules.

## Benefits of DeviceLogix

Local control at the drive level allows for simple local control functions without the need for programmable logic and automation controllers.

Some of the benefits of the DeviceLogix feature include:

- Improves control system performance
- Performs logic on the drive that reduces loading on the centralized controller and reduces drive-related traffic on the network
- Faster reaction. Capable of achieving response times of 2 ms (with 100 instructions blocks)
- Increases system reliability
- Improves diagnostics and reduces troubleshooting time
- Continues to run a process during network interruptions
- Increases system/machine modularity
- Divides control responsibility in the controller for smaller programs that save memory and reduce scan times

DeviceLogix functionality can be powered through three-phase input power or auxiliary 24V DC control power.

Some of the typical applications for DeviceLogix functionality include:

- Material handling
- Cascade pump control
- PID control
- Selector switch functions
- Signal conditioning and scaling
- Fault handling

## DeviceLogix Configuration Tool

DeviceLogix functionality is set through the DeviceLogix editor that runs on a workstation. You can access the DeviceLogix editor through a Studio 5000® Add-on Profile (AOP) or Connected Components Workbench™ software.

## Launch the DeviceLogix Editor Tool

1. In the Drive Properties, select Edit peripherals.
2. Add the Application DLX Only option module in the Peripherals list.

<!-- image -->

<!-- image -->

## DeviceLogix (DLX) functionality is added in port 9.

<!-- image -->

3. To close the window, click OK.

4. Select DeviceLogix and click the Launch Editor icon.
5. When the editor starts, select the editor style.
6. To enter edit mode, click in the taskbar.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

7. Click the blocks or instructions and drag and drop elements on the sheet to add code.
8. Click one connection pin and move the cursor to another pin and then release to interconnect items. Notice that the editor makes a connection line.

<!-- image -->

Double-click the inputs and outputs to define the tags to use, or double-click the function blocks to see the parameters.

<!-- image -->

## DeviceLogix Tag Database

Use the Tag Editor to add the tags to be used in the code.

There are four categories of tags within the database.

- Produced Network Data is the data that is to be sent to the drive, such as Start and Stop.
- Consumed Network Data is the data that is read from the drive, such as Faulted, Ready, and Direction.
- Status Input is the data that comes from the clock/calendar of the drive.
- User Defined Tag are local tags that you create.
1. Select the Show Tag Database option from the Tools menu. The Tag Database window opens.
2. To open the editor, click Launch Tag Editor.

<!-- image -->

Use the Tag Editor to select any drive parameter needed for programming. These tags are called User Selected Tags.

For example, to select digital input 0 from an I/O module in port 4, select 4:1 [Dig In Sts] bit 0 'Input 0' and click Add.

<!-- image -->

<!-- image -->

3. To add other drive parameters to the Tag database, repeat step 1
2. and step 2 .
4. To close the window, click OK.

All added tags appear in the DeviceLogix Editor workspace.

<!-- image -->

## Download and Enable the Logic

1. When the code is completed, click in the task bar to verify the logic. After the verification, a window appears with the result. The message-log window displays any errors.
2. If there are no errors, click in the taskbar to exit edit mode.
3. To download the logic, click in the taskbar. A confirmation window opens.
4. Click Yes.
5. To enable the logic, click in the taskbar. The logic is executed in the drive.

<!-- image -->

<!-- image -->

To disable the logic, click in the taskbar.

<!-- image -->

<!-- image -->

See DeviceLogix Technology for Industrial Applications Application Techniques, publication 193-AT001, for more information.

## Emergency Override Function

The purpose of the function is to allow the drive or bus supply to override its internal protections (faults) in emergency situations. This function is important for applications where customers would trade product longevity for continued running during an emergency situation.

<!-- image -->

ATTENTION: The emergency override function allows you to configure the drive to bypass internal protections when operating in emergency override mode. When the emergency override mode is enabled and active, protections that are selected are bypassed. Do not use the emergency override function without considering applicable local, national, and international codes, standards, regulations, or industry guidelines.

## IMPORTANT

## Configuration

There are two modes for the function: Only Override and Purge Frequency.

The following parameters are used to configure the Emergency Override function.

- 0:454 [Emerg OVRD Mode]
- 0:455 [Emerg Prot OVRD]
- 0:456 [EmergMode Status]
- 0:457 [Purge Frequency]

See PowerFlex Drives with TotalFORCE Control Programming Manual, publication 750-PM100 , for full descriptions of these parameters.

Go to the Overrides group in the Protection file on port 0.

Parameters

<!-- image -->

Go to parameter 0:454 [Emerg OVRD Mode] and select the desired mode.

<!-- image -->

The emergency override of protections and faults can reduce the life of the product (drive or bus supply). Their purpose is to help protect the product from conditions that can damage the product.

The person or company that configures the override assumes responsibility for the damage to the product from the conditions that would otherwise have triggered the protections.

Only Override

In Only Override mode, the product overrides faults to continue running. The product uses its normal methods for starting and stopping. The product follows its regular position/velocity/ torque mode.

## Purge Frequency

In the Purge Frequency mode, the product overrides faults to continue running. It switches to velocity mode and uses the Purge Frequency as its velocity reference. The function treats the Emergency Override command like a Run command. The product runs at the Purge Frequency when the command is set, and stops when the command is cleared.

To set the Purge Frequency, go to parameter 0:457 [Purge Frequency] and enter the speed value.

<!-- image -->

## Activate the Emergency Override Feature

The Emergency Override function can be activated by setting a bit in the controller, or by a discrete-wired digital input.

Logic Command

Program the Logix project to set bit 15 'Emerg OVRD' to create an Emergency Override command.

Program it to clear the bit to remove the Emergency Override command.

Discrete-Wired Digital Input

Use parameter 0:134 [DI EmergencyOVRD] to select a digital input on an I/O option card in one of the option slots. To create an Emergency Override command, wire the input to circuitry that closes or energizes. To remove the Emergency Override command the circuitry opens or deenergizes.

Go to the Command group in the Feedback and I/O file on port 0.

<!-- image -->

Go to parameter 0:134 [DI EmergencyOVRD] and map the function to the input on the option card you have wired to the circuit.

<!-- image -->

Interaction between Logic Command and Digital Input

You cannot use both logic command and digital input in the same configuration. The digital input takes priority over the logic command. If you choose to configure the digital input function, selecting a nonzero value in parameter 0:134 [DI EmergencyOVRD], disables bit 15 'Emerg OVRD' in the Logic Command.

## Decide Which Protections to Override

The person or company that designs the drive or bus supply configuration is responsible for deciding which protections the function can override. That person or company takes responsibility for the damage to the product from the conditions that would otherwise trigger the protections.

Go to the Overrides group in the Protection file on port 0.

Parameters

<!-- image -->

Go to parameter 0:455 [Emerg Prot OVRD].

<!-- image -->

## Reference Motion Planners

Set bits in parameter 0:455 [Emerg Prot OVRD] to configure the product to override classes of protection. Each bit represents a class of protections or faults. Set a bit to override that class of faults. Clear a bit to allow the class of faults to stop the drive or bus supply. For example:

- Bit 0 'LS Ctrl Flts' represents the faults from line-side control (port 13). If the engineer sets this bit, these events do not stop the product (drive or bus supply). If the engineer leaves it cleared, these events stop the product.
- Bit 1 'LS Pwr Flts' represents the faults from the line-side power (port 14) that you can override.

The PowerFlex Drives with TotalFORCE Control programming manual, publication 750-PM100
dibhih fltd bh bitSthditift0455 , pgg p
describes which faults are covered by each bit. See the description for parameter 0:455 [E
Pt OVRD]Althflt d ltblithtblhtiht y pp
[Emerg Prot OVRD]. Also, see the fault and alarm tables in the troubleshooting chapter.

PowerFlex 750-Series drives with TotalFORCE® control provide built-in motion planners with features for flexible configuration and generation of Position and Velocity Reference trajectories across a wide range of applications.

## New Features

Overviews on how to use the Position Reference and Velocity Reference Motion Planners are provided, each highlighting new features to:

- Provide a selection of useful move profile types with easy switching between them
- Allow users to enter acceleration and deceleration times directly
- Complete decoupling of acceleration and deceleration profiles, making it easier to generate asymmetric move profiles
- Smoothly transition in and out of velocity, acceleration, and jerk limits
- Create a simple way to balance smoothness, energy, and peak dynamics
- Automatically increase move final time for best performance when inputs generate constrained circumstances

## Benefits

Leveraging these new features to balance energy efficiency, peak dynamics, and smoothness in a simple way, Position Reference and Velocity Reference motion planners do the following:

- Prevent steps in jerk that beat up mechanical components over time. This often leads to less frequent re-tuning of servo loops and down time to replace components.
- Steps in jerk and other discontinuities generate odd harmonics that excite mechanical resonances. This leads to servo loops working harder to remove these self-induced resonances. As a result, the drive consumes more energy.
- Balance peak dynamics which translates to lower energy requirements for some applications.
- Configure motion profiles to operate closer to machine limits, while preserving high dynamics.
- Configure motion profiles to generate torque-speed curves that improve motor utilization and use more of its operating range.

Some applications that benefit from the resulting smooth motion are listed:

- Liquid slosh control
- Crane and hoist anti-sway control
- Cantilevered load vibration suppression
- Robot end effector oscillation
- Material and web handling
- Unidirectional anti-backup applications
- Repetitive motion profiles
- Belt and chain driving applications

## Position Reference Motion Planner

This section describes how to use the Point-To-Point (PTP) Position Reference Motion Planner. Instructions are given on how to configure each of the new features in the order they are listed in the first section. A block diagram of the PTP Planner is given, showing relevant parameters.

Figure 35 - PTP Planner Block Diagram

<!-- image -->

## Step 1—Configure Move Type

Adjust parameters described in the following table to setup the base PTP move profile.

Table 24 - PTP Configuration Parameters

|                              | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:931 [Ref Move Type]    | Select the move type used for generating position and velocity reference commands. ‘LinScurve’ (0) – Selects the Linear move type with optional S-curve smoothing. This is the LinScurve move type used in 750 series drives. ‘SineSquared’ (1) – Selects the Sine Squared move type. This produces the smoothest possible motion to reduce mechanical wear. ‘Poly5’ (2) – Selects the Fifth Order Polynomial move type. This produces smooth motion, but trades some smoothness at the beginning and end of each move for lower peak dynamics. ‘Cubic’ (3) – Selects the Cubic move type. This is Third Order Polynomial move type that is similar to LinScurve, however it can leverage new features and can be adjusted by 10/ 11:932 [RefEnergyBalance] through 10/11:941 [Ref Fault Config]. |
| 10/11:941 [Ref Fault Config] | Select the drive action for position and velocity reference commands when 10/11:1410 [PTP Move Status], bit 4 [Move Failed] = 1 or 10/11:1938 [VRef Move Status], bit 4 [Move Failed] = 1. ‘Ignore’ (0) – No action is taken ‘Alarm’ (1) – A Type 1 Alarm is indicated ‘Flt Minor’ (2) – A minor fault is indicated. The drive continues to run if it is currently running. ‘FltCoastStop’ (3) - A major fault indicated. The drive coasts to a stop if it currently running. ‘Flt CL Stop’ (4) - A major fault indicated. The drive does a current limit to a stop if it currently running. This value only affects commands that are generated when 10/11:931 [Ref Move Type] =                                                                                                                 |
| 10/11:1381 [PTP Control]     | Sets and clear bits to control the point-to-point position planner. Bit 0 ‘Vel Override’ – Applies the velocity override in 10/11:1402 [PTP Vel Override] to the forward velocity limit in 10/11:1392 [Max Speed Fwd] and the reverse velocity limit in 10/ 11:1393 [Max Speed Rev] as a gain. When the velocity override in 10/11:1402 [PTP Vel Override] is 1.1 and the forward velocity limit in 10/11:1392 [Max Speed Fwd] is 30 Hz, the bit sets the maximum forward velocity to 33 Hz. Bit 1 ‘Move’ – Sets scaled point-to-point position reference to the point-to-point point reference in 10/11:1391 [PTP Command]. When the point-to-point mode selection in 10/ 11:1382 [PTP Mode] is absolute mode (Option 0), the absolute position is set to the point-to point reference in 10/11:1391 [PTP Command] when this bit rises. When the point-to-point mode selection in 10/11:1382 [PTP Mode] is index mode (Option 1), the index position is set to the point-to-point reference in 10/11:1391 [PTP Command] when this bit rises. Bit 2 ‘Reverse Move’ – Changes direction of the index position when the point-to-point mode selection in 10/11:1382 [PTP Mode] is index mode (1). Set the direction with this bit, then set bit 1 ‘Move” to 1 to move. Bit 3 ‘Preset Psn’ – Sets index preset 10/11:1386 [PTP Index Preset] to the point-to-point position command 10/11:1391 [PTP Command] when the point-to-point mode selection 10/11:1382 [PTP Mode] is index mode (1). Bit 4 ‘Intgrtr Hold’ – Holds integrator in the velocity control. Bit 5 ‘Ref Pause’ – Pauses the point-to-point control function. The point-to-point speed forward reference becomes zero, and the position selected reference in 10/11:1684 [PRef Selected] keeps the current position. Bit 6 ‘Ref Sync’ – Sets initial value to the point-to-point feedback in 10/11:1396 [PTP Feedback]. When motor feedback reaches zero speed, the planner resets 10/11:1404 [PTP Reference] and 10/11:1396 [PTP Feedback] to 10/11:1745 [Position Actual].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10/11:1382 [PTP Mode]        | Enter a value to select the mode of the Point to Point Position Planner function: ‘Absolute’ (0) – selects the absolute position mode. When the move bit is set the planner moves the scaled position reference to the position command. ‘Index’ (1) – Selects index position mode. When 10/11:1381 [PTP Control] bit 1 ‘Move’ is set, the reference source, selected by 10/11:1383 [PTP Ref Sel], is multiplied by 10/11:1385 [PTP Ref Scale] and 10/11:1391 [PTP Command] is incremented by the result. ‘Immediate’ (2) – Selects absolute immediate position mode. When 10/11:1381 [PTP Control] bit 1 ‘Move’ is set, and the reference source selected by 10/11:1383 [PTP Ref Sel] changes, 10/11:1391 [PTP Command] is immediately set.                                                      |

10/11:931 [Ref Move Type] provides a selection of useful move profile types with easy switching between them.

When 10/11:931 [Ref Move Type] = 0 'LinScurve', it provides the standard motion profile type used in 750 series drives. A similar move can be generated simply by selecting a different move type. Figure 36 shows different move types for a 10,000 count index move with 1 second acceleration and deceleration times and a maximum velocity of 150 RPM (5Hz for an 1800 RPM motor).

Figure 36 - Index Moves with Different Move Types

<!-- image -->

## Note the following relationships:

- Sine Squared is the smoothest. It trades maximum velocity and acceleration for smoothness.
- Poly5 trades end point smoothness for lower maximum velocity, maximum acceleration, minimum jerk, and energy.
- LinScurve and Cubic are the least smooth. They generate trapezoidal moves and trade smoothness for lower maximum jerk.

## Step 2—Configure Move Distance

Adjust parameters described in the following table to define your target distance. You can enter a constant set point or select an input signal. Note that as an input signal changes, the PTP reference motion planner acts as a filter with a combined cam-on-cam effect.

Table 25 - PTP Distance Parameters

|                               | Parameter Description                                                                                                                                                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1383 [PTP Ref Sel]      | Select a source for the Point to Point Position Planner reference. Select the port and parameter of the source.                                                                                                                                |
| 10/11:1384 [PTP Setpoint]     | Enter a value to set a constant Point to Point Position Planner reference. You can select this parameter as a source for the Point to Point Position Planner reference in 10/11:1385 [PTP Ref Scale].                                          |
| 10/11:1385 [PTP Ref Scale]    | Enter a value to set the scale value for the Point to Point Position Planner reference. The planner multiplies this value with the reference selected by 10/11:1383 [PTP Ref Sel].                                                             |
| 10/11:1386 [PTP Index Preset] | Enter a constant value to set the Preset Index step size. The planner uses this as the step size (in index mode) when 10/11:1381 [PTP Control] bit 3 ‘Preset Psn’ is set.                                                                      |
| 10/11:1391 [PTP Command]      | Displays the position command produced by the Point to Point Position function. The Point to Point Position Planner consumes this signal in order to produce the Velocity Feed Forward signal and the final Point to Point Position Reference. |

## Step 3—Configure Move Time

Overall move time is segmented into two times: acceleration time and deceleration time. Acceleration time is applied when a trajectory is moving away from zero velocity, while deceleration time is applied when moving toward zero velocity. There are two ways to configure move time. Parameter 10/11:933 [Ref Time Base] can be set to 'Rate' or 'Time'.

## Rate Based Move

When 10/11:933 [Ref Time Base] = 'Rate', acceleration and deceleration times are calculated as a function of target distance and parameters in the following table. This is standard functionality in 750 series drives.

Table 26 - PTP Rate Based Move Parameters

|                               | Parameter Description                                                                                                                                                                                                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:933 [Ref Time Base]     | Select how acceleration and deceleration times are calculated for position and velocity reference commands. ‘Rate’ (0) – Calculates acceleration and deceleration rates equivalent to LinScurve behavior. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |
| 10/11:1392 [Max Speed Fwd]    | Enter the maximum forward speed limit coming from the position reference.                                                                                                                                                                                                                                                          |
| 10/11:1393 [Max Speed Rev]    | Enter the maximum reverse speed limit coming from the position reference.                                                                                                                                                                                                                                                          |
| 10/11:1398 [PTP Accel Time]   | Enter the acceleration ramp time used by the Point to Point (PTP) position planner. This value is the time to go from zero to the velocity in 10/11:1392 [Max Speed Fwd].                                                                                                                                                          |
| 10/11:1399 [PTP Decel Time]   | Enter the deceleration ramp time used by the Point to Point (PTP) position planner. This value is the time to go from the velocities in 10/11:1392 [Max Speed Fwd] or 10/11:1393 [Max Speed Rev] to zero.                                                                                                                          |
| 10/11:1402 [PTP Vel Override] | Enter a value to set the multiplier to both forward parameters 10/11:1392 [Max Speed Fwd] and 10/11:1393 [Max Speed Rev]. This parameter applies to the speed limits when Bit 0 ‘Vel Override’ of 10/11:1381 [PTP Control] is set.                                                                                                 |
| 10/11:1403 [PTP S Curve]      | Enter a value to set the S-curve duration for Point-to-Point (PTP) position reference commands. This value is used to calculate acceleration and deceleration rates equivalent to LinScurve behavior when 10/11:933 [Ref Time Base] = ‘Rate’.                                                                                      |

Figure 37 shows different distances for a LinScurve indexing move with 1 second acceleration and deceleration rates and a maximum velocity of 150 RPM (5Hz for an 1800 RPM motor).

Figure 37 - Rate Based Index Moves with Different Distances

<!-- image -->

Note the following relationships:

- Acceleration and deceleration times are calculated based on a constant maximum acceleration (velocity rate).

- Once the move distance increases enough to hit maximum velocity 10/11:1392 [Max Speed Fwd], the acceleration rate remains constant.
- Rate based move times are good when continually indexing to various target distances.

## Time Based Move

When 10/11:933 [Ref Time Base] = 'Time', you can enter acceleration and deceleration times directly using parameters in the following table. However, this only affects commands that are generated when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'. Rate based calculations are always applied when 10/11:931 [Ref Move Type] = 'LinScurve'.

Table 27 - PTP Time Based Move Parameters

|                            | Parameter Description                                                                                                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:933 [Ref Time Base]  | Select how acceleration and deceleration times are calculated for position and velocity reference commands. ‘Time’ (1) – 10/11:934 [Ref Accel Time] and 10/11:935 [Ref Decel Time] are applied directly as acceleration and deceleration times. |
| 10/11:934 [Ref Accel Time] | Enter the acceleration time that is directly applied to position and velocity reference commands when P933 [Ref Time Base] = ‘Time’.                                                                                                            |
| 10/11:935 [Ref Decel Time] | Enter the deceleration time that is directly applied to position and velocity reference commands when P933 [Ref Time Base] = ‘Time’.                                                                                                            |

You can completely decouple acceleration and deceleration parts of a move, making it easier to generate asymmetric move profiles.

Figure 38 - Asymmetric Index Moves

<!-- image -->

## Note the following relationships:

- Asymmetry trades maximum acceleration and jerk for minimum acceleration and jerk
- Asymmetry lets you adjust maximum and minimum acceleration and jerk times
- Asymmetry does not affect energy directly

## Step 4—Configure Dynamic Limits (optional)

Adjust parameters described in the following table to set and balance dynamic limits. Parameters 10/11:1392 [Max Speed Fwd] and 10/11:1393 [Max Speed Rev] apply to all move types, while the remaining parameters apply when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

Table 28 - PTP Dynamic Limit and Balance Parameters

|                              | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1392 [Max Speed Fwd]   | Enter the maximum forward speed limit coming from the position reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 10/11:1393 [Max Speed Rev]   | Enter the maximum reverse speed limit coming from the position reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 10/11:936 [Ref Max Accel]    | Enter the maximum acceleration limit for position and velocity reference commands. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                        |
| 10/11:937 [Ref Max Decel]    | Enter the maximum deceleration limit for position and velocity reference commands. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                        |
| 10/11:932 [RefEnergyBalance] | Enter a skew factor applied to position and velocity reference commands that shifts the acceleration and deceleration peaks forward or backward in time. A lower value allows the acceleration peak to occur at lower velocity for saving energy. A higher value allows the acceleration peak to occur at higher velocity for more aggressive moves. The deceleration peak mirrors the acceleration peak. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |

Limits are typically set high to protect drive systems from dynamics they cannot handle. Slower moves are unaffected by limits, however move dynamics approach limits and then become limited as move times are decreased or move distance is increased.

You can also apply limits proactively by intentionally lowering them to balance dynamics and energy. When limited, a dwell is added to ensure the correct area under the curve and therefore the correct trajectory. The final move time is automatically increased for best performance if required when inputs generate constrained circumstances. Moves will smoothly transition in and out of velocity and acceleration limits when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

The following example shows what happens when acceleration and deceleration limits are lowered below what is required by an unconstrained 2 second move.

Figure 39 - Acceleration Limiting

<!-- image -->

Acceleration and deceleration times can be readjusted to make up for the added dwell time if required. However, times quickly go to zero when the limit approaches about half the required maximum acceleration because the area under the curve becomes square. Any further

lowering of the limit beyond this point forces a velocity dwell to be added, which increases acceleration and deceleration times.

Figure 40 - Acceleration Limiting with Adjusted Times

<!-- image -->

## Note the following relationships:

- Acceleration Limiting trades maximum jerk for lower maximum acceleration
- Acceleration Limiting automatically induces acceleration dwells with smooth transitions, which extends the move time
- Acceleration Limiting does not affect energy directly

The following example shows what happens when velocity limits are lowered below what is required by an unconstrained move with adjusted acceleration and deceleration times.

Figure 41 - Velocity Limiting with Adjusted Times

<!-- image -->

## Note the following relationships:

- Velocity Limiting trades maximum acceleration and jerk for lower maximum velocity and energy
- Velocity Limiting automatically induces a velocity dwell with a smooth transition, which extends the move time
- Velocity Limiting affects energy directly

The following example shows the effect of Energy Balance.

Figure 42 - Energy Balance

<!-- image -->

## Note the following relationships:

- Energy Balance moves the maximum acceleration point horizontally so that it occurs lower or higher in velocity
- For PTP moves, Energy Balance adjusts maximum velocity to balance out area under the curve, which affects energy directly
- For PTP moves, Energy Balance trades max jerk for lower maximum velocity, maximum acceleration, and energy
- Energy Balance does not induce dwells or extend move time

## Step 5—Monitor Outputs (optional)

Parameters described in the following table are used to monitor the shape and behavior of the configured move profile. Parameters 10/11:1404 [PTP Reference] and 10/11:1405 [PTP VRef Fwd] apply to all move types, while the remaining parameters apply when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

Table 29 - PTP Output Parameters

|                            | Parameter Description                                                                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1404 [PTP Reference] | Displays the position reference output of the Point to Point Position Planner. This is the final Point to Point Position Reference. It becomes the position reference for the Position Regulator.     |
| 10/11:1405 [PTP VRef Fwd]  | Displays the velocity reference output of the Point to Point Position Planner. It becomes the velocity reference for the Velocity Regulator.                                                          |
| 10/11:1406 [PTP Vel Max]   | Displays the maximum velocity of the most recent position reference command. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |

Table 29 - PTP Output Parameters (Continued)

|                              | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1407 [PTP Accel Max]   | Displays the maximum acceleration of the most recent position reference command. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10/11:1408 [PTP Decel Max]   | Displays the maximum deceleration of the most recent position reference command. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10/11:1409 [PTP Move Time]   | Displays the total time required to complete the most recent position reference command. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 10/11:1410 [PTP Move Status] | Displays the status of the most recent position reference command. Bit 0: ‘Vel Limited’ – Indicates velocity is limited. Bit 1: ‘AccelLimited’ – Indicates acceleration is limited. Bit 2: ‘DecelLimited’ – Indicates deceleration is limited. Bit 3: ‘Zero Move’ – Indicates that the new command calculated is zero (no move). Bit 4: ‘Move Failed’ – Indicates that the new command calculation failed. See 10/11:941 [Ref Fault Config] to select the drive response when this condition is true. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                               |
| 10/11:1411 [PTP Move Seg]    | Displays the move segment composition (general shape) of the most recent position reference command. ‘Accel Decel’ (0) – Indicates the command accelerates to a peak velocity with an optional dwell, followed by decelerating to the specified value. ‘Dwell Decel’ (1) – Indicates the command is composed of a dwell at initial velocity, followed by decelerating to the specified value. ‘Decel’ (2) – Indicates the command decelerates to the specified value. ‘Reversing’ (3) – Indicates the command decelerates past the specified value, then reverses direction to the specified value. This condition typically occurs when a command currently in progress is interrupted late by a new move command. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |

Typical trajectories moving from rest to rest accelerate to a peak velocity and then decelerate back to zero. When this occurs, parameter 10/11:1411 [PTP Move Seg] = 'AccelDecel'. However, when a move profile is initiated while another is in motion, the new move will start at an initial velocity matching the velocity of the previous move profile at the point of transition. When the initial velocity is high enough, there may only be time to perform a velocity dwell and decelerate to the new target. When this occurs, parameter 10/11:1411 [PTP Move Seg] = 'DwellDecel'.

Figure 43 - Index Moves with Initial Velocity

<!-- image -->

Initial velocities increase as the target distance becomes closer. In this case, there may only be time to decelerate to the new target or decelerate to the new target while hitting the deceleration limit. When this occurs, parameter 10/11:1411 [PTP Move Seg] = 'Decel' or 'DecelLimited', respectively.

Figure 44 - Index Moves that Decelerate Only

<!-- image -->

Initial velocities can increase so much with respect to the approaching target distance, that there may only be time to decelerate past the new target, then reverse back to it. When this occurs, parameter 10/11:1411 [PTP Move Seg] = 'Reversing'.

Figure 45 - Index Move that Reverses

<!-- image -->

## Velocity Reference Motion Planner

This section describes how to use the Velocity Reference Motion Planner. Instructions are given on how to configure each of the new features in the order they are listed in the first section. A block diagram of the Velocity Reference Planner is given, showing relevant parameters.

Figure 46 - Velocity Reference Planner Block Diagram

<!-- image -->

## Step 1—Configure Move Type

Adjust parameters described in the following table to setup the base Velocity Reference move profile.

Table 30 - Velocity Reference Configuration Parameters

|                               | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:931 [Ref Move Type]     | Select the move type used for generating position and velocity reference commands. ‘LinScurve’ (0) – Selects the Linear move type with optional S-curve smoothing. This is the LinScurve move type used in 750 series drives. ‘SineSquared’ (1) – Selects the Sine Squared move type. This produces the smoothest possible motion to reduce mechanical wear. ‘Poly5’ (2) – Selects the Fifth Order Polynomial move type. This produces smooth motion, but trades some smoothness at the beginning and end of each move for lower peak dynamics. ‘Cubic’ (3) – Selects the Cubic move type. This is Third Order Polynomial move type that is similar to LinScurve, however it can leverage new features and can be adjusted by 10/ 11:932 [RefEnergyBalance] through 10/11:941 [Ref Fault Config].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10/11:941 [Ref Fault Config]  | Select the drive action for position and velocity reference commands when 10/11:1410 [PTP Move Status], bit 4 [Move Failed] = 1 or 10/11:1938 [VRef Move Status], bit 4 [Move Failed] = 1. ‘Ignore’ (0) – No action is taken ‘Alarm’ (1) – A Type 1 Alarm is indicated ‘Flt Minor’ (2) – A minor fault is indicated. The drive continues to run if it is currently running. ‘FltCoastStop’ (3) - A major fault indicated. The drive coasts to a stop if it currently running. ‘Flt CL Stop’ (4) - A major fault indicated. The drive does a current limit to a stop if it currently running. This value only affects commands that are generated when 10/11:931 [Ref Move Type] =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10/11:1950 [Vel Ctrl Options] | Set and clear bits to configure options in the Velocity Regulator. Bit 0 ‘Ramp Hold’ – set this bit to stop the Velocity Reference Ramp from changing and to hold constant. Clear this bit to allow the Velocity Reference Ramp to change. If this bit is set while 10/11:1923 [VRef Ramped] is in an S-curve region, the S-curve completes before the output is held. Bit 1 ‘Ramp Disable’ – Set this bit to bypass the Velocity Reference Ramp. 10/11:1923 [VRef Ramped] tracks the Input to the ramp function. Bit 2 ‘StpNoSCrvAcc’ – Set this bit to force the velocity regulator to immediately discontinue acceleration when the drive receives a stop command. Clear this bit to finish accelerating, as part of the S-curve profile, before decelerating in response to a stop command. Bit 9 ‘NoSCrvSpdChg’ – Set this bit to interrupt the S-curve if the drive is accelerating and a new velocity reference is commanded less than the current velocity. The drive will immediately decelerate. Setting this bit will also interrupt the S-curve if the drive is decelerating when the new velocity reference is more than the current velocity. Clearing this bit configures the drive to complete the S-curve before decelerating or accelerating. Note to Tech Writing use NoSCrvSpdChg figure. Bit 10 ‘FastZeroCrs’ – Set this bit to allow the velocity command to cross zero without ramping to zero acceleration. Clear this bit to generate two moves: a first move that ramps to zero acceleration when approaching zero velocity and a second move to ramp from zero acceleration after crossing zero velocity and move to the final velocity. |

10/11:931 [Ref Move Type] provides a selection of useful move profile types with easy switching between them.

When 10/11:931 [Ref Move Type] = 0 'LinScurve', it provides the standard motion profile type used in 750 series drives. A similar move can be generated simply by selecting a different move type. Figure 47 shows different move types for an 1800 RPM velocity move with a 10 second acceleration time.

Figure 47 - Velocity Moves with Different Move Types

<!-- image -->

## Note the following relationships:

- Sine Squared is the smoothest. It trades maximum jerk and snap for smoothness.
- Poly5 trades end point smoothness for lower maximum acceleration, maximum jerk, and minimum snap.
- LinScurve and Cubic are the least smooth. They generate trapezoidal moves and trade smoothness for lower maximum snap.

## Step 2—Configure Move Target Velocity

Adjust parameters described in the following table to define your move target velocity. You can enter a constant set point or select an input signal. Note that as an input signal changes, the Velocity Reference motion planner acts as a filter with a combined cam-on-cam effect.

Table 31 - Velocity Reference Distance Parameters

|                              | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:354 [Motor Side Sts 1] | Displays the operating condition of the Motor Side Inverter: Bit 9 ‘Manual’ indicates the Auto/Manual function is in the Manual mode. Bit 10 ‘SpdRef Bit 0’ indicates the state of the Speed (Velocity) reference selection bit 0. Bit 11 ‘SpdRef Bit 1’ indicates the state of the Speed (Velocity) reference selection bit 1. Bit 12 ‘SpdRef Bit 2’ indicates the state of the Speed (Velocity) reference selection bit 2. Bit 13 ‘SpdRef Bit 3’ indicates the state of the Speed (Velocity) reference selection bit 3. Bit 14 ‘SpdRef Bit 4’ indicates the state of the Speed (Velocity) reference selection bit 4. These bits work together to select a velocity reference. |
| 10/11:1800 [VRef A Sel]      | Select a source for Velocity Reference A. Select the port and parameter of the source. This is the typical Automatic reference. Digital input functions for and bits in the Logic Command select between Velocity Reference A and Velocity Reference B. A Manual selection will override this.                                                                                                                                                                                                                                                                                                                                                                                  |
| 10/11:1801 [VRef A Stpt]     | Enter a constant value to be used as a source for Velocity Reference A. You can select this constant as a reference in 10/11:1800 [VRef A Sel]. This is similar to using a Preset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 10/11:1804 [VRef A Mult]     | Enter a value to define a multiplier for Velocity Reference A. The value from the source selected by 10/11:1800 [VRef A Sel] will be multiplied by this.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 10/11:1914 [VRef Commanded]  | Displays the value of the Velocity Reference after the Skip Speed function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Step 3—Configure Move Time

Overall move time is segmented into two times: acceleration time and deceleration time. Acceleration time is applied when a trajectory is moving away from zero velocity, while deceleration time is applied when moving toward zero velocity. There are two ways to configure move time. Parameter 10/11:933 [Ref Time Base] can be set to 'Rate' or 'Time'.

## Rate Based Move

When 10/11:933 [Ref Time Base] = 'Rate', acceleration and deceleration times are calculated as a function of target velocity and parameters in the following table. This is standard functionality in 750 series drives.

Table 32 - Velocity Reference Rate Based Move Parameters

|                               | Parameter Description                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:933 [Ref Time Base]     | Select how acceleration and deceleration times are calculated for position and velocity reference commands. ‘Rate’ (0) – Calculates acceleration and deceleration rates equivalent to LinScurve behavior. This value only affects commands that are generated when 10/11:931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                   |
| 10/11:403 [Motor NP RPM]      | Enter the rated RPM shown on the motor nameplate.                                                                                                                                                                                                                                                                                                                                    |
| 10/11:1915 [VRef Accel Time1] | Enter the first acceleration ramp time that is applied to velocity reference commands. This value is defined as the time to accelerate from zero to the value in 10/11:403 [Motor NP RPM]. Digital input functions and bits in the Logic Command select between the first and second ramp times.                                                                                     |
| 10/11:1916 [VRef Accel Time2] | Enter the second acceleration ramp time that is applied to velocity reference commands. This value is defined as the time to accelerate from zero to the value in 10/11:403 [Motor NP RPM]. Digital input functions and bits in the Logic Command select between the first and second ramp times.                                                                                    |
| 10/11:1917 [VRef Decel Time1] | Enter the first deceleration ramp time that is applied to velocity reference commands. This value is defined as the time to decelerate from the value in 10/11:403 [Motor NP RPM] to zero. Digital input functions and bits in the Logic Command select between the first and second ramp times. This value is also used for these stop modes: Ramp, Ramp to Hold, and DecelToHold.  |
| 10/11:1918 [VRef Decel Time2] | Enter the second deceleration ramp time that is applied to velocity reference commands. This value is defined as the time to decelerate from the value in 10/11:403 [Motor NP RPM] to zero. Digital input functions and bits in the Logic Command select between the first and second ramp times. This value is also used for these stop modes: Ramp, Ramp to Hold, and DecelToHold. |
| 10/11:1919 [VRef Accel Jerk]  | Enter the percentage of acceleration time applied to the acceleration ramp of velocity reference commands. Increasing this value softens changes in acceleration and reduce jerk. Half of the time associated with this percentage is added at the beginning of the ramp and half is added at the end of the ramp.                                                                   |
| 10/11:1920 [VRef Decel Jerk]  | Enter the percentage of deceleration time applied to the deceleration ramp of velocity reference commands. Increasing this value softens changes in deceleration and reduce jerk. Half of the time associated with this percentage is added at the beginning of the ramp and half is added at the end of the ramp.                                                                   |

Figure 48 shows different target velocities for a LinScurve velocity move with a 10 second acceleration time.

Figure 48 - Rate Based Velocity Moves with Different Distances

<!-- image -->

## Note the following relationships:

- Acceleration and deceleration times are calculated based on a constant maximum jerk (acceleration rate).
- Rate based move times are good when continually indexing to various target velocities.

## Time Based Move

When 10/11:933 [Ref Time Base] = 'Time', you can enter acceleration and deceleration times directly using parameters in the following table. However, this only affects commands that are generated when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'. Rate based calculations are always applied when 10/11:931 [Ref Move Type] = 'LinScurve'.

Table 33 - Velocity Reference Time Based Move Parameters

|                            | Parameter Description                                                                                                                                                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:933 [Ref Time Base]  | Select how acceleration and deceleration times are calculated for position and velocity reference commands. ‘Time’ (1) – 10/11:934 [Ref Accel Time] and P935 [Ref Decel Time] are applied directly as acceleration and deceleration times. |
| 10/11:934 [Ref Accel Time] | Enter the acceleration time that is directly applied to position and velocity reference commands when 10/11:933 [Ref Time Base] = ‘Time’.                                                                                                  |
| 10/11:935 [Ref Decel Time] | Enter the deceleration time that is directly applied to position and velocity reference commands when 10/11:933 [Ref Time Base] = ‘Time’.                                                                                                  |

Individual acceleration and deceleration times allow you more control over decoupling acceleration and deceleration moves. The following example shows various moves with 5 second acceleration times and 10 second deceleration times.

Figure 49 - Velocity Moves that Accelerate and Decelerate

<!-- image -->

## Note the following relationships:

- Acceleration time is applied when moving away from zero velocity
- Deceleration time is applied when moving towards zero velocity
- When crossing zero velocity and 10/11:1950 [Vel Ctrl Options] bit 10 'FastZeroCrs' is not set, two independent moves are created: one move decelerates to zero velocity and acceleration, while a second move accelerates to the final velocity target. However, when 10/11:1950 [Vel Ctrl Options] bit 10 'FastZeroCrs' is set, one move will accelerate through zero velocity from initial to final target.
- Both acceleration and deceleration times are applied when crossing zero velocity. When 10/11:933 [Ref Time base] = 'Time', these times are simply added during fast zero crossing.

Step 4—Configure Dynamic Limits (optional)

Adjust parameters described in the following table to set and balance dynamic limits. Parameters apply when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

Table 34 - Velocity Reference Dynamic Limit and Balance Parameters

|                              | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:936 [Ref Max Accel]    | Enter the maximum acceleration limit for position and velocity reference commands.                                                                                                                                                                                                                                                                                                                        |
| 10/11:937 [Ref Max Decel     | Enter the maximum deceleration limit for position and velocity reference commands.                                                                                                                                                                                                                                                                                                                        |
| 10/11:938 [Ref Max AccJerk]  | Enter the maximum jerk limit during acceleration for velocity reference commands. It is the change of acceleration with respect to time.                                                                                                                                                                                                                                                                  |
| 10/11:939 [Ref Max DecJerk]  | Enter the maximum jerk limit during deceleration for velocity reference commands. It is the change of deceleration with respect to time.                                                                                                                                                                                                                                                                  |
| 10/11:932 [RefEnergyBalance] | Enter a skew factor applied to position and velocity reference commands that shifts the acceleration and deceleration peaks forward or backward in time. A lower value allows the acceleration peak to occur at lower velocity for saving energy. A higher value allows the acceleration peak to occur at higher velocity for more aggressive moves. The deceleration peak mirrors the acceleration peak. |

Limits are typically set high to protect drive systems from dynamics they cannot handle. Slower moves are unaffected by limits, however move dynamics approach limits and then become limited as move times are decreased or move distance is increased.

You can also apply limits proactively by intentionally lowering them to balance dynamics and energy. When limited, a dwell is added to ensure the correct area under the curve and therefore the correct trajectory. The final move time is automatically increased for best performance when inputs generate constrained circumstances. Moves will smoothly transition in and out of acceleration and jerk limits when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

The following example shows what happens when minimum and maximum jerk limits are lowered below what is required by an unconstrained 10 second move.

## Figure 50 - Jerk Limiting

<!-- image -->

Acceleration and deceleration times can be readjusted to make up for the added dwell time if required. However, times quickly go to zero when the limit approaches about half the required maximum jerk because the area under the curve becomes square. Any further lowering of the limit beyond this point forces an acceleration-dwell to be added, which increases acceleration and deceleration times.

Figure 51 - Jerk Limiting with Adjusted Times

<!-- image -->

## Note the following relationships:

- Jerk Limiting trades maximum snap for lower maximum jerk
- Jerk Limiting automatically induces jerk dwells with smooth transitions, which extends the move time
- Jerk Limiting does not affect energy directly

The following example shows what happens when acceleration limits are lowered below what is required by an unconstrained move with adjusted acceleration time.

Figure 52 - Acceleration Limiting with Adjusted Times

<!-- image -->

## Note the following relationships:

- Acceleration Limiting trades maximum jerk and snap for lower maximum acceleration
- Acceleration Limiting automatically induces an acceleration dwell with a smooth transition, which extends the move time
- Acceleration Limiting does not affect energy directly

The following example shows the effect of Energy Balance.

Figure 53 - Energy Balance

<!-- image -->

## Note the following relationships:

- Energy Balance moves the maximum acceleration point horizontally so that it occurs lower or higher in velocity
- For Velocity moves, target velocity is unaffected and, as a result, energy is unaffected
- Energy Balance does not induce dwells or extend move time
- For Velocity moves, Energy Balance creates asymmetry
- Asymmetry trades maximum acceleration and jerk for minimum acceleration and jerk
- Asymmetry lets you adjust maximum and minimum acceleration and jerk times

## Step 5—Monitor Outputs (Optional)

Several parameters described in the following table are used to monitor the shape and behavior of the configured move profile. Parameter 10/11:1923 [VRef Ramped] applies to all move types, while the remaining parameters apply when 10/11:931 [Ref Move Type] = 'SineSquared', 'Poly5', or 'Cubic'.

Table 35 - Velocity Reference Output Parameters

|                               | Parameter Description                                                                                                                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1923 [VRef Ramped]      | Displays the value of the Velocity Reference after the Ramp and Jerk functions.                                                                                                                                         |
| 10/11:1934 [VRef Accel Max]   | Displays the maximum acceleration of the most recent velocity reference command. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                    |
| 10/11:1935 [VRef AccJerk Max] | Displays the maximum jerk in the acceleration region of the most recent velocity reference command. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |

Table 35 - Velocity Reference Output Parameters (Continued)

|                               | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/11:1936 [VRef DecJerk Max] | Displays the maximum jerk in the deceleration region of the most recent velocity reference command. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 10/11:1937 [VRef Move Time]   | Displays the total time required to complete the most recent velocity reference command. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10/11:1938 [VRef Move Status] | Displays the status of the most recent velocity reference command. Bit 0: ‘AccelLimited’ – Indicates acceleration is limited. Bit 1: ‘AccelJerkLim’ – Indicates acceleration jerk is limited. Bit 2: ‘DecelJerkLim’ – Indicates deceleration jerk is limited. Bit 3: ‘Zero Move’ – Indicates that the new command calculated is zero (no move). Bit 4: ‘Move Failed’ – Indicates that the new command calculation failed. See P941 [Ref Fault Config] to select the drive response when this condition is true. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’.                                                                                                                                                                                                            |
| 10/11:1939 [VRef Move Seg]    | Displays the move segment composition (general shape) of the most recent velocity reference command. ‘Accel Decel’ (0) – Indicates the command accelerates to a peak acceleration with an optional dwell, followed by decelerating to the specified value. ‘Dwell Decel’ (1) – Indicates the command is composed of a dwell at initial acceleration, followed by decelerating to the specified value ‘Decel’ (2) – Indicates the command decelerates to the specified value. ‘Reversing’ (3) – Indicates the command decelerates past the specified value, then reverses direction to the specified value. This condition typically occurs when a command currently in progress is interrupted late by a new move command. This value only affects commands that are generated when P931 [Ref Move Type] = ‘SineSquared’, ‘Poly5’, or ‘Cubic’. |

Typical trajectories moving from constant velocity to constant velocity accelerate to a peak acceleration and then decelerate back to zero. When this occurs, parameter 10/11:1939 [VRef Move Seg] = 'AccelDecel'. However, when a move profile is initiated while another is in motion, the new move will start at an initial acceleration matching the acceleration of the previous move profile at the point of transition. When the initial acceleration is high enough, there may only be time to perform an acceleration dwell and decelerate to the new target. When this occurs, parameter 10/11:1939 [VRef Move Seg] = 'DwellDecel'.

Figure 54 - Velocity Moves with Initial Acceleration

<!-- image -->

Initial accelerations increase as the target velocity becomes closer. In this case, there may only be time to decelerate to the new target or decelerate to the new target while hitting the

jerk limit. When this occurs, parameter 10/11:1939 [VRef Move Seg] = 'Decel' or 'DecelLimited', respectively.

Figure 55 - Velocity Moves that Decelerate Only

<!-- image -->

Initial accelerations can increase so much with respect to the approaching target velocity, that there may only be time to decelerate past the new target, then reverse velocity back to it. When this occurs, parameter 10/11:1939 [VRef Move Seg] = 'Reversing'.

Figure 56 - Velocity Move that Reverses

<!-- image -->

## AC Line Commissioning

<!-- image -->

## Active Front End TotalFORCE Control

This chapter discusses commissioning and configuration of Active Front End converters in TotalFORCE® control. Active Front End products with TotalFORCE control include the PowerFlex® 755TL and 755TR drives, and PowerFlex 755TM regenerative bus supplies.

| Topic Page                                               |
|----------------------------------------------------------|
| AC Line Commissioning 119                                |
| Droop Control for Parallel Operation of Bus Supplies 121 |
| AC Line Tuning 124                                       |
| Backup Generator Configuration 130                       |

This section covers the steps that are required to tune PowerFlex 755TL, 755TR, and 755TM regenerative and low harmonic converters to one AC supply source. It is a procedural guide for configuration only and therefore excludes the detailed operational information for the parameters being adjusted. Configuration is supported through direct parameter access as detailed in this section or through the Regenerative Converter Setup Wizard accessible through the Studio 5000 Logix Designer® application Add-on Profile or Connected Components Workbench™ software. For more information on tuning the drive to the AC line, see AC Line Tuning on page 124 .

## Basic Configuration

To configure the PowerFlex 755T active front end, enter basic information about the AC Supply. The information is needed so that the drive can calculate the system impedance and adjust the current regulator gains accordingly.

1. Enter the nominal AC line frequency in 13:30 [Nom Line Freq]
2. Verify that the selected AC Line Source in 13:31 [AC Line Source] is set to 'AC Line A'
3. Enter the apparent power rating of the mains AC Supply transformer in 13:32 [AC Line kVA A].
4. Enter the percent impedance of the mains AC Supply transformer in 13:34 [AC Line Imped% A].

## External DC Bus Capacitance

In common bus installations and some applications, there is more capacitance that is connected to the bus than the inverter is pre-configured to operate with. If the application does not have additional bus capacitance, skip this step.

The PowerFlex 755T regenerative and low harmonic products have a couple of methods to address this additional capacitance. If the additional capacitance value is known, it can be directly inputted into the inverter configuration. If the actual value is not known, the Bus Observer feature can be enabled to compensate for the additional capacitance automatically. For more information see Bus Observer on page 53 .

5. Enter the additional capacitance value in 13:52 [Ext Bus Cap]

And/or

Enable the Bus Observer Feature by setting parameter 13:320 [BusObs Config] to 1 'BusObs Only'

## Limits

For most applications, the converter limits do not need to be modified from their default values. If your application requires more restrictive limits, follow these steps to reduce the settings. For more information about the converter limits, see the PowerFlex Drives with TotalFORCE Control Programming manual, publication 750-PM101 .

6. Verify and adjust as required the Converter Current Limit in 13:100 [Current Limit].
7. Verify and adjust as required the Regenerative Power Limit in 13:104 [Regen Power Lmt].
8. Verify and adjust as required the Motoring Power Limit in 13:105 [Motor Power Lmt].

## Start Mode and Reference Source

While the defaults setting works in most applications, PowerFlex 755T products allow for different converter start modes and DC bus voltage reference sources. See the PowerFlex Drives with TotalFORCE Control Programming manual, publication 750-PM101 for an explanation of the available options. For guidance on applications that would benefit from non-default settings, see the Drives in Common Bus Configurations with PowerFlex 755T Bus Supplies Application Technique, publication DRIVES-AT005 .

9. Select the desired Line Side Start Mode in 0:63 [LS Start Mode].
10. Select the desired DC bus voltage reference source in 13:45 [DC Bus Ref Sel].

## Tuning

For many applications, the default settings work well. In installations with higher system impedance, the default settings can cause resonance current in the LCL filters. There are two approaches for reducing this resonance.

The first is to de-tune by adjusting the voltage and current bandwidths and the second is to use the Active Damping feature. Both methods require you to monitor the band pass filter current and adjust until the current is below the fault threshold values that are specified in the tables in the AC Line Tuning section of this manual. For optimum performance, it is possible to use a combination of de-tuning and Active Damping.

Review tuning for both sources. Ideally, there is a combination that works for both the AC line and the generator. If not, the bandwidths and/or Active Damping values can be changed based on the currently selected AC source through datalinks.

11. Start the drive. It is preferable that the motor is connected to the load for the remaining steps.
12. Monitor the LCL resonance current in parameters 14:1216 [F0 Cap BPF Cur R], 14:1217 [F0 Cap BPF Cur S], and 14:1218 [F0 Cap BPF Cur T], and the bus voltage in parameter 14:109 [L0 DC BusVoltage].
13. Slowly adjust 13:55 [Volt Reg BW] and 13: 75 [Cur Reg BW] down by the same percentage until the resonance current is below the fault levels.
4. Or, slowly reduce 13:81 [Actv Damping Gain] until the resonance current is below the fault levels.
14. Verify that the Bus Voltage is holding at the desired level without too much fluctuation. If not, repeat step 7 but use the other method or a combination of the two until the resonance current is below the fault level and bus voltage is maintaining a steady level.
15. Stop the drive.

Configuration is complete.

## Droop Control for Parallel Operation of Bus Supplies

## Regenerative Converter Setup Wizard

Except for the tuning section, use the Regenerative Converter Setup Wizard in Connected Components Workbench software for configuration. The wizard groups the commonly modified parameters to help expedite the commissioning process. If the wizard shown here is used, perform the Tuning section steps afterward to avoid LCL filter resonance.

<!-- image -->

Droop control of the DC bus voltage reference level is an internal process for sharing the load between multiple AFE bus supplies that are working in parallel to energize a common DC bus. Droop control provides consistent current and power sharing between converters so that one converter is not subjected to a larger share of the load than the other converters. To enable droop control in the PowerFlex 755T, set parameter 13:45 [DC Bus Ref Sel] to 2 'Droop Ctrl'.

## Overview

As the load on the bus supplies increases, the droop function manages DC bus voltage evenly between the parallel bus supplies. The droop function manipulates the DC bus voltage reference to control the output current from each bus supply. Droop control manipulates the DC bus voltage reference so that a bus supply can produce a larger share of current when the load is low and a smaller share of current when the load is high.

In the motoring direction, droop control increases the DC bus voltage reference as the active current reference decreases in magnitude. As the active current reference increases towards full load, droop control decreases the DC bus reference towards the minimum DC bus voltage. The DC bus voltage reference is greater when near zero load than it is when near full load. In this way, the AFE bus supply tends to increase its share near zero load, and is less likely to increase its share near full load.

In the regenerating direction, droop control increases the DC bus voltage reference as the active current reference increases in magnitude (becomes more negative). As the magnitude increases toward full negative load, droop control increases the DC bus reference. The DC bus voltage reference is lower when near zero load than it is when near full negative load. In this way, the AFE bus supply tends to increase its share near zero load, and is less likely to increase its share near full negative load.

In this simple example (Figure 57), we want AFE bus supply #1 to provide roughly the same amount of current and power to the shared bus as AFE bus supply #2. One cannot be certain the impedance from the mains to the shared DC bus is the same between AFE bus supply #1 and AFE bus supply #2. Any impedance mismatch can lead to a mismatch in current and power delivery. If the path through AFE bus supply #1 has a lower impedance, then AFE bus supply #1 delivers more power than AFE bus supply #2. Differences in loading can produce issues with component wear and reliability, which can result in unplanned downtime.

Figure 57 - Shared Bus Supply

<!-- image -->

Shared DC Bus

## Modes of Operation

There are two modes of operation: Linear and Nonlinear. The default mode of operation is Linear. To change the mode of operation in the PowerFlex 755T, adjust parameter 13:350 [DroopCtrlModeSel].

## Linear Mode

The Linear Mode uses a piecewise linear function to determine the DC bus voltage reference. In this function, the active current reference is the input (X-axis). The DC bus voltage reference is the output (Y-axis).

Figure 58 - Linear Mode

Regenerating

<!-- image -->

Minimum DC bus voltage reference is the same as the automatic (optimized) DC bus voltage reference. This is 2% above the peak of the naturally rectified voltage level. For example, if the incoming voltage is 480 V rms , then minimum DC Bus voltage reference is 692.4V DC (VDC = VRMS x SQRT(2) x 1.02).

There are four regions of operation. The Motoring Full Load region is between positive 'Trans Droop Current' and positive full load current. The Motoring No Load region is between zero current and positive 'Trans Droop Current'. The Regen No Load region is between zero current and negative 'Trans Droop Current'. The Regen Full Load region is between negative 'Trans Droop Current' and negative full load current. The value in parameter 13:353 [Trans Droop Cur] defines the positive and negative 'Trans Droop Current' points on the X-axis.

Regenerating

Regenerating

You determine the horizontal boundaries of the regions by entering the value of parameter 13:353 [Trans Droop Cur]. This value determines the locations of the inflection points on DC bus voltage droop curve.

In the Motoring Full Load and Regen Full Load regions, the value in parameter 13:351 [FullLd DroopGain] determines the slope of the curve. Set the value of this parameter as percent increase in DC bus voltage reference (percent of minimum DC bus voltage) over the positive current range (zero load to full load).

In the Motoring No Load and Regen No Load regions, the value in parameter 13:352 [NoLd DroopGain] determines the slope of the curve. Set the value of this parameter as percent increase in DC bus voltage reference (percent of minimum DC bus voltage) over the positive current range (zero load to full load).

Figure 59 - Full Load Regions

<!-- image -->

## Nonlinear Mode

The Nonlinear Mode uses a continuous curve to determine the DC bus voltage reference. The function builds a slope curve using two of the parameters from the Linear Mode. These are 13:351 [FullLd DroopGain] and 13:352 [NoLd DroopGain]. It builds the slope curve with a slope at full load equal to 1.2 x 13:351 [FullLd DroopGain] and the slope at the no load point equal to 0.3 x 13:352 [NoLd DroopGain].

Figure 60 - Nonlinear Mode

<!-- image -->

This results in a smooth and progressive curve for the DC bus voltage reference.

## AC Line Tuning

Regenerating

Figure 61 - DC Bus Voltage Reference

<!-- image -->

## Derating for Voltage Boost

In standalone operation (not parallel), PowerFlex 755TM bus supplies are designed to operate with the DC bus voltage reference equal to the optimized or minimum DC bus level. This optimization maximizes energy efficiency. Because the Droop function raises the DC bus voltage reference, you must account for this when sizing the bus supplies.

Consider the DC bus voltage reference at full load in the regenerating direction with default values. The reference at that operating point is:

Minimum DC Bus Voltage + (No Load Droop Gain/100) x Minimum DC Bus Voltage + (Full Load Droop Gain/100) x Minimum DC Bus Voltage Or

Minimum DC Bus Voltage x [1 + (No Load Droop Gain/100) + (Full Load Droop Gain/100)]

Consider a 480V rms example with default values in the gain parameters.

- Minimum DC Bus Voltage = 480 x SQRT(2) x 1.02 = 692.4V DC
- No Load Droop Gain = 1%
- Full Load Droop Gain = 5%
- Trans Droop Cur = 50%
- DC bus voltage reference = 692.4 x (1 + 0.01 + 0.05) = 733.9V DC

This is a considerable boost to the DC bus voltage. For information about derating for this, see PowerFlex 750-Series Products with TotalFORCE Control, publication 750-TD100 .

PowerFlex 755T regenerative and low harmonic AFE products have parameters that tune the converter to the AC supply. Tuning lets the converter work reliably with a wider range of supplies. You can also configure the converter to switch between two different supplies, which supports the use of backup generators without having to reconfigure the system.

## Overview

The goal of tuning the PowerFlex 755T converter is to obtain a robust bus supply that provides protection against under voltage and over voltage conditions without causing resonance or instability. In addition,

- The converter can be configured for two AC line sources to facilitate the use of a backup generator.
- The robust default current regulator and voltage regulator bandwidths work well in most installations.
- Gains automatically adjust to the line impedance of two different AC line sources.

- The converter can switch between AC line sources with limited interaction.
- Via HIM, Connected Components Workbench software, and Datalinks – all versions
- Digital Input – firmware revision 4 and later
- The converter tuning capabilities and features of PowerFlex 755T products accommodate one AC line source or a primary source with a backup generator.

## AC Source Configuration

The first step to configure the converter is to specify some basic information about the AC source. This basic information is used to calculate the system impedance, which is used to calculate the current regulator gains automatically. Table 36 shows the basic AC line source information required.

Table 36 - AC Line Source Data

| Parameter No. Parameter Name Definition                        |
|----------------------------------------------------------------|
| 13:30 Nom Line Freq 0 = 50 Hz, 1 = 60 Hz                       |
| 13:31 AC Line Source 0 = AC Line A, 1 = AC Line B              |
| 13:32 AC Line kVA A Apparent Power Rating for AC Line Source A |
| 13:33 AC Line kVA B Apparent Power Rating for AC Line Source B |
| 13:34 AC Line Imped% A Impedance of AC Line Source A in %      |
| 13:35 AC Line Imped% B Impedance of AC Line Source B in %      |

System impedance is derived from this information. The converter operates best when system impedance is less than 10%. Use this equation to calculate system impedance.

<!-- formula-not-decoded -->

The Line Source A and Line Source B parameters accommodate situations where the system is powered by two separate sources. An example is when the system has a backup generator that switches on when the main AC line loses power.

If the drive is not going to be powered by different sources, populate only one set of line source data (A or B). Which set is populated does not matter as long as 13:31 [AC Line Source] is pointing to the set with the correct line information.

## External Bus Capacitance

When tuning the converter, some analogies can be made to tuning the inverter. One analogy is the similarity between external bus capacitance and load inertia. Just like inertia resists changes in velocity on the motor side, bus capacitance resists changes in DC Bus Voltage on the line side. Having the correct external bus capacitance is as important to the Voltage Regulator gains as having the correct load inertia is to the Velocity Regulator gains.

The total system capacitance is used in the automatic calculation of the voltage regulator gains. Total system capacitance is the sum of all capacitance that is connected to the DC bus. The drive knows its own capacitance and automatically accounts for it in the calculations, but it does not know the capacitance of external devices that are connected to the bus. Use parameter 13:52 [Ext Bus Cap] to specify the external capacitance so that the total system capacitance is known. External bus capacitance is the sum of the individual bus capacitance values for each drive and any external bus capacitors that are connected to the DC bus.

## IMPORTANT

Do not overstate the external bus capacitance.

Specifying an external capacitance value that is higher than the actual connected capacitance can cause instability. Also, incorrect values cause a noticeable performance degradation. If you don't know the exact capacitance, specify the value on the low side and use the Bus Observer feature to account for the remaining capacitance. See Bus Observer on page 53 for more information. If the external bus capacitance is largely unknown, enter a zero and enable the bus observer to estimate the entire value.

## Bus Regulators

The converter uses a cascaded control loop for voltage regulation and current regulation. The current regulator is the inner loop and the voltage regulator is the outer loop. This method is similar to the cascaded control loop for torque regulation that is employed on the inverter.

## Voltage and Current Regulator Tuning

After the external bus capacitance is specified, the DC bus voltage and current regulator are tuned by adjusting parameters 13:55 [Volt Reg BW] and 13:75 [Cur Reg BW]. The default bandwidth values of these parameters work for most applications. The regulator gains (K p and K i ) are set to automatically calculate from the voltage regulator bandwidth and current regulator bandwidth. The regulator also supports manually entered gain values.

The automatically calculated gain values for the current regulator are displayed by parameters 13:58 [c Volt Reg Kp] and 13:60 [c Volt Reg Ki]. The automatically calculated gain values for the voltage regulator are displayed by parameters 13:78 [c Cur Reg Kp] and 13:80 [c Cur Reg Ki]. These read-only parameter values are recalculated when their respective bandwidth parameter value is changed.

The spacing between Kp and Ki gains can be varied by adjusting the damping factor with parameter 13:56 [Volt Reg Damping]. By default, the system is critically damped (13:56 [Volt Reg Damping] = 1.000).

If an application has a high impedance supply, the default bandwidths can cause the LCL filter to resonate and requires the converter to be de-tuned. To de-tune, adjust 13:55 [Volt Reg BW] and 13:75 [Cur Reg BW] down by the same percentage. As a rule, the current regulator bandwidth is 10 times larger than the voltage regulator bandwidth (10:1 ratio) to avoid interaction and possible resonance. However, in applications that require a fast dynamic response with a soft line supply, you can reduce the ratio down to 6:1.

A good indication that the converter needs to be de-tuned is the presence of 14117 'CapResonanceArm' and 14118 'CapResonanceFlt' alarms. Monitor 14:1216 [F0 Cap BPF Cur R], 14:1217 [F0 Cap BPF Cur S], and 14:1218 [F0 Cap BPF Cur T] to observe the LCL filter resonance. When de-tuning, lower the bandwidths until these parameters are below the capacitor resonance fault threshold. The thresholds are listed in the following tables.

Table 37 - Capacitor Resonance Fault Thresholds—400/480V Products

| Frame   | 400V ND Rating Codes  (1) 480V ND Rating Codes  (1)  Resonance Current [A] Alarm Fault   |
|---------|------------------------------------------------------------------------------------------|
| 5       | C015…C043 D014…D040 3 4                                                                  |
| 5       | C060…C104 D052…D096 6 7                                                                  |
| 6       | C140, C176 D125, D156 11 14                                                              |
| 6       | C205, C260 D186, D248 18 23                                                              |
|         | 7 C302…C585 D302…D617 23 31                                                              |
| 8       | C302…C540 D302…D505 23 31                                                                |
| 8       | C585…C770 D545…D740 31 41                                                                |
| 9       | C920, C1K0 D800, D960 46 62                                                              |
| 9       | C1K1…C1K4 D1K0…D1K3 62 82                                                                |
|         | 10 C1K6…C2K1 D1K4…D2K0 62 82                                                             |
|         | 11 C2K8 D2K6 62 82                                                                       |
|         | 12 C3K5 D3K4 62 82                                                                       |
|         | 13 C4K2 D4K0 62 82                                                                       |
|         | 14 C5K6 D5K4 62 82                                                                       |
|         | 15 C7K0 D6K7 62 82                                                                       |

(1) Catalog number positions 7…10.

Table 38 - Capacitor Resonance Fault Thresholds—600/690V Products

| 600V ND Rating Codes  (1)    |
|------------------------------|
| 5 E011…E062 F015…F061 5 6    |
| 6 E077…E144 F082…F142 10 13  |
| 7 E192…E395 F171…F370 23 31  |
| 8 E242…E545 F215…F505 23 31  |
| E595…E760 F565…F735 31 41    |
| E825, E980 F820, F920 46 62  |
| 10 E1K1…E1K5 F1K0…F1K4 46 62 |
| 11 E2K0 F1K8 46 62           |
| 12 E2K4 F2K3 46 62           |
| 13 E2K9 F2K7 46 62           |
| 14 E3K9 F3K6 46 62           |
| 15 E4K9 F4K5 46 62           |

(1) Catalog number positions 7…10.

Frames 10…15 have multiple LCL filter modules. The first filter module can be used as a guide to de-tune all filter modules in the product. However, it is recommended that you check the other modules to make sure that their currents are below their respective threshold. Table 39 shows the parameter numbers and thresholds for the additional modules that are based on frame size. Table cells with a dash indicate that the frame does not have that LCL module installed.

Table 39 - Resonance Current Thresholds

| LCL Module Parameters                                              |                   |
|--------------------------------------------------------------------|-------------------|
| LCL Module Parameters                                              | 10 11 12 13 14 15 |
| F0 14:1216…14:1218 82 (62) 82 (62) 82 (62) 82 (62) 82 (62) 82 (62) |                   |
| F1 14:1316…14:1318 — — — — — —                                     |                   |
| F2 14:1416…14:1418 41 (31) 82 (62) 82 (62) 41 (31) 82 (62) 82 (62) |                   |
| F3 14:1516…14:1518 — — — 82 (62) — —                               |                   |
| F4 14:1616…14:1618 — — 41 (31) — 82 (62) 41 (31)                   |                   |
| F5 14:1716…14:1718 — — — 41 (31) — 82 (62)                         |                   |
| F6 14:1816…14:1818 — — — — 82 (62) —                               |                   |
| F7 14:1916…14:1918 — — — — — 82 (62)                               |                   |
| F8 14:2016…14:2018 — — — — — —                                     |                   |
| F9 14:2116…14:2118 — — — — — 41 (31)                               |                   |

Voltage Regulator Gains—Manual Adjustment

PowerFlex 755T products allow individual manual adjustment of the proportional and integral terms that are used by the voltage regulator. To enable manual adjustment of the proportional and integral terms, set 13:54 [Volt Reg C/U Sel] to 1 'User Entered'. This setting switches the gains that are used by the voltage regulator from the calculated values to values that are entered in parameters 13:57 [u Volt Reg Kp] and 13:59 [u Volt Reg Ki].

It is recommended to begin manual adjustment with the suggested gain start points. To initiate the transfer of these values, toggle 13:54 [Volt Reg C/U Sel] to 2 'LoadCalcData'. When this option is selected, the calculated gains values are copied to the user entered gain parameters. When the transfer is complete, 13:54 [Volt Reg C/U Sel] will automatically set to 1 'User Entered' for manual adjustment.

Proper adjustment of the individual proportional and integral terms is more difficult than adjusting the bandwidth because the ideal spacing between the proportional and integral terms is not maintained. The theoretical ideal spacing between the proportional and integral terms is where Z = 1 is the desired damping factor. This creates a 4:1 spacing.

Figure 62 - Voltage Regulator and Gains Block Diagram

<!-- image -->

| Parameter No. Parameter Name Definition                                           |
|-----------------------------------------------------------------------------------|
| 13:54 Volt Reg C/U Sel 0 = Calculated, 1 = User Entered, 2 = Load Calculated Data |
| 13:55 Volt Reg BW Voltage regulator bandwidth in Hz                               |
| 13:56 Volt Reg Damping Voltage regulator damping factor                           |
| 13:57 u Volt Reg Kp User entered voltage regulator proportional gain              |
| 13:58 c Volt Reg Kp Calculated voltage regulator proportional gain                |
| 13:59 u Volt Reg Ki User entered voltage regulator integral gain                  |
| 13:60 c Volt Reg Ki Calculated voltage regulator integral gain                    |

## Current Regulator Gains—Manual Adjustment

PowerFlex 755T products allow individual manual adjustment of the proportional and integral terms that are used by the current regulator. To enable manual adjustment of the proportional and integral terms, set 13:74 [Cur Reg C/U Sel] to 1 'User Entered'. This setting switches the gains that are used by the current regulator from the calculated values to values that are entered in parameters 13:77 [u Cur Reg Kp] and 13:79 [u Cur Reg Ki].

It is recommended to begin manual adjustment with the suggested gain start points. To initiate the transfer of these values, toggle 13:74 [Cur Reg C/U Sel] to 2 'LoadCalcData'. When this option is selected, the calculated gains values are copied to the user entered gain parameters. When the transfer is complete, 13:54 [Volt Reg C/U Sel] will automatically set to 1 'User Entered' for manual adjustment.

Proper adjustment of the individual proportional and integral terms is more difficult than adjusting the bandwidth because the ideal spacing between the proportional and integral terms is not maintained. The theoretical ideal spacing between the proportional and integral terms is where Z = 1 is the desired damping factor. This creates a 4:1 spacing.

<!-- image -->

Figure 63 - Current Control (CurrCtrl) Regulator and Gains Block Diagram

| Parameter No. Parameter Name Definition                                          |
|----------------------------------------------------------------------------------|
| 13:74 Cur Reg C/U Sel 0 = Calculated, 1 = User Entered, 2 = Load Calculated Data |
| 13:75 Cur Reg BW Current regulator bandwidth in Hz                               |
| 13:76 Cur Reg Damping Current regulator damping factor                           |
| 13:77 u Cur Reg Kp User entered current regulator proportional gain              |
| 13:78 c Cur Reg Kp Calculated current regulator proportional gain                |
| 13:79 u Cur Reg Ki User entered current regulator integral gain                  |
| 13:80 c Cur Reg Ki Calculated current regulator integral gain                    |

## AC Line Source Switching

PowerFlex 755T regenerative AFE products can switch between two different AC line sources. Set parameter 13:31 [AC Line Source] to point to the active AC line (AC Line A or AC Line B). With firmware revision 3 and earlier, set parameter 13:31 [AC Line Source] using the HIM, Connected Components Workbench software, or datalinks.

With firmware revision 4 and later, you can use a digital input to switch between AC line sources. Set parameter 0:136 [DI AC LineSource] to the digital input that you want to use to switch sources. When the digital input is off, the converter uses AC Line A and when it is on, it uses AC Line B.

## IMPORTANT

Do not switch AC line sources while the converter is modulating.

When switching between two AC line sources, it is important that the converter is tuned to both sources. Individual AC line sources rarely have the same electrical characteristics. Gains that work well for one source can cause resonance when connected to the alternate source.

The converter does not have AC line source-specific gains. In most cases, the bandwidth for the high impedance line source is sufficient when connected to a robust source. The actual current regulator gains are scaled according to the difference in system impedance. If higher performance is desired when connected to the robust source, you can use datalinks to change the voltage regulator bandwidth in parameter 13:55 [Volt Reg BW], and the current regulator bandwidth in parameter 13:75 [Cur Reg BW], based on which source the converter is using.

## Power Loss Source Switching

When the drive is configured for generator switchover, consider how the drive reacts to a power loss event. Use the power loss ride-through feature to pause converter modulation and allow for switching from AC Line A to AC Line B and vice versa. Use the application requirements and system dynamics to configure the power loss action and power loss mode for the inverter. For example, large inertia loads could be decelerated to keep the drive powered for the time required for the generator to come online and start producing power. If there is not sufficient inertia to keep the drive alive during the switchover, you could use a separately sourced 24V DC supply to keep the drive powered during this time. For information about configuring the drive for a power loss, refer to the PowerFlex Drives with TotalFORCE Control programming manual, publication 750-PM100 .

## Backup Generator Configuration

This section covers information about how to size and select an appropriate generator for use with a PowerFlex 755T drive along with drive configuration guidance. Step-by-step instructions are provided in Configuration for Backup Generator on page 132 .

## Generator Design Considerations

There are specific considerations when selecting a generator for use with an AC drive. The first is impedance. Typically, generators have an impedance in the range of 10% to 20% compared to 3% to 5% for a transformer that is connected to the utility AC Supply. This higher impedance leads to larger voltage drops when the generator is heavily loaded.

The second consideration is power factor. The industry standard for generator manufacturers is to specify KW at a power factor of 0.8 lagging. It is important to know the details of how the generator is rated because the PowerFlex 755T family appears as a 0.95…0.98 power factor to the generator. When sizing the generator, the real and apparent power must be considered. If the load power factor is higher (closer to unity) than the rated power factor, the horsepower of the prime mover limits the output. If the power factor is lower than the rated power factor, the output is limited by the current rating of the generator.

Additionally, one must also consider that most synchronous generator manufacturers do not make allowances for non-linear loads. Drives are considered non-linear loads because their input current is not sinusoidal. Because the voltage is being rectified, most of the current draw occurs when the voltage waveform is near its peak value. Even though the RMS current can be well below the generator's capacity, the peak current could approach its full load rating. The combination of the high impedance and higher peak currents of the non-linear load is important because it causes distorted generator output voltages. You can reduce the peak value for the distorted wave form by 30% or more in comparison to the no load voltage. The reduction in peak voltage lowers DC Bus voltage levels in the drive, which could cause the drive to cycle in and out of precharge. This distortion can also lead to frequency tracking issues on active front end converters.

## Generator Selection

When sizing the generator, the alternator portion of the typical generator rating is 150% of the load KVA requirements. Considerations that require the generator rating to be higher than the drive include reducing the observed voltage drop at the drive terminals. Because the impedance is a measure of the percentage voltage drop at full load versus no load voltage, an oversized alternator reduces the percentage current draw which results in better voltage and frequency regulation at the drive terminals.

Another factor is the need to compensate for the drive as a non-linear load. Most generator manufacturers do not make allowances for non-linear loads. Regardless generators have been proven to work with drives provided the non-linear portion of their output is only a small percentage of generator rating. Ideally, the drives and other non-linear loads would not exceed 20% of the generator's total capacity.

If you use six pulse drives, a phase shifting technique can increase the percentage of nonlinear loading of the generator. The phase shifting technique is commonly accomplished by using an isolation transformer with one primary winding (Delta) and two secondary windings (Delta/Y). When the drives are split between the two secondary windings, the peak current that 
° py gp
the generator sees is reduced due to the 30° phase shift in voltage between the two windings.

The use a harmonic trap filter is an accepted method to reduce the effects of non-linear loads. The filter draws current from the generator at 60 Hz. This stored energy is used to supply the non-linear current to the drives as needed.

When choosing a generator, a higher output voltage rating is advantageous. A higher voltage helps reduce voltage distortion. A higher voltage requires less current for a given load. Any reduction in current reduces the impact of the generators higher impedance, which improves voltage characteristics.

## Useful Drive Features for Generator Applications

When using a generator as a power source, the voltage distortion can make it difficult for drives with a SCR bridge to synchronize with the generator frequency. For this reason, it is important to select a drive that has a Phase Locked Loop (PLL) as part of the tracking circuit to allow the drive to respond quickly to line frequency changes. PowerFlex 755T products use a tunable PI controller so that the frequency and angle of the incoming voltage are quickly and accurately tracked even in applications with large frequency oscillations. While the default settings work well in most cases, the response can be modified by adjusting 13:86 [Basic PLL Kp] and 13:87 [Basic PLL Ki]) to accommodate heavily distorted voltage signals if necessary.

The PowerFlex 755T PLL has a feature that helps with generator installations called 'Unbalance Rejection'. This feature is a filter that allows the drive to reject the effects of unbalanced input line voltages. When enabled, it enhances the performance of the PLL such that no detuning is required even in installations where the input voltage is highly unbalanced. To enable Unbalance Rejection set bit 1 of parameter 13:85 [PLL Config] high (1). To fine-tune the filter, modify parameter 13:89 [Unbl Rej Filt BW]. The default Bandwidth (BW) is 200 rad/s. Increase the Bandwidth (BW) to increase the dynamic response for faster attenuation of the unbalance effect. However, this adjustment introduces an overshoot. Decrease the BW to reduce the dynamic response and decrease the overshoot.

Another PLL feature useful in generator applications is DC Offset Cancellation. As the name implies, it is designed to eliminate the measured DC offset of the input voltage. To enable DC Offset Cancellation set 13:85 [PLL Config] bit 2 'PLL DC Ofst' to 1. To fine-tune, modify the filter BW in parameter 13:90 [DC Offst Filt BW]. Increase the BW to decrease the response (overdamped) and decrease the BW to provide a faster (underdamped) response. There is also a Low Pass Filter that can be adjusted using parameter 13:91 [DC Offset LPF BW].

Typically, generators do not support products that regenerate back to the AC supply. The PowerFlex 755T regenerative products can limit regeneration. Set parameter 13:104 [Regen Power Lmt] to the percentage of regenerative energy you want to return to the AC Line. Normally, the limit is set to 5% or less when power is being supplied from a generator. Alternatively, select a non-regenerative bus supply.

The PowerFlex 755T family lets you specify and switch between two different AC line supplies. This capability is useful for backup generator applications because it automatically adjusts the current regulator gains to accommodate the difference in input impedance. There are two methods for switching the line settings. The first is to change the value in parameter 13:31 [AC Line Source] from the HIM, drive software, or a datalink. The second method is to assign a physical input to parameter 0:136 [DI AC LineSource] and use a digital input to select the source. The digital input method is only available with firmware revision 4 and later.

Due to the high line impedance of typical generator supplies, de-tune Active Front End converters to avoid the high resonance conditions that are caused by an interaction between the harmonic filters and the converter control loops. The PowerFlex 755T family of products has a feature that is called Active Damping that mathematically creates a virtual resistor in series with the filter capacitor, which effectively reduces the resonance without de-tuning. To use this feature, adjust the Active Damping Gain in parameter 13:81 [Actv Damping Gn]. Lower the gain from the default value of 1.0 to reduce resonance between the filter and the supply due to the high impedance. By itself, it does not provide much help with resonances due to line notching caused by other devices that are connected to the line.

## Configuration for Backup Generator

This section covers the steps that are required to configure the PowerFlex 755T drive for use with a backup generator. It is a guide to configuration only and excludes recommendations for sizing or design.

Basic Configuration

Enter basic information about the AC Supply and the generator to configure the PowerFlex 755T for use with a backup generator. This information is needed so that the drive can calculate the system impedance and adjust the current regulator gains accordingly.

1. Enter the nominal AC line frequency in 13:30 [Nom Line Freq].
2. Enter the apparent power rating of the mains AC Supply transformer in 13:32 [AC Line kVA A].
3. Enter the apparent power rating of the generator in 13:33 [AC Line kVA B].
4. Enter the percent impedance of the mains AC Supply transformer in 13:34 [AC Line Imped% A].
5. Enter the percent impedance of the generator in 13:35 [AC Line Imped% B].

Configure the drive to switch between Source A and Source B

There are two methods that can be used to switch between the two AC sources that do not require using Connected Components Workbench software or the drive HIM to change the value in 13:31 [AC Line Source]. The method that you chose depends on your system.

## IMPORTANT

Don't change the AC line source when the converter is modulating.

The first method is to configure 13:31 [AC Line Source] as one of the datalinks and use a programmable controller to change the value to 0 for Source A (AC Line) or 1 for Source B (Generator). Datalinks are setup using parameters 0:321 [DL From Net 01] through 0:336 [DL From Net 16]. You can use this method with all firmware revisions.

The second method is to configure a digital input to switch between the two sources. When the digital input is open or de-energized, the drive uses Source A (AC Line) data. When the digital input is closed or energized, the drive uses Source B (Generator). This method is only available for firmware revision 4 and later.

6. Select the first unused datalink and configure it for 'Port13: AC Line Source'. For example, if 0:321 [DL from Net 01] was the first datalink that was set to 'Disabled', change it to 'Port13: AC Line Source'.

Or

Configure 0:136 [DI AC LineSource] for the digital input you want to use to facilitate the switch between sources. For example, if you wanted to use digital input 0 on the I/O card installed in Port 4, change 0:136 [DI AC LineSource] from 'Disabled' to 'Port 4: Dig In Sts.Input 0'.

IMPORTANT

If parameter 0:136 [DI AC LineSource] is configured, the drive ignores the value in 13:31 [AC Line Source].

## External DC Bus Capacitance

In common bus installations and some applications, there is more capacitance that is connected to the bus than the inverter is pre-configured to operate with. If the application does not have additional bus capacitance, skip this step.

The PowerFlex 755T regenerative and low harmonic products have a couple of methods to address this additional capacitance. If the additional capacitance value is known, it can be directly inputted into the inverter configuration. If the actual value is not known, the Bus Observer feature can be enabled to compensate for the additional capacitance automatically.

For more information on the Bus Observer feature, refer to the Bus Observer section in the Adaptive Control chapter in this manual.

7. Enter the additional capacitance value in 13:52 [Ext Bus Cap]

And/or

Enable the Bus Observer Feature by setting 13:320 [BusObs Config] to 1 'BusObs Only'

## Tuning

For many applications, the default settings work well. In installations with higher system impedance, as in generator applications, the default settings can cause resonance current in the LCL filters. There are two approaches for reducing this resonance.

The first is to de-tune by adjusting the voltage and current bandwidths and the second is to use the Active Damping feature. Both methods require that you monitor the band pass filter current and adjust until the current is below the fault threshold values that are specified in the tables in the AC Line Tuning section of this manual. You can use a combination of de-tuning and Active Damping for optimum performance.

## IMPORTANT

Consider tuning both sources. Ideally, there is a combination that works for both the AC line and the generator. If not, the bandwidths and/or Active Damping values can be changed based on the currently selected AC source through datalinks.

## Generator

8. Configure the drive to run from the generator.
9. Start the drive. It is preferable that the drive is run in a high load condition.
10. Monitor the LCL resonance current in parameters 14:1216 [F0 Cap BPF Cur R], 14:1217 [F0 Cap BPF Cur S], and 14:1218 [F0 Cap BPF Cur T], and the bus voltage in parameter 14:109 [L0 DC BusVoltage].
11. Slowly adjust 13:55 [Volt Reg BW] and 13: 75 [Cur Reg BW] down by the same percentage until the resonance current is below the fault levels.

Or

Slowly reduce 13:81 [Actv Damping Gn] until the resonance current is below the fault levels.

12. Verify that the Bus Voltage is holding at the desired level without too much fluctuation. If not, repeat step 9 but use the other method or a combination of the two until the resonance current is below the fault level and bus voltage maintains a steady level.
13. Stop the drive.
14. Record the values in 13:55 [Volt Reg BW], 13: 75 [Cur Reg BW], and 13:81 [Actv Damping Gn].

## AC Line

15. Configure the drive to run from the AC Line.
16. Start the drive. It is preferable that the drive is run in a high load condition.
17. Monitor the LCL resonance current in parameters 14:1216 [F0 Cap BPF Cur R], 14:1217 [F0 Cap BPF Cur S], and 14:1218 [F0 Cap BPF Cur T], and the bus voltage in parameter 14:109 [L0 DC BusVoltage].
18. If the bus voltage is at the desired level without too much fluctuation and the LCL filter resonance current is below the fault levels, tuning is complete, and you can skip ahead to the Exception Actions section. If not, continue with the remaining steps to tune for the AC Line and then programmatically change the bandwidths and Active Damping Gain based on which source is selected.
19. Slowly adjust 13:55 [Volt Reg BW] and 13: 75 [Cur Reg BW] up by the same percentage until the bus voltage is at the desired level without too much fluctuation.

20. Slowly reduce 13:81 [Actv Damping Gn] until the resonance current is below the fault levels.
21. Record the values in 13:55 [Volt Reg BW], 13: 75 [Cur Reg BW], and 13:81 [Actv Damping Gn].
22. Select the first three unused datalinks and configure them for 'Port13: Cur Reg BW', 'Port13: Volt Reg BW', and 'Port13: Actv Damping Gn'. For example, if 0:321 [DL from Net 01] was the first datalink that was set to 'Disabled', change 0:321 [DL from Net 01] to 'Port13: Cur Reg BW', 0:322 [DL from Net 02] to "Port13: Volt Reg BW" and 0:323 [DL from Net 03] to 'Port13: Actv Damping Gn'.
23. Write logic to switch between the values that are recorded for the Generator and the AC Line based on which source is selected.

## IMPORTANT

This procedure assumes the use of a Logix Programmable Automation Controller and Premier Integration. Switching between gain values could also be accomplished with DeviceLogix™ functionality.

## Exception Actions

One of the things to consider when using a backup generator is how the drive responds to a power loss. While the default settings for power loss work in many applications, you can customize them for your application.

## Converter

24. Review parameter 13:170 [PwrLoss Det Actn] to make sure it is set correctly for your application and modify as required.
25. Review parameter 13:172 [RideThrough Time] to make sure it is set correctly for your application and modify as required.

## Inverter

26. Review parameter 10/11:270 [Power Loss Actn] to make sure it is set correctly for your application and modify as required.
27. Review parameter 10/11:273 [Pwr Loss A Time] to make sure it is set correctly for your application and modify as required.

## IMPORTANT

See the PowerFlex Drives with TotalFORCE Control programming manual, publication 750-PM101, for more information on the exception action parameters.

## Regeneration Power Limits

Typically, in generator applications you would select a PowerFlex 755TL Low Harmonic drive because it does not transmit regenerative energy back to the line. If too much regenerative energy is supplied back to a generator source, it could act as a motor and damage the prime mover. Regenerative loads can be supplied by generators provided the amount of regenerative energy that is returned to the source is limited. Many generator manufacturers specify that they can handle applications with 5%…10% regenerative loads.

The PowerFlex 755TR and 755TM products can limit the amount of regenerative energy that gets transmitted back to the supply. This capability makes them an option when it is desirable to regenerate back to the line when connected to AC Line but limit regeneration when being supplied by a generator. The recommendation is to set the Regenerative Power Limit to 5% when being supplied by a generator. Through datalinks or DeviceLogix functionality, the limits can be adjusted programmatically to allow full regeneration when connected to the AC Line but still limit to 5% when connected to the generator.

If you are using a PowerFlex 755TL, you can skip this section. If you are using a PowerFlex 755TR or 755TM, follow the remaining steps to configure the Regenerative Power Limit.

## Static Limit

28. Set parameter 13:104 [Regen Power Lmt] to 5%.

## Dynamic Limit

29. Select the first unused datalink and configure it for 'Port13: Regen Power Lmt'. For example, if 0:321 [DL from Net 01] was the first datalink that was set to "Disabled", change 0:321 [DL from Net 01] to 'Port13: Regen Power Lmt'.
30. Write logic to switch between 5% for the Generator and the desired regeneration level for the AC Line based on which source is selected.

## IMPORTANT

This procedure assumes the use of a Logix Programmable Automation Controller and Premier Integration. Switching between Regenerative Power Limit values could also be accomplished with DeviceLogix functionality.

## Notes:

## High Speed Trending

## Diagnostics and Troubleshooting

This chapter discusses the tools that are available to evaluate and correct performance issues with PowerFlex® products.

| Topic Page                     |
|--------------------------------|
| High Speed Trending 137        |
| Faults and Alarms 143          |
| Input Phase Loss Detection 147 |

The high speed trending wizard configures the onboard trending feature providing high sample rate data capture. The wizard allows you to download the trend configuration to the drive, and uploads the trended data from the drive when finished. This information is saved as a comma-delimited *.csv file for use with Microsoft® Excel® or any other spreadsheet program.

The high speed trending can be configured to trend either four, eight, or sixteen parameters. The number of parameters that are trended effects the sample size and sample rate. See Table 40 to determine the high speed trending tool capabilities are based on the number of parameters being trended.

Table 40 - PowerFlex 755T High Speed Trend Configuration Options

| Number of Parameters   | Number of Samples Minimum Sample Rate   |
|------------------------|-----------------------------------------|
|                        | 4 1024 125 µs                           |
|                        | 8 4096 1 ms                             |
|                        | 16 1024 1 ms                            |

The PowerFlex 755T drive can only run one instance of the onboard high speed trending tool. Once the wizard has downloaded the high speed trend configuration to the drive, you do not have to stay connected to the drive with the software tool. The drive automatically captures data based on the triggered event in the wizard configuration. You reconnect to the drive to upload the trended data.

The configurable sample rate of the onboard high speed trending tool makes it an alternative option to other trending tools available in Logix or Connected Components Workbench™ software. The RPI (requested packet interval) of the device defines the software tool sample rates. The PowerFlex 755T has a minimum RPI of 2 ms. The onboard high speed trend tool in the PowerFlex 755T is a useful resource to:

- Determine application specific tuning characteristics
- Troubleshoot nuisance trip conditions
- Capture data before and after a triggered event
- Capture data when a user is not actively connected to the drive

## Configuration Example

1. Connect to the PowerFlex 755T with the Connected Components Workbench software tool.
2. Navigate to the Wizards on the left panel.

<!-- image -->

3. Select the High Speed Trend Wizard from the options.
4. Once the Welcome screen loads, click Next.

<!-- image -->

<!-- image -->

The Configuration Trend window lets you customize the following high-speed trend details:

- Trend Mode – dictates number of trend butters, total number of samples, and the minimum interval sample rate
- Pre-Trigger samples – dictates number of samples to include in the trend before the trigger
- Sample Interval – the time interval between trend data samples
- Trigger Setup – dictates how the data trend is triggered
- Compares two parameters
- Compares a parameter against a constant
- A test bit in a parameter
- Trend Buffers – dictates the drive and/or peripheral parameters and diagnostic items that are trended

<!-- image -->

5. To configure the Trigger Setup and Trend Buffers, click the Ellipse.

<!-- image -->

<!-- image -->

If you do not see the ellipse for the Trend Buffers, click in the first row of 'Not Used', and the ellipse populates the row.

6. Select the parameter that you want to log by selecting the port, and then scroll through the parameter lists, file folders, diagnostic items, or use the find function. Once a parameter is selected, click Apply.

<!-- image -->

The best way to remove a parameter selection is to uncheck the checkbox in the 'Use' column.

<!-- image -->

'Not Used' is downloaded instead of the selected parameter. The next time that you launch the wizard, the buffer has no parameter set.

In the following example, the trend buffers are configured with five drive parameters consisting of Output Frequency, Pri Vel Feedback, DC Bus Volts, Output Current, and Output Voltage parameter values. The trend is configured for a total of 4096 samples that include 500 samples before the trigger, at a sample rate of 1 millisecond. The trigger of the high speed trend is the Motor Velocity Feedback greater than zero.

<!-- image -->

This configuration for the trend does the following:

- The drive sets the trigger to monitor the primary velocity feedback.
- When you start the drive, the primary velocity feedback &gt; zero.
- The Trend is triggered to pull the first 500 samples before the trigger and continue collecting 3596 more samples for the five parameters selected.
- Once 4096 samples have been collected, the trend stops. The drive continues operating.
- The trend is ready to be uploaded from the drive.
7. Click Download to push the trend configuration to the PowerFlex 755T drive. Once the Download Succeeded message appears, the 'Trend Status' changes to 'Ready'.

<!-- image -->

8. Click Start to start the trend tool. The 'Trend Status' changes to 'Running.' Upload and Start are unavailable when the trend is running.

<!-- image -->

Depending on the trigger configuration, the trend tool may not start storing data until the trigger is tripped.

<!-- image -->

The 'Trend Status' changes to 'Finishing' after the buffers for all parameters have filled, and the trend is processing the data. Press Stop at any point to start the trend before the buffers are filled.

<!-- image -->

The 'Trend Status' changes to 'Complete' when the trend is done.

<!-- image -->

9. Click Upload. The wizard uploads the trend data from the drive and saves the information as a comma-delimited *.csv file for use with Microsoft® Excel® or any other spreadsheet program.

<!-- image -->

## Faults and Alarms

The following is an example of trended data. Use a spreadsheet program to open the *.csv file.

<!-- image -->

Column C here aligns with what is displayed in Connected Components Workbench software or any other drive software tool. Column D shows the value that the drive is using internally. Column D has more accurate data, but the extra precision is often not needed. You cannot get the data in column D from any other wizard or software tool.

For more information on the High Speed Trend Wizard, reference the block diagram that is published in the PowerFlex Drives with TotalFORCE Control programming manual, publication 750-PM100 .

This chapter provides information about the faults and alarms that are accessible through software or the HIM, and status indicators that are used to report the current operating condition of the PowerFlex product.

## Faults

Faults are events or conditions occurring within and/or outside of the drive. These events or conditions by default are considered to be of such significant magnitude that drive operation is discontinued. The STS (Status) indicator on the drive, a HIM, communications network, and/ or contact outputs annunciate faults.

With frames 7…15 drives and bus supplies, the power and precharge modules use status indicators and a 7-segment display to report conditions. The fiber-optic interface and transceiver circuit boards also use a status indicator to report conditions.

See the Troubleshooting section of the PowerFlex Drives with TotalFORCE Control programming manual, publication 750-PM101 .

Detailed information on faults is provided in the PowerFlex Drives with TotalFORCE Control Conditions Reference Data, publication 750-RD102 .

## Drive Response to Faults

When a fault occurs, the fault condition is latched, which requires that you or the application perform a fault reset to clear the latched condition. The condition that caused the fault determines the user response. If the condition that caused the fault still exists after a fault reset, the drive faults again and the fault condition is latched.

In response to a fault, the drive takes a predetermined action that is based on fault type. The drive response to some fault types is configurable. Non-configurable faults turn off the drive output and a 'coast-to-stop' sequence occurs.

The fault code is entered into the first buffer of the fault queue (see the Fault Queue section for rules). Additional data on the status of the drive at the time that the fault occurred is recorded. This information is always related to the most recent fault queue entry captured by 0:610[Last Fault Code]. When another fault occurs, this data is overwritten.

The following data/conditions are captured and latched into non-volatile drive memory.

- Port 10/11:461[Fault Status A]
- Port 10/11:462 [Fault Status B]
- Port 13:240 [Fault Status A]
- Port 13:241 [Fault Status B]

## Fault Queue

Faults are also logged into a fault queue, such that a history of the most recent fault events is retained. Each recorded event includes a fault code (with associated text) and a fault 'time of occurrence.' PowerFlex 755T drives have a 100-event queue.

The fault queue records the occurrence of each fault event that occurs while no other fault is latched. Each fault queue entry includes a fault code and a time stamp value. New fault events are not logged to the fault queue if a previous fault has already occurred but has not yet been reset. Only faults that actually trip the drive are logged. Faults that occur while the drive is faulted are not logged.

The fault queue is a first-in, first-out (FIFO) queue. Fault queue entry 1 is always the mostrecent entry (newest). Entry 100 is always the oldest. As a new fault is logged, each existing entry shifts by one. The previous entry 1 moves to entry 2, previous entry 2 moves to entry 3, and so on. If the queue is full when a fault occurs, the oldest entry is discarded.

The fault queue is saved in nonvolatile storage at power loss and its content is retained when power is cycled.

## Fault Code and Time Stamp

The fault code with descriptive text for each entry can be viewed with a HIM or by software tools like Connected Components Workbench software (CCW) or Logix Designer application.

Event numbers are displayed in one of three formats.

- Port 00 (Host Drive) displays the event number only. For example, Fault 21 'Clr Fault Queue' is displayed as: Fault Code 21.
- Ports 01...09 use the format PEEE, which indicates port number (P) and event number (EEE). For example, Fault 1 'Analog In Loss' on an I/O module that is installed in port 4 is displayed as: Fault Code 4001.
- Ports 10...14 use the format PPEEE, which indicates port number (PP) and event number (EEE). For example, Fault 1 'Power Loss' on port 10 is displayed as: Fault Code 10001.

Once the fault code is displayed, pressing the enter key again on the HIM displays the time stamp that is associated with that fault code. The time stamp is the elapsed time since the fault occurred. When using one of the available software tools, the fault code, descriptive text, and time stamp are displayed simultaneously.

## Reset or Clear a Fault

Clear a latched fault condition by the following methods.

- An off to on transition on a digital input that is configured as DI Clear Fault.
- Press the CLR soft key or Stop on the HIM once a fault is displayed.

- From CCW or Logix Designer application tools, in the Fault/Alarms section by clicking Clear Trip.
- Cycle power to the drive such that the control board goes through a power-up sequence.

A fault reset clears the faulted status indication. If any fault condition still exists, the fault is relatched and another entry is made in the fault queue.

## Clearing the Fault Queue

A fault reset does not clear the fault queue. Clear the fault queue from a menu selection on the HIM or click Clear Queue in the Fault/Alarms section of CCW or Logix Designer application tools.

<!-- image -->

## Event Actions

The drive can be configured such that some events or conditions do not trip the drive.

The following is a list of the options that are available for the drive configurable event actions.

- 'Ignore' – No action is taken.
- 'Alarm' – Type 1 alarm indicated.
- 'Flt Minor' – Minor fault indicated. If running, drive continues to run.
- 'FltCoastStop' – Major fault indicated. Coast-to-stop.
- 'Flt RampStop' – Major fault indicated. Ramp to Stop.
- 'Flt CL Stop' – Major fault indicated. Current Limit Stop.

The following is a brief list of configurable event actions that are listed by port. Accessories such as encoder or I/O modules have additional configurable event actions.

| Port 0 PowerFlex 755T  Port 10 Primary and Port 11 Secondary Motor Side Control  Port 13 Line Side Control   |
|--------------------------------------------------------------------------------------------------------------|
| 0:420 [M Gnd Warn Actn] 10/11:170 [Dec Inhibit Actn] 13:112 [Under Vlt LmtA Actn]                            |
| 0:422 [L Gnd Warn Actn] 10/11:200 [Motor OL Action] 13:115 [Low Vlt LmtA Actn]                               |
| 0:425 [HRG GF Flt Actn] 10/11:242 [Shear Pin 1 Actn] 13:118 [High Vlt LmtA Actn]                             |
| 0:453 [CapOvr Rsn Actn] 10/11:245 [Shear Pin 2 Actn] 13:121 [Over Vlt LmtA Actn]                             |
| 0:515 [PodFan Event Actn] 10/11:250 [Load Loss Action] 13:126 [Under Vlt LmtB Actn]                          |
| 0:518 [StirFan Event Actn] 10/11:256 [OutPhaseLoss Actn] 13:129 [Low Vlt LmtB Actn]                          |
| 0:525 [In Fan Event Actn] 10/11:270 [Power Loss Actn] 13:132 [High Vlt LmtB Actn]                            |
| 0:535 [PwrRFan Event Actn] 10/11:285 [UnderVltg Action] 13:135 [Over Vlt LmtB Actn]                          |
| 0:545 [WrgFan Event Actn] 10/11:289 [InPhase LossActn] 13:142 [Undr Freq LmtA Actn]                          |
| 0:555 [CtrlFan Event Actn] 10/11:314 [MtrBrng EventActn] 13:145 [Low Freq LmtA Actn]                         |
| 0:563 [HSFan Event Actn] 10/11:319 [MtrLube EventActn] 13:148 [High Freq LmtA Actn]                          |
| 0:567 [IGBT Event Actn] 10/11:325 [MchBrng EventActn] 13:151 [Over Freq LmtA Actn]                           |
| 0:571 [BusCap Event Actn] 10/11:330 [MchLube EventActn] 13:156 [Undr Freq LmtB Actn]                         |
| 0:575 [MCS Event Actn] 13:159 [Low Freq LmtB Actn]                                                           |
| 0:579 [MCB Life Event Actn] 13:162 [High Freq LmtB Actn]                                                     |
| 0:583 [PCC Life Event Actn] 13:165 [Over Freq LmtB Actn]                                                     |
| 0:587 [LCLCap Even tActn] 13:170 [PwrLoss Det Actn]                                                          |
| 0:590 [Hi TR Event Actn] 13:173 [VltgSag Det Actn]                                                           |
| 0:591 [Lo TR Event Actn] 13:174 [VltgSag RT Exp Actn]                                                        |
| 13:171 [PwrLoss RT Exp Actn]                                                                                 |
| 13:176 [LSCPhLoss Det Actn]                                                                                  |
| 13:177 [PhLoss RT Exp Actn]                                                                                  |
| 13:179 [DFDT Det Actn]                                                                                       |
| 13:180 [DFDT RdThr Exp Actn]                                                                                 |
| 13:181 [PLL LOS Det Actn]                                                                                    |

## Alarms

Alarms are indications of situations that are occurring within the drive or application that are annunciated to the user. These situations can affect the drive operation or application performance. Conditions such as power loss or analog input signal loss can be detected and displayed for drive or operator action.

There are two types of alarms.

- Type 1 Alarms are conditions that do not cause the drive to trip or shut down, but, if the condition persists, it can lead to a drive fault.
- Type 2 Alarms are conditions that are caused by improper programming and prevent the drive from starting until programming is corrected. An example of a Type 2 alarm is when a start function is assigned to a digital input without a stop function that is also assigned to a digital input.

Detailed information on alarms is provided in the PowerFlex Drives with TotalFORCE Control Conditions Reference Data, publication 750-RD102 .

The alarm queue is accessible through a HIM or through CCW and Logix Designer application tools, provide you with a history of faults, alarms, and events. You can also access diagnostic file parameters for additional information.

## Input Phase Loss Detection

Occasionally, three-phase power sources can fail on one phase while continuing to deliver power between the remaining two phases (single-phase). Operating above 50% output under this single-phase condition can damage the drive. The 755T product has two separate methods dependent on hardware configuration to detect this condition.

- For drives without active front end technology, the input phase loss detection is implemented by hardware that measures DC bus voltage harmonics. This protection is implemented in port 10.
- For drives with active front end technology, input phase loss detection is implemented by hardware that measures the input line voltage and current. This protection is implemented in port 13.

The drive can be programmed to turn on an alarm bit or issue a drive fault (minor or major). Active front end drives can also be programmed to ride through.

- For Powerflex 755T and 755TS, we recommend that input phase loss detection is enabled in port 10 if this condition is likely to occur.
- For Powerflex 755Tand 755TS products with DC input we recommend that input phase loss detection is enabled in port 10 if the bus supply is a simple rectifier with limited diagnostics.
- For Powerflex 755T with active front end technology, we recommend implementing input phase loss detection in port 13 if the condition is likely to occur. Ride through can be enabled if the condition is short duration.

## Configure Input Phase Loss Action

## Parameter 10/11:289 [InPhase LossActn]

The following bits configure the port 10 input phase loss action.

- 'Ignore' (0) – No action is taken.
- 'Alarm' (1) – Type 1 alarm indicated. Type 1 alarms are notifications. They do not prevent starting. They do not stop modulation.
- 'Flt Minor' (2) – Minor fault indicated. Minor faults prevent the drive from starting. They do not stop the drive, if it is already running. You must clear the fault to start or run.
- 'FltCoastStop' (3) – Major fault indicated. The motor side inverter executes a Coast Stop. You must clear the fault to start or run.
- 'Flt RampStop' (4) – Major fault indicated. The motor side inverter executes a Ramp Stop. You must clear the fault to start or run.
- 'Flt CL Stop' (5) – Major fault indicated. The motor side inverter executes a Current Limit Stop. You must clear the fault to start or run.

A port 10 input phase loss is indicated in parameter 10/11:460 [Condition Sts A] bit 4 'InPhaseLoss'.

<!-- image -->

If a fault action has been selected because of port 10 input phase loss, 10/11:461 [Fault Status A] bit 4 'InPhaseLoss' is set.

<!-- image -->

If an alarm action is selected because of port 10 input phase loss, 0:465 [Alarm Status A] bit 4 'InPhaseLoss' is set.

<!-- image -->

## AFE Input Phase Loss

For drives with an active front end, input phase loss is configured in port 13. In this instance, 10/11:289 [InPhase LossActn] can be set to ignore. The following two parameters configure the input phase loss action.

## Parameter 13:176 [LSCPhLossDetActn]

Select the action taken when the port 13 input phase loss condition is detected.

- 'Ignore' (0) – No action is taken.
- 'Type 2 Alarm' (1) – A Type 2 Alarm occurs. Type 2 Alarms prevent the line side converter from starting its modulation.
- 'Ride Thru' (2) – The line side converter pauses modulation for the duration of the Ride Thru Timer. If the Input Phase Loss condition clears before the timer expires, it resumes operation. During the Ride Thru attempt, it logs a Type 2 Alarm.
- 'Major Fault' (3) – A Major Fault occurs immediately. Major Faults stop the line side converter from modulating.

## Parameter 13:177 [PhsLossRTExpActn]

When ride through is selected in 13:176 [LSCPhLossDetActn], this parameter selects the action to take when the input phase loss condition lasts longer than 13:172 [RideThrough Time].

- 'Ignore' (0) – No action is taken.
- 'Type 2 Alarm' (1) – A Type 2 Alarm occurs. Type 2 Alarms prevent the line side converter from starting its modulation.

- 'Ride Thru' (2) – The line side converter pauses modulation for the duration of the Ride Thru Timer. If the Input Phase Loss condition clears before the timer expires, it resumes operation. During the Ride Thru attempt, it logs a Type 2 Alarm.
- 'Major Fault' (3) – A Major Fault occurs immediately. Major Faults stop the line side converter from modulating.

If an alarm or fault action is selected by the firmware as a result for the input phase loss, 13:225 [Line Side Sts 1] bit 22 'InPhaseLoss' is set.

<!-- image -->

If a fault action is selected by the firmware as a result for the input phase loss, 13:240 [Fault Status A] bit 20 'InPhaseLoss' is set.

<!-- image -->

## 10/11:290 [InPhase Loss Lvl]

Sets the threshold for the Input Phase Loss detection function. Decreasing this value increases sensitivity, increasing the value decreases sensitivity. When all three input phases are connected, the sixth harmonic is dominant. When one phase is disconnected, the second harmonic is dominant If the ratio exceeds this threshold, the function detects an Input Phase Loss count. A certain number of events are required to enact the Input Phase Loss action.

This is just a different way of saying that if you know you are going to run single phase, derate the drive by 50%.

Test points are available to assist in adjusting the phase loss level.

- Test point 105 indicates the active ratio of second harmonics amplitude to sixth harmonics
- Test point 106 indicates the active input phase loss counts

## Notes:

## PowerFlex 755T Lifting/ Torque Proving

## Application References

This chapter discusses advanced PowerFlex® 755T product applications.

| Topic Page                                |
|-------------------------------------------|
| PowerFlex 755T Lifting/Torque Proving 151 |
| Anti-Sway Applications 166                |
| Dynamic Braking 174                       |
| Dynamic Bus Control 183                   |
| Carrier (PWM) Frequency 189               |
| Analog Inputs 191                         |
| Analog Outputs 198                        |
| Digital Inputs 203                        |
| Digital Outputs 213                       |
| PTC Motor Thermistor Input 220            |

TorqProve™ is a PowerFlex 755T drive feature that is intended for applications that require proper coordination between motor control and a mechanical brake. Before releasing a mechanical brake, the drive checks motor output phase continuity and verifies proper motor control (torque proving). The drive also verifies that the mechanical brake has control of the load before releasing drive control (brake proving). After the drive sets the brake, it monitors motor movement to confirm that the brake can hold the load.

<!-- image -->

ATTENTION: Loss of control in suspended-load applications can cause personal injury and/or equipment damage. The drive or a mechanical brake must always control the loads. Parameters 9:60 [Brk Release Time]…78 [DI FloatMicroPsn] are designed for lifting/torque prove applications. It's the responsibility of the engineer and/or end user to configure drive parameters, test any lifting functionality and meet safety requirements in accordance with all applicable codes and standards.

## Overview

TorqProve™ can be operated encoderless or with an encoder. See the PowerFlex Drives with TotalFORCE® Control Programming Manual, publication 750-PM100 for detailed information.

TorqProve functionality with an encoder includes:

- Torque Proving (includes flux up and last torque measurement)
- Brake Proving
- Brake Slip (feature slowly lowers load if brake slips/fails)
- Float Capability (ability to hold full torque at zero speed)
- Micro positioning
- Fast Stop
- Speed Deviation Fault, Output Phase Loss Fault, Encoder Loss Fault.

Encoderless TorqProve functionality includes:

- Torque Proving (includes flux up and last torque measurement)
- Micro positioning
- Fast Stop
- Speed Deviation Fault, Output Phase Loss Fault

<!-- image -->

## IMPORTANT

Brake Slip detection and Float capability (ability to hold load at zero speed) are not available in encoderless TorqProve.

## Torque Proving Flow Diagram

All times between Drive Actions are programmable and can be made very small (for example, Brake Release Time can be 0.1 seconds)

<!-- image -->

- (1) For torque proving to function properly, wire a mechanical brake to a relay output on a digital I/O option module. On the I/O module, set nn:10 [RO0 Sel] to 9:52 [Trq Prove Status] Bit 8 'Brake Release'.

## Brake Slip Test

If an encoder is being used, by default, the drive does a brake slip test on every stop. The brake slip test is outlined in the following steps.

1. A stop command is initiated
2. The drive ramps to zero speed. A snap shot (one time recording) of the command torque 10:2087 [Trq Ref Limited] is taken.
3. The drive runs at zero speed for the time that is defined in 9:72 [ZeroSpdFloatTime].
4. The drive engages the brake.
5. The drive continues to command the snap shot torque that is found in step 2 for the time that is allotted in 9:61 [Brk Set Time].
6. The PowerFlex 755T drive begins to slew (lower) the torque down. Parameters 10:2083 [Torque Limit Pos] and 9:53 [Trq Lmt SlewRate] define the rate at which the torque is lowered. The starting point of the ramp is the commanded torque that is found in step 2 plus 20% torque. The drive continues to command the torque that is defined in step 2 until the ramp goes below this torque.
7. During the torque slew defined in step 6, the drive is monitoring the encoder counts. If the drive detects a delta (change) in encoder counts greater than 9:63 [Brk Slip Thresh], the drive brings the torque back up to the torque level that is defined in step 2 .
8. The PowerFlex 755T drive repeats steps 6 and 7 until the drive no longer sees a change in encoder counts that is greater than the threshold in 9:63 [Brk Slip Thresh].
9. If no brake slip is found, the drive turns off and sits stopped and ready, and waits for the next run command. If a brake slip is found in step 7, once the drive lowers the load to the floor, the drive enunciates a 11012 'Brake Slipped Stop' alarm. The drive does not accept a run command again until it's reset or power is cycled to the drive.

To add additional brake control capabilities to the PowerFlex 755T drive when using an encoder, see Brake Proving Configuration on page 153 .

<!-- image -->

## Configuration

You must configure the PowerFlex 755T drive before you access any TorqProve parameters for configuration and commissioning. you can configure the drive through Connected Components Workbench™ software or via parameter settings in the HIM.

To configure the PowerFlex 755T drive via Connected Components Workbench software, follow these steps.

1. Connect to the PowerFlex 755T drive through Connected Components Workbench software
2. Once connected, click 'Device Definition' on the Overview page.
3. Click 'Dynamics Features'.
4. Under 'Application Sel' select Torque Prove. This adds Port 9 – Application Torque Prove to the PowerFlex 755T drive.
5. To accept the changes, click Ok.
6. Power cycle the drive.

To configure the PowerFlex 755T drive via the HIM, follow these steps.

1. Navigate to 0:70 [Application Sel].
2. Click the 'edit' soft key and change 0:70 [Application Sel] = 2 'Torque Prove'
3. To accept changes, click the 'enter' soft key.
4. Power cycle the drive.

## Bus Regulation

When you use a PowerFlex 755T drive in a lifting application, a PowerFlex 755TR drive is used to allow full line regeneration capabilities. You do not need to use a dynamic braking resistor in this configuration. The PowerFlex 755TL drive isn't recommended for lifting applications. Typical bus regulation parameter settings that are associated with regeneration are:

- 10:229 [Regen Power Lim] = -200%
- 10:116 [Bus Reg Mode A] = 0 'Disabled'

## Brake Proving Configuration

By default, the drive is testing for brake slip only during Brake Slip Test, step 7 (see Brake Slip Test on page 152). If the brake fails while the drive is stopped, the load can suddenly drop to the floor. To have the drive monitor for brake slip while the drive is stopped, set 9:50 [Trq Prove Cfg] bit 6 'BrkSlipStart'. With this bit set, if the drive detects a brake slip while the drive is stopped, the drive starts up and takes control of the load, goes into a brake slip test, and lowers the load to the floor. When the drive detects a brake slip in this manner (from a stopped state), the drive allows one start after the load reaches a safe position to move the load. After this point, the drive enunciates a Brake Slipped alarm and a power cycle is required to restart the drive.

If the drive is set up for encoderless torque proving, there's no brake slip test. After stopping, the drive engages the brake when the motor speed falls below the setting in 9:70 [Float Tolerance].

## Tuning the Motor for Torque Prove Applications

It's important that you enter all motor data correctly. When using PowerFlex 755T Autotune features, it's recommended to disconnect the motor from the hoist/crane equipment during the tests. It's recommended that Parameter 10 of the I/O card that is wired to the brake control is set to 10:354 [Motor Side Sts 1] bit 1 'Active', so that the brake releases when the motor starts to run.

<!-- image -->

ATTENTION: To guard against personal injury and/or equipment damage due to an unexpected brake release, verify that the digital output that is used for brake connections and/or programming. The PowerFlex 755T drive does not control the mechanical brake until TorqProve is enabled. If the brake is connected to a digital output, it could be released. If necessary, disconnect the digital output until wiring/programming can be completed and verified .

Torque Proving is only supported on induction motors. PowerFlex 755T motor control modes Induction Sensorless Vector (SV) and Induction Flux Vector (FV) are supported.

## Crane Setup—with Encoder Feedback

<!-- image -->

ATTENTION: Loss of control in suspended load applications can cause personal injury and/or equipment damage. The drive or a mechanical brake must always control the loads. Parameters 9:50…78 are designed for lifting/ torque prove applications. It's the responsibility of the engineer and/or end user to configure drive parameters, test any lifting functionality, and meet safety requirements in accordance with all applicable codes and standards.

These setup instructions assume the following.

- The drive is a 755TR regenerative and low harmonic drive.
- Drive and motor size have been carefully selected.
- The drive is at factory defaults. If not, unplug the output relay terminal block and issue a reset to factory defaults for the HOST and all PORTS. Plug the terminal block back in.
- Programming is done via the Connected Components Workbench software.
- Crane control is done via Run Forward/Run Reverse inputs.
- The drive is equipped with an I/O card, such as a 20-750-2262C-2R, in port (slot) 4. Mechanical brake control is wired to Output Relay 0 on that card.
- The drive is equipped with an incremental (20-750-ENC-1 or 20-750-ENC-1-XT) or dual incremental encoder board (20-750-DENC-1 or 20-750-DENC-1-XT) in port (slot) 5. You can use a Universal Feedback Board (20-750-UFB-1 or 20-750-UFB-1-XT). However, that configuration isn't covered in these instructions.
- The encoder is mounted on the back of the motor (not behind the gearbox).
- Recommended encoder specification: Quadrature differential (A, A-, B, B-), Line driver output, Minimum 1000PPR 5V, or 12V signals (12V preferred).

## Configure the Modular Control Profiles

1. Power up the drive and establish a connection with Connected Components Workbench software.
2. Navigate to the Overview page for the drive. Then click Device Definition.
3. Then click Dynamic Features.
4. Select Induction FV under Primary Motor Control Mode.
5. Only induction motor control modes are compatible with the TorqProve feature.
5. To accept the change to the motor control selection, click OK.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

6. Select Torque Prove under Application Select.

<!-- image -->

The software commits the changes.

8. To navigate to the parameter display, click Parameters in the left pane.
9. Navigate to port 0, which is the Main Product Port.
10. Find parameter 0:33 [VoltageClass Cfg] and enter the configuration for either Low Voltage or High Voltage.
11. Find parameter 0:35 [Duty Rating Cfg] and enter the configuration. Heavy Duty is recommended, but not required.
12. Navigate to parameter 0:46 [Velocity Units] and enter the configuration for Hz or RPM.

<!-- image -->

Cycle Power and Verify the Modular Control Profile Configurations

1. Cycle power or reset the drive (Reset Device) to load the control profiles.

IMPORTANT

You must cycle power or reset the drive (Reset Device) to load the value of these parameters.

2. Re-establish a connection with Connected Components Workbench software. Navigate to port 0.
3. To verify the configuration, navigate to 'Actual' feedback parameters:

0:34 [VoltageClass Act] 0:47 [Vel Units Act] 0:71 [Application Act]

0:36 [Duty Rating Act] 0:66 [Pri MtrCtrl Act]

## Configure the Line Side Converter

1. Navigate to port 13, which is the port for Line Side Converter Control.
2. Navigate to the following parameters and enter the data for the incoming power conditions.

13:30 [Nom Line Freq] 13:32 [AC Line kVA A] 13:34 [AC Line Imped% A]

3. Navigate to parameter 13:104 [Regen Power Lim] and enter a value of -200%.

## Enter the Motor Nameplate Data

1. Navigate to port 10, which is the port for Motor Side Inverter Control.
2. Navigate to the following parameters and enter the data from the motor nameplate.
- (1) If the data is not available on the motor nameplate or data sheet, use the following equation to estimate motor inertia: Motor Inertia = Motor Hp/250 x (Motor Hp/500 + 1)

10:400 [Motor NP Volts] 10:403 [Motor NP RPM] 10:406 [Motor NP Power]

10:401 [Motor NP Amps] 10:407 [Motor Poles] 10:402 [Motor NP Hertz]

10:900 [Motor Inertia] (1)

## Configure the Motor Side Inverter

1. Stay at port 10, which is the port for Motor Side Inverter Control.
2. Navigate to parameter 10:110 [Mtr Stop Mode A] and enter a value of 1 'Ramp'.
3. Navigate to parameter 10:229 [Regen Power Lim] and enter a value of -200%.
4. Navigate to parameter 10:204 [Mtr OL Hertz] and enter a value that reflects the cooling capacity of the motor. See parameter 10:204 [Mtr OL Hertz].
5. Navigate to parameter 10:220 [Drive OL Mode] and enter a value of 2 'Reduce PWM'.
6. Navigate to parameter 10:222 [Current Limit 1] and enter a value equal to 200% of motor nameplate amps.
7. Navigate to parameter 10:256 [OutPhaseLossActn] and enter a value of 3 'FltCoastStop'.
8. Navigate to parameter 10:116 [Bus Reg Mode A] and enter a value of 0 'Disabled'.
9. Navigate to parameter 10:913 [Autotune Trq Lim] and enter a value of 100%.

## Configure the Motor Encoder Feedback

1. Stay at port 10, which is the port for Motor Side Inverter Control.
2. Navigate to parameter 10:1000 [Pri Vel Fb Sel]. Select the encoder feedback on the feedback card in port 5.

If you're following the guidelines at the beginning of this procedure (with a 20-750-ENC1 or 20-750-ENC-1-XT in slot 5), the resulting value is 50004 'Port 5: Enc 0 FB'. Then enter the two-digit port number for the feedback option card, and the four-digit parameter number for the parameter that displays the feedback.

3. Navigate to parameter 10:1013 [PReg Fb Sel]. Then enter the same value that you used for 10:1000 [Pri Vel Fb Sel].
4. Navigate to the port that contains the feedback option card. That would be port 5 when using a 20-750-ENC-1 or 20-750-ENC-1-XT in slot 5.
5. Configure the parameters on the feedback option card so that they match the encoder you're using.

Parameters 5:1 [Encoder Cfg] and 5:2 [Encoder PPR] when using a 20-750-ENC-1 or 20750-ENC-1-XT in slot 5.

6. Navigate to parameter 10:256 [OutPhaseLossActn] and enter a value of 3 'FltCoastStop'.
7. Confirm the value of parameter 5:3 [Fdbk Loss Cfg] is 3 'FltCoastStop'.

## Autotune the Motor Side Inverter

Follow these Autotune steps to configure the motor side inverter.

## Perform Direction Test

| IMPORTANT   | During this test, the drive uses an internal reference that is positive (forward). During operation and other tests, the drive uses an external reference that you select. An external reference can include the HIM, analog input, or communicated reference. The direction of rotation depends on the polarity (direction) of that external reference. Make sure the external reference moves the motor in the intended direction.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1. Stay at port 10, which is the port for motor side inverter control.
2. Navigate to parameter 10:910 [Autotune] and enter a value of 1 'Direction Test'.
3. Start the drive. You can use the control bar feature in Connected Components Workbench software, the start key on the HIM, or the normal start signal.
4. Verify that the motor direction is forward.
5. Verify the polarity of the encoder feedback.
- Navigate to parameter 10:1832 [Enc VRef Sel] and select the encoder feedback on the feedback card in port 5. For example, the value would be 50004 'Port 5: Enc 0 FB' when you use a 20-750-ENC-1 or 20-750-ENC-1-XT in slot 5.
- View the result in parameter 10:1834 [Enc VRef].
6. Stop the drive, using the control bar feature in Connected Components Workbench software, the stop key on the HIM, or the normal stop signal.
7. Address the direction.
- If the direction is forward, proceed to the next step.
- If the direction is reverse, power down and physically reverse the motor leads.
8. Address the polarity of the feedback signal.
- If the polarity is forward, proceed to the next step.
- If the polarity is reverse, power down and physically reverse the encoder leads.

## Perform the Rotate Motor ID Test

During the Rotate Motor ID Test, the motor rotates for approximately 15 seconds in the commanded direction. It runs at speeds up to 75% of motor nameplate speed. You can execute this test with a motor that is disconnected from the crane or with a lightly loaded condition. Lightly loaded conditions include a motor that is connected to a gearbox, cable drum, or cable and hook.

When the motor is connected to a load, verify that there's enough travel distance for the Rotate Motor ID Test sequence to complete. If necessary, run out the crane hook for more travel distance in the opposite direction.

We recommend that you run the Rotate Motor ID Test. If you can't perform the Rotate test to completion, perform the Static Motor ID Test instead.

| IMPORTANT   | Confirm that the Rotate Motor ID Test can be stopped if an end travel condition is likely to occur. Confirm that the crane has control of the load at the end of the test. Manually engage the brake at the end to prevent the load from dropping.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1. Verify that the brake is disengaged.
2. Navigate to parameter 10:1898 [Vel Limit Pos] and enter a value of 40% of maximum speed.
3. Navigate to parameter 10:910 [Autotune] and enter a value of 3 'Rotate MtrID'.
4. Start the drive.

5. When the test is complete, manually engage the brake.
6. Navigate to parameter 10:510 [MtrParam C/U Sel]. Select a value of 1 'User Entered'. This selects the measured results from the Rotate Motor ID test, instead of the values estimated from the motor nameplate data.

## Perform the Static Motor ID Test

Perform this test if you can't perform the Rotate Motor ID Test. If you can perform that test, skip to Confirm Flux-up Time.

1. Set the brake.
2. Navigate to parameter 10:910 [Autotune] and enter a value of 2 'Static MtrID'.
3. Start the drive.
4. When the test is complete, navigate to parameter 10:510 [MtrParam C/U Sel]. Select a value of 1 'User Entered'. This selects the measured results from the Static Motor ID test, instead of the values estimated from the motor nameplate data.

## Confirm Flux-up Time

1. Navigate to parameter 10:432 [c FluxUpTime].
2. If the value is less than 0.05 seconds, change the value of parameter 10:431 [FluxUpTm C/U Sel] to 1 'User Entered'. Then set parameter 10:433 [u FluxUpTime] to 0.05 seconds.

## Configure the Digital Output for Brake Control

1. Determine whether the logic of the brake control circuit is 'Active High' or 'Active Low'. 'Active High' control sets or engages the brake when the signal is energized.
2. 'Active Low' control sets or engages the brake when the signal is de-energized.
2. Navigate to the port that contains the IO option card.
4. For example, navigate to port 4 when using a 20-750-2262C-2R in slot 4.
3. Configure the digital output selector to receive control from the correct bit in the Torque Prove status word.

For example, when using Relay Output 0 on the 20-750-2262C-2R in slot 4 to control the brake, go to parameter 4:10 [RO0 Sel]:

For 'Active High' control, set the value to 9:52 [Trq Prove Status] bit 4 'Brake Set' or

For 'Active Low' control, set the value to 9:52 [Trq Prove Status] bit 8 'BrakeRelease'.

## Configure the Torque Prove Function

1. Navigate to port 9, which is the port for Application Control.
2. Navigate to parameter 9:50 [Trq Prove Cfg]. Set bit 0 'TP Enable'.
3. Then set bit 6 'BrkSlipStart'.
4. Navigate to the following parameters and enter the data for the crane application.

9:53 [Trq Lmt SlewRate] 9:54 [Speed Dev Band] 9:55 [SpdBand Intgrtr]

9:60 [Brk Release Time] 9:61 [Brk Set Time] 9:62 [Brk Alarm Travel]

9:63 [Brk Slip Thresh] 9:64 [Brake Test Torq] 9:68 [DI Brake Fdbk]

9:70 [Float Tolerance] 9:71 [MicroPsnScalePct] 9:72 [ZeroSpdFloatTime]

9:78 [DI FloatMicroPsn]

## Confirm Configuration

1. Check brake control.
2. Run the crane up and down without the load.
3. Run the crane up and down with the load.
4. If necessary, adjust the acceleration and deceleration times.

10:1915 [VRef Accel Time1] 10:1917 [VRef Decel Time1]

5. If the 10007 TorqPrv Spd Band fault occurs, investigate the following:
- Verify that the brake is disengaging properly. A faulty brake rectifier can cause this fault.
- Verify that the current limit isn't impeding acceleration and deceleration. The drive is undersized or the acceleration and deceleration times are too short.
- Verify or adjust parameter 9:54 [Speed Dev Band] and/or parameter 10:906 [System BW].
- Verify that the position, velocity, and torque loops are tuned properly. See the PowerFlex 755T Flux Vector Tuning Manual, publication 750-AT006 .

Troubleshooting information can be found in Knowledgebase Article 1061994, PowerFlex 755T in Lifting Applications .

## Crane Setup—Encoderless

Review the Attention statement that follows if you intend to use the TorqProve feature without an encoder.

<!-- image -->

ATTENTION: You must read the following information before you can use TorqProve with no encoder.

Encoderless TorqProve must be limited to lifting applications where personal safety isn't a concern. Encoders offer additional protection and must be used where personal safety is a concern. Encoderless TorqProve can't hold a load at zero speed without a mechanical brake and does not offer additional protection if the brake slips/fails. Loss of control in suspended load applications can cause personal injury and/or equipment damage.

It is your responsibility to configure drive parameters, test any lifting functionality, and meet safety requirements in accordance with all applicable codes and standards. If encoderless TorqProve is desired, you must certify the safety of the application. To acknowledge that you have read this 'Attention' and properly certified the encoderless application, set bit 3 'EnclsTrqProv' of parameter 10:420 [Mtr Cfg Options] to a value of 1. This action removes Alarm 9014 'TP Encls Config' and allows bit 1 'Encoderless' of parameter 9:50 [Trq Prove Cfg] to be changed to 1 enabling encoderless TorqProve.

These setup instructions assume the following.

- The drive is a 755TR regenerative and low harmonic drive.
- Drive and motor size have been carefully selected.
- The drive is at factory defaults. If not, unplug the output relay terminal block and issue a reset to factory defaults for the HOST and all PORTS. Plug the terminal block back in.
- Programming is done via the Connected Components Workbench software.
- Crane control is done via Run forward/Run Reverse inputs.
- The drive is equipped with an I/O card, such as a 20-750-2262C-2R, in port (slot) 4. Mechanical brake control is wired to Output Relay 0 on that card.

<!-- image -->

ATTENTION: Loss of control in suspended load applications can cause personal injury and/or equipment damage. The drive or a mechanical brake must always control the loads. Parameters 9:60 [Brk Release Time]…78 [DI FloatMicroPsn] are designed for lifting/torque prove applications. It's the responsibility of the engineer and/or end user to configure drive parameters, test any lifting functionality and meet safety requirements in accordance with all applicable codes and standards.

## Configure the Modular Control Profiles

1. Power up the drive and establish a connection with Connected Components Workbench software.
2. Navigate to the Overview page for the drive. Then click Device Definition.
3. Then click Dynamic Features.
4. Select Induction FV under Primary Motor Control Mode.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Permanent Magnet motor control mode isn't compatible with the TorqProve feature.

5. To accept the change to the motor control selection, click OK.
6. Select Torque Prove under Application Select.
7. Click OK.

<!-- image -->

<!-- image -->

The software commits the changes.

8. Navigate to the parameter display by clicking Parameters in the left-hand pane.
9. Navigate to port 0, which is the Main Product Port.
10. Find parameter 0:33 [VoltageClass Cfg] and enter the configuration for Low Voltage or High Voltage.
11. Find parameter 0:35 [Duty Rating Cfg] and enter the configuration. Heavy Duty is recommended, but not required.
12. Navigate to parameter 0:46 [Velocity Units] and enter the configuration for Hz or RPM.

<!-- image -->

## Cycle Power and Verify the Modular Control Profile Configurations

1. Cycle power or reset the drive (Reset Device) to load the control profiles.

## IMPORTANT

You must cycle power or reset the drive (Reset Device) to load

## the value of these parameters.

2. Re-establish a connection with Connected Components Workbench software. Navigate to port 0.
3. To verify the configuration, navigate to 'Actual' feedback parameters:

0:34 [VoltageClass Act] 0:47 [Vel Units Act] 0:71 [Application Act]

0:36 [Duty Rating Act] 0:66 [Pri MtrCtrl Act]

## Configure the Line Side Converter

1. Navigate to port 13, which is the port for Line Side Converter Control.
2. Navigate to the following parameters and enter the data for the incoming power conditions.
3. Navigate to parameter 13:104 [Regen Power Lim] and enter a value of -200%.

13:30 [Nom Line Freq] 13:32 [AC Line kVA A] 13:34 [AC Line Imped% A]

## Enter the Motor Nameplate Data

1. Navigate to port 10, which is the port for Motor Side Inverter Control.
2. Navigate to the following parameters and enter the data from the motor nameplate.
- (1) If the data is not available on the motor nameplate or data sheet, use the following equation to estimate motor inertia: Motor Inertia = Motor Hp/250 x (Motor Hp /500 + 1)

10:400 [Motor NP Volts] 10:403 [Motor NP RPM] 10:406 [Motor NP Power]

10:401 [Motor NP Amps] 10:407 [Motor Poles] 10:402 [Motor NP Hertz]

10:900 [Motor Inertia] (1)

## Configure the Motor Side Inverter

1. Stay at port 10, which is the port for Motor Side Inverter Control.
2. Navigate to parameter 10:110 [Mtr Stop Mode A] and enter a value of 1 'Ramp'.
3. Navigate to parameter 10:229 [Regen Power Lim] and enter a value of -200%.
4. Navigate to parameter 10:204 [Mtr OL Hertz] and enter a value that reflects the cooling capacity of the motor.
5. Navigate to parameter 10:220 [Drive OL Mode] and enter a value of 2 'Reduce PWM'.
6. Navigate to parameter 10:222 [Current Limit 1] and enter a value equal to 200% of motor nameplate amps.
7. Navigate to parameter 10:256 [OutPhaseLossActn] and enter a value of 3 'FltCoastStop'.
8. Navigate to parameter 10:116 [Bus Reg Mode A] and enter a value of 0 'Disabled'.
9. Navigate to parameter 10:913 [Autotune Trq Lim] and enter a value of 100%.

## Autotune the Motor Side Inverter

Follow these Autotune steps to configure the motor side inverter.

Perform the Direction Test

| IMPORTANT   | During this test, the drive uses an internal reference that is positive (forward). During operation and other tests, the drive uses an external reference that you select. An external reference can include the HIM, analog input, or communicated reference. The direction of rotation depends on the polarity (direction) of that external reference. Make sure the external reference moves the motor in the intended direction.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1. Stay at port 10, which is the port for Motor Side Inverter Control.
2. Navigate to parameter 10:910 [Autotune] and enter a value of 1 'Direction Test'.
3. Start the drive. You can use the control bar feature in Connected Components Workbench software, the start key on the HIM or the normal start signal.
4. Verify that the motor direction is forward.
5. Verify the polarity of the encoder feedback.
- Navigate to parameter 10:1832 [Enc VRef Sel] and select the encoder feedback on the feedback card in port 5. The value would be 50004 'Port 5: Enc 0 FB' when using a 20750-ENC-1 or 20-750-ENC-1-XT in slot 5.
- View the result in parameter 10:1834 [Enc VRef].
6. Stop the drive from the control bar feature in Connected Components Workbench software, the stop key on the HIM, or the normal stop signal.
7. Address the direction.
- If the direction is forward, proceed to next step.
- If the direction is reverse, power down and physically reverse the motor leads.

## Perform the Rotate Motor ID Test

During the Rotate Motor ID Test, the motor rotates for around 15 seconds in the commanded direction. It runs at speeds up to 75% of motor nameplate speed. You can execute this test with the motor that is disconnected from the crane or with a lightly loaded condition. Lightly loaded conditions include motor that is connected to gearbox, cable drum, or cable and hook.

If the motor is connected to a load, determine whether there's enough travel distance for the Rotate Motor ID Test sequence to complete. If necessary, run the crane hook to top or bottom for more travel distance in the opposite direction.

It's preferable to run the Rotate Motor ID Test. If you can't perform the Rotate test to completion, perform the Static Motor ID Test instead.

| IMPORTANT   | Verify that the Rotate Motor ID Test can be stopped if an end travel condition is likely to occur. Verify that the crane has control of the load at the end of the test. Manually engage the brake at the end to prevent the load from dropping.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1. Verify that the brake is disengaged.
2. Navigate to parameter 10:1898 [Vel Limit Pos] and enter a value of 40% of maximum speed.
3. Navigate to parameter 10:910 [Autotune] and enter a value of 3 'Rotate MtrID'.
4. Start the drive.
5. When the test is complete, manually engage the brake.

6. Navigate to parameter 10:510 [MtrParam C/U Sel]. Select a value of 1 'User Entered'. This selects the measured results from the Rotate Motor ID test, instead of the values estimated from the motor nameplate data.

## Perform the Static Motor ID Test

Perform this test if you can't perform the Rotate Motor ID test. If you can perform the Rotate Motor ID test, skip to Confirm Flux-up Time.

1. Set the brake.
2. Navigate to parameter 10:910 [Autotune] and enter a value of 2 'Static MtrID'.
3. Start the drive.
4. When the test is complete, navigate to parameter 10:510 [MtrParam C/U Sel]. Select a value of 1 'User Entered'. This selects the measured results from the Static Motor ID test, instead of the values estimated from the motor nameplate data.

## Confirm Flux-up Time

1. Navigate to parameter 10:432 [c FluxUpTime].
2. If the value is less than 0.05 seconds, change the value of parameter 10:431 [FluxUpTm C/U Sel] to 1 'User Entered'. Then set parameter 10:433 [u FluxUpTime] to 0.05 seconds.

## Configure the Digital Output for Brake Control

1. Determine whether the logic of the brake control circuit is 'Active High' or 'Active Low'. 'Active High' control sets or engages the brake when the signal is energized. 'Active Low' control sets or engages the brake when the signal is de-energized.
2. Navigate to the port that contains the IO option card.

For example, navigate to port 4 when using a 20-750-2262C-2R in slot 4.

3. Configure the digital output selector to receive control from the correct bit in the Torque Prove status word.

For example, when using Relay Output 0 on the 20-750-2262C-2R in slot 4 to control the brake, go to parameter 4:10 [RO0 Sel]:

For 'Active High' control, set the value to 9:52 [Trq Prove Status] bit 4 'Brake Set' or

For 'Active Low' control set the value to 9:52 [Trq Prove Status] bit 8 'BrakeRelease'.

## Configure the Torque Prove Function

1. Navigate to port 9, which is the port for Application Control.
2. Navigate to parameter 9:50 [Trq Prove Cfg].
- a. Set bit 0 'TP Enable'
- b. Set bit 1 'Encoderless'
- c. Set bit 5 'BrkSlipEncls'

## IMPORTANT

An alarm indicates that the drive is in the state that is described on page 160. Carefully read the Attention statement and acknowledge it by setting the required parameter.

3. Navigate to the following parameters and enter the data for the crane application.

9:53 [Trq Lmt SlewRate] 9:54 [Speed Dev Band] 9:55 [SpdBand Intgrtr]

9:60 [Brk Release Time] 9:61 [Brk Set Time] 9:62 [Brk Alarm Travel]

9:63 [Brk Slip Thresh] 9:64 [Brake Test Torq] 9:68 [DI Brake Fdbk]

9:70 [Float Tolerance] 9:71 [MicroPsnScalePct] 9:72 [ZeroSpdFloatTime]

9:78 [DI FloatMicroPsn]

## Confirm Configuration

1. Check brake control.

## Anti-Sway Applications

2. Run crane up and down without load.
3. Run crane up and down with load.
4. If necessary, adjust the acceleration and deceleration times.
5. If the 10007 TorqPrv Spd Band fault occurs, investigate the following:
- Verify that the brake is disengaging properly. A faulty brake rectifier can prevent the brake from disengaging.
- Verify that the current limit isn't impeding acceleration and deceleration. The drive is undersized or the acceleration and deceleration times are too short.
- Verify or adjust parameter 9:54 [Speed Dev Band] and/or parameter 10:906 [System BW].
- Verify that the position, velocity, and torque loops are tuned properly. See the PowerFlex 755T Flux Vector Tuning Manual, publication 750-AT006 .

10:1915 [VRef Accel Time1] 10:1917 [VRef Decel Time1]

Troubleshooting information can be found in Knowledgebase Article 1061994, PowerFlex 755T in Lifting Applications .

Anti-Sway is a PowerFlex 755T drive feature that helps to minimize the pendulum effect that can occur when a trolley/gantry of a crane/hoist system moves a suspended load. The distance between the trolley and the load determines the sway frequency. This frequency can be notched from the velocity/position command of the drive so that the pendulum effect on the load isn't excited because of a horizontal move. The pendulum can still be excited from external disturbances such as wind or from nonzero initial conditions like picking up a load off center.

## Reference Notch Filters

Reference notch filters are the main feature that is used to control sway by suppressing the sway frequency during position/velocity reference changes. There are two notch filters in the reference path that modify the ramped reference profile. Values of notch filter parameters can be entered manually or calculated automatically based on hoist cable length.

<!-- image -->

The reference notch filters are applied to the horizontally moving axes, that is the trolley and gantry sections of a crane.

- Reference notch filters can be applied to V/Hz, Sensorless Vector, and Flux Vector motor control modes
- Reference notch filters only affect the motion of the axis due to changing speed references.
- Reference notch filters can be applied to velocity, position, and process control reference sources.
- Anti-sway control doesn't use any load sway feedback sensors.

- Anti-sway control can't compensate for sway induced by external forces such as wind or unbalanced loads.

<!-- image -->

The PowerFlex 755T with TotalFORCE control includes tunable reference notch filters that are in the velocity, position, and process control reference paths after the ramp generator.

Two separate reference notch filters (NF1 and NF2) are provided to tune the anti-sway control more closely for varying or unknown sway frequencies.

Figure 64 - Velocity Reference—Flux Vector

<!-- image -->

Notch Filters are band attenuating filters that allow frequencies above and below the filter center frequency to pass unattenuated. Frequencies near the center frequency are sharply attenuated.

<!-- image -->

## Calculating the Sway Frequency

The reference notch filter frequency is set to the swinging pendulum frequency of the payload that is attached to the hoist axis.

The reference notch filter frequency (f) calculation in [Hz] is a function of cable length (L) and the acceleration of gravity (g).

<!-- formula-not-decoded -->

Where…

f = filter center frequency in Hertz g = acceleration due to gravity 9.81 m/sec 2 , 32.17 ft/sec 2 , 386.09 in/sec 2

L = length from cable pivot point to load center of gravity (meters, feet, or inches)

<!-- image -->

The mass or weight of the Load does not affect the notch filter frequency calculation.

When performing this calculation, you can use any set of consistent unit systems.

If cable lengths can't be measured, estimate the reference notch filter frequency experimentally by displacing the load to an initial angle and let it oscillate for a time period (t) seconds while counting the number of swings (n). With this knowledge, frequency is derived as:

<!-- formula-not-decoded -->

## Cable Length Variation

Knowing the accurate cable length is important as it affects the center frequency of the notch filter.

Based on the application, the cable length can vary between a minimum and maximum length (L min and L max ), which results in a varying sway frequency. The range of such length change can determine the system configuration.

A larger variation of cable length can result in a larger variation in frequency.

<!-- image -->

The following experimental result shows how deviation from the actual cable length affects the sway magnitude when the filter frequency does not accurately match the sway oscillation frequency. The sway magnitude increases as the cable length error becomes higher as shown in Figure 65 .

Figure 65 - Sway Magnitude (Degrees) vs. Cable Length Error (Percent)

<!-- image -->

## Reference Notch Filter Configurations

Different applications have different variations of cable length. Based on these variations there are three configurations.

## Single Filter—One Fixed Frequency

- Simple method offers good compensation, minimal impact on move times
- Filter frequency is based on maximum cable length (L max )
- Load sway varies as cable length changes

Dual Filters—Two Fixed Frequencies

- Improves compensation, reduces variation in load sway
- One filter frequency is based on the maximum cable length (L max )
- The other filter frequency is based on the average cable length (L avg )
- Can increase move times

Single Filter—Variable Frequency Hoist Cable Length Feedback

- Best compensation, variable frequency calculation as cable length changes
- The filter frequency is dynamically varied between the minimum cable length (Lmin) and maximum cable length (L max )
- More complex, requires hoist encoder feedback and Logix controller

## Single Filter—One Fixed Frequency

In this configuration, one of the reference notch filters is set to match the maximum crane length (L max ).

This method provides good anti-sway compensation and fast settling time for moderate variations in hoist cable length.

NF1 reference notch filter frequency calculation.

<!-- formula-not-decoded -->

<!-- image -->

Example: L max = 20 meters, g = 9.81 meter/sec 2

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

NF1 reference notch filter frequency parameter settings.

- 10:966 [Crane Length 1] = 0 (cable length is manually calculated)
- 10:942 [Ref NF1 Freq] = 0.111 (from calculation)
- 10:943 [Ref NF1 Width] = 0.707 (default)
- 10:944 [Ref NF1 Depth] = 0.0 (default)
- 10:945 [Ref NF1 Gain] = 1.0 (default)

Second reference notch filter isn't used.

- 10:948 [Ref NF2 Freq] = 0.0 (default)
- 10:949 [Ref NF2 Width] = 0.707 (default)
- 10:950 [Ref NF2 Depth] = 0.0 (default)
- 10:951 [Ref NF2 Gain] = 1.0 (default)

## Dual Filters—Two Fixed Frequencies

With this configuration, one of the reference notch filters is set to match the average cable length (L avg ).

The other reference notch filter is set to match the maximum cable length (L max ). This method provides better anti-sway compensation than the single filter but can cause longer move times.

Reference Notch Filter NF1 and NF2 calculation.

<!-- image -->

Example: Lmin = 1 meter, L max = 20 meters, g= 9.81 m/sec 2

<!-- formula-not-decoded -->

First reference notch filter Frequency is set for average L frequency

- 10:966 [Crane Length 1] = 0 (cable length is manually calculated)
- 10:942 [Ref NF1 Freq] = 0.154 (from calculation)
- 10:943 [Ref NF1 Width] = 0.707 (default)
- 10:944 [Ref NF1 Depth] = 0.0 (default)
- 10:945 [Ref NF1 Gain] = 1.0 (default)

Second reference notch filter is set for L max frequency

- 10:948 [Ref NF2 Freq] = 0.111 (from calculation)
- 10:949 [Ref NF2 Width] = 0.707 (default)
- 10:950 [Ref NF2 Depth] = 0.0 (default)
- 10:951 [Ref NF2 Gain] = 1.0 (default)

## Single Filter—Variable Frequency Hoist Cable Length Feedback

In this configuration, one reference notch filter is set dynamically as the length of the Hoist crane cable changes between minimum length (Lmin) and maximum length (L max ). This method provides the lowest load sway magnitude over the hoist crane length of motion. One reference notch filter frequency is dynamically varied in response to the Hoist crane length feedback.

<!-- formula-not-decoded -->

<!-- image -->

## Where…

g = acceleration due to gravity 9.81 m/sec 2

L = actual cable length in meters

This approach requires a Logix controller with hardware interconnection and/or communication links.

The encoder position feedback from the hoist drive is sent via a DataLink to the Logix controller.

Within a Logix controller, the hoist encoder position feedback is used to generate and scale the crane length (L) length in meters.

The instantaneous crane length (L) is then sent via DataLinks to trolley and/or gantry drives.

<!-- image -->

## Logix Controller Programming:

- Assign Hoist motor encoder feedback to DataLink
- Logix program task calculates and scales Hoist encoder counts to crane length (L) in meters
- Assign crane length to DataLinks for trolley and gantry drives

Within the Logix controller program task, calculate the cable length from hoist motor encoder feedback. We can assume a linear relationship between the crane length (L) and the encoder counts (X), as:

<!-- formula-not-decoded -->

## Where…

L = current crane length in meters

Xcurrent = current hoist motor encoder feedback counts

Xoffset = hoist motor encoder offset counts

Cal Const = encoder calibration constant in counts/meter

The value of Xoffset must be set such that when the hoist is at maximum operating height the crane length (L) is equal the measured Lmin from the pivot point in meters.

It's important that the crane length (L) isn't equal to or less than zero.

To find the calibration constant (Cal Const), two given points are required: L1 and L2, which can be obtained by measuring the cable length at two arbitrary points and capturing the corresponding hoist encoder counts, X1 and X2.

Determine the crane length calibration constant, Cal Const, in counts/meter:

<!-- image -->

Where…

Cal Const = encoder calibration constant in counts/meter

X1 = encoder counts at L1

X2 = encoder counts at L2

L1 = crane length at X1 in meters

L2 = crane length at X2 in meters

Within the trolley and/or gantry drives, the instantaneous cable length DataLink is assigned to parameter 10:966 [Crane Length 1]

Figure 66 - Automatic Calculation from Cable Length

<!-- image -->

## Dynamic Braking

The trolley and/or gantry drives use the data in parameter 10:966 [Crane Length 1] to calculate the frequency for reference notch filter NF1 dynamically.

<!-- formula-not-decoded -->

Where…

g = acceleration due to gravity 9.81 m/sec 2

L = 10:966 [Crane Length 1] in meters

Automatic Reference Notch Filter Frequency

- 10:966 [Crane Length 1] (DataLink)
- 10:954 [Ref NF1 Freq Act] = 10:966 [Crane Length 1]
- 10:956 [Ref NF1 Depth Act] = 0
- 10:957 [Ref NF1 Gain Act] = 1.0

When an induction motor's rotor is turning slower than the synchronous speed set by the drive's output power; the motor is transforming electrical energy that is obtained from the drive into mechanical energy available at the drive shaft of the motor. This process is referred to as motoring.

When the rotor is turning faster than the synchronous speed set by the drive's output power, the motor is transforming mechanical energy available at the drive shaft of the motor into electrical energy that can be transferred back into the utility grid. This process is referred to as regeneration.

On most AC PWM drives, the AC power available from the fixed frequency utility grid is first converted into DC power with a diode rectifier bridge or controlled SCR bridge, before being inverted into variable frequency AC power. These diode or SCR bridges are cost-effective, but can handle power in only one direction, and that direction is the motoring direction. If the motor is regenerating, the bridge is unable to conduct the necessary negative DC current, and the DC bus voltage increases until the drive trips on an over voltage fault.

There are bridge configurations that use either SCRs or transistors that can transform DC regenerative electrical energy into fixed frequency utility electrical energy but are expensive. A more cost-effective solution is to provide a transistor chopper on the DC bus of the AC PWM drive that feeds a power resistor, which transforms the regenerative electrical energy into thermal heat energy, which is dissipated into the local environment.

This process is called dynamic braking, with the chopper transistor and related control and components that are called the chopper module, and the power resistor called the dynamic brake resistor. The entire assembly of a chopper module with dynamic brake resistor is sometime referred to as the dynamic brake module. More modern AC PWM drives have a dedicated IGBT built into the package for dynamic braking. The rest of this topic discusses drives that have a seventh IGBT.

## How it Works

There are two different types of control for dynamic braking, hysteretic control and PWM control. Each used by themselves in a standard, standalone product has no advantage over the other. The preferred control is the PWM method when the application is a common DC bus. A description of this advantage follows.

## Hysteretic Control

The hysteretic method of dynamic braking uses a voltage sensing circuit to monitor the DC bus. As the DC bus voltage increases to the Vdc\_on level the brake IGBT is turned on and is left on until the voltage drops to the Vdc\_off level, which isn't so desirable in common DC bus
() dc\_of
applications (see the following graph).

<!-- image -->

## PWM Control

This type of control that operates the brake IGBT is similar to the way the output voltage to the motor is controlled. As the DC bus voltage increases and reaches some predetermined limit, the brake IGBT is turned on/off according to a control algorithm switched at 1 kHz. This type of control virtually eliminates bus ripple. The significant advantage is when this type of control is used in a common bus configuration.

<!-- image -->

Duty Cycle

<!-- image -->

## Common DC Bus Applications

In a common bus configuration, when a dynamic braking resistor is installed on each drive on a shared DC bus, it's possible that the brake IGBT in other drives won't turn on. The impression is that the drive isn't functioning correctly or that one drive's brake IGBT is failing while the other drives are fine. The following diagram, shows the DC bus level for two drives on a common bus. The delta between these voltages is exaggerated for clarity. As the voltage increases, the Drive #1 IGBT turns on and decreases the voltage level before Drive #2 sees voltage high enough to be told to turn on. The result is Drive #1 does all dynamic braking. Now this situation could be acceptable as long as the minimum ohmic value for resistance isn't violated and the regeneration event isn't so great that one resistor can't handle the power. If there's a large regeneration event where the voltage continues to rise after Drive #1 has turned on, Drive #2 fires its IGBT when it reaches the voltage limit.

<!-- image -->

Here are two drives with PWM DB control on a common bus. Because one drive turns on at a certain duty cycle, the bus voltage is likely to continue to rise guaranteeing that the other drive's IGBT turns on (at another duty cycle).

<!-- image -->

## How to Select A Chopper Module and Dynamic Brake Resistor

In general, the dynamic brake resistor value can be estimated by using the motor power rating, speed, torque, and regenerative mode of operation. A rule of thumb to use is that a dynamic brake module resistor can be specified when regenerative energy is dissipated on an occasional or periodic basis. When a drive is consistently operating in the regenerative mode of operation, consider using equipment that transforms the electrical energy back to the fixed frequency utility.

The peak regenerative power of the drive must be calculated to determine the maximum Ohmic value of the dynamic brake resistor. A range of allowable dynamic brake ohmic values is now known. These values exist from the minimum value set by the transistor current rating to a maximum value set by the peak regenerative power that the drive develops to decelerate or satisfy other regenerative applications. If a dynamic brake resistance value less than the minimum imposed by the AC drive's specification is applied, damage can occur to the transistor. If a dynamic brake resistance value greater than the maximum imposed by the choice of the peak regenerative drive power is applied, the drive can trip due to transient DC bus overvoltage problems. Once the choice of the approximate Ohmic value of the dynamic brake resistor is made, the wattage rating of the dynamic brake resistor can be determined.

The wattage rating of the dynamic brake resistor is estimated by applying the knowledge of the drive motoring and regeneration modes of operation. The average power dissipation of the regeneration mode must be estimated and the wattage of the chosen dynamic brake resistor to be slightly greater than the average power dissipation of the drive. If the dynamic brake resistor has a large thermodynamic heat capacity, the resistor element is able to absorb a large amount of energy without the temperature of the resistor element exceeding the operational temperature rating. Thermal time constants of 50 seconds and higher satisfy the criteria of large heat capacities for these applications. If a resistor has a small heat capacity, the temperature of the resistor element could exceed the maximum temperature limits during the application of pulse power to the element and could exceed the safe temperature limits of the resistor.

The peak regenerative power can be calculated in English units (horsepower), in The International System of Units, SI (watts), or in the per unit system (pu), which is dimensionless usually. In any event, the final number must be in watts. Calculations in the following examples are demonstrated in SI units.

## Speed, Torque, Power Profile

The following figure is a typical dynamic braking application. The top trace represents speed and is designated by the omega symbol. In the profile, the motor is accelerated to a speed, it holds that speed, and is then decelerated. This deceleration isn't necessarily to zero speed. The cycle is then repeated.

The middle trace represents motor torque. Torque starts out high as the motor is accelerated then drops down to maintain the commanded speed. Then the torque turns negative as the motor is decelerated. The cycle is then repeated.

The bottom trace represents motor power. Power increases as the motor speed increases. Power decreases some to maintain the commanded speed then goes negative when deceleration starts. Point -P b is the first value that must be calculated. The cycle is then repeated.

<!-- image -->

To size the dynamic brake, gather the following information.

- The nameplate power rating of the motor in watts, kilowatts, or horsepower.
- The nameplate speed rating of the motor in rpm or rps.
- The motor inertia and load inertia in kilogram-meters 2 , or lb·ft 2 .
- The gear ratio, if a gear is present between the motor and load, GR.
- Review the speed, torque power profile of the application.

The equations that are used for calculating dynamic braking values use the following variables.

w(t) = The motor shaft speed in radians/second, or Rad s 2N 60 = ----------

N(t) = The motor shaft speed in revolutions per minute (rpm)

T(t) = The motor shaft torque in Newton-meters, 1.0 lb·ft = 1.355818 N·m

P(t) = The motor shaft power in watts (1.0 Hp = 746 watts)

-P b = The motor shaft peak regenerative power in watts

## Internal Brake IGBT for PowerFlex 755TS Drives

Step 1 – Determine the Total Inertia

<!-- formula-not-decoded -->

J T = Total inertia reflected to the motor shaft, kg·m 2 or lb·ft 2

J m = motor inertia, kg·m 2 or lb·ft 2

GR = The gear ratio for any gear between motor and load, dimensionless

J L = load inertia, kg·m 2 or lb·ft 2 (1.0 lb·ft 2 = 0.04214011 kg·m 2 )

Step 2 – Calculate the Peak Braking Power

<!-- formula-not-decoded -->

J T T = Total inertia reflected to the motor shaft, kg·m 2

 = Rated angular rotational speed, Rad s 2N 60 = ----------

N = Rated motor speed, rpm t 3 3 - t 2 2 = Total time of deceleration from the rated speed to 0 speed in seconds

P b = Peak braking power, watts (1.0 Hp = 746 watts)

Compare the peak braking power to that of the rated motor power, if the peak braking power is greater that 1.5 times that of the motor, then the deceleration time, (t3 - t2), needs to be increased so that the drive does not go into current limit. Use 1.5 times because the drive can handle 150% current maximum for 3 seconds.

Peak power can be reduced by the losses of the motor and inverter.

Table 41 - Brake Resistance for 400/480V Drives

| ND kW Catalog Code   | Min Resistance Max DB Current Max Duty Cycle  Min   | ND Hp Catalog Code   | Resistance Max DB Current Max Duty Cycle   |
|----------------------|-----------------------------------------------------|----------------------|--------------------------------------------|
|                      | 0.75 C2P1 79.0 10 0.453 1.0 D2P1 79.0 10 0.453      |                      |                                            |
|                      | 1.5 C3P5 79.0 10 0.453 2.0 D3P4 79.0 10 0.453       |                      |                                            |
|                      | 2.2 C5P0 79.0 10 0.453 3.0 D5P0 79.0 10 0.453       |                      |                                            |
|                      | 4 C8P7 52.7 15 0.453 5.0 D8P0 52.7 15 0.453         |                      |                                            |
|                      | 5.5 C011 31.6 25 0.453 7.5 D011 31.6 25 0.453       |                      |                                            |
|                      | 7.5 C015 31.6 25 0.453 10 D014 31.6 25 0.453        |                      |                                            |
|                      | 0.75 C2P1 31.6 25 0.4844 1.0 D2P1 31.6 25 0.4844    |                      |                                            |
|                      | 1.5 C3P5 31.6 25 0.4844 2.0 D3P4 31.6 25 0.4844     |                      |                                            |
|                      | 2.2 C5P0 31.6 25 0.4844 3.0 D5P0 31.6 25 0.4844     |                      |                                            |
|                      | 4 C8P7 31.6 25 0.4844 5.0 D8P0 31.6 25 0.4844       |                      |                                            |
|                      | 5.5 C011 31.6 25 0.4844 7.5 D011 31.6 25 0.4844     |                      |                                            |
|                      | 7.5 C015 31.6 25 0.4844 10 D014 31.6 25 0.4844      |                      |                                            |
|                      | 11 C022 22.6 34.9 0.5603 15 D022 22.6 34.9 0.5603   |                      |                                            |
|                      | 15 C030 31.6 25 0.9857 20 D027 31.6 25 0.9857       |                      |                                            |
|                      | 18.5 C037 31.6 25 0.9857 25 D034 31.6 25 0.9857     |                      |                                            |
|                      | 22 C043 16.6 47.6 0.9857 30 D040 16.6 47.6 0.9857   |                      |                                            |
| 30(1)  C061(1)       | 15.8 50 0.9857  40(1)                               | D053(1)              | 15.8 50 0.9857                             |
|                      | 30 C060 15.8 50 0.9392 40 D052 15.8 50 0.9392       |                      |                                            |
|                      | 37 C072 15.8 50 0.9392 50 D065 15.8 50 0.9392       |                      |                                            |
| 37(2)  C073(2)       | 12 65.8 0.9392  50(2)                               | D066(2)              | 12 65.8 0.9392                             |
|                      | 45 C086 12 65.8 0.9288 60 D078 12 65.8 0.9288       |                      |                                            |

Step 3 – Calculating the Maximum Dynamic Brake Resistance Value

<!-- formula-not-decoded -->

V d d = The value of DC bus voltage that the drive regulates at and is equal to 375V DC, 750V DC, or 937.5V DC depending on input voltage

P b = The peak braking power calculated in step 2

R db1 1 = The maximum allowable value for the dynamic brake resistor

Choose a dynamic brake resistance value that is less than the value calculated in step 3. If the value is greater than the calculated value, the drive can trip on a DC bus overvoltage fault. Remember to account for resistor tolerances.

## Step 4 – Determine the Minimum Resistance

Each drive with an internal dynamic brake IGBT has a minimum resistance that is associated with it. The dynamic brake resistor can be damaged if a resistance lower than the minimum value for a given drive is connected. The following is a table of minimum resistances for PowerFlex 755TS drives, frames 1...7.

Table 41 - Brake Resistance for 400/480V Drives (Continued)

| 400V 480V          | 400V 480V                                         | 400V 480V                                     | 400V 480V                                         | 400V 480V   |
|--------------------|---------------------------------------------------|-----------------------------------------------|---------------------------------------------------|-------------|
| ND kW Catalog Code | Min Resistance Max DB Current Max Duty Cycle      | ND Hp Catalog Code  Resistance Max Duty Cycle | Min Max DB Current                                |             |
| 37(2)  C075(2)     | 7.9 100 0.8279                                    | 50(2)  D065(2)                                | 7.9 100 0.8279                                    |             |
|                    |                                                   | 45 C085 7.9 100 0.8279 60 D077 7.9 100 0.8279 |                                                   |             |
|                    |                                                   | 55 C104 7.9 100 0.8279 75 D096 7.9 100 0.8279 |                                                   |             |
| 55(2)  C104(2)     | 3.3 239.4 0.912                                   | 75(2)  D096(2)                                | 3.3 239.4 0.912                                   |             |
|                    |                                                   |                                               | 75 C140 3.3 239.4 0.912 100 D125 3.3 239.4 0.912  |             |
|                    |                                                   |                                               | 90 C170 3.3 239.4 0.912 125 D156 3.3 239.4 0.912  |             |
|                    |                                                   |                                               | 110 C205 3.3 239.4 0.912 150 D186 3.3 239.4 0.912 |             |
|                    | 132 C260 3.3 239.4 0.912 200 D248 3.3 239.4 0.912 |                                               |                                                   |             |
| 132(2)  C260(2)    | 2.4 329 0.78                                      | D248(2)                                       | 200(2)  2.4 329 0.78                              |             |
|                    |                                                   | 160 C302 2.4 329 0.78 250 D302 2.4 329 0.78   |                                                   |             |
|                    |                                                   | 200 C367 2.4 329 0.78 300 D361 2.4 329 0.78   |                                                   |             |
|                    |                                                   |                                               | 250 C456 1.65 478.8 0.78 350 D415 1.65 478.8 0.78 |             |
|                    |                                                   |                                               | 270 C477 1.65 478.8 0.78 400 D477 1.65 478.8 0.78 |             |

## Step 5 – Choosing the Dynamic Brake Resistance Value

To avoid damage to this transistor and get the desired braking performance, select a resistor with a resistance between the maximum resistance that is calculated in step 3 and the minimum resistance of the drive IGBT.

Step 6 – Estimating the Minimum Wattage requirements for the dynamic brake resistor

It's assumed that the application exhibits a periodic function of acceleration and deceleration. If (t 3 - t2) = the time in seconds necessary for deceleration from rated speed to 0 speed, and t4
() 3 2
is the time in seconds before the process repeats itself, then the average duty cycle is (t3 - t2)/ t 4 . The power as a function of time is a linearly decreasing function from a value equal to the 4
peak regenerative power to 0 after (t3 - t2) seconds have elapsed. The average power
() 3 2
regenerated over the interval of (t3 - t2) seconds is Pb/2. The average power in watts that are regenerated over the period t4 is:

<!-- formula-not-decoded -->

P av v = Average dynamic brake resistor dissipation, in watts t 3 3 - t 2 2 = Elapsed time to decelerate from rated speed to 0 speed, in seconds

t 4 = Total cycle time or period of process, in seconds

P b = Peak braking power, in watts

The dynamic brake resistor power rating in watts that is chosen will be equal to or greater than the value calculated in step 6.

Step 7 – Calculate the requires Watt-Seconds (joules) for the resistor

To be sure the resistor's thermal capabilities are not violated, a calculation to determine the amount of energy dissipated into the resistor is made. This determines the amount joules the resistor must be able to absorb.

<!-- formula-not-decoded -->

P ws = Required watt - seconds of the resistor t 3 3 - t 2 2 = Elapsed time to decelerate from wb speed to w0 speed, in seconds

P b = Peak braking power, in watts

## Dynamic Bus Control

Applications with cyclic speed and load fluctuations such as servo presses and high-speed cut-to-length systems often have high motoring and regenerative peak torque demands applied within one cycle of machine operation. This type of load typically has a fixed mass (inertia) and low losses. To reduce the power converter peak power demand, large DC bus capacitor banks are employed that are designed to absorb regenerative (deceleration) energy from the load then transfer energy to the load during motoring (acceleration) periods of the cycle.

Typical active front end converter systems attempt to regulate the DC Bus voltage to a setpoint. When in this mode the active front end converter attempts to control the DC Bus to this level whether the drive is motoring or regenerating. The following illustrative plots show a typical cyclical load speed/torque profile with standard internal DC bus capacitance and DC bus voltage regulation enabled. This results in high peak motoring and regenerative Converter AC Input Power peak demands required to regulate the DC bus voltage.

Applications with cyclic speed and load profiles, such as servo presses and rotary shears can use additional DC bus capacitance to soften the peak motoring and regeneration AC line power demand.

<!-- image -->

Figure 67 - DC Bus Voltage Regulation

<!-- image -->

Dynamic bus control was designed to allow the active front end converter to tolerate cyclic fluctuations in DC bus voltage due to energy exchanging from the load to the DC bus capacitor bank with minimal converter motoring or regenerative power exchange with the AC line. Because the converter is supplying system losses the rating of the bus supply converter and AC supply may be reduced. The following illustrative plots show the same load speed/torque profile as the example above but with an external DC bus capacitor bank and Dynamic Bus Control enabled. The peak Converter AC Input Power is significantly reduced compared to the DC Bus Voltage Regulation depicted in Figure 67 .

<!-- image -->

- Dynamic bus control for PowerFlex 755TL low harmonic drives adjusts the motoring power limits based on DC bus voltage.
- Dynamic bus control for the PowerFlex 755TM regenerative bus supply and PowerFlex 755TR regenerative drives adjusts the motoring and regeneration power limits based on the DC bus voltage.
- Dynamic bus control has 'Linear' and 'Non-linear' modes to tailor the control for different applications. There are three DC bus voltage thresholds that are used as transition points to change the converter power limits. These points are defined steps in the linear mode and a curve that is based on power limits and voltage setpoints in non-linear mode. Depending on the DC bus voltage feedback, Dynamic Bus Control selects the high or low voltage thresholds as the DC bus voltage regulator setpoints.

General setting guidelines for Dynamic Bus Control threshold voltage parameters:

- DC Bus Reference Select, parameter 13:45 [DC Bus Ref Sel] = 4 'DBC Control'
- Dynamic Bus Control Mode, parameter 13:61 [DBC Mode Sel] = 0 'Linear', 1 = 'Nonlinear'
- Low bus voltage threshold, parameter 13:62 [DBC V Thresh Lo] = 13:25 [Rated Volts] ×
- High bus voltage threshold, parameter 13:63 [DBC V Thresh Hi] = Default × 0.95 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 790V DC × 0.95 = 750V DC
- Nominal bus voltage threshold, parameter 13:64 [DBC V Thresh Nom] = Default × 0.93 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 741V DC × 0.93 = 689V DC

| Converter Rating 0:33 [VoltageClass Cfg] Default Maximum   |
|------------------------------------------------------------|
| 400/480V 0 ‘Low Voltage’ 650V DC 650V DC                   |
| 400/480V 1 ‘High Voltage’ 790V DC 790V DC                  |
| 600/690V 0 ‘Low Voltage’ 975V DC 975V DC                   |
| 600/690V 1 ‘High Voltage’ 1135V DC 1135V DC                |

| Converter Rating 0:33 [VoltageClass Cfg] Default Maximum   |
|------------------------------------------------------------|
| 400/480V 0 ‘Low Voltage’ 613.5V DC 650V DC                 |
| 400/480V 1 ‘High Voltage’ 741V DC 790V DC                  |
| 600/690V 0 ‘Low Voltage’ 920V DC 975V DC                   |
| 600/690V 1 ‘High Voltage’ 1065V DC 1135V DC                |

## Linear Mode

Select Linear Mode for applications that require a rapid transition from low power limits to maximum power limit, such as when the bus supply is used as a regenerative brake.

The setpoints for motor and regen are Low, Nominal, and High for determining the motoring or regeneration power limits.

- For motoring at or below 13:62 [DBC V Thresh Lo] bus limit, use 13:105 [Motor Power Lmt].
- For motoring above 13:62 [DBC V Thresh Lo] and up to 13:64 [DBC V Thresh Nom], use 13:330 [DBC NomMtrPwrLm].
- For motoring above 13:64 [DBC V Thresh Nom], use 13:331 [DBC IdleMtrPwrLm].
- For regeneration at or above 13:63 [DBC V Thresh Hi], use 13:104 [Regen Power Lmt].
- For regeneration from 13:63 [DBC V Thresh Hi] to 13:64 [DBC V Thresh Nom], use 13:332 [DBC NomRgnPwrLm].
- For regeneration below 13:64 [DBC V Thresh Nom], use 13:333 [DBC IdleRgnPwrLm].

The Dynamic Bus Control is most stable if the motoring and regenerative power limit parameters are not set numerically less than 5%.

The following graphic shows the Linear mode of Dynamic Bus Control. This could be used with a large DC bus capacitor bank application. With a DC bus capacitor bank, the setpoints for power would be used for both motoring and regeneration. In this example the motoring and regeneration power transfer is limited in range between DC bus voltage low and high thresholds.

- The DC bus voltage is allowed to fluctuate due to energy transfer to and from the load and the capacitor bank with minimal allowed power transfer to/from the AC line (grey filled area).
- If the DC bus voltage drops below the low threshold maximum motoring power is allowed to transfer from the AC line (blue filled area).
- If the DC bus voltage rises above the high threshold the maximum regeneration power is allowed to transfer to the AC line (yellow filled area).

## Recommended Settings:

- 13:105 [Motor Power Lmt] = 100%
- 13:330 [DBC NomMtrPwrLm] = 25%
- 13:331 [DBC IdleMtrPwrLm] = 5%
- 13:104 [Regen Power Lmt] = -100%
- 13:332 [DBC NomRgnPwrLm] = -25%
- 13:333 [DBC IdleRgnPwrLm] = -5%
- Low bus voltage threshold, parameter 13:62 [DBC V Thresh Lo] = 13:25 [Rated Volts] ×
- High bus voltage threshold, parameter 13:63 [DBC V Thresh Hi] = Default DC Bus Voltage × 0.95 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 790V DC × 0.95 = 750V DC
- Nominal bus voltage threshold, parameter 13:64 [DBC V Thresh Nom] = Default DC Bus Voltage × 0.93 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 741V DC × 0.93 = 689V DC

<!-- image -->

When a PowerFlex 755TM regenerative bus supply is paralleled with a non-regenerative bus supply converter (Diode/SCR rectifier) the regenerative bus supply Dynamic Bus Control is configured for Regen Braking using Linear Mode operation.

For a Regen Brake mode operation, you would set the motoring idle, nominal and high power limits to minimum (5%). The regenerative idle and nominal power limits would be set to -5% and the high power set to the desired regenerative brake level (-100%). The converter supports minimal motoring power in this configuration. All motoring power must be supplied by the non-regenerative bus supply converter.

## Recommended Settings:

- 13:105 [Motor Power Lmt] = 13:330 [DBC NomMtrPwrLm] = 13:331 [DBC IdleMtrPwrLm] = 5%
- 13:104 [Regen Power Lmt] = -100%
- 13:332 [DBC NomRgnPwrLm] = 13:333 [DBC IdleRgnPwrLm] = -5%
- Low bus voltage threshold, parameter 13:62 [DBC V Thresh Lo] = 13:25 [Rated Volts] × √ g
- High bus voltage threshold, parameter 13:63 [DBC V Thresh Hi] = Default DC Bus Voltage × 0.95 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 790V DC × 0.95 = 750V DC
- Nominal bus voltage threshold, parameter 13:64 [DBC V Thresh Nom] = Default DC Bus Voltage × 0.93 (Default is based on PowerFlex 755TM Voltage Class). For 480V AC, 741V DC × 0.93 = 690V DC

The following graphic shows the Dynamic Bus Control settings for Regen Brake control. In this example the regenerative bus supply motoring and regeneration power transfer is limited in range below the DC bus voltage high threshold.

- If the DC bus voltage is below the high threshold, minimum motoring and regeneration power transfer is allowed from/to from the AC line (gray filled area).
- If the DC bus voltage rises above the high threshold regeneration power is allowed to transfer to the AC line (yellow filled area).

<!-- image -->

## Non-Linear Mode

Non-linear Dynamic Bus Control is similar to linear mode except the DC bus voltage and power limit transition points are based on a curve instead of discrete switching points. Non-linear bus control provides a smoother converter AC input current during DC bus voltage reference and power limit transitions. Select non-linear mode for applications that have large external DC bus capacitor banks and controlled requirements for limiting power such as a servo press or rotary shear.

The combination of the low, nominal, and high voltage thresholds and the idle, nominal, and high motor/regen power limits shape the curve of the non-linear operation of the Dynamic Bus Control.

Below is an example of the constantly changing power limits. The curves in this example are equal but is not a requirement.

<!-- image -->

Nominal power limits and nominal voltage level parameters have the largest effect on the power curves. Changing the values can create curves as in the two curve examples that follow. The dynamic bus control is most stable if the motoring and regenerative power limit parameters are not set numerically less than 5%.

<!-- image -->

## Carrier (PWM) Frequency

Parameter 10:425 [PWM Frequency] sets the carrier frequency at which the inverter output IGBTs (insulated gate bipolar transistors) switch. In general, the lowest possible switching frequency that is acceptable for any particular application is the one to use. An increased carrier frequency causes less motor heat and lowers the audible noise from the motor. However, an increased carrier frequency does cause the IGBTs to heat up faster than by using the factory default PWM frequency of 4 kHz or 2 kHz depending on the frame size. The higher switching frequency smooths the current waveform and therefore creates less vibration in the motor windings and laminations and lower audible noise. Lower audible noise is desirable in some applications such as motors installed close to control rooms or in domestic environments. Because a higher carrier frequency creates more IGBT heating, derating is required. See Figure 68 and Figure 69. Note the output current at 2 kHz and 4 kHz. The "smoothing" of the current waveform continues up to 12 kHz. The maximum carrier frequency per frame size and the derating guidelines according to PWM frequency can be found in the product technical data.

- For PowerFlex 755T products see the PowerFlex 750-Series Products with TotalFORCE Control Technical Data, publication 750-TD100 .
- For PowerFlex 755TS products see the PowerFlex 755TS Products with TotalFORCE Control, publication 750-TD104 .

Figure 68 - Current at 2 kHz PWM Frequency

<!-- image -->

Figure 69 - Current at 4 kHz PWM Frequency

<!-- image -->

Some undesirable effects of higher switching frequencies include higher cable charging currents, higher potential for common mode noise and an increased risk of motor winding insulation breakdown due to the reflected wave phenomenon. See the Wiring and Grounding Guidelines for Pulse-width Modulated (PWM) AC Drives, publication DRIVES-IN001, for further information. Most drive applications perform adequately at 2 kHz or 4 kHz.

Some applications require a fixed minimum PWM frequency such as using a sine wave filter in the output of the drive. In this case, set parameter 10:420 [Mtr Cfg Options] bit 9 'PWM FreqLock' to keep the drive from lowering its carrier frequency due to a drive overload condition.

## Analog Inputs

Analog Inputs for the PowerFlex 755TS drive are available with user installed option modules. There are two analog inputs per I/O module. Up to four I/O modules can be mounted in the drive ports. There is also an eight input option module available from Spectrum Controls. See the PowerFlex 750-Series I/O, Feedback, and Power Option Modules Installation Instructions, publication 750-IN111, for valid ports. Accessing the analog input parameters is done by selecting the port that the module is mounted in, then accessing the Analog Input group of parameters. See the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101, for parameter descriptions.

Inputs are isolated, bipolar, differential, with 11 bit and sign resulting in 2048 steps.

- 4.88 mV resolution for 0…10v signals
- 0.0078125 mA resolution for 4…20 mA signals

Option modules provide the analog input value for use within the drive as well as performing several basic functions.

- Analog Input type selection
- Analog Input Filter
- Analog Input Loss Detection
- Analog Input Square Root function
- Analog Scaling

## Analog Input Type Selection

Analog Input type is determined based on the hardware jumper position on the option module. There is one jumper per input, and each is independently configured. The status of the jumpers can be viewed in option module parameter nn:45 [Anlg In Type].

Figure 70 - 22-Series I/O Option Module Input Mode Jumpers

<!-- image -->

## Analog Input Filter

A filter is provided for each analog input signal using parameters for filter Gain and Bandwidth(rad/s). A gain value of zero results in first order low pass filter behavior. Gain values between zero and one result in a lag type filter. A gain value of one will disable the filter. Bandwidth sets the frequency range of the filter. A value of zero will disable the filter. By default this filter is disabled and can be enabled by changing option module parameters nn:55 [Anlg In0 Filt Gn], nn:56 [Anlg In0 Filt BW], nn:65 [Anlg In1 Filt Gn], and nn:66 [Anlg In1 Filt BW].

- For a light filter use a gain of 0.7 and a bandwidth of 35
- For a heavy filter use a gain of 0.5 and a bandwidth of 20

## Analog Input Loss Detection

Signal loss detection can be enabled for each analog input. Parameter nn:47 [Anlg In Loss Sts] bits 0, 1, 2 indicate if the signal is lost. Bit 0 indicates that one or both signals are lost. Parameters nn:53 [Anlg In0 LssActn] and nn:63 [Anlg In1 LssActn] define what action the drive takes when loss of any analog input signal occurs. Signal loss is defined as an analog signal that is less than 1V or 2 mA. The signal loss event ends and normal operation resumes when the input signal level is greater than or equal to 1.5V or 3 mA.

- 'Ignore' (0) – No action is taken.
- 'Alarm' (1) – Type 1 alarm indicated.
- 'Flt Minor' (2) – Minor fault indicated. Minor faults prevent the drive from starting. They do not stop the drive, if it is already running. You must clear the fault to start or run.
- 'FltCoastStop' (3) – Major fault indicated. Coast to Stop.
- 'Flt RampStop' (4) – Major fault indicated. Ramp to Stop.
- 'Flt CL Stop' (5) – Major fault indicated. Current Limit Stop.
- 'Hold Input' (6) – Holds input at last value.
- 'Set Input Lo' (7) – Sets input to nn:52 [Anlg In0 Lo] or nn:62 [Anlg In1 Lo].
- 'Set Input Hi' (8) – Sets input to nn:51 [Anlg In0 Hi] or nn:61 [Anlg In1 Hi].

If the input is in Current mode, 4 mA is the normal minimum usable input value. Any value below 3.2 mA is interpreted by the drive as a signal loss, and a value of 3.8 mA is required on the input for the signal loss condition to end.

If the input is in Unipolar Voltage mode, 2V is the normal minimum usable input value. Any value below 1.6V is interpreted by the drive as a signal loss, and a value of 1.9V is required on the input for the signal loss condition to end. No signal loss detection is possible while an input is in Bipolar Voltage mode. The signal loss condition never occurs even if signal loss detection is enabled.

## Square Root

The square root function can be applied to each analog input through the use of nn:46[Anlg In Sqrt]. The function should be enabled if the input signal varies with the square of the quantity (e.g. drive speed) being controlled. A common example is the differential pressure flow meter, where measured differential pressure is proportional to the square of the flow. Without a square root function in the meter, the result is error between min and max flow which can be corrected by taking the square root of the signal.

If the mode of the input is bipolar voltage (-10V…+10V), then the square root function returns 0 for all negative voltages.

The function takes square root of the raw analog value as compared to its full scale as defined in the following equation. Note this function does not scale based on Anlg In Hi or Anlg In Lo, so the full range of the input is expected.

<!-- image -->

## Analog Scaling

```
[Anlg Inn Lo] [Anlg Inn Hi]
```

A scaling operation is performed on the value read from an analog input to convert it to units usable for some purpose. Control the scaling by setting parameters that associate a low and high analog value (in volts or mA) with a low and high target (in Hz).

In the following examples the option module port is denoted as nn .

## Example 1

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- 10:1802 [VRef A AnlgHi] = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In1 Hi] = 10V
- nn :62 [Anlg In1 Lo] = 0V

This is the default setting, where 0V represents 0 Hz and 10V represents 60 Hz providing 2048 steps between 0 and 60 Hz.

Example 2

<!-- image -->

Consider the following setup:

- nn:45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- nn :61 [Anlg In1 Hi] = 10V
- nn :62 [Anlg In1 Lo] = 0V
- 10:1802 [VRef A AnlgHi] = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- 10:1898 [Vel Limit Pos] = 45 Hz
- 10:1900 [Vel Low Lim Pos] = 15 Hz

<!-- image -->

In this example, a deadband from 0…2.5V and from 7.5…10V is created. Alternatively, the analog input deadband could be eliminated while maintaining the 15 and 45 Hz limits with the following changes:

- 10:1803 [VRef A AnlgLo] = 15 Hz
- 10:1802 [VRef A AnlgHi] = 45 Hz

## Example 3

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- 10:1802 [VRef A AnlgHi] = 30 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In1 Hi] = 10V
- nn :62 [Anlg In1 Lo] = 0V

This is an application that requires only 30 Hz as a maximum output frequency but is still configured for full 10V input. The result is that the resolution of the input has been doubled, providing 2048 steps between 0 and 30 Hz.

<!-- image -->

## Example 4

- nn :45 [Anlg In Type], bit 0 = 1 'Current'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- 10:1802 [VRef A AnlgHi] = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In1 Hi] = 20 mA
- nn :62 [Anlg In1 Lo] = 4 mA

This configuration is referred to as offset. In this case, a 4…20 mA input signal provides 0…60 Hz output, providing a 4 mA offset in the speed command.

<!-- image -->

## Example 5

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- 10:1802 [VRef A AnlgHi = 0 Hz
- 10:1803 [VRef A AnlgLo] = 60 Hz
- nn :61 [Anlg In1 Hi] = 10V
- nn :62 [Anlg In1 Lo] = 0V

This configuration is used to invert the operation of the input signal. Here, maximum input (10V) represents 0 Hz and minimum input (0V) represents 60 Hz.

<!-- image -->

## Example 6

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:60 [Anlg In1 Value]
- 10:1802 [VRef A AnlgHi = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In1 Hi] = 5V
- nn :62 [Anlg In1 Lo] = 0V

This configuration is used when the input signal is 0…5V. Here, minimum input (0V) represents 0 Hz and maximum input (5V) represents 60 Hz. This provides full scale operation from a 0…5V.

<!-- image -->

## Example 7

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:2000 [Trq Ref A Sel] = nn:60 [Anlg In1 Value]
- 10:2002 [Trq Ref A AnlgHi] = 200%
- 10:2003 [Trq Ref A AnlgLo] = 0%
- nn :61 [Anlg In1 Hi] = 5V
- nn :62 [Anlg In1 Lo] = 0V

This configuration is used when the input signal is 0…10V. The minimum input of 0V represents a torque reference of 0% and maximum input of 10V represents a torque reference of 200%.

<!-- image -->

## Example 8

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:50 [Anlg In0 Value]
- 10:1802 [VRef A AnlgHi] = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In0 Hi] = 10V
- nn :62 [Anlg In0 Lo] = 0V
- nn :46[Anlg In Sqrt] bit 0 = 1

This configuration is used to perform the square root function on the input signal. Here, 0V represents 0 Hz and 10V represents 60 Providing a square root action throughout the input range. Note that Anlg In Value maintains a linear relationship with Output Hz.

<!-- image -->

## Example 9

- nn :45 [Anlg In Type], bit 0 = 0 'Voltage'
- 10:1800 [VRef A Sel] = nn:50 [Anlg In0 Value]
- 10:1802 [VRef A AnlgHi] = 60 Hz
- 10:1803 [VRef A AnlgLo] = 0 Hz
- nn :61 [Anlg In0 Hi] = 5V
- nn :62 [Anlg In0 Lo] = 0V
- nn :46[Anlg In Sqrt] bit 0 = 1

This configuration is used to perform the square root function on the input signal. Here, 0V represents 0 Hz and 10V represents 120 Providing a square root action throughout the input range. Note the output Hz are limited by combination of nn:61 [Anlg In0 Hi] and 10:1802 [VRef A AnlgHi].

<!-- image -->

## Analog Outputs

There are two analog outputs per I/O module. Up to five I/O modules can be mounted in the drive ports. See the PowerFlex 750-Series I/O, Feedback, and Power Option Modules installation instructions, publication 750-IN111 for valid ports. Accessing the analog output parameters by selecting the port that the module is mounted in then accessing the Analog Output group of parameters.

<!-- image -->

Table 42 - Analog Output Specifications

|                                         | Terminal Name Description                                                                                                                                                                        | Related Param (4)   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Shield                                  | Terminating point for wire shields when an EMC plate or conduit box is not p installed. Sh                                                                                                                                                                                                  |                     |
| Ptc– Motor PTC (–)                      | Motor protection device (Positive Temperature Coefficient).                                                                                                                                      | 40 on Port X        |
| Ptc+ Motor PTC (+)                      | Motor protection device (Positive Temperature Coefficient).                                                                                                                                      | 40 on Port X        |
| Ao0– Analog Out 0 (–)                   | Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                                                | 75 on Port X        |
| Ao0+ Analog Out 0 (+)                   | Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                                                | 75 on Port X        |
| Ao1– Analog Out 1 (–)                   | Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                                                | 85 on Port X        |
| Ao1+ Analog Out 1 (+)                   | Bipolar, ±10V, 11 bit & sign, 2 k ohm minimum load. 4-20 mA, 11 bit & sign, 400 ohm maximum load.                                                                                                | 85 on Port X        |
| –10V –10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
|                                         | 10VC 10 Volt Common For (–) and (+) 10 Volt references.                                                                                                                                          |                     |
| +10V +10 Volt Reference 2k ohm minimum. |                                                                                                                                                                                                  |                     |
| Ai0– Analog Input 0 (–)                 | Isolated (2), bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. Current mode: 0-20 mA @ 93 ohm input                                                           | 50, 70              |
| Ai0+ Analog Input 0 (+)                 | Isolated (2), bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. Current mode: 0-20 mA @ 93 ohm input                                                           | on Port X           |
| Ai1– Analog Input 1 (–)                 | Isolated (2), bipolar, differential, 11 bit & sign. Voltage mode: ±10V @ 88k ohm input impedance. Current mode: 0-20 mA @ 93 ohm input                                                           | 60, 70 on Port X    |
| Ai1+ Analog Input 1 (+)                 | impedance.                                                                                                                                                                                       | 60, 70 on Port X    |
|                                         | 24VC 24 Volt Common Drive supplied logic input power. 200 mA max per I/O module p 600 mA max per drive +24V +24 Volt DC                                                                                                                                                                                                  |                     |
|                                         | Di C Digital Input Common Common for Digital Inputs 0…5                                                                                                                                          |                     |
| Di 0  Digital Input 0 (1)               | 24V DC - Opto isolated Low State: less than 5V DC High State: greater than 20V DC 11.2 mA DC 115V AC, 50/60 Hz (3)  - Opto isolated Low State: less than 30V AC High State: greater than 100V AC | 1                   |
| Di 1  Digital Input 1 (1)               |                                                                                                                                                                                                  | on Port X           |
| Di 2  Digital Input 2 (1)               |                                                                                                                                                                                                  | on Port X           |
| Di 3  Digital Input 3 (1)               |                                                                                                                                                                                                  | on Port X           |
| Di 4  Digital Input 4 (1)               |                                                                                                                                                                                                  | on Port X           |
| Di 5  Digital Input 5 (1)               |                                                                                                                                                                                                  | on Port X           |

## Analog Output Configuration

Parameters nn:75 and nn:85 [Anlg Outn Select] are use to specify the signal used on Analog Outputs 1 and 2, respectively. These parameters can be programmed to the following selections.

| Parameter No. Parameter Name   |
|--------------------------------|
| 0:3 DC Bus Volts               |
| nn:50 Anlg In0 Value           |
| nn:60 Anlg In1 Value           |
| 10:1 Output Frequency          |
| 10:2 Output Voltage            |
| 10:3 Output Current            |
| 10:4 Output Power              |
| 10:5 Output Pwr Factr          |
| 10:8 Torque Cur Fb             |
| 10:9 Flux Cur Fb               |
| 10:207 Mtr OL Counts           |
| 10:208 Mtr OL Trip Time        |
| 10:357 Drive OL Count          |
| 10:362 Heatsnk Temp Pct        |
| 10:1044 Motor Vel Fb           |
| 10:1834 Enc VRef               |
| 10:1914 VRef Commanded         |
| 10:2036 LdObs Torque Est       |
| 10:2057 FrctnComp Out          |
| 10:2073 Trq Commanded          |

## Scaling

The scaling for the analog output is defined by entering analog output voltages into two parameters, nn:91 [Anlg Out1 Lo] and nn:90 [Anlg Out1 Hi]. These two output voltages correspond to the bottom and top of the possible range covered by the quantity being output. Scaling of the analog outputs is accomplished with low and high analog parameter settings that are associated with fixed ranges for each target function (see the PowerFlex Drives with TotalFORCE Control Programming Manual, publication 750-PM101). Additionally, PowerFlex 755T products contain an adjustable scale factor to override the fixed target range. Parameter nn :77 [Anlg Out0 Data] and nn:82 [Anlg Out0 Val] are described in the following charts.

## Case 1…4

Case 1: This shows nn:77 [Anlg Out0 Data] the units are consistent with the selection of nn:75 [Anlg Out0 Sel]. In this case, the analog out select is set to 10:1044 [Motor Vel Fb] and the units are in rpm. Parameter nn:80 [Anlg Out0 Hi], nn:81 [Anlg Out0 Lo], nn:78 [Anlg Out0 DataHi], and nn :79 [Anlg Out0 DataLo] are all at default. The motor was started and ramped to 1800 rpm. Note that nn:82 [Anlg Out0 Val] remained zero.

<!-- image -->

Case 2: Here the nn:80 [Anlg Out0 Hi] is changed to 9 and nn:81 [Anlg Out0 Lo] is changed to 1. As the motor ramps up and down, there is no change in the value or scaling of nn:77 [Anlg Out0 Data]. Note that nn:82 [Anlg Out0 Val] is still zero.

Case 3: Now nn:78 [Anlg Out0 DataHi] is changed to 1800 and nn:79 [Anlg Out0 DataLo] is left at zero. When started, nn:82 [Anlg Out0 Val] starts at 1 and reaches 9 when the motor speed is at maximum.

Case 4: In this section the nn:80 [Anlg Out0 Hi] and nn:81 [Anlg Out0 Lo] were reversed in value. Now when the motor ramps up and down nn:82 [Anlg Out0 Val] is just the opposite. It starts out at 9 and is at 1 at full speed.

## Case 5

<!-- image -->

## Case 6

<!-- image -->

## Absolute (Default)

Certain quantities used to drive the analog output are signed, for example the quantity can be both positive and negative. You have the option of having the absolute value (value without sign) of these quantities taken before the scaling occurs. Absolute value is enabled separately for each analog output via the bit enumerated nn:71 [Analog Out Abs].

## Setpoint

Setpoint is a possible source for an analog output. It can be used to control an analog output from a communication device using a DataLink. For Analog Out 0, change nn:75 [Anlg Out0 Sel] to nn:76 [Anlg Out0 Stpt]. Then map a datalink to nn:76 [Anlg Out0 Stpt] and you'll be able to drive the analog output over a network. To configure Analog Out 1 to use a setpoint, change nn :85[Anlg Out1 Sel] to nn:86 [Anlg Out1 Stpt] and map a datalink to nn:86 [Anlg Out1 Stpt].

## Digital Inputs

Physical inputs are programmed to desired digital input functions. These parameters cannot be changed while the drive is running.

## Technical Information

The PowerFlex 755T drive has one digital input on its main control board:

- Di0 - configured for 115V AC or 24V DC
- Shared common (Di C) between Di 0ac and Di 0dc terminals
- TB1 - bottom of the main control board

There are also PowerFlex 750-Series option modules that expand the amount of digital inputs that can be used.

## 20-750-2262C-2R / 20-750-2263C-1R2T

- Six 24V DC input terminals:
- Labeled as Di 0, Di 1, Di 2, Di 3, Di 4, and Di 5
- Shared common (Di C)
- TB1 - front of the option module

## 20-750-2262D-2R

- Six 115V AC input terminals:
- Labeled as Di 0, Di 1, Di 2, Di 3, Di 4, and Di 5
- Shared common terminal (Di C)
- TB1 - front of the option module

PowerFlex 750-Series Option Modules I/O TB1 wiring examples are included in the PowerFlex 750-Series I/O, Feedback, and Power Option Modules Installation Instructions, publication 750-IN111 .

## Configuration

Digital inputs can be programmed to a desired function defined by the parameters in the following table. These parameters cannot be changed while the drive is running.

| Number Parameter Name Number Parameter Name Number Parameter Name    |                                                                     |                                                             |
|----------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
|                                                                      |                                                                     | 0:103 DI M Enable 0:151 DI M MOP Inc 0:853 DI Abort Profile |
| DI L Enable (1)                                                      | 0:105                                                               | 0:152 DI M MOP Dec 0:854 DI Del Override                    |
|                                                                      | 0:108 DI M Stop 0:160 DI M SpTqPs Sel0 0:855 DI StrtStep Sel0       |                                                             |
| 0:109 DI M Stop Mode B 0:161 DI M SpTqPs Sel1 0:856 DI StrtStep Sel1 |                                                                     |                                                             |
|                                                                      | 0:110 DI M CurLmt Stop 0:163 DI M BusRegMode 0:857 DI StrtStep Sel2 |                                                             |
|                                                                      | 0:111 DI M Coast Stop 0:164 DI M PwrLossMode 0:858 DI StrtStep Sel3 |                                                             |
| DI L Stop (1)                                                        | 0:112                                                               | 0:166 DI M Pwr Loss 0:859 DI StrtStep Sel4                  |
|                                                                      | 0:114 DI Clear Fault 0:167 DI M TorqueStptA 0:860 DI Step 1         |                                                             |
|                                                                      | 0:115 DI Aux Fault 0:169 DI Mtr Ctrl Sel 0:861 DI Step 2            |                                                             |
| DI Regen OK (1)                                                      | 0:116  0:170 DI Find Home 0:862 DI Step 3                           |                                                             |
|                                                                      | 0:117 DI M Start 0:171 DI Return Home 0:863 DI Step 4               |                                                             |
|                                                                      | 0:118 DI M HOA Start 0:172 DI Redefine Psn 0:864 DI Step 5          |                                                             |
| DI L Start (1)                                                       | 0:119  0:173 DI OL Home Limit 0:865 DI Step 6                       |                                                             |
|                                                                      | 0:120 DI M Run 0:176 DI Indx Step 0:866 DI Step 7                   |                                                             |
| DI L Run (1)                                                         | 0:123  0:177 DI Indx StepRev 0:867 DI Step 8                        |                                                             |
|                                                                      | 0:124 DI M Jog 1 0:178 DI Indx StepPrst 0:868 DI Step 9             |                                                             |
|                                                                      | 0:127 DI M Jog 2 0:180 DI FwdEndLimit 0:869 DI Step 10              |                                                             |
| 0:130 DI M Fwd Reverse 0:181 DI FwdDecLimit 0:870 DI Step 11         |                                                                     |                                                             |
| 0:132 DI M Manual Ctrl 0:182 DI RevEndLimit 0:871 DI Step 12         |                                                                     |                                                             |

| Number Parameter Name Number Parameter Name Number Parameter Name   |
|---------------------------------------------------------------------|
| 0:134 DI EmergencyOVRD 0:183 DI RevDecLimit 0:872 DI Step 13        |
| 0:135 DI Energy Pause 0:184 DI PHw OvrTrvl 0:873 DI Step 14         |
| 0:140 DI M Speed Sel 0 0:185 DI NHw OvrTrvl 0:874 DI Step 15        |
| 0:141 DI M Speed Sel 1 0:190 DI Precharge 0:875 DI Step 16          |
| 0:142 DI M Speed Sel 2 0:191 DI Prchrg Seal 0:880 DI PCAM Start     |
| 0:144 DI M Accel Time 0:851 DI Hold Step 0:883 DI VCAM Start        |
| 0:145 DI M Decel Time 0:852 DI Abort Step 0:886 DI TqCAM Start      |

Operation for DI Run type parameters can be defined by 0:101 [Digital In Cfg]:

- 'Run Edge' (0) – Control function requires a rising edge (open to close transition) for the drive to run.
- 'Run Level' (1) – As long as a separate "Stop" command is not issued, the level alone (no rising edge required) determines whether the drive runs. When set to 1 'Run Level' the absence of a run command is indicated as a stop asserted and 10:354 [Motor Side Sts 1] bit 0 is low.

<!-- image -->

ATTENTION: Equipment damage and/or personal injury may result if this parameter is used in an inappropriate application. Do not use this function without considering applicable local, national and international codes, standards, regulations, or industry guidelines.

## Functional Descriptions

## DI M Enable

Closing this input lets the drive run when a Start command is issued. If the drive is already running when this input is opened, the drive will coast stop and indicate 'not enabled' on the HIM (if present). This is not considered a fault condition, and no fault is generated. If this function is not configured, the drive is considered enabled.

| IMPORTANT   | If the ENABLE Jumper on the main control board is removed, the Di 0 becomes a hardware enable. Di 0 is found on TB1 on the main control board.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|

A combination of the hardware enable and a software enable can be utilized; however, the drive will not run if any of the inputs are open.

## DI L Enable

Closing this input allows the line side converter to modulate when a Start command is issued. If it opens or resets while it is modulating, the line side converter ceases modulating.

## DI M Stop

An open input causes the drive to stop and become Not Ready. A closed input lets the drive run when given a Start or Run command.

## DI M Stop Mode B

This input is used to select which Stop mode is used when stop command is issued. If the input is open or de-energized, the drive uses the stop mode configured by parameter 10:110 [Mtr Stop Mode A]. If the input is closed or energized, the drive uses the stop mode configured by parameter 10:111 [Mtr Stop Mode B].

## DI M CurLmt Stop

With this digital input function, an open input causes the drive to current limit stop. The drive acknowledges the stop command by setting the motor speed reference to zero, causing the drive to bring the motor down to zero speed as fast as the power limits, torque limits, and current limits allow. When the drive output reaches zero, the output transistors are shut off.

## DI M Coast Stop

With this digital input function, an open input causes the drive to Coast-to-Stop. The drive acknowledges the stop command by shutting off the output transistors and releasing control of the motor. The load/motor will coast or free spin until the mechanical energy is dissipated.

## DI L Stop

An open input causes the converter to stop modulating. A closed input lets the converter modulate when given a Start or Run command.

## DI Clear Fault

The Clear Fault digital input function lets an external device reset drive faults through the terminal block. An open to closed transition on this input causes an active fault (if any) to be reset.

## DI Aux Fault

This input function is normally closed and lets external equipment fault the drive. When this input opens, the drive faults on a code 1 'Auxiliary Input' and stops modulating. The motor will coast to a stop. If this input function is not configured, the fault will not occur.

## DI Regen OK

This input only applies to common bus inverters. It is used to let the inverter know when there is a fault on the bus supply. When the input is open or reset, the fault prevents the drive from starting or running until it is cleared. If the input opens or resets while the drive is running, the drive faults on code 72 'Digin Regen Fail' and stops modulating. The motor will coast to a stop.

## DI M Start

An open to closed transition while the drive is stopped causes the drive to run in the current direction, unless the Stop input function is open. If Start is configured, then a Stop must also be configured or the drive fault with code 171 'No Stop Source'. The Stop does not have to be a digital input. The drive counts the HMI and active network connections as a stop source.

## DI M HOA Start

This digital input function provides Hand-Off-Auto control. It functions like a three-wire start signal; with the exception, that it does not require the DI Stop to be high for a full input cycle before the drive looks for a rising edge on DI HOA Start.

## DI L Start

An open to closed transition while the converter is stopped causes the converter to start modulating. If it goes low after the line side converter is modulating, the line side converter continues to run until it receives a Stop command.

## DI M Run

This digital input runs the drive when closed or energized. If the drive is running, opening or de-energizing the input will stop the drive. This input does not prevent starting the drive if open or de-energized.

## DI L Run

This digital input modulates the converter when closed or energized. If the converter is modulating, opening or de-energizing the input will stop the converter. This input does not prevent starting the converter if open or de-energized.

## DI M Jog 1, DI M Jog 2

Jog is a non-latched command similar to Run, but overrides the normal speed reference and uses 10:1894 [Jog Speed 1] or 10:1895 [Jog Speed 2] respectively. An open to closed transition while the drive is stopped causes the drive to jog unless the Stop input function is configured and open. Direction is determined by another input or another device's command (HIM or communication adapter). In Unipolar mode, the absolute value is used along with a separate direction command. In Bipolar mode, the polarity of 10:1894 [Jog Speed 1] or 10:1895 [Jog Speed 2] determines the direction of jog.

## DI M Fwd Reverse

This digital input function is one of the ways to provide direction control when the Start or Run functions (not combined with direction) are used. An open input sets direction to forward. A closed input sets direction to reverse. If state of input changes and drive is running or jogging, the drive changes direction.

## DI M Manual Ctrl

The digital input function works in conjunction with the overall Auto/Manual function. When this input is closed, it overrides other speed references, but only if another device (HIM) did not have ownership of the Manual state. If the digital input is successful in gaining manual control, the speed reference comes from 0:147 [DI ManRef Sel], which can be set to any of the Analog Inputs, Preset Speeds, MOP Reference, or an applicable Port Reference.

Associated with this digital input function, there is the ability to configure the drive to switch smoothly from an automatic (communicated) speed reference to manual speed reference produced by the Human Interface Module (HIM).

When the drive is commanded to switch from the automatic (communicated) speed reference to the manual reference via a digital input, it preloads the last value from the speed feedback into the HIM. Then the operator can modify the manual reference on the HIM. This avoids a step change in speed that otherwise occurs from the switch. Use this feature by configuring 10:1835 [Alt Man Ref Sel], 0:52 [Manual Preload], 0:132 [DI M Manual Ctrl], and 0:147 [DI ManRef Sel].

This feature requires revision 2.001 of 20-HIM-A6 firmware or later.

## DI EmergencyOVRD

This digital input is used to enable and disable the Emergency Override Function. When the input is closed or energized, Emergency Override is enabled. For information about the Emergency Override Function, Emergency Override Function on page 94 .

## DI Energy Pause

This digital input is used to send the product to and from the Paused (low energy) state. When the input is closed or energized, device will transition to the Paused state. For information about Energy Pause, see Energy Pause Function on page 63 .

## DI AC LineSource

This digital input is used to switch between two AC line sources that have different power and impedance values. When the input is open or de-energized, the Line Side Converter uses parameters 13:32 [AC Line kVA A] and 13:34 [AC Line Imped% A]. When the input is closed or energized, the Line Side Converter uses parameters 13:33 [AC Line kVA B] and 13:35 [AC Line Imped% B]. When this digital input is configured, the product ignores parameter 13:31 [AC Line Source].

## DI M Speed Sel 0, 1, and 2

These digital input functions can be used to select the speed reference. The open/ closed state of all the speed select digital input functions combine to select which source is the speed reference.

| DI Speed Sel 2 DI Speed Sel 1 DI Speed Sel 0 Reference Source (Parameter)   |
|-----------------------------------------------------------------------------|
| 0 0 0 Reference A: 10:1800 [VRef A Sel]                                     |
| 0 0 1 Reference A: 10:1800 [VRef A Sel]                                     |
| 0 1 0 Reference B: 10:1807 [VRef B Sel]                                     |
| 0 1 1 Preset Speed 3: 10:1816 [Preset Speed 3]                              |
| 1 0 0 Preset Speed 4: 10:1817 [Preset Speed 4]                              |
| 1 0 1 Preset Speed 5: 10:1818 [Preset Speed 5]                              |
| 1 1 0 Preset Speed 6: 10:1819 [Preset Speed 6]                              |
| 1 1 1 Preset Speed 7: 10:1820 [Preset Speed 7]                              |

## DI M Accel Time, DI M Decel Time

These digital input functions toggle between primary and secondary ramp rates. For example, with a digital input programmed to 0:144 [DI M Accel Time], an open digital input follows 10:1915 [VRef Accel Time1]. A closed digital input follows 10:1916 [VRef Accel Time2].

## DI M MOP Inc, DI M MOP Dec

These digital input functions are used to increment and decrement the Motor Operated Potentiometer (MOP) value inside the drive. The MOP is a reference value that can be incremented and decremented by external devices. The MOP value has a configurable preload that is retained through a power cycle. For the drive to use the MOP value as the current speed reference, either 10:1800 [VRef A Sel], 10:1807 [VRef B Sel], or 0:147 [DI ManRef Sel] must be set to 10:1823 [MOP Reference].

## DI M SpTqPs Sel0 and 1

These digital input functions provide the ability to switch between different Speed/Torque/ Position modes, (10:30 [PsnVelTrq Mode A], 10:31 [PsnVelTrq Mode B], 10:32 [PsnVelTrq Mode C], and 10:33 [PsnVelTrq Mode D]) from digital input combinations.

| Input Status (1 = Input Actuated)   | Speed-Torque-Position        |
|-------------------------------------|------------------------------|
| DI M SpTqPs Sel1 DI M SpTqPs Sel0   |                              |
|                                     | 0 0 10:30 [PsnVelTrq Mode A] |
|                                     | 0 1 10:31 [PsnVelTrq Mode B] |
|                                     | 1 0 10:32 [PsnVelTrq Mode C] |
|                                     | 1 1 10:33 [PsnVelTrq Mode D] |

## DI M BusRegMode

This digital input function selects how the drive regulates excess voltage on the DC bus. If the input is open, then 10:116 [Bus Reg Mode A] selects which bus regulation mode to use. If the input is closed, then 10:117 [Bus Reg Mode B] selects which bus regulation mode to use. If this input function is not configured, then 10:116 [Bus Reg Mode A] always selects which bus regulation mode to use.

## DI M PwrLossMode

This digital input function selects between two different drive power loss modes. If the input is open, 10:271 [Pwr Loss Mode A] dictates the drive's action during the Power Loss mode. If the input is closed, 10:275 [Pwr Loss Mode B] dictates the drive's action during the power loss. If this input function is not configured, 10:271 [Power Loss Mode A] always dictates the drive's action during the power loss.

## DI M Pwr Loss

The drive contains a sophisticated algorithm to manage initial application of power as well as recovery from a partial power loss event. This digital input function is used to force the drive into a power loss condition. If this input is open, the drive's internal algorithm dictates the power loss condition. If the input is closed, the algorithm is overridden and the drive is externally forced into a power lost condition. Parameter 10:270 [Power Loss Actn] configures the drive's response to a power loss time out condition and 10:273 [Pwr Loss A Time] or 10:277 [Pwr Loss B Time] set the time that the drive remains in Power Loss mode before a fault occurs. 10:272 [Pwr Loss A Level] or 10:276 [Pwr Loss B Level] are used to calculate the power loss threshold.

## DI M TorqueStptA

This digital input function is used to force 10:2001 [Trq Ref A Stpt] as the source for Torque Reference A, regardless of the setting in 10:2000 [Trq Ref A Sel]. Used when the drive is in a mode that is commanding torque. Refer to 10:30 [PsnVelTrq Mode A], 10:31 [PsnVelTrq Mode B], 10:32 [PsnVelTrq Mode C], and 10:33 [PsnVelTrq Mode D].

## DI Mtr Ctrl Sel

This digital input function selects between Primary and Secondary motor control. If the input is open or de-energized, the drive selects the Primary motor type and motor control mode. If the input is closed or energized, the drive selects the Secondary motor type and motor control mode. If there is a conflict between this input and 0:67 [Motor Ctrl Sel], the drive uses the digital input. Parameter 0:65 [Pri MtrCtrl Mode] determines the Primary motor control type and

mode, 0:66 [Sec MtrCtrl Mode] determines the Secondary motor control type and mode, and 0:75 [Mtr Ctrl Sel Act] shows the active motor control.

## DI Find Home

This digital input function starts the Find Home function. Closing or energizing the input initiates the Find Home function. If the drive is not running, a start command is needed after this input goes high, to execute the Find Home function. If this input is configured, it will take the place of parameter 10:1640 [Home Ctrl Opts] bit 0 'Find Home'.

## DI Return Home

This digital input function activates the Return Home function. losing or energizing the input initiates the Return Home function. f the drive is not running, a start command is needed after this input goes high, to execute the Return Home function. f this input is configured, it will take the place of parameter 10:1640 [Home Ctrl Opts] bit 3 'Return Home'.

## DI Redefine Psn

This digital input function starts the Redefine Position function. Closing or energizing the input initiates the Redefine Position function. If the drive is not running, a start command is needed after this input goes high, to execute the Redefine Position function. If this input is configured, it will take the place of parameter 10:1640 [Home Ctrl Opts] bit 4 'Psn Redefine'.

## DI OL Home Limit

This digital input function is used to connect a home limit switch. The polarity of the Open Loop Home Limit function is configured by parameter 10:1640 [Home Ctrl Opts] bit 6 'Home DI Inv'.

## DI Indx Step

This digital input function starts the Index Position Move function. Closing or energizing the input initiates the Index Move. This digital input will be equivalent to setting parameter 10:1381 [PTP Control] bit 1 'Move' when the point-to-point mode 10:1382 [PTP Mode] is set to 0 'Absolute' or 1 'Index'.

## DI Indx StepRev

This digital input function starts the Index Position Reverse Move function. Closing or energizing the input initiates the Reverse Index Move. This digital input will be equivalent to setting parameter 10:1381 [PTP Control] bit 2 'Reverse Move' when the point-to-point mode 10:1382 [PTP Mode] is set to 1 'Index'.

## DI Indx StepPrst

This digital input function starts the Index Preset Position Move function. Closing or energizing the input initiates the Index Preset Move. This digital input will be equivalent to setting parameter 10:1381 [PTP Control] bit 3 'Preset Psn' when the point-to-point mode 10:1382 [PTP Mode] is set to 1 'Index'.

## DI FwdEndLimit, DI RevEndLimit

These digital input functions are used to trigger a Forward End Limit and/or a Reverse End Limit. The resulting action depends on whether the drive is operating as a speed, torque or position regulator. The mode of operation is indicated by 10:354 [Motor Side Sts 1] bit 21 'Speed Mode', bit 22 'PositionMode', and bit 23 'Torque Mode'. When the drive is operating as a speed regulator, the resulting action is to execute a 'Fast Stop' command. After the drive stops in this case, it only restarts in the opposite direction (if given a new start command). This function is usually used with a limit switch near the point where the drive needs to stop.

When the drive is operating as a torque regulator, the resulting action is to execute a 'Fast Stop' command. After the drive stops in this case, it restarts and continues operation (if given a new start command).

When the drive is operating as a position regulator, the resulting action is to execute a 'Fast Stop' command. After the drive stops in this case, it restarts and continues to move towards the position reference (if given a new start command).

## DI FwdDecLimit, DI RevDecLimit

These digital input functions are used to trigger a Forward Decel Limit and/or a Reverse Decel Limit. The resulting action depends on whether the drive is operating as a speed, torque or position regulator. The mode of operation is indicated by 10:354 [Motor Side Sts 1] bit 21 'Speed Mode', bit 22 'PositionMode', and bit 23 'Torque Mode'. When the drive is operating as a speed regulator, the resulting action is to override the speed reference and decelerate to 10:1814 [Preset Speed 1]. This function is usually used with a limit switch and initiates the slowing down process prior to encountering the End Limit.

When the drive is operating as a torque regulator, the drive ignores this signal and continues operating at its torque reference.

When the drive is operating as a position regulator, the drive ignores this signal and continues moving towards its position reference.

## DI PHw OvrTrvl, DI NHw OvrTrvl

These digital input functions are used to trigger a Positive Hardware Over-travel and/or a Negative Hardware Over-travel. The resulting action is to immediately fault and produce zero torque. After the drive is stopped, the condition needs to be cleared and the fault needs to be reset. The drive restarts (if given a new start command), and continues operation. It follows any speed reference, position reference, or torque reference. The drive's direction is not modified or limited after the restart. This function is usually used with a limit switch in a position beyond the 'End Limit', as an extra safety limit to prevent torque from damaging the machine in an over-travel situation.

## DI Precharge

This digital input function is used to manage disconnection from a common DC bus. If the input is closed, this indicates that the drive is connected to common DC bus and normal precharge handling can occur, and that the drive can run (start permissive). If the physical input is open, this indicates that the drive is disconnected from the common DC bus, and the drive enters the precharge state and initiates a coast stop immediately to prepare for reconnection to the bus. If this input function is not configured, then the drive assumes that it is always connected to the DC bus, and no special precharge handling is done.

## DI Prchrg Seal

This digital input function is used to force a unique fault when an external precharge circuit opens. 0:39 [Prchrg Err Cfg] dictates the action taken when an external precharge circuit has opened.

## DI Hold Step

This digital input function sets a digital input port for the hold step in profile/indexer control logic. The digital input that this parameter assigns is equivalent to 10:1202 [Profile Command] bit 8 'Hold Step'. Parameter 0:850 [Prof DI Invert] bit 0 'Hold Step' defines the polarity of the active state.

## DI Abort Step

This digital input function sets a digital input port for the abort profile in profile/indexer control logic. 0:850 [Prof DI Invert] bit 1 'Abort Step' defines the polarity of the active state.

## DI Abort Profile

This digital input function sets a digital input port for the hold step in profile/indexer control logic. 0:850 [Prof DI Invert] bit 2 'AbortProfile' defines the polarity of the active state.

## DI Vel Override

This digital input function sets a digital input port for the velocity override in profile/indexer control logic. The digital input this parameter assigns is equivalent to 10:1202 [Profile Command] bit 9 'Vel Override'. 0:850 [Prof DI Invert] bit 3 'Vel Override' defines the polarity of the active state.

## DI StrtStep Sel0 thru Sel4

This digital input function sets digital input ports for the start step in profile/indexer control logic. The digital inputs that these parameters assign are equivalent to the corresponding bit

in 10:1202 [Profile Command]. 0:850 [Prof DI Invert] bit 4 'StrStepSel0' to bit 8 'StrStepSel4' define the polarities of the active state.

## DI Step 1 thru 16

This digital input function sets digital input source for the corresponding step in profile/ indexer control logic. The input is only required if the index step is configured as one of the following:

1. [Type] Position Absolute [Action] Wait DigIn
2. [Type] Position Incremental [Action] Wait DigIn
3. [Type] Speed Profile [Action] DigIn Blend
4. [Type] Speed Profile [Action] Wait DigIn

0:850 [Prof DI Invert] bit 9 'Step 1' to bit 24 'Step 16' define the polarities of the active state.

## DI PCAM Start

This digital input function starts the CAM in the position reference planner. Closing or energizing the input starts the CAM sequence but not the drive. A separate run command is required to start the drive.

## DI VCAM Start

This digital input function starts the CAM in the velocity reference planner. Closing or energizing the input starts the CAM sequence but not the drive. A separate run command is required to start the drive.

## DI TqCAM Start

This digital input function starts the CAM in the torque reference planner. Closing or energizing the input starts the CAM sequence but not the drive. A separate run command is required to start the drive.

## Status

For the PowerFlex 755T main control board Digital Inputs (Di) 0, 0:100 [Digital In Sts] Bit 0 represents its respective digital input status. For the PowerFlex 750-Series Option Module Digital Inputs (Di) 0, 1, 2, 3, 4, and 5, nn:1 [Dig In Sts] Bits 0, 1, 2, 3, 4, and 5 represents its respective digital input status. When the bit associated with the digital input is on, depicted by a 1, this means that the drive recognizes that the digital input is on. When the bit associated with the digital input is off, represented by a 0, this means that the drive recognizes that the digital input is off.

## Configuration Conflicts

If you configure the digital inputs so that one or more selections conflict with each other, one of the digital input configuration alarms is asserted. As long as the Digital Input Conflict exists, the drive will not start. These alarms are automatically cleared by the drive as soon as the parameters are changed to remove the conflicts. These are examples of configurations that cause an alarm:

- Configuring both the 'Start' input function and the 'Run Forward' input function at the same time. 'Start' is used only in '3-wire' Start mode, and 'Run Forward' is used only in '2wire' Run mode, therefore, do not configure at the same time.
- Configuring the same toggle input function (for instance 'Fwd Reverse') to more than one physical digital input simultaneously.

These alarms, called Type 2 Alarms, are different from other alarms in that it is not possible to start the drive while the alarm is active. It is not possible for any of these alarms to occur while the drive is running, because all digital input configuration parameters can only be changed while the drive is stopped.

Whenever one or more of these alarms is present, the drive ready status becomes 'not ready' and the HIM displays a conflict message. In addition, the drive status light flashes yellow. See the PowerFlex Drives with TotalFORCE Control Conditions Reference Data, publication 750-RD102 for a complete list of Faults and Alarms.

## DigIn Cfg B

Digital input conflict. Input functions that cannot exist at the same time have been selected. Correct Digital Input configuration.

## DigIn Cfg C

Digital input conflict. Input functions that cannot be assigned to the same digital input have been selected. Correct Digital Input configuration.

## Block Diagrams

Figure 71 - PowerFlex 755T

<!-- image -->

Figure 72 - PowerFlex 750-Series Option Module

<!-- image -->

## Digital Outputs

The PowerFlex 755T drive has no outputs embedded on its main control board.

There are PowerFlex 750-Series Option Modules that expand the amount of digital outputs that can be used.

Catalog numbers 20-750-2262C-2R and 20-750-2262D-2R provide two relay outputs on TB2 at the front of the option module.

|                            | Terminal Name Description Rating                       |                                                                 |
|----------------------------|--------------------------------------------------------|-----------------------------------------------------------------|
| R0NC Relay 0 N.C.          | Output Relay 0 normally closed contact                 | 240V AC, 24V DC, 2A max Resistive Only                          |
|                            | R0C Relay 0 Common Output Relay 0 common               | 240V AC, 24V DC, 2A max Resistive Only                          |
| R0NO Relay 0 N.O.          | Output Relay 0 normally open contact                   | 240V AC, 24V DC, 2A max General Purpose (Inductive) / Resistive |
| R1NC Relay 1 N.C.          | Output Relay 1 normally closed contact                 | 240V AC, 24V DC, 2A max Resistive Only                          |
| R1C  Relay 1 Common Output | Relay 1 common                                         | 240V AC, 24V DC, 2A max Resistive Only                          |
|                            | R1NO Relay 1 N.C. Output Relay 1 normally open contact | 240V AC, 24V DC, 2A max General Purpose (Inductive) / Resistive |

Catalog number 20-750-2263C-1R2T provides one relay output and two transistor outputs on TB2 at the front of the option module.

|                                        | Terminal Name Description Rating       |                                                                  |
|----------------------------------------|----------------------------------------|------------------------------------------------------------------|
| R0NC Relay 0 N.C.                      | Output Relay 0 normally closed contact | 240V AC, 24V DC, 2A max Resistive Only                           |
| R0C  Relay 0 Common Output             | Relay 0 common                         | 240V AC, 24V DC, 2A max Resistive Only                           |
| R0NO Relay 0 N.O.                      | Output Relay 0 normally open contact   | 240V AC, 24V DC, 2A max General Purpose (Inductive) / Resistive  |
| T0 Transitor Output 0 Transitor Output |                                        | 24V DC = 1A max 24V DC = 0.4 Max for U.L. applications           |
| Transitor Output Common                | Resistive TC Transitor Output Common Transitor Output Common Transitor Output Common                                        | 24V DC = 1A max 24V DC = 0.4 Max for U.L. applications           |
| T1 Transitor Output 0 Transitor Output |                                        | 24V DC = 1A max 24V DC = 0.4 Max for U.L. applications Resistive |

See the PowerFlex 750-Series I/O, Feedback, and Power Option Modules Installation Instructions, publication 750-IN111 for PowerFlex 750-Series Option Module I/O wiring examples.

## Configuration

Each digital output can be programmed to change state based on one of many different conditions. These conditions can fall into different categories.

- Drive status conditions (fault, alarm, and reverse).
- Level conditions (DC bus voltage, current, and frequency)
- Controlled by a digital input.
- Controlled by the network.
- Controlled by DeviceLogix software.

## Drive Status Conditions

For PowerFlex 750-Series drives utilizing an option module, the table below shows an overview of the selectable configurations for the drive's digital output selection parameters.

| Parameter No. Parameter Name Description   |                                                                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|                                            | 0:59 Energy Status Status of the Energy Pause Function.                                                                                     |
| 0:100 Digital In Sts                       | Status of the digital inputs resident on the main control board (Port 0).                                                                   |
|                                            | 0:456 EmergMode Status Status of the Emergency Override Function                                                                            |
| nn:1 (1)                                   | Dig In Sts Status of the option module digital inputs.                                                                                      |
| nn:7 (1)  Dig Out Setpoint                 | Controls Relay or Transistor Outputs when chosen as the source. Can be used to control outputs from a communication device using DataLinks. |
| nn:13 (1)  RO0 Level CmpSts                | Status of the level compare, and a possible source for a relay or transistor output.                                                        |
| 9:1100… 9:1103 (2) DLX Bool SP1- SP4       | Provides the individual on/off status of the DLX Boolean scratchpad 1…4 memory locations. Each scratchpad location contains 32 bits.        |
| 10:351 M Start Inhibits                    | Indicates which condition is preventing the inverter from starting or running. (examples Faulted, Alarm, Enable, and so on)                 |
|                                            | 10:354 Motor Side Sts 1 Present operating condition of the inverter.                                                                        |
|                                            | 10:355 Motor Side Sts 2 Present operating condition of the inverter.                                                                        |
| 10:365 At Limit Status                     | Status of dynamic conditions within the drive that are either active or a limit is being applied.                                           |
| 10:460 Condition Sts A                     | Status of conditions that can result in the drive taking action (faulting), based on configuration of protective functions.                 |
| 10:10:461 Fault Status A                   | Indicates the occurrence of conditions that have been configured as faults. These conditions are from 10:460 [Condition Sts A].             |
| 10:462 Fault Status B                      | Indicates the occurrence of conditions that have been configured as faults.                                                                 |
| 10:465 Alarm Status A                      | Indicates the occurrence of conditions that have been configured as alarms. These events are from 10:460 [Condition Sts A].                 |
| 10:466 Alarm Status B                      | Indicates the occurrence of conditions that have been configured as alarms.                                                                 |
| 10:467 Type 2 Alarms                       | Indicates the occurrence of conditions that have been configured as alarms.                                                                 |
| 10:469 AlarmB at Fault                     | Indicates the occurrence of conditions that have been configured as alarms that were present at the time of a fault.                        |
| 10:1380 PTP Pref Status                    | Displays the current operating status of the point-to-point Position Planner in the Position Referencing.                                   |
|                                            | 10:1641 Home Status Indicates status of position control logic home function.                                                               |
|                                            | 10:1732 PReg Status Indicates status of position control logic.                                                                             |
| 13:225 (3)                                 | Line Side Sts 1 Present operating condition of the converter.                                                                               |
| 13:226 (3)  At Limit Status                | Status of dynamic conditions within the converter that are either active or a limit is being applied.                                       |
| 13:235 (3)  L Start Inhibits               | Indicates which condition is preventing the converter from starting or running. (examples Faulted, Alarm, Enable, and so on)                |
| 13:240 (3)  Fault Status A                 | Indicates the occurrence of conditions that have been configured as converter faults.                                                       |
| 13:241 (3)  Fault Status B                 | Indicates the occurrence of conditions that have been configured as converter faults.                                                       |
| 13:258 (3)  Alarm Status A                 | Indicates the occurrence of conditions that have been configured as converter alarms.                                                       |
| 13:259 (3)  Alarm Status B                 | Indicates the occurrence of conditions that have been configured as converter alarms.                                                       |

See the PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101 for specific parameter bit level details.

Depending on the PowerFlex 750-Series Option Module or Modules installed in the drive, related selection parameter information is noted in the following table.

| Parameter No. Parameter Name Description                                                    |
|---------------------------------------------------------------------------------------------|
| nn:10 RO0 Sel Selects the source that energizes the relay output.                           |
| nn:20 RO1 Sel or TO0 Sel  Selects the source that energizes the relay or transistor output. |
| nn:30 TO1 Sel Selects the source that energizes the transistor output.                      |

## Example

To configure RO0 on the option module located in port 7 to energize when a fault is present on the drive, set parameter 7:10 [RO0 Sel] to 10:354 [Motor Side Sts 1], bit 7 'Faulted'.

## Level Conditions

A desired level function needs to be programmed into the 'Level Sel' parameter, depending on the output being used. If the value for the specified function (frequency, current, and so forth) is greater than equal to or less than the programmed limit dictated by the 'Level' parameter, the output activates or deactivates depending on how the 'Sel' parameter is configured.

Notice that the Level Select parameters do not have units. The drive assumes the units and the minimum/maximum values from the selected parameter function. For example, if the 'Level Sel' is programmed for 10:362 [Heatsnk Temp Pct], which indicates operating temperature of the drive power section (heat sink), its units are in percentage of the maximum heat sink temperature with minimum/maximum values of -200/+200 percent.

For the PowerFlex 750-Series drives utilizing an Option Module, the table below shows an overview of the selectable configurations for the drive's Digital Output 'Level Sel' parameters.

| Parameter No. Parameter Name Description   |                                                                                                                               |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|                                            | 0:3 DC Bus Volts DC bus voltage.                                                                                              |
| nn:50 (1)  Anlg In0 Value                  | Value of the Analog input after filter, square root, and loss action.                                                         |
| nn:60 (1)  Anlg In1 Value                  | Value of the Analog input after filter, square root, and loss action.                                                         |
| 9:1120…9:1127 (2)  DLX Real Out SP1 - SP8  | Eight 32-bit Real scratchpad registers for DLX program output use.                                                            |
| 10:1 Output Frequency                      | Output frequency present at terminals T1, T2, and T3 (U, V & W).                                                              |
|                                            | 10:2 Output Voltage Output voltage present at terminals T1, T2, and T3 (U, V & W).                                            |
| 10:3 Output Current                        | The total output current present at terminals T1, T2, and T3 (U, V & W).                                                      |
|                                            | 10:4 Output Power Output power present at terminals T1, T2, and T3 (U, V & W).                                                |
|                                            | 10:5 Output Pwr Factr Output power factor.                                                                                    |
| 10:8 Torque Cur Fb                         | Based on the motor, the amount of current that is in phase with the fundamental voltage component.                            |
| 10:9 Flux Cur Fb                           | Amount of current that is out of phase with the fundamental voltage component.                                                |
|                                            | 10:207 Mtr OL Counts Accumulated percentage of motor overload.                                                                |
|                                            | 10:208 Mtr OL Trip Time Displays the inverse of the motor overload time.                                                      |
|                                            | 10:357 Drive OL Count Indicates power unit overload (IT) in percentage.                                                       |
| 10:362 Heatsnk Temp Pct                    | Indicates operating temperature of the drive inverter section (heat sink) in percentage of the maximum heat sink temperature. |
|                                            | 10:1044 Motor Vel Fb Estimated or actual motor speed, with feedback.                                                          |
| 10:1834 Enc VRef                           | Displays the filtered velocity reference from the Encoder Velocity Reference function.                                        |
|                                            | 10:1914 VRef Commanded Value of the active Speed/Frequency Reference.                                                         |

|            | Parameter No. Parameter Name Description   |                                                                                                                                                                                                                                         |
|------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | 10:2036 LdObs Torque Est                   | Displays the load observer torque estimate signal. This value includes load disturbances relative to an ideal unloaded motor.                                                                                                           |
|            | 10:2057 FrctnComp Out                      | Displays the torque reference output of the Friction Compensation function.                                                                                                                                                             |
|            | 10:2073 Trq Commanded                      | Final torque reference value after limits and filtering are applied. Percent of motor rated                                                                                                                                             |
| 13:2 (3)   | AC Line Voltage                            | Displays total 3-phase average AC voltage. Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                                                                                                     |
| 13:3 (3)   | R-S Line Volts                             | Displays the measured line-to-line voltage between phase R (L1) and phase S (L2). Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                                                              |
| 13:4 (3)   | S-T Line Volts                             | Displays the measured line-to-line voltage between phase S (L2) and phase T (L3). Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                                                              |
| 13:5 (3)   | T-R Line Volts                             | Displays the measured line-to-line voltage between phase T (L3) and phase R (L1). Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                                                              |
| 13:6 (3)   | AC Line Current                            | Displays the average measured RMS AC phase current. Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                                                                                            |
| 13:7 (3)   | Active Current                             | Displays the active current. The value is negative during regeneration or producing current and positive during motoring or consuming current. Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered. |
| 13:8 (3)   | Reactive Current                           | Displays the measured reactive current. The value is negative for leading power factor and positive for lagging power factor. Parameter 13:23 [Display Filter] determines whether the value is filtered or unfiltered.                  |
| 13:9 (3)   | R Phase Current                            | Displays the R (L1) Input phase current for the entire line side converter in Amperes RMS.                                                                                                                                              |
| 13:10 (3)  | S Phase Current                            | Displays the S (L2) Input phase current for the entire line side converter in Amperes RMS.                                                                                                                                              |
| 13:11 (3)  | T Phase Current                            | Displays the T (L3) Input phase current for the entire line side converter in Amperes RMS.                                                                                                                                              |
| 13:50 (3)  | DC Bus Command                             | Displays the value of the selected and conditioned DC Bus Voltage reference. The DC bus regulator consumes this signal as its command.                                                                                                  |
| 13:65 (3)  | Active Cur Ref                             | Displays the Active Current (Iq) reference for Active Current mode.                                                                                                                                                                     |
| 13:67 (3)  | Active Cur Cmd                             | Displays the limited and conditioned Active Current reference. The Active Current regulator consumes this signal as its command.                                                                                                        |
| 13:228 (3) | R (L1) OL Count                            | Displays the overload count for the R (L1) phase in percentage. It increases when the current is higher than the line side converter rating for present operating conditions.                                                           |
| 13:229 (3) | S (L2) OL Count                            | Displays the overload count for the S (L2) phase in percentage. It increases when the current is higher than the line side converter rating for present operating conditions.                                                           |
| 13:230 (3) | T (L3) OL Count                            | Displays the overload count for the T (L3) phase in percentage. It increases when the current is higher than the line side converter rating for present operating conditions.                                                           |
| 13:234 (3) | Heatsnk Temp Pct                           | Indicates operating temperature of the drive converter section (heat sink) in percentage of the maximum heat sink temperature.                                                                                                          |

(1) Option modules can be used in Ports 4, 5, 6, 7, and 8 of PowerFlex 755 drives.

(2) Port 9: DeviceLogix software parameters

(3) Port 13: Active Front End converter parameters

Depending on the PowerFlex 750-Series Option Module(s) installed in the drive, related Level Select parameter information noted in the following table.

| Parameter No. Parameter Name Description    |                                                                                      |
|---------------------------------------------|--------------------------------------------------------------------------------------|
|                                             | nn:10 RO0 Sel Selects the source that energizes the relay output.                    |
|                                             | nn:11 RO0 Level Sel Selects the source of the level that is compared.                |
|                                             | nn:12 RO0 Level Sets the level compare value.                                        |
| nn:13 RO0 Level CmpSts                      | Status of the level compare, and a possible source for a relay or transistor output. |
| nn:20 RO1 Sel or TO0 Sel                    | Selects the source that energizes the relay or transistor output.                    |
| nn:21  RO1 Level Sel or TO0 Level Sel       | Selects the source of the level that is compared.                                    |
|                                             | nn:22 RO1 Level or TO0 Level Sets the level compare value.                           |
| nn:23  RO1 Level CmpSts or TO0 Level CmpSts | Status of the level compare, and a possible source for a relay or transistor output. |
|                                             | nn:30 TO1 Sel Selects the source that energizes the transistor output.               |
|                                             | nn:31 TO1 Level Sel Selects the source of the level that is compared.                |
|                                             | nn:32 TO1 Level Sets the level compare value.                                        |

## Example

To configure RO0 on the option module located in port 7 to energize when the drive's operating temperature of the drive power section (heat sink) in percentage of the maximum heat sink temperature is greater than 50 percent, set parameter 7:10 [RO0 Sel] to 7:13 [RO0 Level CmpSts] bit 1 'Grt Than Equ', 7:11 [RO0 Level Sel] to 10:362 [Heatsnk Temp Pct], and 7:12 [RO0 Level] to 50.

## Controlled By Digital Input

A digital output can be programmed to be controlled by a digital input. For example, when the input is closed, the output is energized, and when the input is open, the output is de-energized. Note that the output is controlled by the state of the input, even if the input has been assigned a normal drive function (Start, Jog, and so on).

## Example

To configure RO1 on the option module located in port 7 to energize when digital input 3 on the same module is on, set parameter 7:20 [RO1 Sel] to 7:1 [Dig In Sts] bit 3 'Input 3'.

## Controlled by Network

This configuration is used when it is desired to control the digital outputs over network communication instead of a drive related function. In the case the PowerFlex 750-Series Option Module, nn:7 [Dig Out Setpoint] is utilized. To complete the configuration for control over a network, a datalink must be configured for the Digital Output Setpoint parameter.

Depending on the PowerFlex 750-Series Option Module(s) installed in the drive, related Dig Out Setpoint information is noted in the following table.

| Bit No. Description                                                                  |
|--------------------------------------------------------------------------------------|
| 0 Relay Out0                                                                         |
| 1 Relay Out1 (20-750-2262C-2R and 20-750-2262D-2R) or Trans Out0 (20-750-2263C-1R2T) |
| 2 Trans Out1 (20-750-2263C-1R2T)                                                     |
| 3…15 Reserved                                                                        |

## Example

To configure RO1 on the option module located in port 7 to be controller over the network, first set parameter 7:20 [RO1 Sel] to 7:7 [Dig Out Setpoint]. Next, set one of the unused output datalinks 0:321 [DL From Net 1] thru 0:336 [DL From Net 16] to 7:7 [Dig Out Setpoint]. Finally

write logic in the controller to control bit 1 of the configured datalink. If using Studio 5000 and the Drives Add-On Profiles (AOPs) we can use the created descriptive controller tag 'drivename:O.P7\_DigOutSetpoint.1'. The physical output state will match the state of bit 1 in the datalink unless the output has been inverted in which case it will be the opposite state.

## Controlled by DeviceLogix software

DeviceLogix software control technology provides you with the flexibility to customize a drive to more closely match your application needs. DeviceLogix software controls outputs and manages status information locally within the drive allowing you to operate the drive independently or complimentary to supervisory control helping to improve system performance and productivity. You can use the PowerFlex 750-Series DeviceLogix software to read inputs/write outputs and exclusively control the drive.

To turn on physical outputs using DeviceLogix (DLX), you utilize the 32 bit Boolean scratchpad memory locations 9:1100 [DLX Bool SP1] thru 9:1103 [DLX Bool SP4]. These are User Selectable tags that can be added to the DLX database via the DLX Tag Editor.

## Example

The DeviceLogix program has been written to turn on 9:1102 [DLX Bool SP3], bit 7 when a conveyor photoeye is blocked for more than 5 seconds. We need to turn on a stack light wired to RO0 on the option module installed in port 5, to indicate to the operator that there is a backup on the conveyor. To accomplish this, set 5:10 [RO0 Sel] to 9:1102 [DLX Bool SP3], bit 7.

## Invert

There is a logical invert function associated with the PowerFlex 750-Series drive's digital outputs. It is configured by nn:6 [Dig Out Invert]. This invert function changes the output status bit from a zero, false state, to a one, true state, and vice versa.

This logical invert function requires power to be applied to the drive's control module for the drive's logic to be active. This can be obtained from powering up the drive's control module by either applying power to the drive's input section or from an external 24V DC being wired into the Auxiliary Power Supply Option Module.

Depending on the PowerFlex 750-Series Option Module(s) installed, Invert parameter information noted in the following table.

0 = Output Not Inverted, 1 = Output Inverted

| Bit No. Description                                                                  |
|--------------------------------------------------------------------------------------|
| 0 Relay Out0                                                                         |
| 1 Relay Out1 (20-750-2262C-2R and 20-750-2262D-2R) or Trans Out0 (20-750-2263C-1R2T) |
| 2 Trans Out1 (20-750-2263C-1R2T)                                                     |
| 3…15 Reserved                                                                        |

## Example

In this example, we want to configure RO0 on the option module located in port 7 to energize when digital input 1 on the same option module is open or de-energized. To accomplish this, first set 7:10 [RO0 Sel] to 7:1 [Dig In Sts], bit 1 'Input 1'. This sets RO0 to reflect the same state as Input 1. To get the output to reflect the opposite state, we have to invert the output by setting 7:6 [Dig Out Invert], bit 0 'Relay Out 0' to 1.

## On/Off Time

Each digital output has two user-controlled timers associated with it. The On timer defines the delay time between a False-to-True transition (condition appears) on the output condition and the corresponding change in state of the digital output. The Off timer defines the delay time between a True-to-False transition (condition disappears) on the output condition and the

corresponding change in the state of the digital output. Either timer can be disabled by setting the corresponding delay time to zero.

Depending on the PowerFlex 750-Series Option Module(s) installed, On/Off parameters noted in the following table.

| Parameter No. Parameter Name Description   |                                                                                                                                                     |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| nn:14 RO0 On Time                          | Sets the ‘ON Delay’ time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay.               |
| nn:15 RO0 Off Time                         | Sets the ‘OFF Delay’ time for the digital outputs. This is the time between the disappearance of a condition and de activation of the relay.                                                                                                                                                     |
| nn:24  RO1 On Time or TO0 On Time          | Sets the ‘ON Delay’ time for the digital outputs. This is the time between the occurrence of a condition and activation of the relay or transistor. |
| nn:25  RO1 Off Time or TO0 Off Time        | Sets the ‘OFF Delay’ time for the digital outputs. This is the time between the disappearance of a condition and de activation of the relay or transistor.                                                                                                                                                     |
| nn:34 TO1 On Time                          | Sets the ‘ON Delay’ time for the digital outputs. This is the time between the occurrence of a condition and activation of the transistor.          |
| nn:35 TO1 Off Time                         | Sets the ‘OFF Delay’ time for the digital outputs. This is the time between the disappearance of a condition and de activation of the transistor.                                                                                                                                                     |

Whether a particular type of transition (False-to-True or True-to-False) on an output condition results in an energized or de-energized output depends on the output condition. If a transition on an output condition occurs and starts a timer, and the output condition goes back to its original state before the timer runs out, then the timer is aborted and the corresponding digital output does not change state.

## Example

For example, in the following diagram, a digital output is configured for 10:354 [Motor Side Sts 1], bit 27 'Cur Limit', the On Time is programmed for two seconds and the Off Time is programmed for 0 seconds.

<!-- image -->

## Status

The nn:5 [Dig Out Sts] parameter displays the status of the digital outputs and can be used for troubleshooting the digital outputs. When the bit in associated with the digital output is on, this means that the logic in the drive is telling that digital output to turn on. When the bit associated with the digital input is off, this means that the logic in the drive is telling that digital output to turn off.

| Bit No. Description                                                                  |
|--------------------------------------------------------------------------------------|
| 0 Relay Out0                                                                         |
| 1 Relay Out1 (20-750-2262C-2R and 20-750-2262D-2R) or Trans Out0 (20-750-2263C-1R2T) |
| 2 Trans Out1 (20-750-2263C-1R2T)                                                     |
| 3…15 Reserved                                                                        |

## PTC Motor Thermistor Input

## Block Diagrams

Figure 73 - PowerFlex 750-Series Option Module Outputs

Outputs

Figure 74 - PowerFlex 750-Series Option Module Outputs Compare

<!-- image -->

Output Compare

<!-- image -->

A PTC (Positive Temperature Coefficient) sensing device, also known as a motor thermistor, embedded in the motor windings can be monitored by the drive for motor thermal protection. The motor windings are typically equipped with three PTC sensors (one per phase) wired in series as shown in schematic below. The miniaturized sensors have a low resistance below the rated response temperature, and increase their resistance (exponentially) in the rated response temperatures range. The rated response temperature is defined by the PTC sensor. Motors with different thermal insulation classes (Class F or H) are equipped with different PTC sensors, each with its own response temperature such as 120, 130, and 140 degrees C. Unlike the PT100 or KTY thermistors, which have a linear relation between temperature and resistance, the PTC thermistor is used for a temperature level indication rather than a direct measurement in degrees C.

Figure 75 - PTC Characteristic Temperature/Resistance Curve According to IEC-34-11-2

<!-- image -->

## Hardware and Connection

The PTC thermistor leads are connected to the PTC+ and PTC- terminals on TB1 of one of the optional I/O cards, catalog numbers 20-750-2262C-2R, 20-750-2263C-1R2T, 20-750-2262D-2R.

PTC thermistors of ATEX certified motors connect to the ATEX option module, 20-750-ATEX, which is mounted onto one of the 11-Series I/O cards, catalog numbers 20-750-1132C-2R, 20750-1133C-1R2T, 20-750-1132D-2R

Figure 76 - PTC Connection

<!-- image -->

## Configuration with Optional I/O Board

Parameter nn:40 [PTC Cfg] = 0 'Ignore', 1 'Alarm', 2 'Flt Minor', 3 'Flt CoastStop', 4 'Flt RampStop', or 5 'Flt CL Stop'

Status is shown in nn:41 [PTC Sts] and nn:42 [PTC Raw Value].

## Configuration with 11-Series I/O module fitted with ATEX Option

Status is shown in nn:41 [ATEX Sts] The fault action is not configurable when the ATEX module is used.

## Fault or Alarm Operation

The reaction to an increased PTC resistance depends on the respective PTC configuration, such as alarm or fault. When the ATEX module is used, the result is always fault. When the PTC resistance exceeds 3.2 kOhm a fault or alarm is triggered. The function is reset when the resistance drops below 2.2 kOhm. A short circuit is detected when the resistance value drops below 100 Ohm. If the drive was configured to fault then the fault must be cleared once the PTC function is reset (value is below threshold).

## Notes:

## Numerics

24V DC power source 38

## A

## AC line source

bus regulators 126

configuration 125

external bus capacitance 125

parameter data 125

phase loss 147

switching 129

tuning 124

AC motor types 44

accel/decel time

configure 7

adaptive tuning 52

alarms 146

analog inputs 191

analog outputs 198

anti-sway 166

automatic device configuration

activation 10

compatibility 9

autotune 52

motor side inverter 164

## B

## braking methods 18

coast 19

current limit stop 20

DC brake 23

decel to hold 22

fast brake 24

flux braking 25

ramp 19

ramp to hold 22

bus control 183

bus observer 53

block diagram 54

limitations 53

bus regulation 53

bus supplies 121

derating 124

operation modes 122

## C

calculate sway frequency 168

carrier frequency 189

configuration 30

derating 33

low speed 30

CIP security 59

conditions 28

needed to start 28

control circuitry power 38

## control features

adaptive tuning autotune 52

52

load observer 51

current regulator adjustment 128

## D

## DC bus voltage

bus observer 53

feed forward power 54

derating 33

DeviceLogix 86

digital outputs 218

digital inputs 203

discrete wired 65

functional descriptions 204

digital outputs 213

dynamic braking 174

applications 176

module and resistor 177

PWM control 175

resistance 180

## E

energy saving 63

explicit messaging, predictive maintenance

84

## F

## faults 143

override 94

queue 144

reset or clear 144

response to 143

feed forward power 54

parameters 55

feedback modes

50

## G

## generators

configuration 132 considerations 130 drive features 131 exception actions and limits external capacitance 132 selection 130 tuning 133

## H

high frequency variation 35

high speed trending 137

configuration 137

134

## I

induction motors 44

## inputs

analog digital

191

203

interactive functions 17

## L

## limits

converter 120

regeneration power 134

load observer 51

loss of synchronization 34

low speed operation 30

configuration

30

derating 33

## M

## motion planners

position 98

## motor control

configuration 60 Logix configuration 60 secondary motor control 60 switching between profiles use cases 60

volts/hertz 39

## motors

interior permanent magnet 48

permanent magnet 47

surface permanent magnet synchronous 47 synchronous reluctance 49

wound rotor 46

## N

## notch filter

configurations notch filters 55 , 166

parameters 56

## O

## object hierarchy 79

operation at low speed 30

## outputs

analog 198

digital 213

## P

## phase loss

active front end drives 148

detection 147

possible actions 35 , 147

## power disturbance module

configure 37

power disturbances 34

module description 34

48

169

60

power loss 35

## power loss ride-through

flow diagram 36

## predictive maintenance 67

function details 69

monitoring examples resetting 72

78

setting levels 67

## predictive maintenance CIP objects

CIP messaging example component 81

84

component group 82

environmental conditions 80

preventing start 28

## R

reference notch filters 55

## regulator schemes

diagram 52

regulators

position and velocity 52

## restart

required conditions 16

rotate motor ID test 164

## S

## sleep/wake

parameters sources 17

timers 16

start required conditions 16

static motor ID test 165

## T

timers 16

torque prove function 165

## V

voltage regulator adjustment 127

voltage sag 34 , 35

15

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. To view or download publications, go to rok.auto/literature .

|                                                                                                                                       | Resource Description                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 750-Series Products with TotalFORCE Control Technical Data, publication 750-TD100                                           | Provides detailed information on: • Drive and bus supply specifications • Option specifications • Fuse and circuit breaker ratings                                                                                                                                       |
| PowerFlex 755TM IP00 Open Type Kits Technical Data, publication 750-TD101                                                             | Provides detailed information on: • Kit selection • Kit ratings and specifications • Option specifications                                                                                                                                                               |
| PowerFlex 750-Series Products with TotalFORCE Control Installation Instructions, publication 750-IN100                                | Provides the basic steps to install PowerFlex 755TL low harmonic drives, PowerFlex 755TR regenerative drives, and PowerFlex 755TM drive systems.                                                                                                                         |
| PowerFlex 755TM IP00 Open Type Kits Installation Instructions, publication 750-IN101                                                  | Provides instructions to install IP00 Open Type kits in user-supplied enclosures.                                                                                                                                                                                        |
| PowerFlex Drives with TotalFORCE Control Programming Manual (firmware revision 6.xxx and earlier), publication 750-PM100              | Provides detailed information on: • I/O, control, and feedback options • Parameters and programming • Faults, alarms, and troubleshooting                                                                                                                                |
| PowerFlex TotalFORCE Firmware Documentation Set: • PowerFlex Drives with TotalFORCE Control Programming Manual, publication 750-PM101 | Provides detailed information on: • Startup, control algorithms, and status indicators                                                                                                                                                                                   |
| • PowerFlex Drives with TotalFORCE Control Parameters Reference Data, publication 750-RD101                                           | • Parameters and programming                                                                                                                                                                                                                                             |
| • PowerFlex Drives with TotalFORCE Control Conditions Reference Data, publication 750-RD102                                           | • Faults, alarms, events, and troubleshooting                                                                                                                                                                                                                            |
| Drives in Common Bus Configurations with PowerFlex 755TM Bus Supplies Application Techniques, publication DRIVES-AT005                | Provides basic information to properly wire and ground the following products in common bus applications: • PowerFlex 755TM drive system for common bus solutions • PowerFlex 750-Series AC and DC input drives • Kinetix 5700 servo drives                              |
| PowerFlex 755T Flux Vector Tuning, publication 750-AT006                                                                              | Provides guidance on how to tune Flux Vector position and velocity loops, filters, and other features to achieve the level of performance that is required for a given application. This publication is intended for novice drives users and users with advanced skills. |
| PowerFlex Drives with TotalFORCE Control Built-in EtherNet/IP Adapter User Manual, publication 750COM-UM009                           | Provides information on how to install, configure, and troubleshoot applications for the PowerFlex drives with the built-in EtherNet/IP adapter.                                                                                                                         |
| PowerFlex 750-Series Products with TotalFORCE Control Hardware Service Manual, publication 750-TG100                                  | Provides detailed information on: • Preventive maintenance • Component testing • Hardware replacement procedures                                                                                                                                                         |
| PowerFlex 750-Series Safe Speed Monitor Option Module Safety Reference Manual, publication 750-RM001                                  | These publications provide detailed information on installation, set-up, and operation of the 750-Series safety option modules.                                                                                                                                          |
| PowerFlex 750-Series Safe Torque Off Option Module User Manual, publication 750-UM002                                                 |                                                                                                                                                                                                                                                                          |
| PowerFlex 750-Series ATEX Option Module User Manual, publication 750-UM003                                                            |                                                                                                                                                                                                                                                                          |
| PowerFlex 755 Integrated Safety - Safe Torque Off Option Module User Manual, publication 750-UM004                                    |                                                                                                                                                                                                                                                                          |
| PowerFlex 20-HIM-A6 and 20-HIM-C6S HIM (Human Interface Module) User Manual, 20HIM-UM001                                              | Provides detailed information on HIM components, operation, and features.                                                                                                                                                                                                |
| PowerFlex 750-Series Service Cart Instructions, publication 750-IN105                                                                 | Provides detailed set-up and operating instructions for the module service cart and DC precharge module lift.                                                                                                                                                            |
| 750-IN106                                                                                                                             | accessory.                                                                                                                                                                                                                                                               |
| PowerFlex 755T Module Service Ramp Instructions, publication 750-IN108                                                                | Provides detailed usage instructions for the module service ramp.                                                                                                                                                                                                        |
| Industry Installation Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-AT003                                  | Provides basic information on enclosure systems, considerations to help protect against environmental contaminants, and power and grounding considerations for installing Pulse Width Modulated (PWM) AC drives.                                                         |
| Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001                                   | Provides basic information to properly wire and ground PWM AC drives.                                                                                                                                                                                                    |
| Product Certifications website, rok.auto/certifications                                                                               |                                                                                                                                                                                                                                                                          |
| Rockwell Automation Knowledge Base                                                                                                    |                                                                                                                                                                                                                                                                          |
|                                                                                                                                       | The Rockwell Automation Support Forum.                                                                                                                                                                                                                                   |

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

Allen-Bradley, Connected Components Workbench, DeviceLogix, expanding human possibility, FactoryTalk, PowerFlex, Rockwell Automation, RSLogix 5000, Stratix, Studio 5000 Logix Designer, TorqProve, and TotalFORCE are trademarks of Rockwell Automation, Inc.

EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expanding human possibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIA PACIFIC:Rockwell Automation SEA Pte Ltd, 2 Corporation Road, #04-05, Main Lobby,Corporation Place,Singapore 618494,Tel:(65)6510 6608